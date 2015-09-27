import pygame
class Pong(object): 
    def __init__(self,displaygröße):
        self.displaygröße = displaygröße
        self.xkordinate = 600
        self.ykordinate = 300
    def update(self,ai_schläger,schlaeger):
        self.xkordinate += self.richtung[0]*self.geschwindichkeit
        self.ykordinate += self.richtung[1]*self.geschwindichkeit

    
    def render(self,display):
        pygame.draw.circle(display, self.farbe, self.rect.center, self.radius, 0)
        pygame.draw.circle(display, (1,1,1), self.rect.center, self.radius, 1)



def Menü():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('PONG-Menü')
    fenstergröße = (1200,600)
    fenster = pygame.display.set_mode(fenstergröße)
    laufzeit = True
    
    
    while laufzeit:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                laufzeit = False
            
        
        pygame.display.flip()
        bild = pygame.image.load("Menue.bmp")
        if bild.get_alpha() == None:
            bild = bild.convert()
        else:
            bild = bild.convert_alpha()
        fenster.blit(bild, (0,0))

Menü()
Grund()



