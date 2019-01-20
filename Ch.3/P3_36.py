# Levi VonBank

# Obtains userinput
userInput = float(input("Please enter a wavelenght value: "))

# Determines the following waves
if userInput > 10**-1:
    print("Radio Waves, Frequency < 3x10^9")
elif userInput > 10**-3 and userInput <= 10**-1:
    print("Microwaves, Frequency 3x10^9 to 3x10^11")
elif userInput > 7*10**-7 and userInput <= 10**-3:
    print("Infrared, Frequency 3x10^11 to 3x10^14")
elif userInput > 4*10**-7 and userInput <= 7*10**-7:
    print("Visable light, Frequency 4x10^14 to 7.5x10^14")
elif userInput > 10**-8 and userInput <= 4*10**-7:
    print("Ultraviolet, Frequency 7.5x10^14 to 3x10^16")
elif userInput > 10**-11 and userInput <= 10**-8:
    print("X-rays, Frequency 3x10^16 to 3x10^19")
else:
    print("Gamma rays, Frequency > 3x10^19")