import pygame
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
background_image = pygame.image.load("background")
character_image = pygame.image.load("character")

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
sys.exit()
