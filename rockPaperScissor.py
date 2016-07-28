# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Invalid choice"


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Invalid choice"


def rpsls(player_choice):
    print '\n'
    print "Player chooses", player_choice

    player_number = name_to_number(player_choice)

    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)

    print "Computer chooses", comp_choice

    diff = (player_number - comp_number) % 5

    if diff == 0:
        print "Player and Computer tie!"
    elif (diff == 1) or (diff == 2):
        print "Player wins!"
    else:
        print "Computer wins!"

Player_choice = raw_input("Please provide you choice for rock,Spock,paper,lizard,scissors ")

if Player_choice not in (["rock","Spock","paper","lizard","scissors"]):
    print "You have entered incorrect value"
else:
    rpsls(Player_choice)

# rpsls("rock")
# rpsls("Spock")
# rpsls("paper")
# rpsls("lizard")
# rpsls("scissors")