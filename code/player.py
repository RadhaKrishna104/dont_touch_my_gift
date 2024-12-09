import pygame
from scoreboard import Scoreboard

class Player:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load(
            "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\assets\\gift.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (screen_width // 2, screen_height)
        self.direction = pygame.Vector2(0, 0)  # Initialize movement direction vector
        self.speed = 20 
        self.speed_y = 5# Movement speed
        self.screen = pygame.display.set_mode((600, 700))
        self.scoreboard = Scoreboard()
        self.is_dragging = False
    
    def draw(self, screen):
        # Draw the player image on the screen
        screen.blit(self.image, self.rect)
    
    def move_keyboard(self):
        # Get keys pressed
        keys = pygame.key.get_pressed()
        
        # Reset direction for each frame
        self.direction.x = 0
        self.direction.y = 0
        
        # Get screen width and height
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()

        # Horizontal movement
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if self.rect.left > 0:  # Prevent moving off the left edge
                self.direction.x -= 1
                
                
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self.rect.right < self.width:  # Prevent moving off the right edge
                self.direction.x += 1

        # Vertical movement
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.rect.top > 350:  # Prevent moving off the top edge
                self.direction.y -= 1
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if self.rect.bottom < self.height:  # Prevent moving off the bottom edge
                self.direction.y += 1

        # Normalize the direction vector to avoid faster diagonal movement
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

        # Update position with normalized direction
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed_y


    def move_mouse(self):
        
        for event in pygame.event.get():
            # Check if the mouse button is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.rect.collidepoint(mouse_x, mouse_y):
                    self.is_dragging = True  # Enable dragging

            # Check if the mouse button is released
            elif event.type == pygame.MOUSEBUTTONUP:
                self.is_dragging = False  # Disable dragging

        # If dragging, update the player's position to the mouse's position
        if self.is_dragging and self.rect.top > 350:
            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.rect.center = (mouse_x, mouse_y)
            
        if self.rect.top <= 350:
            self.rect.top = 370
                