# 1.Odd or Even Number Checker
num = int(input("Enter a number: "))
if (num%2) == 0:
    print("Even Number!")
else:
    print("Odd Number!")



# 2.Positive or Negative Number Checker
num = int(input("Enter a number: "))
if (num>=0):
    print("It's a Positive Number")
else:
    print("It's a Negative number")



# 3.Simple Password Checker
passwd = input("Enter your password: ")
if (len(passwd)>8):
    print("Strong Password")
else:
    print("Weak Password!")



# 4.Basic Calculator
a = int(input("Enter 1st Number: \n"))
b = input("Select an operator +, - , *, %: \n")
c = int(input("Enter 2nd number: \n"))

if (b == "+"):
    print("Addition is: ", a+c)
elif (b == "-"):
    print("Substraction is: ", a-c)
elif (b == "*"):
    print("Multiplication is: ", a*c)
elif (b == "%"):
    print("Divison is: ", a//c)


# 5.Month Name Detector
month = int(input("Enter a number to check month: \n"))
if (month == 1):
    print("January")
elif (month == 2):
    print("February")
elif (month == 3):
    print("March")
elif (month == 4):
    print("April")
elif (month == 5):
    print("May")
elif (month == 6):
    print("June")
elif (month == 7):
    print("July")
elif (month == 8):
    print("August")
elif (month == 9):
    print("September")
elif (month == 10):
    print("October")
elif (month == 11):
    print("November")
elif (month == 12):
    print("December")
else:
    print("Wrong number")


# 6.Basic Age Group Classifier
Age = int(input("Enter your age: \n"))
if (Age<=12):
    print("You are a Child")
elif (Age<=19):
    print("You are a Teenager")
elif (Age>=20):
    print("You are an Adult")
elif (Age>=60):
    print("You are a Senior")


