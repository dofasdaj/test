import pygame
from pygame.locals import *
import sys
display = pygame.display.set_mode((1200,600))

class Pong(object): 
    def __init__(self,displaygr):
        self.displaygr = displaygr
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
        self.beruhrung_rechts = False
        self.beruhrung_links = False
        self.geschwindichkeit = 7
        #verschidene schwirgkeitsstufen --> verschiedene Geschwindichkeit
    def update(self,ai_schlager,schlager):
        self.xkordinate += self.richtung[0]*self.geschwindichkeit
        self.ykordinate += self.richtung[1]*self.geschwindichkeit

        self.rect.center = (self.xkordinate,self.ykordinate)
        if self.rect.top <= 0:
            self.richtung[1] = 1
        elif self.rect.bottom >= self.displaygr[1]-1:
            self.richtung[1] = -1

        if self.rect.right >= self.displaygr[0]-1:
            self.beruhrung_rechts = True
        elif self.rect.left <= 0:
            self.beruhrung_links = True
        if self.rect.colliderect(schlager.rect):
            self.richtung[0] = 1
        if self.rect.colliderect(ai_schlager.rect):
            self.richtung[0] = -1

                                                                          
    def render(self,display):
        pygame.draw.circle(display, self.farbe, self.rect.center, self.radius, 0)
        pygame.draw.circle(display, (1,1,1), self.rect.center, self.radius, 1)

class ai_schlager(object):
    def __init__(self, displaygr):
        self.display_gr = displaygr

        self.xkordinate = 50
        self.ykordinate = 300

        self.display = pygame.display.set_mode((1200,600))

        self.display = display


        self.h = 100
        self.breite = 10

        self.rect = pygame.Rect(0, self.ykordinate-int(self.h*0.5),self.breite,self.h)

        self.farbe = (255,255,255)

        self.geschwindichkeit = 7

        
    def update(self,pong):
        if pong.rect.top < self.rect.top:
            self.ykordinate -= self.geschwindichkeit
        elif pong.rect.bottom > self.rect.bottom:
            self.ykordinate += self.geschwindichkeit

        self.rect.center = (self.xkordinate, self.ykordinate)

    def render(self, display):
        pygame.draw.rect(display,self.farbe, self.rect, 0)
        pygame.draw.rect(display, (0,0,0), self.rect, 1)
class schlager(object):
    def __init__(self, displaygr):
        self.display_gr = displaygr

        self.xkordinate = 1150
        self.ykordinate = 300

        self.display = pygame.display.set_mode((1200,600))

        self.display = display


        self.h = 100
        self.breite = 10

        self.rect = pygame.Rect(0, self.ykordinate-int(self.h*0.5),self.breite,self.h)

        self.farbe = (255,255,255)

        self.geschwindichkeit = 7

        
    def update(self,pong):
        if pong.rect.top < self.rect.top:
            self.ykordinate -= self.geschwindichkeit
        elif pong.rect.bottom > self.rect.bottom:
            self.ykordinate += self.geschwindichkeit

        self.rect.center = (self.xkordinate, self.ykordinate)

    def render(self, display):
        pygame.draw.rect(display,self.farbe, self.rect, 0)
        pygame.draw.rect(display, (0,0,0), self.rect, 1)
def Grund():
    pygame.init()

    displaygr = (1200,600)
    
    display = pygame.display.set_mode(displaygr)

    clock = pygame.time.Clock()
    schlager = schlager(displaygr)

    pong = Pong(displaygr)
    ai_schlager = ai_schlager(displaygr)

    

    laufzeit = True
    
    while laufzeit:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                laufzeit = False
            


       

                

        ai_schlager.update(pong)
        schlager.update(pong)
        pong.update(schlager,ai_schlager)

        if pong.beruhrung_rechts:
            print("Win")
            laufzeit = False
        elif pong.beruhrung_links:
            print("Game Over")
            laufzeit = False
        #erzeugung der Grafik
        
        

        display.fill((0,0,0))
        
        pong.render(display)
        
        ai_schlager.render(display)
        schlager.render(display)
        

        pygame.display.flip()
    



Grund()


                
            
            


