import random

class Card(object):
    """
    how to handle ace high or low?
    """
    suit = ""
    value = 0

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
class Hand(object):
    """
    Hand has too much overlap with Deck. Pull out common things as utils?
    """
    hand = []
    suitOrder = {"spade":4, "heart":3, "diamond":2, "club":1}
    altName = {14:"Ace", 13:"King", 12:"Queen", 11:"Jack"}
    
    def __init__(self, card=None):
        if card is not None:
            self.hand = [card]
        else:
            self.hand = []
        
    def add(self, card):
        self.hand.append(card)
        
    def addSorted(self, card):
        # Can be more efficient
        self.hand.append(card)
        self.sort()
        
    def sort(self, sortType="suit"):
        """
        Can take type suit (order by suit ranking first) or value (order by value first)
        """
        if sortType=="suit":
            self.hand.sort(key = lambda x: (self.suitOrder[x.suit], x.value), reverse=True)
        elif sortType=="value":
            self.hand.sort(key = lambda x: (x.value, self.suitOrder[x.suit]), reverse=True)
            
    def take(self, card):
        if card in self.hand:
            return self.hand.remove(card)
        return None
            
    def printHand(self):
        handlist = ""
        for card in self.hand:
            if card.value in self.altName.keys():
                handlist += self.altName[card.value] + " " + card.suit
            else:
                handlist += str(card.value) + " " + card.suit
            if card != self.hand[-1]:
                handlist += ", "
        print(handlist + '\n')

class CardDeck(object):

    numDecks = 0
    numCards = 0
    deck = []
    altName = {14:"Ace", 13:"King", 12:"Queen", 11:"Jack"}
    suitOrder = {"spade":4, "heart":3, "diamond":2, "club":1}
    
    def buildDeck(self):
        pass
    
    def __init__(self, numDecks=1):
        self.numDecks = numDecks
        self.numCards = numDecks*52
        for _ in range(numDecks):
            for s in ["spade","heart","diamond","club"]:
                for i in range(14,1,-1):
                    self.deck.append(Card(s, i))
        
    def shuffle(self):
        random.shuffle(self.deck)
    
    def sort(self, sortType="suit"):
        """
        Can take type suit (order by suit ranking first) or value (order by value first)
        """
        if sortType=="suit":
            self.deck.sort(key = lambda x: (self.suitOrder[x.suit], x.value), reverse=True)
        elif sortType=="value":
            self.deck.sort(key = lambda x: (x.value, self.suitOrder[x.suit]), reverse=True)
    
    def takeTop(self):
        return self.deck.pop(0)
    
    def deal(self, numHands, numCards):
        if numHands*numCards > len(self.deck):
            return None
        hands = []
        for _ in range(numHands):
            hands.append(Hand(self.takeTop()))
        for _ in range(numCards-1):
            for i in range(numHands):
                hands[i].add(self.takeTop())
        return hands
    
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
