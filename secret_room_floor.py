from ursina import *
from ursina.shaders import basic_lighting_shader

def secret_room_floor():
    floor = Entity(
        model='secret_room_hallway_floor.glb',
        collider='box',
        shader=basic_lighting_shader
    )

    # -- secret room --
    floor1 = Entity(
        model='secret_room_floor.glb',
        collider='box',
        shader=basic_lighting_shader
    )

