# Molly Jain
# functionsProject.py

storyPlay = True # this decides whether or not you are playing the game, is true until the user wants to stop playing

# function that prompts users for words, then prints the first story
def story1():
    print("Let's start writing your Halloween story! Please enter words in the requested categories.")
    verb1 = input("Verb:")
    adjective1 = input("Adjective:")
    adjective2 = input("Another adjective:")
    pluralNoun1 = input("Plural noun:")
    pluralNoun2 = input("Another plural noun:")
    noun1 = input("Noun:")
    adjective3 = input("Adjective:")
    color1 = input("Color:")
    noun2 = input("Noun:")
    adjective4 = input("Adjective:")
    animal1 = input("Animal:")
    verb2 = input("Verb:")
    verb3 = input("Another verb:")
    adjective5 = input("Adjective:")
    food1 = input("Food:")
    adjective6 = input("Adjective:")
    food2 = input("Food:")
    print("Here's your Mad Libs story, Halloween Treats!")
    print()
    print("Halloween is the best time to", verb1, ".")
    print("The weather is", adjective1,"and", adjective2,"and you go door to door saying \"Trick or Treat\".")
    print("People give you", pluralNoun1,"and",pluralNoun2, ".")
    print("This year I will dress up as a", noun1, ", a", adjective3, color1, noun2, "or maybe a", adjective4, animal1,".")
    print("If someone says \"Trick\" instead of giving you a treat, you might have to",verb2, "or",verb3,".")
    print("You might have to try to scare them into giving you a", adjective5, food1, "or a", adjective6, food2,".")

# function that prompts the user for words then prints the second story
def story2():
    print("Let's start making your apple picking story! Please enter words in the requested categories.")
    season1 = input("Season:")
    verb1 = input("Verb ending in -ing:")
    color1 = input("Color:")
    color2 = input("Another color:")
    color3 = input("One more color:")
    place1 = input("A place:")
    verb2 = input("Verb:")
    pluralNoun1 = input("Plural noun:")
    noun1 = input("Noun:")
    color4 = input("Color:")
    adjective1 = input("Adjective:")
    noun2 = input("Noun:")
    noun3 = input("Another noun:")
    verb3 = input("Verb:")
    noun4 = input("Noun:")
    noun5 = input("One more noun:")
    adjective2 = input("Adjective:")
    print("Here's your Mad Libs story, Autumn Leaf Sightseeing!")
    print()
    print(season1, "is the time of year when the leaves start",verb1,"colors,like",color1,",",color2,", and",color3,".")
    print("It's fun to drive to the",place1,"to",verb2,"at all the colorful",pluralNoun1,".")
    print("In the mountains, the leaves on the",noun1,"trees turn bright",color4,", which looks",adjective1,"among the",noun2,"trees that stay green year round.")
    print("There are also",noun3,"festivals in the fall, where they",verb3,"the",noun4,"trees to make",noun5,"syrup, which tastes",adjective2,"on pancakes.")

# function that prompts the user for words, then prints the third story
def story3():
    print("Let's start writing leaf sightseeing story! Please enter words in the requested categories.")
    adjective1 = input("Adjective:")
    verb1 = input("Verb:")
    verb2 = input("Another verb:")
    person1 = input("Type of person (ex. brother, firefighter):")
    food1 = input("Type of food:")
    season1 = input("A season:")
    person2 = input("Person,possesive(ex. Bob's):")
    noun1 = input("Noun:")
    person3 = input("A person:")
    noun2 = input("Noun:")
    place1 = input("Place:")
    person4 = input("A person:")
    verb3 = input("Verb in past tense:")
    color1 = input("Color:")
    adjective2 = input("Adjective:")
    print("Here's your Mad Libs story, Apples!")
    print()
    print("Red,",adjective1,"apples! Today we are going to",verb1,"apples.")
    print("I am going to",verb2,"the most. My",person1,"and I are having a",food1,"picking contest this year.")
    print("Every",season1,"we go to",person2,"farm to pick a",noun1,"of apples.")
    print("This year",person3,"wants to make a",noun2,", so we need a lot.")
    print("When we arrive at",place1,",",person4,"counts our apples. We anxiously await the the final count.")
    print("My",person1,"and I",verb3,"! Well actually I had one more than them, but it had a",color1,"slimy worm in it.")
    print("That night we had",adjective2,"applesauce!")

# function that prints a blank line for format, then asks which story
def storySelect():
    print()
    story = int(input("Which story would you like? \n 1.Halloween \n 2.Apple Picking \n 3.Leaf Sightseeing \n Please enter 1,2 or 3:"))
    # continues asking the user to enter 1, 2, or 3 until they do
    while (story != 1) and (story != 2) and (story != 3):
        story = int(input("Please enter 1, 2, or 3."))
    # calls one of the above functions depending on what the user inputs
    if story == 1:
        story1()
    elif story == 2:
        story2()
    elif story == 3:
        story3()

# allows you to play the game as many times as you want
while storyPlay == True:
    print()
    print("Welcome to Mad Libs! Let's start playing.")
    # has the user pick the story
    storySelect()
    keepPlaying = input("Would you like to play again? (y/n)")
    # if the user says yes, the loop will keep going and they can keep play
    if (keepPlaying == "y") or (keepPlaying == "Yes") or (keepPlaying == "yes"):
        storyPlay = True
    # if the user says no, the loop will stop and the program will end
    elif (keepPlaying == "n") or (keepPlaying == "No") or (keepPlaying == "no"):
        print("Thanks for playing Mad Libs!")
        storyPlay = False