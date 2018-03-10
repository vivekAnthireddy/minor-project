import os
from drive import get_drives
import time




def findExe(driveletter):
   count = 0
   time_count=0
   dir_count=0
   time_temp=None
   t = time.time()
   for root, dirs, files in os.walk(driveletter+":\\", topdown=True):
      file_count = float(0)
      file_length = float(len(files))
      dir_count+=1
      for name in files:
         os.system('cls')
         time_count+=1
         file_count += 1
         percent=100*(file_length-file_count)/file_length
         if name.endswith('.exe'):
            count += 1
         if time_count>10:
            time_temp=(float(time.time()-t)*(file_length-file_count)/10)
            t=time.time()
            time_count=0
            print("Inside {} drive \nWorking on {} directory \nRemaining  files {}% \nEstimated time is {}s".format(driveletter,dir_count,percent,time_temp))
         else:
            if time_temp==None:
               time_temp=0
            print("Inside {} drive \nWorking on {} directory \nRemaining  files {}% \nEstimated time is {}s".format(driveletter, dir_count, percent, time_temp))

   os.system('cls')
   return count


drive_letters=get_drives()
count=0
for letter in drive_letters:
   count += findExe(letter)
print('Total number of exe files ', count)
