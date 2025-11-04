from ursina import *
from ursina.shaders import basic_lighting_shader

def secret_room_wall():
    wall = Entity(
        model='secret_room_hallway_wall.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall1 = Entity(
        model='secret_room_hallway_wall1.glb',
        collider='box',
        shader=basic_lighting_shader
    )

    # -- secret room --
    wall1 = Entity(
        model='secret_room_wall.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall1 = Entity(
        model='secret_room_wall1.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall1 = Entity(
        model='secret_room_wall2.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall1 = Entity(
        model='secret_room_wall3.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall1 = Entity(
        model='secret_room_wall4.glb',
        collider='box',
        shader=basic_lighting_shader
    )


