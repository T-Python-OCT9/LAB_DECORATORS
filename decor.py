
def document_it(func):

    def wrapper(*args, **kwargs):
        print("Documenting the function, name : ", func.__name__)
        for arg in args:
            if not (isinstance(arg,str)and len(arg)>5):
                raise ValueError("value should be string and it should have more than 5 characters")
        for kw in kwargs:
            if not (isinstance(kw,str)and len(kw)>5):
                raise ValueError("value should be string and it should have more than 5 characters")

        
        return func(*args, **kwargs)
    
    return wrapper

@document_it
def func_str(strr,strr2):
    print("Welcome ! ", strr,strr2)



name1 = "Nourah"
name2 = "Alqahtani"
try:
    func_str(name1,name2)
except ValueError as e:
    print(e)




