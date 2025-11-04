from ursina import *
from ursina.shaders import basic_lighting_shader

def floor_second_floor():
    floor = Entity(
        model='Floor.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    floor1 = Entity(
        model='Floor1.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    floor2 = Entity(
        model='Floor2.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    floor3 = Entity(
        model='Floor3.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    floor4 = Entity(
        model='Floor4.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    floor5 = Entity(
        model='Floor5.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    floor6 = Entity(
        model='Floor6.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    floor7 = Entity(
        model='Floor7.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    ceiling = Entity(
        model='second_floor_ceiling.glb',
        collider='box',
        shader=basic_lighting_shader
    )
