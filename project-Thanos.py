
import os
import glob
import pandas as pd
import shutil    
import glob
import random
path = r"D:\Profile\Downloads\Compressed\Universe"
for x in range(0,25):
    random_filename = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
   ])
    if os.path.exists(path+"\\"+random_filename):
       os.remove(path+"\\"+random_filename)
    else:
       print("The file does not exist")
    print(path+"\\"+random_filename)