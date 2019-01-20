# Levi VonBank

## Reads two floating­point numbers and tests whether 
# they are the same up to two decimal places.

number1 = float(input("Enter a floating-point number: "))
number2 = float(input("Enter a floating-point number: "))

if abs(number1 - number2) <= 0.01:
    print("They're the same up to two decimal places")
else:
    print("They're different.")