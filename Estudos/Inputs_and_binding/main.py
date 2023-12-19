from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager



class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='Profile'))


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_pallete  = 'Red'
        screen = Builder.load_file('style.kv')
        return screen
    


DemoApp().run()