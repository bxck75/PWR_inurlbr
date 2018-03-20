#!/usr/bin/env python

from modules import CliArgsUitPoeper as PA
from modules import database as DB


conn = DB()
ParseArr = PA()
print(ParseArr)
sql='INSERT INTO `ShodanResults`(`ip`,`ports`,`url`,`shodansearch`,`exploit_type`,`geolookup`) VALUES (NULL,NULL,NULL,NULL,NULL,NULL);'
conn.query(sql);	


#     def __init__(self):
#         self.files = []
#         self.CliArgs = parse_options()
#         print(self.CliArgs[:])

#     def __enter__(self):
#         return self

# 	def foreach(function, iterable):
# 		for element in iterable:
# 			function(element)

#     def UriAna():
#     	print(self)

#     def __exit__(self, exc_type, exc_value, traceback):
#         for file in self.files:
#             os.unlink(file)

