
def saud_D(name,):
    print("hello :" +name)
saud_D("ahmed")

@saud_D
def s_input():
    pass    

inpt_ur_age=input("Enter your age : ")

try:
    saud_D
except ValueError:
    print("arguments should be str and it should have more than 5 characters")
