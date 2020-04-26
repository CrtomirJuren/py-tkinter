print('hi from GUI init\n')
from sys import path
from pprint import pprint
#======================================================================
# Required setup for the PYTONPATH in order to find all package folders
#======================================================================
from site import addsitedir
from os import getcwd, chdir, pardir
while True:
	curFull = getcwd()
	curDir = curFull.split('\\')[-1]
	if 'code-cookbook' == curDir:
		addsitedir(curFull)
		addsitedir(curFull + '/Folder1/Folder2/')
		break
	chdir(pardir)
pprint(path)