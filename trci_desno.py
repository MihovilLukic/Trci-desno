import pygame
from pygame.locals import *
import os
import sys
import math

pygame.init()

W, H = 800, 447
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('TRČI DESNO!')

bg = pygame.image.load(os.path.join('images', 'bg.png')).convert()
bgX = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()

class player(object):
    run = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(8,16)]
    jump = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(1,8)]
    slide = [pygame.image.load(os.path.join('images', 'S1.png')),pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S3.png')), pygame.image.load(os.path.join('images', 'S4.png')), pygame.image.load(os.path.join('images', 'S5.png'))]
    jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpcount = 0
        self.runcount =  0
        self.slideUp = False
        
    def draw(self, win):
        if self.jumping:
            self.y -= self.jumpList[self.jumpcountm] * 1.2
            win.blitt (self.jump[self.jumpcount//18], (self.x,self.y))
            self.jumpcount += 1
            if self.jumpcount > 100:
                self.jumpcount = 0
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            if self.slideCount >= 110:
                self.slideCount = 0
                self.slideUp = False
                self.runcount = 0
            win.blit(self.slide[self.slideCount//10], (self.x, self.y ))
            self.slideCount += 1
        
        else:
            if self.runcount > 42:
                self.runcount = 0
            win.blit(self.run[self.runcount//6], (self.x, self.y))
            self.runcount += 1
 
 
def redraw_window():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX, 0))
    pygame.display.update()             


run = True
speed = 30
      
while run:
    
    clock.tick(speed)
    bgX -= 1.4
    bgX2 -= 1.4
    
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
        
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            draw_window()
            pygame.quit
            quit() 
            
    
                   
        
        