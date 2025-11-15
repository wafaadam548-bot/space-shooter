import pygame
Window_Width,Window_Height=1200,700
pygame.init()
disPlay_surfec=pygame.display.set_mode((Window_Width,Window_Height))
running=True
while running:
    for event in pygame.event.get():
        if event.type==quit:
            running=False

