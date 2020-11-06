# Molly Jain
# classProject.py

import random
# variable that decides if the game is still running
gameOver = False


class Computer:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, opponent):
        # one of the options when dueling
        print(f"The {self.name} attacked you! -10 to your health")
        opponent.health = opponent.health - 10

    def bigAttack(self, opponent):
        # another option when dueling
        print(f"The {self.name} used its special attack against you! -15 to your health")
        opponent.health = opponent.health - 15

    def heal(self):
        # another another options when dueling
        print(f"The {self.name} stopped to catch its breath. +5 to {self.name}'s health")
        self.health += 5

    def computer_move(self):
        # returns a random number that decides which option is used in the duel
        choice = random.randint(1, 4)
        return choice


# ---------------------------------------------- end of computer class -------------------------------------------------

class Character:
    characterNames = []

    def __init__(self, name, school):
        self.myName = name
        self.mySchool = school
        # spells that you can use in a duel
        self.mySpells = ["expelliarmus", "protego", "stupefy", "episkey"]
        self.health = 100
        Character.characterNames.append(self.myName)

    # methods that are called to lower opponent's health during duels
    def expelliarmus(self, opponent):
        opponent.health = opponent.health - 10
        print(f"You used expelliarmus! -10 to the {opponent.name}'s health")

    def stupefy(self, opponent):
        opponent.health = opponent.health - 15
        print(f"You used stupefy! -15 to the {opponent.name}'s health")

    def confundo(self, opponent):
        if "confundo" in self.mySpells:
            opponent.health = opponent.health - 10
            print(f"You used confundo! -10 to the {opponent.name}'s health")
        else:
            print("You don't know that spell yet!")

    def episkey(self):
        self.health += 10
        print("You used episkey! +10 to your health")

    def aguamenti(self, opponent):
        if "aguamenti" in self.mySpells:
            opponent.health = opponent.health - 10
            print(f"You used aguamenti! -10 to the {opponent.name}'s health")
        else:
            print("You don't know that spell yet!")

    def petrificus(self, opponent):
        if "petrificus totalus" in self.mySpells:
            opponent.health = opponent.health - 15
            print(f"You used petrificus totalus! -15 to the {opponent.name}'s health")
        else:
            print("You don't know that spell yet!")

    def levicorpus(self, opponent):
        if "levicorpus" in self.mySpells:
            opponent.health = opponent.health - 10
            print(f"You used levicorpus! -10 to the {opponent.name}'s health")
        else:
            print("You don't know that spell yet!")

    def reducto(self, opponent):
        if "reducto" in self.mySpells:
            opponent.health = opponent.health - 10
            print(f"You used reducto! -10 to the {opponent.name}'s health")
        else:
            print("You don't know that spell yet!")

    def incendio(self, opponent):
        if "incendio" in self.mySpells:
            opponent.health = opponent.health - 15
            print(f"You used incendio! -15 to the {opponent.name}'s health")
        else:
            print("You don't know that spell yet!")

    # takes a parameter and checks what it's equal to, then calls the matching method
    def player_move(self, choice, opponent):
        if choice == "expelliarmus":
            self.expelliarmus(opponent)
        elif choice == "stupefy":
            self.stupefy(opponent)
        elif choice == "confundo":
            self.confundo(opponent)
        elif choice == "aguamenti":
            self.aguamenti(opponent)
        elif choice == "petrificus totalus":
            self.petrificus(opponent)
        elif choice == "levicorpus":
            self.levicorpus(opponent)
        elif choice == "reducto":
            self.reducto(opponent)
        elif choice == "incendio":
            self.incendio(opponent)
        elif choice == "episkey":
            self.episkey()
        elif choice == "quit":
            global gameOver
            gameOver = True
        else:
            print("That's not one of the spells you can use!")


# --------------------------------------------- end of character class -------------------------------------------------

def computerAttack(player, computer):
    print(f"\nEnter spells to fight the {computer.name}!")
    while player.health > 0 and computer.health > 0:
        print()
        print(player.mySpells)
        playerMove = input("What spell would you like to use?")
        computerMove = computer.computer_move()
        # let's the player to quit at anytime during the duel
        if playerMove == "quit":
            global gameOver
            gameOver = True
            break
        # checks spells that block the computer and moves back to the top of the while loop if they are entered
        if playerMove == "protego" or playerMove == "impedimenta":
            print(f"You blocked the {computer.name}! Neither of you were hurt.")
        # checks if the computer blocked the player
        elif computerMove == 1:
            print("You were blocked! No damage done.")
        else:
            # calls the method that calls the appropriate spell method, then calls the computer's method depending on what number its choice is
            player.player_move(playerMove, computer)
            if computerMove == 2:
                computer.attack(player)
            elif computerMove == 3:
                computer.bigAttack(player)
            elif computerMove == 4:
                computer.heal()
        print(f"Your health: {player.health}")
        print(f"Opponent's health: {computer.health}")
    else:
        # prints appropriate statement for who won, ends game if you lost
        if player.health < 1:
            print("You lost!")
            gameOver = True
        elif computer.health < 1:
            print("Congratulations! You won!")
            player.health = 100


# characters and computers used
harry = Character("Harry Potter", "Hogwarts")
cedric = Character("Cedric Diggory", "Hogwarts")
fleur = Character("Fleur Delacour", "Beauxbatons")
viktor = Character("Viktor Krum", "Durmstrang")
dragon = Computer("dragon")
mermaid = Computer("mermaid")

while gameOver == False:
    print("Welcome to Triwizard Adventures!")
    for name in Character.characterNames:
        print(name)
    # choose your character
    playerChoice = input("Which character would you like to be?")
    # makes sure an available player is chosen, then sets player variable to that
    while (playerChoice != "Harry Potter" and playerChoice != "Cedric Diggory" and playerChoice != "Fleur Delacour"
           and playerChoice != "Viktor Krum" and playerChoice != "quit"):
        playerChoice = input("Sorry, you can't choose that character! Please choose another character.")
    if playerChoice == ("Harry Potter"):
        player = harry
    elif playerChoice == "Cedric Diggory":
        player = cedric
    elif playerChoice == "Fleur Delacour":
        player = fleur
    elif playerChoice == "Viktor Krum":
        player = viktor
    elif playerChoice == "quit":
        gameOver = True
        break
    # asks players whether or not to join the tournament
    print("The Triwizard Tournament is beginning again this year!")
    join = input("Would you like to enter your name for the Triwizard Tournament? yes/no")
    if join == "yes":
        print("\nYour name was picked! Get ready to join the competition!")
    elif join == "no":
        print("\nYou decided not to enter, but your name just got picked! Someone must have entered your name...")
    elif join == "quit":
        gameOver = True
        break
    # decides what to do about the first challenge, learns spells based on choices. prints texts
    print("\nLevel 1: The First Task")
    print("\nIt's time for the first challenge! But no one will tell you what it is...")
    print("Your friend offers to study with you so that you can prepare for whatever is coming.")
    print("But another friend tells you that they think they know what the challenge might be.")
    firstChallengeStudy = input("What do you want to do? \nStudy \nFind out what the challenge is \nDo nothing")
    if firstChallengeStudy == "Study":
        print(
            "\nAfter studying for a while, you learn impedimenta, the blocking spell. Hopefully it will help in the first challenge!")
        # um what's that mean? fix that
        player.mySpells.append("impedimenta")
        print("\nCongratualations! You can now use impedimenta in duels!")
        print(
            "\nIt's the day of the first challenge! And they want you to... fight a dragon? You have to get past it and grab that golden egg. Here goes nothing...")
    elif firstChallengeStudy == "Find out what the challenge is":
        print("\nThere are dragons at Hogwarts! The first challenge must have something to do with dragons...")
        print(
            "You decide to learn aguamenti, the water spell. Water has to help against a fire-breathing dragon, right?")
        player.mySpells.append("aguamenti")
        print("\nCongratulations! You can now use aguamenti in duels!")
        print(
            "\nYou were right! The first challenge is to get past one of those dragons and grab a golden egg. How hard could it be?")
    elif firstChallengeStudy == "Do nothing":
        print("\nHow bad could the first challenge be? You should be fine with the spells you already know.")
        print("\nThe first challenge is fighting a DRAGON?! Maybe you should have studied some of those spells...")
    elif firstChallengeStudy == "quit":
        gameOver = True
        break
    # first fight
    computerAttack(player, dragon)
    if gameOver == True:
        break
    print("\nLevel 2: The Golden Egg")
    # introduces second level
    print(
        "You got through the first challenge! (And you only got a few dragon burns...) The next challenge has something to do with this golden egg - but what?")
    print(
        "\nEvery time you open the egg, it make some terrible screaming noise. You guess it's some kind of hint, but what could it be?")
    print("They told you you're only supposed to work it out on your own, but it's rather tempting to ask a friend.")
    print(
        "But you also heard that one of the other competitors already figured it out. You're sure that you could convince them to tell you if you really tried, but isn't that cheating?")
    print(
        "Maybe it's just better to figure it out on your own. It can't be too hard, otherwise they wouldn't have given a hint.")
    # asks what the player wants to do, learn a spell based on your choice (adds to spell list)
    eggChoice = input("\nWhat do you want to do?\nAsk a friend\nBribe the other competitor\nFigure it out alone")
    if eggChoice == "Ask a friend":
        print(
            "\nYou decided to ask your friend what to do.\n\"Well, dragons use fire, which you fight with water. What if you bring it underwater?\"")
        print("That night, you try bringing the egg underwater and... it works! You can hear a song, with these lyrics:"
              "\nCome seek us where our voices sound,"
              "\nWe cannot sing above the ground"
              "\nAnd while you're searching ponder this;"
              "\nWe've taken what you'll sorely miss,"
              "\nAn hour long you'll have to look,"
              "\nAnd to recover what we took,"
              "\nBut past an hour, the prospect's black,"
              "\nToo late, it's gone, it won't come back.")
        print(
            "\n\"We cannot sing above the ground\"...that must mean mermaids! And it sounds like you'll have to fight them to get something back. Better start practicing!")
        player.mySpells.append("petrificus totalus")
        print("\nCongratulations! You can now use petrificus totalus in duels!")
    elif eggChoice == "Bribe the other competitor":
        print(
            "\nIt turns out that competitor is very willing to share in exchange for 100 galleons in Honeydukes candy. But they would only tell you the general idea of the next challenge.")
        print(
            "They said that it has something to do with water, and that you have an hour to get back what someone took. It's not much to work with, but it's a start.")
        print(
            "If the first challenge was fighting dragons, maybe this one wants you to fight water with fire? Maybe you should learn the spell for fire...")
        player.mySpells.append("incendio")
        print("\nCongratulations! You can now use incendio in duels!")
    elif eggChoice == "Figure it out alone":
        print(
            "\nYou're trying to figure out the egg's clue next to the Great Lake when it rolls into the Great Lake. You lunge after it, but before you pull it out, you realize something. It's not making that awful noise anymore!")
        print(
            "That night you put the egg in a bucket of water. It's not making the noise, but something else is coming out of it now. You put your head under the water and hear a song!")
        print("The lyrics say this:"
              "\nCome seek us where our voices sound,"
              "\nWe cannot sing above the ground"
              "\nAnd while you're searching ponder this;"
              "\nWe've taken what you'll sorely miss,"
              "\nAn hour long you'll have to look,"
              "\nAnd to recover what we took,"
              "\nBut past an hour, the prospect's black,"
              "\nToo late, it's gone, it won't come back.")
        print(
            "\n\"We cannot sing above the ground\"...that must mean mermaids! And it sounds like you'll have to fight them to get something back. Better start practicing!")
        player.mySpells.append("reducto")
        print("\nCongratulations! You can now use reducto in duels.")
    elif eggChoice == "quit":
        gameOver = True
        break
    print(
        "\nIt's the day of the second task, but you haven't found anything missing that's valuable. You wonder what's been taken, but the task is about to start.")
    print(
        "\"Welcome to the second task!\" the announcer booms. \"Today, your competitors will have exactly one hour to find a person they value the most at the bottom of the Great Lake! Go!\"")
    print(
        "Of course! You haven't seen your friend all day. You must have to find them in the Great Lake! Talk about pressure...")
    print(
        "You leap in, using a spell to help you breathe under the water. You make it all the way to the bottom of the lake without encountering anyone.")
    print(
        "Just as the bottom comes into sight, a mermaid stops you! Looks like you'll have to fight to get your friend back!")
    # starts another fight
    computerAttack(player, mermaid)
    if gameOver == True:
        break
    print("Thanks for playing Triwizard Adventures")
    gameOver = True
    break
