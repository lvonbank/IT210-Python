# Levi VonBank

gradeCounts = {"A": 8, "D": 3, "B": 15, "F": 2, "C": 6}

print("All Keys")
for key in gradeCounts:
    print(key)
print()

print("All Values")
for value in gradeCounts:
    print(gradeCounts[value])
print()

print("All Keys & Values")
for (key, value) in gradeCounts.items():
    print('%s: %s' %(key, value))
print()

print("Keys in Order")
for (key, value) in sorted(gradeCounts.items()):
    print('%s: %s' %(key, value))
print()

print("The Average")
average = 0
total = 0
count = 0
for (key, value) in sorted(gradeCounts.items()):
    total += value
    count += 1
    if count > 0:
        average = total/count
print(average)
print()

print("Asterisks Equivalent")
for (key, value) in sorted(gradeCounts.items()):
    print('%s: %s' %(key, '*' * value))