from ursina import *
from ursina.shaders import basic_lighting_shader


def first_floor_furniture():
    carpet = Entity(
        model = 'carpet.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    chandelier1 = Entity(
        model = 'chandelier1.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    plant= Entity(
        model = 'plant_stairs_left.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    plant1 = Entity(
        model = 'plant_stairs_right.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )

    #living room
    chest_box = Entity(
        model = 'box_chest1.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    box4_LR = Entity(
        model = 'box4_LR.glb',
        collider = 'box',
        shader=basic_lighting_shader
    )
    cabinet_LR = Entity(
        model='cabinet_LR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    cabinet_LR = Entity(
        model='cabinet_LR1.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    clock_LR = Entity(
        model='clock_LR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    fire_place_LR = Entity(
        model='fire_place_LR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    kurtina_LR = Entity(
        model='kurtina_LR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    piano_LR = Entity(
        model='piano_LR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    picture1_LR = Entity(
        model='picture1_LR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    plant_LR = Entity(
        model='plant_LR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    plant1_LR = Entity(
        model='plant1_LR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    sofa_LR = Entity(
        model='sofa_LR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    sofa1_LR = Entity(
        model='sofa1_LR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    sofa2_LR = Entity(
        model='sofa2_LR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    table_LR = Entity(
        model='table_LR.glb',
        collider='box',
        shader=basic_lighting_shader
    )

    #dining room
    cabinet_DR = Entity(
        model='cabinet_DR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    cabinet2_DR = Entity(
        model='cabinet2_DR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    cabinet4_DR = Entity(
        model='cabinet4_DR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    chair_DR = Entity(
        model='chair_DR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    chair1_DR = Entity(
        model='chair1_DR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    chair2_DR = Entity(
        model='chair2_DR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    chair3_DR = Entity(
        model='chair3_DR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    fan_DR = Entity(
        model='fan_DR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    picture1_DR = Entity(
        model='painting1_DR.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    table_DR = Entity(
        model='table_DR.glb',
        collider='box',
        shader=basic_lighting_shader
    )

    #kitchen room
    cabinet1_kitchen = Entity(
        model='cabinet1_kitchen.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    chandelier_kitchen = Entity(
        model='chandelier_kitchen.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    ref_kitchen = Entity(
        model='ref_kitchen.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    setup_kitchen = Entity(
        model='setup_kitchen.glb',
        collider='box',
        shader=basic_lighting_shader
    )

    #bathroom
    bathtub_bathroom_1 = Entity(
        model='bathtub_bathroom_1.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    sink_bathroom_1 = Entity(
        model='sink_bathroom_1.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    toilet_bathroom_1 = Entity(
        model='toilet_bathroom_1.glb',
        collider='box',
        shader=basic_lighting_shader
    )

    #library
    bookshelf1_library = Entity(
        model='bookshelf1_library.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    bookshelf_library = Entity(
        model='bookshelf_library.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    chair_library = Entity(
        model='chair_library.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    light_library = Entity(
        model='light_library.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    table_library = Entity(
        model='table_library.glb',
        collider='box',
        shader=basic_lighting_shader
    )
    cabinet_library = Entity(
        model='cabinet_library.glb',
        collider='box',
        shader=basic_lighting_shader
    )