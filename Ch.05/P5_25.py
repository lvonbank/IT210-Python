# Levi VonBank

def main():
    userInput = input("Please input a five-digit zip code: ")
    print(printBarCode(userInput))

## Returns the digit sent back as a bar code
# @parm d it takes a digit and determines its specific bar code
# @return bar code for a digit
def printDigit(d):
    if d == 1: return ":::||"
    if d == 2: return "::|:|"
    if d == 3: return "::||:"
    if d == 4: return ":|::|"
    if d == 5: return ":|:|:"
    if d == 6: return ":||::"
    if d == 7: return "|:::|"
    if d == 8: return "|::|:"
    if d == 9: return "|:|::"
    if d == 0: return "||:::"

## Obtains a zip code and turns it in bar code
# @parm zipCode it calculates the total and obtains individual bar codes
# @return send back a complete bar code of a zip code
def printBarCode(zipCode):
    num = zipCode
    length = len(num)
    total = 0
    frame = "|"
    barCode = frame
    if not num.isdigit() or length < 5 or length > 5:
        return "This is not a valid five-digit zip code"
    for i in range(length):
        digit = int(num[i])
        total += digit
        barCode += printDigit(digit)
    checkDigit = printDigit(((total) * 9) % 10)
    end = checkDigit + frame
    return barCode + end

main()