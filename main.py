# Mystery Island: The Lost Lighthouse

from game import (
    new_game,
    CONNECTIONS,
    move_player,
    collect_item,
    show_inventory,
    make_decision
)


def show_introduction():
    print("================================")
    print("        MYSTERY ISLAND")
    print("      THE LOST LIGHTHOUSE")
    print("================================")

    print("\nYou have been stranded on a mysterious island.")
    print("Your mission is to explore the island and restore the lighthouse.")
    print("You have only 5 energy points. Use them carefully!")
    print("\nYou need a Rope to cross the Old Bridge.")
    print("You also need a Lantern to light the lighthouse.")


def show_map():
    print("\n========== ISLAND MAP ==========")
    print("Beach")
    print("  |")
    print("Jungle")
    print("  |")
    print("Cave")
    print("  |")
    print("Old Bridge")
    print("  |")
    print("Lighthouse")
    print("================================")


def handle_decision(player):

    location = player["location"]

    # Check whether a decision is required here
    if location not in ["Jungle", "Cave", "Old Bridge"]:
        return

    if location in player["decisions_made"]:
        return

    # Display the appropriate decision menu
    if location == "Jungle":
        print("\nYou have reached a dangerous part of the jungle.")
        print("1. Take the safe route.")
        print("2. Take the shortcut (costs 1 extra energy).")

    elif location == "Cave":
        print("\nYou discover a mysterious cave.")
        print("1. Search the cave for useful objects.")
        print("2. Leave the cave without searching.")

    elif location == "Old Bridge":
        print("\nThe old bridge looks unstable.")
        print("1. Cross carefully.")
        print("2. Rush across (costs 1 extra energy).")

    # Ask the player to make a decision
    while not player["game_over"]:

        choice = input("Make your decision: ").strip()

        success, message = make_decision(player, location, choice)

        print(f"\n{message}")

        if success:
            break

def play_game(player):

    # Collect the Rope at the Beach
    success, message = collect_item(player)
    print(f"\n{message}")

    print("\nYour adventure begins on the Beach.")

    while not player["game_over"]:

        print("\n========== YOUR STATUS ==========")
        print(f"Player: {player['name']}")
        print(f"Location: {player['location']}")
        print(f"Energy: {player['energy']}")
        print("=================================")

        print(show_inventory(player))
        show_map()

        available_locations = CONNECTIONS[player["location"]]

        print("\nWhere would you like to go?")

        move_choices = {}

        for number, place in enumerate(available_locations, start=1):
            move_choices[str(number)] = place
            print(f"{number}. Go to {place}")

        print("I. View inventory")
        print("Q. Quit game")

        choice = input("\nEnter your choice: ").strip().lower()

        if choice == "q":
            print("\nYou have chosen to leave the island.")
            print("Game ended. Goodbye!")
            player["game_over"] = True
            break

        elif choice == "i":
            print(show_inventory(player))

        elif choice in move_choices:

            destination = move_choices[choice]

            # Use the movement function from game.py
            success, message = move_player(player, destination)

            print(f"\n{message}")

            if not success:
                continue

            # Check whether the player has won
            if player["won"]:
                print(f"\nCongratulations, {player['name']}!")
                print("YOU HAVE WON THE GAME!")
                break

            # Check whether the player has lost
            if player["game_over"]:
                print("\nYou could not complete your mission.")
                print("GAME OVER!")
                break

            # A player who reaches the Lighthouse without a Lantern loses
            if player["location"] == "Lighthouse":
                player["game_over"] = True
                print("\nYou reached the Lighthouse without the Lantern.")
                print("You cannot restore the lighthouse.")
                print("GAME OVER!")
                break

            # Handle decisions at special locations
            handle_decision(player)

            if player["game_over"]:
                print("\nYou could not complete your mission.")
                print("GAME OVER!")

        else:
            print("\nInvalid choice.")
            print("Your energy has not been reduced.")


def start_game():

    show_introduction()

    player_name = input("\nWhat is your name, adventurer? ").strip()

    if player_name == "":
        player_name = "Adventurer"

    # Replay loop
    while True:

        # Create a fresh player for every new game
        player = new_game(player_name)

        print(f"\nWelcome, {player_name}!")

        play_game(player)

        print("\n========== GAME FINISHED ==========")

        replay = input("Would you like to play again? (yes/no): ").strip().lower()

        if replay not in ["yes", "y"]:
            print("\nThank you for playing Mystery Island!")
            break


if __name__ == "__main__":
    start_game()