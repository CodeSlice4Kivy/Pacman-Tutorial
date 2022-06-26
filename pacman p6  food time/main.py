from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.core.window import Window
from player import *
from ghost import *
from food import *
from kivy.clock import Clock

Window.size = (1200,400)

class GamePlay(Screen):
    ps = NumericProperty(77)
    ww = NumericProperty(1200)
    wh = NumericProperty(400)

    pacman = Player()
    ghost1 = Ghost()

    food_point = ['point{0}'.format(i) for i in range(0, len(food))]

    def __init__(self, **kwargs):
        super(GamePlay,self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'up':
            self.pacman.velocity=(0,1)
        elif keycode[1] == 'down':
            self.pacman.velocity=(0,-1)
        elif keycode[1] == 'left':
            self.pacman.velocity=(-1,0)
        elif keycode[1] == 'right':
            self.pacman.velocity=(1,0)
            print('hello')
            
        return True

    def show_food(self):
        for i in range(0, len(food)):
            if i != 179 and 1 != 170:
                globals()[self.food_point[i]] = Points(pos=food[i], size = (5,5))
                #now lets add our widgets
                self.add_widget(globals()[self.food_point[i]])

    def update(self, dt):
        self.pacman.move()

# We will use walls to create the maze  
class Wall(Widget):
    pass


class PacmanApp(App):
    def build(self):
        game = GamePlay()
        game.show_food()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

PacmanApp().run()
