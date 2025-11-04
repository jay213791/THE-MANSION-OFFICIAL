from ursina import *

class Drawer(Entity):
    def __init__(self, locked = False, required_item = None, **kwargs):
        super().__init__(collider = 'box', **kwargs)
        self.is_open = False
        self.locked = locked
        self.required_item = required_item
        self.start_position = self.position
        self.open_offset = Vec3(-0.4, 0, 0)
        self.open_offset1 = Vec3(0, 0, -0.4)
        self.open_sound = Audio('assets/drawer-open.wav', autoplay=False)
        self.close_sound = Audio('assets/drawer_close.wav', autoplay=False)

    def try_unlock(self, held_key):
        if not self.locked:
            return True
        if held_key is None:
            return False
        elif held_key != self.required_item:
            return "wrong"
        else:
            self.locked = False
            if hasattr(held_key, 'hud_icon') and held_key.hud_icon:
                destroy(held_key.hud_icon)
            held_key.visible = False
            return True

    def toggle(self):
        if self.is_open:
            self.close()
        else:
            self.open()

    def toggle1(self):
        if self.is_open:
            self.close()
        else:
            self.open1()

    def open(self):
        target = self.start_position + self.open_offset
        self.animate_position(target, duration = 0.6)
        self.is_open = True
        self.open_sound.play()

    def open1(self):
        target = self.start_position + self.open_offset1
        self.animate_position(target, duration = 0.6)
        self.is_open = True
        self.open_sound.play()

    def close(self):
        self.animate_position(self.start_position, duration=0.6)
        self.is_open = False
        self.close_sound.play()

class Painting(Entity):
    def __init__(self, locked = False, required_item = None, **kwargs):
        super().__init__(collider = 'box', **kwargs)
        self.is_open = False
        self.locked = locked
        self.required_item = required_item
        self.open_sound = Audio('assets/drawer-open.wav', autoplay=False)
        self.close_sound = Audio('assets/drawer_close.wav', autoplay=False)

    def try_unlock(self, held_key):
        if not self.locked:
            return True
        if held_key is None:
            return False
        elif held_key != self.required_item:
            return "wrong"
        else:
            self.locked = False
            if hasattr(held_key, 'hud_icon') and held_key.hud_icon:
                destroy(held_key.hud_icon)
            held_key.visible = False
            return True

    def toggle(self):
        if self.is_open:
            self.close()
        else:
            self.open()

    def open(self):
        self.animate_rotation_y(90, duration=0.5)
        self.is_open = True
        self.open_sound.play()

    def close(self):
        self.animate_rotation_y(0, duration=0.5)
        self.is_open = False
        self.close_sound.play()

class Password(Entity):
    def __init__(self, password="1234",**kwargs):
        super().__init__(
            **kwargs
        )
        self.correct_code = str(password)
        self.entered_code = ""
        self.is_open = False
        self.locked = True
        self.keypad_ui = None
        self.code_display = None
        self.open_audio = Audio('assets/painting_open.wav', autoplay=False)
        self.keypad_audio = Audio('assets/keypad_sound.wav', autoplay=False)

    def try_unlock(self):
        if self.locked:
            self.open_keypad()
        else:
            self.open()

    def open_keypad(self):
        if not self.locked:
            return

        if self.keypad_ui:
            return

        mouse.visible = True
        mouse.locked = False
        self.keypad_audio.play()
        self.keypad_ui = Entity(parent=camera.ui)
        bg = Entity(
            parent=self.keypad_ui,
            model='quad',
            texture = 'assets/passcode_bg.png',
            scale=(0.5, 0.6),
            position=(0, 0),
            z=1
        )
        self.display_bg = Entity(
            parent=self.keypad_ui,
            model='quad',
            color=color.white10,
            scale=(0.3, 0.1),
            position=(0, 0.20),
            z=-0.1
        )
        self.code_display = Text(
            parent=self.keypad_ui,
            text="", y=0.21,
            x=-0.08,
            scale=2,
            color=color.black,
            z=-1
        )

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        positions = [
            (-0.1, 0.1), (0, 0.1), (0.1, 0.1),
            (-0.1, 0), (0, 0), (0.1, 0),
            (-0.1, -0.1), (0, -0.1), (0.1, -0.1),
            (0, -0.2)
        ]

        for num, pos in zip(numbers, positions):
            b = Button(
                text=str(num),
                parent=self.keypad_ui,
                scale=(0.1, 0.1),
                position=pos,
                texture = 'assets/button.png',
                color = color.white
            )
            b.text_entity.scale = 14
            b.text_entity.color = color.white
            b.on_click = lambda n=num: self.add_digit(n)

        enter_btn = Button(
            text="Enter",
            parent=self.keypad_ui,
            scale=(0.15, 0.1),
            position=(0.15, -0.2),
            texture='assets/enter.png',
            color=color.white,
            z=-1
        )
        enter_btn.on_click = self.check_code

        clear_btn = Button(
            text="Clear",
            parent=self.keypad_ui,
            scale=(0.15, 0.1),
            position=(-0.15, -0.2),
            texture='assets/clear.png',
            color = color.white,
            z=-1
        )
        clear_btn.on_click = self.clear_code

        exit_btn = Button(
            text="X",
            parent=self.keypad_ui,
            scale=(0.06, 0.06),
            position=(0.20, 0.25),
            color=color.rgba32(148, 0, 0, 204),
            z=-1
        )
        exit_btn.on_click = self.close_keypad

    def add_digit(self, num):
        if len(self.entered_code) < 6:
            self.entered_code += str(num)
            self.code_display.text = "*" * len(self.entered_code)

    def clear_code(self):
        self.entered_code = ""
        self.code_display.text = ""

    def check_code(self):
        if len(self.entered_code) < 6:
            wrong_text = Text("NOT ENOUGH NUMBER!", origin=(0, 0), scale=1.5, color=color.red, z=-1)
            invoke(destroy, wrong_text, delay=1)
            self.clear_code()
            return

        if self.entered_code == self.correct_code:
            self.unlock()
            return

        wrong_text = Text("Incorrect Passcode!", origin=(0, 0), scale=2, color=color.red, z=-1)
        invoke(destroy, wrong_text, delay=1)
        self.clear_code()

    def unlock(self):
        self.locked = False
        self.close_keypad()
        self.open()

    def open(self):
        if not self.is_open:
            self.animate_rotation_y(90, duration=0.5)
            self.is_open = True
            self.open_audio.play()

    def close_keypad(self):
        if self.keypad_ui:
            destroy(self.keypad_ui)
            self.keypad_ui = None
            self.code_display = None
            self.entered_code = ""

        mouse.visible = False
        mouse.locked = True

class Arm(Entity):
    def __init__(self, locked=False, required_item=None, **kwargs):
        super().__init__(collider='box', **kwargs)
        self.is_open = False
        self.locked = locked
        self.required_item = required_item
        self.place_audio = Audio('assets/place_item.wav', autoplay=False)

    def try_unlock(self, held_item):
        if not self.locked:
            return True
        if held_item is None:
            return False
        elif held_item != self.required_item:
            return "wrong"
        else:
            self.locked = False
            if hasattr(held_item, 'hud_icon') and held_item.hud_icon:
                destroy(held_item.hud_icon)
            held_item.visible = False
            return True

    def open(self):
        self.is_open = True
        self.place_audio.play()

class Secret_cabinet(Entity):
    def __init__(self, **kwargs):
        super().__init__(collider='box', **kwargs)
        self.is_open = False
        self.open_sound = Audio('assets/drawer-open.wav', autoplay=False)

    def open(self):
        if not self.is_open:
            self.animate_rotation_y(20, duration=0.6, curve=curve.in_out_quad)
            self.is_open = True
            self.open_sound.play()

class chest(Entity):
    def __init__(self, locked=False, required_item=None, **kwargs):
        super().__init__(collider='box', **kwargs)
        self.is_open = False
        self.locked = locked
        self.required_item = required_item
        self.open_audio = Audio('assets/Chest_open.wav', autoplay=False)
        self.close_audio = Audio('assets/drawer_close.wav', autoplay=False)


    def try_unlock(self, held_item):
        if not self.locked:
            return True
        if held_item is None:
            return False
        elif held_item != self.required_item:
            return "wrong"
        else:
            self.locked = False
            if hasattr(held_item, 'hud_icon') and held_item.hud_icon:
                destroy(held_item.hud_icon)
            held_item.visible = False
            return True

    def toggle(self):
        if self.is_open:
            self.close()
        else:
            self.open()

    def open(self):
        self.animate_rotation_z(50, duration=1)
        self.is_open = True
        self.open_audio.play()

    def close(self):
        self.animate_rotation_z(0, duration=0.5)
        self.is_open = False
        self.close_audio.play()

class Candle(Entity):
    def __init__(self, locked=False, required_item=None, **kwargs):
        super().__init__(collider='box', **kwargs)
        self.is_open = False
        self.locked = locked
        self.required_item = required_item
        self.place_audio = Audio('assets/place_item.wav', autoplay=False)

    def try_unlock(self, held_item):
        if not self.locked:
            return True
        if held_item is None:
            return False
        elif held_item != self.required_item:
            return "wrong"
        else:
            self.locked = False
            if hasattr(held_item, 'hud_icon') and held_item.hud_icon:
                destroy(held_item.hud_icon)
            held_item.visible = False
            return True

    def open(self):
        self.is_open = True
        self.place_audio.play()

class Candle_show(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            visible=False,
            **kwargs
        )

    def appear(self):
        self.visible = True

class PasswordBox(Entity):
    def __init__(self, password="1234",**kwargs):
        super().__init__(
            collider='box',
            **kwargs
        )
        self.correct_code = str(password)
        self.entered_code = ""
        self.is_open = False
        self.locked = True
        self.keypad_ui = None
        self.code_display = None
        self.keypad_audio = Audio('assets/keypad_sound.wav', autoplay=False)
        self.open_audio = Audio('assets/painting_open.wav', autoplay=False)


    def try_unlock(self):
        if self.locked:
            self.open_keypad()
        else:
            self.open()

    def open_keypad(self):
        if not self.locked:
            return

        if self.keypad_ui:
            return

        mouse.visible = True
        mouse.locked = False

        self.keypad_audio.play()
        self.keypad_ui = Entity(parent=camera.ui)
        bg = Entity(
            parent=self.keypad_ui,
            model='quad',
            texture='assets/passcode_bg.png',
            scale=(0.5, 0.7),
            position=(0, 0),
            z=1
        )
        self.display_bg = Entity(
            parent=self.keypad_ui,
            model='quad',
            color=color.white10,
            scale=(0.3, 0.1),
            position=(0, 0.20),
            z=-1
        )
        self.code_display = Text(
            parent=self.keypad_ui,
            text="", y=0.21,
            x=-0.038,
            scale=2,
            color=color.black,
            z=-1
        )
        self.code_title = Text(
            parent=self.keypad_ui,
            text="HOW MANY NAMES?", y=0.29,
            x=-0.12,
            scale=1
        )

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        positions = [
            (-0.1, 0.1), (0, 0.1), (0.1, 0.1),  # 1, 2, 3
            (-0.1, 0), (0, 0), (0.1, 0),  # 4, 5, 6
            (-0.1, -0.1), (0, -0.1), (0.1, -0.1),  # 7, 8, 9
            (0, -0.2)  # 0
        ]

        for num, pos in zip(numbers, positions):
            b = Button(
                text=str(num),
                parent=self.keypad_ui,
                scale=(0.1, 0.1),
                position=pos,
                texture='button.png',
                color=color.white
            )
            b.text_entity.scale = 14
            b.text_entity.color = color.white
            b.on_click = lambda n=num: self.add_digit(n)

        enter_btn = Button(
            text="Enter",
            parent=self.keypad_ui,
            scale=(0.15, 0.1),
            position=(0.15, -0.2),
            texture='assets/enter.png',
            color=color.white,
            z=-1
        )
        enter_btn.on_click = self.check_code

        clear_btn = Button(
            text="Clear",
            parent=self.keypad_ui,
            scale=(0.15, 0.1),
            position=(-0.15, -0.2),
            texture='assets/clear.png',
            color=color.white,
            z=-1
        )
        clear_btn.on_click = self.clear_code

        exit_btn = Button(
            text="X",
            parent=self.keypad_ui,
            scale=(0.06, 0.06),
            position=(0.20, 0.25),
            color=color.rgba32(148, 0, 0, 204),
            z=-1
        )
        exit_btn.on_click = self.close_keypad

    def add_digit(self, num):
        if len(self.entered_code) < 2:
            self.entered_code += str(num)
            self.code_display.text = self.entered_code

    def clear_code(self):
        self.entered_code = ""
        self.code_display.text = ""

    def check_code(self):

        if self.entered_code == self.correct_code:
            self.unlock()
            return

        wrong_text = Text("Incorrect Passcode!", origin=(0, 0), scale=2, color=color.red, z=-1)
        invoke(destroy, wrong_text, delay=1)
        self.clear_code()

    def unlock(self):
        self.locked = False
        self.close_keypad()
        self.open()

    def open(self):
        if not self.is_open:
            self.animate_rotation_y(-90, duration=1)
            self.is_open = True
            self.open_audio.play()

    def close_keypad(self):
        if self.keypad_ui:
            destroy(self.keypad_ui)
            self.keypad_ui = None
            self.code_display = None
            self.entered_code = ""

        mouse.visible = False
        mouse.locked = True




