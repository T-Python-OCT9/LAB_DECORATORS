import string
from xml.dom.minidom import Document

def document_it(text):

   def fun1(text):
      if len(text) > 5 and type(text) == string():
         print("OK",text.__name__)
         return text()
      else:
         raise ValueError("the arguments should be str and it should have more than 5 characters")

   return fun1        

@document_it 
def fun2(name):
    print(name) 
    

fun2("SaraAhmad")  

