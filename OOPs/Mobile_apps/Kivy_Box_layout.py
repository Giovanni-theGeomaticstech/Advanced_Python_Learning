import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]


class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(
                text=f"Button {i}",
                background_color=random.choice(colors),
                # Adding size_hint and pos_hint
                size_hint=(0.5, 0.5),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
            btn.bind(on_press=self.on_press_button)
            layout.add_widget(btn)
        return layout

    def on_press_button(self, instance):
        print("You pressed button")


if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()
