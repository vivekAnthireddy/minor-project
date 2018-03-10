import sqlite3
import json
from datetime import datetime


def createTable(db):
    query='create table if not exists parent_reply ( parent_id text PRIMARY KEY , comment_id text ,parent TEXT ,comment text,subreddit text, unix int , score int)'
    db.execute(query)

def data_entry(db):
    query='insert into chat values("abcbd" , 56)'
    db.execute(query)
    conn.commit()

def format_data(data):
    data=data.replace("\n"," newlinechar ").replace('\r'," newlinechar ").replace('"',"'")
    return data

def find_parent(pid):
    try:
        query="select comment from parent_reply where comment_id = '{}' limit 1 ".format(pid)
        db.execute(query)
        res=db.fetchone()
        if res != None :
            return res[0]
        else :
            return False
    except Exception as e:
        print("find parent",e)
        return False


def find_score(pid):
    try:
        query = "select score from parent_reply where parent_id = '{}' limit 1 ".format(pid)
        db.execute(query)
        res = db.fetchone()
        if res != None:
            return res[0]
        else:
            return False
    except Exception as e:
        print("find parent", e)
        return False


def acceptable(data):
    if len(data.split(" ")) > 50 or len(data) < 1 :
        return False
    elif len(data) > 1000:
        return False
    elif data=='[deleted]' or data=='[removed]' :
        return False
    else:
        return True

def transaction_bldr(sql):
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



def sql_insert_replace_comment(comment_id,parent_id,parent_data,body,score,subreddit,created_utc):
    try:
        query='update parent_reply set parent_id= ? , comment_id=?, parent=?,comment=?,subreddit=?,unix=?,score=? where parent_id =?;'.format(parent_id,comment_id,parent_data,body,subreddit,int(created_utc),score,parent_id)
        transaction_bldr(query)
    except Exception as e:
        print('replace comment ',e)

def sql_insert_has_parent(comment_id,parent_id,parent_data,body,score,subreddit,created_utc):
    try:
        sql = """INSERT INTO parent_reply (parent_id, comment_id, parent, comment, subreddit, unix, score) VALUES ("{}","{}","{}","{}","{}",{},{});""".format(
            parent_id, comment_id, parent_data, body, subreddit, int(created_utc), score)
        transaction_bldr(sql)
    except Exception as e:
        print('s0 insertion', str(e))


def sql_insert_no_parent(comment_id,parent_id,body,score,subreddit,created_utc):
    try:
        sql = """INSERT INTO parent_reply (parent_id, comment_id, comment, subreddit, unix, score) VALUES ("{}","{}","{}","{}",{},{});""".format(
            parent_id, comment_id, body, subreddit, int(created_utc), score)
        transaction_bldr(sql)
    except Exception as e:
        print('s0 insertion', str(e))


timeframe= '2017-11'
sql_transaction = []

conn=sqlite3.connect('{}.db'.format(timeframe))
db=conn.cursor()
if __name__ == '__main__':
    createTable(db)
    row_count=0
    paired=0
    with open('RC_{}'.format(timeframe) , buffering=1000) as f:
        for row in f:
            #print(row_count)
            row_count+=1
            row=json.loads(row)
            parent_id=row['parent_id']
            body = format_data(row['body'])
            created_utc = row['created_utc']
            score=row['score']
            subreddit = row['subreddit']
            comment_id = row['link_id']
            parent_data=find_parent(parent_id)

            if score == None:
                continue

            if score >= 3 :
                if acceptable(body):
                    existing_score= find_score(parent_id)
                    if existing_score :
                        if score >existing_score:
                            sql_insert_replace_comment(comment_id,parent_id,parent_data,body,score,subreddit,created_utc)

                    else:
                        if parent_data:
                            sql_insert_has_parent(comment_id,parent_id,parent_data,body,score,subreddit,created_utc)
                            paired+=1
                        else:
                            sql_insert_no_parent(comment_id,parent_id,body,score,subreddit,created_utc)
            if row_count % 100000 == 0:
                print('Total Rows Read: {}, Paired Rows: {}, Time: {}'.format(row_count, paired,
                                                                              str(datetime.now())))
#data_entry(db)
