# Imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.conversation import Conversation

# Define asset path
application.asset_folder = Path(r'''C:\Users\darry\source\repos\db3706\CS-11\Adventure Game''')

app = Ursina()

 # Calls myFunc after 5 seconds
# Map
depths = Entity(model='map/depths.obj', collider='mesh', scale=40, texture='brick', positon=(0,0,0))

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
               enabled=True)

wall3 = Entity(model='cube',
               texture='brick',
               collider='box',
               position=(-40,2.5,-9), 
               scale=(1,5,14), 
               texture_scale=(5,5)
               )

# Vault models
vault_door = Entity(model='cube',
               texture='brick',
               collider='box',
               position=(-31,2.5,-9), 
               scale=(1,5,4), 
               visible=True, 
               texture_scale=(5,5),
               color=color.dark_gray,
               enabled=True)

debris = Entity(model='assets/stone_debris/scene.gltf',
               position=(-30,0,-9), 
               scale=0.005,
               texture='brick',
               color=color.dark_gray,
               visible=False
               )

# Gate
gate1 = Entity(model='cube',
               texture='brick',
               collider='box',
               position=(2.5,2.5,-40), 
               scale=(5,5,1), 
               texture_scale=(5,5),
               color=color.gold
               )

gate2 = Entity(model='cube',
               texture='brick',
               collider='box',
               position=(-2.5,2.5,-40), 
               scale=(5,5,1), 
               texture_scale=(5,5),
               color=color.gold
               )

# Area beyond the gate
ground = Entity(model='cube',
               texture='brick',
               collider='box',
               position=(0,-.5,-45), 
               scale=(10,1,10), 
               texture_scale=(5,5)
               )


# The two quest keys and their functions
# Credits: https://skfb.ly/6WP69

key1 = Entity(model='assets/old_gold_key/scene.gltf',
              position=(0,.1,0),
              scale=.1,
              collider='box',
              enabled=True)

key2 = Entity(model='assets/old_gold_key/scene.gltf',
              position=(5,.1,0),
              scale=.1,
              collider='box',
              enabled=True)

key_variables = Empty(
    all_keys_found = 0, # 0 = 0 found, 1 = 1 found, 2 = both keys have been found
    closed = 0
)
key_popup = Conversation(variables_object=key_variables, enabled=False)

key_dialog = dedent('''
Fodder
--- Key found ---
    * *Pick up* (all_keys_found += 1)
        --- Key added to inventory ---
            * *leave* (closed += 1)
                Fodder
''')

# Quest Items

#   Cube
quest_cube = Entity(model='assets/cube_companion/scene.gltf', 
                position=(30,1,0),
                collider='box',
                scale=.5,
                enabled=False)


#   Treasure Chest
treasure_chest = Entity(model='assets/treasure_chest_model/scene.gltf',
                        position=(-38,0,-9), 
                        scale=.2,
                        collider='mesh',
                        rotation=(0,-90,0)
                        )

#   Treasure chest dialog
chest_variables = Empty(
    closed = 0
)

chest_popup = Conversation(variables_object=chest_variables, enabled=False)

chest_dialog = dedent('''
Fodder
Wow, that's a lot of gold coins... I count about 40...
    If I don't tell the explorer and keep the money for myself, I'll have the full amount...
        Or, I could tell the explorer and split the money evenly and I'll end up with 20 gold coins.
            * *leave* (closed += 1)
                Fodder
''')

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


# Credits: https://skfb.ly/ooJLu
explorer = Entity(model='assets/grog_the_adventurer/scene.gltf',
                  collider='box',
                  scale=6, 
                  position=(-16,0,35), 
                  rotation=(0,0,0)
                  )


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

# Credits: https://skfb.ly/6QV9t
gatekeeper = Entity(model='assets/npc_character/scene.gltf',
                  collider='box',
                  scale=0.02, 
                  rotation=(0,180,0),
                  position=(0,0,-38)
                  )





# Coins
coin1 = Entity(model='assets/lowpoly_gold_coin/scene.gltf', 
              color=color.yellow, 
              position=(-4,0,0),
              collider='box')

coin2 = Entity(model='assets/lowpoly_gold_coin/scene.gltf', 
              color=color.yellow, 
              position=(17,0,-13),
              collider='box')

coin3 = Entity(model='assets/lowpoly_gold_coin/scene.gltf', 
              color=color.yellow, 
              position=(-8,0,-22),
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
                Yes. The only way out is the yellow gate at the end of the hallway behind me.
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
    haggled = 0,

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
    shopkeeper_open = 0,
    key_route = 0
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
                                                                    * Let me guess, there's a key... (mission_solved += 1)
                                                                        There's a ke-.. Yeah, there is... But, the creator of the vault actually made two keys and scattered them across the labyrinth. I haven't been able to find them, but you, being all adventurous and determined, could definitely find it.
                                                                            And also, if you're the lazy type, you can also buy dynamite as an alternative to opening that vault.
                                                                                So, the choice is yours. Do you want to find the two keys or buy dynamite for opening the vault?
                                                                                    * I'll buy dynamite. (shopkeeper_open += 1)
                                                                                        Alright. You'll have to buy it from the shopkeeper robot. He's pretty easy to spot as he's painted red and accompanied with a merchant cart.
                                                                                            * *leave* (closed += 1)
                                                                                                Fodder
                                                                                    * I'll find the two keys. (key_route += 1)
                                                                                        Alright. Good luck on finding them...
                                                                                            * *leave* (closed += 1)
                                                                                                Fodder
                                                                                        
                                                                
    * *leave* (closed += 1)
        Fodder
''')

explorer_convo2 = dedent('''
Fodder
Remember to tell me once you've successfully found the gold so we can split it evenly!
    * *leave* (closed += 1)
        Fodder
''')

# Shopkeeper Dialog
shop_variables = Empty(
    mission_solved = 0, # 0 = not started, 1 = ongoing, 
    closed = 0,
    enough_money = 0,
    dynamite_obtained = 0
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
                            * Explosives you say? --I could use it for opening the vault-- (mission_solved += 1)
                                Yes. I have dynamite which will cost you 15 gold coins.
                                    * *leave* (closed += 1)
                                        Fodder
                                
''')

shop_convo2 = dedent('''
Fodder
You don't have enough money for the dynamite. Come back once you have 15 gold coins.
    * *leave* (closed += 1)
        Fodder
''')

shop_convo3 = dedent('''
Fodder
You have enough money to buy the dynamite. Would you like to spend 15 gold coins?
    * Yes (dynamite_obtained += 1)
        --- Dynamite has been added to your inventory --- 
            * Thanks Mr. Robot. (mission_solved += 1)
                Stay safe out there.
                    * *leave* (closed += 1)
                        Fodder
    * No (closed += 1)
        Fodder
''')

shop_convo4 = dedent('''
Fodder
Good luck out there...
    * *leave* (closed += 1)
        Fodder
''')
# 
gate_variables = Empty(
    mission_solved = 0, # 0 = not started, 1 = ongoing, 2 = enough money to open gate
    closed = 0,
)


gate_conversation = Conversation(variables_object=gate_variables, enabled=False)
gate_convo1 = dedent('''
Fodder
...
    * Who are you?
        I'm the gatekeeper. My job is to guard the gate against those who have not gathered enough coins.
            * ... (mission_solved += 1)
                I'm also the only one capable of opening and closing this gate.
                    If on the slim chance you manage to gather 50 coins, talk to me and I'll open the gate for you.
                        * *leave* (closed += 1)
                            Fodder
''')

gate_convo2 = dedent('''
Fodder
Talk to me once you've gathered 50 coins and I'll open the gate for you.
    * *leave* (closed += 1)
        Fodder
''')
gate_convo3 = dedent('''
Fodder
...
    * I have enough money.
        It seems you do. Congratulations, it's been a while since someone's accomplished this feat.
            * ...
                As promised, I'll open the gate now...
                    * Finally...
                        Good luck...
                            * *leave* (closed += 1)
                                Fodder
''')

# Cube functions
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
    global coins
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
        explorer_variables.closed -= 1

    # If the player opens the option to get dynamite
    if explorer_variables.shopkeeper_open == 1:
        wall2.disable()
        explorer_variables.shopkeeper_open -= 1

    # If the player chooses to find the keys
    if explorer_variables.key_route == 1:
        key1.enable()
        key2.enable()
# Vault key popup closer
    if key_variables.closed == 1:
        player.enable()
        key_popup.disable()
        key_variables.closed -= 1

# Treasure chest popup closer
    if chest_variables.closed == 1:
        player.enable()
        chest_popup.disable()
        coins += 50
        coins_ui.text = str(coins)
        chest_variables.closed -= 1
        treasure_chest.disable()

# Shopkeeper NPC
    # Shopkeeper dialog closer
    if shop_variables.closed == 1:
        player.enable()
        shop_conversation.disable()
        shop_variables.closed -= 1

    # Subtracts 15 coins from player wallet after buying dynamite
    if shop_variables.dynamite_obtained == 1:
        coins -= 15
        coins_ui.text = str(coins)
        shop_variables.dynamite_obtained += 1 


# Gatekeeper NPC
    # Gatekeeper dialog closer
    if gate_variables.closed == 1:
        player.enable()
        gate_conversation.disable()
        gate_variables.closed -= 1
# Blackout and explosion variables
black_screen = Button(color=color.dark_gray, scale=100, enabled=False)
explosion_audio = Audio('sounds/Explosion.mp3', loop=False, autoplay=False, volume=0.5)

# Other audio
coin_audio = Audio('sounds/Mario Coin Sound.mp3', loop=False, autoplay=False, volume=0.5)


def explosion():
    explosion_audio.play()
    vault_door.disable()

def vault_destroyed():
    debris.visible = True
    black_screen.disable()

def vault_explosion():
    black_screen.enable()
    invoke(explosion, delay=1)
    invoke(vault_destroyed, delay=4)


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
        global coins
        if key == 'left mouse down':
            # If the player hasn't talked to the shopkeeper yet
            if shop_variables.mission_solved == 0:
                player.disable()
                shop_conversation.enable()
                shop_conversation.start_conversation(shop_convo1)
            
            # If the player has already talked to the shopkeeper
            if shop_variables.mission_solved == 1:

                # If the player returns but doesn't have enough money
                if coins < 15:
                    player.disable()
                    shop_conversation.enable()
                    shop_conversation.start_conversation(shop_convo2)

                # If the player returns and has enough money
                if coins >= 15:
                    player.disable()
                    shop_conversation.enable()
                    shop_conversation.start_conversation(shop_convo3)

                # If the player has already bought dynamite
            if shop_variables.mission_solved == 2:
                player.disable()
                shop_conversation.enable()
                shop_conversation.start_conversation(shop_convo4)

# Gatekeeper NPC
    if gatekeeper.hovered == True:
        if key =='left mouse down':
            # If the player hasn't talked to the gatekeeper yet
            if gate_variables.mission_solved == 0:
                player.disable()
                gate_conversation.enable()
                gate_conversation.start_conversation(gate_convo1)

            # If the player has gathered enough money
            if gate_variables.mission_solved == 1:
                if coins >= 50:
                    player.disable()

# Vault Door

    if vault_door.hovered == True:
        if key == 'left mouse down':
            if shop_variables.dynamite_obtained == 3:
                vault_explosion()

            if key_variables.all_keys_found == 2:
                vault_door.animate_position(vault_door.position+(vault_door.down)*2, duration=5, curve=curve.linear)

# Treasure chest
    if treasure_chest.hovered == True:
        if key == 'left mouse down':
                player.disable()
                chest_popup.enable()
                chest_popup.start_conversation(chest_dialog)

# Coin
    if coin1.hovered == True:
        if key == 'left mouse down':
            coin_audio.play()
            coins += 15
            coins_ui.text = str(coins)
            coin1.disable()


    if coin2.hovered == True:
        if key == 'left mouse down':
            coin_audio.play()          
            coins += 1
            coins_ui.text = str(coins)
            coin2.disable()


    if coin3.hovered == True:
        if key == 'left mouse down':
            coin_audio.play()            
            coins += 1
            coins_ui.text = str(coins)
            coin3.disable()

# Vault Keys
    if key1.hovered == True:
        if key == 'left mouse down':
            player.disable()
            key_popup.enable()
            key_popup.start_conversation(key_dialog)
            key1.disable()

    if key2.hovered == True:
        if key == 'left mouse down':
            player.disable()
            key_popup.enable()
            key_popup.start_conversation(key_dialog)
            key2.disable()

    if key == 'tab':    # press tab to toggle edit/play mode
        ec.enabled = not ec.enabled
        player.enabled = not player.enabled


app.run()