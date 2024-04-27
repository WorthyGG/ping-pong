# ping-pong
from pygame import*
window = display.set_mode((700, 500))
class GameSprite(sprite.Sprite):
    def __init__(self, player_x, player_y, player_image, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y)) 

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_DOWN] and self.rect.x < 620:
            self.rect.x += self.speed
