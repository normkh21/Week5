# functions
# from email.utils import * # this line will make all functions inside the utils module(in the email package) avaialble in current file
import time

#defining the functions
def greet_user():
    # for user
    """Greets the user."""""
    print("Welcome to Class!")
    print("this was basic function")

def greet_user_1(name):
    """Greets the user with given name."""""
    print(f"welcome to {name}!")

def greet_user_2(username, company="Google'"):  # COMPANY ARGUMENT IS AN OPIONAL ARGUMENT, AND DEFAULT VALUE IS GOOGLE
    """Greets the user with given name."""""
    print(f"{username}, welcome to {company.upper() }!")
    print("have a Great Day")

def greet_user_3(username, company="Google'"):  # COMPANY ARGUMENT IS AN OPIONAL ARGUMENT, AND DEFAULT VALUE IS GOOGLE
    """Greets the user with given username and keyword arguemtn 'company'."""""
    print(f"{username}, welcome to {company.upper() }!")
    print("have a Great Day")


def greet_user_4(username, company=None):  # COMPANY ARGUMENT IS AN OPIONAL ARGUMENT, AND DEFAULT VALUE IS GOOGLE
    """Greets the user with given username and keyword arguemtn 'company'."""""
    if company is None:
        print(f"{username.title()}, Welcome to new home ")
    else:
        print(f"{username.title()}, Welcome to {company.upper()}")
    print("have a Great Day")



# comp = 'level up'
# greet_user() # this is the execution of the code inside the function >> calling the function
# time.sleep(5)
# greet_user_1(comp)  # name parameter is required here, otherwise TypeError is  thrown
# greet_user_1("Jungle")  # name parameter is required here, otherwise TypeError is  thrown
#
# greet_user_1(input("enter company name:"))


##print("Print statement")


# Packages -  directory with '_init_.py' empty file
# Module - '.py' file (python file)

greet_user_2('levelup' , 'Rustem')
greet_user_2('Rustem', 'Google')  # position is important here TO PRINT OR DO THE EXECUTION CORRECTLY
# greet_user_2('Rustem') # TypeError: greet_user_2() missing 1 required positional argument: 'username'
greet_user_3('Polina') # here function is using default value for company argument, which was not provided in the call
greet_user_3('Abdul', 'Facebook' ) # function overwrites the default 'google' value for the company argument
greet_user_4('Vika') # company argument was not used, see if condition in the function
greet_user_4('Murod', 'Bloomberg')

# HW: FROM 8-1 TO