import pygame
import random
Window_Width,Window_Height=1000, 600
pygame.init()
disPlay_surfec=pygame.display.set_mode((Window_Width,Window_Height))
pygame.display.set_caption("Space Shoter")
running=True
surf=pygame.Surface((100,200))
surf.fill("orange")
x=100
star=pygame.image.load("images/star.png").convert_alpha()
player=pygame.image.load("images/player.png").convert_alpha()#convert alpha like collisionshape in godot
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    disPlay_surfec.fill("darkGray")    
    disPlay_surfec.blit(player,(x,150))  
    disPlay_surfec.blit( star,(random.randint(0, Window_Width), random.randint(0, Window_Height)))
    x+=0.3
    if x>=Window_Width:
        x=100 
    pygame.display.update()
pygame.quit()            

