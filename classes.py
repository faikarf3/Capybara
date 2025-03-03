import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        capybara_image = pygame.image.load("capybara.png").convert_alpha()
        self.image = capybara_image
        self.image = pygame.transform.scale(capybara_image, (capybara_image.get_width() * 2, capybara_image.get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.gravity = 0
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -10
        # if keys[pygame.K_LEFT]:
        #     self.rect.x -= self.speed
        # if keys[pygame.K_RIGHT]:
        #     self.rect.x += self.speed
        # if keys[pygame.K_UP]:
        #     self.rect.y -= self.speed
        # if keys[pygame.K_DOWN]:
        #     self.rect.y += self.speed

    def apply_gravity(self):
        self.gravity += 0.1
        self.rect.y += self.gravity
        if self.rect.bottom < 300:
            self.rect.bottom = 300

    def update(self):
        self.player_input()
        self.apply_gravity()
