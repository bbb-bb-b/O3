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
    def update(self):
        pressed = key.get_pressed()
        if pressed[K_LEFT] and self.rect.x >= 5:
            self.rect.x -= self.speed
        if pressed[K_RIGHT] and self.rect.x <= 1295:
            self.rect.x += self.speed

font.init()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(60)