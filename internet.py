import os

def check():
    filename="test"
    os.system(""" ping google.com > {}.txt""".format(filename))
    with open('test.txt','r') as f:
        if len(f.readlines())>1:
            temp=True
        else:
            temp=False
    os.system(""" del {}.txt""".format(filename))
    return temp



if __name__ == '__main__':
    print(check())
