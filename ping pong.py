from pygame import*
window = display.set_mode((600, 500))
clock = time.Clock()

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
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 50:
            self.rect.y += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 50:
            self.rect.y += self.speed



#Игровая сцена:
back = (200, 255, 255)#цвет фона(background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False 
clock = time.Clock()
FPS = 60

#Флаги отвечающие за состояние игры
racket1 = Player( 30, 20,'png-clipart-opengameart-org-concept-art-music-two-dimensional-space-platform-miscellaneous-texture.png', 30, 150, 10)
racket2 = Player( 520, 200,'png-clipart-opengameart-org-concept-art-music-two-dimensional-space-platform-miscellaneous-texture.png', 30, 150, 10)
ball = GameSprite( 200, 200,'tennis.png', 70, 70, 1)

#создание мяча и ракетки
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (100, 0, 0))
lose2 = font.render('PLAYER 2 LOSE', True, (100, 0, 0))

speed_x = 5
speed_y = 5

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        # if e.type == KEYDOWN:
        #     if e.key == K_UP:

    if finish != True:
        window.fill(back)
        racket1.update_1()
        racket2.update_2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1
        
        if ball.rect.y > win_height -50 or ball.rect.y < 0:
            speed_y *= -1


        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True
        

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        racket1.reset()
        racket2.reset()
        ball.reset()
        
    display.update()
    clock.tick(FPS)
        
       