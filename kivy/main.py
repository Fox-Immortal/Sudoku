import kivy 
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
# from socket_client
import os
import sys
kivy.require("1.10.1")



class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if os.path.isfile("pre_details.txt"):
            with open("pre_details.txt", "r") as file:
                d = file.read().split(",")
                prev_ip = d[0]
                prev_port = d[1]
                prev_username = d[2]
        else:
            prev_ip = ""
            prev_port = ""
            prev_username = ""
        self.cols = 2
        self.add_widget(Label(text="IP:"))
        self.ip = TextInput(text=prev_ip, multiline=False)
        self.add_widget(self.ip)
    
        self.add_widget(Label(text="Port:"))
        self.port = TextInput(text=prev_port, multiline=False)
        self.add_widget(self.port)
    
        self.add_widget(Label(text="Username:"))
        self.username = TextInput(text=prev_username,multiline=False)
        self.add_widget(self.username)

        self.join = Button(text="Join")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)

    def join_button(self, instance):
        port = self.port.text
        ip = self.ip.text
        username = self.username.text 
        
        with open("prev_details.txt", "w") as file:
            file.write(f"{ip},{port},{username}")
        info = f"Attepting to join {ip}:{port} and {username}"
        chatApp.info_page.update_info(info)
        chatApp.screen_manager.current = "Info"
        # Clock.schedule_ince(self.connect, 1)
    def connect(self, _):
        port = int(self.port.text)
        ip = self.ip 
        username = self.username.text
        chatApp.create_chat_page()
        chatApp.screen_manager.current = "Chat"

class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.message = Label(halign="center", valign="middle", font_size=30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)

    def update_info(self, message):
        self.message.text = message
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width*0.9, None)


class ChatPage(GridLayout):
    def __init__(slef, **kwagrs):
        super().__init__(**kwagrs)
        self.cols = 1
        self.add_widget(Label(text="Hey it at least woked up till this point"))





class EpicApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.connect_page = ConnectPage()
        screen = Screen(name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.info_page = InfoPage()
        screen = Screen(name="Info")
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager
    def create_chat_page(self):
        self.chat_page = ChatPage()
        screen = Screen(name="Chat")
        screen.add_widget(self.chat_page)
        self.screen_manager.add_widget(screen)

def show_error(message):
    chat_app_.info_page.update_info(message)
    chat_app.screen_manager.current = "Info"
    Clock.schedule_once(sys.exit, 10)

if __name__ == "__main__":
    chatApp = EpicApp()
    chatApp.run()
