import random

#opening word file
file = open("gistfile1.txt","r")

#Turns the text file into a list and also excluding the '\n' character
lines = [line[:-1] for line in file]

#random index for the word
num = random.randrange(0,3130)

#word being selected randomly
word = lines[num]
word = word.strip().lower()

print("You have 6 rounds to guess the word, good luck!")
for i in range(6):
    print("- - - - - ROUND:", i+1 ," - - - - -")
    print("Guess the word")
    guess = input("")
    guess = guess.lower()
    while guess not in lines:
        print("Guess a valid word")
        guess = input("")
        guess = guess.lower()
    if(guess == word):
        print("You guessed it correctly!\nThe Word is" , word)
        break
    for i in range(4):
        if guess[i] in word:
            print("The word contains",guess[i])
            if word[i] == guess[i]:
                print("The placement of",word[i],"is also correct")
print("- - - GAME OVER - - -")
print("The word is:",word )