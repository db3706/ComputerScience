from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

for z in range(10):
    for x in range(10):
        Entity(
            model="cube", color=color.dark_gray, collider="box", ignore=True,
            position = (x, 0, z),
            parent=scene,
            origin_y = 0.5,
            texture = "white_cube"
            )

class TextureBox(Button):
    def __init__(self, position=(5,2,5)):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            origin_y=0.5,
            texture="ursina_logo",
            color=color.color(0,0,1)
            )

        self.texture_choice = 0
        self.textures = ["ursina_logo", "grass", "shore"]

    def input (self, key):
        if self.hovered:
            if key == 'left mouse down':
                self.texture_choice += 1
                self.texture_choice  %= len(self.textures)
                self.texture = self.textures[self.texture_choice]
                chatbox.enable()


chatbox = WindowPanel(title='Hello. I am a red cube')
chatbox.y = chatbox.panel.scale_y / 2 * chatbox.scale_y    # center the window panel

chatbox.disable()

TextureBox()
player = FirstPersonController()
app.run()
