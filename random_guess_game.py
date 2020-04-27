# Importing sys to enable it run in the terminal
import sys
import random


def guess_game(guess, ans):
    try:
        if 0 < guess < 11:
            if guess == ans:
                print("Great you guessed right.\n Congratulations!!!!!")
                return True
            elif guess > ans:
                print("Your guess is to high")
            else:
                print("Your guess is to low")
        else:
            print(f'I said from {sys.argv[1]}-{sys.argv[2]}, dummy!!!')
            return False
    except (TypeError, AssertionError) as typ:
        print(f"{typ} is not a number")


if __name__ == '__main__':
    ans = random.randint(int(sys.argv[1]), int(sys.argv[2]))

    while True:
        try:
            guess = int(input(f"Guess a number from {sys.argv[1]}-{sys.argv[2]}: "))
            if guess_game(guess, ans):
                break
        except (ValueError, TypeError, AssertionError) as ve:
            print(f"{ve} is not a number")
            continue
