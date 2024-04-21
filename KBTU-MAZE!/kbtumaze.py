'''
import pygame
import sys
import random

# Initialize Pygame
pygame.init()
pygame.display.set_caption("KBTU MAZE!")

# Define constants
WIDTH, HEIGHT = 1000, 480
BACKGROUND_SCALE = 2
PLAYER_RUN_FRAMES = 8
COIN_COUNT = 10
TIMER_POS = (WIDTH - 100, 10)
COIN_COUNT_POS = (WIDTH - 200, 10)
PLAYER_VELOCITY = 5
PLAYER_RUN_VELOCITY = 10
PLAYER_RUN_FRAME_DELAY = 5
PLAYER_WIDTH, PLAYER_HEIGHT = 30, 60

# Initialize the game display mode
game_display = pygame.display.set_mode((WIDTH, HEIGHT))

# Load images after setting display mode
background = pygame.image.load('kbtu_map.png').convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
player_stationary = pygame.image.load('character_standing-removebg-preview.png').convert_alpha()  # Changed to use alpha channel
player_stationary = pygame.transform.scale(player_stationary, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_run_sheet = pygame.image.load('character_running-removebg-preview.png').convert_alpha()  # Changed to use alpha channel
player_run_sheet = pygame.transform.scale(player_run_sheet, (PLAYER_WIDTH, PLAYER_HEIGHT))
coin = pygame.image.load('coin.png').convert_alpha()
coin = pygame.transform.scale(coin, (15, 15))

# Initialize variables
player_run_frame = 0
player_run_frame_time = 0
coin_objects = []
coin_count = 0
clock = pygame.time.Clock()
game_active = True  # Initially, the game is active

# Set player's initial position to a random location
player_rect = player_stationary.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))

# Load background music and play in loop
pygame.mixer.music.load('backsound.mp3')
pygame.mixer.music.play(-1)

# Create a function to add coins to the list
def add_coin(x, y):
    coin_objects.append(pygame.Rect(x, y, coin.get_width(), coin.get_height()))

# Create a function to draw all coins
def draw_coins(screen):
    for coin_rect in coin_objects:
        screen.blit(coin, (coin_rect.x, coin_rect.y))

# Create a function to check for collisions between the player and coins
def check_collisions():
    global coin_count
    for coin_rect in coin_objects[:]:
        if player_rect.colliderect(coin_rect):
            coin_objects.remove(coin_rect)
            coin_count += 1

# Create a function to draw the timer and coin count
def draw_timer_and_coin_count(screen):
    timer_text = font.render(str(int(clock.get_time() / 60)), True, (255, 255, 255))
    screen.blit(timer_text, TIMER_POS)
    coin_count_text = font.render(str(coin_count), True, (255, 255, 255))
    screen.blit(coin_count_text, COIN_COUNT_POS)

# Create a function to check for input and move the player
def handle_input():
    global player_rect
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.y > 0:
        player_rect.y -= PLAYER_VELOCITY
    elif keys[pygame.K_DOWN] and player_rect.y < HEIGHT - player_rect.height:
        player_rect.y += PLAYER_VELOCITY
    elif keys[pygame.K_LEFT] and player_rect.x > 0:
        player_rect.x -= PLAYER_VELOCITY
    elif keys[pygame.K_RIGHT] and player_rect.x < WIDTH - player_rect.width:
        player_rect.x += PLAYER_VELOCITY

# Create a function to draw the player
def draw_player(screen):
    global player_run_frame  # Declare as global
    player_image = player_run_sheet if player_run_frame > 0 else player_stationary
    screen.blit(player_image, player_rect)

# Create a function to handle the game loop
def game_loop(screen):
    global player_run_frame, player_run_frame_time, game_active
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_active:
            handle_input()
            check_collisions()

        player_run_frame_time += 1
        if player_run_frame_time % PLAYER_RUN_FRAME_DELAY == 0:
            player_run_frame = (player_run_frame + 1) % PLAYER_RUN_FRAMES

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        draw_coins(screen)
        draw_player(screen)
        draw_timer_and_coin_count(screen)

        pygame.display.flip()
        clock.tick(60)

# Create a function to add coins to the list
def add_coins():
    for _ in range(COIN_COUNT):
        add_coin(random.randint(0, WIDTH - coin.get_width()), random.randint(0, HEIGHT - coin.get_height()))

# Initialize the game display
add_coins()
font = pygame.font.Font(None, 36)

# Start game loop
game_loop(game_display)'''



'''import pygame
import sys
import random

# Initialize Pygame
pygame.init()
pygame.display.set_caption("KBTU MAZE!")

# Define constants
WIDTH, HEIGHT = 1000, 480
BACKGROUND_SCALE = 2
PLAYER_RUN_FRAMES = 8
COIN_COUNT = 10
TIMER_POS = (WIDTH - 100, 10)
COIN_COUNT_POS = (WIDTH - 200, 10)
PLAYER_VELOCITY = 5
PLAYER_RUN_VELOCITY = 10
PLAYER_RUN_FRAME_DELAY = 5
PLAYER_WIDTH, PLAYER_HEIGHT = 30, 60

# Initialize the game display mode
game_display = pygame.display.set_mode((WIDTH, HEIGHT))

# Load images after setting display mode
background = pygame.image.load('kbtu_map.png').convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
player_stationary = pygame.image.load('character_standing-removebg-preview.png').convert_alpha()  # Changed to use alpha channel
player_stationary = pygame.transform.scale(player_stationary, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_run_sheet = pygame.image.load('character_running-removebg-preview.png').convert_alpha()  # Changed to use alpha channel
player_run_sheet = pygame.transform.scale(player_run_sheet, (PLAYER_WIDTH, PLAYER_HEIGHT))
coin = pygame.image.load('coin.png').convert_alpha()
coin = pygame.transform.scale(coin, (15, 15))

# Initialize variables
player_run_frame = 0
player_run_frame_time = 0
coin_objects = []
coin_count = 0
clock = pygame.time.Clock()
game_active = False  # Initially, the game is not active

# Set player's initial position to a random location
player_rect = player_stationary.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))

# Load background music and play in loop
pygame.mixer.music.load('backsound.mp3')
pygame.mixer.music.play(-1)

# Create a function to add coins to the list
def add_coin(x, y):
    coin_objects.append(pygame.Rect(x, y, coin.get_width(), coin.get_height()))

# Create a function to draw all coins
def draw_coins(screen):
    for coin_rect in coin_objects:
        screen.blit(coin, (coin_rect.x, coin_rect.y))

# Create a function to check for collisions between the player and coins
def check_collisions():
    global coin_count
    for coin_rect in coin_objects[:]:
        if player_rect.colliderect(coin_rect):
            coin_objects.remove(coin_rect)
            coin_count += 1
            if coin_count >= COIN_COUNT:
                game_win()

# Create a function to draw the timer and coin count
def draw_timer_and_coin_count(screen):
    timer_text = font.render(str(int(pygame.time.get_ticks() / 1000)), True, (255, 255, 255))
    screen.blit(timer_text, TIMER_POS)
    coin_count_text = font.render(str(coin_count), True, (255, 255, 255))
    screen.blit(coin_count_text, COIN_COUNT_POS)

# Create a function to check for input and move the player
def handle_input():
    global player_rect, game_active
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.y > 0:
        player_rect.y -= PLAYER_VELOCITY
    elif keys[pygame.K_DOWN] and player_rect.y < HEIGHT - player_rect.height:
        player_rect.y += PLAYER_VELOCITY
    elif keys[pygame.K_LEFT] and player_rect.x > 0:
        player_rect.x -= PLAYER_VELOCITY
    elif keys[pygame.K_RIGHT] and player_rect.x < WIDTH - player_rect.width:
        player_rect.x += PLAYER_VELOCITY
    elif keys[pygame.K_SPACE]:
        game_active = True

# Create a function to draw the player
def draw_player(screen):
    global player_run_frame  # Declare as global
    player_image = player_run_sheet if player_run_frame > 0 else player_stationary
    screen.blit(player_image, player_rect)

# Create a function to handle the game loop
def game_loop(screen):
    global player_run_frame, player_run_frame_time, game_active
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_active:
            handle_input()
            check_collisions()

        player_run_frame_time += 1
        if player_run_frame_time % PLAYER_RUN_FRAME_DELAY == 0:
            player_run_frame = (player_run_frame + 1) % PLAYER_RUN_FRAMES

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        draw_coins(screen)
        draw_player(screen)
        draw_timer_and_coin_count(screen)

        pygame.display.flip()
        clock.tick(60)

# Create a function to add coins to the list
def add_coins():
    for _ in range(COIN_COUNT):
        add_coin(random.randint(0, WIDTH - coin.get_width()), random.randint(0, HEIGHT - coin.get_height()))

# Create a function to display game win screen
def game_win():
    game_display.fill((0, 0, 0))
    win_text = font.render("You Win!", True, (255, 255, 255))
    game_display.blit(win_text, (WIDTH // 2 - 50, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# Initialize the game display
add_coins()
font = pygame.font.Font(None, 36)

# Display intro image
intro_image = pygame.image.load('image.png').convert_alpha()
intro_image = pygame.transform.scale(intro_image, (WIDTH, HEIGHT))
intro_active = True  # Flag to track if intro is active

while intro_active:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            intro_active = False  # Disable intro when spacebar is pressed

    game_display.blit(intro_image, (0, 0))
    pygame.display.flip()
    clock.tick(60)

# Start game loop
game_loop(game_display)
'''


'''import pygame
import sys
import random

# Инициализация Pygame
pygame.init()
pygame.display.set_caption("KBTU MAZE!")

# Определение констант
WIDTH, HEIGHT = 1000, 480
BACKGROUND_SCALE = 2
PLAYER_RUN_FRAMES = 8
COIN_COUNT = 10
TIMER_POS = (WIDTH - 100, 10)
COIN_COUNT_POS = (WIDTH - 200, 10)
PLAYER_VELOCITY = 5
PLAYER_RUN_VELOCITY = 10
PLAYER_RUN_FRAME_DELAY = 5
PLAYER_WIDTH, PLAYER_HEIGHT = 30, 60

# Инициализация игрового дисплея
game_display = pygame.display.set_mode((WIDTH, HEIGHT))

# Загрузка изображений после установки режима отображения
background = pygame.image.load('kbtu_map.png').convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
player_stationary = pygame.image.load('character_standing-removebg-preview.png').convert_alpha()  # Изменено для использования альфа-канала
player_stationary = pygame.transform.scale(player_stationary, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_run_sheet = pygame.image.load('character_running-removebg-preview.png').convert_alpha()  # Изменено для использования альфа-канала
player_run_sheet = pygame.transform.scale(player_run_sheet, (PLAYER_WIDTH, PLAYER_HEIGHT))
coin = pygame.image.load('coin.png').convert_alpha()
coin = pygame.transform.scale(coin, (15, 15))

# Инициализация переменных
player_run_frame = 0
player_run_frame_time = 0
coin_objects = []
coin_count = 0
clock = pygame.time.Clock()
game_active = True  # Изначально игра активна

# Установка начальной позиции игрока в случайном месте
player_rect = player_stationary.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))

# Загрузка фоновой музыки и воспроизведение в цикле
pygame.mixer.music.load('backsound.mp3')
pygame.mixer.music.play(-1)

# Создание функции для добавления монет в список
def add_coin(x, y):
    coin_objects.append(pygame.Rect(x, y, coin.get_width(), coin.get_height()))

# Создание функции для отрисовки всех монет
def draw_coins(screen):
    for coin_rect in coin_objects:
        screen.blit(coin, (coin_rect.x, coin_rect.y))

# Создание функции для проверки коллизий между игроком и монетами
def check_collisions():
    global coin_count
    for coin_rect in coin_objects[:]:
        if player_rect.colliderect(coin_rect):
            coin_objects.remove(coin_rect)
            coin_count += 1

# Создание функции для отрисовки таймера и количества монет
def draw_timer_and_coin_count(screen):
    timer_text = font.render(str(int(clock.get_time() / 60)), True, (255, 255, 255))
    screen.blit(timer_text, TIMER_POS)
    coin_count_text = font.render(str(coin_count), True, (255, 255, 255))
    screen.blit(coin_count_text, COIN_COUNT_POS)

# Создание функции для обработки ввода и движения игрока
def handle_input():
    global player_rect
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.y > 0:
        player_rect.y -= PLAYER_VELOCITY
    elif keys[pygame.K_DOWN] and player_rect.y < HEIGHT - player_rect.height:
        player_rect.y += PLAYER_VELOCITY
    elif keys[pygame.K_LEFT] and player_rect.x > 0:
        player_rect.x -= PLAYER_VELOCITY
    elif keys[pygame.K_RIGHT] and player_rect.x < WIDTH - player_rect.width:
        player_rect.x += PLAYER_VELOCITY

# Создание функции для отрисовки игрока
def draw_player(screen):
    global player_run_frame  # Объявление глобальной переменной
    player_image = player_run_sheet if player_run_frame > 0 else player_stationary
    screen.blit(player_image, player_rect)

# Создание функции для обработки игрового цикла
def game_loop(screen):
    global player_run_frame, player_run_frame_time, game_active
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_active:
            handle_input()
            check_collisions()

        player_run_frame_time += 1
        if player_run_frame_time % PLAYER_RUN_FRAME_DELAY == 0:
            player_run_frame = (player_run_frame + 1) % PLAYER_RUN_FRAMES

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        draw_coins(screen)
        draw_player(screen)
        draw_timer_and_coin_count(screen)

        pygame.display.flip()
        clock.tick(60)

# Создание функции для добавления монет в список
def add_coins():
    for _ in range(COIN_COUNT):
        add_coin(random.randint(0, WIDTH - coin.get_width()), random.randint(0, HEIGHT - coin.get_height()))

# Инициализация игрового дисплея
add_coins()
font = pygame.font.Font(None, 36)

# Отображение заставки
intro_image = pygame.image.load('image.png').convert_alpha()
intro_image = pygame.transform.scale(intro_image, (WIDTH, HEIGHT))
intro_active = True  # Флаг для отслеживания активности заставки

while intro_active:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            intro_active = False  # Отключение заставки при нажатии пробела

    game_display.blit(intro_image, (0, 0))
    pygame.display.flip()
    clock.tick(60)

# Начало игрового цикла
game_loop(game_display)
'''

'''import pygame
import sys
import random

# Инициализация Pygame
pygame.init()
pygame.display.set_caption("KBTU MAZE!")

# Определение констант
WIDTH, HEIGHT = 1000, 480
BACKGROUND_SCALE = 2
PLAYER_RUN_FRAMES = 8
COIN_COUNT = 10
TIMER_POS = (WIDTH - 100, 10)
COIN_COUNT_POS = (WIDTH - 200, 10)
PLAYER_VELOCITY = 5
PLAYER_RUN_VELOCITY = 10
PLAYER_RUN_FRAME_DELAY = 5
PLAYER_WIDTH, PLAYER_HEIGHT = 30, 60

# Инициализация игрового дисплея
game_display = pygame.display.set_mode((WIDTH, HEIGHT))

# Загрузка изображений после установки режима отображения
background = pygame.image.load('kbtu_map.png').convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
player_stationary = pygame.image.load('character_standing-removebg-preview.png').convert_alpha()  # Изменено для использования альфа-канала
player_stationary = pygame.transform.scale(player_stationary, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_run_sheet = pygame.image.load('character_running-removebg-preview.png').convert_alpha()  # Изменено для использования альфа-канала
player_run_sheet = pygame.transform.scale(player_run_sheet, (PLAYER_WIDTH, PLAYER_HEIGHT))
coin = pygame.image.load('coin.png').convert_alpha()
coin = pygame.transform.scale(coin, (15, 15))

# Инициализация переменных
player_run_frame = 0
player_run_frame_time = 0
coin_objects = []
coin_count = 0
clock = pygame.time.Clock()
game_active = True  # Изначально игра активна

# Установка начальной позиции игрока в случайном месте
player_rect = player_stationary.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))

# Загрузка фоновой музыки и воспроизведение в цикле
pygame.mixer.music.load('backsound.mp3')
pygame.mixer.music.play(-1)

# Создание функции для добавления монет в список
def add_coin(x, y):
    coin_objects.append(pygame.Rect(x, y, coin.get_width(), coin.get_height()))

# Создание функции для отрисовки всех монет
def draw_coins(screen):
    for coin_rect in coin_objects:
        screen.blit(coin, (coin_rect.x, coin_rect.y))

# Создание функции для проверки коллизий между игроком и монетами
def check_collisions():
    global coin_count
    for coin_rect in coin_objects[:]:
        if player_rect.colliderect(coin_rect):
            coin_objects.remove(coin_rect)
            coin_count += 1

# Создание функции для отрисовки таймера и количества монет
def draw_timer_and_coin_count(screen):
    timer_text = font.render(str(int(clock.get_time() / 60)), True, (255, 255, 255))
    screen.blit(timer_text, TIMER_POS)
    coin_count_text = font.render(str(coin_count), True, (255, 255, 255))
    screen.blit(coin_count_text, COIN_COUNT_POS)

# Создание функции для проверки ввода и движения игрока
def handle_input():
    global player_rect
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.y > 0:
        player_rect.y -= PLAYER_VELOCITY
    elif keys[pygame.K_DOWN] and player_rect.y < HEIGHT - player_rect.height:
        player_rect.y += PLAYER_VELOCITY
    elif keys[pygame.K_LEFT] and player_rect.x > 0:
        player_rect.x -= PLAYER_VELOCITY
    elif keys[pygame.K_RIGHT] and player_rect.x < WIDTH - player_rect.width:
        player_rect.x += PLAYER_VELOCITY

# Создание функции для отрисовки игрока
def draw_player(screen):
    global player_run_frame  # Объявление глобальной переменной
    player_image = player_run_sheet if player_run_frame > 0 else player_stationary
    screen.blit(player_image, player_rect)

# Создание функции для обработки игрового цикла
def game_loop(screen):
    global player_run_frame, player_run_frame_time, game_active
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_active:
            handle_input()
            check_collisions()

        player_run_frame_time += 1
        if player_run_frame_time % PLAYER_RUN_FRAME_DELAY == 0:
            player_run_frame = (player_run_frame + 1) % PLAYER_RUN_FRAMES

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        draw_coins(screen)
        draw_player(screen)
        draw_timer_and_coin_count(screen)

        # Проверка на победу
        if coin_count >= 10:
            game_active = False
            screen.fill((0, 0, 0))  # Очистка экрана
            win_text = font.render("WIN!", True, (255, 255, 255))
            screen.blit(win_text, (WIDTH - 550, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.delay(2000)  # Задержка перед завершением игры
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(60)

# Создание функции для добавления монет в список
def add_coins():
    for _ in range(COIN_COUNT):
        add_coin(random.randint(0, WIDTH - coin.get_width()), random.randint(0, HEIGHT - coin.get_height()))

# Инициализация игрового дисплея
add_coins()
font = pygame.font.Font(None, 36)

# Отображение заставки
intro_image = pygame.image.load('image.png').convert_alpha()
intro_image = pygame.transform.scale(intro_image, (WIDTH, HEIGHT))
intro_active = True  # Флаг для отслеживания активности заставки

while intro_active:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            intro_active = False  # Отключение заставки при нажатии пробела

    game_display.blit(intro_image, (0, 0))
    pygame.display.flip()
    clock.tick(60)

# Начало игрового цикла
game_loop(game_display)
'''

import pygame
import sys
import random

# Инициализация Pygame
pygame.init()
pygame.display.set_caption("KBTU MAZE!")

# Определение констант
WIDTH, HEIGHT = 1000, 480
BACKGROUND_SCALE = 2
PLAYER_RUN_FRAMES = 8
COIN_COUNT = 10
TIMER_POS = (WIDTH - 100, 10)
COIN_COUNT_POS = (WIDTH - 200, 10)
PLAYER_VELOCITY = 5
PLAYER_RUN_VELOCITY = 10
PLAYER_RUN_FRAME_DELAY = 5
PLAYER_WIDTH, PLAYER_HEIGHT = 30, 60

# Инициализация игрового дисплея
game_display = pygame.display.set_mode((WIDTH, HEIGHT))

# Загрузка изображений после установки режима отображения
background = pygame.image.load('kbtu_map.png').convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
player_stationary = pygame.image.load('character_standing-removebg-preview.png').convert_alpha()  # Изменено для использования альфа-канала
player_stationary = pygame.transform.scale(player_stationary, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_run_sheet = pygame.image.load('character_running-removebg-preview.png').convert_alpha()  # Изменено для использования альфа-канала
player_run_sheet = pygame.transform.scale(player_run_sheet, (PLAYER_WIDTH, PLAYER_HEIGHT))
coin = pygame.image.load('coin.png').convert_alpha()
coin = pygame.transform.scale(coin, (15, 15))

# Инициализация переменных
player_run_frame = 0
player_run_frame_time = 0
coin_objects = []
coin_count = 0
clock = pygame.time.Clock()
game_active = True  # Изначально игра активна

# Установка начальной позиции игрока в случайном месте
player_rect = player_stationary.get_rect(center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))

# Загрузка фоновой музыки и воспроизведение в цикле
pygame.mixer.music.load('backsound.mp3')
pygame.mixer.music.play(-1)

# Создание функции для добавления монет в список
def add_coin(x, y):
    coin_objects.append(pygame.Rect(x, y, coin.get_width(), coin.get_height()))

# Создание функции для отрисовки всех монет
def draw_coins(screen):
    for coin_rect in coin_objects:
        screen.blit(coin, (coin_rect.x, coin_rect.y))

# Создание функции для проверки коллизий между игроком и монетами
def check_collisions():
    global coin_count
    for coin_rect in coin_objects[:]:
        if player_rect.colliderect(coin_rect):
            coin_objects.remove(coin_rect)
            coin_count += 1

# Создание функции для отрисовки таймера и количества монет
def draw_timer_and_coin_count(screen):
    timer_text = font.render(str(int(clock.get_time() / 60)), True, (255, 255, 255))
    screen.blit(timer_text, TIMER_POS)
    coin_count_text = font.render(str(coin_count), True, (255, 255, 255))
    screen.blit(coin_count_text, COIN_COUNT_POS)

# Создание функции для проверки ввода и движения игрока
def handle_input():
    global player_rect
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.y > 0:
        player_rect.y -= PLAYER_VELOCITY
    elif keys[pygame.K_DOWN] and player_rect.y < HEIGHT - player_rect.height:
        player_rect.y += PLAYER_VELOCITY
    elif keys[pygame.K_LEFT] and player_rect.x > 0:
        player_rect.x -= PLAYER_VELOCITY
    elif keys[pygame.K_RIGHT] and player_rect.x < WIDTH - player_rect.width:
        player_rect.x += PLAYER_VELOCITY

# Создание функции для отрисовки игрока
def draw_player(screen):
    global player_run_frame  # Объявление глобальной переменной
    player_image = player_run_sheet if player_run_frame > 0 else player_stationary
    screen.blit(player_image, player_rect)

def display_menu(screen):
    font = pygame.font.Font(None, 36)
    menu_options = ["Continue", "Off sound", "Exit"]
    menu_y = HEIGHT // 2 - len(menu_options) * 30 // 2
    for option in menu_options:
        text = font.render(option, True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, menu_y))
        screen.blit(text, text_rect)
        menu_y += 30
    pygame.display.flip()

def handle_menu_input():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        # Обработка перемещения вверх по меню
        pass
    elif keys[pygame.K_DOWN]:
        # Обработка перемещения вниз по меню
        pass
    elif keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
        # Обработка выбора опции меню
        pass

# Создание функции для обработки игрового цикла
def game_loop(screen):
    global player_run_frame, player_run_frame_time, game_active
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    display_menu(screen)
                    handle_menu_input()

        if game_active:
            handle_input()
            check_collisions()

        player_run_frame_time += 1
        if player_run_frame_time % PLAYER_RUN_FRAME_DELAY == 0:
            player_run_frame = (player_run_frame + 1) % PLAYER_RUN_FRAMES

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        draw_coins(screen)
        draw_player(screen)
        draw_timer_and_coin_count(screen)

        # Проверка на победу
        if coin_count >= 10:
            game_active = False
            screen.fill((0, 0, 0))  # Очистка экрана
            win_text = font.render("WIN!", True, (255, 255, 255))
            screen.blit(win_text, (WIDTH - 550, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.delay(2000)  # Задержка перед завершением игры
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(60)

# Создание функции для добавления монет в список
def add_coins():
    for _ in range(COIN_COUNT):
        add_coin(random.randint(0, WIDTH - coin.get_width()), random.randint(0, HEIGHT - coin.get_height()))

# Инициализация игрового дисплея
add_coins()
font = pygame.font.Font(None, 36)

# Отображение заставки
intro_image = pygame.image.load('image.png').convert_alpha()
intro_image = pygame.transform.scale(intro_image, (WIDTH, HEIGHT))
intro_active = True  # Флаг для отслеживания активности заставки

while intro_active:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            intro_active = False  # Отключение заставки при нажатии пробела

    game_display.blit(intro_image, (0, 0))
    pygame.display.flip()
    clock.tick(60)

# Начало игрового цикла
game_loop(game_display)

