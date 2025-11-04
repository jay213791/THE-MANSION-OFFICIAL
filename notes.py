from ursina import *

class Items(Entity):
    def __init__(self, image_texture, **kwargs):
        super().__init__(**kwargs)
        self.image_ui = Entity(
            parent = camera.ui,
            model = 'quad',
            texture = image_texture,
            scale = (0.7, 0.7),
            visible = False
        )
        self.paper_sound = Audio('assets/paper_sound.wav', autoplay=False)

    def pickup(self):
        self.paper_sound.play()
        self.image_ui.visible = not self.image_ui.visible