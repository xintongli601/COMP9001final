# 🃏 Blackjack Game in Python
## Game Description

Blackjack is a very famous and popular card game at the Casino💰. Players play against the dealer to win money!

You bet money, double it if you win, but lose it if you lose.

How to win?

Get a higher total than the dealer with your cards or simply get a Blackjack (a total of 21)


## User Instructions

This is a simple, command-line version of Blackjack. The user plays against the computer (dealer). 

1. Start the game

2. You're welcomed to the Blackjack table.

3. You can choose to view your past records, the amount previous players have won or lost.

4. Enter your name 

5. Select a difficulty mode:

Easy (E): Dealer plays normally.

Hard (H): Dealer plays more aggressively (keeps drawing if their total is below yours).

6. Buy Chips

You must buy chips in order to play the game. The minimum purchase is $20 because the minimum bet for each hand is $20.

7. Place a Bet

Before each round, you place a bet (minimum $20 and up to your total chips).

8. Card Dealing

Both you and the dealer get two cards.
You can see both of your cards but only one of the dealer's cards is shown, the other is hidden for now.

9. You decide to Hit (H) (draw a card) or Stand (S) (keep your total).
    
If your total is 21 at some point, you win the hand. 
But if your total goes over 21, you bust and lose your bet. 
Don't worry! The program calculates your total for you!
It will always be your turn before you choose to stand or get a total over 21.

10. When you are happy with your total and choose to stand, the dealer draws their cards.

Occasionally, a Lucky Event may occur: You might get a free Ace. (greater possibility to win)

Or an Unlucky Event: The dealer might receive a strong card.

11. The two totals are then compared.

You win by getting a BlackJack (total of 21) or a higher total than the dealer.

11. Result & Chips Update

If you win: you gain the bet amount.

If you lose: you lose the bet.

If it’s a tie: no chips are lost.

12. Keep Playing or Quit

After each round, you can decide to keep playing.

If your chips drop below $20, you can buy more.

13. Game End & Score Saving

If you choose to quit, the game ends.

Your performance (profit or loss) is saved to blackjack_score.txt.

You can view past game records anytime.


