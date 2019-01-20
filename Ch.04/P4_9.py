# Levi VonBank

# Obtains users word
word = input("Please input a word: ")

# Initializes variables
count = len(word)
string = ""

# Concatenates each syllable in reverse
for i in range(count):
    string = string + word[count - 1 - i]

print(string)