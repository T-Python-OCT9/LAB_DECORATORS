#definig a decorator function
def document_it(func):

    def wrapper(*args, **kwargs):
        print("Documenting the function, name : ", func.__name__)
        print(1+1)
        return func(*args, **kwargs)
    
    return wrapper

#using a decorator
@document_it
def greet(name , age):
    print("Welcome ! ", name)
    
@document_it
def welcom(firstName, city):
    print("Another welcom", firstName)



greet(name = "ahemd", age = 34)
welcom("Mona", "Jeddah")