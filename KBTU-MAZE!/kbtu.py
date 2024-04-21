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
PAUSE_BUTTON_POS = (10, 10)
TIMER_POS = (WIDTH - 100, 10)
COIN_COUNT_POS = (WIDTH - 200, 10)
PLAYER_POS = (0, 0)
PLAYER_VELOCITY = 5
PLAYER_RUN_VELOCITY = 10
PLAYER_RUN_FRAME_DELAY = 5

# Initialize the game display mode
game_display = pygame.display.set_mode((WIDTH, HEIGHT))

# Load images after setting display mode
background = pygame.image.load('kbtu_map.png').convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
player_stationary = pygame.image.load('character_standing.jpg').convert()
player_stationary = pygame.transform.scale(player_stationary, (30, 30))
player_run_sheet = pygame.image.load('character_running.jpg').convert()
player_run_sheet = pygame.transform.scale(player_run_sheet, (30, 30))
coin = pygame.image.load('coin.png').convert()
coin = pygame.transform.scale(coin, (30, 30))
pause_button = pygame.image.load('pause_button.jpeg').convert()
pause_button = pygame.transform.scale(pause_button, (30, 30))  

# Initialize variables
player_run_frame = 0
player_run_frame_time = 0
coin_objects = []
coin_count = 0
clock = pygame.time.Clock()
game_active = False  # Initially, the game is not active
player_rect = player_stationary.get_rect()

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
def draw_player(screen):
    global player_run_frame  # Declare as global
    if player_run_frame_time % PLAYER_RUN_FRAME_DELAY == 0:
        player_run_frame = (player_run_frame + 1) % PLAYER_RUN_FRAMES
    player_image = player_run_sheet.subsurface(pygame.Rect(player_run_frame * player_run_sheet.get_width() / PLAYER_RUN_FRAMES, 0, player_run_sheet.get_width() / PLAYER_RUN_FRAMES, player_run_sheet.get_height()))
    screen.blit(player_image, player_rect)

# Create a function to handle the pause button
def handle_pause_button():
    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        if pause_button.get_rect(topleft=PAUSE_BUTTON_POS).collidepoint(mouse_pos):
            return True
    return False

# Create a function to handle the game loop
def game_loop(screen):
    global player_run_frame_time, game_active
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_menu(screen)

        if game_active:
            handle_input()
            check_collisions()
            player_run_frame_time += 1

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        draw_coins(screen)
        draw_player(screen)
        draw_timer_and_coin_count(screen)
        screen.blit(pause_button, PAUSE_BUTTON_POS)

        if handle_pause_button():
            game_active = not game_active

        pygame.display.flip()
        clock.tick(60)

# Create a function to add coins to the list
def add_coins():
    for _ in range(COIN_COUNT):
        add_coin(random.randint(0, WIDTH - coin.get_width()), random.randint(0, HEIGHT - coin.get_height()))

# Create a function to display game menu
def game_menu(screen):
    menu_font = pygame.font.Font(None, 36)
    menu_options = ["Continue", "Off Sound", "Quit"]
    selected_option = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        return  # continue
                    elif selected_option == 1:
                        pygame.mixer.music.set_volume(0) if pygame.mixer.music.get_volume() > 0 else pygame.mixer.music.set_volume(1)  # Включение/выключение звука
                    elif selected_option == 2:
                        pygame.quit()
                        sys.exit()  # exit

        screen.fill((0, 0, 0))
        for i, option in enumerate(menu_options):
            text_color = (255, 255, 255) if i == selected_option else (128, 128, 128)
            text = menu_font.render(option, True, text_color)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 40))
            screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

# Initialize the game display
add_coins()
font = pygame.font.Font(None, 36)

# Display intro image
intro_image = pygame.image.load('image.png').convert()
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
