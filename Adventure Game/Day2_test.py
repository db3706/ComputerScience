# Imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Add footsteps
app = Ursina()

# Create objective status
objective_status = ["Not started"]

# Create a ground so the player can move
ground = Entity(model='plane', collider='box', scale=100, texture='brick', texture_scale=(10,10))

# Create the walls
wall1 = Entity(model='cube', collider='box', position=(0,0,15), scale=(20,7,1), texture='brick', texture_scale=(5,5))
wall2 = duplicate(wall1, z=-7)
wall3 = Entity(model='cube', collider='box', position=(-10,0,4), scale=(1,7,21), texture='brick', texture_scale=(5,5))
wall4 = Entity(model='cube', collider='box', position=(10,0,6), scale=(1,7,18), texture='brick', texture_scale=(5,5))

# Kirby
model = Entity(model='scene.gltf', texture='Material_baseColor.png', posiiton=(0,0,0), collider='mesh')
# Create two basic cube shapes

# The red objective cube
cube1 = Entity(model='cube', 
                position=(20,.5,10),
                collider='box',
                texture='shore', 
                color=color.red,
                scale=.5,
                enabled=False)

# The talking cube NPC
cube2 = Entity(model='cube', 
                position=(-3,1,10), 
                texture='white_cube', 
                color=color.blue,
                collider='box')



# Prefabs
player = FirstPersonController()

# Buttons
yes_button1 = Button(text='Yes', color=color.azure)
no_button = Button(text='No', color=color.red)
ok_button = Button(text='Okay', color=color.azure)
np_button = Button(text='No problem', color=color.azure)
brb_button = Button(text='Be right back', color=color.azure)

# NPC Dialog Windows
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

# Functions that define the buttons
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
    
# Buttons for the UI
no_button.on_click = close_UI
ok_button.on_click = ok_clicked
yes_button1.on_click = yes_clicked
np_button.on_click = objective_finished
brb_button.on_click = objective_ongoing
cube1.on_click = cube1clicked

# Have the UI disabled by default
introduction.disable()
agree.disable()
success.disable()
unfinished.disable()


# Click detector for Herbert the cube
def input(key):
    # Checks if the mouse is hovered over the cube
    if cube2.hovered == True:
        if key == 'left mouse down':
            # Checks if the player hasn't accepted Herbert's quest yet
            if "Not started" in objective_status:
                introduction.enable()
                player.disable()
            # Checks if the player accepted the quest, but hasn't completed it
            elif "Ongoing" in objective_status:
                unfinished.enable()
                player.disable()
            # Checks if the player has successfully found the cube
            elif "Finished" in objective_status:
                success.enable()
                player.disable()

app.run()