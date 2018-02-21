# Project name

Performing CRUD operations on relational databases using mySQL and Python.

##  Environment 

- OS: Ubuntu
- Python 2.X
- mySQL

## Objective: <br>
The aim of this project is to perform the following mySQL operations: <br>
- creating a database
- creating tables within databases
- utilizing the concept of primary to uniquely identify each row in a table
- uilizing the concept of foreign keys to maintain the integrity of data across tables
- creating a row in a table (C)
- retrieving a row in a table (R)
- updating a row in a table (U)
- deleting a row in a table (D)

## Libraries needed: 


## Template tables
- Create a database named DB <br>
- To create the database DB, type in mySQL server: <br>
```` create database DB; ````
- To use database, type in mySQL server: <br>
```` use DB;  ````
- To create a table named Orders, type in my SQL server: <br>
```` 
CREATE TABLE Orders (OrderID int NOT NULL AUTO_INCREMENT, 
                     OrderNumber int NOT NULL,
                     PersonID int, 
                     PRIMARY KEY(OrderID), 
                     FOREIGN KEY(PersonID) REFERENCES Persons(PersonID));
````
- To create a table named Persons, type in mySQL server: <br>
````
 CREATE TABLE Persons (PersonID int NOT NULL AUTO_INCREMENT, 
                       LastName varchar(255) NOT NULL, 
                       FirstName varchar(255), 
                       Address varchar(255), 
                       City varchar(255), 
                       PRIMARY KEY(PersonID));
````

## Files available: 
1. config.py - contains connection to mySQL parameters
2. connect_mysql.py - contains a function that connects to mySQL server using parameters from config.py
3. orders_model.py - contains helper functions for CRUD operations meant for the table Orders
4. persons_model.py - contains helper functions for CRUD operations meant for the table Persons
5. main.py - main code that uses abovementioned helper functions to carry out simple tasks like managing a person's food orders using PersonID.

## Details: 
- In order to commence this project, a connection to mySQL server has to be established. In order to accomplish this, the parameters in the config.py file are used within the function from connect_mysql.py. 
- The orders.py file contains basic functions that can be called to retrieve/add/update/delete a row from the table Orders. An additional function to display the entire table has been included as well. The information regarding formats for function inputs can be found within the comment section of each function.
- Like the orders. py file, the person.py file has similar basic functions that can be applied to the table Persons. Additional functions that show the entire table and find the maximum value for a specified column can also be found. The information regarding formats for function inputs can be found within the comment section of each function.
- The main function runs a small program where the records within both tables can be managed by the user.
  - The program begins by asking the user to input a PersonID: 
  - If the id number provided exists in the Person's table, the order numbers and order ids for that person from the Orders table are displayed. The  user is next asked if he/she wants to
    1. add a new order 
    2. delete an existing order using an order id
    3. update an order
    4. exit the program
  - If the person id provided does not exist in the Persons table, an error shows that the id is not present, and a prompt asks the user to create an entry for the person and takes in necessary fields to populate the Persons table. An id is automatically created for the new person entry and displayed to the user. Once this is done, the options available to an existant person id will show.

- The program continues till the user wishes to exit the program.

## How to run? :
- Run the main.py file but remember to change relevant parameters in config.py.
