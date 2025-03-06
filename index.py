import pygame
from classes import Player
<<<<<<< HEAD
from Camera import *
from pytmx.util_pygame import load_pygame
from abc import ABC, abstractmethod


def blit_all_tiles(window, tmxdata, camera):   
    for layer in tmxdata:
        for tile in layer.tiles():
            scaled_tile = pygame.transform.scale(tile[2], (32, 32))
            x_pixel = tile[0] * 32 - camera.offset.x
            y_pixel = tile[1] * 32 - camera.offset.y
            window.blit(scaled_tile, (x_pixel, y_pixel))






pygame.init()
pygame.display.set_mode((1, 1))  # Small dummy display to allow image conversion

vec = pygame.math.Vector2
# Load the TMX file
tmxdata = load_pygame("graphics/map.tmx") 
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Capybara Game")  # Set window title

player = Player(300, 300)

camera = Camera(player)
follow = Follow(camera, player)
camera.setmethod(follow)
=======

pygame.init()


screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Capybara Game")  # Set window title
background_color = (30, 30, 30)  # Background color

player = Player(300, 300, "capybara.png")
>>>>>>> d11f7dd0afd729200b2f1d6e896ae9eec951642d

all_sprites = pygame.sprite.Group()
all_sprites.add(player)


running = True
clock = pygame.time.Clock()

<<<<<<< HEAD
world_offset = [0,0]

while running:
    
=======
while running:
>>>>>>> d11f7dd0afd729200b2f1d6e896ae9eec951642d
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()

    # Draw everything
<<<<<<< HEAD
    screen.fill((0, 0, 0))  # Fill screen with black before drawing

    blit_all_tiles(screen, tmxdata, camera)

    camera.scroll()
    player_pos = (screen.get_width() // 2 - player.image.get_width() // 2, 
              screen.get_height() // 2 - player.image.get_height() // 2)
    screen.blit(player.image, player_pos)


=======
    screen.fill(background_color)  # Fill screen with background color
    all_sprites.draw(screen)  # Draw sprites
>>>>>>> d11f7dd0afd729200b2f1d6e896ae9eec951642d

    pygame.display.flip()  # Refresh the display

    

    clock.tick(60)

pygame.quit()