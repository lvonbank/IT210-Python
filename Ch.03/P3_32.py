# Levi VonBank

## This is a program which will ask the user for the number of hours 
# they have worked

name = input("Please enter your name: ")
hourlyWage = float(input("Please enter an hourly wage: "))
hours = float(input("Please enter the number of hours: "))

# 150 percent of the hourly wage
bonus = 1.5
paycheck = 0

if hours <= 40:
    paycheck = hourlyWage * hours
elif hours > 40:
    pay = hourlyWage * 40
    overtime = hours - 40
    bonusPay = overtime * hourlyWage * bonus
    paycheck = pay + bonusPay

# Prints paycheck paycheck 
print()
print("%s's total salary is %.2f" %(name, paycheck))