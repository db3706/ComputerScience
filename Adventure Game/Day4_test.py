# Imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.conversation import Conversation

# Define asset path
application.asset_folder = Path(r'''C:\Users\darry\source\repos\db3706\CS-11\Adventure Game''')

app = Ursina()

window.fps_counter.enabled = False

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
               color=color.red,
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
               position=(0,-.5,-55), 
               scale=(10,1,30), 
               texture_scale=(5,5)
               )

wall4 = Entity(model='cube',
               texture='brick',
               collider='box',
               position=(5,2,-55), 
               scale=(1,5,30), 
               texture_scale=(5,5)
               )
wall5 = Entity(model='cube',
               texture='brick',
               collider='box',
               position=(-5,2,-55), 
               scale=(1,5,30), 
               texture_scale=(5,5)
               )

# Treasure chest dialog
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


# The two quest keys and their functions
# Credits: https://skfb.ly/6WP69

key1 = Entity(model='assets/old_gold_key/scene.gltf',
              position=(-8,.1,0),
              scale=.1,
              collider='box',
              enabled=True)

key2 = Entity(model='assets/old_gold_key/scene.gltf',
              position=(16,.1,0),
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

# Cube item dialog
cube_item_variables = Empty(
    closed = 0
)

cube_item_popup = Conversation(variables_object=cube_item_variables, enabled=False)

cube_item_dialog = dedent('''
--- Cube added to inventory ---
    * *leave* (closed += 1)
        Fodder
''')

# Credits: https://skfb.ly/6WOHL
treasure_chest = Entity(model='assets/treasure_chest/scene.gltf',
                        position=(-38,0,-9), 
                        scale=0.01,
                        collider='mesh',
                        rotation=(0,0,0)
                        )

# UI
coins = 0
coins_ui = Text(text = '0', 
             origin = (0, 0), 
             size = 0.05, 
             scale = (1, 1), 
             position = window.top_right - (0.1, 0.1))
money_ui = Text(text = 'Coins:', 
             origin = (0, 0), 
             size = 0.05, 
             scale = (1, 1), 
             position = window.top_right - (0.2, 0.1))
# NPCs

# Credits: https://skfb.ly/6Y8Jr

intro_guy = Entity(model='assets/skeleton_in_a_suit/scene.gltf', 
                   collider='mesh',  
                   scale=0.015, 
                   position=(0,0,30), 
                   rotation=(0,180,0)
                   )

overseer = Entity(model='assets/skeleton_in_a_suit/scene.gltf', 
                   collider='mesh',  
                   scale=0.015, 
                   position=(0,0,-50), 
                   rotation=(0,180,0)
                   )

# Credits: https://skfb.ly/6RVpC
cube_guy = Entity(model='assets/homer_simpson_fan_art_sculpt/scene.gltf', 
                 collider='box',
                 scale=.5, 
                 position=(26,1.5,24), 
                 rotation=(0,90,0))


# Credits: https://skfb.ly/6QTTA
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



def intro_disappear():
    intro_guy.disable()

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

coin4 = Entity(model='assets/lowpoly_gold_coin/scene.gltf', 
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

# When you meet the intro NPC (revealed to be the Overseer) after opening the gate
overseer_variables = Empty(
    closed_good = 0,
    closed_bad = 0
)

overseer_conversation = Conversation(variables_object=overseer_variables, enabled=False)

overseer_convo1 = dedent('''
Fodder
Hello again...
    * Aren't you the guy from the start?
        Yes, I am. But, I'm not just some "guy". I'm the Overseer of The Depths.
            * What?
                I'm tasked with monitoring every depth dweller who attempts to leave this place.
                    * Why?
                        Why, you ask? After we first met, you assumed that gathering 50 gold coins was the ONLY condition for leaving this place.
                        However, anyone can accomplish this, and there's a high chance that letting out the wrong person could cause harm to the citizens.
                        So, we decided to monitor you depth dwellers, not only to see you gather 50 coins, but to also see your character, especially how you treat others.
                        For example, if someone were to gather 50 gold coins, but they consistently harmed others during their stay in The Depths,
                        then I will deny access to the exit as they will cause harm to others outside of The Depths.
                        With that being said, I watched you treat others with respect and kindess, for the most part.
                        You helped that old man retrieve his cube and you kept your word by splitting the treasure with the explorer.
                        So, I permit you to leave this labyrinth and have a second chance at living your life out in the world.
                            * Guess it was a good choice to split that money...
                                Indeed. Congratulations and have a nice life out there...
                                    * --- finish the game --- (closed_good += 1)
                                        Fodder
''')
overseer_convo2 = dedent('''
Fodder
Hello again...
    * Aren't you the guy from the start?
        Yes, I am. But, I'm not just some "guy". I'm the Overseer of The Depths.
            * What?
                I'm tasked with monitoring every depth dweller who attempts to leave this place.
                    * Why?
                        Why, you ask? After we first met, you assumed that gathering 50 gold coins was the ONLY condition for leaving this place.
                        However, anyone can accomplish this, and there's a high chance that letting out the wrong person could cause harm to the citizens.
                        So, we decided to monitor you depth dwellers, not only to see you gather 50 coins, but to also see your character, especially how you treat others.
                        For example, if someone were to gather 50 gold coins, but they consistently harmed others during their stay in The Depths,
                        then I will deny access to the exit as they will cause harm to others outside of The Depths.
                        With that being said, I watched you betray and backstab others.
                        Although you helped that old man retrieve his cube, the explorer trusted you, yet you decided to keep the treasure for yourself and dishonour your agreement with him.
                        So, I deny you permission to leave this labyrinth and you will never have a second chance at leaving this place.
                            * What??!! So what am I supposed to do??
                                Spend the rest of your days here in this labyrinth, rotting away...
                                    * --- finish the game --- (closed_bad += 1)
                                        Fodder
''')


# Good ending screen
good_ending_screen = Button(text="Good Ending: You passed the Overseer's test and escaped the labyrinth...", color=color.dark_gray, scale=100, enabled=False)
good_ending_audio = Audio('sounds/HOME - Resonance.mp3', loop=False, autoplay=False, volume=0.2)

def good_ending():
    good_ending_screen.enable()
    good_ending_audio.play()

# Bad ending screen
bad_ending_screen = Button(text="Bad Ending: You failed the Overseer's test and forever stuck in the labyrinth...", color=color.dark_gray, scale=100, enabled=False)
bad_ending_audio = Audio('sounds/matt maltese.mp3', loop=False, autoplay=False, volume=0.2)

def bad_ending():
    bad_ending_screen.enable()
    bad_ending_audio.play()

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
                            * Directly to my right?? If it's so close then why don't you get it yourself?
                                That's besides the point rookie! Now go find it and I'll reward you with 10 gold coins.
                                    * Alright. (closed += 1)
                                        Thanks.
                                    * "5" gold coins? I feel like I should be rewarded with much more, don't you think? (haggled += 1)
                                        You greedy little cow... Fine, 15 gold coins it is...
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
    key_route = 0,
    money_split = 0
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
                                                                                And also, I painted the vault door red so you can spot it easily
                                                                                    * *leave* (closed += 1)
                                                                                        Fodder
                                                                            * I'll find the two keys. (key_route += 1)
                                                                                Alright. Good luck on finding them...
                                                                                And also, I painted the vault door red so you can spot it easily
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

explorer_convo3 = dedent('''
Fodder
Great to see you again!
    * I found the treasure. It amounts to 40 gold coins.
        Fantastic! Thanks for keeping up your end of the deal. It would've been easy to just bail on me...
            * *split the money* (money_split += 1)
                Here's your half of the money, 20 gold coins, and that concludes our business together.
                    I wish you the best of luck on your quest...
                        * *leave* (closed += 1)
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
    closed = 0,
    gate_open = 0
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
...
    * I have enough money.
        It seems you do. Congratulations, it's been a while since someone's accomplished this feat.
            * ...
                As promised, I'll open the gate now...
                    * Finally... (gate_open += 1)
                        Good luck...
                            * *leave* (closed += 1)
                                Fodder
''')

gate_convo3 = dedent('''
Fodder
...
    * *leave* (closed += 1)
        Fodder
''') 
# 
def cube_clicked():
    quest_cube.disable()
    player.disable()
    cube_item_popup.enable()
    cube_item_popup.start_conversation(cube_item_dialog)

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
        invoke(intro_disappear, delay=15)
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

    # Cube Item dialog closer
    if cube_item_variables.closed == 1:
        player.enable()
        cube_item_popup.disable()
        cube_item_variables.closed -= 1

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

    # If the player returns with the money
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

    # Gate Opener
    if gate_variables.gate_open == 1:
        gate1.animate_position(gate1.position+(gate1.right)*1.1, duration=6, curve=curve.linear)
        gate2.animate_position(gate2.position+(gate2.left)*1.1, duration=6, curve=curve.linear)
        gate_variables.gate_open += 1

# Overseer NPC
    # Endings
    if overseer_variables.closed_good == 1:
        overseer_conversation.disable()
        good_ending()
        overseer_variables.closed_good -= 1
    if overseer_variables.closed_bad == 1:
        overseer_conversation.disable()
        bad_ending()
        overseer_variables.closed_bad -= 1

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

            # If the player retrieved the treasure
            if explorer_variables.mission_solved == 2:
                player.disable()
                explorer_conversation.enable()
                explorer_conversation.start_conversation(explorer_convo3)

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
            if gate_variables.gate_open == 0:
                # If the player doesn't have enough money
                if coins < 50:
                    player.disable()
                    gate_conversation.enable()
                    gate_conversation.start_conversation(gate_convo1)
            # If the player has gathered enough money
                if coins >= 50:
                    player.disable()
                    gate_conversation.enable()
                    gate_conversation.start_conversation(gate_convo2)

            if gate_variables.gate_open == 2:
                player.disable()
                gate_conversation.enable()
                gate_conversation.start_conversation(gate_convo3)

# Overseer NPC
    if overseer.hovered == True:
        if key =='left mouse down':
            # Bad ending, money was not split
            if explorer_variables.money_split == 0:
                player.disable()
                overseer_conversation.enable()
                overseer_conversation.start_conversation(overseer_convo2)
            
            # Good ending, money was split
            if explorer_variables.money_split == 1:
                player.disable()
                overseer_conversation.enable()
                overseer_conversation.start_conversation(overseer_convo1)        
            
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
            explorer_variables.mission_solved += 1
            player.disable()
            chest_popup.enable()
            chest_popup.start_conversation(chest_dialog)
                

# Coin
    if coin1.hovered == True:
        if key == 'left mouse down':
            coin_audio.play()
            coins += 1
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

    if coin4.hovered == True:
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