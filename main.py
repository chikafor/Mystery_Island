
# Mystery Island: The Lost Lighthouse


def show_introduction():
    print("================================")
    print("        MYSTERY ISLAND")
    print("      THE LOST LIGHTHOUSE")
    print("================================")

    print("\nYou have been stranded on a mysterious island.")
    print("Your mission is to explore the island and restore the lighthouse.")
    print("You have only 5 energy points. Use them carefully!")


def show_map():
    print("\n========== ISLAND MAP ==========")
    print("Beach <--> Jungle")
    print("           |")
    print("       Cave")
    print("           |")
    print("       Old Bridge <--> Lighthouse")
    print("================================")


def start_game():
    show_introduction()

    player_name = input("\nWhat is your name, adventurer? ").strip()

    if player_name == "":
        player_name = "Adventurer"

    # The player's starting information
    energy = 5
    location = "Beach"

    # This dictionary describes the locations connected to each place.
    connections = {
        "Beach": ["Jungle"],
        "Jungle": ["Beach", "Cave", "Old Bridge"],
        "Cave": ["Jungle"],
        "Old Bridge": ["Jungle", "Lighthouse"],
        "Lighthouse": ["Old Bridge"]
    }

    print(f"\nWelcome, {player_name}!")
    print("Your adventure begins on the Beach.")

    # The game continues while the player has energy.
    while energy > 0:

        print("\n========== YOUR STATUS ==========")
        print(f"Player: {player_name}")
        print(f"Location: {location}")
        print(f"Energy: {energy}")
        print("=================================")

        show_map()

        # Get the locations connected to the player's current location.
        available_locations = connections[location]

        print("\nWhere would you like to go?")

        # Create numbered choices for the available locations.
        move_choices = {}

        for number, place in enumerate(available_locations, start=1):
            move_choices[str(number)] = place
            print(f"{number}. Go to {place}")

        print("Q. Quit game")

        choice = input("\nEnter your choice: ").strip().lower()

        if choice == "q":
            print("\nYou have chosen to leave the island.")
            print("Game ended. Goodbye!")
            break

        elif choice in move_choices:

            # Only a valid move reaches this point.
            destination = move_choices[choice]

            location = destination
            energy = energy - 1

            print(f"\nYou travelled to the {location}.")
            print("You used 1 energy point.")

            if energy == 0:
                print("\nYou have run out of energy!")
                print("You could not complete your mission.")
                print("GAME OVER!")

        else:
            print("\nInvalid choice.")
            print("Please select one of the displayed options.")
            print("Your energy has not been reduced.")


if __name__ == "__main__":
    start_game()
