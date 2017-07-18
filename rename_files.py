#!/usr/bin/env python3

# Discription: A Python script for rename files base on your demands
# Author : J.S


import os
import re

DIRECTORY = ''
FILES = []
NEWFILES = []
REPLACEMENT = {}

# get the work directory
DIRECTORY = input("Please input the ABS directory(default is .):")
if DIRECTORY is not '':
	try:
		os.chdir(DIRECTORY)
	except FileNotFoundError:
		print("Path does not exist! Please try again.")
		quit()

DIRECTORY = os.getcwd()

# show the files, so you can copy the patterns
print('Here are the files under the folder(not start with \".\"):')
for item in os.listdir(DIRECTORY):
	if not re.search('^\.', item):
		if re.search('\..*$', item):
			FILES.append(item)
			print(item)

# process the input string, show which files are affacted
old_str = input('Input the patterns you want to replace(support RE, separate by ,):')
new_str = input('Input the new strings(separate by ",", use space as None):')
REPLACEMENT = {}
for old, new in zip(old_str.split(','), new_str.split(',')):
	if new is ' ':
		new = ''
	REPLACEMENT[old] = new

# for item in REPLACEMENT.items():
# 	print('"' + item[0] + '"\t\t---> ', end='')
# 	if item[1] is '':
# 		print('delete')
# 	else:
# 		print('"' + item[1] + '"')

print("Here are the affected files:")
for file in FILES:
	newfile = file
	for item in REPLACEMENT.items():
		newfile = re.sub(item[0], item[1], newfile)
	if newfile != file:
		print('{0:30}\t---> {1}'.format(file, newfile))
	NEWFILES.append(newfile)


# comfirm to rename
yon = input("Sure to rename the files?(y/n):")
if yon is "y":
	for old, new in zip(FILES, NEWFILES):
		os.rename(old, new)
else:
	quit()







