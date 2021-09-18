#создай игру "Лабиринт"!
from pygame import *
'''Необходимые классы'''

#класс-родитель для спрайтов 
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (55, 55))
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#класс-наследник для спрайта-врага (перемещается сам)
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 450:
            self.side = "right"
        if self.rect.x >= win_width - 90:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

#класс для спрайтов-препятствий
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
 
        # картинка стены - прямоугольник нужных размеров и цвета
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
 
        # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
 
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))

#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

#Персонажи игры:
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 400, 0)

w1 = Wall(14, 86, 64, 60, 40, 15, 350)
w2 = Wall(14, 86, 64, 60, 470, 600, 15)
w3 = Wall(14, 86, 64, 60, 40, 600, 15)
w4 = Wall(14, 86, 64, 165, 130, 15, 350)
w5 = Wall(14, 86, 64, 250, 50, 15, 350)
w6 = Wall(14, 86, 64, 350, 130, 15, 350)
w7 = Wall(14, 86, 64, 450, 50, 15, 350)
w8 = Wall(14, 86, 64, 650, 40, 15, 445)

walls = [w1, w2, w3, w4, w5, w6, w7, w8]

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

#музыка


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        monster.update()
        
        player.reset()
        monster.reset()
        final.reset() 

    
        for wall in walls:
            wall.draw_wall() 

        for wall in walls:
            if sprite.collide_rect(player, wall):
                player.rect.x = 5
                player.rect.y = win_height - 80

        if sprite.collide_rect(player, monster):
            finish = True
            window.blit(lose, (200,200))

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
        


    display.update()
    clock.tick(FPS)