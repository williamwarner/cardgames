from deck import CardDeck
from deck import Card

class shanghai():

    numHands = 0
    hands = []
    
    def __init__(self, numHands):
        self.numHands = numHands
        deck = CardDeck(2)
        self.hands = deck.deal(numHands)
        
    
