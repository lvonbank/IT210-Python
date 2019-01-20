# Levi VonBank

# Produces a list of [1,2,3,...10]
listA = []
for i in range(1,11):
    listA.append(i)

# Produces a list of [2,4,6,...20]
listB = []
for i in range(0,22,2):
    listB.append(i)

# Produces a list of [1,4,9,...100]
listC = []
for i in range(1,11):
    listC.append(i*i)

# Produces a list of [0,...0]
listD = []
for i in range(10):
    listD.append(0)

# Produces a list of [1, 4, 9, 16, 9, 7, 4, 9, 11]
listE = []
for i in range(1,5):
    listE.append(i*i)
for i in range(9,6,-2):
    listE.append(i)
listE.append(listE[1])
for i in range(9,12,2):
    listE.append(i)

# Produces a list of [0,1,0,...0]
listF = []
for i in range(0,11):
    if i % 2 == 1:
        listF.append(1)
    else: listF.append(0)

# Produces a list of [0,1,2,3,4] * 2
listG = []
for i in range(0,5):
    listG.append(i)
listG += listG

# Prints all generated lists
print("listA", listA)
print("listB", listB)
print("listC", listC)
print("listD", listD)
print("listE", listE)
print("listF", listF)
print("listG", listG)