from pickle import TRUE

def document_it(func):
    def wrapper(*args):
        try:
            for x in (args):
                if len(args) >= 5 and type(args) == str:
                    print("== len(5) and == type")
                elif not len(args) >= 5  and not type(args) == str:
                    print("!== len(5) and !== type")
            raise ValueError 
        except ValueError("then not 5 characters"):
            return func(args)
    return wrapper

@document_it
def userinput(x):
    return x

userinput(input("enter characters: "))
