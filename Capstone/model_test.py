from ursina import *
from direct.actor.Actor import Actor


app = Ursina()
application.asset_folder = Path(r'''C:\Users\darry\source\repos\db3706\CS-11\Adventure Game''')

EditorCamera()
actor = Actor('assets/door/scene.gltf')
actor.reparentTo(Entity(scale=2, 
                           rotation=(0,180,0),
                           position=(0,0,0)
                           ))



actor.play("")
print(actor.getAnimNames())
app.run()