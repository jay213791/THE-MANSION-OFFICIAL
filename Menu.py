from ursina import *
from Instruction import start_instruction
from Main import Game


app = Ursina()
mouse.visible = False


hover_sound = Audio('assets/hover.wav', autoplay=False)
click_sound = Audio('assets/clicked.wav', autoplay=False)
menu_music = Audio('assets/scary-horror-sound-menu.wav', loop=True, autoplay=True)




window.size = ( 1366 ,768 )
window.title = 'The Mansion'
window.borderless = True
window.fullscreen = True

background = Entity(
    model = 'quad',
    texture = 'assets/background.png',
    scale=(window.aspect_ratio * 10, 10),
     z = 1
)
shadow = Text(
    "The \n Mansion",
    scale=4.4,
    position=(0, .2),
    origin=(0,0),
    color=color.black66,
    font='assets/GideonRoman-Regular.ttf'
)
title = Text(
    "The \n Mansion",
    scale = 4,
    position=(0, .2),
    origin=(0, 0),
    color=color.red,
    font = 'assets/GideonRoman-Regular.ttf',
)
Continue = Button(
    text ="Play",
    scale = (.2,0.2),
    position = (0, -.1),
    origin = (0,0),
    color=color.rgba(0, 0, 0, 0),
    text_color = color.white66,
)
Exit = Button(
    text ="Exit",
    scale = (.2,.1),
    position = (0, -.3),
    origin = (0,0),
    color = color.rgba(0,0,0,0),
    text_color = color.white66,
)
cursor = Entity(
    parent = camera.ui,
    model = 'quad',
    texture = 'assets/cursor.png',
    scale = (0.05, 0.05),
    origin = (0.5, 0.5)
)
prompt = Text('', scale=1.5, origin=(0,0), y=-0.4)

Continue.text_entity.scale = 9
Continue.text_entity.z = 1
Continue.text_entity.font = 'assets/GideonRoman-Regular.ttf'

Exit.text_entity.scale = 9
Exit.text_entity.z = 1
Exit.text_entity.font = 'assets/GideonRoman-Regular.ttf'

was_hovered = {
    "continue" : False,
    "exit" : False
}
game_started = False
game = Game(prompt) # VERY IMPORTANT!! cuz it create Game instance here

def update():
    global game_started
    cursor.position = mouse.position

    if Continue.hovered and not was_hovered["continue"]:
        hover_sound.play()
        Continue.text_entity.color = color.red
        was_hovered["continue"] = True
    elif not Continue.hovered:
        Continue.text_entity.color = color.white
        was_hovered["continue"] = False

    if game_started:
        game.update()

    if Exit.hovered and not was_hovered["exit"]:
        hover_sound.play()
        Exit.text_entity.color = color.red
        was_hovered["exit"] = True
    elif not Exit.hovered:
        Exit.text_entity.color = color.white
        was_hovered["exit"] = False


def input(key):
    global game_started
    if key == 'left mouse down':
        if Continue.hovered:
            click_sound.play()
            menu_music.stop()
            invoke(lambda: start_instruction(game, cursor), delay=0.5)
            title.enabled = False
            shadow.enabled = False
            Continue.enabled = False
            Exit.enabled = False
            background.enabled = False
            game_started = True
        elif Exit.hovered:
            click_sound.play()
            invoke(application.quit, delay=0.5)

    # this pass input to game when running so you can add input function sa main py
    if game_started:
        game.input(key)

app.run()