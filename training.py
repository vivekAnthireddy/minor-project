import sqlite3
import pandas as pd

timeframe='2017-11'
conn=sqlite3.connect('{}.db'.format(timeframe))
db=conn.cursor()
limit=5000
last_unix=0
cur_length=limit
count=0
test=False

while cur_length==limit:
    df=pd.read_sql("select * from parent_reply WHERE  unix > {} and parent not null and score > 0 order by unix ASC  limit {}".format(last_unix,limit),conn)
    print(len(df))
    last_unix=df.tail(1)['unix'].values[0]
    cur_length=len(df)
    if not test:
        with open("test.from",'a',encoding='utf8') as f:
            for content in df['parent'].values:
                f.write(content+'\n')
        with open("test.to",'a',encoding='utf8') as f:
            for content in df['comment'].values:
                f.write(content+'\n')
        test=True
    else:
        with open("train.from",'a',encoding='utf8') as f:
            for content in df['parent'].values:
                f.write(content+'\n')
        with open("train.to",'a',encoding='utf8') as f:
            for content in df['comment'].values:
                f.write(content+'\n')
    count+=1
    print(count)
    if count %20 ==0 :
        print(count*limit,'rows completed so far')