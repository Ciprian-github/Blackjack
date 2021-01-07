# things to import
from Classes import Card, Deck,Hand, Player
from os import system,name
system("cls")
from time import sleep
from pip._vendor.colorama import init
init()
from pip._vendor.colorama import Back, Fore, Style

# list of variables
player_1 = None
player_2 = None
player_3 = None
player_4 = None
Dealer = Player('Dealer', ' ')
hand_1 = Hand()
hand_2 = Hand()
hand_3 = Hand()
hand_4 = Hand()
dealer = Hand()
dealer_hid_card = Card(' ',' ')
hid_card = []
new_deck = Deck()
player_list = [player_1,player_2,player_3,player_4]
hand_list = [hand_1,hand_2,hand_3,hand_4,dealer]
ply_option = {'H':'Hit', 'S':'Stand', 'D':'Double Down'}


# functions for the game

def table(player_list):
    '''
    Some sort of GUI
    :param player_list:
    :return:
    '''
    system('cls')
    print(Back.LIGHTBLUE_EX+Fore.WHITE + '{0:^161}\n{1:^161}\n{1:^161}'.format('Blackjack', ' ')+Fore.RESET)
    print(Fore.BLACK+'{0:^55}{1:^49}{0:^56} \n{0:55}{2}{0:57}'.format(' ', 'Dealer', dealer,))
    print(Fore.MAGENTA +'{0:^55}{1:^49}{0:^56} \n{0:161}\n{0:161}'.format(' ', f'{dealer.value()}-{Dealer.status}')+Fore.RESET)
    print(Fore.BLACK+'{0:^49} {1:^30} {2:^30} {3:^49}'.format(player_list[3].name+':'+str(player_list[3].chips_value)+' bet:'+str(player_list[3].amount_bet), ' ', ' ', player_list[0].name+':'+str(player_list[0].chips_value)+' bet:'+str(player_list[0].amount_bet)))
    print('{0} {1:^30} {2:^30} {3}'.format(hand_4, ' ', ' ', hand_1))
    print(Fore.MAGENTA+'{0:^49} {1:^30} {2:^30} {3:^49}'.format(f'{hand_4.value()} -{player_list[3].status}', ' ', ' ', f'{hand_1.value()} -{player_list[0].status}')+Fore.RESET)
    print(Fore.BLACK+'{0:^30} {1:^49} {2:^49} {3:^30}'.format(' ', player_list[2].name+':'+str(player_list[2].chips_value)+' bet:'+str(player_list[2].amount_bet), player_list[1].name+':'+str(player_list[1].chips_value)+' bet:'+str(player_list[1].amount_bet), ' '))
    print('{0:^30} {1} {2} {3:^30}'.format(' ', hand_3, hand_2, ' '))
    print(Fore.MAGENTA+'{0:^30} {1:^49} {2:^49} {3:^30}\n{0:161}'.format(' ',f'{hand_3.value()} -{player_list[2].status}', f'{hand_2.value()} -{player_list[1].status}', ' ')+Fore.RESET+Back.RESET)

def deal(num_players,player_list,hand_list):
    new_deck.shuffle()
    for x in range(2):
        for player in range(num_players + 1):
            if player < no_players:
                if player_list[player].amount_bet != 0:
                    hand_list[player].add_card(new_deck.deal_one())
                    sleep(0.5)
                    table(player_list)
            else:
                if x == 0:
                    hand_list[4].add_card(dealer_hid_card)
                    hid_card.append(new_deck.deal_one())
                    sleep(0.5)
                    table(player_list)
                else:
                    hand_list[4].add_card(new_deck.deal_one())
                    table(player_list)
                    sleep(0.5)
                    table(player_list)
def bet(player):
    if player.chips_value > 0:
        while True:
            try:
                amount = int(input(f'{player.name} place your bet:'))
                player.bet(amount)
                break
            except:
                print("Please try again")
def win(player):
    player.chips_value += 2*player.amount_bet
    player.amount_bet = 0
    player.status = 'Win!'
    table(player_list)
def bust(player):
    player.amount_bet = 0
    player.status = 'Bust!'
    table(player_list)
def lose(player):
    player.amount_bet = 0
    player.status = 'Lose!'
    table(player_list)
def push(player):
    player.chips_value += player.amount_bet
    player.amount_bet = 0
    player.status = 'Push!'
    table(player_list)

# setting the number of players and player's name
while True:
    try:
        no_players = int(input('Please choose the number of players (max.4):'))
    except:
        print('Please choose a number between 1-4!')
    else:
        if no_players in range(1,5):
            break
        else:
            print('Please choose a number between 1-4!')

for player in range(4):
    if player < no_players:
        player_list[player] = Player(input(f'Player {player+1}\'s name:'),100)
    else:
        player_list[player] = Player(f'Player {player+1}',0)
table(player_list)

def blackjack():
    for player in player_list:
        bet(player)
        sleep(0.5)
        table(player_list)
    # THE CARDS DEALING ROUTINE
    deal(no_players, player_list, hand_list)

    game_on = True
    while game_on:
        for player in range(no_players):
            round = 1
            y = player_list[player].amount_bet
            while True:
                try:
                    if hand_list[player].value() == 21:
                        if round ==1:
                            player_list[player].status = 'BlackJack'
                        else:
                            break
                    elif round == 1 and player_list[player].amount_bet <= player_list[player].chips_value and player_list[player].amount_bet != 0:
                        x = input(f'{player_list[player].name} choose your option H:Hit; S:Stand; D:Double Down:').upper()
                        table(player_list)
                        if ply_option[x] == 'Hit':
                            hand_list[player].add_card(new_deck.deal_one())
                            table(player_list)
                            if hand_list[player].value() > 21:
                                bust(player_list[player])
                                break
                        elif ply_option[x] == 'Double Down':
                            hand_list[player].add_card(new_deck.deal_one())
                            player_list[player].bet(y)
                            table(player_list)
                            if hand_list[player].value() > 21:
                                bust(player_list[player])
                                break
                            break
                        else:
                            table(player_list)
                            break
                    elif player_list[player].amount_bet != 0 and ply_option[input(f'{player_list[player].name} choose your option H:Hit; S:Stand:').upper()] == 'Hit':
                        hand_list[player].add_card(new_deck.deal_one())
                        table(player_list)
                        if hand_list[player].value() >21:
                            bust(player_list[player])
                            break
                    else:
                        table(player_list)
                        break
                    round += 1
                except:
                    print('Try again, you are drunk!')

        if filter(lambda x: x.amount_bet> 0,player_list) != []:
            dealer.replace_card(dealer_hid_card,hid_card[0])
            table(player_list)
        else:
            table(player_list)
            break

        while True:
            if len(dealer) == 2 and dealer.value() == 21:
                Dealer.status = 'BlackJack'
                table(player_list)
                break
            elif dealer.value()<17:
                dealer.add_card(new_deck.deal_one())
                sleep(0.5)
                table(player_list)
            elif dealer.value() > 21:
                Dealer.status = 'Bust!'
                break
            else:
                break
        for player in range(no_players):
            if hand_list[player].value() <= 21:
                if hand_list[player].value() == 21 and len(hand_list[player]) == 2:
                    if dealer.value() == 21 and len(dealer.value()) == 2:
                        push(player_list[player])
                    else:
                        win(player_list[player])
                elif dealer.value() == 21 and len(dealer) == 2:
                    lose((player_list[player]))
                elif dealer.value()>21:
                    win(player_list[player])
                elif dealer.value() < hand_list[player].value():
                    win(player_list[player])
                elif dealer.value() == hand_list[player].value():
                    push(player_list[player])
                else:
                    lose(player_list[player])
        game_on = False
blackjack()
game_opt = {'C': 'Continue', 'S':'Stop'}
while True:
    try:
        if game_opt[input('Do you want to continue(C) or do you wish to stop(S):').upper()] == 'Continue':
            new_deck.add_cards(dealer.clear_hand())
            Dealer.clear_status()
            for player in range(no_players):
                new_deck.add_cards(hand_list[player].clear_hand())
                player_list[player].clear_status()
            table(player_list)
            blackjack()
        else:
            print('Goodbye!')
            break
    except:
        print('Attention, idiot!!! \n Choose C or S.')
# de schimbat























