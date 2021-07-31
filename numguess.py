import random
s = random.randint(1, 99)

print('Guess the number between 1 and 99. You have 6 tries')
tries = 0


guess = 0


while guess != s and tries<6:

    guess = input('What is your guess? ')
    guess = int(guess)

    tries+=1
    if guess>s:
        print('Your guess was too high. That was attempt number' ,tries)

    elif guess < s:
        print('Your guess was too low. That was attempt number' ,tries)

if tries==6:
    print('You have run out of tries. The number was', s)

if guess == s:
    print('You guessed the number!')