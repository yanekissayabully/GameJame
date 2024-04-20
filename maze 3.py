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
background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))

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
  
    # Update camera position based on player pos
    camera_offset_x = player.rect.x - screen.get_width() / 2 + player.rect.width / 2
    camera_offset_y = player.rect.y - screen.get_height() / 2 + player.rect.height / 2

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
