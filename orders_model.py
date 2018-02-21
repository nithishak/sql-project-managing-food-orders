from config import *
from connect_mysql import *

class Orders: 

  db = connectToDB(getConnectionConfig())
  cur = db.cursor()

  TABLENAME = 'Orders'
  SELECT_SQL_BY_PERSON_ID = 'SELECT * FROM %(table_name)s WHERE PersonID = %(person_id)d'
  SELECT_SQL_ALL = 'SELECT * FROM %(table_name)s'
  INSERT_ROW = 'INSERT INTO %(table_name)s (OrderNumber,PersonID) VALUES (%(order_number)d, %(person_id)d)' 
  UPDATE_ROW = 'UPDATE %(table_name)s set %(column_data_info)s WHERE OrderID = %(order_id)d' #column_data_info can be 'column_name = 2' eg.
  DELETE_ROW = 'DELETE FROM %(table_name)s WHERE OrderNumber = %(order_number)d'

  def getRowById(self, Person_id):
    self.cur.execute (self.SELECT_SQL_BY_PERSON_ID %{'table_name' : self.TABLENAME , 'person_id' : Person_id})
    rows = self.cur.fetchall()
    if len(rows) == 0:
      print ("No orders found, please place an order!")
    else:
      print "Here are the person's orders:"
      #rows is a tuple of tuples
      for row in rows:
        print 'OrderNumber : ' + str(row[1]) + ' , OrderID : ' + str(row[0]) 


  def getAllRows(self):
    self.cur.execute(self.SELECT_SQL_ALL %{'table_name' : self.TABLENAME})
    rows = self.cur.fetchall() #tuple of tuples
    for row in rows:
      print row[0], row[1], row[2]

  def insertRow(self,new_row_dict): #new_row_dict here is a dictionary eg. {'orderNumber': 2, 'person_ID': 3}
    self.cur.execute (self.INSERT_ROW %{
      'table_name': self.TABLENAME, 
      'order_number' : new_row_dict['orderNumber'], 
      'person_id': new_row_dict['person_ID']
      })
    self.db.commit()

  def getDictToString(self,sep, dict): #for updateRow function
    final_list = []
    for key, value in dict.items(): #eg. dict = {'column1': 'updated_value1', 'column2' : 'updated_value2'}
      output = '%s = %s' %(key, value) #eg. 'column1 = updated_value1'
      final_list.append(output)
    return sep.join(final_list) # eg. (column1 = updated_value1, column2 = updated_value2)

  def updateRow(self,id, updatedValueDict):
    self.cur.execute (self.UPDATE_ROW %{'table_name': self.TABLENAME, 'column_data_info': self.getDictToString (',', updatedValueDict), 'order_id': id})
    self.db.commit()

  def deleteRow(self,id):
    self.cur.execute(self.DELETE_ROW %{'table_name': self.TABLENAME, 'order_number': id})
    self.db.commit()
