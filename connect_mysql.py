#!/usr/bin/python
import MySQLdb

def connectToDB(connection):
  db = MySQLdb.connect(host=connection['host'],    # your host, usually localhost
                     user=connection['user'],         # your username
                     passwd=connection['password'],  # your password
                     db=connection['database'])        # name of the data base
  return db

def closeConnection(db):
  db.close()