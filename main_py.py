import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

kivy.require('1.0.7')


class MainPage(GridLayout):
    def __ini__(self, **kwargs):
        super().__init__(**kwargs)
        self.t = TextInput(text="Hello World")
        self.add_widget(self.t)

class EpicApp(App):
    def build(self):
        self.main_page = MainPage()
        return self.main_page


if __name__ == '__main__':
    EpicApp().run()