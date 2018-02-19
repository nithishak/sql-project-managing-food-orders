from sys import stdin
from person_model import *
from orders_model import *

person = Persons()
order = Orders()

personID = input('Please enter a PersonID number: ') #raw_inout is for strs
isPersonInDataBase = person.getRowById(personID) #returns either true or false

while True:

  if isPersonInDataBase == False:
    print "Please create an entry for this person"
    row_inputs = {}
    row_inputs['firstname'] = raw_input('Please enter the person''s last name: ')
    row_inputs['lastname'] = raw_input('Please enter the person''s first name: ')
    row_inputs['address'] = raw_input('Please enter the person''s address: ')
    row_inputs['city'] = raw_input('Please enter the person''s city: ')
    person.insertRow(row_inputs)
    personID = person.maxColumn('PersonID')
    print "Thank you. The person's id is " + str(personID)
    isPersonInDataBase = True
  else:
    order.getRowById(personID) #
    user_input = input('What would you like to do? Please choose \n 1.to add an order \n 2 to delete an order\n 3 to update an order \n 4 to exit\n')
    
    if user_input == 1:
      orderNumber = input('Please enter order number: ')
      new_row_inputs = {}
      new_row_inputs['orderNumber'] = orderNumber
      new_row_inputs['person_ID'] = personID
      order.insertRow(new_row_inputs)
    elif user_input == 2:
      orderId = input('Please enter order to delete: ')
      order.deleteRow(orderId)
    elif user_input == 3:
      orderId = input('Please enter order ID to update: ')
      orderNumber = input('Please enter order number: ')
      order.updateRow(orderId, {'OrderNumber':orderNumber})
    elif user_input == 4:
      sys.exit()
    else:
      print "invalid option, pick again"
