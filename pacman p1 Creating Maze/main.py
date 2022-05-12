from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

# This will be our window size for this tut
Window.size = (1200,400)

class GamePlay(Screen):
    # ps stands for player size
    ps = NumericProperty(77)

    # ww stands for Window width
    ww = NumericProperty(1200)

    #wh stands for window height
    wh = NumericProperty(400)

class Wall(Widget):
    pass

class PacmanApp(App):
    def build(self):
        return GamePlay()

PacmanApp().run()
