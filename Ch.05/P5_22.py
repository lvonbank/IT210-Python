# Levi VonBank

def main():
    initialBalance = input("Please enter the initial balance: ")
    interestRate = input("Please enter the interest rate (%): ")
    years = input("Please enter the years: ")
    total = interest(initialBalance, interestRate, years)
    print()
    print("The new balance over %s is $%.2f" %(years, total))

## Calculates the interest of an initial balance relative to years
# @parm intBal obtains the initial balance to be calculated
# @parm intRate obtains the interest rate to be calculated
# @parm yrs obtains the years to be calculated
# @return sends back the calculated balance with interest
def interest(intBal, intRate, yrs):
    newBal = float(intBal)
    rate = int(intRate)
    year = int(yrs)
    while year > 0:
        interest = newBal * (rate / 100)
        newBal += interest
        year = year - 1
    return newBal

main()