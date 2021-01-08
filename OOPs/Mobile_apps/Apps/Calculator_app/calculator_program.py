from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput # This is a widget provides a box for editable plain text
from kivy.properties import ObjectProperty

class CalcButtonsWidget(BoxLayout):
    '''
        This is my custom made Widget
        https://blog.kivy.org/2019/06/widget-interactions-between-python-and-kv/
    '''
    box_layout_created_python = ObjectProperty() # Adding this the ObjectProperty()
    def __init__(self, **kwargs):
        super(CalcButtonsWidget,self).__init__()

        # add our new button code
        buttons = [
            ["1", "2", "3", "-"],
            ["4", "5", "6", "*"],
            ["7", "8", "9", "/"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout(
                orientation='vertical',
                spacing=1,
            )
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={'center_x':0.5, 'center_y':0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
                self.add_widget(h_layout)
                self.box_layout_created_python = h_layout  # Save a reference

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        self.add_widget(equals_button)
        self.equal_button = equals_button

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            "Clear the solution widget"
            self.solution.text = ""
        else:
            if current and (
                    self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution



class OuterContainerWidget(BoxLayout):
    def on_touch_down(self, instance):
        print(instance)
        print("Inner box")

class CalculatorApp(App):
    '''This is going to be the Outer box layer'''

    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_operator = None
        self.last_button = None
        return OuterContainerWidget()


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
