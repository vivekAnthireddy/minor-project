import sqlite3
import progressbar


sql_transaction=[]


def transaction_bldr(db ,conn,sql):
    global sql_transaction
    sql_transaction.append(sql)
    if len(sql_transaction) > 1000:
        db.execute('BEGIN TRANSACTION')
        for s in sql_transaction:
            try:
                db.execute(s)
            except:
                pass
        conn.commit()
        sql_transaction = []

def createTable(db,conn,table_name):
    query='create table if not exists {} ( {}_name text PRIMARY KEY ,location TEXT ,{}_nickname text)'.format(table_name,table_name,table_name)
    db.execute(query)

def insertion(table_name,program_name, location, program_nickname,db,conn):
    try:
        sql = """INSERT INTO {} ( {}_name, location, {}_nickname) VALUES ("{}","{}","{}");""".format(table_name,table_name,table_name,program_name, location, program_nickname)
        transaction_bldr(db,conn,sql)
    except Exception as e:
        print('s0 insertion', str(e))

def check(program_name,db,conn):
    try:
        sql="""select * from programs where program_name='{}'""".format(program_name)
        res=db.execute(sql)
        if len(res.fetchall()) == 0 :
            return True
        else:
            return False
    except Exception as e:
        print('check exe name \n',str(e))



def database(name,location):
    db_name = 'data'
    conn = sqlite3.connect('{}.db'.format(db_name))
    db = conn.cursor()
    tables=['programs','document','videos','music','images','misc']
    for table in tables:
        createTable(db,conn,table)
    bar = progressbar.ProgressBar()
    for i in bar(range(len(name))):
        nickname=name[i].split('.')[0]
        if name[i].endswith('.exe'):
            insertion(tables[0],name[i],location[i],nickname,db,conn)
        elif name[i].endswith('.mp3'):
            insertion(tables[3],name[i],location[i],nickname,db,conn)
        elif name[i].endswith('.mp4'):
            insertion(tables[2],name[i],location[i],nickname,db,conn)
        elif name[i].endswith('.pdf') or name[i].endswith('.ppt') or name[i].endswith('.doc') or name[i].endswith('docx') or name[i].endswith('.txt'):
            insertion(tables[1],name[i],location[i],nickname,db,conn)
        elif name[i].endswith('.jpg') or name[i].endswith('.png') or name[i].endswith('jpeg') or name[i].endswith('gif'):
            insertion(tables[4],name[i],location[i],nickname,db,conn)
        else:
            insertion(tables[5],name[i],location[i],nickname,db,conn)



