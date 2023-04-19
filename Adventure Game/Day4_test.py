# Imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Define asset path
application.asset_folder = Path(r'''C:\Users\darry\source\repos\db3706\CS-11\Adventure Game''')

app = Ursina()

# Map
depths = Entity(model='map/depths.obj', collider='mesh', scale=40, texture='brick')

# Walls
wall1 = Entity(model='cube', 
               collider='box', 
               position=(0,2,28), 
               scale=(5,6,1), 
               visible=False, 
               texture_scale=(5,5),
               color=color.brown)


# Quest Items
jar = Entity(model='assets/jar/scene.gltf', 
                position=(30,0,0),
                collider='box',
                scale=.15,
                enabled=False)

# NPCs
# Credits: https://skfb.ly/6XFtT
intro_guy_status = ['Not started']
intro_guy = Entity(model='assets/spongebob_squarepants/scene.gltf', 
                   collider='box',  
                   scale=1, 
                   position=(0,0,30), 
                   rotation=(0,180,0),
                   texture='assets/spongebob_squarepants/textures/spongebob_baseColor.png')

jar_guy_status = ['Not started']
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


def jar_clicked():
    if 'Ongoing' in jar_guy_status:
        jar_guy_status.remove('Ongoing')
        jar_guy_status.append('Finished')
        jar.disable()
    elif 'Bargained' in jar_guy_status:
        jar_guy_status.remove('Bargained')
        jar_guy_status.append('Finished_Bargained')
        jar.disable()

jar.on_click = jar_clicked
# Coins
coin1 = Entity(model='assets/lowpoly_gold_coin/scene.gltf', 
              color=color.yellow, 
              position=(-4,0,0),
              collider='box')


# Buttons
intro_button = Button(text='Where am I?', color=color.azure)
intro_button2 = Button(text='What?', color=color.azure)
intro_button3 = Button(text='...', color=color.azure)
intro_button4 = Button(text='...', color=color.azure)
intro_button5 = Button(text='Is there a way out?', color=color.azure)
intro_button6 = Button(text='...', color=color.azure)
intro_button7 = Button(text='How much money are we talking here?', color=color.azure)
intro_button8 = Button(text='Well, I best get to it then.', color=color.azure)
intro_finished_button = Button(text='Thanks.', color=color.azure)

jarquest_button = Button(text='Sure, what is it?', color=color.azure)
jardecline_button = Button(text='Nope, later',color=color.red)
jarbargain_button = Button(text="5 Gold Coins and I'll do it.", color=color.azure)
jarquest_button2 = Button(text="Alright. I'll be back when I find it.", color=color.azure)
jarquest_close1_button = Button(text="I'll be back when I find it.", color=color.azure)
jarquest_close2_button = Button(text="...", color=color.azure)
jarquest_ongoing_close_button = Button(text="...", color=color.azure)
jarquest_ending1_button = Button(text='No problem!', color=color.azure)
jarquest_ending2_button = Button(text='Thanks, later.', color=color.azure)

# NPC Dialog Windows
#   Introduction
introduction = WindowPanel(
    title='Stranger',
    content=(
        Text('Oh, how unfortunate...'),
        intro_button,
        ),
    position=(0,-.2),
    enabled=False
    )

introduction2 = WindowPanel(
    title='Stranger',
    content=(
        Text("You're in the depths, my friend."),
        intro_button2,
        ),
    position=(0,-.2),
    enabled=False
    )

introduction3 = WindowPanel(
    title='Stranger',
    content=(
        Text("Forsaken AND uneducated. I'll enlighten you."),
        intro_button3,
        ),
    position=(0,-.2),
    enabled=False
    )

introduction4 = WindowPanel(
    title='Stranger',
    content=(
        Text("You have been sent to The Depths, a dense, labyrinth-like region underneath the capital.", wordwrap=30),
        intro_button4,
        ),
    position=(0,-.2),
    enabled=False
    )

introduction5 = WindowPanel(
    title='Stranger',
    content=(
        Text("People who fall under the social credit score are sent here to waste away and die.", wordwrap=30),
        intro_button5,
        ),
    position=(0,-.2),
    enabled=False
    )

introduction6 = WindowPanel(
    title='Stranger',
    content=(
        Text("Yes. The only way out is the gate at the end of the hallway behind me.", wordwrap=30),
        intro_button6,
        ),
    position=(0,-.2),
    enabled=False
    )

introduction7 = WindowPanel(
    title='Stranger',
    content=(
        Text("And opening it requires a hefty sum of money to prove your worth.", wordwrap=30),
        intro_button7,
        ),
    position=(0,-.2),
    enabled=False
    )

introduction8 = WindowPanel(
    title='Stranger',
    content=(
        Text("About 50 Gold Coins. There are coins scattered around the labyrinth, dropped from those who failed to escape.", wordwrap=30),
        intro_button8,
        ),
    position=(0,-.2),
    enabled=False
    )

introduction_finished = WindowPanel(
    title='Stranger',
    content=(
        Text("Good luck out there"),
        intro_finished_button,
        ),
    position=(0,-.2),
    enabled=False
    )

#   Jar Guy
jar_quest = WindowPanel(
    title='Desperate Guy',
    content=(
        Text('Hey you! I need a favor!'),
        jarquest_button,
        jardecline_button
        ),
    position=(0,-.2),
    enabled=False
    )

jar_quest2 = WindowPanel(
    title='Desperate Guy',
    content=(
        Text('My precious jar, I lost it! Could you find it for me?'),
        jarbargain_button,
        jarquest_button2,
        ),
    position=(0,-.2),
    enabled=False
    )

jar_quest_bargain = WindowPanel(
    title='Desperate',
    content=(
        Text("Wow, greedy aren't ya? Alright, deal."),
        jarquest_close1_button
        ),
    position=(0,-.2),
    enabled=False
    )

jar_quest3 = WindowPanel(
    title='Desperate Guy',
    content=(
        Text('Thank you kind sir!'),
        jarquest_close2_button
        ),
    position=(0,-.2),
    enabled=False
    )

jar_quest_ongoing = WindowPanel(
    title='Desperate Guy',
    content=(
        Text("Come back when you've found my jar."),
        jarquest_ongoing_close_button
        ),
    position=(0,-.2),
    enabled=False
    )

jar_quest_ending1 = WindowPanel(
    title='Desperate Guy',
    content=(
        Text(("Thank you sir! I am forever in debt to you!"), 
        wordwrap=30),
        jarquest_ending1_button
        ),
    position=(0,-.2),
    enabled=False
    )

jar_quest_ending2 = WindowPanel(
    title='Desperate Guy',
    content=(
        Text("As promised, here's your 5 Gold."),
        jarquest_ending2_button
        ),
    position=(0,-.2),
    enabled=False
    )

# Functions that define the buttons
def intro():
    introduction.disable()
    introduction2.enable()

def intro2():
    introduction2.disable()
    introduction3.enable()

def intro3():
    introduction3.disable()
    introduction4.enable()

def intro4():
    introduction4.disable()
    introduction5.enable()
    
def intro5():
    introduction5.disable()
    introduction6.enable()

def intro6():
    introduction6.disable()
    introduction7.enable()

def intro7():
    introduction7.disable()
    introduction8.enable()

def intro8():
    introduction8.disable()
    player.enable()
    wall1.collision = False
    intro_guy_status.remove('Not started')
    intro_guy_status.append('Finished')
   
def intro_finished():
    introduction_finished.disable()
    player.enable()


def jar_quest1():
    jar_quest.disable()
    jar_quest2.enable()

def jar_quest_decline():
    jar_quest.disable()
    player.enable()

def jar_quest_haggled():
    jar_quest2.disable()
    jar_quest_bargain.enable()

def jar_quest_haggled_close():
    jar_quest_bargain.disable()
    player.enable()
    jar.enable()
    jar_guy_status.remove('Not started')
    jar_guy_status.append('Bargained')

def jar_quest_close():
    jar_quest2.disable()
    jar_quest3.enable()

def jar_quest_close2():
    jar_quest3.disable()
    player.enable()
    jar.enable()
    jar_guy_status.remove('Not started')
    jar_guy_status.append('Ongoing')

def jar_quest_ongoing_close():
    jar_quest_ongoing.disable()
    player.enable()

def jar_quest_ending1_close():
    jar_quest_ending1.disable()
    player.enable()

def jar_quest_ending2_close():
    jar_quest_ending2.disable()
    player.enable()

# Asign the functions to the buttons
#   Buttons for Introduction dialog
intro_button.on_click = intro
intro_button2.on_click = intro2
intro_button3.on_click = intro3
intro_button4.on_click = intro4
intro_button5.on_click = intro5
intro_button6.on_click = intro6
intro_button7.on_click = intro7
intro_button8.on_click = intro8
intro_finished_button.on_click = intro_finished

#   Buttons for Jar quest dialog
jarquest_button.on_click = jar_quest1
jardecline_button.on_click = jar_quest_decline
jarbargain_button.on_click = jar_quest_haggled
jarquest_button2.on_click = jar_quest_close
jarquest_close1_button.on_click = jar_quest_haggled_close
jarquest_close2_button.on_click = jar_quest_close2
jarquest_ongoing_close_button.on_click = jar_quest_ongoing_close
jarquest_ending1_button.on_click = jar_quest_ending1_close
jarquest_ending2_button.on_click = jar_quest_ending2_close

# Prefabs
player = FirstPersonController(position=(0,5,35), rotation=(0,180,0))
ec = EditorCamera()
ec.enabled = False

# https://github.com/mandaw2014/Sandbox/blob/master/player.py Line 100

# Controls what happens when you click on an NPC
def input(key):
    # Checks if the mouse is hovered over the NPC
    if intro_guy.hovered == True:
        if key == 'left mouse down':
            if 'Not started' in intro_guy_status:
                introduction.enable()
                player.disable()
            elif 'Finished' in intro_guy_status:
                introduction_finished.enable()
                player.disable()

    if jar_guy.hovered == True:
        if key == 'left mouse down':
            if 'Not started' in jar_guy_status:
                jar_quest.enable()
                player.disable()
            elif 'Ongoing' in jar_guy_status:
                jar_quest_ongoing.enable()
                player.disable()
            
            elif 'Bargained' in jar_guy_status:
                jar_quest_ongoing.enable()
                player.disable()
            elif 'Finished' in jar_guy_status:
                jar_quest_ending1.enable()
                player.disable()
            elif 'Finished_Bargained' in jar_guy_status:
                jar_quest_ending2.enable()
                player.disable()
            
    # Placeholder coin, will finish in final version
    if coin1.hovered == True:
        if key == 'left mouse down':
            coin1.disable()

    if key == 'tab':    # press tab to toggle edit/play mode
        ec.enabled = not ec.enabled
        player.enabled = not player.enabled

# Will be the money count in the final version
money = Text(text = "Placeholder", 
             origin = (0, 0), 
             size = 0.05, 
             scale = (1, 1), 
             position = window.top_right - (0.1, 0.1))

app.run()