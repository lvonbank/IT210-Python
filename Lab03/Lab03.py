# Levi VonBank

# Obtains the money spent
moneySpent = float(input("Please enter the cost of your groceries: "))

# These variables are used to initializest discount, percent, sufficientFunds
discount = 0
percent = 0
sufficientFunds = False

# Determines how much the discount coupon is
if moneySpent > 210:
    discount = moneySpent * 0.14
    percent = "14"
    sufficientFunds = True
elif moneySpent > 150 and moneySpent <= 210:
    discount = moneySpent * 0.12
    percent = "12"
    sufficientFunds = True
elif moneySpent > 60 and moneySpent <= 150:
    discount = moneySpent * 0.10
    percent = "10"
    sufficientFunds = True
elif moneySpent >= 10 and moneySpent <= 60:
    discount = moneySpent * 0.08
    percent = "8"
    sufficientFunds = True

# Determines what is applicable in the print function
if sufficientFunds == True:
    qualification = "win"
    endLine = " of $%.2f. (%s%% of your purchase)" % (discount, percent)
else:
    qualification = "do not qaulify for"
    endLine = "."

print("You %s a discount coupon%s" % (qualification, endLine))