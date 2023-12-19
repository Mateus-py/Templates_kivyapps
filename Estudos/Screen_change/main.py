from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager



class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class UploadScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='Profile'))
sm.add_widget(UploadScreen(name='Upload'))


class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_file('style.kv')
        return screen
    


DemoApp().run()