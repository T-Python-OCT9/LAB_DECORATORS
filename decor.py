def document_it(func):

    def wrapper(*args, **kwargs):
        print("Documenting the function, name : ", func.__name__)
        print(len(*args))
        if type(*args, **kwargs) == str:
            if len(args) > 5:
                print("Documenting the function, name : ", func.__name__)
        return func(*args, **kwargs)
    
    return wrapper

@document_it
def greet(strr,strr2):
    i = len(strr)
    print("Welcome ! ", strr,strr2)

name = "nourah"
name2 = "hyaa"
greet(name,name2)
i = 7




