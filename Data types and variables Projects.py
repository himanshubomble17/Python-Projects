


# 1.Personal Information System:-

# Initialize empty lists to store user information
names = []
ages = []
emails = []

# Add first user information
print("Enter first user information:")
names += [input("Name: ")]
ages += [input("Age: ")]
emails += [input("Email: ")]

# Add second user information
print("\nEnter second user information:")
names += [input("Name: ")]
ages += [input("Age: ")]
emails += [input("Email: ")]

# Display user information
print("\nUser Information:")
print(f"\nUser 1:")
print(f"Name: {names[0]}")
print(f"Age: {ages[0]}")
print(f"Email: {emails[0]}")

print(f"\nUser 2:")
print(f"Name: {names[1]}")
print(f"Age: {ages[1]}")
print(f"Email: {emails[1]}")




# 2.Simple Calculator

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
 
print("The addition is: ", a+b)
print("The subtraction is: ", a-b)
print("The multiplication is: ", a*b)
print("The divison is: ", a/b)



# 3.Currency Converter 

usd_to_eur_rate = 0.0
usd_to_gbp_rate = 0.0
amount_usd = 0.0
amount_eur = 0.0
amount_gbp = 0.0

# Get user input for exchange rates
usd_to_eur_rate = float(input("Enter USD to EUR exchange rate: "))
usd_to_gbp_rate = float(input("Enter USD to GBP exchange rate: "))

# Get user input for amount in USD
amount_usd = float(input("Enter amount in USD: "))

# Convert USD to EUR and GBP
amount_eur = amount_usd * usd_to_eur_rate
amount_gbp = amount_usd * usd_to_gbp_rate

# Display converted amounts
print("\nCurrency Conversion:")
print(f"Amount in USD: {amount_usd} USD")
print(f"Amount in EUR: {amount_eur} EUR")
print(f"Amount in GBP: {amount_gbp} GBP")


# 4.Student Gradebook

print("Fill the following fo Student 1: ")
Name = input("Enter Student name: ")

Subject1 = input("Enter Subject 1: ")
Subject2 = input("Enter Subject 2: ")
Subject3 = input("Enter Subject 3: ") 
Subject4 = input("Enter Subject 4: ")

Grades1 = float(input("Enter Grades for Subject 1: "))
Grades2 = float(input("Enter Grades for Subject 2: "))
Grades3 = float(input("Enter Grades for Subject 3: "))
Grades4 = float(input("Enter Grades for Subject 4: "))

Avg = (Grades1 + Grades2 + Grades3 + Grades4) / 4

print("\nStudent name:", Name)
print("Subjects: ", Subject1, Subject2, Subject3, Subject4)
print("Grades: ", Grades1, Grades2, Grades3, Grades4)
print("Average:", Avg)  

print("Fill the following fo Student 2: ")
Name = input("Enter Student name: ")

Subject1 = input("Enter Subject 1: ")
Subject2 = input("Enter Subject 2: ")
Subject3 = input("Enter Subject 3: ") 
Subject4 = input("Enter Subject 4: ")

Grades1 = float(input("Enter Grades for Subject 1: "))
Grades2 = float(input("Enter Grades for Subject 2: "))
Grades3 = float(input("Enter Grades for Subject 3: "))
Grades4 = float(input("Enter Grades for Subject 4: "))

Avg = (Grades1 + Grades2 + Grades3 + Grades4) / 4

print("\nStudent name:", Name)
print("Subjects: ", Subject1, Subject2, Subject3, Subject4)
print("Grades: ", Grades1, Grades2, Grades3, Grades4)
print("Average:", Avg)


# 5.Expense Tracker

food = 0.0
transportation = 0.0
entertainment = 0.0
other = 0.0
total_expenses = 0.0
expense_count = 0

# Get user input for the first expense
category1 = input("Enter expense category (food, transportation, entertainment, other): ")
amount1 = float(input("Enter expense amount: "))
date1 = input("Enter expense date (YYYY-MM-DD): ")

# Update category totals and overall total for the first expense
total_expenses += amount1
expense_count += 1

# Get user input for the second expense
category2 = input("Enter expense category (food, transportation, entertainment, other): ")
amount2 = float(input("Enter expense amount: "))
date2 = input("Enter expense date (YYYY-MM-DD): ")

# Update category totals and overall total for the second expense
total_expenses += amount2
expense_count += 1

# Display summary of expenses
print("\nExpense Summary:")
print(f"Food: ${food}")
print(f"Transportation: ${transportation}")
print(f"Entertainment: ${entertainment}")
print(f"Other: ${other}")
print(f"Total Expenses: ${total_expenses}")
print(f"Number of Expenses: {expense_count}")



 