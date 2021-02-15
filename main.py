from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
Window.size = (375, 620)


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)


class MainApp(MDApp):
    def build(self):
        self.screen = MainScreen(name="main_screen")
        self.sm = ScreenManager()
        self.sm.add_widget(self.screen)
        return self.sm


MainApp().run()
