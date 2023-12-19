from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window


# ao fazer apps dedicados e necessario remover isso.
Window.size = (300,500)

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        screen = Builder.load_file('style.kv')
        return screen
    
    
    def navigation_draw(self):
        print('Navigation')


DemoApp().run()