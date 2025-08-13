# input value
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
option = int(input("Enter choice (1/2/3/4): "))
if (option in [1,2,3,4]):
    number1 = int(input("Enter the first number"))
    number2 = int(input("Enter the second number"))
    if(option==1):
        result = number1+number2
    elif(option==2):
        result = number1-number2
    elif(option==3):
        result = number1*number2
    elif(option==4):
        result = number1/number2
else:
    print("invalid text")
# output
# Result
print(f"the result of the operation is {result}")


