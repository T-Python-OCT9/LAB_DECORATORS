'''
## Create a decorator that decorates a function with one or more arguments.
- This decorator should check that the argument is of type str and the length of the str is more than 5 
- else raise an exception of type ValueError telling the user the arguments should be str and .
'''



def document_it(func:str):
    def wrapper(*args):

        if len(text)>=6  and isinstance(text,str) :
            print("you input is string and have more than 5 character")
            return func(*args)
        elif len(text) <6 or not isinstance(text,str):
            raise ValueError("ERROR:you input may not string and it should have more than 5 characters")
         
    return wrapper


@document_it
def check(text:str):
    print("checked !")
      
text=input("please enter your text:\n")
check(text)