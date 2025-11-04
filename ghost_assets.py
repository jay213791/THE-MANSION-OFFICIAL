from ghost.ghost_function import Ghost, look_back, Steady, Steady1, Steady2, sound
from ursina import *
from ursina.shaders import basic_lighting_shader

def create_ghosts(player):
    whisper = Audio('ghost/ghost_assets/scary-ghost-whisper.wav', autoplay=False)
    whisper1 = Audio('ghost/ghost_assets/girl_child.wav', autoplay=False)
    whisper2 = Audio('ghost/ghost_assets/get_out.wav', autoplay=False)
    whisper3 = Audio('ghost/ghost_assets/monster-laugh.wav', autoplay=False)
    whisper4 = Audio('ghost/ghost_assets/cry_sound.wav', autoplay=False)
    whisper5 = Audio('ghost/ghost_assets/black_sounud.wav', autoplay=False)
    whisper6 = Audio('ghost/ghost_assets/monster-scream-1-45669.wav', autoplay=False)
    whisper7 = Audio('ghost/ghost_assets/scream-noise-142446.wav', autoplay=False)
    whisper8 = Audio('ghost/ghost_assets/play.wav', autoplay=False)





    ghost1 = Ghost(
        player=player,
        model='ghost/ghost_assets/horror__girl___character.glb',
        scale=(1.5, 2.5, 1),
        position=(20, 5.2, 0),
        speed= 10,
        whisper_sounds=[whisper7]
    )
    ghost1.jumpscare_image = 'ghost/ghost_assets/hands_hands.png'
    ghost1.scream_sound = Audio('ghost/ghost_assets/scary-scream.wav', autoplay=False)

    look_ghost = look_back(
        player=player,
        model='ghost/ghost_assets/horror__girl___character.glb',
        color=color.white,
        scale=(1, 3, 1),
        position=(-7.5, 6, -2),
        speed=7,
        whisper_sound=whisper
    )
    look_ghost.jumpscare_image = 'ghost/ghost_assets/hands_hands.png'
    look_ghost.scream_sound = Audio('ghost/ghost_assets/scary-scream.wav', autoplay=False)

    ghost2 = Steady(
        player=player,
        model='horror__girl___character.glb',
        scale=(1, 2, 1),
        position=(7.5, 5.5, 9),
        whisper_sounds=[whisper2]
    )
    ghost2.scream_sound = Audio('scary-scream.wav', autoplay=False)

    ghost3 = Steady(
        player=player,
        model='shadow_wraith.glb',
        scale=(1, 2.7, 1),
        position=(82, 5.4, -0.7),
        color = color.black,
        speed=2,
        shader=basic_lighting_shader,
        whisper_sounds=[whisper3]
    )
    ghost3.scream_sound = Audio('scary-scream.wav', autoplay=False)

    ghost4 = Steady2(
        player=player,
        model='ghost/ghost_assets/creepy_teen_girl.glb',
        scale=(1, 1, 1),
        position=(85, 5.3, -0.7),
        shader=basic_lighting_shader,
        whisper_sounds=[whisper8, whisper2]
    )
    ghost4.jumpscare_image = 'ghost/ghost_assets/2nd_jumpscare.png'
    ghost4.scream_sound = Audio('scary-scream.wav', autoplay=False)

    ghost5 = sound(
        whisper_sounds=[whisper4, whisper3]
    )

    ghost6 = Steady(
        player=player,
        model='shadow_wraith.glb',
        scale=(1.5, 1.7, 1),
        position=(9, 6, -9),
        color = color.black,
        shader=basic_lighting_shader,
        whisper_sounds=[whisper5]
    )
    ghost7 = sound(
        whisper_sounds=[whisper6, whisper3]
    )
    ghost8 = Steady(
        player=player,
        model='ghost/ghost_assets/creepy_teen_girl.glb',
        scale=(1, 1, 1),
        position=(2, 5.18, -10.5),
        shader=basic_lighting_shader,
        whisper_sounds=[whisper1]
    )

    ghost9 = Steady1(
        player=player,
        model='ghost/ghost_assets/creepy_teen_girl.glb',
        scale=(1, 1, 1),
        position=(-12.4,3.6,-2.5),
        shader=basic_lighting_shader,
        whisper_sounds=[whisper2]
    )




    return [ghost1, look_ghost, ghost2, ghost3, ghost4, ghost5, ghost6, ghost7, ghost8, ghost9]
