# Imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Create a ground so the player can move
ground = Entity(model='plane', collider='box', scale=64, texture='grass')

# Create a basic cylinder shape
entity = Entity(model='cube', 
                position=(1,1,10), 
                texture='white_cube', 
                color=color.yellow)

# Prefabs
player = FirstPersonController()
sky = Sky()

app.run()
