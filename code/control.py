import pygame
import sys
import mainKeyboard 
import mainMouse
from mouse_set import MouseSet

class Control:
    def __init__(self):
        #initialise pygame
        pygame.init()
        
        #set dimensions
        WINDOW_WIDTH = 600
        WINDOW_HEIGHT = 700
        
        #screen and title
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("DONT TOUCH MY PRESENT")
        
        self.running = True
        
        #background
        self.bg_image = pygame.image.load(
            "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\assets\\bg.png")
        
        #button
        self.button_image = pygame.image.load(
            "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\assets\\scoreboard.png")
        
        #text
        self.font = pygame.font.Font(
            "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\assets\\Shred Handed.otf", 33)
        
        # Setup background music
        pygame.mixer.init()
        self.bg_music = "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\audio\\merry_christmas.ogg"
        pygame.mixer.music.load(self.bg_music)
        pygame.mixer.music.set_volume(3)
        pygame.mixer.music.play(-1)

        self.button1_rect = pygame.Rect(130, 308, 202, 43 )
        self.button2_rect = pygame.Rect(339, 308, 202, 43)
        
        self.clock = pygame.time.Clock()
    
    #text draw
    def display_score(self):
        #t1
        self.text1 = "KEYBOARD"
        score_text = self.font.render(f"{self.text1}", True, (0, 0, 0))
        self.screen.blit(score_text, (140, 315))  
        
        #t2
        self.text2 = "MOUSE"
        score_text = self.font.render(f"{self.text2}", True, (0, 0, 0))
        self.screen.blit(score_text, (360, 315))  
    
    def event(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                
                # For keyboard button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    
                    # Get current mouse position
                    if self.button1_rect.collidepoint(mouse_x, mouse_y):
                         #sound effect
                        pygame.mixer.Sound(
                                "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\audio\\slap.wav"
                            ).play()
                        game = mainKeyboard.Game()
                        game.run()
                    
                    #for mouse button
                    elif self.button2_rect.collidepoint(mouse_x, mouse_y):
                         #sound effect
                        pygame.mixer.Sound(
                                "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\audio\\slap.wav"
                            ).play()
                        game = MouseSet()
                        game.run()
                       
                     
    #main run func    
    def run(self):
        while self.running:
            self.clock.tick(60)
            # Handle events
            self.event()
                        
            self.screen.blit(self.bg_image, (0,0))
            
            #blit buttons
            self.screen.blit(self.button_image, (120, 300))            
            self.screen.blit(self.button_image, (330, 300))
            
            #blit texts
            self.display_score()
            
            pygame.display.update()
            
        pygame.quit()
    
    
if __name__ == "__main__":
    control = Control()
    control.run()