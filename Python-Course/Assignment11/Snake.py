import random
# from tkinter.messagebox import NO
import arcade
import PIL.Image
import PIL.ImageOps
import PIL.ImageDraw
from time import sleep
from math import modf

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        
        self.width = 16
        self.height = 18
        self.color1 = arcade.color.GREEN
        self.color2 = arcade.color.DARK_GREEN
        self.change_x = 0
        self.change_y = 0
        self.score = 0
        self.center_x = SCREEN_WIDTH // 2
        self.center_y =  SCREEN_HEIGHT // 2
        self.speed = 4
        self.body = []

    def move(self):
        #add old head position to body
        self.body.append([self.center_x, self.center_y])

        if len(self.body) > self.score:
            self.body.pop(0)
        #update head position
        if self.change_x > 0:
            self.center_x += self.speed
        elif self.change_x < 0:
            self.center_x -= self.speed
        if self.change_y > 0:
            self.center_y += self.speed
        elif self.change_y < 0:
            self.center_y -= self.speed
    def eat(self):
        self.score += 1
    def yum(self):
        self.score +=2
    def ugh(self):
        self.score -=1
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color1)
        for i in range(len(self.body)):
            if i %2 == 0 :    
                arcade.draw_rectangle_filled(self.body[i][0], self.body[i][1], self.width, self.height, self.color1 )
            else:
                arcade.draw_rectangle_filled(self.body[i][0], self.body[i][1], self.width, self.height, self.color2 )
          
class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.color = arcade.color.RED
        self.r = 8
        self.center_x = random.randint(0, SCREEN_WIDTH)
        self.center_y = random.randint(0, SCREEN_HEIGHT)
    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)
        

 

class Bonus(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.color = arcade.color.BLUE
        self.r = 8
        self.center_x = random.randint(0, SCREEN_WIDTH)
        self.center_y = random.randint(0, SCREEN_HEIGHT)
    def draw(self):
        
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)




class Poo(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.color = arcade.color.BROWN
        self.r = 8
        self.center_x = random.randint(0, SCREEN_WIDTH)
        self.center_y = random.randint(0, SCREEN_HEIGHT)
    def draw(self):
        
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)
   
# class Text(arcade.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.text = f'Score:{modf(self.snake.score)[1]}'
#         self.textOver = 'GAME OVER'
#         self.x = 50
#         self.y = 50
#         self.x2 = SCREEN_WIDTH // 3
#         self.y2 = SCREEN_HEIGHT // 3
#         self.color = arcade.color.BLACK
#         self.size = 12
#         self.size2 = 34
#     def draw(self):
#         arcade.draw_text(self.text, self.x, self.y, self.color, self.size)


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width =500, height = 500, title='Snake Game', antialiasing = False)
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake()
        self.apple = Apple()
        self.bonus = Bonus()
        self.poo1 = Poo()
        self.poo2 = Poo()
        self.poo3 = Poo()
        self.poo4 = Poo()
        self.text = f'Score:{self.snake.score}'
        self.textOver = 'GAME OVER'
        self.x = 50
        self.y = 50
        self.x2 = SCREEN_WIDTH // 3
        self.y2 = SCREEN_HEIGHT // 3
        self.color = arcade.color.BLACK
        self.size = 12
        self.size2 = 34

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        self.bonus.draw()
        self.poo1.draw()
        self.poo2.draw()
        self.poo3.draw()
        self.poo4.draw()
        arcade.draw_text(f'Score:{modf(self.snake.score)[1]}', self.x, self.y, self.color, self.size)
        if self.snake.score <= -1 or self.snake.center_x >= SCREEN_WIDTH or self.snake.center_x <= 0 or self.snake.center_y >= SCREEN_HEIGHT or self.snake.center_y <= 0:
            arcade.draw_text(self.textOver, self.x2, self.y2, self.color, self.size2)
            sleep(1)

    def on_update(self, delta_time: float):
        self.snake.move() 
        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat()
            self.apple = Apple()
        if arcade.check_for_collision(self.snake, self.bonus):
            self.snake.yum()
            self.bonus = Bonus()
        if arcade.check_for_collision(self.snake,self.poo4):
            self.snake.ugh()
            self.poo4 = Poo()
            print(self.snake.score)
        if arcade.check_for_collision(self.snake,self.poo1):
            self.snake.ugh()
            self.poo1 = Poo()

        if arcade.check_for_collision(self.snake,self.poo2):
            self.snake.ugh()
            self.poo2 = Poo()
                
        if arcade.check_for_collision(self.snake,self.poo3):
            self.snake.ugh()
            self.poo3 = Poo()


    def on_key_release(self,key: int, modifier: int):
        if key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        if key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0

        if key == arcade.key.UP:
            self.snake.change_y = 1
            self.snake.change_x = 0

        if key == arcade.key.DOWN:
            self.snake.change_y = -1
            self.snake.change_x = 0



my_game = Game()
arcade.run()

#pyinstaller 1.py --onefile
#arcade pyinstaller