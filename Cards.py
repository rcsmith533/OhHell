import random
import math
from collections import OrderedDict
players = OrderedDict()

def genDeck():
        deck = []
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

def dealCardsRound(shuffeledDeck,num):
    cardsDealt = 0
    while cardsDealt < num:
        for i in players:
            players[i]['Hand'].append(shuffeledDeck.pop())
        cardsDealt += 1

def clearHands():
    for i in players:
        players[i]['Hand'].clear()
    
def legalCards(hand):
    #TODO
    #Returns a list of cards that can be played
    return None

def startRound(numOfCards):
    d = genDeck()
    random.shuffle(d)
    dealCards(d)

def totalCardsDealt():
    total = 0
    for i in players:
        total = total + len(players[i]['Hand'])
    return total

def playersHaveCards():
    if totalCardsDealt() == 0:
        return False
    else:
        return True

def genRounds():
    maxRounds = ((math.floor(52/len(players)))*2)-1
    x = 0
    cards = math.floor(52/len(players))
    roundCardCount = []
    halfwayPoint = math.ceil(maxRounds/2)
    while x < maxRounds:
        if x < halfwayPoint-1:
            roundCardCount.append(cards)
            cards -= 1
            x += 1
        else:
            roundCardCount.append(cards)
            cards += 1
            x += 1
    return roundCardCount

def printHands():
    for i in players:
        print(i, players[i]['Hand'],len(players[i]['Hand']))

def swapDealer():
    players.move_to_end(list(players.keys())[0])

d = genDeck()
random.shuffle(d)
clearHands()

addPlayer('Connor')
addPlayer('Sarah')
addPlayer('Joe')
addPlayer('Al')
addPlayer('p1')
addPlayer('p2')
addPlayer('p3')
addPlayer('p4')

def startGame():
    maxRounds = ((math.floor(52/len(players)))*2)-1
    gameRound = 0
    cardCount = genRounds()
    while gameRound < maxRounds:
        print('Round:',gameRound + 1)
        print('Total Cards:',cardCount[gameRound])
        startRound(cardCount[gameRound])
        while playersHaveCards():
            for i in players:
                c = players[i]['Hand'].pop()
                print(i,c)
        swapDealer()
        gameRound += 1

clearHands()
startGame()



    