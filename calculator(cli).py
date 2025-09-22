def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return"Error:division By Zero"
    else:
      return x/y
def modulo(x,y):
    return x%y
def exponential(x,y):
    return x**y

print("Simple Calculator")
print("Choose from Options")
print("1.Add(+)")
print("2.Subtrac(-)")
print("3.Multiply(*)")
print("4.Divide(/)")
print("5.Modulo(%)")
print("6.Exponential(^)")
op=input("Enter your choice(+,-,*,/,%,^)= ")
a=int(input("Enter the first number= "))
b=int(input("Enter the second number= "))
if op=="+":
    result=add(a,b)
    print(f"{a}{op}{b}= {result}")
elif op=="-":
    result=subtract(a,b)
    print(f"{a}{op}{b}= {result}")
elif op=="*":
    result=multiply(a,b)
    print(f"{a}{op}{b}= {result}")
elif op=="/":
    result=divide(a,b)
    print(f"{a}{op}{b}= {result}")
elif op=="%":
    result=modulo(a,b)
    print(f"{a}{op}{b}= {result}")
elif op=="^":
    result=exponential(a,b) 
    print(f"{a}{op}{b}= {result}")       
else:
    print("Invalid operator") 
    
     



        