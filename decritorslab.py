# this is Decorators lab - 18 oct - ghadah alahrbi 

from pickle import TRUE


def docurat_it(func):

    def wrapper(args):
        try:
            x = args
            if x.isdigit()==False  and len(x) ==5 :
                print("Thank you , you entered the right number :) ")
            else: 
                raise ValueError
        except ValueError:
            print("it should be a string and with 5 char only ")
        
        return func(args)
    return wrapper

@docurat_it
def userinput(x):
    return x


userinput(input("enter : "))



