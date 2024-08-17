
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

class MouseTrackerApp(App):
    def build(self):
        # Create a layout and a label to display the coordinates
        self.layout = BoxLayout(orientation='vertical')
        self.coord_label = Label(text='Move the mouse over this window')
        self.layout.add_widget(self.coord_label)

        # Bind the on_mouse_pos method to mouse movement
        Window.bind(mouse_pos=self.on_mouse_pos)
        Window.bind(on_touch_down=self.on_touch_down)
        
        return self.layout

    def on_mouse_pos(self, window, pos):
        # Update the label text with the mouse position
        x, y = pos
        self.coord_label.text = f'Mouse Position: ({x}, {y})'

    def on_touch_down(self, instance, touch):
        # Print the touch position (coordinates)
        print(f'Mouse Clicked at: ({touch.x}, {touch.y})')
        return True


MouseTrackerApp().run()