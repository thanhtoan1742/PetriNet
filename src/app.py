from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage

from petri_net import PetriNet

class MainApp(App):
    def reload_ui(self):
        self.net.draw(self.filename)
        self.image.reload()

        print(self.net.get_enabled_transitions())
        self.transition_dropdown.clear_widgets()
        for tran in self.net.get_enabled_transitions():
            btn = Button(text=tran, **self.button_props)
            btn.bind(on_release=lambda btn: self.transition_dropdown.select(btn.text))
            self.transition_dropdown.add_widget(btn)
        setattr(self.transition_button, 'text', self.transition_button_prompt)


    def fire_transition(self, btn):
        transition = self.transition_button.text
        if transition == self.transition_button_prompt:
            return
        self.net.fire_transition(transition)
        self.reload_ui()

    def build(self):
        self.filename = 'graph.png'
        self.transition_button_prompt = 'transition to fire'
        self.button_props = {
            'size_hint_y': None,
            'height': 40,
            'pos_hint': {'top': 1},
        }
        self.net = PetriNet()
        self.net.read_from_file('input.txt')

        layout = BoxLayout()
        self.image = Image(source=self.filename, size_hint_x=5/6)
        layout.add_widget(self.image)
        transition_chooser = StackLayout(orientation='lr-tb', size_hint_x=1/6)
        layout.add_widget(transition_chooser)

        self.transition_button = Button(text=self.transition_button_prompt, **self.button_props)
        transition_chooser.add_widget(self.transition_button)
        fire_button = Button(text='fire', **self.button_props, background_color='#EBE859')
        transition_chooser.add_widget(fire_button)

        self.transition_dropdown = DropDown()
        self.transition_button.bind(on_release=self.transition_dropdown.open)
        self.transition_dropdown.bind(on_select=lambda ins, x: setattr(self.transition_button, 'text', x))
        fire_button.bind(on_release=self.fire_transition)

        self.reload_ui()

        return layout


if __name__ == '__main__':
    MainApp().run()

