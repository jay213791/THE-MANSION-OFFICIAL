from ursina import *

class Doors(Entity):
    def __init__(self, locked = False, required_key = None, **kwargs):
        super().__init__(model = 'cube',texture = 'door.png',collider = 'box', **kwargs)
        self.is_open = False
        self.locked = locked
        self.required_key = required_key
        self.open_sound = Audio('assets/opening-door.wav', autoplay = False)
        self.close_sound = Audio('assets/door-close.wav', autoplay = False)
        self.unlock_sound = Audio('assets/unlock_door.wav', autoplay=False)

    def try_unlock(self, held_key):
        if not self.locked:
            return True
        if held_key is None:
            return False
        elif held_key != self.required_key:
            return "wrong"
        else:
            self.locked = False
            if hasattr(held_key, 'hud_icon') and held_key.hud_icon:
                destroy(held_key.hud_icon)
            held_key.visible = False
            self.unlock_sound.play()
            return True
    def toggle(self):
        if self.is_open:
            self.close()
        else:
            self.open()

    def open(self):
        self.animate_rotation_y(90, duration = 0.5)
        self.is_open = True
        self.open_sound.play()

    def close(self):
        self.animate_rotation_y(0, duration = 0.5)
        self.is_open = False
        self.close_sound.play()
