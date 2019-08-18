import pygame
import time
import random

pygame.init()

WIDTH, HEIGHT = 1200, 700

white = (255,255,255)
black = (0,0,0)
speed_of_obstacle = 10

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Dinosaur")

# loading images
jiren = pygame.image.load('jiren.jpg')
goku = pygame.image.load('goku.png')
fire = pygame.image.load('fire.png')
clock = pygame.time.Clock()
screen.fill(white)

def hit(goku_x,goku_y,fire_x,fire_y):
    num = random.randint(1,2)
    if num == 2:
        while(fire_x > 0):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print("PRessed")
                        goku_y = 200

            screen.blit(fire, (fire_x,fire_y))
            screen.blit(goku, (goku_x,goku_y))
            pygame.display.update()
            fire_x -= 50
            time.sleep(0.1)
            goku_y = 399
            lose(goku_y,fire_x,fire_y)

def lose(goku_y, fire_x, fire_y):
    if fire_x >= 62 and fire_x <= 157 and goku_y <= 469:
        print("FUCK I AM LOSING TO JIREN")

def jump():

def game_loop():
    goku_x, goku_y = 10, 399
    fire_x, fire_y = 850, 469
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_UP:
            #         print("PRessed")
            #         goku_y = 200


        screen.fill(white)
        pygame.draw.line(screen, black, (0,600), (1000,600), 3)
        screen.blit(jiren, (1000,340))
        screen.blit(goku, (goku_x, goku_y))
        hit(goku_x,goku_y,fire_x,fire_y)
        #lose(goku_y,fire_x,fire_y)
        # num = hit()
        # if num == 2:
        #     screen.blit(fire, (fire_x, fire_y))
        #     fire_x -= 150
        #     lose(goku_y, fire_x, fire_y)
        #pygame.display.update()
        #time.sleep(0.3)
        #goku_y = 399
        clock.tick(30)



game_loop()
