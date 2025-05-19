import random   # Import random module to shuffle the deck

class Deck:
    def __init__(self):
        """
        Initialize a standard deck of 52 cards.
        Suits: ♠️, ♣️, ♥️, ♦️
        Ranks: A, 2-10, J, Q, K
        """
        suits = ['♠️', '♣️', '♥️', '♦️']
        self.cards = []

        for i in range(1, 14):      # Loop through ranks 1 to 13
            if i == 1:
                card = 'A'          # Ace
            elif i == 11:
                card = 'J'          # Jack
            elif i == 12:
                card = 'Q'          # Queen
            elif i == 13:
                card = 'K'          # King
            else:
                card = i            # 2–10

            for suit in suits:      # Add current card into the deck
                self.cards.append([suit, card])

        random.shuffle(self.cards)  # Randomly shuffle the deck after all the cards have been added

    def draw_card(self):
        return self.cards.pop()     # Draw the top card from the deck

class Hand:
    def __init__(self):
        """
        Initialize a hand with:
        - cards: list to store dealt cards
        - sum: total score of the hand
        - aces: count of aces valued at 11 (for flexible scoring: 1 or 11)
        """
        self.cards = []
        self.sum = 0
        self.aces = 0

    def add_card(self, card):
        """
        Add a card to the hand and update the hand's score.
        Aces are initially counted as 11, but may be adjusted later.
        """
        self.cards.append(card)
        if card[1] == 'A':
            self.sum += 11
            self.aces += 1
        elif card[1] in ['J', 'Q', 'K']:
            self.sum += 10
        else:
            self.sum += card[1]     # For numeric cards 2–10

        self.adjust_for_aces()      # Adjust if total exceeds 21 and there are aces

    def adjust_for_aces(self):
        """
        Reduce total score by 10 for each ace if the sum exceeds 21.
        This allows an ace to count as 1 instead of 11 when needed.
        """
        while self.sum > 21 and self.aces > 0:
            self.sum -= 10
            self.aces -= 1

    def display(self, owner='Player'):
        """
        Print out all the cards in the hand with the name of the owner.
        """
        print(f"\n{owner}'s cards:", end=' ')
        for card in self.cards:
            print(f'\n{card[0]}{card[1]}', end=' ')
        print()
