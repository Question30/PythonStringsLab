#Ask the user to enter a word.
word = input("Enter a word: ")
#Print the length of the word
print("Length of word:", len(word))
#Print the word in uppercase and lowercase
print("Uppercase:", word.upper())
print("Lowercase:", word.lower())
#Ask the user to enter a letter abd count how many times that letter appears in the word
letter = input("Enter a letter:")
print(letter + " appears " , int(word.count(letter)), " time(s) in " + word )
#Ask the user to enter a starting and ending index, and then slice the word and print the result
startIndex = input("Enter a starting index:")
endIndex = input("Enter an ending index:")
print("Sliced word:", word[int(startIndex):int(endIndex)])
#Ask uset to enter a character and replace the first occurance of that character with another character
character = input("Enter a character to replace:")
replacement = input("Enter the replacement character:")
print("Replaced:", word.replace(character, replacement))
#Concatenate the origional word with a second word entered by the user
word2 = input("Enter a second word:")
print("Concatenated:", word + word2)
#Check if the orgional word is a palindrome
answer = "No"
if(word == word[::-1]):
    answer = "Yes"

print("Is a palindrome?", answer)

#Check if the original word is a valid Python identifier
answer = "No"
if(word.isidentifier()):
    answer = "Yes"

print("Is a valid Python identifier?", answer)