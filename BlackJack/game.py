import time
import random
from deck import Deck, Hand  # Importing custom Deck and Hand classes

class BlackjackGame:
    def __init__(self):
        self.invest = 0
        self.chips = 0
        self.name = ''
        self.difficulty = 'E'

    def get_safe_int(self, prompt, min_value=None, max_value=None):
        # Get a valid integer input from the user 
        while True:
            user_input = input(prompt).strip()
            try:
                value = int(user_input)
                if (min_value is not None and value < min_value):
                    print(f'\nPlease enter a number between {min_value} and {max_value}.')
                    continue
                return value
            except ValueError:
                print('\nInvalid input. Please enter a valid number.')

    def get_player_name(self):
        # Ask the player to enter a nickname
        name = input('\nEnter your nickname: ').strip()
        while not name:
            name = input('\nPlease enter a valid name: ').strip()
        print(f'\nWelcome, {name}! Let\'s play Blackjack.')
        return name

    def choose_difficulty(self):
        """
        Let the player choose between Easy and Hard difficulty.
        Easy: The dealer stops hitting after they get 17 or higher
        Hard: The dealer keeps hitting until they bust or beat the player
        """
        mode = input('\nChoose difficulty: (E)asy or (H)ard? ').strip().upper()
        while mode not in ['E', 'H']:
            mode = input('\nInvalid input. Choose (E)asy or (H)ard: ').strip().upper()
        return mode

    def buy_chips(self):
        # Ask the player to buy chips (minimum $20) and set initial chip count
        self.invest = self.get_safe_int('\nHow much chips would you like to buy? $', min_value=20)
        self.chips = self.invest
        print(f'\nYou have: ${self.chips}, good luck!')
        return True

    def get_yes_no(self, prompt):
        while True:
            answer = input(prompt).strip().upper()
            if answer in ['Y', 'N']:
                return answer
            print('\nInvalid input.')

    def get_hit_or_stand(self, prompt):
        # Ask the player to choose to hit or stand ('H' or 'S')
        while True:
            answer = input(prompt).strip().upper()
            if answer in ['H', 'S']:
                return answer
            print('\nInvalid input. Please enter H or S.')

    def place_bet(self):
        # Let the player place a bet for the current hand
        return self.get_safe_int('\nHow much would you like to bet on this hand? $', min_value=20, max_value=self.chips)

    def lucky_event(self, hand, who='player'):
        # Trigger a random 5% chance, lucky/unlucky event 
        if random.random() < 0.05:
            if who == 'player':
                print('\n🍀 Lucky Event! You received an extra Ace!')
                hand.add_card(['♦️', 'A'])
            else:
                print('\n💥 Unlucky! Dealer got a powerful card.')
                hand.add_card(['♠️', 'K'])

    def save_score(self):
        # Read existing score records and update them with the current game's result
        record = {}
        try:
            with open('blackjack_score.txt', 'r') as f:
                for line in f:
                    if ':' in line:
                        name, score = line.strip().split(':')
                        record[name.strip()] = int(score.strip().strip('$'))
        except FileNotFoundError:
            pass

        # Update the record for this player
        record[self.name] = record.get(self.name, 0) + (self.chips - self.invest)

        # Save updated records back to file
        with open('blackjack_score.txt', 'w') as f:
            for name, score in record.items():
                f.write(f'{name}: ${score}\n')

    def show_history(self):
        # Display the last 10 game records if available
        print('\n📜 Past Game Records:')
        try:
            with open('blackjack_score.txt', 'r') as f:
                records = f.readlines()
                if records:
                    for line in records[-10:]:
                        print(line.strip())
                else:
                    print('\nNo records found.')
        except FileNotFoundError:
            print('\nNo record file found. Play at least one round to generate it.')

    def play_hand(self):
        # Play a single round of Blackjack
        deck = Deck()
        player = Hand()
        dealer = Hand()

        bet = self.place_bet()

        # Deal the cards with a time lag
        for _ in range(2):
            print(f'\nDealing card to {self.name}...')
            time.sleep(2)
            player.add_card(deck.draw_card())

            print('\nDealing card to Dealer...')
            time.sleep(2)
            dealer.add_card(deck.draw_card())

        self.lucky_event(player, 'player')

        player.display(self.name)
        print(f'\nDealer\'s card: {dealer.cards[0][0]}{dealer.cards[0][1]}')

        # Check for blackjack
        if player.sum == 21:
            print('\nBLACK JACK! YOU WIN! 💰')
            self.chips += bet
            return

        # Player's turn to choose to hit or stand
        while player.sum < 21:
            print(f'\n{self.name} has {player.sum}')
            option = self.get_hit_or_stand('\nWould you like to hit or stand? (H/S) ')
            if option == 'H':
                print(f'\nDealing card to {self.name}...')
                time.sleep(2)
                player.add_card(deck.draw_card())
                player.display(self.name)
                if player.sum > 21:
                    print(f'\n{self.name} has {player.sum}')
                    print('\n💥 BUST! YOU LOSE!')
                    self.chips -= bet
                    return
                elif player.sum == 21:
                    print(f'\n{self.name} has {player.sum}')
                    print('\nBLACK JACK! YOU WIN! 💰')
                    self.chips += bet
                    return
            else:
                break

        # Dealer's turn
        print("\nDealer's turn...")
        while dealer.sum < 17 or (self.difficulty == 'H' and dealer.sum < player.sum):
            print('\nDealing card to Dealer...')
            time.sleep(2)
            dealer.add_card(deck.draw_card())
            self.lucky_event(dealer, 'dealer')

        dealer.display('Dealer')
        print(f'\nThe dealer has {dealer.sum}')

        # Determine outcome of the round
        if dealer.sum > 21:
            print('\nDealer bust! YOU WIN! 💰')
            self.chips += bet
        elif dealer.sum == 21:
            print('\nBLACK JACK! YOU LOSE!')
            self.chips -= bet
        elif dealer.sum > player.sum:
            print('\nDealer has a higher hand. YOU LOSE!')
            self.chips -= bet
        elif dealer.sum == player.sum:
            print('\nIt\'s a tie!')
        else:
            print('\nYou have a higher hand! YOU WIN! 💰')
            self.chips += bet

    def play(self):
        # Main game loop
        print('🎰 Welcome to the BlackJack table! 🎲')
        print('\nEach play is $20 minimum, you can bet higher but you can\'t bet lower')

        see = self.get_yes_no('\nWould you like to see past records? (Y/N) ')
        if see == 'Y':
            self.show_history()

        self.name = self.get_player_name()
        self.difficulty = self.choose_difficulty()

        if not self.buy_chips():
            print('\nSorry that you are not playing.\nYou are welcome to come back and play at anytime!')
            return

        while self.chips >= 20:
            self.play_hand()
            print(f'\nYou now have ${self.chips}')
            play = self.get_yes_no('\nWould you like to continue playing? (Y/N) ')
            if play == 'N':
                break
            if self.chips < 20:
                print(f'\nYou only have: ${self.chips}, that is not enough to play.')
                more = self.get_yes_no('\nWould you like to buy more chips? (Y/N) ')
                if more == 'Y':
                    more_chips = self.get_safe_int('\nHow much more would you like to buy? $', min_value=20)
                    self.chips += more_chips
                    self.invest += more_chips
                else:
                    break

        # The game ends and reports
        if self.chips < 20:
            print('\nSorry that you are not playing.\nYou are welcome to come back and play at anytime!')
        else:
            print(f'\n🎉 You walk away with ${self.chips}!')
            if self.chips > self.invest:
                print(f'\nYou have made a profit of ${self.chips - self.invest} today! Congratulations! 🏆')
            else:
                print('\nHope you enjoyed playing!')

        self.save_score()  # Save result to file
