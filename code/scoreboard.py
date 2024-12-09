import pygame

class Scoreboard:
    def __init__(self):
        self.image = pygame.image.load(
            "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\assets\\scoreboard.png")
        self.rect = self.image.get_rect()
        self.rect.right = 370
        self.rect.top = 50
        self.score = 0 
        self.font = pygame.font.Font(
            "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\assets\\Shred Handed.otf", 33)
        
        
    def draw(self,screen):
        screen.blit(self.image, self.rect)
        
    def update_score(self, score):
        self.score += score
        
        if self.score == 10:
            pygame.mixer.init()
            m1 = "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\audio\\cheer_2.wav"
            pygame.mixer.Sound(m1).play()
        
        if self.score == 2:
            m2 = "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\audio\\cheer_3.wav"
            pygame.mixer.Sound(m2).play()
              
        if self.score == 50:
            m3 = "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\audio\\cheer_4.wav"
            pygame.mixer.Sound(m3).play()
        
        if self.score == 100:
            m4 = "C:\\Users\\amars\\Desktop\\dont touch my present\\dont-touch-my-presents\\data\\audio\\cheer.wav"
            pygame.mixer.Sound(m4).play()
        
        
    def display_score(self, screen):
        score_text = self.font.render(f"{self.score}", True, (135, 206, 235))
        screen.blit(score_text, (297, 65))