import os
import random

decks = input("Enter number of decks to use: ")
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*(int(decks)*4)

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = 'J'
        if card == 12:card = 'Q'
        if card == 13:card = 'K'
        if card == 14:card = 'A'
        hand.append(card)
    return hand

def play_again():
    again = input("Do you want to lose more money? (Y/N) : ").lower()
    if again == 'y':
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*(int(decks)*4)
        game()
    elif again == 'n':
        print("Adios idiota!")
        exit()
    else:
        print("Invalid input, idiot!")
        exit()

def total(hand):
    total = 0
    for card in hand:
        if card == 'J' or card == 'Q' or card == 'K':
            total += 10
        elif card == 'A':
            if total >=11: 
                total += 1
            else:
                 total += 11
        else: 
            total += card
    return total

def hit(hand):
    card = deck.pop()
    card = deck.pop()
    if card == 11:card = 'J'
    if card == 12:card = 'Q'
    if card == 13:card = 'K'
    if card == 14:card = 'A'
    hand.append(card)

    return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer_hand, player_hand):
    clear()

    print("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congrats! You've got a BJ!\n")
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Haha, you're fucked! The dealer got a BJ\n")
        play_again()


def score(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congrats! You've got a BJ!\n")
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Haha, you're fucked! The dealer got a BJ\n")
        play_again()
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Haha, you're busted! Loser!\n")
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("The dealer is a moron! You win!\n")
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Your cards are shit! You lose!\n")
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("You win this time!\n")


def game():
    choice = 0
    clear()
    print("Welcome to Trudes' BlackJack table!\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print("The dealer is showing a " + str(dealer_hand[0]))
    print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
    blackjack(dealer_hand, player_hand)

    quit = False

    while not quit:        
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        clear()
        if choice == 'h':
            hit(player_hand)
            print("The dealer is showing a " + str(dealer_hand[0]))
            print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
            if total(player_hand) > 21:
                print("Haha, you busted! Loser!")
                play_again()            
        elif choice == 's':
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            score(dealer_hand, player_hand)
            play_again()
        elif choice == 'q':
            print("Adios!")
            quit = True
            exit()
        else:
            print("Invalid input, idiot!")


if __name__ == "__main__":
    game()