import pygame
Window_Width,Window_Height=1000, 600
pygame.init()
disPlay_surfec=pygame.display.set_mode((Window_Width,Window_Height))
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.update()
pygame.quit()            

