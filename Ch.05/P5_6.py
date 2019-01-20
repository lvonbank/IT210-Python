# Levi VonBank

def main():
    userInput = input("Please enter a string: ")
    print("There is %s vowels in this string." % countVowels(userInput))

## Returns a count of all vowels
# @parm string it turns a string into a count of vowels
# @return send back a count of the vowels
def countVowels(string):
    vowels = 0
    for char in string:
        if char.lower() in "aeioe" :
            vowels += 1
    return vowels

main()