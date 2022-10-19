'''

# LAB_DECORATORS

## Create a decorator that decorates a function with one or more arguments.
- This decorator should check that the argument is of type str and the length of the str is more than 5 
- else raise an exception of type ValueError telling the user the arguments should be str and it should have more than 5 characters .




def DECORATORSFunc(theFunction):
     def decorator(*args, **kwargs):
         for i in args:
             if not (isinstance(i, str) and len(i) > 5):
                 raise ValueError(
                     'the arguments should be str and it should have more than 5 characters .')
         for i in kwargs:
             if not (isinstance(i, str) and len(i) > 5):
                 raise ValueError(
                     'the arguments should be str and it should have more than 5 characters .')
         return theFunction(*args, **kwargs)
     return decorator

@DECORATORSFunc
def baseFunction(name: str):
     pass
@DECORATORSFunc
prin("Pleas enter your names!! peco you have more names so pleas tell to users whats th ecolor you love if she love the black color tel me pleaz ")

try:
     baseFunction(name='fgh')
except ValueError:
     print('Name must be a tring and more than 5 characters')

     '''


def DECORATORSFunc(argument : str):
     def wrapper (*args , **kwargs):
         if len(name) >= 5 and type(name) == str :
             print ("what u typed is string and more then 5 ")
             return argument (*args,**kwargs)
         else:  not len(name) >= 5 and not type(name) == str 
         return argument(*args,**kwargs)
     return wrapper

@DECORATORSFunc
def  check_string_type (name: str) :
     print ("is less then 5 and type is not string")

name = str(input("Enter your full name : "))

try :
     check_string_type(name)
except ValueError:
     print (" The arguments should be str and it should have more than 5 characters . ")

