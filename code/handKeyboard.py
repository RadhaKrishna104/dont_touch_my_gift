import pygame
from pygame.sprite import Sprite
import time


# Global variable class to manage hand speed
class HandManager:
    base_speed = 2.0

    @classmethod
    def increment_base_speed(cls):
        """Increase the global base speed for all hands."""
        cls.base_speed += 0.1
       

class RightHand(Sprite):
    def __init__(self, screen_width, screen_height, offset_from_ground=200):
        super().__init__()
        self.r_hand_image = pygame.image.load(
            "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\assets\\right_hand.png"
        )
        self.image = self.r_hand_image
        self.rect = self.image.get_rect()

        # Position the hand on the right side of the screen
        self.rect.x = screen_width - self.rect.width
        self.rect.y = screen_height - self.rect.height - offset_from_ground

        # Hand speed
        self.hand_speed_y = HandManager.base_speed
        self.hand_speed_x = 2  # Adjust speed for smoother movement

        self.moving_time = pygame.time.get_ticks()
        self.direction = 1  # -1 for left, 1 for right

        self.passed = False

    def update(self):
        """Move the hand and remove it if off the screen."""
        self.rect.y += self.hand_speed_y
        if self.rect.top > 700:
            self.kill()

    def increment_speed(self):
        """Update the hand's speed to match the global base speed."""
        self.hand_speed_y = HandManager.base_speed

    def move(self):
        """Move left and right continuously."""
        current_time = pygame.time.get_ticks()
        if current_time - self.moving_time > 1000:  # Change direction every 1 second
            self.direction *= -1 # Reverse direction
            self.moving_time = current_time  # Reset moving time

        self.rect.x += self.hand_speed_x * self.direction


class LeftHand(Sprite):
    def __init__(self, screen_width, screen_height, offset_from_ground=300):
        super().__init__()
        self.l_hand_image = pygame.image.load(
            "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\assets\\left_hand.png"
        )
        self.image = self.l_hand_image
        self.rect = self.image.get_rect()

        # Position the hand on the left side of the screen
        self.rect.x = 0
        self.rect.y = screen_height - self.rect.height - offset_from_ground

        # Hand speed
        self.hand_speed_y = HandManager.base_speed
        self.hand_speed_x = 2

        self.moving_time = pygame.time.get_ticks()
        self.direction = -1  # 1 for right, -1 for left

        self.passed = False

    def update(self):
        """Move the hand and remove it if off the screen."""
        self.rect.y += self.hand_speed_y
        if self.rect.top > 700:
            self.kill()

    def increment_speed(self):
        """Update the hand's speed to match the global base speed."""
        self.hand_speed_y = HandManager.base_speed

    def move(self):
        """Move left and right continuously."""
        current_time = pygame.time.get_ticks()

        # Reverse direction every second
        if current_time - self.moving_time > 1000:
            
                self.direction *= -1  # Reverse direction
                self.moving_time = current_time  # Reset moving time

       
        self.rect.x += self.hand_speed_x * self.direction

        
