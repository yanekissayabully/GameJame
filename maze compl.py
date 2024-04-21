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

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def game_menu():
    font = pygame.font.SysFont(None, 50)  # Define font here
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()  # Get mouse position
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False  # Exit the menu without continuing the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 250 <= mouse_pos[0] <= 550 and 200 <= mouse_pos[1] <= 250:
                    return True  # Continue the game
                elif 250 <= mouse_pos[0] <= 550 and 300 <= mouse_pos[1] <= 350:
                    pygame.mixer.music.stop()  # Stop music
                elif 250 <= mouse_pos[0] <= 550 and 400 <= mouse_pos[1] <= 450:
                    pygame.quit()
                    sys.exit()  # Exit game
        screen.fill((0, 0, 0))  # Fill the screen with black
        draw_text("Game Menu", font, (255, 255, 255), screen, WIDTH // 2, 100)
        # Draw menu options
        draw_text("Continue", font, (255, 255, 255), screen, WIDTH // 2, 225)
        draw_text("Off music", font, (255, 255, 255), screen, WIDTH // 2, 325)
        draw_text("Exit", font, (255, 255, 255), screen, WIDTH // 2, 425)
        pygame.display.flip()
        clock.tick(60)
    return False  # Return False if the menu loop ends without a choice

os.environ["SDL_VIDEO_CENTERED"] = "1" 
pygame.init() 
pygame.display.set_caption("KBTU MAZE!") 
WIDTH, HEIGHT = 1000, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 

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
    "W   W     W W W  W                      ", 
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
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

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

# Load and play background music
pygame.mixer.music.load("backsound.mp3")
pygame.mixer.music.play(-1)  # Play music in a loop

while running: 
    clock.tick(60) 
     
    for e in pygame.event.get(): 
        if e.type == pygame.QUIT: 
            running = False 
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: 
            if game_menu():  # Open game menu, and continue only if True is returned
                pygame.mixer.music.play(-1)  # Play music in a loop

    key = pygame.key.get_pressed() 
    if key[pygame.K_LEFT]: 
        player.move(-2, 0) 
    if key[pygame.K_RIGHT]: 
        player.move(2, 0) 
    if key[pygame.K_UP]: 
        player.move(0, -2) 
    if key[pygame.K_DOWN]: 
        player.move(0, 2) 
  
    # Update camera position based on player pos
    camera_offset_x = player.rect.x - WIDTH / 2 + player.rect.width / 2
    camera_offset_y = player.rect.y - HEIGHT / 2 + player.rect.height / 2

    if player.rect.colliderect(coin_rect): 
        pygame.quit() 
        sys.exit() 
  
    # Draw background with camera offset
    screen.blit(background_image, (-camera_offset_x, -camera_offset_y))

    # Draw walls with camera offset
    for wall in walls: 
        screen.blit(wall.image, (wall.rect.x - camera_offset_x, wall.rect.y - camera_offset_y))

    # Draw player and coin with camera offset
    pygame.draw.rect(screen, (255, 215, 0), (coin_rect.x - camera_offset_x, coin_rect.y - camera_offset_y, coin_rect.width, coin_rect.height)) 
    pygame.draw.rect(screen, (245, 69, 0), (player.rect.x - camera_offset_x, player.rect.y - camera_offset_y, player.rect.width, player.rect.height)) 

    pygame.display.flip() 

pygame.quit()
'''


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

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def game_menu():
    font = pygame.font.SysFont(None, 50)  # Define font here
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()  # Get mouse position
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False  # Exit the menu without continuing the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 250 <= mouse_pos[0] <= 550 and 200 <= mouse_pos[1] <= 250:
                    return True  # Continue the game
                elif 250 <= mouse_pos[0] <= 550 and 300 <= mouse_pos[1] <= 350:
                    pygame.mixer.music.stop()  # Stop music
                elif 250 <= mouse_pos[0] <= 550 and 400 <= mouse_pos[1] <= 450:
                    pygame.quit()
                    sys.exit()  # Exit game
        screen.fill((0, 0, 0))  # Fill the screen with black
        draw_text("Game Menu", font, (255, 255, 255), screen, WIDTH // 2, 100)
        # Draw menu options
        draw_text("Continue", font, (255, 255, 255), screen, WIDTH // 2, 225)
        draw_text("Off music", font, (255, 255, 255), screen, WIDTH // 2, 325)
        draw_text("Exit", font, (255, 255, 255), screen, WIDTH // 2, 425)
        pygame.display.flip()
        clock.tick(60)
    return False  # Return False if the menu loop ends without a choice

os.environ["SDL_VIDEO_CENTERED"] = "1" 
pygame.init() 
pygame.display.set_caption("KBTU MAZE!") 
WIDTH, HEIGHT = 1000, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 

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
    "W   W     W W W  W                      ", 
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
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

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
game_started = False  # To check if the game has started

# Load and play background music
pygame.mixer.music.load("backsound.mp3")
pygame.mixer.music.play(-1)  # Play music in a loop

# Display startup screen
startup_font = pygame.font.SysFont(None, 50)
startup_text = startup_font.render("Press Space to Start", True, (255, 255, 255))
startup_rect = startup_text.get_rect(center=(WIDTH // 2, HEIGHT - 50))

while running: 
    clock.tick(60) 
     
    for e in pygame.event.get(): 
        if e.type == pygame.QUIT: 
            running = False 
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: 
            if game_menu():  # Open game menu, and continue only if True is returned
                pygame.mixer.music.play(-1)  # Play music in a loop
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            game_started = True  # Start the game if Space is pressed

    if game_started:  # Start drawing and updating only if the game has started
        key = pygame.key.get_pressed() 
        if key[pygame.K_LEFT]: 
            player.move(-2, 0) 
        if key[pygame.K_RIGHT]: 
            player.move(2, 0) 
        if key[pygame.K_UP]: 
            player.move(0, -2) 
        if key[pygame.K_DOWN]: 
            player.move(0, 2) 

        # Update camera position based on player pos
        camera_offset_x = player.rect.x - WIDTH / 2 + player.rect.width / 2
        camera_offset_y = player.rect.y - HEIGHT / 2 + player.rect.height / 2

        if player.rect.colliderect(coin_rect): 
            pygame.quit() 
            sys.exit() 

        # Draw background with camera offset
        screen.blit(background_image, (-camera_offset_x, -camera_offset_y))

        # Draw walls with camera offset
        for wall in walls: 
            screen.blit(wall.image, (wall.rect.x - camera_offset_x, wall.rect.y - camera_offset_y))

        # Draw player and coin with camera offset
        pygame.draw.rect(screen, (255, 215, 0), (coin_rect.x - camera_offset_x, coin_rect.y - camera_offset_y, coin_rect.width, coin_rect.height)) 
        pygame.draw.rect(screen, (245, 69, 0), (player.rect.x - camera_offset_x, player.rect.y - camera_offset_y, player.rect.width, player.rect.height)) 

    else:  # Draw startup screen if the game hasn't started
        screen.blit(background_image, (0, 0))  # Draw background
        screen.blit(startup_text, startup_rect)  # Draw startup text

    pygame.display.flip() 

pygame.quit()

