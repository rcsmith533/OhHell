deck = []
import random

def genDeck(deck):
        nums = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        suits = ['S','H','C','D']
        s = 0
        while s < 4:
            for i in nums:
                deck.append(i+suits[s])
            s += 1
        return deck

d = genDeck(deck)

print(d)
random.shuffle(d)
print(d)