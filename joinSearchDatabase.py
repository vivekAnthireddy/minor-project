import os
from database import database
from drive import get_drives



location=[]
files=[]
drive_letters=get_drives()
#drive_letters=['G']
for drive in drive_letters:
    for root,dir,file in os.walk('{}:\\'.format(drive),topdown=True):
        for name in file:
            files.append(str(name))
            location.append(str(root))
        if len(files)>10000:
            database(files,location)
            files=[]
            location=[]

database(files,location)