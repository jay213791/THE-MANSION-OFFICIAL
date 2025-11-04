from ursina import *

class Setting(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent = camera.ui, enabled = False)

        self.hover_sound = Audio('assets/hover.wav', autoplay = False)

        self.bg = Entity(
            parent = self,
            model = 'quad',
            texture = 'assets/background.png',
            scale = (2.2, 1),
            z = 1
        )
        self.shadow = Text(
            parent = self,
            text = "The \n Mansion",
            font = 'assets/GideonRoman-Regular.ttf',
            color = color.black66,
            scale = 4.4,
            origin = (0, 0),
            y = .3
        )
        self.title = Text(
            parent = self,
            text = "The \n Mansion",
            font='assets/GideonRoman-Regular.ttf',
            color = color.red,
            scale = 4,
            y = .3,
            origin = (0,0)
        )

        self.exit_btn = Button(
            parent = self,
            text = "Exit",
            position = (0, -.1),
            origin = (0, 0),
            scale = (.2,0.2),
            color = color.rgba(0, 0, 0, 0),
            text_color = color.white66,
        )
        self.exit_btn.on_click = application.quit

        self.little_text = Text(
            parent = self,
            text = "Press ESC to go back",
            font='assets/GideonRoman-Regular.ttf',
            color = color.yellow,
            scale = 0.9,
            position = (0, -.2),
            origin = (0,0)
        )

        self.exit_btn.text_entity.scale = 9
        self.exit_btn.z = 1
        self.exit_btn.text_entity.font = 'assets/GideonRoman-Regular.ttf'

        self.exit_btn.on_mouse_enter = lambda: self.on_hover(self.exit_btn, True)
        self.exit_btn.on_mouse_exit = lambda: self.on_hover(self.exit_btn, False)


    def toggle(self):
        self.enabled = not self.enabled
        mouse.locked = not self.enabled

    def on_hover(self, button, state):
        if state:
            button.text_entity.color = color.red
            self.hover_sound.play()
        else:
            button.text_entity.color = color.white66