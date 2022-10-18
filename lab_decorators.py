'''
Create a decorator that decorates a function with one or more arguments.
This decorator should check that the argument is of type str and the length of the str is more than 5
else raise an exception of type ValueError telling the user the arguments should be str and it should have more than 5 characters .
'''


def valueErrorFunction(theFunction):
    def decorator(*args, **kwargs):
        for i in args:
            if not (isinstance(i, str) and len(i) > 5):
                raise ValueError(
                    'Name must be a tring and more than 5 characters')
        for i in kwargs:
            if not (isinstance(i, str) and len(i) > 5):
                raise ValueError(
                    'Name must be a tring and more than 5 characters')
        return theFunction(*args, **kwargs)
    return decorator


@valueErrorFunction
def baseFunction(name: str):
    pass


try:
    baseFunction(name='fgh')
except ValueError:
    print('Name must be a tring and more than 5 characters')
