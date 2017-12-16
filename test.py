#!/usr/bin/python
from ftplib import FTP
from config import *

ftp = FTP(host=Hostname, user=Username, passwd=Password)
ftp.retrlines('LIST')