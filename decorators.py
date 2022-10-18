'''
## Create a decorator that decorates a function with one or more arguments.
- This decorator should check that the argument is of type str and the length of the str is more than 5 
- else raise an exception of type ValueError telling the user the arguments should be str and it should have more than 5 characters .
'''



def document_it(func:str):
    def wrapper(*args, **kwargs):
    
        if len(text)>=6  :
            print("you input is string and have more than 5 character")
            return func(*args, **kwargs)
        else :
            print("you input may not string or have less than 5 character")
            return func(*args, **kwargs)
        
    return wrapper


@document_it
def check(text:str):
    print("checked !")

text:str=input("please enter your text:\n")
try:
    check(text)
except ValueError:
    print("VALUE ERROR: the arguments should be str and it should have more than 5 characters")    

