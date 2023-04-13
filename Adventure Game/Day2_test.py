# Imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Add footsteps
app = Ursina()

# Create objective status
objective_status = ["Not started"]

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

cube2 = Entity(model='cube', 
                position=(-3,1,10), 
                texture='white_cube', 
                color=color.blue,
                collider='box')



# Prefabs
player = FirstPersonController()
Sky()

# Buttons
yes_button1 = Button(text='Yes', color=color.azure)
no_button = Button(text='No', color=color.red)
ok_button = Button(text='Okay', color=color.azure)
np_button = Button(text='No problem', color=color.azure)
<<<<<<< HEAD


=======
brb_button = Button(text='Be right back', color=color.azure)

# NPC Dialog Windows
>>>>>>> 72f9d43cb36c7e304763957eb302d3ac5529c8bf
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

unfinished = WindowPanel(
    title='Herbert',
    content=(
        Text(text='Where is the cube?'),
        brb_button,
        ),
    position=(0,-.2)
    )

# Functions
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
    objective_status.remove("Not started")
    objective_status.append("Ongoing")

def objective_finished():
    success.disable()
    player.enable()

def objective_ongoing():
    unfinished.disable()
    player.enable()

def cube1clicked():
    objective_status.remove("Ongoing")
    objective_status.append("Finished")
    cube1.disable()
    
# Buttons
no_button.on_click = close_UI
ok_button.on_click = ok_clicked
yes_button1.on_click = yes_clicked
np_button.on_click = objective_finished
<<<<<<< HEAD
=======
brb_button.on_click = objective_ongoing
cube1.on_click = cube1clicked
>>>>>>> 72f9d43cb36c7e304763957eb302d3ac5529c8bf

# Have the UI disabled by default
introduction.disable()
agree.disable()
success.disable()
unfinished.disable()


# Click detector for Herbert the cube
def input(key):
    if cube2.hovered == True:
        if key == 'left mouse down':
            if "Not started" in objective_status:
                introduction.enable()
                player.disable()

            elif "Ongoing" in objective_status:
                unfinished.enable()
                player.disable()

            elif "Finished" in objective_status:
                success.enable()
                player.disable()

app.run()