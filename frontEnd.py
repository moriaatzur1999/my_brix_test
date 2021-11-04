#Author: Moria Mashiah

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout
import kivy
from kivy.app import App
import requests
import random

pic_src = "data:image/jpeg;base64,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"
users_data = requests.get("https://randomuser.me/api/?results=3").json()['results']


class MyApp(App):

    def build(self):
        self.window = RelativeLayout(size =(300, 300))
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}
        self.window.add_widget(Image(source=pic_src,
                                     size_hint_x= 0.2,
                                     pos =(0, 230),
                                     allow_stretch =True,
                                     width= 50))
        self.greeting = Label(text = 'Hi, please click on the requested information',color = '#00FFCE', bold = True, pos =(20, 200))
        self.window.add_widget(self.greeting)

        self.button1 = Button(text="full names",
                             #size=(0.3, 0.4),
                             size_hint=(0.25, 0.25),
                              pos=(-25, 250),
                             bold=True,
                             background_color='#00FFCE')
        self.button1.bind(on_press=self.callback1)
        self.window.add_widget(self.button1)

        self.button2 = Button(text="email",
                            size_hint=(0.25, 0.25),
                            pos=(175, 250),
                             bold=True,
                             background_color='#00FFCE')
        self.button2.bind(on_press=self.callback2)
        self.window.add_widget(self.button2)

        self.button3 = Button(text="address",
                              size_hint=(0.25, 0.25),
                              pos=(375, 250),
                             bold=True,
                             background_color='#00FFCE')
        self.button3.bind(on_press=self.callback3)
        self.window.add_widget(self.button3)
        return self.window


    def callback1(self, user):
        x = 0
        for user in users_data:
            self.greeting1 = Label(text=user['name']['first'] + " " + user['name']['last'],
                                   bold = True,
                                  font_size = 15,
                                  color = '#00FFCE',
                                  pos=(-210, 0+x))
            x-=50
            self.window.add_widget(self.greeting1)


    def callback2(self, user):
        x = 0
        for user in users_data:
            self.greeting2 = Label(text=user['email'] ,
                                   bold = True,
                                  font_size = 15,
                                  color = '#00FFCE',
                                   pos=(0, 0+x))
            x-=50
            self.window.add_widget(self.greeting2)


    def callback3(self, user):
        x =0
        for user in users_data:
            self.greeting = Label(text=user['location']['street']['name'] + " " + str(user['location']['street']['number']),
                                  bold = True,
                                  font_size = 15,
                                  color = '#00FFCE',
                                  pos=(210, 0+x))
            x -= 50
            self.window.add_widget(self.greeting)


if __name__ == '__main__':
    MyApp().run()




