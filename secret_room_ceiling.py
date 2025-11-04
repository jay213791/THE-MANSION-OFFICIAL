from ursina import *
from ursina.shaders import basic_lighting_shader

def secret_room_ceiling():
    ceiling = Entity(
        model='secret_room_hallway_ceiling.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    ceiling = Entity(
        model='secret_room_hallway_ceiling1.glb',
        collider='box',
        shader=basic_lighting_shader
    )
