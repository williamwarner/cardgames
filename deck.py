class Card(object):
    suit = ""
    value = 0
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class CardDeck(object):

    numDecks = 0
    numCards = 0
    deck = []
    
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
        pass
    
    def sort(self):
        pass
    
    def takeTop(self):
        pass
    
    def printDeck(self):
        pass
