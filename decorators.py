
def check (Function):
    def document_it(*args):
        for i in args:
            if (isinstance(i, str) and len(i) > 5):
                raise ValueError('Name must be a string and more than 5 characters')      
        return Function(*args,)
    return document_it


@check
def strname(name: str):
  return name 


try:
    strname(name='Razan')
except ValueError:
    print('Name must be a tring and more than 5 characters')