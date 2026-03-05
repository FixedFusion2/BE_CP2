import pygame
import random
import sys

pygame.init()

# Constants
SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 1000
FPS = 60
GRAVITY = 0.6
JUMP_STRENGTH = -20
PLAYER_SPEED = 5
ENEMY_SPEED = 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.vel_x = 0
        self.on_ground = False

    def update(self, platforms, enemies):
        keys = pygame.key.get_pressed()
        self.vel_x = 0
        
        if keys[pygame.K_LEFT]:
            self.vel_x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.vel_x = PLAYER_SPEED
        if keys[pygame.K_UP] and self.on_ground:
            self.vel_y = JUMP_STRENGTH
            self.on_ground = False

        self.vel_y += GRAVITY
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        self.on_ground = False
        for platform in platforms:
            if (self.rect.bottom >= platform.rect.top and 
                self.rect.bottom <= platform.rect.top + 10 and
                self.vel_y >= 0 and
                self.rect.right > platform.rect.left and
                self.rect.left < platform.rect.right):
                self.vel_y = 0
                self.rect.bottom = platform.rect.top
                self.on_ground = True

        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                if self.vel_y > 0 and self.rect.bottom <= enemy.rect.top + 15:
                    enemy.kill()
                    self.vel_y = JUMP_STRENGTH
                else:
                    return False
        
        if self.rect.top > SCREEN_HEIGHT:
            return False
        
        return True

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, direction=1):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = direction
        self.vel_y = 0

    def update(self, platforms):
        self.vel_y += GRAVITY
        self.rect.x += self.direction * ENEMY_SPEED
        self.rect.y += self.vel_y

        on_ground = False
        for platform in platforms:
            if (self.rect.bottom >= platform.rect.top and 
                self.rect.bottom <= platform.rect.top + 10 and
                self.vel_y >= 0 and
                self.rect.right > platform.rect.left and
                self.rect.left < platform.rect.right):
                self.vel_y = 0
                self.rect.bottom = platform.rect.top
                on_ground = True

        if not on_ground:
            if self.rect.top > SCREEN_HEIGHT:
                self.kill()
                return

        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.direction *= -1

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect(topleft=(x, y))

class Flag(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 50))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(topleft=(x, y))

def generate_level(level_num):
    platforms = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    
    # Ground
    platforms.add(Platform(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40))
    
    # Random platforms
    for _ in range(20 + level_num):
        x = random.randint(0, SCREEN_WIDTH - 100)
        y = random.randint(100, SCREEN_HEIGHT - 150)
        w = random.randint(80, 150)
        platforms.add(Platform(x, y, w, 20))
    
    # Random enemies (more enemies at higher levels)
    for _ in range(3 + level_num):
        x = random.randint(0, SCREEN_WIDTH - 25)
        y = random.randint(50, SCREEN_HEIGHT - 150)
        enemies.add(Enemy(x, y, random.choice([-1, 1])))
    
    # Flag at the top
    flag_x = random.randint(50, SCREEN_WIDTH - 50)
    flag = Flag(flag_x, 20)
    
    return platforms, enemies, flag

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Platformer Game")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    
    level = 1
    player = Player(50, SCREEN_HEIGHT - 100)
    platforms, enemies, flag = generate_level(level)
    
    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        alive = player.update(platforms, enemies)
        if not alive:
            level = 1
            player = Player(50, SCREEN_HEIGHT - 100)
            platforms, enemies, flag = generate_level(level)
            continue
        
        for enemy in enemies:
            enemy.update(platforms)
        
        # Check if flag reached
        if player.rect.colliderect(flag.rect):
            level += 1
            player = Player(50, SCREEN_HEIGHT - 100)
            platforms, enemies, flag = generate_level(level)
        
        # Draw
        screen.fill(WHITE)
        platforms.draw(screen)
        enemies.draw(screen)
        screen.blit(player.image, player.rect)
        screen.blit(flag.image, flag.rect)
        
        level_text = font.render(f"Level: {level}", True, BLACK)
        screen.blit(level_text, (10, 10))
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()