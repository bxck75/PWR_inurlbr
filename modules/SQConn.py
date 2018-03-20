#!/usr/bin/env python

import re, sys, time, math
import urllib2
import urlparse
import optparse
from cgi import escape
from traceback import format_exc
from Queue import Queue, Empty as QueueEmpty
from BeautifulSoup import BeautifulSoup
import itertools
import sqlite3
from sqlite3 import OperationalError

__version__ = '0.01'
__copyright__ = 'Copyright 2018'
__license__ = 'MIT'
__author__ = 'Boudewijn Kooij'

USAGE = "%prog [options] <url>"
VERSION = "%prog v" + __version__
# pretend to be IE9
# set agent and size
AGENT = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'
MAX_CONTENT_SIZE = 1024 * 1024
""" create a database connection to a SQLite database """
DBConn = sqlite3.connect('/usr/local/bin/GlobalDorkDB.sqlite3')
cursor = DBConn.cursor()

#setup shop
fd = open('/usr/local/bin/GlobalDorkDB.sql', 'r')
sqlFile = fd.read()
fd.close()
sqlCommands = sqlFile.split(';')

for command in sqlCommands:
    # This will skip and report errors
    # For example, if the tables do not yet exist, this will skip over
    # the DROP TABLE commands
    try:
        cursor.execute(command)
    except OperationalError, msg:
        print "Command skipped: ", msg

#DBConn.execute("INSERT INTO `ShodanResults`(`ip`,`ports`,`url`,`shodansearch`,`exploit_type`,`geolookup`) VALUES (NULL,NULL,NULL,NULL,NULL,NULL);")

query = "SELECT * from `ShodanResults`;"
result = list(DBConn.execute(query))

Ip,Port = result[0][1],result[0][2]

print Ip+':'+Port
#run_id = list(DBConn.execute(query))
DBConn.commit()
cursor.close()
DBConn.close()


