
name = str(input("Enter your full name : "))

def DECORATORSFunc(argument : str):
    def wrapper (*args , **kwargs):
        
         if len(name) >= 5 and type(name) == str :
             print ("what u typed is string and more then 5 ")
             return argument (*args,**kwargs)
         else:  not len(name) >= 5 and not type(name) == str 
         return argument(*args,**kwargs)
    return wrapper

def  check_string_type (name: str) :
     print ("is less then 5 and type is not string")

try :
     check_string_type(name)
except ValueError:
     print (" The arguments should be str and it should have more than 5 characters . ")
