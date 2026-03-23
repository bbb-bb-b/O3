from pygame import *

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





font.init()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((207,134,109))
    racket_l.update_l()
    racket_l.reset()
    racket_r.update_r()
    racket_r.reset()
    display.update()
    clock.tick(60)