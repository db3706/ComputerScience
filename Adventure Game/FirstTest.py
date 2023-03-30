# Imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Create a ground so the player can move
ground = Entity(model='plane', collider='box', scale=64, texture='grass')

# Create a basic cylinder shape
entity = Entity(model=Cylinder(6, start=-.5), position=Vec3(1,1,1))
entity.x = 0

# Prefabs
player = FirstPersonController()
sky = Sky()

app.run()