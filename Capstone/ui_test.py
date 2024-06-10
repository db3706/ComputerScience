'''
clicker game
make a gold counter
make a button
you earn gold for every click
when you have enough gold you can unlock new nodes to automatically generate gold!
'''



from ursina import *

app = Ursina()
window.color = color._20

gold = 0
counter = Text(text='0', y=.25, z=-1, scale=2, origin=(0,0), background=True)
button = Button(text='+', color=color.azure, scale= .125)

def button_click():
    global gold
    gold += 1
    counter.text = str(gold)

button.on_click = button_click



app.run()