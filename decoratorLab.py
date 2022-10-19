
txt = str
def document_it(fun):
    def wrapper(*args,**kwargs):
         if type(txt) == str and len(txt) > 5 :
           print(txt)
         return fun
    return wrapper()

@document_it
def check(txt):
    if txt != str or len(txt)<5 :
           raise ValueError ("user the arguments should be str and it should have more than 5 characters.")
    else:
      print(txt)
          

check("txt")



