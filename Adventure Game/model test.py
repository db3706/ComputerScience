# Imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Define asset path
application.asset_folder = Path(r'''C:\Users\darry\source\repos\db3706\CS-11\Adventure Game''')

player_money = ['0']
app = Ursina()

# Map
depths = Entity(model='map/depths.obj', collider='mesh', scale=40, texture='brick')


# NPCs
intro_guy = Entity(model='assets/lowpoly_person/scene.gltf', 
                   collider='box', 
                   color=color.azure, 
                   scale=.3, 
                   position=(0,0,30), 
                   rotation=(0,180,0))

jar_guy = Entity(model='assets/lowpoly_person/scene.gltf', 
                 collider='box', 
                 color=color.red, 
                 scale=.3, 
                 position=(24,0,24), 
                 rotation=(0,90,0))

explorer = Entity(model='assets/lowpoly_person/scene.gltf', 
                 collider='box', 
                 color=color.yellow, 
                 scale=.3, 
                 position=(-16,0,35), 
                 rotation=(0,0,0))



# Prefabs
player = FirstPersonController(position=(0,0,35), rotation=(0,180,0))
ec = EditorCamera()
ec.enabled = False

# https://github.com/mandaw2014/Sandbox/blob/master/player.py Line 100
money = Text(text = str(player_money), origin = (0, 0), size = 0.05, scale = (1, 1), position = window.top_right - (0.1, 0.1))



def input(key):
    if key == 'tab':    # press tab to toggle edit/play mode
        ec.enabled = not ec.enabled
        player.enabled = not player.enabled






app.run()