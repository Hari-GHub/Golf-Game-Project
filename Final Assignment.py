import random


# main function - gets initial details and displays the final scores
def play_tropical_golf():
    # gets the players name and validates it
    Name = str(input("What is your name?\n"))
    while not Name.isalpha():
        print("Please enter only alphabets\n")
        Name = str(input())
    print("Welcome  " + Name)
    print("Let's play golf,CP1401 Style!")
    # gets the numerical par and validates it
    try:
        par_value = int(input("Choose a par for this course(between 3-5 inclusive)\n"))
        while not (2 < par_value < 6):
            print("I'm sorry,you must choose a number between 3-5 inclusive.Please enter again\n")
            par_value = int(input())
    except ValueError:
        print("par should be an integer")
    # gets the distance of the ball from the hole and validates it
    try:
        distance_to_hole = int(input("How many meters to the hole(between 195-250 inclusive)\n"))
        while not (19.4 < distance_to_hole < 251):
            print("I'm sorry,you must choose a number between 195-250 inclusive.Please enter again\n")
            distance_to_hole = int(input())
    except ValueError:
        print("distance should be an integer")

    # updates the scores of every round in a list and displays the final score
    updated_score_list = []
    option = display_menu()
    select_menu(option, Name, distance_to_hole, par_value, updated_score_list)
    while not (option.upper() == "Q"):
        option = display_menu()
        result = select_menu(option, Name, distance_to_hole, par_value, updated_score_list)
        if option.upper() == "P":
            updated_score_list = result
    display_score_list(updated_score_list, par_value)


# displays the menu
def display_menu():
    print("(I)nstructions")
    print("(P)lay round")
    print("(Q)uit \n")
    menu = input()
    return menu


# Allows the player to select the menu and performs the selected operation
def select_menu(menu, player_name, distance_to_hole, par, score_list):
    if menu.upper() == "I":
        show_instructions(distance_to_hole, par, player_name, score_list)
    elif menu.upper() == "P":
        result = play_game(distance_to_hole, par, score_list)
        return result
    elif menu.upper() == "Q":
        print("Farewell and thanks for playing " + player_name)
    else:
        print("Invalid menu choice \n")
        print("Let's play golf,CP1401 Style!\n")
        print("Golf!")


# Prints the instruction of the game
def show_instructions(distance_to_hole, par, name, score_list):  # coding standards
    print("This is a simple golf game in which each hole is " + str(distance_to_hole) + " game away with par " + str(
        par) + ". You are able to choose from 3 clubs, the Driver, Iron or Putter. The Driver will hit around 100m, "
               "the Iron around 30m and the Putter around 10m. The putter is best used very close to the hole.")
    print("Golf!")
    option = display_menu()
    select_menu(option, name, distance_to_hole, par, score_list)


# Allows the player to select the club and modifies the distance to the hole.Updates the score corresponding to the
# round.
def play_game(distance_to_hole, par, score_list):
    print("This hole is a " + str(distance_to_hole) + "m par " + str(par) + "\n")
    shot_count = 0
    actual_distance = 0
    while not (distance_to_hole == 0):
        # selects the club
        print("You are " + str(distance_to_hole) + "m from the hole,after " + str(shot_count) + " shot/s")
        print("Club selection: press D for driver,I for Iron,P for Putter.")
        club = str(input("Choose club:"))
        shot_count += 1
        # Generates a random distance to the hole and modifies it
        if club.upper() == "D":
            actual_distance = random.randint(80, 120)
        elif club.upper() == "I":
            actual_distance = random.randint(24, 36)
        elif club.upper() == "P" and distance_to_hole < 10:
            if (0.8 * distance_to_hole) > 0:
                actual_distance = random.randint(int(0.8 * distance_to_hole), int(1.2 * distance_to_hole))
            else:
                actual_distance = random.randint(1, int(1.2 * distance_to_hole))
        elif club.upper() == "P":
            actual_distance = random.randint(8, 12)
        else:
            print("Invalid club selection = air swing :( \n" + "Your shot went 0m.You are " + str(
                distance_to_hole) + "from the hole,after" + str(shot_count) + "shot/s")

        distance_to_hole = abs(distance_to_hole - actual_distance)
        print("Your shot went " + str(actual_distance) + "m.\n")
    current_score = shot_count
    # displays the score for the round
    if current_score > par:
        print("Clunk... After " + str(current_score) + " hits, the ball is in the hole! Disappointing. You are " + str(
            current_score - par) + " over par.")
    elif current_score == par:
        print("Clunk... After " + str(current_score) + " hits, the ball is in the hole! And that's par.")
    else:
        print("Clunk... After " + str(current_score) + " hits, the ball is in the hole! Congratulations,you are " + str(
            par - current_score) + "under par.")

    # print(sum(score_list)+current_score)
    updated_score_list = update_score_list(score_list, current_score)
    return updated_score_list


# updates the current score to the score list
def update_score_list(score_list, new_score):
    score_list.append(new_score)
    return score_list


# displays the score in the given format
def display_score_list(score_list, par):
    for indx in range(0, len(score_list)):
        if score_list[indx] > par:
            print("Round " + str(indx + 1) + " :" + str(score_list[indx]) + " shots. " + str(
                score_list[indx] - par) + " over par")
        elif score_list[indx] == par:
            print("Round " + str(indx + 1) + " :" + str(score_list[indx]) + " shots. On par")
        else:
            print("Round " + str(indx + 1) + " :" + str(score_list[indx]) + " shots. " + str(
                par - score_list[indx]) + " under par.")


try:
    play_tropical_golf()
except:
    print("Something went wrong")
