# Two Player Dice Game
# Rule: roll dice (1-6), if 6 -> extra turn, first to reach 100 wins

import random

scores = {"Player 1": 0, "Player 2": 0}
players = ["Player 1", "Player 2"]

current_player_index = 0

while True:
    player = players[current_player_index]
    input(f"\n{player}'s turn. Press Enter to roll dice...")

    roll = random.randint(1, 6)
    print(f"{player} rolled: {roll}")

    scores[player] += roll
    print(f"Total score of {player}: {scores[player]}")

    # Check winner
    if scores[player] >= 100:
        print(f"\n🎉 {player} wins the game!")
        break

    # If roll is not 6, switch player
    if roll != 6:
        current_player_index = 1 - current_player_index
    else:
        print("Got a 6! Play again.")
