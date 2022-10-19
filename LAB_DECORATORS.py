
'''

## Create a decorator that decorates a function with one or more arguments.
- This decorator should check that the argument is of type str and the length of the str is more than 5 
- else raise an exception of type ValueError telling the user the arguments should be str and it should have more than 5 characters .
 '''
'''
def checkArgument(fun):  
    def wrapper(*args , **kwargs ):
      argumentLength = len(*args , **kwargs)
      print(argumentLength)
      return func(*args, **kwargs)

    
      #n = 0 
    #x = 1
      #i= -1
      #for i in range( argumentLength - 1, -1 , -1 ):
       # if ('0' <= str[i] and str[i] <= '5') :
     #   n = (ord(str[i]) - ord('0') * x + n )
    return wrapper 
@checkArgument
def inputtt (argument :str ):
     print(argument)
'''



def checkArgument(fun) :
    def wrapper (*args , **kwargs ):
        print(args)
        for i in args:
            if isinstance(i,  str ) and len(i) > 5 :
               argumentli =(len(args))
               #if argumentli == 5 :
               return True
            else :

               return False   
        return fun(*args , **kwargs)
    
    return wrapper
    
 

@checkArgument
def greet(name):
    A= "hi"
    b= "wwlcome "
    c= "to"
    d= " the"
    e= "woord "
    

n = greet("mahaaaa")
print(" The number of arguments are 5 or more ? : ", n)

try:
     greet(name)
except ValueError as e:
    print(e)





