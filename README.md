<h1> Example of CRUD operations with python and mysql </h1>

<h2> Envinornment </h2>
<ol> OS - Ubuntu </ol>
<ol> Python - 2.X </ol>

<h2> Prerequisites </h2>
<ol> <code> sudo apt-get install mysql-server </code></ol>
<ol> <code> sudo apt-get install python-pip python-dev libmysqlclient-dev </code></ol>
<ol> Create table Orders <code> 
create database testDB;
CREATE TABLE `Orders` (
  `OrderID` int(11) NOT NULL,
  `OrderNumber` int(11) DEFAULT NULL,
  `PersonID` int(11) DEFAULT NULL,
  PRIMARY KEY (`OrderID`),
  KEY `PersonID` (`PersonID`),
  CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`PersonID`) REFERENCES `Persons` (`PersonID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Persons` (
  `PersonID` int(11) NOT NULL,
  `LastName` varchar(255) DEFAULT NULL,
  `FirstName` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `City` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`PersonID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
</code> </ol>


<h2> How to run ? </h2>


