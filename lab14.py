# LAB_DECORATORS
def document_it(func):

    def wrapper(*args, **kwargs):

        for x in (args):
            if not (isinstance(x,str) and len(x) > 5):
                raise ValueError("the arguments should be str and it should have more than 5 characters .")
        for x in (kwargs):
            if not (isinstance(x,str) and len(x) > 5):
                raise ValueError("the arguments should be str and it should have more than 5 characters .")
        return func(*args, **kwargs)
    
    return wrapper

def fun_name(name : str):
    print("Your name is: " + name)

decorated_fun_name = document_it(fun_name)
decorated_fun_name("Mohammed")



