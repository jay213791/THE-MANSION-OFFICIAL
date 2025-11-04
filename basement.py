from ursina import *
from ursina.shaders import basic_lighting_shader

def basement():
    # Basement WALL & FLOOR
    basement_wall = Entity(
        model='basement_wall.glb',
        shader=basic_lighting_shader
    )
    basement_floor = Entity(
        model='basement_floor.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    basement_support_right = Entity(
        model='cube',
        collider='box',
        scale=(0.2, 5.2, 12),
        position=(-19, -2.5, 6),
        color=color.red,
        visible=False
    )
    basement_support_left = Entity(
        model='cube',
        collider='box',
        scale=(0.2, 5.2, 12),
        position=(-7.7, -2.5, 6),
        color=color.red,
        visible=False
    )
    basement_support_back = Entity(
        model='cube',
        collider='box',
        scale=(0.2, 5.2, 12),
        position=(-13, -2.5, 11.5),
        rotation=(0, 90, 0),
        color=color.red,
        visible=False
    )
    basement_support_front = Entity(
        model='cube',
        collider='box',
        scale=(0.2, 5.2, 12),
        position=(-13, -2.5, 1),
        rotation=(0, 90, 0),
        color=color.red,
        visible=False
    )