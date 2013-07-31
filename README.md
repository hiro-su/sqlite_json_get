# Create SQLite3 Database
    $ sqlite3 test.db
    SQLite version 3.7.16.1 2013-03-29 13:44:34
    Enter ".help" for instructions
    Enter SQL statements terminated with a ";"
    sqlite> create table test (k, v);
    sqlite> insert into test values(1375277875,'{"key1":1,"key2":"value2"}');
    sqlite> insert into test values(1375277875,'{"key1":1,"key2":"value2"}');
    sqlite> insert into test values(1375277875,'{"key1":1,"key2":"value2"}');
    sqlite> insert into test values(1375277875,'{"a":123.00000}');
    sqlite> .q

# Search
## sample1
    $ ./sqlite_json_get.py -q 'select v(v,"key1") from test' -d test.db
    1
    1
    1
    null

## sample2
    $ ./sqlite_json_get.py -q 'select v(v,"key2") from test' -d test.db
    value2
    value2
    value2
    null

## sample3
    $ ./sqlite_json_get.py -q 'select v(v,"a") from test' -d test.db
    null
    null
    null
    123.0

## sample4
    $ ./sqlite_json_get.py -q 'select * from test' -d test.db
    1375277875,{"key1":1,"key2":"value2"}
    1375277875,{"key1":1,"key2":"value2"}
    1375277875,{"key1":1,"key2":"value2"}
    1375277875,{"a":123.00000}
