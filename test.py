#!/usr/bin/python
from ftplib import FTP
from config import *

ftp = FTP(host=Hostname) #user=Username, passwd=Password
ftp.login(Username, Password) 
#ftp.retrlines('LIST')
#ftp.dir('LIST','myPython')
#ftp.cwd('myPython/')#set the current directory
#ftp.storlines("STOR " + 'test.py', open('test.py', 'r'))#upload the file to the current directory
#ftp.mkd('myPython/test')


#print ftp.getwelcome()
#ftp.quit()

def uploadFile(filePath,fileName):
	ftp.cwd(filePath)
	ftp.storlines("STOR " + fileName, open(fileName, 'r'))#upload the file to the current directory
	print ('The file is uploaded to %s%s' % (filePath,fileName))
    

uploadFile(raw_input("What is the file Path? "),raw_input("What is your file name? "));
ftp.quit()
#https://docs.python.org/2/library/ftplib.html
#http://adampresley.github.io/2013/04/20/how-i-deployed-a-php-app-via-ftp-using-fabric-and-git.html