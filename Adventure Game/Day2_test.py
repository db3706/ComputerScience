# Imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

application.asset_folder = Path(r'''C:\Users\darry\source\repos\db3706\CS-11\Adventure Game''')

app = Ursina()

# Create objective status. This will change depending on the player's actions.
objective_status = ["Not started"]

# Create a ground so the player can move
ground = Entity(model='plane', collider='box', scale=100, texture='brick', texture_scale=(10,10))

# Create the walls
wall1 = Entity(model='cube', 
               collider='box', 
               position=(0,0,15), 
               scale=(20,7,1), 
               texture='brick', 
               texture_scale=(5,5),
               color=color.brown)

wall2 = duplicate(wall1, 
                  z=-7, 
                  texture_scale=(5,5))

wall3 = Entity(model='cube', 
               collider='box', 
               position=(-10,0,4), 
               scale=(1,7,21), 
               texture='brick', 
               texture_scale=(5,5),
               color=color.brown)

wall4 = Entity(model='cube', 
               collider='box', 
               position=(10,0,6), 
               scale=(1,7,18), 
               texture='brick', 
               texture_scale=(5,5),
               color=color.brown)


# Create two shapes:

# The jar (objective)
# Credits: https://skfb.ly/6WNQF
jar = Entity(model='assets/jar/scene.gltf', 
                position=(20,.2,10),
                collider='box',
                scale=.15,
                enabled=False)

# The talking NPC (Kirby)
# Credits: https://skfb.ly/6VRDs
kirby = Entity(model='assets/kirby/scene.gltf', 
               position=(-3,1.5,10), 
               rotation=(0,90,0), 
               collider='box', 
               scale =.01,
               texture='assets/kirby/textures/Material_baseColor.png')


# Prefabs
player = FirstPersonController()

# Buttons. Create these as variables so they can be referred to later.
yes_button1 = Button(text='Yes', color=color.azure)
no_button = Button(text='No', color=color.red)
ok_button = Button(text='Okay', color=color.azure)
np_button = Button(text='No problem', color=color.azure)
brb_button = Button(text='Be right back', color=color.azure)

# NPC Dialog Windows
introduction = WindowPanel(
    title='Kirby',
    content=(
        Text('Greetings. Could I ask a favour of you?'),
        yes_button1,
        no_button,
        ),
    position=(0,-.2)
    )

agree = WindowPanel(
    title='Kirby',
    content=(
        Text(text='Great! I just need you to find a jar for me.', scale=.9),
        ok_button,
        ),
    position=(0,-.2)
    )

success = WindowPanel(
    title='Kirby',
    content=(
        Text(text='Fantastic! Thanks for your help!'),
        np_button,
        ),
    position=(0,-.2)
    )

unfinished = WindowPanel(
    title='Kirby',
    content=(
        Text(text='Where is the jar?'),
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
    jar.enable()
    objective_status.remove("Not started")
    objective_status.append("Ongoing")

def objective_finished():
    success.disable()
    player.enable()

def objective_ongoing():
    unfinished.disable()
    player.enable()

def jarclicked():
    objective_status.remove("Ongoing")
    objective_status.append("Finished")
    jar.disable()
    
# Buttons for the UI
no_button.on_click = close_UI
ok_button.on_click = ok_clicked
yes_button1.on_click = yes_clicked
np_button.on_click = objective_finished
brb_button.on_click = objective_ongoing
jar.on_click = jarclicked

# Have the UI disabled by default
introduction.disable()
agree.disable()
success.disable()
unfinished.disable()


# Click detector for Kirby the cube
def input(key):
    # Checks if the mouse is hovered over the cube
    if kirby.hovered == True:
        if key == 'left mouse down':
            # Checks if the player hasn't accepted Kirby's quest yet
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