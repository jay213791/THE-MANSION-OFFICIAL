from ursina import *
from ursina.shaders import basic_lighting_shader

def stairs():
    # STAIRSS
    inner = Entity(
        model='inner.glb',
        shader=basic_lighting_shader
    )
    center_Center = Entity(
        model='center_Center.glb',
        collider='box',
        shader=basic_lighting_shader
    )

    first_right = Entity(
        model='first_right.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    first_left = Entity(
        model='first_left.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    second_left_left = Entity(
        model='second_left_left.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    second_left_right = Entity(
        model='second_left_right.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    second_right_left = Entity(
        model='second_right_left.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    second_right_right = Entity(
        model='second_right_right.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    basement_stairs = Entity(
        model='basement_stair.glb',
        shader=basic_lighting_shader
    )
    second_floor_front = Entity(
        model = 'second_floor_front.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    second_floor_left = Entity(
        model = 'second_floor_left.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    second_floor_left1 = Entity(
        model = 'second_floor_left1.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    second_floor_right = Entity(
        model = 'second_floor_right.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    second_floor_right1 = Entity(
        model = 'second_floor_right1glb.glb',
        collider='box',
        shader=basic_lighting_shader
    )


    # STAIRS RAMP!!!
    ramp = Entity(
        model='cube',
        scale=(3, 2.8, 7.5),
        position=(-8, -0.3, -2.2),
        rotation=(25, 90, 0),
        collider='box',
        color=color.red,
        visible=False
    )
    ramp_right = Entity(
        model='cube',
        scale=(3, 0.5, 4),
        position=(-13, 3.3, 2),
        rotation=(25, 182, 0),
        collider='box',
        color=color.red,
        visible=False
    )
    ramp_left = Entity(
        model='cube',
        scale=(3, 0.5, 5.2),
        position=(-13, 3, -6.1),
        rotation=(25, 0, 0),
        collider='box',
        color=color.red,
        visible=False
    )
    ramp_basement = Entity(
        model='cube',
        scale=(3, 0.5, 10),
        position=(-16.5, -2.5, 7),
        rotation=(-30, 0, 0),
        collider='box',
        color=color.red,
        visible=False
    )