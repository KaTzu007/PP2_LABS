import pygame
import time

#Поставьте норм балл пожалуйста! Я делал это долго 🥲...
pygame.init() #Инициализация
screen = pygame.display.set_mode((500, 500)) #Размер экрана
clock = pygame.time.Clock() #Для фпс

#Импорт
body = pygame.image.load("img/body.jpg")
rightHand = pygame.image.load("img/rightHandCopy.png")
leftHand = pygame.image.load("img/leftHandCopy.png")

#Размер изображений
body = pygame.transform.scale(body, (380, 380))
rightHand = pygame.transform.scale(rightHand, (220, 220))
leftHand = pygame.transform.scale(leftHand, (200, 200))

#Рамка для фоток(условно)
rectr = rightHand.get_rect(center =  (250, 250))
rectl = leftHand.get_rect(center =  (250, 250))

done = False

while not done:
    screen.fill((255, 255, 255)) #Заполняем экран

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    now = time.localtime()
    seconds = now.tm_sec #Получаем секунды
    minutes = now.tm_min #Получаем минуты

    secAngle = -seconds * 6
    minAngle = -minutes * 6

    #Поворачиваем изображения
    rotRight = pygame.transform.rotate(rightHand, secAngle)
    rotLeft = pygame.transform.rotate(leftHand, minAngle)

    #Получаем новые рамки(уже для новых фоток)
    newRectR = rotRight.get_rect(center = (250, 250))
    newRectL = rotLeft.get_rect(center = (250, 250))

    #Рисует поверх фоток
    screen.blit(body, (60, 60))
    screen.blit(rotRight, newRectR.topleft) #Топлефт автоматом расчитывает координаты для рамок
    screen.blit(rotLeft, newRectL.topleft)

    pygame.display.flip() #Для того чтобы было видно все изменения
    clock.tick(60) #60 фпс

pygame.quit()