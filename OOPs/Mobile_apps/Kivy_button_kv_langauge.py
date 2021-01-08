from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    """ Comes from button.kv file I created"""
    def build(self):
        return Button()

    def on_press_button(self):
        print('You pressed the button !')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()
