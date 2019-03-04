#import and run pygame
import pygame
pygame.init()

#window size for the game
win = pygame.display.set_mode((500, 500))

#the name of the window
pygame.display.set_caption("First Gamew")

#attributes, variable initializations for rectangle
x = 50  
y = 50
width = 40
height = 60
vel = 5 #speed

#main loop
run = True
while run:
    pygame.time.delay(100) #"clock" in game, fps (in milisec)

    #events:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False

    #how to continually move an object
    #origin is at top left corner, horizontal = x, vertical = y -> reverse 4th quadrant
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= vel
        if keys[pygame.K_RIGHT]:
            x += vel
        if keys[pygame.K_UP]:
            y -= vel
        if keys[pygame.K_DOWN]:
            y += vel

    #fills in screen over with black so the old rectangle gets covered
    win.fill((0, 0, 0))
    
    #rectangle thing(object location, (color: rbg), (attributes)
    #attribute: x position, y pos, width, height
    pygame.draw.rect(win, (255, 0, 0), (x,y, width, height))
    pygame.display.update()

#make sure to have or it will live forever!!! :)
pygame.quit()
    
