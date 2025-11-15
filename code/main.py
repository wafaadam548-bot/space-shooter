import pygame
Window_Width,Window_Height=1000, 600
pygame.init()
disPlay_surfec=pygame.display.set_mode((Window_Width,Window_Height))
pygame.display.set_caption("Space Shoter")
running=True
surf=pygame.Surface((100,200))
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    disPlay_surfec.fill("darkGray")    
    disPlay_surfec.blit(surf,(100,150))    
    pygame.display.update()
pygame.quit()            

