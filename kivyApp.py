import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# For dev purposes, require kivy 1.10.1
kivy.require("1.10.1")

# ConnectPage inherits from GridLayout
class ConnectPage(GridLayout):
    def __init__(self,**kwargs):
        # Run __init__ of GridLayout
        super().__init__(**kwargs)
        self.cols = 2               # We'll have two columns

        # Add widgets
        self.add_widget(Label(text="IP:"))

        self.ip = TextInput(multiline=False)
        self.add_widget(self.ip)

        self.add_widget(Label(text="Port:"))

        self.port = TextInput(multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text="Username:"))

        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

class ChatApp(App):
    # On build print Oola
    def build(self):
        return ConnectPage()

if __name__ == '__main__':
    ChatApp().run()
