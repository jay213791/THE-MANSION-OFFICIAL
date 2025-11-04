from ursina import *
from doors.key import Key
from function.classes import Drawer, Painting, Password, Arm, Secret_cabinet, chest, Candle, Candle_show, PasswordBox
from doors.key import Item, Item1, Item2
from doors.Door1 import Doors
from ursina.shaders import basic_lighting_shader

def puzzle_functions():
    # --- PUZZLE PAINTING ---
    painting_base = Password(
        model='cube',
        color=color.clear,
        scale=(1.5, 1, 1),
        position=(10.1, 6, 15),
        origin_x=-0.5,
        password="789012"
    )
    painting_model = Entity(
        parent = painting_base,
        model = 'painting.glb',
        position=(-10.8, -6, -15),
        origin_x=-0.5,
        shader=basic_lighting_shader
    )

    # --- PUZZLE BOX ---
    box_base = PasswordBox(
        position=(84.07, 5.4, -0.7),
        origin_x=-0.5,
        password="7",
    )
    box_model = Entity(
        parent=box_base,
        model='box_front.glb',
        position=(-83.95, -5.4, 0.7),
        shader=basic_lighting_shader
    )

    # --- PUZZLE NUMBER 5 TO ENTER SECRET ROOM ---
    arm_base1 = Arm(
        model='cube',
        color=color.clear,
        scale=(1, 1, 1),
        position=(19, 6.12, 3),
        locked=True
    )
    arm_model1 = Entity(
        model='hand_left.glb',
        shader=basic_lighting_shader
    )
    skull_model1 = Candle_show(
        model= 'skull1.glb'
    )

    arm_base2 = Arm(
        model='cube',
        color=color.clear,
        scale=(1, 1, 1),
        position=(19, 6.12, -4),
        locked=True
    )
    arm_model3 = Entity(
        model='hand_right.glb',
        shader=basic_lighting_shader
    )
    skull_model2 = Candle_show(
        model= 'skull2.glb'
    )

    secret_cabinet_base1 = Secret_cabinet(
        model='cube',
        scale=(1, 1, 1),
        color=color.clear,
        position=(20, 6.18, 1),
        rotation=(0, 90, 0),
        origin_x=0.5,
    )
    secret_cabinet_model1 = Entity(
        parent=secret_cabinet_base1,
        model='second_floor_bookshelf_for_secret_room.glb',
        collider='box',
        position=(1, -6.18, -19.5),
        rotation=(-0, -90, -0),
        origin_x=0.5,
        shader=basic_lighting_shader
    )

    # --- CHEST SA LIVING ROOM ---
    chest_base1 = chest(
        model = 'cube',
        color = color.clear,
        position = (19.5, 0.1, 6),
        origin_y=-0.5,
        locked=True
    )
    chest_model = Entity(
        parent = chest_base1,
        model = 'heaad_chest1.glb',
        origin_y=-0.5,
        position=(-19.5, -0.67, -13.4),
        shader=basic_lighting_shader
    )

    # --- CHEST SA ROOM 4 ---
    chest_base2 = chest(
        model='cube',
        color=color.clear,
        position=(4.7, 3.9, -9.5),
        rotation = (0,180,0),
        origin_y=-0.5,
        locked=True
    )
    chest_model = Entity(
        parent=chest_base2,
        model='head_chest2.glb',
        origin_y=-0.5,
        position=(-4.4, -4.4, 9.7),
        shader=basic_lighting_shader
    )

    # --- CANDLE PUZZLE ---
    candle_base1 = Candle(
        model='cube',
        color=color.clear,
        scale=(1, 1, 1),
        position=(15, 6.12, -9.3),
        locked=True
    )
    candle_model1 = Candle_show(
        model= 'candle.glb',
        position=(15.1, 5.8, -9.35),
        scale = (0.4, 0.4, 0.4)
    )
    cup_model = Entity(
        model = 'candle_cup1.glb'
    )

    candle_base2 = Candle(
        model='cube',
        color=color.clear,
        scale=(1, 1, 1),
        position=(15, 6.12, -15),
        locked=True
    )
    candle_model2 = Candle_show(
        model= 'candle.glb',
        position=(15.1, 5.8, -15.28),
        scale = (0.4, 0.4, 0.4)
    )
    cup_model = Entity(
        model = 'candle_cup2.glb'
    )

    candle_base3 = Candle(
        model='cube',
        color=color.clear,
        scale=(1, 1, 1),
        position=(5, 6.12, -13),
        locked=True
    )
    candle_model3 = Candle_show(
        model= 'candle.glb',
        position=(4.85, 5.75, -12.85),
        scale = (0.4, 0.4, 0.4)
    )
    cup_model = Entity(
        model = 'candle_cup3.glb'
    )

    item2 = Item1(position=(17.4, -0.7, 5.6), scale=(0.8, 0.8 , 0.8), model='skull.glb', item_id="skull1")
    item3 = Item1(position=(2.8, 3.3, -10), scale=(0.8, 0.8 , 0.8), model='skull.glb', item_id="skull2")

    item4 = Item2(position=(11, 0.9, 10.5), scale=(0.12, 0.12 , 0.12), model='rusted_copper_gear.glb', item_id="gear1")
    item5 = Item2(position=(9, 5.2, 1), scale=(0.12, 0.12 , 0.12), model='rusted_copper_gear.glb', item_id="gear2")

    item6 = Item2(position=(4.5, 5.6, 7.1), scale=(0.4, 0.4, 0.4), model='candle.glb', item_id="candle1")
    item7 = Item2(position=(4.85, 5.75, -12.85), scale=(0.4, 0.4, 0.4), model='candle.glb', item_id="candle2")
    item8 = Item2(position=(15.1, 5.8, -9.35), scale=(0.4, 0.4, 0.4), model='candle.glb', item_id="candle3")




    arm_base1.required_item = item2
    arm_base2.required_item = item3

    chest_base1.required_item = item4
    chest_base2.required_item = item5

    candle_base1.required_item = item6
    candle_base2.required_item = item7
    candle_base3.required_item = item8



    return [painting_base], [box_base], [arm_base1], [arm_base2], [secret_cabinet_base1], [chest_base1], [chest_base2], [candle_base1], [candle_base2], [candle_base3], [candle_model1,  candle_model2,  candle_model3], [skull_model1, skull_model2], [item2] , [item3], [item4], [item5], [item6], [item7], [item8]