#! Python3

"""Counts the number of source lines of code in programs

Usage:
	line.py (c|c#|python) PATH
	line.py -h | --help
	line.py --version

Arguments:
  	c 			c-code
  	c# 			c-sharp code
  	python 			python code
  	PATH 			code path

Options:
	-h --help 		show this help message
	--version 		show version
"""

import os
import sys
import time
from docopt import docopt

fileFilters = []

def countFileLine(fname):
	count = 0
	for file_line in open(fname, 'rb').readlines():
		if file_line.replace(b' ', b'') != b'\r\n':
			count += 1
	return count

def walkDir():
	tLines = 0
	cDirName = os.getcwd()
	print('Local:' + cDirName + ':')

	for folder, subFolders, fileNames in os.walk(cDirName):
		if len(fileNames) == 0:
			continue
		
		dLines = 0
		print('The Current folder is ' + folder)
		outAligh = len(max(fileNames, key = len))
		outAligh+= 1
		
		for fileName in fileNames:
			fLines = 0
			if fileName.split('.')[-1] in fileFilters:
				print(fileName.ljust(outAligh), end = '')
				fLines = countFileLine(os.path.join(folder, fileName))
				print('%d' % fLines)
			dLines += fLines
		
		print('Lines in Folder: %d\n' % dLines)
		tLines += dLines
	return tLines


if __name__ == '__main__':
	arguments = docopt(__doc__, version='1.0.0.0')
	
	if arguments['c']:
		fileFilters = ['c', 'h']
	elif arguments['c#']:
		fileFilters = ['cs']
	elif arguments['python']:
		fileFilters = ['py']

	
	startTime = time.clock()
		
	try:
		os.chdir(arguments['PATH'])
		print('Total lines: %d\n' % walkDir())
	except Exception as err:
		print('An exception happened: ' + str(err))
	
	print('Done! Cost Time: %0.2f second' % (time.clock() - startTime))
