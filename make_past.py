#!/usr/bin/env python
from os import *

if __name__ == "__main__":
	try:
		system("sudo chmod 777 *.*")
	except:
		print('Error execute command.')

	try:
		system("mkdir video")
		system("mkdir audio")
	except:
		print('Error make path')