# Levi VonBank

def main():
    userInput = input("Please enter an integer: ")
    numOfDig = numDigits(userInput)
    print("There is %s digit[s] in this integer." % numOfDig)

## Use recursion to determine the number of digits in an integer
# @parm n it takes a number and counts its equivalent digits
# @return is recursion for the quantity of digits
def numDigits(n):
    if n != "":
        num = int(n)
        if num < 10:
            return 1
        else: return numDigits(num // 10) + 1
    return "No"

main()