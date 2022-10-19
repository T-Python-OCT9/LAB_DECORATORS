# Create a decorator that decorates a function with one or more arguments.

def document_it(func):
    '''this function will reiceve the text and heck that the argument is of type str and the length of the str is more than 5 '''
    for text in args:
        if not isinstance(text, str):
            raise TypeError(f'"{text} The agruments must be a string."')
        elif len(text) <= 5:
            raise ValueError(f'"{text}"The arguments must be more than 5 charcters...')
        else:
            print(f'{text}The arguments is correct !')  
    for key,value in kwargs.text():
        if not isinstance(value, str):
            raise TypeError(f'"Type Error : "{value}the arguments must be a string ,try again !"')   
        elif len(value) <=5:
            raise ValueError(f'ValueError : "{value}" the argument have to be more than 5 charcters')
        else:
            print(f'"{value}" is correct !') 
def text_check(*string):
    pass

try:
    text_check(FirstName ='Samaa' , FName =
    'Nawaf')
except(TypeError, ValueError)as Errors:
    print(Errors) 
else:
    print(" the opration done successfully")       
                                 
'''  def wrapper(*args, **kwargs):
        print("this function name is ", func.__name__)
        return func(*args, **kwargs)
        return wrapper
#use the decorator
@document_it
def some_func():
    print("some operation")
'''