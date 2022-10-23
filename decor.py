

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
    print("the arguments should be str and it should have more than 5 characters")

    
    

