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
        self.suit = suit
        self.vals = vals

    def __str__(self):
        """
          >>> print(Card(2, 11))
          Queen of Hearts
        """
        return '{0} of {1}'.format(Card.VALS[self.vals],
                                   Card.SUITS[self.suit])

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
