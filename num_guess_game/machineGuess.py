import math

print("Make the computer guess a number between 1 and 100!")
target = int(input())
if target > 100 or target < 1:
    print("Number must be between 1 and 100")
while target > 100 or target < 1:
    target = int(input())
    print("Number must be between 1 and 100")
print("We're making the computer guess your number,",target)
num_guess = 1
low = 1
high = 100
guess = (high + low) // 2
print("Computer Guessed:",guess)
if guess == target:
    print("Computer guessed correctly!")
    print(f"Computer guessed {num_guess} time")
while guess != target:
    if guess > target:
        high = guess
        guess = math.ceil((high + low) // 2)
    else:
        low = guess
        guess = math.floor((high + low) // 2)
    print("Computer Guessed:",guess)
    num_guess = num_guess + 1

print("Computer guessed correctly!")
print(f"Computer guessed {num_guess} times")

        


