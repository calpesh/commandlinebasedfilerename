from os import listdir
from os.path import isfile, join
import os
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--a1')
parser.add_argument('--a2')
args = vars(parser.parse_args())

l1 = list(args.values())

onlyfiles = [f for f in listdir(l1[0]) if isfile(join(l1[0], f))]
for filename in onlyfiles:
    if filename.startswith(l1[1]):
        os.rename(join(l1[0], filename), join(l1[0], filename[len(l1[1]):]))

# python .\renamer.py --a1  'D:\BIOINFROMATICS\New folder (6)' --a2 'Manolis Kellis Uploads from Manolis Kellis 0068 '