from ursina import *
from ursina.shaders import basic_lighting_shader

def second_floor_furniture():
    # --- hallway ---
    bookshelf = Entity(
        model='second_floor_bookshelf.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    bookshelf1 = Entity(
        model='second_floor_bookshelf1.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    chair = Entity(
        model='second_floor_chair.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    ladder = Entity(
        model='second_floor_ladder.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    picture = Entity(
        model='second_floor_picture.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    table = Entity(
        model='second_floor_table.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    table1 = Entity(
        model='second_floor_table1.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    table2 = Entity(
        model='second_floor_table2.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    light = Entity(
        model='second_floor_light.glb',
        collider='box',
        shader=basic_lighting_shader
    )

    # --- BATHROOM ---
    bathtub = Entity(
        model='second_floor_bathroom_bathtub.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    bowl = Entity(
        model='second_floor_bathroom_bowl.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    cabinet = Entity(
        model='second_floor_bathroom_cabinet.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    carpet = Entity(
        model='second_floor_bathroom_carpet.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    sink = Entity(
        model='second_floor_bathroom_sink.glb',
        collider='box',
        shader=basic_lighting_shader
    )

    # --- ROOM1 ---
    cabinet = Entity(
        model = 'second_floor_room1_cabinet.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    cabinet = Entity(
        model = 'second_floor_room1_cabinet1.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    fan = Entity(
        model = 'second_floor_room1_fan.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    bed = Entity(
        model = 'second_floor_room1_bed.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    bed = Entity(
        model = 'second_floor_room1_bed1.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )

    # --- ROOM2 ---
    cabinet = Entity(
        model = 'second_floor_room2_cabinet.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    cabinet = Entity(
        model = 'second_floor_room2_cabinet1.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    bed = Entity(
        model = 'second_floor_room2_bed.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    fan = Entity(
        model = 'second_floor_room2_fan.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    lamp = Entity(
        model = 'second_floor_room2_lamp.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )

    # --- ROOM3 ---
    cabinet = Entity(
        model = 'second_floor_room3_cabinet.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    cabinet1 = Entity(
        model='second_floor_room3_cabinet1.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    bed = Entity(
        model='second_floor_room3_bed.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    lamp = Entity(
        model='second_floor_room3_lamp.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    fan = Entity(
        model='second_floor_room3_fan.glb',
        collider='box',
        shader=basic_lighting_shader
    )

    # --- ROOM4 ---
    cabinet = Entity(
        model = 'second_floor_room4_cabinet.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    cabinet = Entity(
        model = 'second_floor_room4_cabinet1.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    cabinet = Entity(
        model = 'second_floor_room4_cabinet2.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    cabinet = Entity(
        model = 'second_floor_room4_cabinet3.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    box_chest = Entity(
        model = 'box_chest2.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    bed = Entity(
        model = 'second_floor_room4_bed.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    lamp = Entity(
        model = 'second_floor_room4_lamp.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )

    #-- SECRET ROOM & SECRET ROOM HALLWAY
    torch = Entity(
        model = 'secret_room_hallway_torch.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    torch = Entity(
        model = 'secret_room_hallway_torch1.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    torch = Entity(
        model = 'secret_room_hallway_torch2.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    torch = Entity(
        model = 'secret_room_hallway_torch3.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    torch = Entity(
        model = 'secret_room_hallway_torch4.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    torch = Entity(
        model = 'secret_room_hallway_torch5.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    torch = Entity(
        model = 'secret_room_hallway_torch6.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )

    star = Entity(
        model='star.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    table = Entity(
        model='secret_room_table1.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    box = Entity(
        model='box_body.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    cabinet = Entity(
        model='secret_room_cabinet.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    cabinet1 = Entity(
        model='secret_room_cabinet1.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    table1 = Entity(
        model='secret_room_table.glb',
        collider='box',
        shader=basic_lighting_shader
    )




