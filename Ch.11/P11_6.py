# Levi VonBank

## 
# Determine wether or not a substring is present in a string using recursion
# 

## Determine wether or not text is in string.
# @parm text the text to search for 
# @parm string the string to search for text
# @parm True if string is in text, False otherwise
#
def find(text, string):
    if text.startswith(string):
        return True
    elif len(string) < len(text):
        return find(text[1: ], string)
    return False

def main():
    # Demonstrate the find function.
    print(find("Mississippi", "sip"))
    print("Expected: True")
    
    print(find("Mississippi", "pip"))
    print("Expected: False")

# Call the main function.
main()