import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
# Overall class to manage game assets and behavior. 
    def __init__(self):

    # Initialize the game, and create game resources.
        pygame.init()
        pygame.display.set_caption("Aline Invasion")  
        self.settings = Settings() 
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

    # set background color
        self.bg_color = (230,230,230)
    
        self.ship = Ship(self)

    def run_game(self):
    # Start the main loop for the game
        while True:
            self._check_events()
            self._update_screen()

            pygame.display.flip()
    def _check_events(self):
        # respond to keypress and mouse events.
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
    def _update_screen(self):
        # update images on the screen, and flip to the new screen.
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

if __name__ == "__main__":
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai = ai.run_game()

