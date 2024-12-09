import pygame
from player import Player
from handMouse import RightHand, LeftHand
import sys
from random import choice, randint
from scoreboard import Scoreboard


class Game:
    def __init__(self):
        pygame.init()
        WINDOW_WIDTH = 600
        WINDOW_HEIGHT = 700
        
        # Set up the display
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("DONT TOUCH MY PRESENT")
        
        # Load the background image
        self.bg_image = pygame.image.load(
            "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\assets\\bg.png"
        )
        self.running = True
        self.clock = pygame.time.Clock()

        # Create the player and hands
        self.player = Player(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.hands = pygame.sprite.Group()
        self.scoreboard = Scoreboard()
        
       
         # Time tracking for creating hands
        self.last_hand_creation_time = 0
        self.hand_creation_interval = 1500  # 3 seconds in milliseconds
        
        #create initial 3 sec font
        self.font = pygame.font.Font(
            "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\assets\\Shred Handed.otf", 33)
 
        
        self._create_initial_hands(WINDOW_WIDTH, WINDOW_HEIGHT)
        
        
        #lives 
        self.life = 1
        
      
       
        
        # Create a group for all sprites
        self.all_sprites = pygame.sprite.Group(*self.hands)
        
                #setup bg music
        pygame.mixer.init()
        self.bg_music = "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\audio\\sleigh_ride.ogg"
        pygame.mixer.music.load(self.bg_music)
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1, fade_ms = 1000)
        
      

    
    
            
    def _create_initial_hands(self, WINDOW_WIDTH, WINDOW_HEIGHT):
                #not calling make hands because initial position is not same as afters
        rhand1 = RightHand(WINDOW_WIDTH, WINDOW_HEIGHT, offset_from_ground=150)
        rhand2 = RightHand(WINDOW_WIDTH, WINDOW_HEIGHT, offset_from_ground=700)
        
        lhand = LeftHand(WINDOW_WIDTH, WINDOW_HEIGHT, offset_from_ground=425)
        self.hands.add(rhand1, rhand2, lhand)
        

    def make_hands(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        self.all_sprites = pygame.sprite.Group(*self.hands)
        

        hand_choice = ['right', 'left']
        
        
        if choice(hand_choice) == 'right':
            rhand1 = RightHand(WINDOW_WIDTH, WINDOW_HEIGHT, offset_from_ground=700)
            self.hands.add(rhand1)
            self.all_sprites.add(rhand1)
        else:
            lhand1 = LeftHand(WINDOW_WIDTH, WINDOW_HEIGHT, offset_from_ground=700)
            self.hands.add(lhand1)
            self.all_sprites.add(lhand1)
        
    def collision(self):
        #check collisions
            for hand in self.hands:
                if self.player.rect.colliderect(hand.rect):
                    self.life -= 1
                    hand.kill()
                    
                   
                if not self.life:
                    from lobby import Lobby
                    self.lobby = Lobby()
                    self.lobby.main()
                    sys.exit()
      
    def _button_down(self):
                     # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event .type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    
    def score(self):
        
        for hand in self.hands:
            if self.player.rect.y <= hand.rect.top and not hand.passed:
                self.scoreboard.update_score(1)
                hand.passed = True  # Mark the hand as passed to avoid counting it again
         
         #play score sound effect
                score_sound = pygame.mixer.Sound(
                    "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\audio\\score.wav")
                score_sound.set_volume(1)
                score_sound.play()
    
    def moving_hand(self):
            for hand in self.hands:
                hand.update()
                hand.move()
      
        
    def run(self):
        while self.running:
            self.clock.tick(60)

            self._button_down()
                
            # Check if 2 seconds have passed
            current_time = pygame.time.get_ticks()
            if current_time - self.last_hand_creation_time > self.hand_creation_interval:
                self.make_hands(600, 700)
                self.last_hand_creation_time = current_time
            
            # Update all sprites
            self.all_sprites.update()

            # Draw the background
            self.screen.blit(self.bg_image, (0, 0))
            
            
            
            self.player.move_mouse()
           
            
            self.moving_hand()
            
                
            # Draw all sprites
            self.all_sprites.draw(self.screen)
            self.player.draw(self.screen)
            self.scoreboard.draw(self.screen)
            self.score()
            self.scoreboard.display_score(self.screen)
            
           
            self.collision()
            
            
            # Update the display
            pygame.display.update()
        
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
