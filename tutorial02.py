#import and run pygame
import pygame
pygame.init()

#window size for the game
win = pygame.display.set_mode((500, 500))

#the name of the window
pygame.display.set_caption("First Gamew")

#attributes, variable initializations for rectangle

#can use variable instead to make dynamic:
#screenWidth = 500

x = 50  
y = 425
width = 40
height = 60
vel = 5 #speed

#//jump variables
isJump = False
jumpCount =10

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

        #//to keep object within window box and not out of bounds 
        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
        if keys[pygame.K_RIGHT] and x < 500 - width - vel:
            x += vel
        #//encapsulates jumping
        if not(isJump):
                
            if keys[pygame.K_UP] and y > vel:
                y -= vel
            if keys[pygame.K_DOWN] and y > 500 - height - vel:
                y += vel

            #//jump code (if we can figure it out)
            if keys[pygame.K_SPACE]:
                isJump = True
        else:
            #//so jump can go down
            if jumpCount >= -10:
                if jumpCount < 0:
                    neg = 1
                    if jumpCount < 0:
                        neg = -1
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1

            #//resets jump so can jump again
            else:
                isJump = False
                jumpCount = 10

    #fills in screen over with black so the old rectangle gets covered
    win.fill((0, 0, 0))
    
    #rectangle thing(object location, (color: rbg), (attributes)
    #attribute: x position, y pos, width, height
    pygame.draw.rect(win, (255, 0, 0), (x,y, width, height))
    pygame.display.update()

#make sure to have or it will live forever!!! :)
pygame.quit()
    
