import pygame
import random

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("audio/game_music.wav")
pygame.mixer.music.play(-1)
laser_sound = pygame.mixer.Sound("audio/laser.wav")

w, h = 1000, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Space Shooter")

star = pygame.image.load("images/star.png").convert_alpha()
player_img = pygame.image.load("images/player.png").convert_alpha()
meteor_img = pygame.image.load("images/meteor.png").convert_alpha()
laser_img = pygame.image.load("images/laser.png").convert_alpha()

player_rect = player_img.get_rect(center=(w//2, 500))

clock = pygame.time.Clock()
player_speed = 300
laser_speed = 350
meteor_speed = 180

lasers = []
meteors = []
spawn_timer = 0
score = 0
font = pygame.font.Font(None, 40)

running = True

while running:
    dt = clock.tick(60) / 1000

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    move_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    move_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]

    player_rect.x += move_x * player_speed * dt
    player_rect.y += move_y * player_speed * dt
    player_rect.x = max(0, min(player_rect.x, w - player_rect.width))
    player_rect.y = max(0, min(player_rect.y, h - player_rect.height))

    if keys[pygame.K_SPACE]:
        laser_rect = laser_img.get_rect(midbottom=player_rect.midtop)
        lasers.append(laser_rect)
        laser_sound.play()

    spawn_timer += dt
    if spawn_timer > 0.6:
        x = random.randint(0, w - meteor_img.get_width())
        m = meteor_img.get_rect(topleft=(x, -50))
        meteors.append(m)
        spawn_timer = 0

    for l in lasers[:]:
        l.y -= laser_speed * dt
        if l.bottom < 0:
            lasers.remove(l)

    for m in meteors[:]:
        m.y += meteor_speed * dt
        if m.top > h:
            meteors.remove(m)

    for m in meteors[:]:
        for l in lasers[:]:
            if m.colliderect(l):
                meteors.remove(m)
                lasers.remove(l)
                score += 1
                break

    for m in meteors:
        if m.colliderect(player_rect):
            score = 0
            meteors.clear()
            lasers.clear()
            player_rect.center = (w//2, 500)

    screen.fill("black")

    for _ in range(40):
        screen.blit(star, (random.randint(0, w), random.randint(0, h)))

    for l in lasers:
        screen.blit(laser_img, l)

    for m in meteors:
        screen.blit(meteor_img, m)

    screen.blit(player_img, player_rect)

    score_text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
