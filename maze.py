'''import pygame
import random

pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Лабиринт')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

# параметры стен и дверей
line_width = 10
line_gap = 40
line_offset = 20
door_width = 20
door_gap = 40
max_openings_per_line = 5

# параметры и стартовая позиция игрока
player_radius = 10
player_speed = 5
player_x = screen_width - 12
player_y = screen_height - line_offset

# рисуем стены и двери
lines = []
for i in range(0, screen_width, line_gap):
    rect = pygame.Rect(i, 0, line_width, screen_height)
    num_openings = random.randint(1, max_openings_per_line)
    if num_openings == 1:
        # одна дверь посередине стены
        door_pos = random.randint(line_offset + door_width, screen_height - line_offset - door_width)
        lines.append(pygame.Rect(i, 0, line_width, door_pos - door_width))
        lines.append(pygame.Rect(i, door_pos + door_width, line_width, screen_height - door_pos - door_width))
    else:
        # несколько дверей
        opening_positions = [0] + sorted([random.randint(line_offset + door_width, screen_height - line_offset - door_width) for _ in range(num_openings-1)]) + [screen_height]
        for j in range(num_openings):
            lines.append(pygame.Rect(i, opening_positions[j], line_width, opening_positions[j+1]-opening_positions[j]-door_width))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # передвижение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > player_radius:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < screen_width - player_radius:
        player_x += player_speed
    elif keys[pygame.K_UP] and player_y > player_radius:
        player_y -= player_speed
    elif keys[pygame.K_DOWN] and player_y < screen_height - player_radius:
        player_y += player_speed

    # проверка столкновений игрока со стенами
    player_rect = pygame.Rect(player_x - player_radius, player_y - player_radius, player_radius * 2, player_radius * 2)
    for line in lines:
        if line.colliderect(player_rect):
            # в случае столкновения возвращаем игрока назад
            if player_x > line.left and player_x < line.right:
                if player_y < line.top:
                    player_y = line.top - player_radius
                else:
                    player_y = line.bottom + player_radius
            elif player_y > line.top and player_y < line.bottom:
                if player_x < line.left:
                    player_x = line.left - player_radius
                else:
                    player_x = line.right + player_radius
    screen.fill(black)
    for line in lines:
        pygame.draw.rect(screen, green, line)
    pygame.draw.circle(screen, red, (player_x, player_y), player_radius)
    pygame.display.update()
    clock.tick(60)'''

'''import pygame

import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)

# Создание окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Персонаж на тропинке")

# Загрузка изображений
background_image = pygame.image.load("background.png")
character_image = pygame.image.load("wall.png")

# Начальные координаты персонажа
character_x = 50
character_y = WINDOW_HEIGHT - character_image.get_height()

# Скорость движения персонажа
character_speed = 5

# Главный цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение персонажа
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed

    # Отрисовка фона и персонажа
    window.fill(WHITE)
    window.blit(background_image, (0, 0))  # Рисуем фон
    window.blit(character_image, (character_x, character_y))  # Рисуем персонажа

    # Обновление экрана
    pygame.display.update()

    # Задержка для контроля скорости обновления экрана
    pygame.time.delay(30)

# Завершение работы Pygame
pygame.quit()
sys.exit()'''



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

# Camera offset
camera_offset_x = 0
camera_offset_y = 0

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
  
    # Update camera position to keep the player centered
    camera_offset_x = player.rect.x - 320
    camera_offset_y = player.rect.y - 240

    if player.rect.colliderect(coin_rect): 
        pygame.quit() 
        sys.exit() 
  
    # Draw background image
    screen.blit(background_image, (0, 0))

    # Draw walls
    for wall in walls: 
        screen.blit(wall.image, (wall.rect.x - camera_offset_x, wall.rect.y - camera_offset_y))

    # Draw player and coin
    pygame.draw.rect(screen, (255, 215, 0), (coin_rect.x - camera_offset_x, coin_rect.y - camera_offset_y, coin_rect.width, coin_rect.height)) 
    pygame.draw.rect(screen, (245, 69, 0), (player.rect.x - camera_offset_x, player.rect.y - camera_offset_y, player.rect.width, player.rect.height)) 

    pygame.display.flip() 

pygame.quit()
'''



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

# Camera offset
camera_offset_x = 0
camera_offset_y = 0

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
  
    # Update camera position based on player's position
    camera_offset_x = player.rect.x - screen.get_width() / 2 + player.rect.width / 2
    camera_offset_y = player.rect.y - screen.get_height() / 2 + player.rect.height / 2

    if player.rect.colliderect(coin_rect): 
        pygame.quit() 
        sys.exit() 
  
    # Draw background image with camera offset
    screen.blit(background_image, (-camera_offset_x, -camera_offset_y))

    # Draw walls with camera offset
    for wall in walls: 
        screen.blit(wall.image, (wall.rect.x - camera_offset_x, wall.rect.y - camera_offset_y))

    # Draw player and coin with camera offset
    pygame.draw.rect(screen, (255, 215, 0), (coin_rect.x - camera_offset_x, coin_rect.y - camera_offset_y, coin_rect.width, coin_rect.height)) 
    pygame.draw.rect(screen, (245, 69, 0), (player.rect.x - camera_offset_x, player.rect.y - camera_offset_y, player.rect.width, player.rect.height)) 

    pygame.display.flip() 

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

wall_image = pygame.image.load("wall.png").convert()
background_image = pygame.image.load("background.png").convert()

background_image = pygame.transform.scale(background_image, (1920,1080))

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

camera_offset_x = 0
camera_offset_y = 0

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
  
    # camera.pos
    camera_offset_x = player.rect.x - screen.get_width() / 2 + player.rect.width / 2
    camera_offset_y = player.rect.y - screen.get_height() / 2 + player.rect.height / 2

    if player.rect.colliderect(coin_rect): 
        pygame.quit() 
        sys.exit() 
  
    # Draw background image with camera offset
    screen.blit(background_image, (-camera_offset_x, -camera_offset_y))

    # Draw walls with camera offset
    for wall in walls: 
        screen.blit(wall.image, (wall.rect.x - camera_offset_x, wall.rect.y - camera_offset_y))

    # Draw player and coin with camera offset
    pygame.draw.rect(screen, (255, 215, 0), (coin_rect.x - camera_offset_x, coin_rect.y - camera_offset_y, coin_rect.width, coin_rect.height)) 
    pygame.draw.rect(screen, (245, 69, 0), (player.rect.x - camera_offset_x, player.rect.y - camera_offset_y, player.rect.width, player.rect.height)) 

    pygame.display.flip() 

pygame.quit()



