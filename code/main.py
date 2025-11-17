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
player_direction=pygame.math.Vector2()
plan_rect=pygame.FRect()
clock=pygame.time.Clock()
player_speed=20
while running:
    dt=clock.tick()/100
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        keys=pygame.key.get_pressed()
        player_direction.x=int(keys[pygame.K_RIGHT])-int(keys[pygame.K_LEFT])
        player_direction.y=int(keys[pygame.K_DOWN])-int(keys[pygame.K_UP])

        if player_direction.x>=Window_Width:
            x=0
      #  if  keys[pygame.K_LEFT]:
          #  player_direction=-1
        #player_rect.center+=player_direction*player_speed*dt    
    

      #  if event.type==pygame.MOUSEMOTION:
           # player_rect.center=event.pos
    disPlay_surfec.fill("darkGray")    
    for pos in start_positions:
        disPlay_surfec.blit( star,pos)
    disPlay_surfec.blit( motors,motors_rect)
    disPlay_surfec.blit(lasre,laser_rect)
    player_rect.center+=player_direction*player_speed*dt 
    #player_rect.y-=10
    disPlay_surfec.blit(player,player_rect)  
    #if player_rect.bottom>=Window_Height:
       # player_rect=Window_Height
        #player_direction.y=-1
    #if player_rect.right>=Window_Width or player_rect.left<0:
      #  player_direction.x*=-1 
   # if player_rect.top<0 or player_rect.bottom>Window_Height:
       # player_direction.y*=-1    
    pygame.display.update()
pygame.quit()            

