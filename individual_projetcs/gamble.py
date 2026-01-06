import random
import time
import os
import sys

#!/usr/bin/env python3
"""
Terminal Casino — fun, text-based gambling mini-game.
Save as lists.py and run: python lists.py

Features:
- Start with chips, choose games: Slots, Dice, High Card
- Simple ASCII art and animations
- Betting, payouts, win/lose messages
"""


STARTING_CHIPS = 100
SLEEP_SHORT = 0.15
SLEEP_LONG = 0.5

SLOT_SYMBOLS = ["🍒", "🍋", "🔔", "⭐", "7️⃣", "🍊"]
SLOT_PAYOUTS = {
    ("7️⃣", "7️⃣", "7️⃣"): 50,
    ("⭐", "⭐", "⭐"): 20,
    ("🔔", "🔔", "🔔"): 10,
    ("🍒", "🍒", "🍒"): 5,
}

HEADER = r"""
  ____              _       ____                 
 / ___|  __ _ _ __ | | __  / ___|  ___ __ _ _ __  
 \___ \ / _` | '_ \| |/ /  \___ \ / __/ _` | '_ \ 
  ___) | (_| | | | |   <    ___) | (_| (_| | | | |
 |____/ \__,_|_| |_|_|\_\  |____/ \___\__,_|_| |_|
            Terminal Casino - Good luck!
"""

def clear_screen():
    # Best-effort cross-platform clear
    os.system('cls' if os.name == 'nt' else 'clear')

def prompt_bet(chips):
    while True:
        try:
            bet = input(f"Place your bet (1 - {chips}, or 'q' to cancel): ").strip().lower()
            if bet == 'q':
                return 0
            bet = int(bet)
            if 1 <= bet <= chips:
                return bet
        except ValueError:
            pass
        print("Invalid bet. Try again.")

def pause():
    input("\nPress Enter to continue...")

def print_header(chips):
    clear_screen()
    print(HEADER)
    print(f"Chips: {chips}\n")

def animate_slots(result):
    # Show spinning animation then final result
    rows = 3
    cols = 3
    for step in range(8):
        frame = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(random.choice(SLOT_SYMBOLS))
            frame.append(" ".join(row))
        clear_screen()
        print(HEADER)
        print("\n-- SLOTS --\n")
        print("\n".join(frame))
        time.sleep(SLEEP_SHORT)
    clear_screen()
    print(HEADER)
    print("\n-- SLOTS --\n")
    for r in result:
        print(" ".join(r))
    print()

def play_slots(chips):
    print("\nWelcome to the Slot Machine!")
    bet = prompt_bet(chips)
    if bet == 0:
        return chips
    # spin
    rows, cols = 3, 3
    result = [[random.choice(SLOT_SYMBOLS) for _ in range(cols)] for _ in range(rows)]
    animate_slots(result)
    # Check middle row for matching 3
    middle = tuple(result[1])
    payout_multiplier = SLOT_PAYOUTS.get(middle, 0)
    # small win for any horizontal triple
    if payout_multiplier == 0:
        # check diagonals or other triples (optional small payouts)
        if len(set(result[0])) == 1:
            payout_multiplier = 2
        elif len(set(result[2])) == 1:
            payout_multiplier = 2
        elif len(set(result[1])) == 1:
            payout_multiplier = 3
    if payout_multiplier > 0:
        win = bet * payout_multiplier
        chips += win
        print(f"JACKPOT! You won {win} chips (x{payout_multiplier}).")
    else:
        chips -= bet
        print(f"No win. You lost {bet} chips.")
    pause()
    return chips

def play_dice(chips):
    print("\nDice Roll — Bet on HIGH (8-12) or LOW (2-6). 7 is house win!")
    bet = prompt_bet(chips)
    if bet == 0:
        return chips
    choice = ""
    while choice not in ("high", "low"):
        choice = input("Choose 'high' or 'low': ").strip().lower()
    print("Rolling two dice...")
    time.sleep(SLEEP_SHORT)
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    total = d1 + d2
    print(f"Dice: [{d1}] + [{d2}] = {total}")
    # Evaluate
    if total == 7:
        # house wins
        chips -= bet
        print("7 rolled — House wins!")
    elif total >= 8:
        outcome = "high"
    else:
        outcome = "low"
    if total != 7:
        if outcome == choice:
            win = bet
            chips += win
            print(f"You guessed {choice}. You win {win} chips!")
        else:
            chips -= bet
            print(f"You guessed {choice}. You lose {bet} chips.")
    pause()
    return chips

def draw_card():
    ranks = list(range(2, 11)) + ["J","Q","K","A"]
    suits = ["♠","♥","♦","♣"]
    r = random.choice(ranks)
    s = random.choice(suits)
    return str(r) + s, rank_value(r)

def rank_value(rank):
    if rank == "J": return 11
    if rank == "Q": return 12
    if rank == "K": return 13
    if rank == "A": return 14
    return int(rank)

def play_high_card(chips):
    print("\nHigh Card — Draw against the dealer. Higher card wins.")
    bet = prompt_bet(chips)
    if bet == 0:
        return chips
    print("Drawing cards...")
    time.sleep(SLEEP_SHORT)
    player_card, player_val = draw_card()
    dealer_card, dealer_val = draw_card()
    # ensure not exact same combination too often (optionally reroll equal)
    print(f"You:   {player_card}  ({player_val})")
    print(f"Dealer:{dealer_card}  ({dealer_val})")
    if player_val > dealer_val:
        chips += bet
        print(f"You win! Gained {bet} chips.")
    elif player_val < dealer_val:
        chips -= bet
        print(f"You lose! Lost {bet} chips.")
    else:
        print("Tie! Push, no chips exchanged.")
    pause()
    return chips

def main():
    chips = STARTING_CHIPS
    while True:
        print_header(chips)
        print("Choose a game:")
        print("1) Slots")
        print("2) Dice (High/Low)")
        print("3) High Card")
        print("4) Quit")
        choice = input("\nEnter choice: ").strip()
        if choice == "1":
            chips = play_slots(chips)
        elif choice == "2":
            chips = play_dice(chips)
        elif choice == "3":
            chips = play_high_card(chips)
        elif choice == "4":
            print("\nThanks for playing. Cashing out...")
            time.sleep(SLEEP_SHORT)
            break
        else:
            print("Invalid choice.")
            time.sleep(SLEEP_SHORT)
        if chips <= 0:
            print_header(chips)
            print("You ran out of chips! Game over.")
            break
    print(f"\nFinal chips: {chips}\nGoodbye!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Goodbye.")
        sys.exit(0)