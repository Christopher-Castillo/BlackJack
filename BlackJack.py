import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        if rank in ['Jack', 'Queen', 'King']:
            self.value = 10
        elif rank == 'Ace':
            self.value = 11 
        else:
            self.value = int(rank)

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

class Player:
    def __init__(self):
        self.hand = []
    
    def draw(self,deck):
        self.hand.append(deck.cards.pop())

    def show_hand(self):
        for card in self.hand:
            print(f'{card.rank} of {card.suit}')
 
    def get_hand_value(self):
        hand_value = sum([card.value for card in self.hand])
        num_aces = sum([1 for card in self.hand if card.rank == 'Ace'])
        while hand_value > 21 and num_aces > 0:
            hand_value -= 10
            num_aces -= 1
        return hand_value

deck = Deck()
player = Player()
dealer = Player()

player.draw(deck)
dealer.draw(deck)
player.draw(deck)
dealer.draw(deck)
print("Your hand:")

player.show_hand()
while True:
    choice = input("Do you want to hit or stand? ")
    if choice == 'hit':
        player.draw(deck)
        print("Your hand:")
        player.show_hand()
        if player.get_hand_value() > 21:
            print("Bust! You lost.")
            break
    elif choice == 'stand':
        break

print("Dealer's turn:")
print("Dealer's hand:")
dealer.show_hand()
while dealer.get_hand_value() < 17:
    dealer.draw(deck)
    print("Dealer's hand:")
    dealer.show_hand()
    if dealer.get_hand_value() > 21:
        print("Dealer busts! You won.")
        break


player_hand_value = player.get_hand_value()
dealer_hand_value = dealer.get_hand_value()
if player_hand_value > 21:
    pass 
elif dealer_hand_value > 21:
    print("Dealer busts! You won.")
elif player_hand_value > dealer_hand_value:
    print("You won!")
elif player_hand_value == dealer_hand_value:
    print("It's a tie.")
else:
    print("Dealer won.")    
