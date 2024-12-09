import pygame
import sys
from mainKeyboard import Game
from control import Control

# Initialize Pygame
class Lobby:
    def __init__(self):
        pygame.init()

        # Screen dimensions
        WINDOW_WIDTH = 600
        WINDOW_HEIGHT = 700

        # Create the screen
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Game Lobby")

        # Clock for controlling the frame rate
        self.clock = pygame.time.Clock()

        # Load assets (after setting up the display)
        self.bg_image = pygame.image.load(
            "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\assets\\bg.png"
        ).convert()  # Use .convert() for optimized blitting

        self.text_image = pygame.image.load(
            "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\menu\\title.png"
        ).convert_alpha()  # Use .convert_alpha() for images with transparency

        self.holding_gift_image = pygame.image.load(
            "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\menu\\holding_gift.png"
        ).convert_alpha()

        self.press_button_image = pygame.image.load(
            "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\menu\\press_any_key.png"
        ).convert_alpha()

        # Setup background music
        pygame.mixer.init()
        self.bg_music = "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\audio\\merry_christmas.ogg"
        pygame.mixer.music.load(self.bg_music)
        pygame.mixer.music.set_volume(3)
        pygame.mixer.music.play(-1)

        # Get the mouse position
        self.rect = pygame.Rect(205, 553, 202, 42)
    
    #event handling
    def event(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                # Detect mouse button down event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()  # Get current mouse position

                    # Check if the mouse is inside the rectangle using its edges
                    if self.rect.collidepoint(mouse_x, mouse_y):
                        if event.button == 1:  # Left mouse button (1)
                            pygame.mixer.Sound(
                                "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\audio\\slap.wav"
                            ).play()
                            control = Control()
                            control.run()

                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound(
                                "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\audio\\slap.wav"
                            ).play()
                    control = Control()
                    control.run()
    
    # Main loop
    def main(self):
        running = True
        while running:
            # Event handling
            self.event()
                    
            # Draw the background
            self.screen.blit(self.bg_image, (0, 0))

            # Draw text
            self.screen.blit(self.text_image, (125, 100))

            # Draw center image
            self.screen.blit(self.holding_gift_image, (125, 200))

            # Draw "press any key" image
            self.screen.blit(self.press_button_image, (125, 500))

            # Update the screen
            pygame.display.update()

            # Limit the frame rate to 60 FPS
            self.clock.tick(60)

        # Quit Pygame
        pygame.quit()
        sys.exit()


# Run the game lobby
if __name__ == "__main__":
    lobby = Lobby()
    lobby.main()
