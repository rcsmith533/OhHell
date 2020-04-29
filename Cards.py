import random
import math
deck = []
players = {}
gameRound = 0

def genDeck(deck):
        nums = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        suits = ['S','H','C','D']
        s = 0
        while s < 4:
            for i in nums:
                deck.append(i+suits[s])
            s += 1
        return deck

def addPlayer(playerName):
    players[playerName] = {'Score':0,'Bids':[],'Hand':[]}

def dealCards(shuffeledDeck):
    cardsDealt = 0
    while cardsDealt < math.floor(52/len(players)):
        for i in players:
            players[i]['Hand'].append(shuffeledDeck.pop())
        cardsDealt += 1
    
def legalCards(hand):
    #TODO
    #Returns a list of cards that can be played
    return None
        
d = genDeck(deck)
random.shuffle(d)
addPlayer('Connor')
addPlayer('Sarah')
addPlayer('Joe')
addPlayer('Al')
addPlayer('Luke')
addPlayer('Alesha')
dealCards(d)
for i in players:
    print(i, players[i]['Hand'],len(players[i]['Hand']))