import pygame
import pytmx

# Initialize pygame
pygame.init()
pygame.display.set_mode((1, 1))  # Small dummy display to allow image conversion

# Load the TMX file
tmxdata = pytmx.util_pygame.load_pygame("graphics/map.tmx")

# Continue with the rest of your game logic...
