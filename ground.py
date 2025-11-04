from ursina import *
from ursina.shaders import basic_lighting_shader



def ground():
    floor = Entity(
        model='floor1.glb',
        collider='box',
        shader=basic_lighting_shader,
    )
    floor1 = Entity(
        model='floor2.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    floor2 = Entity(
        model='floor3.glb',
        collider='box',
        shader=basic_lighting_shader
    )
