import random

number = random.randint(1, 100)

print("Guess the number between 1 and 100 (Only 3 chances each)")

players = ["Player 1", "Player 2"]
attempts = {}

for player in players:
    print(f"\n{player}'s turn")
    success = False

    for i in range(1, 4):  # only 3 chances
        guess = int(input(f"Attempt {i}: Enter your guess: "))

        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        else:
            print(f"Correct! Guessed in {i} attempts")
            attempts[player] = i
            success = True
            break

    if not success:
        print("Out of chances!")
        attempts[player] = 999  # large number means failed

# Decide winner
if attempts["Player 1"] < attempts["Player 2"]:
    print("\nPlayer 1 wins!")
elif attempts["Player 1"] > attempts["Player 2"]:
    print("\nPlayer 2 wins!")
else:
    print("\nIt's a tie!")

print(f"\nThe correct number was: {number}")