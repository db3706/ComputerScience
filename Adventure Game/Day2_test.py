# Imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

#
finished = ["False"]
app = Ursina()

# Create a ground so the player can move
ground = Entity(model='plane', collider='box', scale=64, texture='grass',)

# Create two basic cube shapes
cube1 = Entity(model='cube', 
                position=(6,.5,10),
                collider='box',
                texture='shore', 
                color=color.red,
                scale=.5,
                enabled=False)

def cube1clicked():
    finished.remove("False")
    finished.append("True")
    cube1.disable()

cube1.on_click = cube1clicked

cube2 = Entity(model='cube', 
                position=(-3,1,10), 
                texture='white_cube', 
                color=color.blue,
                collider='box')

# Prefabs
player = FirstPersonController()
Sky()


yes_button1 = Button(text='Yes', color=color.azure)
no_button = Button(text='No', color=color.red)
ok_button = Button(text='Okay', color=color.azure)
np_button = Button(text='No problem', color=color.azure)


introduction = WindowPanel(
    title='Herbert',
    content=(
        Text('Greetings. Could I ask a favour of you?'),
        yes_button1,
        no_button,
        ),
    position=(0,-.2)
    )

agree = WindowPanel(
    title='Herbert',
    content=(
        Text(text='Great! I just need you to find a red cube for me.', scale=.9),
        ok_button,
        ),
    position=(0,-.2)
    )

success = WindowPanel(
    title='Herbert',
    content=(
        Text(text='Fantastic! Thanks for your help!'),
        np_button,
        ),
    position=(0,-.2)
    )




def close_UI():
    introduction.disable()
    player.enable()

def yes_clicked():
    introduction.disable()
    agree.enable()

def ok_clicked():
    agree.disable()
    player.enable()
    cube1.enable()

def objective_finished():
    success.disable()
    player.enable()

no_button.on_click = close_UI
ok_button.on_click = ok_clicked
yes_button1.on_click = yes_clicked
np_button.on_click = objective_finished

# Have the UI disabled by default
introduction.disable()
agree.disable()
success.disable()


def input(key):
    if cube2.hovered == True:
        if key == 'left mouse down':
            if "False" in finished:
                introduction.enable()
                player.disable()
            elif "True" in finished:
                success.enable()
                player.disable()

app.run()