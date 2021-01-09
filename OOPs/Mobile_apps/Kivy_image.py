from kivy.app import App
from kivy.uix.image import Image


class MainApp(App):
    def build(self):
        img = Image(
            source="kivy_text_output_sample.png",
            size_hint=(1, 0.5),
            pos_hint=dict(center_x=0.5, center_y=0.5),
        )
        return img


if __name__ == "__main__":
    app = MainApp()
    app.run()
