import pygame

pygame.init() #Инициализация
screen = pygame.display.set_mode((500, 400)) #Размер экрана
clock = pygame.time.Clock() #Для фпс

x, y = 250, 200 #Координаты для шара

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed() #Какая кнопка была нажата

    #Границы
    if pressed[pygame.K_UP] and y > 30: 
        y -= 20
    if pressed[pygame.K_DOWN] and y < 370: 
        y += 20
    if pressed[pygame.K_LEFT] and x > 30: 
        x -= 20
    if pressed[pygame.K_RIGHT] and x < 470: 
        x += 20

    screen.fill((255, 255, 255)) #Заполняем экран
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25) #рисуем шар

    pygame.display.flip() #Для того чтобы было видно все изменения
    clock.tick(60) #60 фпс

pygame.quit()