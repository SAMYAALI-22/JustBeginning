num1=int(input("ENTER A NUMBER:"))
num2=int(input("ENTER A NUMBER:"))
num3=int(input("ENTER A NUMBER:"))

if(num1 >= num2) and (num1 >= num3):
    largest=num1

elif(num2 >= num1) and (num2 >= num3):
    largest=num2

else:
    largest=num3

print("The Largest No. Is",largest)
