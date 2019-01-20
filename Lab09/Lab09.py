# Levi VonBank
# Group Members: Scott Fleming

# Fibonacci Lab

# This is the standard recursive implementation of the fibonacci calculation
def fib1(n):
    global count # These first two statements are only used to count the
    count += 1   # number of recursive calls.
    if n <= 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

#  Build the starting dictionary and then call the function that will recurse
def fibWithHelp(n):
    fibDict = {1:1,2:1}
    return fib2(n,fibDict)

# This version of fib will check to see if n is in the dictionary and if so,
# simply return the value stored there.  If it is not in the dictionary,
# perform the calculation, update the dictionary and return the calculated
# value.
def fib2(n, fibDict):
    global count # These first two statements are only used to count the
    count += 1   # number of recursive calls.
    if n in fibDict:
        return fibDict[n]
    else:
        f1 = fib2(n-1, fibDict)
        f2 = fib2(n-2, fibDict)
        fibDict[n] = f1 + f2
        return f1 + f2

    # Finish writing the code for this implementation.  Ensure that you
    # use fib2 when recursing, not fib1

if __name__ == "__main__":
    for x in (3,10,25,30,35):
        count = 0
        print("fib1(%d): %d.  fib1 was called %d times." % (x, fib1(x), count))
    print()
    for x in (3,10,25,30,35,100,500): # Much larger problems are possible here
        count = 0
        print("fibWithHelp(%d): %d.  fib2 was called %d times." % (x, fibWithHelp(x), count))

