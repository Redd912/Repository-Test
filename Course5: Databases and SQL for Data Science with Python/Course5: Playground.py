#============================================ Module 1 =======================================================================
# SQL is a language used for relational databases to get data out of a database
# What data? Facts (words, numbers), Pictures, Assets
# What is a database? Repository of data, provides functionality for adding, modyfing and querying that data
# Basic SQL commands: CREATE, SELECT, INSERT, UPDATE, DELETE

# Select: 
SELECT COLUMN1, COLUMN2, ... FROM TABLE_1 ; # General syntax
SELECT * FROM TABLE_1 ; # To retreive all columns
SELECT <COLUMNS> FROM TABLE_1 WHERE <predicate> ; # To filter data based on a predicate
# e.g. to select first 5 rows: SELECT * FROM TABLE_1 WHERE ID <= 5 ;
# another e.g.: select * from FilmLocations where Locations = 'City Hall'

# Count:
# Retreives number of rows that matches the query criteria (NOT ROW CONTENT, JUST HOW MANY ROWS MATCH THE CRITERIA)
select COUNT(COUNTRY) from MEDALS where COUNTRY = 'CANADA' 

# Distinct:
# Removes duplicate values from a result set
select DISTINCT COUNTRY from MEDALS where MEDALTYPE = 'GOLD' # In case some countries receive multiple gold medals

# Limit:
# Restricts the number of rows retreived from the database
select * from tablename LIMIT 10
select * from MEDALS where YEAR = 2018 LIMIT 5 # shows 5 rows in the MEDALS table for a particular year

# Insert:
# Add new rows to a table
insert into tablename (Name, Surname, Age) values ('Mateusz', 'Pawlaczyk', 20) # IMPORTANT no. of columns must = to no. of values
# we can also add multiple rows to our Name, Surname, Age columns, just do another bracket () under the one above

# Update:
# Welp it updates a row
UPDATE tablename SET Columnname = Value WHERE condition # if you don't specify where, all the rows will be updated
# UPDATE Author SET Lastname='KATTA', FIRSTNAME='Lakshmi' WHERE Author_ID='A2'

# Delete
# deletes rows
DELETE FROM Author WHERE Author_ID IN ('A2','A3') # if you don't specify where, all rows will be removed (careful buddy)

#============================================ Module 2 =======================================================================
# Data Definition Language (DDL) Statements
# Used to define, change, or drop data - tables
# E.g. CREATE, ALTER, TRUNCATE, DROP


# Data Manipulation Language (DML) Statements
# Used to read and modify data - rows
# E.g. INSERT, SELECT, UPDATE, DELETE - row (like in module 1)

# Create:
# Syntax: 
CREATE TABLE table_name
    (
      column_name_1 datatype optional_parameters,
      column_name_2 datatype,
      column_name_n datatype
    )
# datatypes include: CHAR(2) - string of fixed length 2 AND VARCAHAR(14) - variable length, up to 14 chatacters long
# optional parametrs include: PRIMARY KEY (prevents dulicates in the table), NOT NULL

# Better example:
CREATE TABLE EMPLOYEES (
                            EMP_ID CHAR(9) NOT NULL, 
                            F_NAME VARCHAR(15) NOT NULL,
                            L_NAME VARCHAR(15) NOT NULL,
                            SSN CHAR(9),
                            B_DATE DATE,
                            SEX CHAR,
                            ADDRESS VARCHAR(30),
                            JOB_ID CHAR(9),
                            SALARY DECIMAL(10,2),
                            MANAGER_ID CHAR(9),
                            DEP_ID CHAR(9) NOT NULL,
                            PRIMARY KEY (EMP_ID));
                            
  CREATE TABLE JOB_HISTORY (
                            EMPL_ID CHAR(9) NOT NULL, 
                            START_DATE DATE,
                            JOBS_ID CHAR(9) NOT NULL,
                            DEPT_ID CHAR(9),
                            PRIMARY KEY (EMPL_ID,JOBS_ID));
 
 CREATE TABLE JOBS (
                            JOB_IDENT CHAR(9) NOT NULL, 
                            JOB_TITLE VARCHAR(30),
                            MIN_SALARY DECIMAL(10,2),
                            MAX_SALARY DECIMAL(10,2),
                            PRIMARY KEY (JOB_IDENT));

CREATE TABLE DEPARTMENTS (
                            DEPT_ID_DEP CHAR(9) NOT NULL, 
                            DEP_NAME VARCHAR(15) ,
                            MANAGER_ID CHAR(9),
                            LOC_ID CHAR(9),
                            PRIMARY KEY (DEPT_ID_DEP));

CREATE TABLE LOCATIONS (
                            LOCT_ID CHAR(9) NOT NULL,
                            DEP_ID_LOC CHAR(9) NOT NULL,
                            PRIMARY KEY (LOCT_ID,DEP_ID_LOC));

# Alter:
# Add/remove columns, keys, constraints, or modify datatype
# Syntax:
ALTER TABLE <your_table_name> # and then, same line either:
ADD COLUMN <column_name_n> datatype
MODIFY <column_name_n> <data_type>
 # To change the data type of an existing column to varchar data type write:
ALTER TABLE table_name ALTER COLUMN column_name SET DATA TYPE VARCHAR(20);
#  To add a column ‘ID’ that contains 7 character alpha-numeric values to our database
ALTER TABLE Employees ADD ID char(7)


# Drop (delete)
DROP TABLE <table name>;
DROP COLUMN <column_name_n>

# Truncate (delete data in table without deleting table itself)
TRUNCATE TABLE <table_name>
  IMMEDIATE # specifies to process statement immediately, cannot be undone)

# SCENARIO:
# create a table with CREATE
# ALTER - create a new column
# UPDATE - add values e.g. update petsale set quantity = 24 where ID = 1
# after each modification, use select * from petsale to SEE THE TABLE (otherwise won't show up)

#============================================ Module 3 =======================================================================
# ===== REFINING YOUR RESULTS
# Retreiving rows when predicate unknown e.g. can't use ID because don't remember the specific number
SELECT firstname FROM Author WHERE firstname like 'R%' # finds all names that start with the letter R (% can be in front of R, after R or BEFORE AND AFTER - [THERE ARE RULES - see SOME EXAMPLES OF GROUPING/SORTING], but MUST BE within quotation marks)
SELECT title FROM Book WHERE pages >=290 AND pages<=300 # finds all books whose number of pages is between 290 and 300
SELECT title FROM Book WHERE pages BETWEEN 290 AND pages 300 # alternative version
# Now, what do we do when we can't select range, e.g. when we want to know which country the authors are from?
SELECT firstname, lastname, country FROM Author WHERE country="Australia" OR "country"=BR # this is if we know which country we're interested in
SELECT firstname, lastname, country FROM Author WHERE country IN('AU','BR','CH','PL') # this is if you want to use maaaany countries (less typing)

# Sorting Result Sets (e.g. alphabetically)
SELECT * FROM Book # this will show you the whole dataset, but what if you want to select titles only?
SELECT title FROM book # ok, but now the list isn't sorted in any order as we don't have IDs, let's sort alphabetically
SELECT title FROM book ORDER BY title # ascending order
SELECT title FROM book ORDER BY title DESC # descending order, now it's from Z to A 
SELECT title FROM book ORDER BY 2 # if you want to sort by indicating column sequence number, in this case we're talking about second column (pages)

# Grouping Result Sets
# E.g. eliminating duplicates and further restricting values
SELECT country FROM Author ORDER BY 1 # full list of countries where authors come from (alphabetically), there are duplicates
SELECT DISTINCT(country) FROM Author # no duplicates :D, but we don't know how many authors come from each country :<, so:
SELECT country, count(country) FROM Author GROUP BY country # wheeeyyyy, ok but now we have a new column that's called '2' yuck
SELECT country, count(country) as Count FROM Author GROUP BY country # sa,e as above but count column is actually called count
# wanna see countries where the number of authors is greater than say 4?
SELECT country, count(country) as Count FROM Author GROUP BY country HAVING COUNT(country)>4 # having is a condition for group by clause

# SOME EXAMPLES OF GROUPING/SORTING
# basics
SELECT F_NAME, L_NAME FROM EMPLOYEES WHERE ADDRESS LIKE '%Elgin,IL%'; # to find names and surnames who live in Elgin
...WHERE B_DATE LIKE '197%'; # those who were born in the 70's
# first example & before and after - indicates that address string can have more character, both before and after required text - results appear as Elgin, IL, X Street or Y Street, Elgin, IL, if % before Elgin, then only Elgin, IL, X Street would show up
# second example, extra values can only appear after 7 (1970-1979) not before 1
# actual grouping
SELECT DEP_ID, COUNT(*) FROM EMPLOYEES GROUP BY DEP_ID; # Grouping - for each department ID, we want to find the number of employees in department
SELECT DEP_ID, AVG(SALARY) FROM EMPLOYEES GROUP BY DEP_ID HAVING AVG(SALARY) >=60000; # group by dep_id and filter the ones that have avg. salary of >= 60,000
ORDER BY AVG(SALARY) DESC # ADD THIS TO THE ONE ABOVE TO SORT BY DESCENDING ORDER :)

# EXAMPLE OF SORTING
SELECT F_NAME, L_NAME, DEP_ID FROM EMPLOYEES ORDER BY DEP_ID;

# Practice Quiz answers
SELECT * FROM Employees ORDER BY Lastname # if you want to retreive a list of employees in alphabetial order of Lastname 
HAVING # Used in order to set a filtering condition when using GROUP BY clause
SELECT * FROM Author WHERE Country IN ('A','B','C') # you want to retreive a list of authors from 3 countries
SELECT Title, Price FROM Book WHERE Price >= 10 and Price <= 25; # TWO WAYS TO RETREIVE LIST OF BOOKS PRICES IN RANGE $10-$25
SELECT Title, Price FROM Book WHERE Price BETWEEN 10 and 25; # TWO WAYS TO RETREIVE LIST OF BOOKS PRICES IN RANGE $10-$25

# ===== FUNCTIONS, MULTIPLE TABLES AND SUB-QUERIES

# Aggregate or column functions
# 1) takes a collection of like values (e.g. takes all the values in a column as input and returns a single value or null)
# 2) SUM(), MIN(), MAX(), AVG()

SELECT SUM(column_name) FROM table_name # gives back a small column with a given number, if you want that column to have an actual name do:
SELECT SUM(column_name) as column_name FROM table_name 

# Similarly:
SELECT MIN/MAX()

# Get min value of ID column for dogs:
SELECT MIN(ID) FROM Pets WHERE Animal = 'Dog'

# Calculate avg. cost per dog:
SELECT AVG(COST / QUANTITY) FROM Pets WHERE Animal = 'Dog'


# Scalar functions
# 1) perform operations on every input value:
# 2) ROUND(), LENGTH(), UCASE, LCASE
SELECT ROUND(column_name, decimal_places) FROM table_name
SELECT ROUND(Cost, 2) FROM Pets

SELECT UCASE(ANIMAL) FROM PETRESCUE # prints out all animal names in upper case
# Date and Time functions
# SQL contains DATE, TIME, TIMESTAMP types:
# DATE = 8 digits = YYYYMMDD
# Time has 6 = HHMMSS
# TIMESTAMP has 20 = YYYYXXDDHHMMSSZZZZZ where XX = month and ZZZZZ = microseconds

# To select a year from a given RescueDate column:
SELECT YEAR(RESCUEDATE) FROM PETRESCUE;

# To add 1 year to all dates in the rescuedate column:
SELECT DATE_ADD(RESCUEDATE, INTERVAL 1 YEAR) FROM PETRESCUE # to do days/months, keep everything the same, just change 1 year to idk 3 DAY 4 month

# Similarly
SELECT DATE_SUB(RESCUEDATE, INTERVAL 3 DAY) FROM PETRESCUE

# Difference between today and the dates in the table (in days)
SELECT DATEDIFF(CURRENT_DATE, RESCUEDATE) FROM PETRESCUE

# How much time has passed since each date in the column relative to current date)
SELECT FROM_DAYS(DATEDIFF(CURRENT_DATE, RESCUEDATE)) FROM PETRESCUE

# ===== Sub-queries and nested selects
# Query inside another query
# e.g.:
SELECT column1 FROM table WHERE column2 = (SELECT MAX(column2) FROM TABLE)

# Why use them? Say you want to select all employees where salary > avg(salary)
SELECT * FROM EMPLOYEES WHERE SALARY < AVG(SALARY)
# oh noes D: le *bigge erroré*, but wait! I know what to do:
SELECT * FROM EMPLOYEES WHERE SALARY < (SELECT AVG(SALARY) FROM EMPLOYEES);
# sub-query works :DD

# Another example: (first and last names of the oldest employee - smallest date of birth) 
SELECT F_NAME, L_NAME FROM EMPLOYEES WHERE B_DATE = (SELECT MIN(B_DATE) FROM EMPLOYEES);

# Another one: retreive job information for employees earning >$70,000.
# Retreive details from JOBS table, which has common IDs with those available in EMPLOYEES table, provided the salary
# in the EMPLOYEES table is greater than 70k, do:
SELECT JOB_TITLE, MIN_SALARY, MAX_SALARY, JOB_IDENT
FROM JOBS
WHERE JOB_IDENT IN (select JOB_ID from EMPLOYEES where SALARY > 70000 );

# Yet another one: (creating derived table - can be used to query specific info)
# Say you want to know avg salary of top 5 earners in company, you first extract a table of top 5 salaries as a table
# then, from that table you can query the avg vale of salary:
SELECT AVG(SALARY) 
FROM (SELECT SALARY 
      FROM EMPLOYEES 
      ORDER BY SALARY DESC 
      LIMIT 5) AS SALARY_TABLE;
# Note that it is necessary to give an alias to any derived tables.

# ===== WORKING WITH MULTIPLE TABLES
# Ways to access multiple tables in the same query:
# 1) sub-queries
# 2) implicit JOIN
# 3) JOIN operators (INNER JOIN, OUTER JOIN, and so on)

# e.g. Retreive JOB information and a list of employees whose b_year is after 1976:
# sub-query:
SELECT JOB_TITLE, MIN_SALARY, MAX_SALARY, JOB_IDENT
FROM JOBS
WHERE JOB_IDENT IN (SELECT JOB_ID
                    FROM EMPLOYEES
                    WHERE YEAR(B_DATE)>1976 );
# implicit join
SELECT J.JOB_TITLE, J.MIN_SALARY, J.MAX_SALARY, J.JOB_IDENT
FROM JOBS J, EMPLOYEES E
WHERE E.JOB_ID = J.JOB_IDENT AND YEAR(E.B_DATE)>1976;

# e.g. Retrieve only the list of employees whose JOB_TITLE is Jr. Designer
# Sub-query:
SELECT *
FROM EMPLOYEES
WHERE JOB_ID IN (SELECT JOB_IDENT
                 FROM JOBS
                 WHERE JOB_TITLE= 'Jr. Designer');
# Implicit joins:
SELECT *
FROM EMPLOYEES E, JOBS J # 
WHERE E.JOB_ID = J.JOB_IDENT AND J.JOB_TITLE= 'Jr. Designer';

# notice how we're assigning aliases in joins, helpful in cases where specific columns are to be accessed from different tables
# also notice how both sub-queries and joins give the same results :)
