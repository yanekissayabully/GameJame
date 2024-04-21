'''import os 
import sys 
import random 
import pygame 

class Player(object):   
    def __init__(self): 
        self.rect = pygame.Rect(32, 32, 16, 16) 
  
    def move(self, dx, dy):  
        if dx != 0: 
            self.move_single_axis(dx, 0) 
        if dy != 0: 
            self.move_single_axis(0, dy) 
     
    def move_single_axis(self, dx, dy): 
        self.rect.x += dx 
        self.rect.y += dy 
  
        for wall in walls: 
            if self.rect.colliderect(wall.rect): 
                if dx > 0:
                    self.rect.right = wall.rect.left 
                if dx < 0:
                    self.rect.left = wall.rect.right 
                if dy > 0:
                    self.rect.bottom = wall.rect.top 
                if dy < 0: 
                    self.rect.top = wall.rect.bottom 
  
class Wall(object): 
    def __init__(self, pos): 
        walls.append(self) 
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16) 
os.environ["SDL_VIDEO_CENTERED"] = "1" 
pygame.init() 
pygame.display.set_caption("KBTU MAZE!") 
screen = pygame.display.set_mode((640, 480)) 
  
clock = pygame.time.Clock() 
walls = []
player = Player()
level = [ 
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", 
    "W                                      W", 
    "W         WWWWWW                       W", 
    "W   WWWW       W                       W", 
    "W   W        WWWW                      W", 
    "W WWW  WWWW                            W", 
    "W   W     W W W  W                     W", 
    "W   W     W   WWW W                    W", 
    "W   WWW WWW   W W                      W", 
    "W     W   W   W W                      W", 
    "WWW   W   WWWWW W                      W", 
    "W W      WW                            W", 
    "W W   WWWW   WWW                       W", 
    "W                                      W",
    "W     W       W                        W", 
    "W                                      W", 
    "W                                      W",
    "W                WWWWWWWWWWWWWWWWWW    W",
    "W                                      W",
    "W                                      W",
    "W                                      W",
    "W                                      W",
    "W         WW               WW          W",
    "W                                      W",
    "W                                      W",
    "W                              E       W",
    "W                                      W",
    "W                 WWWW                 W",
    "W                                      W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
] 

x = y = 0 
for row in level: 
    for col in row: 
        if col == "W": 
            Wall((x, y)) 
        if col == "E": 
            coin_rect = pygame.Rect(x, y, 16, 16) 
        x += 16 
    y += 16 
    x = 0 
  
running = True 
while running: 
     
    clock.tick(60) 
     
    for e in pygame.event.get(): 
        if e.type == pygame.QUIT: 
            running = False 
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: 
            running = False 

    key = pygame.key.get_pressed() 
    if key[pygame.K_LEFT]: 
        player.move(-2, 0) 
    if key[pygame.K_RIGHT]: 
        player.move(2, 0) 
    if key[pygame.K_UP]: 
        player.move(0, -2) 
    if key[pygame.K_DOWN]: 
        player.move(0, 2) 
  
    if player.rect.colliderect(coin_rect): 
        pygame.quit() 
        sys.exit() 
  
    screen.fill((0, 0, 0)) 
    for wall in walls: 
        pygame.draw.rect(screen, (1, 48, 3), wall.rect) 
    pygame.draw.rect(screen, (255, 215, 0), coin_rect) 
    pygame.draw.rect(screen, (245, 69, 0), player.rect) 
    pygame.display.flip() 
    clock.tick(144)

pygame.quit()'''

'''import os 
import sys 
import random 
import pygame 

class Player(object):   
    def __init__(self): 
        self.rect = pygame.Rect(32, 32, 16, 16) 
  
    def move(self, dx, dy):  
        if dx != 0: 
            self.move_single_axis(dx, 0) 
        if dy != 0: 
            self.move_single_axis(0, dy) 
     
    def move_single_axis(self, dx, dy): 
        self.rect.x += dx 
        self.rect.y += dy 
  
        for wall in walls: 
            if self.rect.colliderect(wall.rect): 
                if dx > 0:
                    self.rect.right = wall.rect.left 
                if dx < 0:
                    self.rect.left = wall.rect.right 
                if dy > 0:
                    self.rect.bottom = wall.rect.top 
                if dy < 0: 
                    self.rect.top = wall.rect.bottom 
  
class Wall(object): 
    def __init__(self, pos, image): 
        walls.append(self) 
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        self.image = image

os.environ["SDL_VIDEO_CENTERED"] = "1" 
pygame.init() 
pygame.display.set_caption("KBTU MAZE!") 
screen = pygame.display.set_mode((1000, 480)) 
  
clock = pygame.time.Clock() 
walls = []
player = Player()
level = [ 
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW", 
    "W                                      W", 
    "W         WWWWWW                       W", 
    "W   WWWW       W                       W", 
    "W   W        WWWW                      W", 
    "W WWW  WWWW                            W", 
    "W   W     W W W  W                     W", 
    "W   W     W   WWW W                    W", 
    "W   WWW WWW   W W                      W", 
    "W     W   W   W W                      W", 
    "WWW   W   WWWWW W                      W", 
    "W W      WW                            W", 
    "W W   WWWW   WWW                       W", 
    "W                                      W",
    "W     W       W                        W", 
    "W                                      W", 
    "W                                      W",
    "W                WWWWWWWWWWWWWWWWWW    W",
    "W                                      W",
    "W                                      W",
    "W                                      W",
    "W                                      W",
    "W         WW               WW          W",
    "W                                      W",
    "W                                      W",
    "W                              E       W",
    "W                                      W",
    "W                 WWWW                 W",
    "W                                      W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
] 

# Load wall image
wall_image = pygame.image.load("wall.png").convert()

x = y = 0 
for row in level: 
    for col in row: 
        if col == "W": 
            Wall((x, y), wall_image) 
        if col == "E": 
            coin_rect = pygame.Rect(x, y, 16, 16) 
        x += 16 
    y += 16 
    x = 0 
  
running = True 
while running: 
     
    clock.tick(60) 
     
    for e in pygame.event.get(): 
        if e.type == pygame.QUIT: 
            running = False 
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: 
            running = False 

    key = pygame.key.get_pressed() 
    if key[pygame.K_LEFT]: 
        player.move(-2, 0) 
    if key[pygame.K_RIGHT]: 
        player.move(2, 0) 
    if key[pygame.K_UP]: 
        player.move(0, -2) 
    if key[pygame.K_DOWN]: 
        player.move(0, 2) 
  
    if player.rect.colliderect(coin_rect): 
        pygame.quit() 
        sys.exit() 
  
    screen.fill((0, 0, 0)) 
    for wall in walls: 
        screen.blit(wall.image, wall.rect)
    pygame.draw.rect(screen, (255, 215, 0), coin_rect) 
    pygame.draw.rect(screen, (245, 69, 0), player.rect) 
    pygame.display.flip() 
    clock.tick(144)

pygame.quit()'''


import os 
import sys 
import random 
import pygame 

class Player(object):   
    def __init__(self): 
        self.rect = pygame.Rect(32, 32, 16, 16) 
  
    def move(self, dx, dy):  
        if dx != 0: 
            self.move_single_axis(dx, 0) 
        if dy != 0: 
            self.move_single_axis(0, dy) 
     
    def move_single_axis(self, dx, dy): 
        self.rect.x += dx 
        self.rect.y += dy 
  
        for wall in walls: 
            if self.rect.colliderect(wall.rect): 
                if dx > 0:
                    self.rect.right = wall.rect.left 
                if dx < 0:
                    self.rect.left = wall.rect.right 
                if dy > 0:
                    self.rect.bottom = wall.rect.top 
                if dy < 0: 
                    self.rect.top = wall.rect.bottom 
  
class Wall(object): 
    def __init__(self, pos, image): 
        walls.append(self) 
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        self.image = image

os.environ["SDL_VIDEO_CENTERED"] = "1" 
pygame.init() 
pygame.display.set_caption("KBTU MAZE!") 
screen = pygame.display.set_mode((1000, 480)) 
  
clock = pygame.time.Clock() 
walls = []
player = Player()
level = [ 
    "WWWWWWWWWWWWWWWWWWWWWWW", 
    "W                     W", 
    "W         WWWWWW      W", 
    "W   WWWW       W      W", 
    "W   W                 W", 
    "W WWW  WWWW           W", 
    "W   W                 W", 
    "W   W                 W", 
    "W   WWW WWW           W", 
    "W     W   W   W W     W", 
    "WWW   W               W", 
    "W W                   W", 
    "W W   WWW             W", 
    "W                     W",
    "W     W       W       W", 
    "W                     W", 
    "W                     W",
    "W                     W",
    "W                     W",
    "W                     W",
    "W                     W",
    "W                     W",
    "W         WW          W",
    "W                     W",
    "W                     W",
    "W          E          W",
    "W                     W",
    "W                 WWW W",
    "W                     W",
    "WWWWWWWWWWWWWWWWWWWWWWW",
] 

# Load wall and background images
wall_image = pygame.image.load("wall.png").convert()
background_image = pygame.image.load("background.png").convert()

x = y = 0 
for row in level: 
    for col in row: 
        if col == "W": 
            Wall((x, y), wall_image) 
        if col == "E": 
            coin_rect = pygame.Rect(x, y, 16, 16) 
        x += 16 
    y += 16 
    x = 0 
  
running = True 
while running: 
     
    clock.tick(60) 
     
    for e in pygame.event.get(): 
        if e.type == pygame.QUIT: 
            running = False 
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: 
            running = False 

    key = pygame.key.get_pressed() 
    if key[pygame.K_LEFT]: 
        player.move(-2, 0) 
    if key[pygame.K_RIGHT]: 
        player.move(2, 0) 
    if key[pygame.K_UP]: 
        player.move(0, -2) 
    if key[pygame.K_DOWN]: 
        player.move(0, 2) 
  
    if player.rect.colliderect(coin_rect): 
        pygame.quit() 
        sys.exit() 
  
    screen.blit(background_image, (0, 0)) 
    for wall in walls: 
        screen.blit(wall.image, wall.rect)
    pygame.draw.rect(screen, (255, 215, 0), coin_rect) 
    pygame.draw.rect(screen, (245, 69, 0), player.rect) 
    pygame.display.flip() 
    clock.tick(144)

pygame.quit()

