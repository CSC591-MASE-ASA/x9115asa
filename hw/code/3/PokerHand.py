"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *


class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_three_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_four_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def has_two_pair(self):
        self.rank_hist()
        pairs = 0
        for val in self.ranks.values():
            if val >= 2:
                pairs = pairs + 1
        if pairs >= 2:
            return True
        return False

    def has_straight(self):
        self.rank_hist();
        keys = self.ranks.keys()
        keys.sort()
        if 1 in self.ranks:
            keys.append(15)
        count = 0
        for i in xrange(1,16):
            if i in keys:
                count = count + 1
                if count == 5:
                    return True
                else:
                    count = 0
        return False

    def has_full_house(self):
        self.rank_hist();
        fh_hist = {}
        for val in self.ranks.values():
            fh_hist[val] = fh_hist.get(val,0) + 1;
        print self.ranks
        print fh_hist
        count3 = 0
        #count number of ranks with frequency >= 3
        for key in fh_hist.keys():
            if key >= 3:
                 count3 = count3 + fh_hist[key]
         if count3 >= 1:
             count3 = count3 - 1
             return (count3 + fh_hist.get(2,0) >= 2)
         return False



if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(2):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print hand
        print hand.has_flush()
        print "fh"
        hand.has_full_house()
        print ''
