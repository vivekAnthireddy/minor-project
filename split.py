import os

temp='RC_2017-11_db'
temp2='RC_2017-11'
try:
    os.makedirs(temp)
except:
    pass

row=0
count=1
x=open('{}/{}-{}'.format(temp,temp,count),'w')

with open('{}'.format(temp2),buffering=1000) as f:
    for line in f:
        if row >1000000:
            print(count)
            count+=1
            x = open('{}/{}-{}'.format(temp, temp, count), 'w')
            row=0
        x.write(line)
        row+=1

