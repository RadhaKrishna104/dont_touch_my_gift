import pygame
import mainMouse

class MouseSet:
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
       
        
        #text
        self.font = pygame.font.Font(
            "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\assets\\Shred Handed.otf", 33)
        
        # Setup background music
        pygame.mixer.init()
        self.bg_music = "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\audio\\merry_christmas.ogg"
        pygame.mixer.music.load(self.bg_music)
        pygame.mixer.music.set_volume(3)
        pygame.mixer.music.play(-1)

        self.clock = pygame.time.Clock()
    
    def adjusting_text(self):
       
        self.text = "LEFT CLICK ON GIFT PLAYER FOR 2 SECONDS"
        adj_text = self.font.render(self.text, True, (0, 0, 0))
           
        self.screen.blit(adj_text, (90,170)) 
        
        self.text = "TO ATTACH YOUR MOUSE TO THE GIFT "
        adj_text = self.font.render(self.text, True, (0, 0, 0))
           
        self.screen.blit(adj_text, (120,270)) 
        
        self.text = "CLICK MOUSE TO START PLAYING"
        adj_text = self.font.render(self.text, True, (0, 0, 0))
           
        self.screen.blit(adj_text, (140,570)) 
    
    def event(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                
                # Detect mouse button down event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game = mainMouse.Game()
                    game.run()
                    
                    
                     
    #main run func    
    def run(self):
        while self.running:
            self.clock.tick(60)
            # Handle events
            self.event()
                        
            self.screen.blit(self.bg_image, (0,0))
            
            
            self.adjusting_text()
            
            pygame.display.update()
            
        pygame.quit()
    
    
if __name__ == "__main__":
    control = Control()
    control.run()