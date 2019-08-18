import pygame
import time

pygame.init()

# Loading the images
goku = pygame.image.load('goku.png')
jiren = pygame.image.load('jiren.png')
fireball = pygame.image.load('fire.png')
bg = pygame.image.load('main.jpg')



pygame.display.set_caption("Dragon Ball")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

class Game:
    WIDTH, HEIGHT = 1200, 720
    def __init__(self):
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.goku_x = 1
        self.goku_y = 400
        self.fireball_x = 900
        self.fireball_y = 480
        self.jiren_x = 1000
        self.jiren_y = 350
        self.vy = 0
        self.gravity = 5

    def text_objects(self, text, font):
        textSurface = font.render(text, True, RED)
        return textSurface, textSurface.get_rect()

    def jump(self):
        self.vy = 250
        self.goku_y -= self.vy

    def move(self):
        self.goku_y += self.gravity

    def move_fireball(self):
        self.fireball_x -= 5

    def is_hit(self):

        if self.fireball_x > 49 and self.fireball_x < 145:
            if self.goku_y > 300 and self.goku_y < 598:
                largeText = pygame.font.SysFont("comicsansms",115)
                TextSurf, TextRect = self.text_objects("Goku Lost!", largeText)
                TextRect.center = (self.WIDTH/2, self.HEIGHT/2)
                self.screen.blit(TextSurf, TextRect)
                pygame.display.update()
                time.sleep(5)
                pygame.quit()

    def game_loop(self):
        pygame.mixer.music.load('music.mp3')
        pygame.mixer.music.play(-1)
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.goku_y == 400:
                        self.jump()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())

            self.screen.blit(pygame.transform.scale(bg, (1200, 720)), (0, 0))
            self.screen.blit(jiren, (self.jiren_x,self.jiren_y))
            self.screen.blit(goku, (self.goku_x,self.goku_y))
            self.screen.blit(fireball, (self.fireball_x,self.fireball_y))
        #    pygame.draw.line(self.screen, BLACK, (0,600),(1200,600),3)

            if self.fireball_x >= -100:
                self.move_fireball()
            else:
                self.fireball_x = 900
                self.fireball_y = 480
                self.screen.blit(fireball, (self.fireball_x,self.fireball_y))

            if self.goku_y < 400:
                self.move()
            self.is_hit()
            pygame.display.update()


game = Game()
game.game_loop()
