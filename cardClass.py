import pygame
from random import *

pygame.init()
win = pygame.display.set_mode((550, 500))

pygame.display.set_caption("Card")

def text_to_screen(surface, text, x, y):

    # set size of text
    size = 20

    # set color
    color = (0, 0, 0)

    # try to update and print text
    try:

        # print text
        text = str(text)

        # set font
        font = pygame.font.Font("Roboto-Regular.ttf", size)

        # render text
        text = font.render(text, True, color)

        # print to screen
        surface.blit(text, (x, y))

    # prints Error if there is an error
    except:
        print("Error")


class Card:
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    VALS = ('narf', 'Ace', '2', '3', '4', '5', '6', '7',

             '8', '9', '10', 'Jack', 'Queen', 'King')
    
    def __init__(self, suit, vals):
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

        self.suit = suit
        self.vals = vals

    def __str__(self):
        """
          >>> print(Card(2, 11))
          Queen of Hearts
        """
        return '{0} of {1}'.format(Card.VALS[self.vals],
                                   Card.SUITS[self.suit])
        # alternate method - Ms. Harris
        
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

        # Set Icon
        pygame.display.set_icon(icon)

        # Global Constants
        black = (0, 0, 0)
        white = (255, 255, 255)
        gray = (192, 192, 192)

        cards = [diamondA, clubA, heartA, spadeA, \
                 diamond2, club2, heart2, spade2, \
                 diamond3, club3, heart3, spade3, \
                 diamond4, club4, heart4, spade4, \
                 diamond5, club5, heart5, spade5, \
                 diamond6, club6, heart6, spade6, \
                 diamond7, club7, heart7, spade7, \
                 diamond8, club8, heart8, spade8, \
                 diamond9, club9, heart9, spade9, \
                 diamond10, club10, heart10, spade10, \
                 diamondJ, clubJ, heartJ, spadeJ, \
                 diamondQ, clubQ, heartQ, spadeQ, \
                 diamondK, clubK, heartK, spadeK]
        cardA = [diamondA, clubA, heartA, spadeA]
        card2 = [diamond2, club2, heart2, spade2]
        card3 = [diamond3, club3, heart3, spade3]
        card4 = [diamond4, club4, heart4, spade4]
        card5 = [diamond5, club5, heart5, spade5]
        card6 = [diamond6, club6, heart6, spade6]
        card7 = [diamond7, club7, heart7, spade7]
        card8 = [diamond8, club8, heart8, spade8]
        card9 = [diamond9, club9, heart9, spade9]
        card10 = [diamond10, club10, heart10, spade10, \
                  diamondJ, clubJ, heartJ, spadeJ, \
                  diamondQ, clubQ, heartQ, spadeQ, \
                  diamondK, clubK, heartK, spadeK]
        
        
        
        
        
        
    def diamond(self, x, y, width, height, color):
        pygame.draw.polygon(win, (0, 0, 0), ((150, 100), (400, 100), (400, 400), (150, 400)), 2)  # draws border
        x = x + width/2
        pygame.draw.polygon(win, color, ((x, y), (x + width / 2, y + height / 2), (x, y + height), (x - width / 2, y + height / 2)))
    def spades(self, x, y):
        pygame.draw.polygon(win, (0, 0, 0), ((150, 100), (400, 100), (400, 400), (150, 400)), 2)  # draws border
        for i in range(6):
            pygame.draw.polygon(win, (0, 0, 0), [[x - 40, y + 55], [x + 40, y + 55], [x, y]])
            pygame.draw.ellipse(win, (0, 0, 0), [x - 50, y + 45, 60, 60])
            pygame.draw.ellipse(win, (0, 0, 0), [x - 10, y + 45, 60, 60])
            pygame.draw.polygon(win, (0, 0, 0), [[x - 25, y + 130], [x + 25, y + 130], [x, y + 90]])
    def heart(self, x, y, colour):
        pygame.draw.polygon(win, (0, 0, 0), ((150, 100), (400, 100), (400, 400), (150, 400)), 2)  # draws border
        pygame.draw.ellipse(win, colour, (x - 10, y, 32, 32))
        pygame.draw.ellipse(win, colour, (x + 10, y, 32, 32))
        pygame.draw.polygon(win, colour, ((x - 9, y + 20), (x + 40, y + 20), (x + 16, y + 55)))

    def club(self, circlex, circley, size):
        pygame.draw.polygon(win, (0, 0, 0), ((150, 100), (400, 100), (400, 400), (150, 400)), 2)  # draws border
        pygame.draw.ellipse(win, (0, 0, 0), ((circlex, circley), (size, size)), 0)
        pygame.draw.ellipse(win, (0, 0, 0), ((circlex - 25, circley + 45), (size, size)), 0)
        pygame.draw.ellipse(win, (0, 0, 0), ((circlex + 25, circley + 45), (size, size)), 0)
        pygame.draw.polygon(win, (0, 0, 0), ((circlex + 25, circley + 75), (circlex, circley + 125), (circlex + 60, circley + 125)), 0)

    def drawNum(self):
        if self.suit == 'Clubs':
            if self.vals == '5':
                Card.club(self, 250, 250, 50)
                text_to_screen(win, str(self.vals), 175, 125)
            if self.vals == '6':
                Card.club(self, 250, 250, 50)
                text_to_screen(win, str(self.vals), 175, 125)
            if self.vals == '7':
                Card.club(self, 250, 250, 50)
                text_to_screen(win, str(self.vals), 175, 125)
            if self.vals == '8':
                Card.club(self, 250, 250, 50)
                text_to_screen(win, str(self.vals), 175, 125)
            if self.vals == '9':
                Card.club(self, 250, 250, 50)
                text_to_screen(win, str(self.vals), 175, 125)
        if self.suit == 'Diamonds':
            if self.vals == '5':
                Card.diamond(self, 250, 250, 50, 50, (0, 0, 0))
                text_to_screen(win, str(self.vals), 175, 125)
            if self.vals == '6':
                Card.diamond(self, 250, 250, 50, 50, (0, 0, 0))
                text_to_screen(win, str(self.vals), 175, 125)
            if self.vals == '7':
                Card.diamond(self, 250, 250, 50, 50, (0, 0, 0))
                text_to_screen(win, str(self.vals), 175, 125)
            if self.vals == '8':
                Card.diamond(self, 250, 250, 50, 50, (0, 0, 0))
                text_to_screen(win, str(self.vals), 175, 125)
            if self.vals == '9':
                Card.diamond(self, 250, 250, 50, 50, (0, 0, 0))
                text_to_screen(win, str(self.vals), 175, 125)
        if self.suit == 'Hearts':
            if self.vals == '5':
                Card.heart(self, 250, 250, (255, 0, 0))
                text_to_screen(win, str(self.vals), 175, 125)
            if self.vals == '6':
                Card.heart(self, 250, 250, (255, 0, 0))
                text_to_screen(win, str(self.vals), 175, 125)
            if self.vals == '7':
                Card.heart(self, 250, 250, (255, 0, 0))
                text_to_screen(win, str(self.vals), 175, 125)
            if self.vals == '8':
                Card.heart(self, 250, 250, (255, 0, 0))
                text_to_screen(win, str(self.vals), 175, 125)
            if self.vals == '9':
                Card.heart(self, 250, 250, (255, 0, 0))
                text_to_screen(win, str(self.vals), 175, 125)
        if self.suit == 'Spades':
            if self.vals == '5':
                Card.spades(350, 300, 50)
                text_to_screen(win, str(self.vals), 175, 125)
            if self.vals == '6':
                Card.spades(250, 250, 50)
                text_to_screen(win, str(self.vals), 175, 125)
            if self.vals == '7':
                Card.spades(250, 250, 50)
                text_to_screen(win, str(self.vals), 175, 125)
            if self.vals == '8':
                Card.spades(250, 250, 50)
                text_to_screen(win, str(self.vals), 175, 125)
            if self.vals == '9':
                Card.spades(250, 250, 50)
                text_to_screen(win, str(self.vals), 175, 125)


card = Card('Spades', '5')

run = True
while run:
    pygame.time.delay(100) # time screen stays up in milliseconds

    for event in pygame.event.get():
        # loop to check if something has happened
        if event.type == pygame.QUIT:
            run = False # quits
    # draws rectangle
    win.fill((255, 255, 255))
    card.drawNum()
    # updates screen
    pygame.display.update()


pygame.quit()
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
