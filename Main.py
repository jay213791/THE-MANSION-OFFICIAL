from ursina import *
from ursina.audio import Audio
from ursina import invoke
from ursina.prefabs.first_person_controller import FirstPersonController
from first_floor.ground import ground
from first_floor.wall import wall
from second_floor.floor import floor_second_floor
from second_floor.wall import wall_second_foor
from secret_room.secret_room_floor import secret_room_floor
from secret_room.secret_room_wall import secret_room_wall
from secret_room.secret_room_ceiling import secret_room_ceiling
from basement.basement import basement
from stairs.stairs import stairs
from funiture.first_floor import first_floor_furniture
from funiture.second_floor import second_floor_furniture
from funiture.basement import basement_furniture
from function.obj import create_objects
from function.puzzle import puzzle_functions
from ghost.ghost_assets import create_ghosts
from setting import Setting
from wall_blood_text.wall_blood import image



class Game:
    def __init__(self, prompt): #(self, prompt)
        self.player = None
        self.setting = None
        self.icon_texture = None
        self.prompt = prompt
        self.thunder_sound = Audio('assets/loud-thunder.wav', autoplay=False)
        self.next_thunder_time = 0

    def start(self):
        ground()
        floor_second_floor()
        secret_room_floor()
        wall()
        wall_second_foor()
        secret_room_wall()
        secret_room_ceiling()
        stairs()
        basement()
        first_floor_furniture()
        second_floor_furniture()
        basement_furniture()
        image()
        self.spawn = Vec3(17,2,-2)
        self.spawn_rotation = Vec3(0,-90,0)
        self.player = FirstPersonController(y=2, origin_y=-.5, x = 17, z = -2, rotation = (0,-90,0))
        #EditorCamera()
        self.ghosts = create_ghosts(self.player)
        self.player.speed = 8
        self.player.jump_height = 0  # No vertical movement
        self.player.jump_up_duration = 0
        self.player.input = lambda key: None
        Sky(texture = 'assets/sky.png')
        self.setting = Setting()
        self.held_key = None
        self.held_items = None
        self.crosshair = self.player.cursor
        self.all_doors, self.cube, self.cube1,self.cube2,self.cube3,self.cube4,self.cube5,self.cube6, self.key1, self.key2, self.key3, self.key4, self.item1,  self.paper1, self.paper2, self.paper3, self.paper4, self.paper5, self.paper6,self.paper7,self.paper8,self.paper9, self.drawer1, self.drawer2, self.drawer3, self.drawer4, self.drawer5, self.drawer6, self.drawer7, self.drawer8, self.drawer9, self.picture1, self.picture2, self.picture3, self.picture4= create_objects()
        self.painting_base,self.box_base, self.arm_base1, self.arm_base2, self.secret_cabinet_base1, self.chest_base1, self.chest_base2, self.candle_base1, self.candle_base2, self.candle_base3, self.all_candle_model, self.all_skull_model, self.item2, self.item3, self.item4, self.item5, self.item6, self.item7, self.item8 = puzzle_functions()
        self.next_thunder_time = time.time() + 2

    def respawn(self):
        self.player.position = self.spawn
        self.player.rotation = self.spawn_rotation

    def update(self):

        if time.time() > self.next_thunder_time:
            self.thunder_sound.play()
            self.next_thunder_time = time.time() + 25

        if held_keys['t']:
            self.respawn()

        if not self.setting or self.setting.enabled:
            self.prompt.text = ''
            return

        shown = False

        # --- ITEMS ---
        for item in self.item1 + self.item4 + self.item5 + self.item6 + self.item7 + self.item8:
            horizontal_dist = distance_xz(self.player.position, item.position)
            vertical_dist = abs(self.player.y - item.y)
            if horizontal_dist < 2 and vertical_dist < 2 and not item.picked_up:
                self.prompt.text = "[E] Pick up / [Q] Drop"
                shown = True
                return

        #----- DOORS -----
        for door in self.all_doors:
            horizontal_dist = distance_xz(self.player.position, door.position)
            vertical_dist = abs(self.player.y - door.y)

            if horizontal_dist < 2 and vertical_dist < 2:
               if door.locked:
                   if self.held_key:
                       self.prompt.text = "[E] Unlock door"
                       shown = True
                   else:
                       self.prompt.text = "[Door is locked! Find the key]"
                       shown = True
               else:
                   self.prompt.text = "[E] Open / Close"
                   shown = True
               return

        # ----- DRAWERS -----
        for drawer in self.drawer1 + self.drawer2 + self.drawer3 + self.drawer4  + self.drawer6 + self.drawer7 + self.drawer8:
            horizontal_dist = distance_xz(self.player.position, drawer.position)
            vertical_dist = abs(self.player.y - drawer.y)
            if 1.3 < horizontal_dist < 2 and 0 < vertical_dist < 2:
                self.prompt.text = "[E] Open / Close drawer"
                shown = True
                return

        # ----- PAPERS -----
        for drawer in self.drawer1:
            if drawer.is_open:
                for paper in self.paper3:
                    if distance_xz(self.player.position, paper.position) < 1.5:
                        self.prompt.text = "[E] Read"
                        shown = True
                        return

        for drawer in self.drawer2:
            if drawer.is_open:
                for paper in self.paper4:
                    if distance_xz(self.player.position, paper.position) < 1.5:
                        self.prompt.text = "[E] Read"
                        shown = True
                        return

        for drawer in self.drawer3:
            if drawer.is_open:
                for paper in self.paper2:
                    if distance_xz(self.player.position, paper.position) < 1.5:
                        self.prompt.text = "[E] Read"
                        shown = True
                        return

        for drawer in self.drawer4:
            if drawer.is_open:
                for paper in self.paper1:
                    if distance_xz(self.player.position, paper.position) < 1.5:
                        self.prompt.text = "[E] Read"
                        shown = True
                        return

        for drawer in self.drawer7:
            if drawer.is_open:
                for paper in self.paper5:
                    if distance_xz(self.player.position, paper.position) < 1.5:
                        self.prompt.text = "[E] Read"
                        shown = True
                        return

        for paper in self.paper6:
            horizontal_dist = distance_xz(self.player.position, paper.position)
            vertical_dist = abs(self.player.y - paper.y)
            if horizontal_dist < 1.5 and vertical_dist < 2:
                self.prompt.text = "[E] Read"
                shown = True
                return

        for paper in self.paper7:
            horizontal_dist = distance_xz(self.player.position, paper.position)
            vertical_dist = abs(self.player.y - paper.y)
            if horizontal_dist < 1.5 and vertical_dist < 2:
                self.prompt.text = "[E] Read"
                shown = True
                return

        for paper in self.paper8:
            if distance_xz(self.player.position, paper.position) < 1.5:
                self.prompt.text = "[E] Read"
                shown = True
                return

        for paper in self.paper9:
            if distance_xz(self.player.position, paper.position) < 1.5:
                self.prompt.text = "[E] Read"
                shown = True
                return

        # --- FOR DRAWER SA BASEMENT ---
        for drawer in self.drawer5:
            horizontal_dist = distance_xz(self.player.position, drawer.position)
            vertical_dist = abs(self.player.y - drawer.y)
            if horizontal_dist < 2 and vertical_dist < 2:
                if drawer.locked:
                    if self.held_items:
                        self.prompt.text = "[E] Fix the drawer"
                        shown = True
                    else:
                        self.prompt.text = "[Drawer is broken! Find screw driver to open it]"
                        shown = True
                elif drawer.is_open:
                    for key in self.key1:
                        if distance_xz(self.player.position, key.position) < 1.5:
                            self.prompt.text = "[E] Pick up key / [Q] Drop"
                            shown = True
                            return
                else:
                    self.prompt.text = "[E] Open / Close drawer"
                    shown = True
                return

                # --- FOR DRAWER SA ROOM1 ---
            for drawer in self.drawer6:
                horizontal_dist = distance_xz(self.player.position, drawer.position)
                vertical_dist = abs(self.player.y - drawer.y)
                if horizontal_dist < 2 and vertical_dist < 2:
                    if drawer.is_open:
                        for key in self.key3:
                            if distance_xz(self.player.position, key.position) < 1.5:
                                self.prompt.text = "[E] Pick up key / [Q] Drop"
                                shown = True
                                return
                    else:
                        self.prompt.text = "[E] Open / Close drawer"
                        shown = True
                    return

                # --- FOR DRAWER SA ROOM3 ---
            for drawer in self.drawer8:
                horizontal_dist = distance_xz(self.player.position, drawer.position)
                vertical_dist = abs(self.player.y - drawer.y)
                if horizontal_dist < 2 and vertical_dist < 2:
                    if drawer.is_open:
                        for key in self.key4:
                            if distance_xz(self.player.position, key.position) < 1.5:
                                self.prompt.text = "[E] Pick up "
                                shown = True
                                return
                    else:
                        self.prompt.text = "[E] Open / Close drawer"
                        shown = True
                    return

            for drawer in self.drawer9:
                horizontal_dist = distance_xz(self.player.position, drawer.position)
                vertical_dist = abs(self.player.y - drawer.y)
                if horizontal_dist < 2 and vertical_dist < 2:
                    if drawer.is_open:
                        for picture in self.picture2:
                            if distance_xz(self.player.position, picture.position) < 1.5:
                                self.prompt.text = "[E] Pick up "
                                shown = True
                                return


        # --- ALL THE PICTURES (FAMILY PIC) ---
        for picture in self.picture1 + self.picture3:
            horizontal_dist = distance_xz(self.player.position, picture.position)
            vertical_dist = abs(self.player.y - picture.y)
            if 1 < horizontal_dist < 2 and vertical_dist < 2:
                self.prompt.text = "[E] Pick up"
                shown = True
                return

        # --- PAINTING SA ROOM 2 ---
        for painting in self.painting_base:
            horizontal_dist = distance_xz(self.player.position, painting.position)
            vertical_dist = abs(self.player.y - painting.y)
            if horizontal_dist < 2 and vertical_dist < 2:
                if painting.locked:
                    self.prompt.text = "[E] Enter Passcode"
                    shown = True
                elif painting.is_open:
                    for key in self.key2:
                       if distance_xz(self.player.position, key.position) < 1.5:
                         self.prompt.text = "[E] Pick up key / [Q] Drop"
                         shown = True
                else:
                    self.prompt.text = ""
                    return

        # --- FOR BOX IN SECRET ROOM ---
        for box in self.box_base:
            horizontal_dist = distance_xz(self.player.position, box.position)
            vertical_dist = abs(self.player.y - box.y)
            if horizontal_dist < 2 and vertical_dist < 2:
                if box.locked:
                    self.prompt.text = "[E] Enter Passcode"
                    shown = True
                elif box.is_open:
                    for picture in self.picture4:
                        if distance_xz(self.player.position, picture.position) < 2:
                            self.prompt.text = "[E] Pick up"
                            shown = True
                else:
                    self.prompt.text = ""
                    return

        # --- SECRET ROOM BOOK SHELF PUZZLE
        if self.arm_base1[0].is_open and self.arm_base2[0].is_open:
            for cabinet in self.secret_cabinet_base1:
                if not cabinet.is_open:
                    invoke(cabinet.open, delay = 1.5)

        # --- CANDLE DRAWER PUZZLE OPEN ---
        if self.candle_base1[0].is_open and self.candle_base2[0].is_open and self.candle_base3[0].is_open:
            for drawer in self.drawer9:
                if not drawer.is_open:
                    invoke(drawer.open, delay = 1)

        # --- ARM 1 & 2 FOR BOOKSHELF ---
        for arm1 in self.arm_base1:
            if distance_xz(self.player.position, arm1.position) < 2:
                if arm1.locked:
                    if self.held_items:
                        self.prompt.text = "[E] Place the item"
                        shown = True
                    else:
                        self.prompt.text = "[Find the skull to open the secret door]"
                        shown = True
                else:
                    if not hasattr(arm1, 'complete_shown'):
                        access = Text("COMPLETE", origin = (0, 0), scale = 2)
                        invoke(destroy, access, delay = 0.5)
                        arm1.complete_shown = True
                        return

        for arm2 in self.arm_base2:
            if distance_xz(self.player.position, arm2.position) < 2:
                if arm2.locked:
                    if self.held_items:
                        self.prompt.text = "[E] Place the item"
                        shown = True
                    else:
                        self.prompt.text = "[Find the skull to open the secret door]"
                        shown = True
                else:
                    if not hasattr(arm2, 'complete_shown'):
                        access = Text("COMPLETE", origin=(0, 0), scale=2)
                        invoke(destroy, access, delay=0.5)
                        arm2.complete_shown = True
                        return

        # --- CHEST 1 & 2 PROMPT SA LIVING ROOM AND ROOM 4 ---
        for chest1 in self.chest_base1:
            horizontal_dist = distance_xz(self.player.position, chest1.position)
            vertical_dist = abs(self.player.y - chest1.y)
            if horizontal_dist < 2 and vertical_dist < 2:
                if chest1.locked:
                    if self.held_items:
                        self.prompt.text = "[E] Attach"
                        shown = True
                    else:
                        self.prompt.text = "[It’s missing a gear... maybe it’s around here.]"
                        shown = True
                elif chest1.is_open:
                    for item in self.item2:
                        if distance_xz(self.player.position, item.position) < 1.5:
                            self.prompt.text = "[E] Pick up / [Q] Drop"
                            shown = True
                            return
                else:
                    self.prompt.text = "[E] Open / Close Chest"
                    shown = True
                return

        for chest2 in self.chest_base2:
            horizontal_dist = distance_xz(self.player.position, chest2.position)
            vertical_dist = abs(self.player.y - chest2.y)
            if horizontal_dist < 2 and vertical_dist < 2:
                if chest2.locked:
                    if self.held_items:
                        self.prompt.text = "[E] Attach"
                        shown = True
                    else:
                        self.prompt.text = "[It’s missing a gear... maybe it’s around here.]"
                        shown = True
                elif chest2.is_open:
                    for item in self.item3:
                        if distance_xz(self.player.position, item.position) < 3:
                            self.prompt.text = "[E] Pick up / [Q] Drop"
                            shown = True
                            return
                else:
                    self.prompt.text = "[E] Open / Close Chest"
                    shown = True
                return


        # --- FOR TRIGGER SA MULTO ---
        for cubes in self.cube:
            dist = distance_xz(self.player.position, cubes.position)
            if dist < 2:
                if not hasattr(cubes, 'ghost_triggered'):
                    self.ghosts[0].appear()
                    cubes.ghost_triggered = True
                return

        for cubes in self.cube1:
            dist = distance_xz(self.player.position, cubes.position)
            if dist < 2:
                if not hasattr(cubes, 'ghost_triggered'):
                    self.ghosts[4].appear()
                    cubes.ghost_triggered = True
                return

        for cubes in self.cube2:
            horizontal_dist = distance_xz(self.player.position, cubes.position)
            vertical_dist = abs(self.player.y - cubes.y)
            if horizontal_dist < 2 and vertical_dist < 3:
                if not hasattr(cubes, 'ghost_triggered'):
                    self.ghosts[2].appear()
                    cubes.ghost_triggered = True
                return

        for cubes in self.cube3:
            horizontal_dist = distance_xz(self.player.position, cubes.position)
            vertical_dist = abs(self.player.y - cubes.y)
            if horizontal_dist < 2 and vertical_dist < 3:
                if not hasattr(cubes, 'ghost_triggered'):
                    self.ghosts[6].appear()
                    cubes.ghost_triggered = True
                return

        for cubes in self.cube4:
            horizontal_dist = distance_xz(self.player.position, cubes.position)
            vertical_dist = abs(self.player.y - cubes.y)
            if horizontal_dist < 2 and vertical_dist < 3:
                if not hasattr(cubes, 'ghost_triggered'):
                    self.ghosts[7].appear()
                    cubes.ghost_triggered = True
                return

        for cubes in self.cube5:
            horizontal_dist = distance_xz(self.player.position, cubes.position)
            vertical_dist = abs(self.player.y - cubes.y)
            if horizontal_dist < 2 and vertical_dist < 3:
                if not hasattr(cubes, 'ghost_triggered'):
                    self.ghosts[8].appear()
                    cubes.ghost_triggered = True
                return

        for cubes in self.cube6:
            horizontal_dist = distance_xz(self.player.position, cubes.position)
            vertical_dist = abs(self.player.y - cubes.y)
            if horizontal_dist < 2 and vertical_dist < 3:
                if not hasattr(cubes, 'ghost_triggered'):
                    self.ghosts[9].appear()
                    cubes.ghost_triggered = True
                return


        if not shown:
            self.prompt.text = ''

    def input(self, key):

        if key == 'escape' and self.setting:
            self.setting.toggle()

            is_paused = self.setting.enabled

            self.crosshair.enabled = not is_paused
            mouse.locked = not is_paused
            mouse.visible = is_paused

            if self.icon_texture:
                self.icon_texture.enabled = not is_paused

            return

        if self.setting and self.setting.enabled:
            return

        if key == 'e':
            # ----- KEYS & ITEMS & PICTURE -----
            for items in self.item1:
                horizontal_dist = distance_xz(self.player.position, items.position)
                vertical_dist = abs(self.player.y - items.y)
                if horizontal_dist < 2 and vertical_dist < 2 and not items.picked_up:
                    items.pickup(self.player, icon_texture='doors/key_assets/screw_driver_image.png')
                    self.held_items = items
                    self.icon_texture = items.hud_icon
                    return

            for items3 in self.item4 + self.item5:
                horizontal_dist = distance_xz(self.player.position, items3.position)
                vertical_dist = abs(self.player.y - items3.y)
                if horizontal_dist < 2 and vertical_dist < 2 and not items3.picked_up:
                    items3.pickup(self.player, icon_texture='doors/key_assets/gear_image.png')
                    self.held_items = items3
                    self.icon_texture = items3.hud_icon
                    return

            for items3 in self.item6 + self.item7 + self.item8:
                horizontal_dist = distance_xz(self.player.position, items3.position)
                vertical_dist = abs(self.player.y - items3.y)
                if horizontal_dist < 2 and vertical_dist < 2 and not items3.picked_up:
                    items3.pickup(self.player, icon_texture='doors/key_assets/candle_image.png')
                    self.held_items = items3
                    self.icon_texture = items3.hud_icon
                    return

            for picture in self.picture1:
                horizontal_dist = distance_xz(self.player.position, picture.position)
                vertical_dist = abs(self.player.y - picture.y)
                if horizontal_dist < 1.5 and vertical_dist < 2 and not picture.picked_up:
                    picture.pickup(self.player)
                    self.picture1.remove(picture)
                    return

            for drawer in self.drawer9:
                if drawer.is_open:
                    for picture in self.picture2:
                        horizontal_dist = distance_xz(self.player.position, picture.position)
                        vertical_dist = abs(self.player.y - picture.y)
                        if horizontal_dist < 2 and vertical_dist < 2 and not picture.picked_up:
                            picture.pickup(self.player)
                            self.picture2.remove(picture)
                            return

            for picture in self.picture3:
                horizontal_dist = distance_xz(self.player.position, picture.position)
                vertical_dist = abs(self.player.y - picture.y)
                if horizontal_dist < 1.5 and vertical_dist < 2 and not picture.picked_up:
                    picture.pickup(self.player)
                    self.picture3.remove(picture)
                    return

            # ----- DOORS -----
            for door in self.all_doors:
                horizontal_dist = distance_xz(self.player.position, door.position)
                vertical_dist = abs(self.player.y - door.y)

                if horizontal_dist < 2 and vertical_dist < 2:
                    if door.locked:
                        result = door.try_unlock(self.held_key)
                        if result == "wrong":
                            wrong_text = Text("Wrong key!", origin=(0, 0), scale=2)
                            invoke(destroy, wrong_text, delay=1)
                        elif result is True:
                            self.held_key = None
                    else:
                        door.toggle()
                    return

            # ----- DRAWERS -----
            for drawer in self.drawer1 + self.drawer2 + self.drawer3:
                horizontal_dist = distance_xz(self.player.position, drawer.position)
                vertical_dist = abs(self.player.y - drawer.y)
                if 1.3 < horizontal_dist < 2 and vertical_dist < 2:
                    drawer.toggle()
                    return

            for drawer in self.drawer4 + self.drawer6 + self.drawer7 + self.drawer8:
                horizontal_dist = distance_xz(self.player.position, drawer.position)
                vertical_dist = abs(self.player.y - drawer.y)
                if 1.3 < horizontal_dist < 2 and vertical_dist < 2:
                    drawer.toggle1()
                    return

            # --- DRAWER SA BASEMENT ---
            for drawer in self.drawer5:
                horizontal_dist = distance_xz(self.player.position, drawer.position)
                vertical_dist = abs(self.player.y - drawer.y)
                if 1.3 < horizontal_dist < 2 and vertical_dist < 2:
                    if drawer.locked:
                        result = drawer.try_unlock(self.held_items)
                        if result == "wrong":
                            wrong_text = Text("Wrong Item!", origin=(0, 0), scale=2)
                            invoke(destroy, wrong_text, delay=1)
                        elif result is True:
                            self.held_items= None
                    else:
                        drawer.toggle()
                        if not hasattr(drawer, 'ghost_triggered'):
                            def show_text():
                                behind_you_text = Text("BEHIND YOUUU!", origin=(0, 0), scale=2)
                                invoke(destroy, behind_you_text, delay=1.5)

                            invoke(show_text, delay = 1)
                            invoke(self.ghosts[1].appear, delay=0.2)
                            drawer.ghost_triggered = True
                    return

            # --- CHEST SA LIVING ROOM AND ROOM 4---
            for chest1 in self.chest_base1:
                horizontal_dist = distance_xz(self.player.position, chest1.position)
                vertical_dist = abs(self.player.y - chest1.y)
                if 1.3 < horizontal_dist < 2 and vertical_dist < 2:
                    if chest1.locked:
                        result = chest1.try_unlock(self.held_items)
                        if result == "wrong":
                            wrong_text = Text("Wrong Item!", origin=(0, 0), scale=2)
                            invoke(destroy, wrong_text, delay=1)
                        elif result is True:
                            self.held_items = None
                    else:
                        chest1.toggle()
                        if not hasattr(chest1, 'ghost_triggered'):
                            self.ghosts[5].appear()
                            chest1.ghost_triggered = True
                    return

            for chest2 in self.chest_base2:
                horizontal_dist = distance_xz(self.player.position, chest2.position)
                vertical_dist = abs(self.player.y - chest2.y)
                if 1.3 < horizontal_dist < 2 and vertical_dist < 2:
                    if chest2.locked:
                        result = chest2.try_unlock(self.held_items)
                        if result == "wrong":
                            wrong_text = Text("Wrong Item!", origin=(0, 0), scale=2)
                            invoke(destroy, wrong_text, delay=1)
                        elif result is True:
                            self.held_items = None
                    else:
                        chest2.toggle()
                    return

            # ----- PAPERS -----
            for drawer in self.drawer1:
                if drawer.is_open:
                    for paper in self.paper3:
                        if distance_xz(self.player.position, paper.position) < 1.5:
                            paper.pickup()
                            return

            for drawer in self.drawer2:
                if drawer.is_open:
                    for paper in self.paper4:
                        if distance_xz(self.player.position, paper.position) < 1.5:
                            paper.pickup()
                            return

            for drawer in self.drawer3:
                if drawer.is_open:
                    for paper in self.paper2:
                        if distance_xz(self.player.position, paper.position) < 1.5:
                            paper.pickup()
                            return

            for drawer in self.drawer4:
                if drawer.is_open:
                    for paper in self.paper1:
                        if distance_xz(self.player.position, paper.position) < 1.5:
                            paper.pickup()
                            return

            for drawer in self.drawer7:
                if drawer.is_open:
                    for paper in self.paper5:
                        if distance_xz(self.player.position, paper.position) < 1.5:
                            paper.pickup()
                            return

            for paper in self.paper6:
                horizontal_dist = distance_xz(self.player.position, paper.position)
                vertical_dist = abs(self.player.y - paper.y)
                if horizontal_dist < 1.5 and vertical_dist < 2:
                    paper.pickup()
                    return

            for paper in self.paper7:
                horizontal_dist = distance_xz(self.player.position, paper.position)
                vertical_dist = abs(self.player.y - paper.y)
                if horizontal_dist < 1.5 and vertical_dist < 2:
                    paper.pickup()
                    return

            for paper in self.paper8:
                if distance_xz(self.player.position, paper.position) < 1.5:
                    paper.pickup()
                    return

            for paper in self.paper9:
                if distance_xz(self.player.position, paper.position) < 1.5:
                    paper.pickup()
                    return


            # -- FOR PAINTING VAULT KEY PAD --
            for painting in self.painting_base:
                horizontal_dist = distance_xz(self.player.position, painting.position)
                vertical_dist = abs(self.player.y - painting.y)
                if horizontal_dist < 2 and vertical_dist < 2 and not painting.is_open:
                        painting.open_keypad()
                        return

            # -- FOR KEY INSIDE THE PAINTING VAULT --
            for painting in self.painting_base:
                if painting.is_open:
                    for key in self.key2:
                        horizontal_dist = distance_xz(self.player.position, key.position)
                        vertical_dist = abs(self.player.y - key.y)
                        if horizontal_dist < 2 and vertical_dist < 2 and not key.picked_up:
                            key.pickup(self.player, icon_texture='doors/key_assets/key_picture.png')
                            self.held_key = key
                            return

            # -- FOR BOX KEY PAD --
            for box in self.box_base:
                horizontal_dist = distance_xz(self.player.position, box.position)
                vertical_dist = abs(self.player.y - box.y)
                if horizontal_dist < 2 and vertical_dist < 2 and not box.is_open:
                    box.open_keypad()
                    return


            for box in self.box_base:
                if box.is_open:
                    invoke(self.ghosts[3].appear, delay=0.2)
                    box.ghost_triggered = True
                    for picture in self.picture4:
                        horizontal_dist = distance_xz(self.player.position, picture.position)
                        vertical_dist = abs(self.player.y - picture.y)
                        if horizontal_dist < 2 and vertical_dist < 2 and not picture.picked_up:
                            picture.pickup(self.player)
                            self.picture4.remove(picture)
                            return

            # -- KEYS INSIDE THE DRAWER BASEMENT --
            for drawer in self.drawer5:
                if drawer.is_open:
                    for key in self.key1:
                        horizontal_dist = distance_xz(self.player.position, key.position)
                        vertical_dist = abs(self.player.y - key.y)
                        if horizontal_dist < 2 and vertical_dist < 2 and not key.picked_up:
                            key.pickup(self.player, icon_texture='doors/key_assets/key_picture.png')
                            self.held_key = key
                            return

            for drawer in self.drawer6:
                if drawer.is_open:
                    for key in self.key3:
                        horizontal_dist = distance_xz(self.player.position, key.position)
                        vertical_dist = abs(self.player.y - key.y)
                        if horizontal_dist < 2 and vertical_dist < 2 and not key.picked_up:
                            key.pickup(self.player, icon_texture='doors/key_assets/key_picture.png')
                            self.held_key = key
                            return

            #--- PARA SA PICTURE LOOB NG DRAWER ROOM 3
            for drawer in self.drawer8:
                if drawer.is_open:
                    for key in self.key4:
                        horizontal_dist = distance_xz(self.player.position, key.position)
                        vertical_dist = abs(self.player.y - key.y)
                        if horizontal_dist < 2 and vertical_dist < 2 and not key.picked_up:
                            key.pickup(self.player, icon_texture='doors/key_assets/key_picture.png')
                            self.held_key = key
                            return



            for chest1 in self.chest_base1:
                if chest1.is_open:
                    for item in self.item2:
                        horizontal_dist = distance_xz(self.player.position, item.position)
                        vertical_dist = abs(self.player.y - item.y)
                        if horizontal_dist < 2 and vertical_dist < 2 and not item.picked_up:
                            item.pickup(self.player, icon_texture='doors/key_assets/skull_img.png')
                            self.held_items = item
                            return

            for chest2 in self.chest_base2:
                if chest2.is_open:
                    for item in self.item3:
                        horizontal_dist = distance_xz(self.player.position, item.position)
                        vertical_dist = abs(self.player.y - item.y)
                        if horizontal_dist < 4 and vertical_dist < 4 and not item.picked_up:
                            item.pickup(self.player, icon_texture='doors/key_assets/skull_img.png')
                            self.held_items = item
                            return

            for arm1 in self.arm_base1:
                if distance_xz(self.player.position, arm1.position) < 2:
                    if arm1.locked:
                        result = arm1.try_unlock(self.held_items)
                        if result == "wrong":
                            wrong_text = Text("Wrong item!", origin=(0, 0), scale=2)
                            invoke(destroy, wrong_text, delay=1)
                        elif result is True:
                            arm1.open()
                            self.all_skull_model[0].appear()
                    return

            for arm2 in self.arm_base2:
                if distance_xz(self.player.position, arm2.position) < 2:
                    if arm2.locked:
                        result = arm2.try_unlock(self.held_items)
                        if result == "wrong":
                            wrong_text = Text("Wrong item!", origin=(0, 0), scale=2)
                            invoke(destroy, wrong_text, delay=1)
                        elif result is True:
                            arm2.open()
                            self.all_skull_model[1].appear()
                    return

            for candle1 in self.candle_base1:
                if distance_xz(self.player.position, candle1.position) < 2:
                    if candle1.locked:
                        result = candle1.try_unlock(self.held_items)
                        if result == "wrong":
                            wrong_text = Text("Wrong item!", origin=(0, 0), scale=2)
                            invoke(destroy, wrong_text, delay=1)
                        elif result is True:
                            candle1.open()
                            self.all_candle_model[0].appear()
                    return

            for candle2 in self.candle_base2:
                if distance_xz(self.player.position, candle2.position) < 2:
                    if candle2.locked:
                        result = candle2.try_unlock(self.held_items)
                        if result == "wrong":
                            wrong_text = Text("Wrong item!", origin=(0, 0), scale=2)
                            invoke(destroy, wrong_text, delay=1)
                        elif result is True:
                            candle2.open()
                            self.all_candle_model[1].appear()
                    return

            for candle3 in self.candle_base3:
                if distance_xz(self.player.position, candle3.position) < 2:
                    if candle3.locked:
                        result = candle3.try_unlock(self.held_items)
                        if result == "wrong":
                            wrong_text = Text("Wrong item!", origin=(0, 0), scale=2)
                            invoke(destroy, wrong_text, delay=1)
                        elif result is True:
                            candle3.open()
                            self.all_candle_model[2].appear()
                    return

        if key == 'q':
            if self.held_key:
                self.held_key.drop(self.player)
                self.held_key = None
                return

            if self.held_items:
                self.held_items.drop(self.player)
                self.held_items = None
                return





# DELETE MO PARA MA CONNECT SA MENU


