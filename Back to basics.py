#Loops: 

# 1.Calculate the sum of all numbers from 1 to a given number
# initial_num = 0
# num = int(input("Enter a number: "))
# for i in range (num):
#     num = i+num
# print(num)


# 2.Write a program to print multiplication table of a given number
# num = int(input("Enter a number: "))
# for i in range (1, 11):
#     i = i*num
#     print(i)


# 3. Count the total number of digits in a number
# num = int(input("Enter a number: "))
# count = 0

# # Iterate over each digit by converting the number to a string
# for digit in str(num):
#     count += 1

# print("Total digits are:", count)


# 4. Print list in reverse order using a loop
# list1 = [10, 20, 30, 40, 50]
# new_list = reversed(list1)
# for item in new_list:
#     print(item)


# 5. Find the factorial of a given number
# num = int(input("Enter a number: "))
# factorial = 1
# for i in range (1, num + 1):
#     factorial =  factorial*i
# print(factorial)



# Functions

# 1.Write a program to create a function that takes two arguments, name and age, and print their value.
# def func (name, age):
#     print(name, age)
# func("John", 20)


# 2.Function to return addition and substraction from givenn values.
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# def calc(a,b):
#     add = num1+num2
#     sub = num1-num2
#     return add, sub

# res = calc(num1, num2)
# print(res)


# 5.Program to show name and salary of employee
# def show_employee(name, salary=9000):
#     print(f"Employee Name: {name}")
#     print(f"Salary: ${salary}")
# employee_name = input("Enter Name: ")
# employee_salary = int(input("Enter salary: ") or 9000)

# show_employee(employee_name, employee_salary)



# Conditionals
#1. wap to check the give number is above 10 using if.
# a = int(input("Enter a number: "))
# if a > 10:
#     print("Number is above 10")
# else:
#     print("Less than 10")


#2. wap to check value of a is above 50 or not.if yes add it with b
# a =  int(input("Enter a number: "))
# if a > 50:
#     print("Given value is above 50 hence, ")
#     b  = a + 50
#     print("The value is", b)
# else:
#     print("Less than 50")


#3. wap to check the given character is vowel
# a = input("Enter a word: ")
# if a in "aeiou" or "AEIOU":
#     print("A vowel")
# else:
#     print("Other")


#4. wap to check word(string) is starting from vowel or not.(a,e,i,o,u)
# s = input("Enter a string: ")
# vowel = "aeiou"
# if s.startswith(tuple(vowel)):
#     print("String starts with a vowel")
# else:
#     print("Does not starts with a vowel")


#5. wap to check whether string is starting and ending with vowel or not
# s = input("Enter a string: ")
# vowel = "aeiou"
# if s.startswith(tuple(vowel)) and s.endswith(tuple(vowel)):
#     print("String starts and ends with vowels")
# else:
#     print("Does not starts and ends with vowels")


#6. wap to check the number of words in string, if string have more than 5 words then print string is too long.
# s = input("Enter a string: ") 
# length = len(s)
# if length > 5:
#     print("String is too long")
# else:
#     print(length)


#7. wap to check whether the given number is even.
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")


# 8. wap to check the given number is multiple of 5
# num = int(input("Enter a number: "))
# if num % 5 == 0:
#     print("Yes")
# else:
#     print("No")


# 9. check whether the given number is positive or not.
# num = int(input("Enter a number: "))
# if num >= 0:
#     print("Positive")
# else:
#     print("Negative")


# 10. check whether given triangle is right angle triangle or not.
# n1 = int(input("Enter number1: "))
# n2 = int(input("Enter number2: "))
# n3 = int(input("Enter number3: "))
# if n1 == 90 or n2 == 90 or n3 == 90 and n1+n2+n3 == 180:
#     print("Perfect Triangle")


# 11. wap to check whether the word is in upper case or lower case.if upper convert it to lower and if lower convert it to upper.
# word = input("Enter a word: ")
# if word.isupper():
#     print("Lower word is",word.lower())
# else:
#     print("Upper word is",word.upper())


# 12. wap to check a word is starting from vowel or consonent,if consonent then convert it to upper case.
# word = input("Enter a word: ")
# vowel = "AEIOUaeiou"
# if word.startswith(tuple(vowel)):
#     print("Starts with a vowel")
# else:
#     print(word.upper())


# 13. wap to check the given number is even or odd, if even multiply it by 2 else multiply it by 5
# num = int(input("Enter number: "))
# if num %2 == 0:
#     print(num*2)
# else:
#     print(num*5)










