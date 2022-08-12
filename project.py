#importing stuff and initialising pygame
import pygame
from random import randint as rdt
import time
from pygame.locals import * 

pygame.init()

# defining variables like x, y, position & velocity
player = pygame.image.load("borb.jpg")
player_alt = pygame.image.load("seacat.jpg")

s_width = 800
s_height = 600

x = y = t = 0

pos = pygame.math.Vector2((0,0))
vel = pygame.math.Vector2((0,0))

clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((s_width,s_height))


#gameloop
running = True
while running:
    keys = pygame.key.get_pressed()
    mKeys = pygame.mouse.get_pressed()
    
    #exiting the game(work in progress :) )
    for event in pygame.event.get():
        if event == pygame.KEYDOWN:
            if event.key == K_BACKSPACE:
                running = False
    
    move_speed = 1

    if keys[pygame.K_SPACE] and pos.y == 0:
        vel.y = 20

    #calculating player height
    vel += pygame.math.Vector2((0, -9.81)) * t
    print(f"position = {pos}")
    t += 1/fps
    pos += vel

    #bounding the player
    x_max = s_width - player.get_width()

    if pos.x <= 0: pos.x = 0
    elif pos.x >= x_max: pos.x = x_max
    screen.fill((102, 229, 255))
    if pos.y <= 0:
        pos.y = 0
        vel.y = 0
        t = 0

        screen.blit(player, (pos.x, s_height - pos.y - player.get_height()))
    
    else:
        screen.blit(player_alt, (pos.x, s_height - pos.y - player.get_height()))

    """
    #if keys[K_s]:
       #y+=move_speed
    if keys[K_a]:
        x-=move_speed
    if keys[K_d]:
        x+=move_speed

    if x < 0: x = 0
    if y < 0: y = 0
    if x > s_width: x = s_width
    if y > s_height: x = s_height
    
    
    
    screen.blit(player.img, (x, y))

    pygame.display.flip()

    time.sleep(1/1000)
    """
    

    pygame.display.flip()
    clock.tick(fps)
pygame.quit()