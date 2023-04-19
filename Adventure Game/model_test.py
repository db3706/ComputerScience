from ursina import *


app = Ursina()
application.asset_folder = Path(r'''C:\Users\darry\source\repos\db3706\CS-11\Adventure Game''')

EditorCamera()

plane = Entity(model='plane', scale=10, color=color.gray)
model = Entity(model='assets/pamtri_spongebob/scene.gltf', 
               y=1, 
               scale=0.1)






app.run()