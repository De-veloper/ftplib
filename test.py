#!/usr/bin/python
from ftplib import FTP
from config import *

ftp = FTP(host=Hostname, user=Username, passwd=Password)
ftp.retrlines('LIST')

#https://docs.python.org/2/library/ftplib.html
#http://adampresley.github.io/2013/04/20/how-i-deployed-a-php-app-via-ftp-using-fabric-and-git.html