from pprint import pprint

import odbcinst

pprint(odbcinst.j())
"""console output:
{'DRIVERS': '/etc/odbcinst.ini',
 'FILE DATA SOURCES': '/etc/ODBCDataSources',
 'SQLLEN Size': '8',
 'SQLSETPOSIROW Size': '8',
 'SQLULEN Size': '8',
 'SYSTEM DATA SOURCES': '/etc/odbc.ini',
 'USER DATA SOURCES': '/home/gord/.odbc.ini',
 'unixODBC': '2.3.4'}
"""

print(repr(odbcinst.j("unixODBC")))
# '2.3.4'
