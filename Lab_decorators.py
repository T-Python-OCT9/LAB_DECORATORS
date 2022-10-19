from ast import arg


def document_it(argument : str):
    def wrapper (*args , **kwargs):
        if len(text) >= 5 and type(text) == str :
            print ("what u typed is string and more then 5 ")
            return argument (*args,**kwargs)
        else:  not len(text) >= 5 and not type(text) == str 
        return argument(*args,**kwargs)
    return wrapper

@document_it
def  check_string_type (text: str) :
    print ("is less then 5 and type is not string")

text = str(input(" please enter your text : "))
try :
    check_string_type(text)
except ValueError:
    print ("the value u entered should be str and more then 5 characters")
        
        

    





