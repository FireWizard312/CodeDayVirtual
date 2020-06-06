# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mom = Character("Mother")
define dad = Character("Father")
define bro = Character("Brother")
define sis = Character("Taylor")
define nar = Character("Narrator")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene forest
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # These display lines of dialogue.

    nar "You're exploring the dark woods with your brother and his dog. Suddenly, you guys hear a noise and decide to investigate. As you get closer, you can see the faint outline of a dog"

menu:
    
    "Leave the dog, listen to common sense.":
        jump safety

    "Take the dog home, it looks so cute!":
        jump dog

label safety:
    nar "As you leave the dog behind, you feel like a great weight has been lifted off your chest. When you go back to the forest the next day, the dog was no where to be found."
    pause 1
    nar "Ending: Safe"
    return

label dog:
    nar "You bring the dog back home."
    scene house
    with fade
    show mother at left
    mom "Where did you guys get this dog?"
    show brother at right
    bro "We found it in the forest."
    mom "Well I guess now we have two dogs."
    hide brother
    hide mother
    nar "You've noticed that your two dogs have been acting aggresively to each other. This morning, when you wake up, both dogs are missing."

menu:

    "Go look for the dogs, they have to somewhere close.":
        jump detective
    
    "Wait for the dogs to come back.":
        jump passive     
    
label detective:
    nar "You follow where your dogs' footsteps lead, and and you find blood all over the doggy door."

menu:

    "Weird. How did that get there without anyone noticing it?":
        jump detective2
    
    "Must have been a dog fight.":
        jump passive

label passive:
    
    nar "One day later, the newly adopted dog comes back, but there is no sign of your old dog. Your brother takes the loss really hard, and starts to bond with the new dog."
    scene house    
    show brother
    bro "I'm going out with the new dog!"
    hide brother

menu:

    "Look for your brother":
        jump accused
    
    "Wait for him, he might just have been lost.":
        jump alldead
    
label detective2:   

    nar "You decide to follow where the bloodstains lead, and find your old dog mangled and dead in the nearby forest, actually quite close to the same place where you found the new dog."
    scene house
    nar "Your brother takes the loss of his dog very hard, and bonds with the new dog."
    nar "You point out how strange it is that the new dog came back unscathed while the old dog was found mangled right next to where you found the new dog."
    show angrybrother
    bro "You're delusional! I'm going to take a walk with the dog, don't come looking for me."
    hide angrybrother
    nar "5 hours pass, your brother doesn't come back. You begin to worry."

menu:

    "Look for your brother":
        jump accused
    
    "Wait for him, he might just have been lost.":
        jump telldad

label accused:
    nar "You find your brother's body all mangled and ripped up in the river. However, once you call the cops and tell your parents, they don't believe the story of the ghost dog, and believe that you killed him"
    nar "You are arrested and thrown into jail."
    pause 1
    nar "Ending: Accused"
    return

label alldead:
    nar "A few days later, someone knocks on your door."
    nar "It's your neighbor. He comes bearing bad news."
    nar "You can't hear the conversation, but your mother seems distressed."
    scene house
    show distressmom at left
    with fade
    mom "He's dead!"
    show distressdad at right
    with fade
    dad "Who?"
    mom "Our son!"
    dad "How could this happen?"
    mom "I don't know! They just found his body in the forest!"
    hide distressmom
    hide distressdad   
    pause 0.5
    nar "One week later, the dog comes back. You have questions about how the dog came back perfectly fine but your brother was dead. However, you chose to ignore all the clues, as you did before."
    pause 0.5
    nar "You wake up in the dead of the night. You hear growling, and find the dog in your room. Your last thought before it kills you is of regret."
    pause 1
    nar "Ending: Oblivious"
    return

label telldad:
    nar "A few days later, someone knocks on your door."
    nar "It's your neighbor. He comes bearing bad news."
    nar "You can't hear the conversation, but your mother seems distressed."
    scene house
    show distressmom at left
    with fade
    mom "He's dead!"
    show distressdad at right
    with fade
    dad "Who?"
    mom "Our son!"
    dad "How could this happen?"
    mom "I don't know! They just found his body in the forest!"
    hide distressmom
    hide distressdad   
    pause 0.5
    nar "Since you followed all the clues, you put together that the dog must be behind all the murders. You tell your father your findings."
    pause 0.5
    show distressdad
    with fade
    dad "What do we do?"

menu:
    
    "Shoot the dog":
        jump fool

    "Slip the dog a sedative and leave":
        jump run
    
label fool:
    hide distressdad
    scene house
    with fade
    nar "You try and shoot the dog. However, the dog doesn't die. Your last thought is one of regret."
    pause 1
    nar "Ending: Fool"
    return

label run:
    hide distressdad
    scene house
    with fade
    nar "You slip the dog a sedative and take your sister, father, mother and run."
    nar "You find a new house, and try to forget this whole debacle."
    pause 1
    nar "Ending: Running"
    return