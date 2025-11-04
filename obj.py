from ursina import *
from doors.Door1 import Doors
from doors.key import Key, Picture, Item
from notes.notes import Items
from function.classes import Drawer
from ursina.shaders import basic_lighting_shader

def create_objects():
    door1 = Doors(
        scale=(1.80, 2.90, 0.1),
        position=(0.10, 1.61, 3.8),
        origin_x=0.5,
        shader=basic_lighting_shader,
    )
    door2 = Doors(
        scale=(1.5, 3.1, 0.1),
        position=(-13.5, 1.61, 6.7),
        rotation=(0, -1, 0),
        origin_x=0.5,
        shader=basic_lighting_shader
    )

    door3 = Doors(
        scale=(1.80, 3.1, 0.1),
        position=(1.6, 5.6, 7.7),
        rotation=(0, -1, 0),
        origin_x=0.5,
        shader=basic_lighting_shader,
        locked=True
    )
    door4 = Doors(
        scale=(1.80, 3.1, 0.1),
        position=(9.65, 5.6, 7.7),
        rotation=(0, -1, 0),
        origin_x=0.5,
        shader=basic_lighting_shader,
        locked = True
    )
    door5 = Doors(
        scale=(1.80, 3.1, 0.1),
        position=(14.6, 5.6, 7.7),
        rotation=(0, -1, 0),
        origin_x=0.5,
        shader=basic_lighting_shader,
        locked = True
    )
    door6 = Doors(
        scale=(1.80, 3.1, 0.1),
        position=(9.2, 5.6, -7.92),
        rotation=(0, -1, 0),
        origin_x=0.5,
        shader=basic_lighting_shader,
        locked = True
    )

    door7 = Doors(
        scale=(1.80, 3.1, 0.1),
        position=(1.75, 5.6, -7.94),
        rotation=(0, -1, 0),
        origin_x=0.5,
        shader=basic_lighting_shader
    )

    key2 = Key(position=(10.8, 5.6, 15.5), scale=(0.0005, 0.0005, 0.0005), color=color.green, model='key.glb', key_id="green_key")

    picture1 = Picture(position=(6.5, 5.2, 13), model='quad', texture='function/hint_assets/puzzel_1.png', scale=0.5, rotation=(90, 90, 0), pics_id='pic_a')
    picture3 = Picture(position=(3.6, 5.18, -11.5), model='quad', texture='function/hint_assets/puzzel_3.png', scale=0.5, rotation=(90, 90, 0), pics_id='pic_c')
    picture4 = Picture(position=(84.4, 5.3, -0.5), model='quad', texture='function/hint_assets/puzzel_4.png', scale=0.5, rotation=(90, 90, 0), pics_id='pic_d')



    door3.required_key = key2

    # --- Drawer sa dining room ---
    drawer_base1 = Drawer(
        model = 'cube',
        color = color.clear,
        scale = (1.2, 1.0, 1),
        position = (15.2, 1.5, -9.5)
    )
    drawer_model1 = Entity(
        parent = drawer_base1,
        model = 'drawer.glb',
        position=(-15.1, -1.5, 9.5),
        shader=basic_lighting_shader
    )
    drawer_base2 = Drawer(
        model = 'cube',
        color = color.clear,
        scale = (1.2, 1.0, 1),
        position = (15.2, 1.5, -15.2)
    )
    drawer_model2 = Entity(
        parent = drawer_base2,
        model = 'drawer1.glb',
        position=(-15.2,-1.5,15.2),
        shader=basic_lighting_shader
    )
    # --- Drawer sa living room ---
    drawer_base3 = Drawer(
        model = 'cube',
        color = color.clear,
        scale = (1, 1.0, 1),
        position = (19.8, 1.5, 13.4)
    )
    drawer_model3 = Entity(
        parent = drawer_base3,
        model = 'drawer2.glb',
        position=(-19.8, -1.5, -13.4),
        shader=basic_lighting_shader
    )
    # --- Drawer sa library room ---
    drawer_base4 = Drawer(
        model='cube',
        color=color.clear,
        scale=(1, 1.0, 0.8),
        position=(-7.9, 1.5, 11.2),
    )
    drawer_model4 = Entity(
        parent=drawer_base4,
        model='drawer3.glb',
        position=(7.9, -1.5, -11.2),
        shader=basic_lighting_shader
    )

    # --- DRAWER SA BASEMENT ---
    drawer_base5 = Drawer(
        model='cube',
        color=color.clear,
        scale=(1, 1.0, 1),
        position=(-8.1,-2.4, 6.3),
        locked=True
    )
    drawer_model5 = Entity(
        parent=drawer_base5,
        model='drawer4.glb',
        position=(8.1,2.4, -6.3),
        shader=basic_lighting_shader
    )

    # -- DRAWER SA SECOND FLOOR ROOM 1 --
    drawer_base6 = Drawer(
        model='cube',
        color=color.clear,
        scale=(1, 1, 1),
        position=(1.55, 5, 14.6),
    )
    drawer_model6 = Entity(
        parent=drawer_base6,
        model='second_floor_room1_drawer.glb',
        position=(-1.55, -5, -14.6),
        shader=basic_lighting_shader
    )

    # -- DRAWER SA SECOND FLOOR ROOM 2 --
    drawer_base7 = Drawer(
        model='cube',
        color=color.clear,
        scale=(1, 1, 1),
        position=(10.5, 5, 14.6),
    )
    drawer_model7 = Entity(
        parent=drawer_base7,
        model='second_floor_room2_drawer.glb',
        position=(-10.5, -5, -14.6),
        shader=basic_lighting_shader
    )

    # -- DRAWER SA SECOND FLOOR ROOM 3 --
    drawer_base8 = Drawer(
        model='cube',
        color=color.clear,
        scale=(1, 1, 1),
        position=(16.5, 5, 15),
    )
    drawer_model8 = Entity(
        parent=drawer_base8,
        model='second_floor_room3_drawer.glb',
        position=(-16.5, -5, -15),
        shader=basic_lighting_shader
    )

    # -- DRAWER SA SECOND FLOOR ROOM 4 --
    drawer_base9 = Drawer(
        model='cube',
        color=color.clear,
        scale=(1, 1, 1),
        position=(15, 5, -9.5),
    )
    drawer_model9 = Entity(
        parent=drawer_base9,
        model='second_floor_room4_drawer.glb',
        position=(-15, -5, 9.5),
        shader=basic_lighting_shader
    )

    item1 = Item(position=(-17, 1.3, -9.5), scale=(2.1, 2.1, 2.1),rotation=(90, 120, 0), model='screw_driver.glb', item_id="screw_driver")

    key1 = Key(parent = drawer_model5, position=(-8.2,-2.52, 6.3), color=color.red, model='key.glb',scale=(0.0005, 0.0005, 0.0005), key_id="drawer5_key")
    key3 = Key(parent = drawer_model6, position=(1.55, 5.07, 14.6), scale=(0.0005, 0.0005, 0.0005), color=color.brown, model='key.glb', key_id="brown_key")
    key4 = Key(parent = drawer_model8, position=(16.5, 5.5, 14.6), scale=(0.0005, 0.0005, 0.0005), color=color.yellow, model='key.glb', key_id="yellow_key")


    picture2 = Picture(parent = drawer_model9, position=(15, 5.4, -9.3), model='quad', texture='function/hint_assets/puzzel_2.png', scale=0.5, rotation=(90, 90, 0), pics_id='pic_b')

    drawer_base5.required_item = item1
    door4.required_key = key1
    door5.required_key = key3
    door6.required_key = key4



    # --- PIPER :P ---

    # -- Library --
    paper1 = Items(
        parent=drawer_model4,
        image_texture='function/hint_assets/90.png',
        model='quad',
        texture='function/hint_assets/90.png',
        scale=(0.7, 0.7),
        rotation=(90, 90, 0),
        position=(-7.9, 1.2, 11.2)
    )

    # -- Living room --
    paper2 = Items(
        parent=drawer_model3,
        image_texture='function/hint_assets/12.png',
        model='quad',
        texture='function/hint_assets/12.png',
        scale=(0.7, 0.7),
        rotation=(90, 90, 0),
        position=(19.8, 1.4, 13)
    )

    # -- Dining room --
    paper3 = Items(
        parent=drawer_model1,
        image_texture='function/hint_assets/hint1.png',
        model='quad',
        texture='function/hint_assets/hint1.png',
        scale=(0.4, 0.4),
        rotation=(90, 90, 0),
        position=(15.2, 1.4, -9.5)
    )
    paper4 = Items(
        parent=drawer_model2,
        image_texture='function/hint_assets/78.png',
        model='quad',
        texture='function/hint_assets/78.png',
        scale=(0.4, 0.4),
        rotation=(90, 90, 0),
        position=(15.2, 1.4, -15.2)
    )
    paper5 = Items(
        parent=drawer_model7,
        image_texture='function/hint_assets/room2_hint.png',
        model='quad',
        texture='function/hint_assets/room2_hint.png',
        scale=(0.4, 0.4),
        rotation=(90, 90, 0),
        position=(10.5, 4.7, 14.6)
    )
    paper6 = Items(
        image_texture='function/hint_assets/skull_hint.png',
        model='quad',
        texture='function/hint_assets/skull_hint.png',
        scale=(0.4, 0.4),
        rotation=(90,180,0),
        position=(12.7, 5.4, -7.4)
    )
    paper7 = Items(
        image_texture='function/hint_assets/candle_hint.png',
        model='quad',
        texture='function/hint_assets/candle_hint.png',
        scale=(0.4, 0.4),
        rotation=(90,90,0),
        position=(11.2, 5.17, -13)
    )
    paper8 = Items(
        image_texture='function/hint_assets/name_hint.png',
        model='quad',
        texture='function/hint_assets/name_hint.png',
        scale=(0.4, 0.4),
        rotation=(90,90,0),
        position=(90.5, 5.38, -0.8)
    )
    paper9 = Items(
        image_texture='function/hint_assets/picture_hint.png',
        model='quad',
        texture='function/hint_assets/picture_hint.png',
        scale=(0.4, 0.4),
        rotation=(90,170,0),
        position=(9, 1.38, -11.8)
    )


    # --- trigger cube sa secret room hallway ---
    cube = Entity(
        model = 'cube',
        scale = (1, 5 , 5),
        position=(35, 5.2, 0),
        color = color.clear
    )
    cube1 = Entity(
        model='cube',
        scale=(1, 5, 10),
        position=(82, 5.2, 0),
        color=color.clear
    )
    cube2 = Entity(
        model = 'cube',
        scale=(1, 4, 10),
        position=(10, 6.6, 11.5),
        rotation=(0, 90, 0),
        color = color.clear
    )
    cube3 = Entity(
        model = 'cube',
        scale=(1, 4, 3),
        position=(9, 6.6, -11.5),
        rotation=(0, 90, 0),
        color = color.clear
    )
    cube4 = Entity(
        model = 'cube',
        scale=(3,2,1),
        position=(15,0.7,-2),
        rotation_y = 90,
        color = color.clear
    )
    cube5 = Entity(
        model = 'cube',
        scale=(3,2,1),
        position=(2, 5.18, -11.5),
        color = color.clear
    )
    cube6 = Entity(
        model = 'cube',
        scale=(3,2,1),
        position=(-5.5,0.7,-2),
        rotation_y = 90,
        color = color.clear
    )




    return [door1, door2, door3, door4, door5, door6, door7],[cube], [cube1],[cube2],[cube3],[cube4],[cube5],[cube6], [key1], [key2], [key3], [key4], [item1], [paper1], [paper2], [paper3], [paper4], [paper5],[paper6],[paper7],[paper8],[paper9], [drawer_base1], [drawer_base2], [drawer_base3], [drawer_base4], [drawer_base5], [drawer_base6], [drawer_base7], [drawer_base8], [drawer_base9], [picture1], [picture2], [picture3], [picture4]