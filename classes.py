import pygame

class Player(pygame.sprite.Sprite):
<<<<<<< HEAD
    def __init__(self, x, y):
        super().__init__()
        capybara_image = pygame.image.load("graphics/jami.png").convert()
        capybara_image.set_colorkey((255, 255, 255))
=======
    def __init__(self, x, y, image_path):
        super().__init__()
        capybara_image = pygame.image.load("capybara.png").convert_alpha()
        self.image = capybara_image
>>>>>>> d11f7dd0afd729200b2f1d6e896ae9eec951642d
        self.image = pygame.transform.scale(capybara_image, (capybara_image.get_width() * 2, capybara_image.get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
<<<<<<< HEAD
        
    
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
=======
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
>>>>>>> d11f7dd0afd729200b2f1d6e896ae9eec951642d

    def apply_gravity(self):
        self.gravity += 0.1
        self.rect.y += self.gravity
        if self.rect.bottom < 300:
            self.rect.bottom = 300

    def update(self):
        self.player_input()
<<<<<<< HEAD
        # self.apply_gravity()
=======
        self.apply_gravity()
>>>>>>> d11f7dd0afd729200b2f1d6e896ae9eec951642d
