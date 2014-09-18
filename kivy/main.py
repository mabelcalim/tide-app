from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_string('''
#:import random random.random
#:import SlideTransition kivy.uix.screenmanager.SlideTransition
#:import SwapTransition kivy.uix.screenmanager.SwapTransition
#:import WipeTransition kivy.uix.screenmanager.WipeTransition
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import RiseInTransition kivy.uix.screenmanager.RiseInTransition
#:import FallOutTransition kivy.uix.screenmanager.FallOutTransition
#:import NoTransition kivy.uix.screenmanager.NoTransition

<CustomScreen>:
    hue: random()
    canvas:
        Rectangle:
            size: self.size
            source: 'android_view.jpg'
    Button:
        text: 'tide data'
        size_hint: None, None
        pos_hint: {'right': 1}
        size: 150, 50
        on_release: root.manager.current = root.manager.next()


<Screen1>:
    tab_pos: 'top'
    size_hint: (1, 1)
    pos_hint: {'right':1}
    FloatLayout:
        RstDocument:
            id: default_content
            source:('mydata.rst')
   
    Button:
        text: 'refresh '
        size_hint: None, None
        pos_hint: {'top': 1, 'right':1}
        size: 150, 50
        on_press: app.start()
 
    Button:
        text: 'menu'
        size_hint: None, None
        size: 150, 50
        on_release: root.manager.current = root.manager.previous()
''')


class CustomScreen(Screen):
    hue = NumericProperty(0)

class Screen1(Screen):
    pass

class ScreenManagerApp(App):
    Clock.max_iteration = 70
    def start(self):
	 Clock.schedule_interval(lambda dt:self.database(),0.5)

    def database(self):
        import database2
        return

    def build(self):
        root = ScreenManager()
        for x in range(1):
            root.add_widget(CustomScreen(name='%s'%x))
        if x ==0:
            #video= VideoPlayer(source='softboy.avi', state='play') 
            root.add_widget(Screen1())
        return root

if __name__ == '__main__':
    ScreenManagerApp().run()

