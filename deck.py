import random

class Card(object):
    """
    TODO:MAKE CARD VALUE LIST
    """
    suit = ""
    value = 0

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class CardDeck(object):

    numDecks = 0
    numCards = 0
    deck = []
    altName = {14:"Ace", 13:"King", 12:"Queen", 11:"Jack"}
    
    def buildDeck(self):
        pass
    
    def __init__(self, numDecks=1):
        self.numDecks = numDecks
        self.numCards = numDecks*52
        for _ in range(numDecks):
            for s in ["spade","diamond","heart","club"]:
                for i in range(14,1,-1):
                    self.deck.append(Card(s, i))
            
        
    def shuffle(self):
        random.shuffle(self.deck)
    
    def sort(self):
        pass
    
    def takeTop(self):
        return self.deck.pop(0)
    
    def printDeck(self):
        decklist = ""
        for card in self.deck:
            if card.value in self.altName.keys():
                decklist += self.altName[card.value] + " " + card.suit
            else:
                decklist += str(card.value) + " " + card.suit
            if card != self.deck[-1]:
                decklist += ", "
        print(decklist + '\n')
