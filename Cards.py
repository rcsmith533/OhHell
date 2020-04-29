import random
import math
deck = []
players = {}
gameRound = 0
dealer = 0

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
        
d = genDeck(deck)
random.shuffle(d)
addPlayer('Connor')
addPlayer('Sarah')
addPlayer('Joe')
addPlayer('Al')
#addPlayer('Luke')
#addPlayer('Alesha')
#addPlayer('Brad')
#addPlayer('Rachel')
#addPlayer('Cammie')
#addPlayer('Brandon')
#addPlayer('Hannah')
#addPlayer('Hailey')
dealCards(d)
for i in players:
    print(i, players[i]['Hand'],len(players[i]['Hand']))

def startRound(deck,numOfCards):
    d = genDeck(deck)
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

d = genDeck(deck)
random.shuffle(d)
clearHands()
dealCardsRound(d,1)
for i in players:
    print(i, players[i]['Hand'],len(players[i]['Hand']))

def startGame():
    maxRounds = (math.floor(52/len(players)))*2
    gameRound = 1
    while gameRound <= maxRounds:
        print('Round:',gameRound)
        print('Total Cards:',totalCardsDealt())
        if gameRound == 1:
            startRound(deck,maxRounds/2)
            while playersHaveCards():
                for i in players:
                    c = players[i]['Hand'].pop()
                    print(i,c)
        else:
            startRound(deck,(maxRounds/2)-(gameRound-1))
            while playersHaveCards():
                for i in players:
                    c = players[i]['Hand'].pop()
                    print(i,c)
        gameRound += 1

clearHands()
startGame()
for i in players:
    print(i, players[i]['Hand'],len(players[i]['Hand']))


    