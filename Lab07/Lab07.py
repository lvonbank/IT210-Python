# Levi VonBank
# Group Members: Scott Fleming & Peter Fischbach 

def main():
    # Obtains strings from the user
    set1 = set(input("Enter a string to be used as set1: "))
    set2 = set(input("Enter a string to be used as set2: "))
    set3 = set(input("Enter a string to be used as set3: "))

    # Determines elements that are in set1 or set2, but not both.
    a = set1.union(set2) - set1.intersection(set2)
    
    # Determines elements only in one of the three sets
    diff1 = set1.difference(set2.union(set3))
    diff2 = set2.difference(set1.union(set3))
    diff3 = set3.difference(set1.union(set2))
    b = set.union(diff1, diff2, diff3)
    
    # Determines elements that are in exactly two of the sets
    intAll = set.intersection(set1, set2, set3)
    int1 = set1.intersection(set2)
    int2 = set2.intersection(set3)
    int3 = set3.intersection(set1)
    c =  set.union(int1, int2, int3) - intAll

    # Prints results
    print('Part A:', makeStr(a))
    print('Part B:', makeStr(b))
    print('Part C:', makeStr(c))

def makeStr(collection):
    string = ""
    for char in sorted(collection):
        string += char
    return string

main()