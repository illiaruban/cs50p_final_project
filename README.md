# "LightLang", The Shop For Language Courses
#### Video Demo: https://youtu.be/DUWwCE--Eb4
#### Description:
**"LightLang"** is an online shop which allows to purchase courses as a customer and create courses as an administrator. 

## PROGRAM DESIGN
In the file called project.py three classes with their methods are created - **Course, Administrator and Customer**.

- **Course** class has its name, language, level of the course(A1-C2 etc.) and its price
- **Administrator** has his special password(specifically 10 number password)
- **Customer** has his name, password(between 8 and 16 alphanumeric characters), balance(money), basket and bought courses represented as lists that can be(and should be) updated

Now we can see the ***customer operations***.
### CUSTOMER OPERATIONS
**Customer** can:
- see all the personal information(name, password, amount of the course in the basket and the amount of bought courses)
- see the courses in the basket
- see the courses customer bought
- see all the courses in the courses database(classmethod and used in administrator class)
- recharge his account to buy a course(if there is not enough money)
- add course in the basket
- delete course from the basket
- buy a course
- log out from his account

**It must be said that to buy a course customers must:**
- recharge his account(if not enough money so optional)
- add course to the basket
- select "to buy" operation and choose the right course
And then course will disappear from the basket but appear in the list of bought courses.

Let`s move on to the ***administrator operations***.
### ADMINISTRATOR OPERATIONS
**Administrator** is able to:
- see all the courses
- to add a course
- to delete a course
- to print out all the customers
- to print all the info about the certain customer(including basket and bought courses)
- log out from his account

To add a course administrator must enter all the parameters of the course after calling **add_course()** function(which calls **create_course()** method from **Course** class) from the **Course** class and course will appear in the courses database for every customer(same with deleting a course).

### START OF THE PROJECT
If text files for storing information do not exist(they will be talked about later), user must at the beginning create admin account to start creating courses. Then with creating accounts of the customer the amount of information will grow and develop in all aspects.
Now we can talk about the ***flow of the program***.

### FLOW OF THE PROGRAM
When a user enters "LightLang", he is asked to sign up(create a new account) or sign in(if he already has one). 
If user does not have an account, he enters the name and password and has access to the features of customer`s accounts.
If user has an account, he can simply enter his password to log in. 
Then, if user is done with his actions, he can log out and see start screen again. 
However, if user has a password of administrator account, he can enter this account by inputting password and he is able to change courses etc. 

### FINISH OF THE PROGRAM
After the program is stopped a function from **Administrator** class is called to collect all the data and rewrite it into three files - "admin_data.txt", "customers_list.txt" and "courses_base.txt". 
File with customers will keep their account information as well as indexes of the courses in the basket and the list of bought courses. In this case index means a position of the course(variable **self.position**) in the original courses database so the file with customers will not be incorrect and inconvenient to read. When program starts again, all the information about basket and bought courses will be given to the certain account again through the indexes placed in the text file.

And when program starts again, all the information will be read from text files to continue updating the databases. 

This was "LightLang".








