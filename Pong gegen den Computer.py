import pygame
from pygame.locals import *
import sys
display = pygame.display.set_mode((1200,600))

class Pong(object): 
    def __init__(self,displaygröße):
        self.displaygröße = displaygröße
        self.xkordinate = 600
        self.ykordinate = 300
        self.display = pygame.display.set_mode((1200,600))
        self.display = display

        self.radius = 10

        self.rect = pygame.Rect(self.xkordinate-self.radius,
                                   self.ykordinate-self.radius,
                                   self.radius*2,self.radius*2)
        self.farbe = (255,255,255)

        self.richtung = [1,1]
        self.berührung_rechts = False
        self.berührung_links = False
        self.geschwindichkeit = 7
        #verschidene schwirgkeitsstufen --> verschiedene Geschwindichkeit
    def update(self,ai_schläger,schlaeger):
        self.xkordinate += self.richtung[0]*self.geschwindichkeit
        self.ykordinate += self.richtung[1]*self.geschwindichkeit

        self.rect.center = (self.xkordinate,self.ykordinate)
        if self.rect.top <= 0:
            self.richtung[1] = 1
        elif self.rect.bottom >= self.displaygröße[1]-1:
            self.richtung[1] = -1

        if self.rect.right >= self.displaygröße[0]-1:
            self.berührung_rechts = True
        elif self.rect.left <= 0:
            self.berührung_links = True
        if self.rect.colliderect(schlaeger.rect):
            self.richtung[0] = 1
        if self.rect.colliderect(ai_schläger.rect):
            self.richtung[0] = -1

                                                                          
    def render(self,display):
        pygame.draw.circle(display, self.farbe, self.rect.center, self.radius, 0)
        pygame.draw.circle(display, (1,1,1), self.rect.center, self.radius, 1)

class ai_schläger(object):
    def __init__(self, displaygröße):
        self.display_größe = displaygröße

        self.xkordinate = 50
        self.ykordinate = 300

        self.display = pygame.display.set_mode((1200,600))

        self.display = display


        self.höhe = 150
        self.breite = 10

        self.rect = pygame.Rect(0, self.ykordinate-int(self.höhe*0.5),self.breite,self.höhe)

        self.farbe = (255,255,255)

        self.geschwindichkeit = 4

        
    def update(self,pong):
        if pong.rect.top < self.rect.top:
            self.ykordinate -= self.geschwindichkeit
        elif pong.rect.bottom > self.rect.bottom:
            self.ykordinate += self.geschwindichkeit

        self.rect.center = (self.xkordinate, self.ykordinate)

    def render(self, display):
        pygame.draw.rect(display,self.farbe, self.rect, 0)
        pygame.draw.rect(display, (0,0,0), self.rect, 1)
class schläger(object):
    def __init__(self, displaygröße):
        self.display_größe = displaygröße

        self.xkordinate = 1150
        self.ykordinate = 300

        self.display = pygame.display.set_mode((1200,600))

        self.display = display


        self.höhe = 150
        self.breite = 10

        self.rect = pygame.Rect(0, self.ykordinate-int(self.höhe*0.5),self.breite,self.höhe)

        self.farbe = (255,255,255)

        self.geschwindichkeit = 4
        self.richtung = 0

        
    def update(self,pong):
        self.ykordinate += self.richtung*self.geschwindichkeit
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.display_größe[1]-1:
            self.rect.bottom = self.display_größe[1]-1

        self.rect.center = (self.xkordinate, self.ykordinate)

    def render(self, display):
        pygame.draw.rect(display,self.farbe, self.rect, 0)
        pygame.draw.rect(display, (0,0,0), self.rect, 1)
def Grund():
    pygame.init()

    displaygröße = (1200,600)
    
    display = pygame.display.set_mode(displaygröße)

    clock = pygame.time.Clock()
    schlaeger = schläger(displaygröße)

    pong = Pong(displaygröße)
    ai_schlaeger = ai_schläger(displaygröße)

    

    laufzeit = True
    
    while laufzeit:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                laufzeit = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    laufzeit = False
                if event.key == K_UP:
                    schlaeger.richtung = -1
                elif event.key == K_DOWN:
                    schlaeger.richtung = 1
            if event.type == KEYUP:
                if event.key == K_UP and schlaeger.richtung == -1:
                    schlaeger.richtung = 0
                if event.key == K_DOWN and schlaeger.richtung == 1:
                    schlaeger.richtung = 0    
            


       

                

        ai_schlaeger.update(pong)
        schlaeger.update(pong)
        pong.update(schlaeger,ai_schlaeger)
        
    
        
        

        #Man muss noch den Text auf dem display erzeugen!!!
        #Neustart ermöglichen

        if pong.berührung_rechts:
           
            laufzeit = False
        elif pong.berührung_links:
            
            laufzeit = False
        #erzeugung der Grafik
        
        

        display.fill((0,0,0))
        
        pong.render(display)
        
        ai_schlaeger.render(display)
        schlaeger.render(display)
        

        pygame.display.flip()
    



Grund()


                
            
            


