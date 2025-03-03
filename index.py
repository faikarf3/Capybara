import pygame
from classes import Player

pygame.init()


screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Capybara Game")  # Set window title
background_color = (30, 30, 30)  # Background color

player = Player(300, 300, "capybara.png")

all_sprites = pygame.sprite.Group()
all_sprites.add(player)


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()

    # Draw everything
    screen.fill(background_color)  # Fill screen with background color
    all_sprites.draw(screen)  # Draw sprites

    pygame.display.flip()  # Refresh the display

    

    clock.tick(60)

pygame.quit()