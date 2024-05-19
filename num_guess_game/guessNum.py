import random

target = random.randint(1,100)
guesses = []
num_guess = 1
print("Guess an integer number between 1 and 100: ")
guess = int(input())
guesses.append(guess)
if guess > target:
    print("Guess a lower number\n")
elif guess > 100 or guess < 1:
    print("Guess out of bounds, guess number between 1 and 100")
else:
    print("Guess a higher number\n")
print("Guesses so far:",guesses)
while guess != target:
    num_guess = num_guess + 1
    print("Guess an integer number between 1 and 100: ")
    guess = int(input())
    guesses.append(guess)
    if guess == target:
        break
    elif guess > target:
        print("Guess a lower number")
    elif guess > 100 or guess < 1:
        print("Guess out of bounds, guess number between 1 and 100")
        continue
    else:
        print("Guess a higher number")
    print("Guesses so far:",guesses,"\n")
msg = "You won!\nYou guessed"
msg += f" {num_guess} time" if num_guess == 1 else f" {num_guess} times"

print(msg)