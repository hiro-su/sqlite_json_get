#!/usr/bin/env python
#coding: UTF-8

import sqlite3
import sys
import optparse
import json

parser = optparse.OptionParser()
parser.add_option('--query', '-q', action="store")
parser.add_option('--db', '-d', action="store")

(options, args) = parser.parse_args()

argvs = sys.argv
database = options.db
sql = options.query.replace("\"", "\'")
conn = sqlite3.connect(database)

def py_json_get(col,val):
    try:
        json_data = json.loads(col)
        return json_data[val]
    except:
        return "null"

conn.create_function("v", 2, py_json_get)

result = conn.execute(sql)

for row in result:
    print ','.join(map(str, row))

conn.close()
