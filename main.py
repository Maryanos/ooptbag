from room import Room
from character import Enemy

# Setting room names and descriptions
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall = Room("Dining hall")
dining_hall.set_description("A large room with ornate golden decorations")


# Linking the rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")


#Creating a new character Dave from the Enemy child class
dave = Enemy("Dave", "A smelly zombie\n")
dave.set_conversation("Hello! I'm Dave, I'm not a zombie, I swear to God!")
dave.set_weakness("cheese")


#Creating a new character Dave from the Enemy child class
anne = Enemy("Anne", "Not the most friendly person...\n")
anne.set_conversation(None)
anne.set_weakness("None")


# Loop allowing the player to move between the rooms
current_room = ballroom
while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    command = input("> ")
    current_room = current_room.move(command)

    # Placing Dave character into the dinning hall
    if current_room == dining_hall:
        print("\n")
        dave.describe()
        dave.talk()
        fight_with = input("What will you fight with?\n> ")
        dave.fight(fight_with)

    if current_room == kitchen:
        print("\n")
        anne.describe()
        anne.talk()




# Rooms Plan        #####################
                    #                   #
         #N         #                   #
      #W     #E     #     Kitchen       #
         #S         #                   #
                    #                   #
##############################  #########
#                   #                   #
#                   #                   #
#     Ballroom      #    Dining Hall    #
#                                       #
#                   #                   #
#########################################




