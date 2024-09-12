import pygame
import random

pygame.init()

# Параметры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

# Иконка игры
icon = pygame.image.load('image/IMG_3862.JPG')
pygame.display.set_icon(icon)

# Изображение мишени
target_image = pygame.image.load("image/target .png")
target_width = 150
target_height = 195

# Изображение выстрела
shot_image = pygame.image.load("image/shot.png")
shot_width, shot_height = shot_image.get_size()

# Позиция мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Счет игры
score = 0
font = pygame.font.SysFont(None, 55)

# Список для хранения относительных координат выстрелов на мишени
shots = []


# Функция для отображения текста
def show_text(text, x, y):
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))


# Функция меню игры
def game_menu():
    menu = True
    while menu:
        screen.fill((0, 0, 0))
        show_text("Добро пожаловать в игру Тир!", 100, 200)
        show_text("Нажмите ENTER, чтобы начать игру", 100, 300)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu = False


# Вызов меню перед началом игры
game_menu()

# Основной цикл игры
running = True

while running:
    screen.fill(color)

    # Отрисовка мишени
    screen.blit(target_image, (target_x, target_y))

    # Отрисовка всех выстрелов на мишени
    for shot in shots:
        shot_x = target_x + shot[0]  # Абсолютная координата X выстрела
        shot_y = target_y + shot[1]  # Абсолютная координата Y выстрела
        screen.blit(shot_image, (shot_x - shot_width // 2, shot_y - shot_height // 2))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Проверка попадания по мишени
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Рассчитываем относительные координаты выстрела
                relative_shot_x = mouse_x - target_x
                relative_shot_y = mouse_y - target_y

                # Добавляем относительные координаты выстрела в список
                shots.append((relative_shot_x, relative_shot_y))

                # Перемещаем мишень на новое случайное место
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

                # Увеличиваем счет на 10
                score += 10

                # Проверка условия победы
                if score >= 100:
                    show_text("Вы победили!", 250, 250)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    running = False

    # Отображение счета
    show_text(f"Счет: {score}", 10, 10)

    pygame.display.update()

pygame.quit()

