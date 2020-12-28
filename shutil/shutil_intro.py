import shutil
import os

source = './A/'

destination = './B/'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)
