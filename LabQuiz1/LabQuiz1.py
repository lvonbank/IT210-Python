# Levi VonBank

userInput = input("Enter a string: ")

def middleChar(string):
    position = len(string) // 2 - 1
    if len(string) % 2 == 1:
        result = string[position]
        if result.isdigit:
            return True
    return False

count = len(userInput)
first = str(userInput[0])
last = str(userInput[len(userInput)-1])

if userInput == "":
    print("Nothing there.")
elif count % 2 == 0  and count != 0:
    print("The second character is: %s" % userInput[1])
    if first == last:
        print("Bookends.")
elif count % 2 != 0:
    if middleChar(userInput):
        print("Middle character is a digit.")

print("Done.")