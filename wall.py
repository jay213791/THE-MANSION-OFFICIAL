from ursina import *
from ursina.shaders import basic_lighting_shader

def wall():
    # WALL
    outer = Entity(
        model='outer_front.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    outer1 = Entity(
        model='outer_left.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    outer2 = Entity(
        model='outer_right.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    outer3 = Entity(
        model='outer_back.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall1 = Entity(
        model='out1.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall2 = Entity(
        model='out2.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall3 = Entity(
        model='wall3.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall4 = Entity(
        model='wall4.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall5 = Entity(
        model='wall5.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall6 = Entity(
        model='wall6.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall7 = Entity(
        model='wall7.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall8 = Entity(
        model='wall8.glb',
        collider='box',
        shader=basic_lighting_shader
    )

    wall9 = Entity(
        model='wall10.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall10 = Entity(
        model='wall11.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall11 = Entity(
        model='wall12.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall12 = Entity(
        model='wall13.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall13 = Entity(
        model='wall14.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall14 = Entity(
        model='wall15.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall15 = Entity(
        model='wall16.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    wall15 = Entity(
        model='Pantakip.glb',
        collider='box',
        shader=basic_lighting_shader
    )

    # PILARR
    pillar = Entity(
        model='pillar.glb',
        collider='box',
        shader=basic_lighting_shader
    )

    # STAIRS WALLL
    stair_wall = Entity(
        model='stairs_front_center_wall.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    stair_wall1 = Entity(
        model='stairs_front_left_wall.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    stair_wall2 = Entity(
        model='stairs_front_right_wall.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    stair_wall3 = Entity(
        model='stairs_side_right_wall.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    stair_wall4 = Entity(
        model='stairs_side_left_wall.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    stair_wall5 = Entity(
        model='stairs_wall_back.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    door1_upper_wall = Entity(
        model='door1_upper_wall.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    door2_upper_wall = Entity(
        model='door2_upper_wall.glb',
        collider='box',
        shader=basic_lighting_shader
    )
