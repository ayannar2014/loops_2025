# Ask the user for a word.
word = input("Enter a word: ")
vowels =  str (["a", "e", "i", "o", "u"])
count = 0
# Use a for loop to print each letter on a new line.
for letter in word:
     print (letter)
     if vowels in word:
        count += 1
        print (count)

# Challenge:
# Count how many vowels are in the word.