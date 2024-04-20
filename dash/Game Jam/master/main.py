import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_SCALE = 2
BACKGROUND_IMAGE = 'path/to/background.png'
PLAYER_STATIONARY_IMAGE = 'path/to/player_stationary.png'
PLAYER_RUN_IMAGE = 'path/to/player_run.png'
PLAYER_RUN_FRAMES = 8
COIN_IMAGE = 'path/to/coin.png'
COIN_COUNT = 10
PAUSE_BUTTON_IMAGE = 'path/to/pause_button.png'
PAUSE_BUTTON_POS = (10, 10)
TIMER_FONT = 'path/to/font.ttf'
TIMER_POS = (WIDTH - 100, 10)
COIN_COUNT_POS = (WIDTH - 200, 10)
PLAYER_POS = (0, 0)
PLAYER_VELOCITY = 5
PLAYER_RUN_VELOCITY = 10
PLAYER_RUN_FRAME_DELAY = 5

# Load images
background = pygame.image.load(BACKGROUND_IMAGE).convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
player_stationary = pygame.image.load(PLAYER_STATIONARY_IMAGE).convert_alpha()
player_run_sheet = pygame.image.load(PLAYER_RUN_IMAGE).convert_alpha()
coin = pygame.image.load(COIN_IMAGE).convert_alpha()
pause_button = pygame.image.load(PAUSE_BUTTON_IMAGE).convert_alpha()

# Initialize variables
player_run_frame = 0
player_run_frame_time = 0
coin_objects = []
coin_count = 0
clock = pygame.time.Clock()
game_active = True
player_rect = player_stationary.get_rect()

# Create a function to add coins to the list
def add_coin(x, y):
    coin_objects.append(pygame.Rect(x, y, coin.get_width(), coin.get_height()))

# Create a function to draw all coins
def draw_coins():
    for coin in coin_objects:
        screen.blit(coin, (coin.x, coin.y))

# Create a function to check for collisions between the player and coins
def check_collisions():
    global coin_count
    for coin in coin_objects:
        if player_rect.colliderect(coin):
            coin_objects.remove(coin)
            coin_count += 1

# Create a function to draw the timer and coin count
def draw_timer_and_coin_count():
    timer_text = font.render(str(int(clock.get_time() / 60)), True, (255, 255, 255))
    screen.blit(timer_text, TIMER_POS)
    coin_count_text = font.render(str(coin_count), True, (255, 255, 255))
    screen.blit(coin_count_text, COIN_COUNT_POS)

# Create a function to check for input and move the player
def handle_input():
    global player_run_frame, player_run_frame_time
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.y > 0:
        player_rect.y -= PLAYER_VELOCITY
        player_run_frame_time += 1
        if player_run_frame_time % PLAYER_RUN_FRAME_DELAY == 0:
            player_run_frame = (player_run_frame + 1) % PLAYER_RUN_FRAMES
    if keys[pygame.K_DOWN] and player_rect.y < HEIGHT - player_rect.height:
        player_rect.y += PLAYER_VELOCITY
        player_run_frame_time += 1
        if player_run_frame_time % PLAYER_RUN_FRAME_DELAY == 0:
            player_run_frame = (player_run_frame + 1) % PLAYER_RUN_FRAMES
    if keys[pygame.K_LEFT] and player_rect.x > 0:
        player_rect.x -= PLAYER_VELOCITY
        player_run_frame_time += 1
        if player_run_frame_time % PLAYER_RUN_FRAME_DELAY == 0:
            player_run_frame = (player_run_frame + 1) % PLAYER_RUN_FRAMES
    if keys[pygame.K_RIGHT] and player_rect.x < WIDTH - player_rect.width:
        player_rect.x += PLAYER_VELOCITY
        player_run_frame_time += 1
        if player_run_frame_time % PLAYER_RUN_FRAME_DELAY == 0:
            player_run_frame = (player_run_frame + 1) % PLAYER_RUN_FRAMES

# Create a function to draw the player
def draw_player():
    if player_run_frame_time % PLAYER_RUN_FRAME_DELAY == 0:
        player_run_frame = (player_run_frame + 1) % PLAYER_RUN_FRAMES
    player_image = player_run_sheet.subsurface(pygame.Rect(player_run_frame * player_run_sheet.get_width() / PLAYER_RUN_FRAMES, 0, player_run_sheet.get_width() / PLAYER_RUN_FRAMES, player_run_sheet.get_height()))
    screen.blit(player_image, player_rect)

# Create a function to handle the pause button
def handle_pause_button():
    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        if pause_button.collidepoint(mouse_pos):
            game_active = not game_active

# Create a function to handle the game loop
def game_loop():
    global player_run_frame_time
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_active:
            handle_input()
            check_collisions()
            player_run_frame_time += 1
        else:
            handle_pause_button()

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        draw_coins()
        draw_player()
        draw_timer_and_coin_count()
        screen.blit(pause_button, PAUSE_BUTTON_POS)
        pygame.display.flip()
        clock.tick(60)

# Create a function to add coins to the list
def add_coins():
    for i in range(COIN_COUNT):
        add_coin(random.randint(0, WIDTH - coin.get_width()), random.randint(0, HEIGHT - coin.get_height()))

# Initialize the game
add_coins()
font = pygame.font.Font(TIMER_FONT, 36)
game_loop()