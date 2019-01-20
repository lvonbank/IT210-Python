# Levi VonBank
# Group Members: Scott Fleming 

## P5.30
#  Check whether a password has the required properties.
#

def main() :
   # Read input from the user.
   password1 = input("Enter your password: ")
   password2 = input("Re-enter your password: ")

   # Keep looping until the passwords match and have the desired properties.
   while password1 != password2 or not isValidPassword(password1) :
      print("Passwords didn't match or didn't have the required properties.")

      # Read the next pair of passwords.
      password1 = input("Enter your password: ")
      password2 = input("Re-enter your password: ")

   # Display the final message.
   print("That pair of passwords will work.")

## Determine if a password has the desired properties: >=8 characters long, at
#  least one uppercase letter, at least one lowercase letter and at least one
#  digit.
#  @param password the password to check
#  @return True if all four properties are present, False otherwise
#
def isValidPassword(password) :
    # Initializes starting variables for match, upper, lower, & digit
    match = False
    upper = False
    lower = False
    digit = False
    
    # Determines if the password is the correct length
    if len(password) < 8: return False

    # Checks to see if their is an upper/lowercase letter and a digit     
    for i in range(len(password)):
        if password[i].isupper():
            upper = True
        if password[i].islower():
            lower = True
        if password[i].isdigit():
            digit = True
        if upper and lower and digit:
            match = True
    
    # Retuns findings
    return match

# Call the main function.
main()