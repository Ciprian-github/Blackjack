import random

suits = ('♥', '♦', '♠','♣' )
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11, ' ':0}
chip_value = 5
class Card():
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[self.rank]
    def __str__(self):
        return '|{0:>2} {1:>1}|'.format(self.rank,self.suit)

class Deck():
    def __init__(self):
        self.useddeck = []
        self.newdeck = []
        for suit in suits:
            for rank in ranks:
                card = Card(rank,suit)
                self.newdeck.append(card)
    def __str__(self):
        deck_comp = ''
        for card in self.newdeck:
            deck_comp += '\n' + card.__str__()
        return f'The deck has {len(self.newdeck)} crads:{deck_comp}'
    def shuffle(self):
        random.shuffle(self.newdeck)
    def deal_one(self):
        return self.newdeck.pop(0)
    def add_cards(self,cards):
        if type(cards) == list:
            self.newdeck.extend(cards)
        else:
            self.newdeck.append(cards)
class Hand():
    def __init__(self):
        self.hand_cards = []
    def __str__(self):
        hand_comp = ' '
        for card in self.hand_cards:
            hand_comp +=card.__str__() + ' '
        return '{0:^49}'.format(hand_comp)
    def __len__(self):
        return len(self.hand_cards)
    def add_card(self,card):
        self.hand_cards.append(card)
    def replace_card(self,card_out, card_in):
        self.hand_cards.insert(self.hand_cards.index(card_out), card_in)
        self.hand_cards.remove(card_out)
    def value(self):
        hand_value = 0
        card_rank = []
        for card in self.hand_cards:
            hand_value += card.value
            card_rank.append(card.rank)
        for A in range(card_rank.count('A')):
            if hand_value>21:
                hand_value += -10
        return hand_value
    def clear_hand(self):
        clear_hand = []
        clear_hand.extend(self.hand_cards)
        self.hand_cards.clear()
        return clear_hand
class Player():
    def __init__(self, name,chips_value ):
        self.name = name
        self.chips_value = chips_value
        self.amount_bet = 0
        self.status = ' '
    def __str__(self):
        if self.amount_bet == 0:
            return f'{self.name} has {self.chips_value} in chips value'
        else:
            return f'{self.name} has {self.chips_value} in chips value and bet {self.amount_bet}'
    def bet(self,amount_bet):
        if amount_bet > self.chips_value:
            print(f'You don\'t have that amount, your bet is {self.chips_value}')
            self.amount_bet += self.chips_value
            self.chips_value += -self.chips_value
        else:
            self.chips_value += -amount_bet
            self.amount_bet += amount_bet
    def clear_status(self):
        self.status = ''






















