from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
import subprocess

class MyLayout(Widget):
    pass

class MyApp(App):
    def build(self):
        return Button(on_press = self.btn_press, background_normal = 'images/off-button.png', background_down = 'images/on-button.png', font_size = 1)


    def btn_press(self, instance):
        subprocess.Popen('C:/Users/nikit/AppData/Local/Yandex/YandexBrowser/Application/browser')


if __name__ == '__main__':
    MyApp().run()