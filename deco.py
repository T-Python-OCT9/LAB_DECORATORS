def documentStringfunc(func):
    def wrapper(*args):
        for n in args:
            if isinstance(n,str) and len(n)>5:
              print("The typ of argument is :",type(n), ", length is: ", len(n))      
            else:
              raise ValueError("you must enter string and more than 5 charcters")
        return func(*args)
    
    return wrapper




@documentStringfunc
def nameString(name:str, city)->str:
    print("name is : ",name ,", and your city is : ")

name:str
name=input("write your name : ")
city=input("enter your city name ")


try:
    nameString(name, city)
except ValueError as error:
    print(error)










