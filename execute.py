import os
import sqlite3


def displayresult(result):
    for i in range(len(result)):
        print(i+1," : ",result[i][2])

def fileopen(file):
    conn = sqlite3.connect('data.db')
    db = conn.cursor()
    sql="""select * from programs where programs_nickname like "%{}%" """.format(file)
    #print(sql)
    res=db.execute(sql)
    result=res.fetchall()
    #print(len(result))
    if len(result) == 0:
        print("Nothing like that exists")
        return
    if len(result)>1:
        displayresult(result)
        index=int(input("Which {}".format(file)))
        file_name=result[index-1][0]
        location=result[index-1][1]
        path=str(location)+"\\"+str(file_name)
        print(path)
        os.system(path)
    else:
        file_name = result[0][0]
        location = result[0][1]
        path = str(location) + "/" + str(file_name)
        os.system(path)


if __name__ == '__main__':
    temp = input("Enter file name :")
    fileopen(temp)

