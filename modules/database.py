#!/usr/bin/env python
# -*- coding: utf-8 -*-


# make sure it's a new style class
__metaclass__ = type 

import sqlite3 as lite
import sys


class database:

	def __init__(self,dbname='GlobalDorkDB.sqlite3',dbfolder='/usr/local/bin/'):
		self.dbfolder = dbfolder
		self.dbname = dbname
		self.dbPath = self.dbfolder+self.dbname
		print(self.dbPath)
		self.con = None
		self.getConnection(self.dbPath)
		print('init db')

	def getConnection(self, dbPath):
		
		try:
			self.con = lite.connect(dbPath)
			print "connection created"
		except lite.Error, e:

			print "Error %s:" % e.args[0]
			#sys.exit(1)


	def query(self,sql):
		
		rows = []	
		
		try:
			echo "hireerrew"
			#with self.con:	
			cur = self.con.cursor()
			cur.execute(sql)

			# print "the first element in rows will be the column names."
			column_names = [x[0] for x in cur.description]
			rows.append(column_names)

			while True:
				row = cur.fetchone()
			
				if row == None:
					break
				
				rows.append(row)

		except lite.Error, e:

			print "Error %s:" % e.args[0]
			#sys.exit(1)
		
		return rows


def main():
	
	sqlmgr = SqlMgr()
	
	print "the first element in rows will be the column names."	
	rows = sqlmgr.query("select * from buildings")
	cols = rows.pop(0)
	
	print "column names"	
	print cols
	print "data"	
	print rows


if __name__ == "__main__":
	main()