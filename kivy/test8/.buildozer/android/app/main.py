#!/bin/sh
#!/usr/bin/kivy
import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
import kivy.uix.image
from kivy.uix.image import AsyncImage,Image
#__version__ = '1.7.2'

Builder.load_string('''
<CustomScreen>:
    canvas:
        Rectangle:
            size: self.size
            source: 'android_view.jpg'
    Button:
        text: 'tide data'
        size_hint: None, None
        pos_hint: {'right': 1}
        size: 200, 100
        on_release: root.manager.current = root.manager.next()

<Screen1>:
    canvas:
        Rectangle:
            size: self.size
            source: 'rst.jpg'
    Button:
        text: 'menu'
        size_hint: None, None
        size: 150, 50
        on_release: root.manager.current = root.manager.previous()
    
    AsyncImage:
        source: 'https://raw.githubusercontent.com/mabelcalim/tide-app/master/kivy/fig_data.png'
        size: self.size
        pos_hint: {'center_x':.5, 'center_y': .3}

''')


class CustomScreen(Screen):
    hue = NumericProperty(0)

class Screen1(Screen):
    pass

class ScreenManagerApp(App):
    def build(self):
        root = ScreenManager()
        for x in range(1):
        	root.add_widget(CustomScreen(name='%s'%x))
        if x ==0:
        	root.add_widget(Screen1())
        return root

if __name__ == '__main__':
    ScreenManagerApp().run()

