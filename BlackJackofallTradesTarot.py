import random

# Define the deck of cards
suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
minor_arcane_cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Knight', 'Page', 'Queen', 'King']  # Additional cards for minor arcane
minor_arcane_suits = ['Wands', 'Swords', 'Pentacles', 'Cups']

# Create the normal deck
deck = [(card, suit) for suit in suits for card in cards]

# Create the minor arcane deck
minor_arcane_deck = [(card, suit) for suit in minor_arcane_suits for card in minor_arcane_cards]

# Define the value of each card
card_value = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Knight': 10, 'Page': 10}

# Define the function to calculate the value of a hand
def hand_value(hand):
    value = sum(card_value[card] for card, suit in hand)
    num_aces = sum(1 for card, suit in hand if card == 'Ace')

    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1

    return value

# Define the function to play the game
def play_game():
    global scores  # Make 'scores' global to update it within the function
    # Shuffle the decks
    random.shuffle(deck)
    random.shuffle(minor_arcane_deck)

    # Deal the cards
    player_hands = [[] for _ in range(num_players)]
    dealer_hand = []

    for _ in range(2):
        for i in range(num_players):
            choice_deck = random.choice([deck, minor_arcane_deck])
            card = choice_deck.pop()
            player_hands[i].append(card)

        choice_deck = random.choice([deck, minor_arcane_deck])
        card = choice_deck.pop()
        dealer_hand.append(card)

    # Play the game
    for i in range(num_players):
        while True:
            print(f'Player {i+1} hand: {player_hands[i]}')
            print(f'Dealer hand: [{dealer_hand[0]}, ?]')
            print(f'Player: {hand_value(player_hands[i])}, Dealer: {hand_value([dealer_hand[0]])}', end=', ')
            if hand_value(player_hands[i]) > 21:
                print(f'Player {i+1} busts!')
                break
            elif input('Hit or stand? ').lower() == 'hit':
                choice_deck = random.choice([deck, minor_arcane_deck])
                card = choice_deck.pop()
                player_hands[i].append(card)
                if player_hands[i][-1][0] in cards or player_hands[i][-1][0] in minor_arcane_cards:
                    if hand_value(player_hands[i]) > 21:
                        card_value[player_hands[i][-1][0]] = -card_value[player_hands[i][-1][0]]
            else:
                break

        print(f'Player {i+1} hand: {player_hands[i]}')
        print(f'Dealer hand: {dealer_hand}')
        print(f'Player: {hand_value(player_hands[i])}, Dealer: {hand_value(dealer_hand)}')

    # Play the dealer's turn
    while hand_value(dealer_hand) < 17:
        choice_deck = random.choice([deck, minor_arcane_deck])
        card = choice_deck.pop()
        dealer_hand.append(card)

    print(f'Dealer hand: {dealer_hand}')
    print(f'Player: {hand_value(player_hands[i])}, Dealer: {hand_value(dealer_hand)}')

    # Check the result
    if hand_value(dealer_hand) > 21:
        print(f'Dealer busts! Player {i+1} wins! - Player {i+1} Score: {scores[i]+1}')
        scores[i] += 1
    elif hand_value(dealer_hand) < hand_value(player_hands[i]):
        print(f'Player {i+1} wins! - Player {i+1} Score: {scores[i]+1}')
        scores[i] += 1
    elif hand_value(dealer_hand) > hand_value(player_hands[i]):
        print(f'Dealer wins! Player {i+1} loses! - Dealer Score: {scores[num_players]+1}')
        scores[num_players] += 1
    else:
        print(f'Tie!')
    print(f'Scores: {scores}')

# Define the number of players
num_players = int(input('Enter the number of players (1-3): '))

# Play the game
scores = [0 for _ in range(num_players+1)]
while True:
    play_game()
    if any(score >= 10 for score in scores):
        break
    input('Press enter to continue...')
    print()

print('Game over!')
