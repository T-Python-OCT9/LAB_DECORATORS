def my_decorator(func): 
    ''' this function will check if the positional or keyword arguments are strings and more than 5 characters'''
    def warp(*args,**kwargs):  

        for item in args: # loop for positional arguments
            if not isinstance(item,str): # check if the item in the tuple is not string  
                raise TypeError(f'"{item}" Should Be String') # rasing exsaption if its not string
            elif len(item) <= 5: # check if the item is more than 5 characters 
                raise ValueError(f'"{item}" Should Be More Than 5 Characters') # rasing exsaption if its not more than 5
            else:
                print(f'{item} Is Correct') # if it's string and more than 5 characters

        for key ,value in kwargs.items(): # loop for keyword arguments
            if not isinstance(value,str): # check if the item in the tuple is not string  
                raise TypeError(f'TypeError: "{value}" Should Be String') # rasing exsaption if its not string
            elif len(value) <= 5: # check if the item is more than 5 characters 
                raise ValueError(f'ValueError: "{value}" Should Be More Than 5 Characters') # rasing exsaption if its not more than 5
            else:
                print(f'{value} Is Correct') # if it's string and more than 5 characters

    return warp

@my_decorator
def text(*string):
    pass

try:
    text(name1='khalid', name2='saud')
except (TypeError, ValueError) as e:
    print(e)
else:
    print("The Name checked successfully")
    