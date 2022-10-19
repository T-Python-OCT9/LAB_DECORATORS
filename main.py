def string_args(func):

    def wrapper(*args, **kwargs):
        #do the operations needed
        for arg in args:
            if not (isinstance(arg, str) and len(arg) > 5):
                raise ValueError("The arguments should be of type string and has more than 5 characters")

        for kwarg in kwargs.values():
            if not (isinstance(kwarg, str) and len(kwarg) > 5):
                raise ValueError("The arguments should be of type string and has more than 5 characters")

        print("doing an operation")
        return func(*args, **kwargs)
    
    return wrapper



@string_args
def greeting(name , city):
    return f"Name: {name} and from {city}"



try:
    print(greeting("Abdulrahman", city = "Medina"))
except ValueError as e:
    print(e)