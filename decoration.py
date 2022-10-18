'''
# LAB_DECORATORS

## Create a decorator that decorates a function with one or more arguments.
- This decorator should check that the argument is of type str and the length of the str is more than 5 
- else raise an exception of type ValueError telling the user the arguments should be str and it should have more than 5 characters .
'''


def check_it(func):
    def deco_condition(*args):
        for x in (args):
            if (isinstance(x, str) and len(x) > 5):
                print(f"You have entered approved word * {x} *")
            else:
                raise ValueError("arguments should be str and it should have more than 5 characters ")
        return  func(*args)
    return deco_condition
    
@check_it
def test_input(firstName, lastName):
    pass

fname_input=input("Enter your first name: ")
lname_input=input("Enter you last name: ")
try:
    test_input(fname_input, lname_input)
except ValueError:
    print("arguments should be str and it should have more than 5 characters")
    



