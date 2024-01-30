'''
Name of the project: "LIGHTLANG", THE SHOP FOR LANGUAGE COURSES

Made by: Illia Ruban
City and country(current): Puchheim 82178, Germany
City and country(native): Rubizhne, Luhanska Oblast, Ukraine

Github: https://github.com/illiaruban
LinkedIn: https://www.linkedin.com/in/illia-ruban-91194b2aa/

Date of recording: 16.01.2024
'''
import re
import sys
import os


class Course:
    def __init__(self, name, language, level, price):
        self.name = name
        self.language = language
        self.level = level
        self.price = price
        self.position = 0
    
    def __str__(self):
        info = f"Name of the course: {self.name}\nLanguage: {self.language}\nLevel: {self.level}\nPrice: ${self.price}"
        return info
    #getters and setters
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name,):
        if not name:
            raise ValueError("Course must have a name")
        self._name = name
    
    @property
    def language(self):
        return self._language
    @language.setter
    def language(self, language):
        if not language:
            raise ValueError("Course must have a language")
        elif matches := re.search(r"^([a-zA-Z-]{2,100})$", language):
            self._language = language
        else:
            raise ValueError("Language must be written only with alphabetic characters")

    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, level):
        if not level:
            raise ValueError("Course must have a level")
        self._level = level
    
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if not price:
            raise ValueError("Course must have a price")
        if price < 0:
            raise ValueError("Price of the course must be a non-negative value")
        self._price = price
    
    @classmethod
    def create_course(cls, courses_base):
        while True:
            try:
                while True:
                    name = input("Enter the name of the course: ")
                    for i in range(len(courses_base)):
                        if name == courses_base[i].name:
                            print("There is already a course with such name. Please, try again.\n")
                    break
                language = input("Enter the language of the course: ")
                level = input("Enter the level of the course: ")
                price = float(input("Enter the price of the course: "))
                course = Course(name, language, level, price)
                print("Course was created.")
                courses_base.append(course)
                course.position = len(courses_base) - 1 
                break
            except ValueError as error:
                print(f"{error}.\nPlease, try again:")
                continue
        return courses_base

class Administrator:
    def __init__(self, password="0000000000"):
        self.password = password

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        if matches:= re.search(r"^([0-9]{10})$", password):
            self._password = password  
        else:
            raise ValueError("Administrator password is incorrect:\n- only numeric characters\n- 10 characters in length")
    
    @classmethod
    def create_admin(cls):
        while True:
            try:
                password = input("Enter the password: ").strip()
                admin = cls(password)
                print("Successful registration.")
                break
            except ValueError as error:
                print(f"{error}.\nPlease, try again.")
                continue
        return admin

    def sign_in(self):
        password = input("Enter the password: ")
        if password == self.password:
            print(f"You entered as administrator.\n")
            return True
        else:
            print("Incorrect password.\n")
            return False

    @classmethod
    def print_course(cls, courses_base):
        return Customer.print_course(courses_base)

    @classmethod
    def print_customers(cls, customers_list):
        #prints 10 customers(if exist) and then prompts user to agree to see next 10 customers
        if customers_list == []:
            print("No customers yet.\n")
            return
        if len(customers_list) <= 10:
            for i in range(len(customers_list)):
                print(f"{i + 1}. ")
                print(customers_list[i])
                print("------------------")
        else:
            limit = 10
            while True:
                for i in range(limit):
                    print(f"{i + 1}. ")
                    print(customers_list[i])
                    print(f"Password: {customers_list[i].password}")
                    print("------------------")
                while True:
                    flag = input("Would you like to see more customers(yes/no)? ")
                    if flag == "yes":
                        if len(customers_list) >= limit + 10:
                            limit += 10
                        else:
                            limit += len(customers_list) - limit
                        break
                    elif flag == "no":
                        return 
                    else:
                        print("Invalid response. Please, try again.\n")
         
    @classmethod
    def print_customers_info(cls, customers_list):
        if customers_list == []:
            print("No customers yet.")
            return
        while True:
            index = int(input("Enter the number of the customer you would like to print out: ")) - 1
            if index < 0 or index > len(customers_list):
                print("Invalid index. Please, try again.")
                continue
            print(customers_list[index])
            print("Basket:\n")
            Administrator.print_course(customers_list[index].basket)
            print("Bought courses:\n")
            Administrator.print_course(customers_list[index].bought_courses)
            break
    
    @classmethod
    def add_course(cls, courses_base):
        Course.create_course(courses_base)
    
    @classmethod
    def delete_course(cls, courses_base):
        while True:
            index = int(input("Enter the number of course you want to delete(0 - to cancel): ")) - 1
            if index == -1:
                return
            if index < 0 or index > len(courses_base):
                print("Invalid index. Please, try again.")
                continue
            break
        courses_base.pop(index)
        print("Course was removed from the base.")
    
    def admin_service(self, courses_base, customers_list):
        while True:
            a = int(input("Choose the function:\n1 - to print out courses\n2 - to add a course\n3 - to delete a course\n4 - print out the customers\n5 - print out the certain customer`s account information\n0 - to exit: "))
            print("------------------------------")
            match(a):
                case 1:
                    print("Courses:\n")
                    Administrator.print_course(courses_base)
                    print("------------------------------")
                    continue
                case 2:
                    Administrator.add_course(courses_base)
                    print("------------------------------")
                    continue
                case 3:
                    Administrator.print_course(courses_base)
                    Administrator.delete_course(courses_base)
                    print("------------------------------")
                    continue
                case 4:
                    print("Customers:\n")
                    Administrator.print_customers(customers_list)
                    print("------------------------------")
                    continue
                case 5:
                    Administrator.print_customers(customers_list)
                    Administrator.print_customers_info(customers_list)
                    print("------------------------------")
                    continue
                case 0:
                    print("You logged out from administrator account.")
                    print("------------------------------")
                    return
                case _:
                    print("Invalid command.")
                    print("------------------------------")
                    continue
    
    def write_to_file(self, courses_base, customers_list):
        with open("admin_data.txt", "w") as adfile:
            adfile.write(f"{self.password}")

        with open("courses_base.txt", "w") as coursefile:
            if len(courses_base) == 0:
                coursefile.write("No courses yet.")
            else:
                for course in courses_base:
                    coursefile.write(f"{course.position},{course.name},{course.language},{course.level},{course.price}\n")
        #fix problems with \n characters 
        with open("customers_list.txt", "w") as custfile:
            if len(customers_list) == 0:
                custfile.write("No customers yet.")
            else:
                custfile.write(f"{len(customers_list)}\n")
                for customer in customers_list:
                    str_cust = f"{customer.name},{customer.password},{customer.balance}\n"
                    if customer.basket != []:
                        pos_list_basket = [customer.basket[k].position for k in range(len(customer.basket))]
                        str_cust += ','.join(map(str, pos_list_basket)) + "\n"
                    else:
                        str_cust += "Empty basket\n"

                    if customer.bought_courses != []: 
                        pos_list_bought = [customer.bought_courses[k].position for k in range(len(customer.bought_courses))]
                        str_cust += ','.join(map(str, pos_list_bought)) + "\n"
                    else:
                        str_cust += "No bought courses\n"
                    str_cust += "---------------------------------\n"
                    custfile.write(str_cust)
        print("Data is successfully saved.\n")

    def read_file(self, courses_base, customers_list):
        with open("admin_data.txt", "r") as adfile:
            self.password = adfile.readline()

        with open("courses_base.txt", "r") as coursefile:
            lines = coursefile.readlines()
            if len(lines) == 1 and lines[0] == "No courses yet":
                courses_base = []
            else:
                for line in lines:
                    position, name, language, level, pr = line.split(",")
                    price = float(pr)
                    course = Course(name, language, level, price)
                    course.position = position
                    courses_base.append(course)
            
        with open("customers_list.txt", "r") as custfile:
            amount = custfile.readline()
            if amount == "No customers yet":
                customers_list = []
            else:
                for i in range(int(amount)):
                    info = custfile.readline()
                    name, password, balance= info.split(",")
                    customer = Customer(name, password)
                    customer.balance = float(balance)
                    basket_info = custfile.readline()
                    bought_info = custfile.readline()
                    if basket_info != "Empty basket\n":
                        pos_basket = basket_info.split(",")
                        for pos in pos_basket:
                            customer.basket.append(courses_base[int(pos)])
                    if bought_info != "No bought courses\n":
                        pos_bought = bought_info.split(",")
                        for pos in pos_bought:
                            customer.bought_courses.append(courses_base[int(pos)])
                    customers_list.append(customer)
                    empty_line = custfile.readline()

class Customer:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.balance = 0.0
        self.bought_courses = []
        self.basket = []
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if matches := re.search(r"^([0-9a-zA-Z_ ]{8,50})$", name):
            self._name = name
        else:
            raise ValueError("Incorrect name:\n- name must only contain alphanumeric characters, space and underscore\n- name must be between 8 and 50 characters long")

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        if matches := re.search(r"^([0-9a-zA-Z]{8,16})$", password):
            self._password = password
        else:
            raise ValueError("Incorrect password:\n- length of the password must be between 8 and 16 symbols\n- password must only contain alphanumeric characters")
    
    def __str__(self):
        info = f"Username: {self.name}\nBalance: ${self.balance}\nBasket: {len(self.basket)} courses\nBought courses: {len(self.bought_courses)} courses"
        return info

    #methods
    @classmethod
    def print_course(cls, courses_base):
        if courses_base == []:
            print("No courses yet.\n")
            return
        if len(courses_base) <= 10:
            for i in range(len(courses_base)):
                print(f"{i + 1}. ")
                print(courses_base[i])
                print("------------------")
        else:
            limit = 10
            while True:
                for i in range(limit):
                    print(f"{i + 1}. ")
                    print(courses_base[i])
                    print("------------------")
                while True:
                    flag = input("Would you like to see more courses(yes/no)? ")
                    if flag == "yes":
                        if len(courses_base) >= limit + 10:
                            limit += 10
                        else:
                            limit += len(courses_base) - limit
                        break
                    elif flag == "no":
                        return 
                    else:
                        print("Invalid response. Please, try again.\n")

    @classmethod
    def sign_up(cls, customers_list):
        while True:
            try:
                name = input("Enter the username: ").strip()
                password = input("Enter the password: ").strip()
                customer = cls(name, password)
                print("Successful registration. Thank you!")
                customers_list.append(customer)
                break
            except ValueError as error:
                print(f"{error}.\nPlease, try again.")
                continue
        return customers_list
    
    @classmethod
    def sign_in(cls, customers_list):
        password = input("Please, enter the password: ").strip()
        flag = False
        for i in range(len(customers_list)):
            if password == customers_list[i].password:
                print(f"You entered as {customers_list[i].name}\n")
                flag == True
                return i
        if flag == False:
            print("No accounts with such name of password\n")
            return None

    def add_to_basket(self, courses_base, index): 
        for i in range(len(self.basket)):
            if courses_base[index].name == self.basket[i].name:
                print("Course was already added in the basket.")
                return
        self.basket.append(courses_base[index])
        print("Course was added in the basket.")
    
    def delete_from_basket(self, index):
        if self.basket == []:
                print("Basket is empty.\n")
                return
        self.basket.pop(index)
        print("Course was deleted from the basket.")    

    def buy(self, index):
        if self.basket == []:
                print("Basket is empty.\n")
                return
        if self.balance < self.basket[index].price:
            print("Not enough money to purchase this course. Please, recharge your account.")
            return 
        self.bought_courses.append(self.basket[index])
        self.balance -= self.basket[index].price
        self.balance = round(self.balance, 2)
        self.basket.pop(index)
        print("Course was bought. Thank you!")
        
    def recharge_account(self):
        cash = float(input("Enter the amount of money you would like to add: "))
        if cash < 0:
            print("You entered negative value. Unsuccessful operation.")
            return
        while True:
            resp = input(f"You entered {cash}$. Are you sure(yes/no/other response to exit)? ").lower().strip()
            if resp == "yes":
                self.balance += cash
                print(f"Account was recharged, current balance: {self.balance}$. Thank you!")
                break
            elif resp == "no":
                continue
            else:
                print("Operation is cancelled.")
                return
  
    def customer_service(self, courses_base):
        while True:
            a = int(input("Choose the operation:\n1 - to see the account info\n2 - to see basket\n3 - to see the bought courses\n4 - to recharge your account\n5 - to see the courses\n6 - to add course to the basket\n7 - to delete course from the basket\n8 - buy\n0 - to exit: "))
            print("------------------------------")
            match(a):
                case 1:
                    print("Account info:\n")
                    print(self)
                    print("------------------------------")
                    continue
                case 2:
                    print("Basket:\n")
                    self.print_course(self.basket)
                    print("------------------------------")
                    continue
                case 3:
                    print("Bought courses:\n")
                    self.print_course(self.bought_courses)
                    print("------------------------------")
                    continue
                case 4:
                    self.recharge_account()
                    print("------------------------------")
                    continue
                case 5:
                    self.print_course(courses_base)
                    continue
                case 6:
                    self.print_course(courses_base)
                    index = int(input("Enter the number of course you would like to add to basket: ")) - 1
                    if index < 0 or index > len(courses_base) - 1:
                        print("Invalid index.\n")
                        continue
                    self.add_to_basket(courses_base, index)
                    print("------------------------------")
                    continue
                case 7:
                    print("Basket:\n")
                    self.print_course(self.basket)
                    index = int(input("Enter the number of course would you like to delete from the basket(0 - to cancel)? ")) - 1
                    if index < 0 or index > len(self.basket) - 1:
                        print("Invalid index.\n")
                        continue
                    self.delete_from_basket(index)
                    print("------------------------------")
                    continue
                case 8:
                    self.print_course(self.basket)
                    index = int(input("Enter the number of the course you want to buy: ")) - 1
                    if index < 0 or index > len(self.basket) - 1:
                        print("Invalid index.\n")
                        continue
                    self.buy(index)
                    print("------------------------------")
                    continue
                case 0:
                    print("You logged out from the account. Come back later :)")
                    print("------------------------------")
                    return
                case _:
                    print("Invalid command. Please, try again")
                    print("------------------------------")
                    continue

def main():
    courses_base = []
    customers_list = []
    admin = Administrator()

    if os.path.exists("admin_data.txt"):
        admin.read_file(courses_base, customers_list)
    else:
        print("New session started. Please, create accounts and courses.\n")
    while True:
        a = int(input("Welcome to the LightLang! What would you like to do?\n1 - to sign up\n2 - to sign in\n3 - to enter as the administrator\n0 - to exit: "))
        match(a):
            case 1:
                Customer.sign_up(customers_list)
                print("------------------------------")
                customers_list[len(customers_list) - 1].customer_service(courses_base)
                continue
            case 2:
                index = Customer.sign_in(customers_list)
                if index != None:
                    customers_list[index].customer_service(courses_base)
                continue
            case 3:
                if admin.password == "0000000000":
                    print("There is no admin. Please, create the account:\n")
                    admin = Administrator.create_admin()
                    print("------------------------------")
                    admin.admin_service(courses_base, customers_list)
                    continue
                else:
                    if admin.sign_in() == True:
                        admin.admin_service(courses_base, customers_list)
                    continue
            case 0:
                admin.write_to_file(courses_base, customers_list)
                print("Goodbye! :)")
                sys.exit()
            case _:
                print("Invalid command. Please, try again\n")
                continue

if __name__ == "__main__":
    main()
        