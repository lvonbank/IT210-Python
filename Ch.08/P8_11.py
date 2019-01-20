# Levi VonBank

def main():
    try:
        # Prompts the user for file names
        filename = input("Enter a file name: ")
    
        # Opens file.
        inputFile = open(filename , "r")
    
        try:
            letInWord = {}
        
            # Counts the occurrences of words in file 1
            for line in inputFile:
                line = line.lower()
                line = line.rstrip()
                wordList = line.split()
                for word in wordList:
                    word = word.strip('.,?!')
                    add(letInWord, word)
            
            # Prints out keys with word in alphabetical order
            for key in sorted(letInWord):
                print(key)
                print('-' * 8)
                wordset = letInWord[key]
                for word in sorted(wordset):
                    print(word)
                print()

        finally:
            # Close file on completion
            inputFile.close()

    except IOError:
        print('Error: file not found')

## Adds words to a dictionary with corresponding characters
# @parm is given the intended dictionary to affect
# @word is given a word to iterate over and add
def add(dictionary, word):
    for char in word:
        if char in dictionary:
            wordset = dictionary[char]
            wordset.add(word)
        else:
            wordset = set([word])
            dictionary[char] = wordset
            
main()