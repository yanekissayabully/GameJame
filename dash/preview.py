import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Превью меню")

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Загрузка изображения превью меню
preview_menu_image = pygame.image.load('preview_menu_image.png')

def main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            # Обработка нажатий клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Здесь можно добавить код для перехода к основной части игры
                    print("Игра началась!")
        
        # Отрисовка превью меню
        screen.fill(WHITE)
        screen.blit(preview_menu_image, (0, 0))

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
