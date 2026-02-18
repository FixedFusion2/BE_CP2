import pygame
import sys
from enum import Enum

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
GRAVITY = 0.6
JUMP_STRENGTH = -12

class PlayerState(Enum):
    IDLE = 1
    RUNNING = 2
    JUMPING = 3

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 48))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.vel_x = 0
        self.state = PlayerState.IDLE
        self.on_ground = False

    def handle_input(self, keys):
        self.vel_x = 0
        if keys[pygame.K_LEFT]:
            self.vel_x = -5
            self.state = PlayerState.RUNNING
        if keys[pygame.K_RIGHT]:
            self.vel_x = 5
            self.state = PlayerState.RUNNING
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = JUMP_STRENGTH
            self.state = PlayerState.JUMPING
            self.on_ground = False
        if self.vel_x == 0 and self.on_ground:
            self.state = PlayerState.IDLE

    def update(self, platforms):
        self.rect.x += self.vel_x
        self.check_collisions(platforms, 'horizontal')
        
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y
        self.on_ground = False
        self.check_collisions(platforms, 'vertical')

    def check_collisions(self, platforms, direction):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if direction == 'vertical':
                    if self.vel_y > 0:
                        self.rect.bottom = platform.rect.top
                        self.vel_y = 0
                        self.on_ground = True
                    elif self.vel_y < 0:
                        self.rect.top = platform.rect.bottom
                        self.vel_y = 0
                elif direction == 'horizontal':
                    if self.vel_x > 0:
                        self.rect.right = platform.rect.left
                    elif self.vel_x < 0:
                        self.rect.left = platform.rect.right

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=(x, y))

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Mario Platformer")
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.player = Player(100, SCREEN_HEIGHT - 150)
        self.platforms = pygame.sprite.Group()
        self.create_level()

    def create_level(self):
        self.platforms.add(Platform(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40))
        self.platforms.add(Platform(150, 450, 200, 20))
        self.platforms.add(Platform(500, 350, 200, 20))
        self.platforms.add(Platform(250, 250, 150, 20))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)
        self.player.update(self.platforms)

    def draw(self):
        self.screen.fill((135, 206, 235))
        self.platforms.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()