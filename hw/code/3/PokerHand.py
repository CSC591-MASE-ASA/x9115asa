"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

# from __future__ import divison
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
        # print "Rank Hist"
        # print self.ranks
        for val in self.ranks.values():
            if val >= 4:
                # print val
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
        if 1 in self.ranks:
            keys.append(14)
        # print "Straight:",keys
        return self.check_straight(keys)

    def check_straight(self, keys):
        keys.sort()
        # print "keys",keys
        count = 0
        for i in xrange(1,15):
            # print "i",i
            if i in keys:
                # print "true"
                count = count + 1
                if count == 5:
                    return True
            else:
                count = 0

        return False

    def has_full_house(self):
        self.rank_hist();
        fh_hist = {}
        # print "rank hist",self.ranks
        for val in self.ranks.values():
            fh_hist[val] = fh_hist.get(val,0) + 1;
        # print "fh_hist",fh_hist
        # print self.ranks
        # print fh_hist
        count3 = 0
        #count number of ranks with frequency >= 3
        for key in fh_hist.keys():
            if key >= 3:
                 count3 = count3 + fh_hist[key]
        # print "count3", count3
        if count3 >= 1:
            # count3 = count3 - 1
            return (count3 + fh_hist.get(2,0) >= 2)
        return False

    def has_straight_flush(self):
        self.sort()
        # print "chacking straight flush"
        # print self.cards
        suit_rank_dict = {}
        for suit in xrange(4):
            this_suite_ranks = []
            for card in self.cards:
                if suit == card.suit:
                    this_suite_ranks.append(card.rank)
            if this_suite_ranks:
                suit_rank_dict[suit] = this_suite_ranks
            # print "This suite rank",suit,this_suite_ranks
        # print "Dict",suit_rank_dict
        res = False
        for val in suit_rank_dict.values():
            # print "val", val
            if 1 in val:
                val.append(14)
            # print "val2", val
            # print "self.check_straight(val)",self.check_straight(val)
            res = res or self.check_straight(val)
        return res




    def set_classification(self, classification):
        self.classification = classification

    def classify(self):
        if self.has_straight_flush():
            self.label = classification[0]
            return 0;
        if self.has_four_of_a_kind():
            self.label = self.classification[1]
            return 1;
        if self.has_full_house():
            self.label = self.classification[2]
            return 2;
        if self.has_flush():
            self.label = self.classification[3]
            return 3;
        if self.has_straight():
            self.label = self.classification[4]
            return 4;
        if self.has_three_of_a_kind():
            self.label = self.classification[5]
            return 5;
        if self.has_two_pair():
            self.label = self.classification[6]
            return 6;
        if self.has_pair():
            self.label = self.classification[7]
            return 7;
        else:
            self.label = "No classification"
            return

class Hist():
    seq = {}
    def __init__(self, categories):
        for category in categories:
            self.seq[category] = 0;

    def increment_count(self, key):
        self.seq[key] = self.seq.get(key,0) + 1

    def get_hist(self):
        return self.seq

if __name__ == '__main__':

    classification = ["Straight Flush","Four of a kind","Full house","Flush",
                    "Straight", "Three of a kind", "Two pair","Pair"]

    class_hist = Hist(classification)
    # hand = PokerHand()
    # hand.set_classification(classification)
    # c1 = Card(3,13)
    # c2 = Card(2,12)
    # c3 = Card(1,11)
    # c4 = Card(3,7)
    # c5 = Card(0,8)
    # c6 = Card(1,7)
    # c7 = Card(2,11)
    # hand.add_card(c1)
    # hand.add_card(c2)
    # hand.add_card(c3)
    # hand.add_card(c4)
    # hand.add_card(c5)
    # hand.add_card(c6)
    # hand.add_card(c7)
    # hand.sort()
    # print hand;
    # hand.classify()
    # print hand.label

    labels = []
    n = 10000
    for i1 in xrange(n):
    # make a deck
        deck = Deck()
        deck.shuffle()

        # deal the cards and classify the hands
        for i in range(7):
            hand = PokerHand()
            deck.move_cards(hand, 7)
            hand.sort()
            hand.set_classification(classification)
            # print "Hand",i
            # print hand
            # print "label"
            hand.classify()
            labels.append(hand.label)
            # print hand.label + "\n"

    for label in labels:
        class_hist.increment_count(label)

    total = n * 7.0;
    freq_hist = class_hist.get_hist()
    print "Total : "+ str(total)
    print freq_hist
    for key in classification:
        frequency = freq_hist.get(key,0)
        probability = (frequency/total)*100
        print "probability for %s = %.2f" % (key, probability)
