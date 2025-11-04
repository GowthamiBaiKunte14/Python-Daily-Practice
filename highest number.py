'''num1=100
num2=200
if num1>num2:
    print("the highest number is", num1)
else:
    print("the highest number is",num2)'''

# among three variables
num1 = 15
num2 = 10
num3 = 5
if num1 > num2:
    if num1 > num3:
        print(f"{num1} is highest")
    else:
        print(f"{num3} is highest")
else:
    if num2 > num3:
        print(f"{num2} is highest")
    else:
        print(f"{num3} is highest")

# among four variables
num1 = 15
num2 = 10
num3 = 5
num4 = 7
if num1 > num2 and num1 > num3 and num1 > num4:
    print('num1 is highest')
elif num2 > num3 and num2 >num4:
    print('num2 is highest')
elif num3 > num4:
    print('num3 is highest')
else:
    print('num4 is highest')

