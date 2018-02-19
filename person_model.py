from config import *
from connect_mysql import *

class Persons:

  db = connectToDB(getConnectionConfig())
  cur = db.cursor()

  TABLENAME = 'Persons'
  SELECT_SQL_BY_ID = 'select * from %(tableName)s where PersonID = %(personID)d'
  SELECT_SQL_ALL = 'select * from %(tableName)s'
  INSERT_ROW = '''insert into %(tableName)s 
  (FirstName,LastName,Address,City) values 
  ('%(firstname)s', '%(lastname)s', '%(address)s', '%(city)s' )'''
  UPDATE_ROW = 'update %(tableName)s set %(columnToValue)s where PersonID = %(personID)d'
  DELETE_ROW = 'delete from %(tableName)s where PersonID = %(personID)d '
  MAX_COLUMN = 'select max(%(column_name)s) from %(tableName)s'
  
  def maxColumn(self, columnName):
    self.cur.execute(self.MAX_COLUMN %{'column_name': columnName, 'tableName': self.TABLENAME})
    max_col_value =  self.cur.fetchall() #tuple of tuples
    return max_col_value [0][0]


  def getRowById(self,id):
    self.cur.execute(self.SELECT_SQL_BY_ID %{'personID':id, 'tableName' : self.TABLENAME})
    rows  = self.cur.fetchall() #this command retches results from function, dont call it again as it will have nothing to fetch, call on rows which now contain the reuslts
    #print type(rows) #tuple
    #print len(rows)
    if (len(rows) == 0): 
      print "This person does not exist in the database!"
      return False
    else:
      for row in rows:
        #print row[0], row[1], row[2] 
        print "This person exists in the database!"
        print "This person's details are: " + str(row) 
        return True
       
    

  def getAllRows(self):
    self.cur.execute(self.SELECT_SQL_ALL %{'tableName' : TABLENAME})
    for row in cur.fetchall():
      print row[0], row[1], row[2]

  def insertRow(self, row):
    self.cur.execute(self.INSERT_ROW %{
      'tableName' : self.TABLENAME,
      'firstname':row['firstname'],
      'lastname':row['lastname'],
      'address':row['address'],
      'city':row['city']
      })
    self.db.commit()

  def getDictToString(self, sep, dict):
    columnToValue= []
    for key,value in dict.items():
      i = '''%s = '%s' '''%(key,value)
      columnToValue.append(i)  
    return sep.join(columnToValue)

  def updateRow(self, id, updatedValueDic):
     
    self.cur.execute(self.UPDATE_ROW %{'tableName': self.TABLENAME, 'columnToValue':self.getDictToString(',',updatedValueDic) , 'personID': id }) 
    self.db.commit()  

  def deleteRow(self, id):
    cur.execute (DELETE_ROW %{'tableName' : TABLENAME, 'personID': id})
    db.commit()
