#this python code is used to move the images which are there in the csv from one folder to another



import pandas as pd
import shutil

src_dir = '/Users/shambhavikrishna/Desktop/Source'
dest_dir = '/Users/shambhavikrishna/Desktop/Destination'

df = pd.read_csv('IDRiD.csv')
l = df.Image.tolist()
#print(l)
for f in l:
    # print(f, type(f))
   
#shutil.copy(sourcePath, destinationPath)
    ex_file = src_dir+'/'+f+'.jpg'
    #print(ex_file)
    shutil.copy(ex_file, dest_dir)
