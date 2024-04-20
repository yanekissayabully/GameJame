import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Меню игры")

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Определение шрифтов
font = pygame.font.SysFont(None, 50)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def main_menu():
    running = True
    while running:
        screen.fill(WHITE)
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            # Обработка нажатий клавиш мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 100 <= mouse_pos[0] <= 300 and 200 <= mouse_pos[1] <= 250:
                    print("Продолжить игру")
                elif 100 <= mouse_pos[0] <= 250 and 300 <= mouse_pos[1] <= 350:
                    print("Пауза")
                elif 100 <= mouse_pos[0] <= 310 and 400 <= mouse_pos[1] <= 450:
                    print("Настройка музыки")

        # Отрисовка кнопок меню
        pygame.draw.rect(screen, GRAY, (100, 200, 200, 50))
        pygame.draw.rect(screen, GRAY, (100, 300, 150, 50))
        pygame.draw.rect(screen, GRAY, (100, 400, 210, 50))

        # Отрисовка текста на кнопках
        draw_text("Продолжить игру", font, BLACK, screen, 200, 225)
        draw_text("Пауза", font, BLACK, screen, 175, 325)
        draw_text("Настройка музыки", font, BLACK, screen, 205, 425)

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
