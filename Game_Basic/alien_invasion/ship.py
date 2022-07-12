import pygame
class Ship:
    # A class to manage the ship
    def __init__(self,ai_game):
        # Initialize the ship and set its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load(r'D:\Python_Code\Game_Basic\alien_invasion\ship.png')
        self.rect = self.image.get_rect()
        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # draw the ship at its current location.
        self.screen.blit(self.image,self.rect)