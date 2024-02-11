# 1.Reverse Countdown Timer
num =  int(input("Enter a number: "))
for i in range (num, 0, -1):
    print(i)



# 2. Multiplication Table
num = int(input("Enter a number: "))
for i in range (1, 11):
    print(num*i)



# 3.Simple Counter
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    print(i)



# 4.Factorial Calculator
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print(factorial)



# 5.Print Patterns
num= int(input("Enter number of patterns: "))
for i in range (1, num + 1):
    print("*" * i)



# 6.Print Even Numbers
num = int(input("Enter a number: "))
for i in range (1, num, 2):
    print (i+1)



# 7.Print Odd Numbers
num = int(input("Enter a number: "))
for i in range (1, num, 2):
    print (i)



# 8.Sum of Digits
number = int(input("Enter a number: "))
sum = 0
for i in range(1, number + 1):
    sum = sum + i
print(sum)





    
   
