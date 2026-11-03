# Mystery Island: The Lost Lighthouse

def show_introduction():
    print("================================")
    print("     MYSTERY ISLAND")
    print("   THE LOST LIGHTHOUSE")
    print("================================")

    print("\nYou have been stranded on a mysterious island after a storm.")
    print("Your mission is to explore the island and restore the lighthouse.")
    print("You must manage your energy carefully.")
    print("If your energy runs out before you complete your mission, you lose.")

    print("\nGood luck, adventurer!")


def start_game():
    show_introduction()

    player_name = input("\nWhat is your name, adventurer? ").strip()

    if player_name == "":
        player_name = "Adventurer"

    print(f"\nWelcome, {player_name}!")
    print("\nYou wake up on a quiet beach.")
    print("Waves crash against the shore, and the jungle lies ahead.")

    energy = 5
    location = "Beach"

    while True:
        print("\n========== BEACH ==========")
        print(f"Player: {player_name}")
        print(f"Energy: {energy}")
        print(f"Location: {location}")

        print("\nWhat would you like to do?")
        print("1. Explore the beach")
        print("2. Look around")
        print("3. Quit game")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print("\nYou walk along the beach and discover footprints.")
            print("They appear to lead towards the jungle.")

        elif choice == "2":
            print("\nYou see the ocean behind you and a thick jungle ahead.")

        elif choice == "3":
            print("\nYou have decided to leave the island adventure.")
            print("Game ended. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    start_game()
