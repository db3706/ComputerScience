# Imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.conversation import Conversation

# Define asset path
application.asset_folder = Path(r'''C:\Users\darry\source\repos\db3706\CS-11\Adventure Game''')

app = Ursina()

 # Calls myFunc after 5 seconds
# Map
depths = Entity(model='map/depths.obj', collider='mesh', scale=40, texture='brick')

# Walls
wall1 = Entity(model='cube',
               texture='brick',
               collider='box', 
               position=(0,2,28), 
               scale=(5,6,1), 
               visible=False, 
               texture_scale=(5,5),
               color=color.brown)

wall2 = Entity(model='cube',
               texture='brick',
               collider='box',
               position=(6,2,9), 
               scale=(1,5,7.5), 
               visible=True, 
               texture_scale=(5,5),
               color=color.brown,
               enabled=False)

# Quest Items
quest_cube = Entity(model='assets/cube_companion/scene.gltf', 
                position=(30,0,0),
                collider='box',
                scale=.5,
                enabled=False)

# UI
coins = 0
coins_ui = Text(text = '0', 
             origin = (0, 0), 
             size = 0.05, 
             scale = (1, 1), 
             position = window.top_right - (0.1, 0.1))

# NPCs

# Credits: https://skfb.ly/6XFtT

intro_guy = Entity(model='assets/skeleton_in_a_suit/scene.gltf', 
                   collider='mesh',  
                   scale=0.015, 
                   position=(0,0,30), 
                   rotation=(0,180,0)
                   )

# Credits: https://skfb.ly/6RVpC
cube_guy = Entity(model='assets/homer_simpson_fan_art_sculpt/scene.gltf', 
                 collider='box',
                 scale=.5, 
                 position=(24,1.5,24), 
                 rotation=(0,90,0))


# Credits: https://skfb.ly/6S9tt
explorer = Entity(model='assets/lowpoly_person/scene.gltf',
                  collider='box',
                  scale=0.3, 
                  position=(-16,0,35), 
                  rotation=(0,0,0)
                  )

# Shopkeeper
# Credits: https://skfb.ly/6Sxso
shopkeeper = Entity(model='assets/k-vrc_rigged/scene.gltf',
                  collider='box',
                  scale=0.2, 
                  rotation=(0,90,0),
                  position=(11,0,10)
                  )



shop_stand = Entity(model='assets/saharahs_cart_-_animal_crossing_fanart/scene.gltf',
                  scale=0.03, 
                  rotation=(0,0,0),
                  position=(11,0,7)
                  )
# Coins
coin1 = Entity(model='assets/lowpoly_gold_coin/scene.gltf', 
              color=color.yellow, 
              position=(-4,0,0),
              collider='box')




# Introduction NPC Dialog
intro_variables = Empty(
    mission_solved = 0,
    closed = 0,
)

intro_conversation = Conversation(variables_object=intro_variables, enabled=False)

intro_convo1 = dedent('''
Fodder
Oh, how unfortunate...
    * Where am I?
        Forsaken AND uneducated. I'll enlighten you.
        You have been sent to The Depths, a dense, labyrinth-like region underneath the capital.
        People who fall under the social credit score are sent here to waste away and die.
            * Is there a way out?
                Yes. The only way out is the gate at the end of the hallway behind me.
                And opening it requires a hefty sum of money to prove your worth.
                    * How much are we talking here? (mission_solved += 1)
                        About 50 Gold Coins. There are coins scattered around the labyrinth, dropped from those who failed to escape.
                            * Alright, I best get to it then. 
                                Good luck out there. 
                                    * *leave* (closed += 1)
                                        Fodder

''')
intro_convo2 = dedent('''
Fodder
Good luck out there.
    * *leave* (closed += 1)
        Fodder
''')

# Cube Quest Dialog
cube_variables = Empty(
    mission_solved = 0, 
    closed = 0,
    haggled = 0
)


cube_conversation = Conversation(variables_object=cube_variables, enabled=False)

cube_convo1 = dedent('''
Fodder
Hey you! I need a favour!
    * What is it?
        My precious cube! I accidently dropped it while in a room, which just so happened to be a room full of other cubes!
            * How inconvenient and random is that...
                That doesn't matter! What matters is that you get my cube back!
                    * Alright, where is it and what does it look like? (mission_solved += 1)
                        It's an intricate cube with heart icons on it and you can find it in the room directly to your right.
                            * Alright... I'll go get it for you. (closed += 1)
                                Thanks.
                            * Directly to my right?? If it's so close then why don't you get it yourself?
                                That's besides the point rookie! Now go find it and I'll reward you with 5 gold coins.
                                    * Alright. (closed += 1)
                                        Thanks.
                                    * "5" gold coins? I feel like I should be rewarded with much more, don't you think? (haggled += 1)
                                        You greedy little cow... Fine, 10 gold coins it is...
                                            * That's better... (closed += 1)
                                                Wow

                        
    * Nope, later. (closed += 1)
        Wow
''')

cube_convo2 = dedent('''
Fodder
Come back once you've found my cube. Remember, it's an intricate cube with heart icons on it!
    * *leave* (closed += 1)
        Fodder
''')

cube_convo3 = dedent('''
Fodder
You found it, my precious cube! Thank you, and a deal's a deal. Here's your reward.
    * Thanks. (mission_solved += 1)
        Be careful out there. He's always watching...
            * *leave* (closed += 1)
                Fodder
''')

cube_convo4 = dedent('''
Fodder
Thanks again for your help!
    * *leave* (closed += 1)
        Fodder
''')

# Explorer Quest Dialog
explorer_variables = Empty(
    mission_solved = 0, 
    closed = 0,
    shopkeeper_open = 0
)

explorer_conversation = Conversation(variables_object=explorer_variables, enabled=False)

explorer_convo1 = dedent('''
Fodder
Greetings! I haven't seen you around before. You must be new here. It's unfortunate that the government just sends us here waste away.
    * Agreed.
        Indeed... Despite this, we are given a chance of redeeming ourselves so long as we meet the gold coin requirement, and I think I've found a way to get myself closer to that goal..
            * Go on...
                Some time before you arrived, there was a newcomer, and just like you, he wanted to escape by gathering enough coins to open the gate.
                    * ...
                        Unfortunately, before he managed to gather 50 gold coins, he discovered that he had an illness and only a few months left to live.
                            * ...
                                So, he spent his last remaining months creating a vault to protect his gold coin stash.
                                    * Why didn't he just share it?
                                        Buddy, we're sent down here for a reason... We're sent here due to low social credit, but social credit is mainly lowered due to severe crimes committed on the surface.
                                            * ... 
                                                With that being said, sharing it with random people in this place could potentially bring an irredeemable criminal one step closer to escaping, and I'm guessing that the man who stashed his gold didn't want this.
                                                    * I see...
                                                        But! I can tell that you aren't like those incorrigable criminals considering you haven't threatened me yet. So, I'd like to ask a favour of you. Of course there's a hefty reward.
                                                            * Sure, I'm listening...
                                                                Alright, so unbenkownst to everyone else, I actually found the location of the vault, but opening it is the tricky part.
                                                                    * Let me guess, there's a key...
                                                                        There's a ke-.. Yeah, there is... But, the creator of the vault actually made two keys and scattered them across the labyrinth. I haven't been able to find them, but you, being all adventurous and determined, could definitely find it.
                                                                            * ... (shopkeeper_open += 1)
                                                                                And most importantly, if you manage to unlock the vault, we'll split the money evenly.
                                                                                    * Fair. I best get to it then. (closed += 1)
                                                                                        Good luck out there!
                                                                                    * Cool, but I don't feel like running around on some treasure hunt looking for some keys.
                                                                                        Ah, the lazy type eh? If you're that lazy, an alternative would be using dynamite to blow up the vault door. That would require you to buy it from a shopkeeper.
                                                                                            * Alright, that gives me two options... (mission_solved += 1)
                                                                                                Yep. You can either find the two keys or buy dynamite from a shopkeeper.
                                                                                                    * *leave* (closed += 1)
                                                                                                        Fodder
                                                                
    * *leave* (closed += 1)
        Fodder
''')

explorer_convo2 = dedent('''
Fodder
Remember to tell me once you've successfully found the gold so we can split it evenly!
    * *leave* (close += 1)
        Fodder
''')

# Shopkeeper Dialog
shop_variables = Empty(
    mission_solved = 0, 
    closed = 0,
    enough_money = False
)

shop_conversation = Conversation(variables_object=shop_variables, enabled=False)
shop_convo1 = dedent('''
Fodder
Hello. I am the shopkeeper of this labyrinth. How can I help you?
    * You're a robot?
        Yes. I am a robot commissioned by the government to aid you depth dwellers in your quest for redemption.
            * Ah.
                So, what do you need?
                    * What do you have?
                        I have clothes, blankets, explosives, used toys, and more.
                            * Explosives you say? --I could use it for opening the vault--
                                Yes. I have dynamite which will cost you 15 gold coins.
                                    * *leave* (closed += 1)
                                        Fodder
                                


''')

shop_convo2 = dedent('''
Fodder
You don't have enough money for the dynamite. It costs 15 gold coins.
    * *leave* (closed += 1)
''')

shop_convo3 = dedent('''
Fodder
You have enough money to buy the dynamite. Would you like to spend 15 gold coins?
    * Yes 
        --- Dynamite has been added to your inventory ---
            Thank you and have a nice day.
                * *leave* (closed += 1)
    * No (closed += 1)
        Fodder
''')
# 
def cube_clicked():
    quest_cube.disable()
    cube_variables.mission_solved += 1

quest_cube.on_click = cube_clicked
# Prefabs
player = FirstPersonController(position=(0,5,35), rotation=(0,180,0))
ec = EditorCamera()
ec.enabled = False

# https://github.com/mandaw2014/Sandbox/blob/master/player.py Line 100


   

# Updater
def update():
# Intro NPC
    # Intro dialogue closer
    if intro_variables.closed == 1:
        player.enable()
        intro_conversation.disable()
        wall1.collision = False
        intro_variables.closed -= 1

# Cube NPC
    # cube Quest dialogue closer
    if cube_variables.closed == 1:
        player.enable()
        cube_conversation.disable()
        cube_variables.closed -= 1

    # cube Quest spawn in the cube
    if cube_variables.mission_solved == 1:
        quest_cube.enable()
        cube_variables.mission_solved += 1

    # cube Quest finish and reward
    if cube_variables.mission_solved == 4:
        if cube_variables.haggled == 0:
            global coins
            coins += 5
            coins_ui.text = str(coins)
            cube_variables.haggled -= 1
            cube_variables.mission_solved += 1
        else:
            coins += 10
            coins_ui.text = str(coins)
            cube_variables.haggled += 1
            cube_variables.mission_solved += 1

# Explorer NPC
    # Explorer dialog closer
    if explorer_variables.closed == 1:
        player.enable()
        explorer_conversation.disable()
        intro_variables.closed -= 1

    if coins == 15:
        shop_variables.enough_money = True

# Shopkeeper NPC
    # Shopkeeper dialog closer
    if shop_variables.closed == 1:
        player.enable()
        shop_conversation.disable()
        shop_variables.closed -= 1

# Controls what happens when you click on an NPC
def input(key):
# Introduction NPC
    # Checks if the mouse is hovered over the NPC
    if intro_guy.hovered == True:
        if key == 'left mouse down':
            # If the player hasn't talked to the Intro NPC
            if intro_variables.mission_solved == 0:
                player.disable()
                intro_conversation.enable()
                intro_conversation.start_conversation(intro_convo1)

            # If the player has already talked to the Intro NPC
            if intro_variables.mission_solved == 1:
                player.disable()
                intro_conversation.enable()
                intro_conversation.start_conversation(intro_convo2)
        
# Cube Quest NPC
    if cube_guy.hovered == True:
        if key == 'left mouse down':
            # If the player hasn't talked to the cube NPC
            if cube_variables.mission_solved == 0:
                player.disable()
                cube_conversation.enable()
                cube_conversation.start_conversation(cube_convo1)

            # If the player has already talked to the cube NPC but hasn't found the cube
            if cube_variables.mission_solved == 2:
                player.disable()
                cube_conversation.enable()
                cube_conversation.start_conversation(cube_convo2)

            # If the player finds the cube
            if cube_variables.mission_solved == 3:
                player.disable()
                cube_conversation.enable()
                cube_conversation.start_conversation(cube_convo3)

            # If the player has already finished the quest
            if cube_variables.mission_solved == 5:
                player.disable()
                cube_conversation.enable()
                cube_conversation.start_conversation(cube_convo4)

# Explorer NPC
    if explorer.hovered == True:
        if key =='left mouse down':
            # If the player hasn't talked to the explorer yet
            if explorer_variables.mission_solved == 0:
                player.disable()
                explorer_conversation.enable()
                explorer_conversation.start_conversation(explorer_convo1)

            # If the player hasn't unlocked the vault yet
            if explorer_variables.mission_solved == 1:
                player.disable()
                explorer_conversation.enable()
                explorer_conversation.start_conversation(explorer_convo2)

# Shopkeeper NPC
    if shopkeeper.hovered == True:
        if key =='left mouse down':
            # If the player hasn't talked to the explorer yet
            if shop_variables.mission_solved == 0:
                player.disable()
                shop_conversation.enable()
                shop_conversation.start_conversation(shop_convo1)

# Placeholder coin, will finish in final version
    if coin1.hovered == True:
        if key == 'left mouse down':
            global coins
            coins += 15
            coins_ui.text = str(coins)

    if key == 'tab':    # press tab to toggle edit/play mode
        ec.enabled = not ec.enabled
        player.enabled = not player.enabled


app.run()