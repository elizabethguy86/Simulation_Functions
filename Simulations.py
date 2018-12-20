import random
import numpy as np

def outcome():
    '''Find outcome for the coin_flip() function.'''
    prob = random.random()
    if prob > 0.5:
        return 'T'
    else:
        return 'H'

def coin_flip():
    '''Two players, A and B, play a game by alternating flipping a fair coin starting with A.
    The sequence of outcomes is recorded. The game ends if a person tosses a tail following a head 
    (the tail does not have to immediately follow the head, nor 
    does it have to be tossed by the same person who tossed the head), and that person wins the game. 
    What is the probability that A wins?'''
    head_played = False
    player = 'A'
    while True:
        result = outcome()
        if result == 'H':
            head_played = True
        elif (result == 'T') and (head_played == True):
            return player == 'A'
        if player == 'A':
            player = 'B'
        elif player == 'B':
            player = 'A'
probability_A = sum(coin_flip() for _ in range(1000000))
#return the actual probability
probability_A/1000000


def star_cards(n=60, s=3, d=3, draw=5):
    """
    You have a shuffled deck of 60 cards containing the following cards of special
    interest:
    - Three of the cards in the deck are marked with a diamond.
    - Three of the cards are marked with a star.  
    - The remaining cards are nothing special.
    You draw an initial hand of five cards, after which you *must* discard any of
    the star cards for an additional three cards drawn from the top of the deck.
    This process is repeated until you find yourself with a hand that does *not*
    contain any star cards. Write a simulation to approximate the probability that
    your initial draw results in a final hand containing a diamond card.
    """
    hand = np.random.choice(range(1, n+1), draw)
    if n == 0:
        return 0
    stars = 0
    for c in hand:
        if c <= d:
            return 1
    if (c > d) and (c <= d+s):
        stars += 1
    if stars > 0:
        return star_cards(n - draw, s - stars, d = 3, draw = 3*stars)
    if stars == 0:
        return 0
