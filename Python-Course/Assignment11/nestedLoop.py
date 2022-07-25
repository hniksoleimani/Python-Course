import random
import arcade
import PIL.ImageOps
import PIL.ImageDraw
from time import sleep
from math import modf

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 150
BOTTOM_MARGIN = 150

class Exercise1(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.color1 = arcade.color.BLUE
        self.color2 = arcade.color.RED
        self.r = 8
        self.loopx = []
        self.loopy = []
        print(len(self.loopx))
                
    def nest(self):
        for column in range(10):
            self.x = column * COLUMN_SPACING + LEFT_MARGIN
            self.loopx.append(self.x)
            self.y = column * ROW_SPACING + BOTTOM_MARGIN
            self.loopy.append(self.y)
    def draw(self):
        for i in range(len(self.loopx)):
            for j in range(len(self.loopy)):
                if (i+j) %2 == 0:
                    arcade.draw_circle_filled(self.loopx[i], self.loopy[j], self.r, self.color1)
                else:
                    arcade.draw_circle_filled(self.loopx[i], self.loopy[j], self.r, self.color2)
                       

class Screen(arcade.Window):
    def __init__(self):
        super().__init__(width =500, height = 500, title='Complex loop', antialiasing = False)
        arcade.set_background_color(arcade.color.SAND)
        self.exer = Exercise1()
        self.exer.nest()
    def on_draw(self):
        arcade.start_render()
        self.exer.draw()
        arcade.finish_render()


my_game = Screen()
arcade.run()

#pyinstaller 1.py --onefile
#arcade pyinstaller