# Imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Create a ground so the player can move
ground = Entity(model='plane', collider='box', scale=64, texture='grass')

# Create two basic cube shapes
cube1 = Entity(model='cube', 
                position=(3,1,10), 
                texture='white_cube', 
                color=color.red)

cube2 = Entity(model='cube', 
                position=(-3,1,10), 
                texture='white_cube', 
                color=color.blue)

# Prefabs
player = FirstPersonController()
sky = Sky()


# Testing the UI capabilities of Ursina
chatbox = WindowPanel(title='Hello. Testing.')

# Have the UI disabled by default
chatbox.disable()

def input(key):
    # When T is pressed, show the UI
    if key == 't':
        chatbox.enable()
    # When F is pressed, close the UI
    elif key == 'f':
        chatbox.disable()

app.run()
