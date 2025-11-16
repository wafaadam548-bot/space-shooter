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
start_positions = [
    (random.randint(0, Window_Width), random.randint(0, Window_Height))
    for i in range(20)
]
motors=pygame.image.load("images/meteor.png").convert_alpha()
motors_rect=motors.get_frect(center=(Window_Width/2,Window_Height/2))
star=pygame.image.load("images/star.png").convert_alpha()
player=pygame.image.load("images/player.png").convert_alpha()#convert alpha like collisionshape in godot
player_rect=player.get_frect(center=(Window_Width/2,350))
lasre=pygame.image.load("images/laser.png")
laser_rect=lasre.get_frect(bottomleft=(20,Window_Height-20))
player_direction=-1
plan_rect=pygame.FRect()
clock=pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    disPlay_surfec.fill("darkGray")    
    for pos in start_positions:
        disPlay_surfec.blit( star,pos)
    disPlay_surfec.blit( motors,motors_rect)
    disPlay_surfec.blit(lasre,laser_rect)
    disPlay_surfec.blit(player,player_rect)  
    
    player_rect.x+=player_direction*0.4
    if player_rect.right>=Window_Width or player_rect.left<0:
        player_direction*=-1 
    pygame.display.update()
pygame.quit()            

