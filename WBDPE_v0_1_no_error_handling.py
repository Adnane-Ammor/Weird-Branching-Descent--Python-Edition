# THIS IS THE GAME BEFORE I GAVE IT TO GEMINI AND ASKED IT TO WRITE THE ERROR HANDLING FOR ME


print('''
 █████╗ ██████╗ ███╗   ██╗ █████╗ ███╗   ██╗ ██████╗ 
██╔══██╗██╔══██╗████╗  ██║██╔══██╗████╗  ██║██╔════╝ 
███████║██║  ██║██╔██╗ ██║███████║██╔██╗ ██║████║      
██╔══██║██║  ██║██║╚██╗██║██╔══██║██║╚██╗██║██║      
██║  ██║██████╔╝██║ ╚████║██║  ██║██║ ╚████║╚██████╗ 
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
''')

# Variable, flags and dictionaries

flags = {

}

PRONOUNS = {
    "he": {"subjective": "he", "objective": "him", "possesive1": "his", "possesive2": "his", "sub_verb": "he is"},
    "she": {"subjective": "she", "objective": "her", "possesive1": "her", "possesive2": "hers", "sub_verb": "she is"},
    "they": {"subjective": "they", "objective": "them", "possesive1": "their", "possesive2": "theirs", "sub_verb": "they are"}
}

ALIVEP = {
    "dad": {"al_parent": "dad", "al_parent2": "father", "subjective": "he", "objective": "him", "possesive1": "his", "possesive2": "his", "sub_verb": "he is", "alc_bev": "and a few cans of beer on the floor with one in his hand"},
    "mom": {"al_parent": "mom", "al_parent2": "mother", "subjective": "she", "objective": "her", "possesive1": "her", "possesive2": "hers", "sub_verb": "she is", "alc_bev": "a bottle of red wine on the floor"}
}

DEADP = {
    "dad": {"d_parent": "dad", "d_parent2": "father", "subjective": "he", "objective": "him", "possesive1": "his", "possesive2": "his", "sub_verb": "he is"},
    "mom": {"d_parent": "mom", "d_parent2": "mother", "subjective": "she", "objective": "her", "possesive1": "her", "possesive2": "hers", "sub_verb": "she is"}
}

partner = {
    "he": {"subjective": "he", "objective": "him", "possesive1": "his", "possesive2": "his", "sub_verb": "he is"},
    "she": {"subjective": "she", "objective": "her", "possesive1": "her", "possesive2": "hers", "sub_verb": "she is"},
    "they": {"subjective": "they", "objective": "them", "possesive1": "their", "possesive2": "theirs", "sub_verb": "they are"}
}

# Story Nodes/Parts

def story_node1():

    lines = [
        "\nYou've just been born...",
        f'"{name}, what a beautiful baby you are!" Your father exclaims.',
        f'"What a beautiful baby {player_pronouns['sub_verb']} indeed!", your mother says, with bags under her eyes, the ones she got from spending 6 hours in labor trying to push you out...',

    ]
    for line in lines:
        input(line)


def story_node1_choice():
    dead_parent = input("\nFive years later, God himself comes to you in a dream and gives you the choice to either kill your mom or dad [mom | dad]: ")
    if dead_parent == "mom":
        input("\nYou chose your mom because she took away your iPad earlier today.")
        DEADP_choice = DEADP[dead_parent]
        ALIVEP_choice = ALIVEP["dad"]

    elif dead_parent == "dad":
        input("\nYou choose your dad because he had punished you for not eating your veggies, honestly kinda deserved.")
        DEADP_choice = DEADP[dead_parent]
        ALIVEP_choice = ALIVEP["mom"]
    
    input(f"\nNext day, your {dead_parent} comically dies by hitting {DEADP_choice['possesive1']} neck on the stairs, turns out {DEADP_choice['subjective']} had slipped on a banana peel you had forgotten to pick up near the staircase.")
    input(f"A funeral was obviously held and your {ALIVEP_choice['al_parent2']} becomes an alcoholic, you're too young to even understand what's going on.")


def story_node2():
    lines = [
        "\nA few years later, you're now 9 years old.",
        "You're at school, it's lunch time and you're chillin' playing Half-Life 2 Episode 2 on your Steam Deck 3 XL, then you hear a loud, annoying, smelly voice:",
        '\n"Hey small fry!"',
        "\nYou wonder if you were in a 2010's Nickelodeon sitcom, and then lift your head up.",
        "It's the class bully."
        '\n"Gimme that!" he says.',
        "He violently snatches the console off of your small child fingers.",
        "You stand up and stare at him."
    ]
    for line in lines:
        input(line)

def story_node2_choiceB():
    input("\nYou throw a good punch to the side of his head,")
    input("he then proceeds to chokeslam you WWE-style on the ground.")
    input("You see him walk away, the console is still with him...")
    choice_B = input('''A. Do you follow him and try to get it back.
B. Rest on the ground for a bit? [A | B]: ''')
    if choice_B == "A":
        input("\nYou try to get up but you're too dizzy from the shock your little head just suffered that you have to sit down...")
        input("The PE teacher notices you and goes to check up on you,") 
        input("you tell him about what happened and he decides to get your console back from the bully.")

    elif choice_B == "B":
        input("\nYou stayed on the ground for a bit...")
        input("The PE teacher notices you and goes to check up on you,") 
        input("you tell him about what happened and he decides to get your console back from the bully.")
        input("...")
        input("A few minutes later the teacher comes back and gives you your Steam Deck 3 XL still running Half-Life 2 Episode 2 back.")
        coach_choice = input('''He then asks: "Hey kiddo, you want me to give you some self-defense classes after-school?"
    Do you accept [y | n]: ''')
        if coach_choice == "y":
            input(f'You wanted to say yes, and then you remembered the whole thing your {ALIVEP_choice['al_parent2']} told you about "Stranger Danger",')
            input("so you politely decline.")
        if coach_choice == "n":
            input("You wanted to say no,")
            input(f'honestly completely fair choice after everything your {ALIVEP_choice['al_parent2']} told you about "Stranger Danger".')





def story_node2_choice():
    input("\nA. Do you keep staring at him?")
    input("B. do you punch him?")
    bully_standoff = input("or C. do you run off and tell a trusted adult? [A | B | C]: ")
    if bully_standoff == "A":
        input("The bully gets so creeped out he just hands you the console back.")

    elif bully_standoff == "C":
        input("You run up to your PE teacher and tell him about it,") 
        input("he actually goes and talks to the bully and gets your console back.") 
        input("Who knew listening to the anti-bullying campaign's advice would actually work...")

    elif bully_standoff == "B":
        story_node2_choiceB()
        


def ending_A():
    input("You turn your face and body to the wall on your left...")
    input('\n"Today was an okay day..."')
    input("...")
    input("...")
    input("zzzzzzzzz")

    input("\nPASSIVE ENDING: THE END\n")

def ending_B():
    input("You turn your face and body to the ceiling,") 
    input("you keep staring at it for a bit.")
    input('\n"What a weird day this was..."')
    input("...")
    input("...")
    input("zzzzzzzzz")

    input("\nENDING B: THE END\n")



def ending():
    input("\n**THREE HOURS LATER**")

    input("\nAfter a tiring day at school, you're finally home...")
    input("You open the front door, you enter with your slouched back and a heavy sigh:")
    input("\n[ASCII art of a staircase in front, door to the right, and couch to the left]")
    input("(we don't have the budget for graphics so pretend it's there)\n")
    input(f"To your right is the portal  to the garage, to your left is the living room, where you see your {ALIVEP_choice['al_parent']} passed out on the couch {ALIVEP_choice['alc_bev']}.")
    input("\nIn front of you are the stairs that lead to your room...")
    input("Advance forward? [y | n]: ")
    input("(didn't I already tell you that we ran out of funding? Do you think this is Life is Strange?)")
    input("So you advance forward.")

    input("\nYou open your bedroom door, throw your bag next to your bed and jump all the way to your cozy bed.")


    if bully_standoff in ("A", "C"):
        ending_A()
    
    elif bully_standoff == "B":
        ending_B()
    
    else:
        print("How the hell did you even get here?")


def credits():
    print('''
    ┌─────────────────────────────┐
    │    WEIRD BRANCHING DESCENT  │
    │       by Adnane Ammor       │
    │     (Open Source, 2026)     │
    └─────────────────────────────┘
    ''')
    

# Game sequence

print("WELCOME TO Weird Branching Descent: Python Edition")
input("\nPress [Enter] to start")

name = input("Name your character: ")
pronoun_choice = input("What pronouns? [he | she | they]: ").lower()
player_pronouns = PRONOUNS[pronoun_choice]

story_node1()
story_node1_choice()
story_node2()
story_node2_choice()
ending()
credits()
