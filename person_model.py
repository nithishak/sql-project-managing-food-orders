from config import *
from connect_mysql import *

class Persons:

  db = connectToDB(getConnectionConfig())
  cur = db.cursor()

  TABLENAME = 'Persons'
  SELECT_SQL_BY_ID = 'SELECT * FROM %(tableName)s WHERE PersonID = %(personID)d'
  SELECT_SQL_ALL = 'SELECT * FROM %(tableName)s'
  INSERT_ROW = '''INSERT INTO %(tableName)s 
                  (FirstName,LastName,Address,City) VALUES
                  ('%(firstname)s', '%(lastname)s', '%(address)s', '%(city)s' )'''
  UPDATE_ROW = 'UPDATE %(tableName)s SET %(column_data_info)s WHERE PersonID = %(personID)d' #column_data_info can be 'column_name = 2' eg.
  DELETE_ROW = 'DELETE FROM %(tableName)s WHERE PersonID = %(personID)d '
  MAX_COLUMN = 'SELECT MAX (%(column_name)s) FROM %(tableName)s'
  

  def getRowById(self,id):
    self.cur.execute(self.SELECT_SQL_BY_ID %{'personID':id, 'tableName' : self.TABLENAME})
    rows  = self.cur.fetchall() #this command fetches results from function, dont call it again as it will have nothing to fetch, call on rows which now contain the reuslts
    #rows is a tuple of tuples
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
    self.cur.execute(self.SELECT_SQL_ALL %{'tableName' : self.TABLENAME})
    rows = self.cur.fetchall():
    for row in rows:
      print row[0], row[1], row[2]

  def insertRow(self, new_row_dict): #new_row_dict is a dictionary eg. {'firstname': 'Tina', 'lastname': 'White','address' : '20 Fox St', 'city': 'Clearlake'}
    self.cur.execute(self.INSERT_ROW %{
      'tableName' : self.TABLENAME,
      'firstname': new_row_dict['firstname'],
      'lastname': new_row_dict['lastname'],
      'address': new_row_dict['address'],
      'city': new_row_dict['city']
      })
    self.db.commit()

  def getDictToString(self, sep, dict): #for updateRow function
    final_list= []
    for key,value in dict.items():
      output = '%s = %s' %(key,value)
      final_list.append(output)  
    return sep.join(final_list)

  def updateRow(self, id, updatedValueDict): #updatedValueDict is a dictionary eg. {'FirstName': 'Tinah', 'LastName': 'Whitt'}
    self.cur.execute(self.UPDATE_ROW %{'tableName': self.TABLENAME, 'column_data_info':self.getDictToString(',',updatedValueDict) , 'personID': id }) 
    self.db.commit()  

  def deleteRow(self, id):
    self.cur.execute (DELETE_ROW %{'tableName' : TABLENAME, 'personID': id})
    self.db.commit()

  def maxColumn(self, columnName):
    self.cur.execute(self.MAX_COLUMN %{'column_name': columnName, 'tableName': self.TABLENAME})
    max_col_value =  self.cur.fetchall() #tuple of tuples
    return max_col_value [0][0]