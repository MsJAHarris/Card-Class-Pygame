class Card:
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    VALS = ('narf', 'Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King']
        # Load Images - all in resources - borrowed from Open source, not remembered where now.
    icon = pygame.image.load('resources/icon.png')
    cBack = pygame.image.load('resources/cards/cardback.png')
    diamondA = pygame.image.load('resources/cards/ad.png')
    clubA = pygame.image.load('resources/cards/ac.png')
    heartA = pygame.image.load('resources/cards/ah.png')
    spadeA = pygame.image.load('resources/cards/as.png')
    diamond2 = pygame.image.load('resources/cards/2d.png')
    club2 = pygame.image.load('resources/cards/2c.png')
    heart2 = pygame.image.load('resources/cards/2h.png')
    spade2 = pygame.image.load('resources/cards/2s.png')
    diamond3 = pygame.image.load('resources/cards/3d.png')
    club3 = pygame.image.load('resources/cards/3c.png')
    heart3 = pygame.image.load('resources/cards/3h.png')
    spade3 = pygame.image.load('resources/cards/3s.png')
    diamond4 = pygame.image.load('resources/cards/4d.png')
    club4 = pygame.image.load('resources/cards/4c.png')
    heart4 = pygame.image.load('resources/cards/4h.png')
    spade4 = pygame.image.load('resources/cards/4s.png')
    diamond5 = pygame.image.load('resources/cards/5d.png')
    club5 = pygame.image.load('resources/cards/5c.png')
    heart5 = pygame.image.load('resources/cards/5h.png')
    spade5 = pygame.image.load('resources/cards/5s.png')
    diamond6 = pygame.image.load('resources/cards/6d.png')
    club6 = pygame.image.load('resources/cards/6c.png')
    heart6 = pygame.image.load('resources/cards/6h.png')
    spade6 = pygame.image.load('resources/cards/6s.png')
    diamond7 = pygame.image.load('resources/cards/7d.png')
    club7 = pygame.image.load('resources/cards/7c.png')
    heart7 = pygame.image.load('resources/cards/7h.png')
    spade7 = pygame.image.load('resources/cards/7s.png')
    diamond8 = pygame.image.load('resources/cards/8d.png')
    club8 = pygame.image.load('resources/cards/8c.png')
    heart8 = pygame.image.load('resources/cards/8h.png')
    spade8 = pygame.image.load('resources/cards/8s.png')
    diamond9 = pygame.image.load('resources/cards/9d.png')
    club9 = pygame.image.load('resources/cards/9c.png')
    heart9 = pygame.image.load('resources/cards/9h.png')
    spade9 = pygame.image.load('resources/cards/9s.png')
    diamond10 = pygame.image.load('resources/cards/10d.png')
    club10 = pygame.image.load('resources/cards/10c.png')
    heart10 = pygame.image.load('resources/cards/10h.png')
    spade10 = pygame.image.load('resources/cards/10s.png')
    diamondJ = pygame.image.load('resources/cards/jd.png')
    clubJ = pygame.image.load('resources/cards/jc.png')
    heartJ = pygame.image.load('resources/cards/jh.png')
    spadeJ = pygame.image.load('resources/cards/js.png')
    diamondQ = pygame.image.load('resources/cards/qd.png')
    clubQ = pygame.image.load('resources/cards/qc.png')
    heartQ = pygame.image.load('resources/cards/qh.png')
    spadeQ = pygame.image.load('resources/cards/qs.png')
    diamondK = pygame.image.load('resources/cards/kd.png')
    clubK = pygame.image.load('resources/cards/kc.png')
    heartK = pygame.image.load('resources/cards/kh.png')
    spadeK = pygame.image.load('resources/cards/ks.png')

    def __init__(self, suit=0, vals=0):
        self.suit = suit
        self.vals = vals

    def __str__(self):
        """
          >>> print(Card(2, 11))
          Queen of Hearts
        """
        return '{0} of {1}'.format(Card.VALS[self.vals],
                                   Card.SUITS[self.suit])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
