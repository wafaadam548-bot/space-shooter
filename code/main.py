import pygame
import random

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("audio/game_music.wav")
pygame.mixer.music.play(-1)
laser_sound = pygame.mixer.Sound("audio/laser.wav")

Window_Width, Window_Height = 1000, 600
disPlay_surfec = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption("Space Shoter")
running = True

motors_lest = []

start_positions = [
    (random.randint(0, Window_Width), random.randint(0, Window_Height))
    for i in range(20)
]

motors = pygame.image.load("images/meteor.png").convert_alpha()
star = pygame.image.load("images/star.png").convert_alpha()
player = pygame.image.load("images/player.png").convert_alpha()
player_rect = player.get_frect(center=(Window_Width / 2, 350))
lasre = pygame.image.load("images/laser.png")

player_direction = pygame.math.Vector2()
clock = pygame.Clock()
player_speed =300
laser_rect = None


def creat_motors():
    x_pos = random.randint(0, Window_Width - motors.get_width())
    motors_rect = motors.get_frect(topleft=(x_pos, -motors.get_height()))
    motors_lest.append(motors_rect)


spawn_timer = 1

while running:
    dt = clock.tick(60) / 1000

    spawn_timer += dt
    if spawn_timer > 1:
        creat_motors()
        spawn_timer = 0

    for motor_rect in motors_lest[:]:
        motor_rect.y += 150 * dt

        if laser_rect and motor_rect.colliderect(laser_rect):
            motors_lest.remove(motor_rect)
            laser_rect = None

        if motor_rect.colliderect(player_rect):
            running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

    if player_direction.length() > 0:
        player_direction = player_direction.normalize()

    if keys[pygame.K_SPACE] and laser_rect is None:
        laser_rect = lasre.get_frect(midbottom=player_rect.midtop)
        laser_sound.play()

    player_rect.centerx += player_direction.x * player_speed * dt
    player_rect.centery += player_direction.y * player_speed * dt

    disPlay_surfec.fill("darkGray")

    for pos in start_positions:
        disPlay_surfec.blit(star, pos)

    for motor_rect in motors_lest:
        disPlay_surfec.blit(motors, motor_rect)

    if laser_rect:
        laser_rect.y -= 300 * dt
        if laser_rect.bottom < 0:
            laser_rect = None
        else:
            disPlay_surfec.blit(lasre, laser_rect)

    disPlay_surfec.blit(player, player_rect)
    pygame.display.update()
   