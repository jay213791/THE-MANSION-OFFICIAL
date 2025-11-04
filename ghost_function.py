from ursina import *
from math import atan2, degrees
import random

class Ghost(Entity):
    def __init__(self, player = None, whisper_sounds = None,speed = 6, **kwargs):
        super().__init__(
            visible = False,
            **kwargs
        )
        self.player = player
        self.speed = speed
        self.active = False
        self.jumpscare_image = None
        self.jumpscare_ui = None
        self.float_task = None

        if isinstance(whisper_sounds, list):
            self.whisper_sounds = whisper_sounds
        elif whisper_sounds is not None:
            self.whisper_sounds = [whisper_sounds]
        else:
            self.whisper_sounds = []

        self.has_whispered = False

    def appear(self):
        self.visible = True
        self.active = True
        self.start_floating()
        self.play_whisper()

    def disappear(self):
        self.visible = False
        self.active = False

        if self.jumpscare_ui:
            destroy(self.jumpscare_ui)
            self.jumpscare_ui = None

        self.stop_floating()

    def start_floating(self):
        def float_ghost():
            if not self.visible:
                return

            self.animate_y(self.y + 0.5, duration = 1, curve = curve.sin)
            invoke(lambda: self.animate_y(self.y - 0.5, duration = 1, curve = curve.sin), delay = 1)
            invoke(float_ghost, delay = 2)

        float_ghost()

    def stop_floating(self):
        self.float_task = None

    def play_whisper(self):
        if not self.has_whispered and self.whisper_sounds:
            for sound in self.whisper_sounds:
                sound.play()
            self.has_whispered = True

    def update(self):
        if self.active and self.player:
            direction = Vec3(
                self.player.x - self.x,
                0,
                self.player.z - self.z
            ).normalized()

            self.position += direction * self.speed * time.dt

            target_rotation = atan2(direction.x, direction.z)
            self.rotation = Vec3(0, degrees(target_rotation) + 180, 0)

            if distance(self.position, self.player.position) < 2:
                self.jumpscare()

    def jumpscare(self):
        if not self.jumpscare_ui and self.jumpscare_image:
            self.jumpscare_ui = Entity(
                parent = camera.ui,
                model = 'quad',
                texture = self.jumpscare_image,
                scale = (2, 1.5),
                z = -1
            )

            if hasattr(self, 'scream_sound'):
                self.scream_sound.play()

            invoke(self.disappear, delay = 1.5)

class look_back(Entity):
    def __init__(self, player = None, speed = 6, whisper_sounds = None, **kwargs):
        super().__init__(visible = False, **kwargs)
        self.player = player
        self.speed = speed
        self.active = False
        self.jumpscare_image = None
        self.jumpscare_ui = None
        self.jumpscare_triggered = False

        if isinstance(whisper_sounds, list):
            self.whisper_sounds = whisper_sounds
        elif whisper_sounds is not None:
            self.whisper_sounds = [whisper_sounds]
        else:
            self.whisper_sounds = []

        self.has_whispered = False

    def appear(self):
        if not self.player:
            return

        forward = self.player.forward
        self.position = self.player.position - forward * 3
        self.position = Vec3(self.position.x, self.player.y, self.position.z)

        self.rotation_y = self.player.rotation_y
        self.visible = True
        self.active = True
        self.has_whispered = False
        self.jumpscare_triggered = False

        self.start_floating()

        invoke(self.play_whisper, delay = 1)

    def disappear(self):
        self.visible = False
        self.active = False

        if self.jumpscare_ui:
            destroy(self.jumpscare_ui)
            self.jumpscare_ui = None

    def start_floating(self):
        def float_ghost():
            if not self.visible:
                return

            self.animate_y(self.y + 0.3, duration=1, curve=curve.sin)
            invoke(lambda: self.animate_y(self.y - 0.3, duration=1, curve=curve.sin), delay=1)
            invoke(float_ghost, delay=2)

        float_ghost()

    def play_whisper(self):
        if self.whisper_sound and not self.has_whispered:
            self.whisper_sound.play()
            self.has_whispered = True

    def update(self):
        if not (self.active and self.visible and self.player):
            return

        if self.active and self.player:
            direction = Vec3(
                self.player.x - self.x,
                0,
                self.player.z - self.z
            ).normalized()

            target_rotation = atan2(direction.x, direction.z)
            self.rotation = Vec3(0, degrees(target_rotation) + 180, 0)

        to_player = (self.player.position - self.position).normalized()
        player_forward = self.player.forward
        dot = player_forward.dot(to_player)

        if not self.jumpscare_triggered and dot < -0.7:
            self.jumpscare_triggered = True
            self.play_whisper()
            invoke(self.jumpscare, delay=1)

    def jumpscare(self):
        if not self.jumpscare_image:
            return

        self.jumpscare_ui = Entity(
            parent=camera.ui,
            model='quad',
            texture=self.jumpscare_image,
            scale=(2, 1.5),
            z=-1
        )

        if hasattr(self, 'scream_sound'):
            self.scream_sound.play()

        invoke(self.disappear, delay=1.5)

class Steady(Entity):
    def __init__(self, player = None, whisper_sounds = None, **kwargs):
        super().__init__(
            visible = False,
            **kwargs
        )
        self.player = player
        self.active = False
        self.looked_back = False
        self.float_task = None
        if isinstance(whisper_sounds, list):
            self.whisper_sounds = whisper_sounds
        elif whisper_sounds is not None:
            self.whisper_sounds = [whisper_sounds]
        else:
            self.whisper_sounds = []

        self.has_whispered = False

    def appear(self):
        self.visible = True
        self.active = True
        self.play_whisper()

    def disappear(self):
        self.visible = False
        self.active = False

    def play_whisper(self):
        if not self.has_whispered and self.whisper_sounds:
            for s in self.whisper_sounds:
                s.play()
            self.has_whispered = True

    def update(self):
        if not (self.active and self.visible and self.player):
            return

        direction = Vec3(
            self.player.x - self.x,
            0,
            self.player.z - self.z
        ).normalized()

        target_rotation = atan2(direction.x, direction.z)
        self.rotation = Vec3(0, degrees(target_rotation) + 180, 0)

        to_player = (self.player.position - self.position).normalized()
        player_forward = self.player.forward
        dot = player_forward.dot(to_player)

        if not self.looked_back and dot < -0.7:
            self.looked_back = True
            invoke(self.disappear, delay=1.5)


class Steady1(Entity):
    def __init__(self, player=None, whisper_sounds=None, **kwargs):
        super().__init__(
            visible=False,
            **kwargs
        )
        self.player = player
        self.active = False
        self.looked_back = False
        self.float_task = None
        if isinstance(whisper_sounds, list):
            self.whisper_sounds = whisper_sounds
        elif whisper_sounds is not None:
            self.whisper_sounds = [whisper_sounds]
        else:
            self.whisper_sounds = []

        self.has_whispered = False

    def appear(self):
        self.visible = True
        self.active = True
        self.play_whisper()

    def disappear(self):
        self.visible = False
        self.active = False

    def play_whisper(self):
        if not self.has_whispered and self.whisper_sounds:
            for s in self.whisper_sounds:
                s.play()
            self.has_whispered = True

    def update(self):
        if not (self.active and self.visible and self.player):
            return

        direction = Vec3(
            self.player.x - self.x,
            0,
            self.player.z - self.z
        ).normalized()

        target_rotation = atan2(direction.x, direction.z)
        self.rotation = Vec3(0, degrees(target_rotation) + 180, 0)

        to_player = (self.player.position - self.position).normalized()
        player_forward = self.player.forward
        dot = player_forward.dot(to_player)

        if not self.looked_back and dot < 0.7:
            self.looked_back = True
            invoke(self.disappear, delay=1.5)

class Steady2(Entity):
    def __init__(self, player=None, whisper_sounds=None, **kwargs):
        super().__init__(visible=False, **kwargs)
        self.player = player
        self.active = False

        if isinstance(whisper_sounds, list):
            self.whisper_sounds = whisper_sounds
        elif whisper_sounds is not None:
            self.whisper_sounds = [whisper_sounds]
        else:
            self.whisper_sounds = []

        self.has_whispered = False
        self.jumpscare_image = None
        self.jumpscare_ui = None
        self.scream_sound = None
        self.has_jumpscared = False

    def appear(self):
        self.visible = True
        self.active = True
        self.has_jumpscared = False
        self.play_whisper()

    def play_whisper(self):
        if not self.whisper_sounds:
            return
        whisper = random.choice(self.whisper_sounds)
        whisper.play()

    def random_whisper_loop(self):
        if not self.active or not self.visible:
            return
        if random.random() < 0.6:
            self.play_whisper()
        invoke(self.random_whisper_loop, delay=random.uniform(5, 10))

    def jumpscare(self):
        if self.has_jumpscared or not self.jumpscare_image:
            return
        self.has_jumpscared = True

        self.jumpscare_ui = Entity(
            parent=camera.ui,
            model='quad',
            texture=self.jumpscare_image,
            scale=(2, 1.5),
            z=-1
        )
        if self.scream_sound:
            self.scream_sound.play()
        invoke(self.remove_jumpscare_ui, delay=1.5)

    def remove_jumpscare_ui(self):
        if self.jumpscare_ui:
            destroy(self.jumpscare_ui)
            self.jumpscare_ui = None

    def update(self):
        if not (self.active and self.visible and self.player):
            return

        direction = Vec3(self.player.x - self.x, 0, self.player.z - self.z).normalized()
        target_rotation = atan2(direction.x, direction.z)
        self.rotation = Vec3(0, degrees(target_rotation) + 180, 0)

        if distance(self.position, self.player.position) < 1.5 and not self.has_jumpscared:
            self.jumpscare()


class sound(Entity):
    def __init__(self, whisper_sounds=None, **kwargs):
        super().__init__(
            **kwargs
        )
        self.whisper_sounds = whisper_sounds if whisper_sounds else []
        self.has_whispered = False


    def appear(self):
        self.play_whisper()


    def play_whisper(self):
        if not self.has_whispered and self.whisper_sounds:
            for s in self.whisper_sounds:
                s.play()
            self.has_whispered = True




