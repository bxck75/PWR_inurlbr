#!/usr/bin/env python
import argparse,os,sys
import optparse
import json

__version__ = '0.1'
USAGE = "%prog [options] <url>"
VERSION = "%prog v" + __version__

class CliArgsUitPoeper:

	def __init__(self):
		#self.ParseArr = parse_options()
		self.ParseOpts = [	['-q', '--query','store','sql_query','Query the SQLite3 DB'],
							['-i', '--insert','store','sql_insert','insert a record SQLite'],
							['-u', '--update','store','sql_update','update a record (SQLite)'],
							['-x', '--execute','store','sql_execute','Execute a command (SQLite)'],
							['-l', '--limit','store','sql_limit','limit nr of output records (SQLite)']]


		self.parse_options()
		#list of list of args to parse
		
	def parse_options(self):

		parser = optparse.OptionParser(usage=USAGE, version=VERSION)

		for P_Arg in self.ParseOpts:
			parser.add_option(P_Arg[0],P_Arg[1], action=P_Arg[2], dest=P_Arg[3], help=P_Arg[4])
		
		parser.add_option('-v', '--verbose', action='store_false', default=True, help='Display each URL as it is processed')




		# parser.add_option('-l', '--limit', action='store', type='str', dest='limit_sql', help='Maximum depth to traverse')
		# parser.add_option('-q', '--query', action='store', type='str', dest='query_sql', help='Maximum depth to traverse')
		# parser.add_option('-i', '--insert', action='store', type='str', dest='insert_sql', help='Maximum depth to traverse')
		# parser.add_option('-u', '--update', action='store', type='str', dest='update_sql', help='Maximum depth to traverse')
		# parser.add_option('-x', '--execute', action='store', type='str', dest='execute_sql', help='Maximum depth to traverse')
		

		# parser.add_option('--host', action='append', default=[], help='Additional host domain(s) to crawl')
		# parser.add_option('--url-timeout', action='store', default=5, help='Maximum time in seconds to wait for a URL response')
		# parser.add_option('--max-urls', action='store', type='int', default=0, help='Maximum URLs to fetch')
		# parser.add_option('--max-bytes', action='store', type='int', default=0, help='Maximum bytes to download')
		# parser.add_option('--max-time', action='store', default=0, help='Maximum time in seconds to wait for a URL response')

		opts, args = parser.parse_args()
		print opts
		if len(args) < 1:
			parser.print_help()
			raise SystemExit, 1

		return opts, args

