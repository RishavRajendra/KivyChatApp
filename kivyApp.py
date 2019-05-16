import kivy
from kivy.app import App
from kivy.uix.label import Label

# For dev purposes, require kivy 1.10.1
kivy.require("1.10.1")

class ChatApp(App):
    # On build print Oola
    def build(self):
        return Label(text="Oola!")

if __name__ == '__main__':
    ChatApp().run()
