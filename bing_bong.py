from pygame import *
from random import randint
window = display.set_mode((1200,900))
display.set_caption('Бинг-бонг')
window.fill((207,134,109))
clock = time.Clock()
game = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, imagee, speed, x, y, height, width):
        super().__init__()
        self.image = transform.scale(image.load(imagee), (height,width))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        pressed = key.get_pressed()
        if pressed[K_w] and self.rect.y >= 10:
            self.rect.y -= self.speed
        if pressed[K_s] and self.rect.y <= 640:
            self.rect.y += self.speed

    def update_r(self):
        pressed = key.get_pressed()
        if pressed[K_o] and self.rect.y >= 10:
            self.rect.y -= self.speed
        if pressed[K_k] and self.rect.y <= 640:
            self.rect.y += self.speed

racket_l = Player('racket.png', 7.52670910203014, 50, 300, 100, 250)
racket_r = Player('racket.png', 7.52670910203014, 1050, 300, 100, 250)
ball = GameSprite('volan.png', 3, randint(300,600), randint(200,700), 50, 70)
speed_x = 3
speed_y = 2


font.init()
fontt = font.Font(None, 35)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill((207,134,109))
        racket_l.update_l()
        racket_l.reset()
        racket_r.update_r()
        racket_r.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 830 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket_l, ball) or sprite.collide_rect(racket_r, ball):
            speed_x *= -1
            if randint(1,2) == 1:
                if speed_x < 0:
                    speed_x -= 1
                    if speed_y < 0:
                        speed_y -= 1
                    else:
                        speed_y += 1
                else:
                    speed_x += 1
                    if speed_y < 0:
                        speed_y -= 1
                    else:
                        speed_y += 1                    

        if ball.rect.x < 0:
            loser_l = fontt.render('LEVYY LOSER!', True, (0,0,0))
            window.blit(loser_l, (50,50))
            finish = True
        if ball.rect.x > 1150:
            loser_r = fontt.render('PRAVYY LOSER!', True, (0,0,0))
            window.blit(loser_r, (50,50))
            finish = True      
    display.update()
    clock.tick(60)