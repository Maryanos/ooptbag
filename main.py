from room import Room
from character import Enemy


# Setting room names and descriptions
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall = Room("Dining hall")
dining_hall.set_description("A large room with ornate golden decorations")
gaming_room = Room("Gaming Room")
gaming_room.set_description("Room full of exciting techy stuff")
bar = Room("Bar")
bar.set_description("Relaxing area but watch out don't trust anyone here")
beer_garden = Room("Beer garden")
beer_garden.set_description("Garden area full of drunked people, wait are they drunk or ....?")
main_garden = Room("Main garden")
main_garden.set_description("The biggest and most beautifull garden you have ever seen in your life... ")
hunting_area = Room("Hunting area")
hunting_area.set_description("The sounds of hunting rifles are heard very clocely... Not a safe place to be!")


# Linking the rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
dining_hall.link_room(bar, "south")
ballroom.link_room(dining_hall, "east")
ballroom.link_room(gaming_room, "south")
gaming_room.link_room(ballroom, "north")
gaming_room.link_room(bar, "east")
bar.link_room(dining_hall, "north")
bar.link_room(gaming_room, "west")
bar.link_room(beer_garden, "east")
bar.link_room(main_garden, "south")
main_garden.link_room(gaming_room, "north")
main_garden.link_room(hunting_area, "east")
beer_garden.link_room(bar, "west")
beer_garden.link_room(hunting_area, "south")
hunting_area.link_room(main_garden, "west")
hunting_area.link_room(beer_garden, "north")


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


