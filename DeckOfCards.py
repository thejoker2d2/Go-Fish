import random
# A class of a deck of cards
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    # builds the deck with 52 playing cards
    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", 'Hearts']:
            for val in range(2, 15):
                if val == 11:
                    self.cards.append(Card(suit, "Jack"))

                elif val == 12:
                    self.cards.append(Card(suit, "Queen"))

                elif val == 13:
                    self.cards.append(Card(suit, "King"))

                elif val == 14:
                    self.cards.append(Card(suit, "Ace"))

                else:
                    self.cards.append(Card(suit, val))

    # method to show all cards in the deck
    def show(self):
        for c in self.cards:
            c.show()

    # shuffles the deck
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    # pulls a card from the deck
    def drawCard(self):

        if len(self.cards) == 0:
            return 0
        else:
            number = random.randint(0, len(self.cards))
            return self.cards.remove(number)

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print(f"{self.val} of {self.suit}")

class Player:

    def __init__(self):
        self.hand = []

    def draw(self, deck):
        if deck.drawCard() == 0:
            print("No cards left in the deck. \n")
        else:
            self.hand.append(deck.drawCard())
            return self

    def show_hand(self):
        print("Player hand: ")
        for card in self.hand:
            card.show()
        print('\n')

## TODO: Implement end game procedures.

def go_fish():
    count = 2
    cards_played = 0
    player_score = 0
    computer_score = 0
    answer = False
    while cards_played != 52:
        if count % 2 == 0:
            test = True
            while test == True:
                check_hand(player_score,cards_played, player1)

                if len(player1.hand) == 0:
                    player1.draw(card_deck)

                guess_card = str(input("What card would you like to request? "))
                if len(guess_card) < 3:
                    guess_card = int(guess_card)

                if look_for_card(guess_card, computer) == True:
                    print( "Congratulations. You guessed correctly.")
                    print('\n')

                    for good_card in player1.hand:
                        if good_card.val == guess_card:
                            player1.hand.remove(good_card)

                    for good_card in computer.hand:
                        if good_card.val == guess_card:
                            computer.hand.remove(good_card)

                    empty_hand(player1)
                    empty_hand(computer)
                    player1.show_hand()

                else:
                    print("Go Fish.\n")
                    count += 1


                    if check_deck() == True:
                        player1.draw(card_deck)
                        player1.show_hand()
                        check_hand(player_score, cards_played, player1)
                        test = False

                    else:
                        test = False

        else:
            test = True
            while test == True:
                check_hand(computer_score, cards_played, computer)

                if len(computer.hand) == 0:
                    computer.draw(card_deck)

                guess_card = computer_guess()
                print(f"Do you have a {guess_card}\n")

                answer = input("> ")
                if answer == "yes":
                    for good_card in computer.hand:
                        if good_card.val == guess_card:
                            computer.hand.remove(good_card)

                    for good_card in player1.hand:
                        if good_card.val == guess_card:
                            player1.hand.remove(good_card)

                    empty_hand(player1)
                    empty_hand(computer)
                    player1.show_hand()

                else:
                    print("Go Fish. \n")
                    count += 1


                    if check_deck() == True:
                        computer.draw(card_deck)
                        test = False

                    else:
                        test = False

    if computer_score > player_score:
        print(" You lose!")
        print(f" You successfully made {player_score / 2} pairs!")
        print(f" The computer successfully made {computer_score / 2} pairs!")

    elif player_score > computer_score:
        print("You Win!")
        print(f" You successfully made {player_score / 2} pairs!")
        print(f" The computer successfully made {computer_score / 2} pairs!")

    else:
        print("It's a tie")
        print(f" You successfully made {player_score / 2} pairs!")
        print(f" The computer successfully made {computer_score / 2} pairs!")

def computer_guess():
    guess = computer.hand[random.randint(0, len(computer.hand) - 1)]
    guess = guess.val

    if guess == 11:

        guess = "Jack"

    elif guess == 12:

        guess = "Queen"

    elif guess == 13:

        guess = "King"

    elif guess == 14:

        guess = "Ace"

    else:
        guess = guess

    return guess

def check_hand(player_score, cards_played, player):
    for card1 in player.hand:
        for card2 in player.hand:
            if card1.val == card2.val and card1.suit != card2.suit:
                player_score += 2
                cards_played += 2
                player.hand.remove(card1)
                player.hand.remove(card2)
                if player == player1:
                    player.show_hand()

def check_deck():

    if card_deck.cards != 0:
        return True

    else:
        return False

def look_for_card(guess, player):
    answer = False
    for card in player.hand:
        if guess == card.val:
            answer = True
            break
    return answer

def empty_hand(player):

    if len(player.hand) == 0:
        player.draw(card_deck)


player1 = Player()
computer = Player()

card_deck = Deck()
card_deck.shuffle()


for i in range(1,8):
    player1.draw(card_deck)

for j in range(1,8):
    computer.draw(card_deck)

card_deck.show()

player1.show_hand()
print("Computers hand:")
computer.show_hand()
go_fish()
