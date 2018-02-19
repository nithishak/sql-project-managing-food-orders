from config import *
from connect_mysql import *

class Orders: 

  db = connectToDB(getConnectionConfig())
  cur = db.cursor()

  TABLENAME = 'Orders'
  SELECT_SQL_BY_PERSON_ID = 'select * from %(table_name)s where PersonID = %(person_id)d'
  SELECT_SQL_ALL = 'select * from %(table_name)s'
  INSERT_ROW = 'insert into %(table_name)s (OrderNumber,PersonID) values (%(order_number)d, %(person_id)d)' 
  UPDATE_ROW = 'update %(table_name)s set %(column_data_info)s where OrderID = %(order_id)d'
  DELETE_ROW = 'delete from %(table_name)s where OrderNumber = %(order_no)d'

  def getRowById(self, Person_id):
    self.cur.execute (self.SELECT_SQL_BY_PERSON_ID %{'table_name' : self.TABLENAME , 'person_id' : Person_id})
    rows = self.cur.fetchall()
    if len(rows) == 0:
      print ("No orders found, please place an order!")
    else:
      print "Here are the person's orders:"
      #print rows #tuple of tuples
      for row in rows:
        print 'OrderNumber : ' + str(row[1]) + ' , OrderID : ' + str(row[0]) #orderID


  def getAllRows(self):
    self.cur.execute(self.SELECT_SQL_ALL %{'table_name' : self.TABLENAME})
    for row in cur.fetchall():
      print row[0], row[1], row[2]

  def insertRow(self,new_row): #row here is a dictionary
    self.cur.execute (self.INSERT_ROW %{'table_name': self.TABLENAME, 'order_number' : new_row['orderNumber'], 'person_id': new_row['person_ID']})
    self.db.commit()

  def getDictToString(self,sep, dict): #for updateRow function
    final_list = []
    for key, value in dict.items():
      output = '%s = %s' %(key, value)
      final_list.append(output)
    return sep.join(final_list)

  def updateRow(self,id, updatedValueDic):
    self.cur.execute (self.UPDATE_ROW %{'table_name': self.TABLENAME, 'column_data_info': self.getDictToString (',', updatedValueDic), 'order_id': id})
    self.db.commit()

  def deleteRow(self,id):
    self.cur.execute(self.DELETE_ROW %{'table_name': self.TABLENAME, 'order_no': id})
    self.db.commit()
