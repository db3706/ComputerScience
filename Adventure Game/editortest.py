from ursina import *

app = Ursina(size=(1920,1080))
'''
pixel editor example, it's basically a drawing tool.
can be useful for level editors and such
here we create a new texture, but can also give it an existing texture to modify.
'''
from PIL import Image
t = Texture(Image.new(mode='RGBA', size=(32,32), color=(0,0,0,1)))
from ursina.prefabs.grid_editor import PixelEditor
PixelEditor(texture=load_texture('brick'), x=-.7, scale=.6)

'''
same as the pixel editor, but with text.
'''
from ursina.prefabs.grid_editor import ASCIIEditor
ASCIIEditor(x=0, scale=.1)

app.run()