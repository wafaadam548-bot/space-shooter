import pygame
Window_Width,Window_Height=1000, 600
pygame.init()
disPlay_surfec=pygame.display.set_mode((Window_Width,Window_Height))
pygame.display.set_caption("Space Shoter")
running=True
surf=pygame.Surface((100,200))
surf.fill("orange")
x=100
player=pygame.image.load("images/player.png")
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    disPlay_surfec.fill("darkGray")    
    disPlay_surfec.blit(surf,(x,150))   
    x+=0.3
    if x>=Window_Width:
        x=100 
    pygame.display.update()
pygame.quit()            

