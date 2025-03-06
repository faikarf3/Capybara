import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        capybara_image = pygame.image.load("graphics/jami.png").convert()
        capybara_image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(capybara_image, (capybara_image.get_width() * 2, capybara_image.get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
        #     self.gravity = -10
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

    def apply_gravity(self):
        self.gravity += 0.1
        self.rect.y += self.gravity
        if self.rect.bottom < 300:
            self.rect.bottom = 300

    def update(self):
        self.player_input()
        # self.apply_gravity()
