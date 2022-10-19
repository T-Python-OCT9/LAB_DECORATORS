
from logging import exception


def decorators(func):

    def wrapper(*args, **kwargs):
        for i in  args:
            if isinstance(*args, str) and isinstance (len(*args)> 5):
              print("OK")
                    
            return decorators(*args, **kwargs)
        
    return wrapper

#use the decorator

@decorators
def checker(x:str,b:str ):
    print(x)
    print(b)

try:
   checker("123") 
except ValueError:
    print("the arguments should be str and it should have more than 5 characters")
except Exception:
    print("there is something wrong")



