'''

LAB_DECORATORS

'''

def _decorator(func):                                              # Create a decorator that decorates a function with one or more arguments.
    def wrapper(*args, **kwargs):
        ''' This decorator should check that the argument is of type str 
                        and the length of the str is more than 5 '''
        for element in args :
            if isinstance(element , str) and len(element) > 5:
                print("You used a function, clalled:" , func.__name__) # this will be printing  for evey argument
            else:                                                 #  else raise an exception of type ValueError telling the user the arguments should be str and it should have more than 5 characters 
                raise ValueError("The user the arguments should be str and it should have more than 5 characters")      
        for element in kwargs :
            if not isinstance(element , str) and len(element) > 5: # i used (not) to rais error only without any other if else statment
                raise ValueError("The user the arguments should be str and it should have more than 5 characters")
        return func(*args, **kwargs)
    return wrapper


@_decorator                                                                     #using decorator
def test( name : str  , favColor : str ) -> str:
    print(f"My name is : {name} , my favorite color is : {favColor}" )

name = input("Please enter your first name :" )
favColor = input("What is your favorite color? ")


test(name , favColor)                                                           #Calling func




