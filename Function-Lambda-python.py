



#-----------------------
#---------- Function => Lamda-------
#---------- Anonymous Function------ 
#------------------------
# [1] It Has no Name
# [2] you can call it inline without defining it
# [3] you can use it in Return Data from another Function
# [4] Lamda used for Simple Functions and Def Handle the Large Tasks
# [5] Lamda Is One Single expression not Block of Code
# [6]  Lamde Type is Function
#----------------------------------------

# one Way

def say_hello(name) :
    return f"Hello {name}"

print(say_hello("Salar")) # Hello Salar

# seconde Way

def say_hello(name) : return f"Hello {name}" 
print(say_hello("Salar")) # Hello Salar
print(say_hello.__name__) # say_hello

hello = lambda name : f"Hello {name} "
print(hello("Salar Issa")) # Hello Salar Issa
print(hello.__name__) # <lambda>



def say_hello(name , age) : return f"Hello {name} and your age is {age} :" 
print(say_hello("Salar" , 27)) # Hello Salar and your age is 27 :
print(say_hello.__name__) # say_hello


hello = lambda name , age : f"Hello {name} and your is {age} :  "
print(hello("Salar Issa" , 27)) # Hello Salar Issa and your is 27 :
print(hello.__name__) # <lambda>

print(type(hello)) # <class 'function'>
