from ursina import *

class Key(Entity):
    def __init__(self, key_id=None, **kwargs):
        super().__init__(
            collider = 'box',
            **kwargs
        )
        self.key_id = key_id
        self.picked_up = False
        self.hud_icon = None
        self.pickup_audio = Audio('take_item.wav', autoplay= False)
        self.drop_audio = Audio('drop_sound.wav', autoplay= False)


    def pickup(self, player, icon_texture=None):
        if self.picked_up:
            return
        self.parent = player
        self.position = (0.5, 1.3, 0.8)
        self.picked_up = True
        self.pickup_audio.play()

        if icon_texture:
            self.hud_icon = Sprite(
                parent = camera.ui,
                texture = icon_texture,
                scale = 0.05,
                x = -0.80, y = 0.40
            )

    def drop(self, player):
        if not self.picked_up:
            return
        self.parent = scene
        self.position = player.position + Vec3(1,0,1)
        self.picked_up = False
        self.drop_audio.play()
        if self.hud_icon:
            destroy(self.hud_icon)
            self.hud_icon = None

class Item(Entity):
    def __init__(self, item_id=None, **kwargs):
        super().__init__(
            collider = 'box',
            **kwargs
        )
        self.item_id = item_id
        self.picked_up = False
        self.hud_icon = None
        self.pickup_audio = Audio('item_sound.wav', autoplay= False)
        self.drop_audio = Audio('drop_sound.wav', autoplay= False)

    def pickup(self, player, icon_texture=None):
        if self.picked_up:
            return
        self.parent = player
        self.position = (0.5, 1.3, 0.8)
        self.rotation = (90, 1, 0)
        self.picked_up = True
        self.pickup_audio.play()

        if icon_texture:
            self.hud_icon = Sprite(
                parent = camera.ui,
                texture = icon_texture,
                scale = 0.05,
                x = -0.80, y = 0.40
            )

    def drop(self, player):
        if not self.picked_up:
            return
        self.parent = scene
        self.position = player.position + Vec3(1, 0, 1)
        self.picked_up = False
        self.drop_audio.play()
        if self.hud_icon:
            destroy(self.hud_icon)
            self.hud_icon = None

class Item1(Entity):
    def __init__(self, item_id=None, **kwargs):
        super().__init__(
            collider = 'box',
            **kwargs
        )
        self.item_id = item_id
        self.picked_up = False
        self.hud_icon = None
        self.pickup_audio = Audio('item_sound.wav', autoplay=False)
        self.drop_audio = Audio('drop_sound.wav', autoplay=False)

    def pickup(self, player, icon_texture=None):
        if self.picked_up:
            return
        self.parent = player
        self.position = (-1, 1.3, 0.8)
        self.rotation = (90, 1, 0)
        self.picked_up = True
        self.pickup_audio.play()

        if icon_texture:
            self.hud_icon = Sprite(
                parent = camera.ui,
                texture = icon_texture,
                scale = 0.05,
                x = -0.80, y = 0.40
            )

    def drop(self, player):
        if not self.picked_up:
            return
        self.parent = scene
        self.position = player.position + Vec3(0, 0.4, 0)
        self.picked_up = False
        self.drop_audio.play()
        if self.hud_icon:
            destroy(self.hud_icon)
            self.hud_icon = None

class Item2(Entity):
    def __init__(self, item_id=None, **kwargs):
        super().__init__(
            collider = 'box',
            **kwargs
        )
        self.item_id = item_id
        self.picked_up = False
        self.hud_icon = None
        self.pickup_audio = Audio('item_sound.wav', autoplay=False)
        self.drop_audio = Audio('drop_sound.wav', autoplay=False)

    def pickup(self, player, icon_texture=None):
        if self.picked_up:
            return
        self.parent = player
        self.position = (1, 1.3, 1.3)
        self.picked_up = True
        self.pickup_audio.play()

        if icon_texture:
            self.hud_icon = Sprite(
                parent = camera.ui,
                texture = icon_texture,
                scale = 0.03,
                x = -0.80, y = 0.40
            )

    def drop(self, player):
        if not self.picked_up:
            return
        self.parent = scene
        self.position = player.position + Vec3(0, 0.1, 0)
        self.picked_up = False
        self.drop_audio.play()
        if self.hud_icon:
            destroy(self.hud_icon)
            self.hud_icon = None


class Picture(Entity):
    total_pictures = 4
    collected_count = 0
    progress_text = None
    cutscene_started = False

    def __init__(self, pics_id=None, **kwargs):
        super().__init__(
            collider='box',
            **kwargs
        )
        self.pics_id = pics_id
        self.picked_up = False
        self.pickup_audio = Audio('assets/paper_sound.wav', autoplay=False)

    def pickup(self, player):
        if self.picked_up:
            return
        self.picked_up = True
        self.pickup_audio.play()
        destroy(self)

        Picture.collected_count += 1

        if Picture.collected_count == Picture.total_pictures and not Picture.cutscene_started:
            Picture.cutscene_started = True
            self.start_cutscene()

    def start_cutscene(self):
        mouse.visible = False

        dialogue = [
            "Next....",
            "Once, there was a lonely child Eliora \nignored and unseen by her family. \n"
            "Every night, she whispered to her only friend,\n "
            "a shadow that listened when no one else would.",
            "He told her she could make them love her — \n"
            "all she had to do was read from a special book.\nA book he gave her,\n bound in red and whispering her name.",
            "She believed him. \nShe only wanted to be loved. \n",
            "That night, the air turned cold. \nThe candles burned black.",
            "And one by one, her family began to scream. \nBy morning… they were gone.",
            "Her friend laughed  a voice no longer soft, but monstrous. \nHe had tricked her. \n"
            "The book wasn’t for love. \nIt was a curse, and she was now bound to it.",
            "For years, everyone believed an\n outsider had cursed the family\n — a witch, a jealous spirit, a stranger’s vengeance.\n But the truth was far darker.",
            "The curse was born from within.\n Long ago, one of Eliora’s ancestors made a forbidden pact\n — a promise sealed in blood binding their bloodline\n to the very shadow that deceived her.\n Eliora never summoned it… she inherited it.",
            "Now, her soul roams the house\n — trapped, crying, waiting to be freed.\n Her imaginary friend still lurks in the dark corners,\n feeding on regret… a piece of her family’s sin that refuses to die.",
            "And you… \n You are the one who free the cursed child.",
            "....",

        ]

        audio_for_dialogue = {
            1: 'frame_assets/Audio_1.wav',
            2: 'frame_assets/Audio_2.wav',
            3: 'frame_assets/Audio_3.wav',
            4: 'frame_assets/Audio_4.wav',
            5: 'frame_assets/Audio_5.wav',
            6: 'frame_assets/Audio_6.wav',
            7: 'frame_assets/audio_9.wav',
            8: 'frame_assets/audio_10.wav',
            9: 'frame_assets/audio_11.wav',
            10: 'frame_assets/Audio_7.wav',
            11: 'frame_assets/Audio_8.wav',

        }

        backgrounds = [load_texture(path) for path in [
            'frame_assets/frame_7.png',
            'frame_assets/frame_1.png',
            'frame_assets/frame_2.png',
            'frame_assets/frame_3.png',
            'frame_assets/frame_4.png',
            'frame_assets/frame_5.png',
            'frame_assets/frame_6.png',
            'frame_assets/frame_9.png',
            'frame_assets/frame_10.png',
            'frame_assets/frame_11.png',
            'frame_assets/frame_7.png',
            'frame_assets/frame_8.png',
        ]]

        current_index = 0
        current_audios = []

        bg = Entity(
            parent=camera.ui,
            model='quad',
            scale=(window.aspect_ratio, 1),
            texture=backgrounds[0]
        )
        story_text = Text(
            text='',
            origin=(0, 0),
            y=-.3,
            scale=2,
            color=color.white,
            font = 'assets/GideonRoman-Regular.ttf'
        )
        continue_text = Text(
            text='Press SPACE to continue',
            origin=(0, 0),
            y=-.43,
            scale=1,
            color=color.yellow,
            enabled=False
        )

        def type_writer(text, delay=0.06):
            story_text.text = ''
            continue_text.enabled = False
            for char in text:
                story_text.text += char

                for _ in range(max(1, int(delay * 60))):
                    yield
            continue_text.enabled = True

        text_animation = type_writer(dialogue[current_index])

        def cutscene_update():
            nonlocal text_animation
            try:
                next(text_animation)
            except StopIteration:
                pass

        bg.update = cutscene_update

        def cutscene_input(key):
            nonlocal current_index, text_animation, current_audios
            if key == 'space' and continue_text.enabled:
                current_index += 1
                if current_index < len(dialogue):
                    bg.texture = backgrounds[current_index]
                    text_animation = type_writer(dialogue[current_index])

                    if current_index in audio_for_dialogue:
                        audio_path = audio_for_dialogue[current_index]
                        sfx = Audio(audio_path, autoplay=True)
                        sfx.volume = 1.5
                        current_audios.append(sfx)
                else:
                    bg.animate_color(color.clear, duration=0.8)
                    story_text.animate_color(color.clear, duration=0.8)
                    continue_text.animate_color(color.clear, duration=0.8)
                    invoke(application.quit, delay=0.9)

        bg.input = cutscene_input



