import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Hello")

x = 5
y = 10
width = 50
height = 50

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x,y, width, height))
    
    pygame.display.update()

pygame.quit()
