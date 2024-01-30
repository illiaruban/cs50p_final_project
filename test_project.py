from project import User, Customer, Course, Administrator
import pytest

def test_init_customer():
    #case with too short password for object - error
    with pytest.raises(ValueError):
        cust1 = Customer("illia", "111")
    #case with empty strings for object - error
    with pytest.raises(ValueError):
        cust2 = Customer("", "")
    #case with too long password - error
    with pytest.raises(ValueError):
        cust3 = Customer("illia ruban", "1111111111111111111111111111111111")
    #check if no customer was created - amount of customers = 0``


def test_init_course():
    #case with empty strings for object - error
    with pytest.raises(ValueError):
        course1 = Course("", "", "", 9.99)
    #case with negative price - error
    with pytest.raises(ValueError):
        course2 = Course("Basic English", "English", "A1", -9.99)

def test_init_admin():
    #incorrect format of password - error
    with pytest.raises(ValueError):
        admin = Administrator("a234561789")
    #too many characters for password - error
    with pytest.raises(ValueError):
        admin = Administrator("11111234561789")

def test_basket():
    course = Course("test", "english", "a1", 15.99)
    customer = Customer("illia ruban", "13032003")
    courses_base = []
    courses_base.append(course)
    #add course to the basket
    customer.add_to_basket(courses_base, 0)
    assert len(customer.basket) == 1
    #check if right course is in the basket
    assert customer.basket[0].name == courses_base[0].name
    assert customer.basket[0].price == courses_base[0].price

    #delete course from the basket
    customer.delete_from_basket(0)
    assert len(customer.basket) == 0 

    

def test_buy():
    course = Course("test", "english", "a1", 15.99)
    customer = Customer("illia ruban", "13032003")
    courses_base = []
    courses_base.append(course)
    #add course to the basket
    customer.add_to_basket(courses_base, 0)

    #current balance - 0.00$ - not enough money to buy
    customer.buy(0)
    assert len(customer.bought_courses) == 0

    #simply replicate the recharge account function
    customer.balance += 20
    #current balance - 20.00$
    customer.buy(0)
    assert len(customer.bought_courses) == 1
    assert customer.bought_courses[0].name == courses_base[0].name
    assert customer.balance == 4.01