print ("==============================================================================")

#Addition function
def add(a,b):
    result = a+b
    print (result)

#Subtract function
def sub(a,b):
    result = a-b
    print (result)

#Multiply function
def mul(a,b):
    result = a*b
    print (result)

#Divide function
def div(a,b):
    result = a/b
    rounded = round(result, dp)
    print (rounded)

#percentage function
def per(a,b):
    result = (100/a)*b
    rounded = round (result, dp)
    print (rounded, "%")

#power function
def power(a,b):
    result = a**b
    print (result)

#User input variables and operation input receiver
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
op=input("Enter the operation (+, /, *, -, ^, %): ")

#percentage function decimal place input receiver
if op=="%":
    dp = int(input("How many decimal places should the percentage value have? Type here: "))

#devision function decimal place input receiver
if op=="/":
    dp = int(input("How many decimal places should the division value have? Type here: "))

#Logic. functions called here
if op=="+":
    add (a,b)
    
elif op=="-":
    sub (a,b)
    
elif op=="/":
    div (a,b)

elif op=="*":
    mul (a,b)
    
elif op=="%":
    per (a,b)

elif op=="^":
    power (a,b)

else:
    print ("Syntax Error!")

print ("==============================================================================")
