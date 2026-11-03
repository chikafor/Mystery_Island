def new_game(player_name):
    player = {
        "name": player_name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "decisions_made": set(),
        "game_over": False,
        "won": False 
    }

    return player

#  The location a player can move to from each location
CONNECTIONS = {
    "Beach": ["Jungle"],
    "Jungle": ["Cave"],
    "Cave": ["Old Bridge"],
    "Old Bridge": ["Lighthouse"],
    "Lighthouse": []
}

# Items available at each location
ITEMS = {
    "Beach": "Rope",
    "Cave": "Lantern"
}


def collect_item(player):
    """
    Allows the player to collect an item at their current location.
    Each item can only be collected once.
    """

    # Check whether the game has ended
    if player["game_over"]:
        return False, "The game is already over."

    # Find out whether an item is available at the current location
    location = player["location"]

    if location not in ITEMS:
        return False, "There is no item to collect here."

    item = ITEMS[location]

    # Prevent the player from collecting the same item twice
    if item in player["inventory"]:
        return False, f"You have already collected the {item}."

    # Add the item to the player's inventory
    player["inventory"].append(item)

    return True, f"You collected the {item}!"

def move_player(player, destination):
    """
    Moves the player to another location if the move is allowed.
    Each successful movement costs one energy point.
    """
    # This checks whether the game has alreasy ended
    if player["game_over"]:
        return False, "The game is already over."
    
    # This checks whether the destination is a valid location
    if destination not in CONNECTIONS:
        return False, "That location does not exist."
    
    # This checks whether the destination is connected to the current location
    current_location = player["location"]

    if destination not in CONNECTIONS[current_location]:
        return False, "You cannot move there from your current location."

    # The player needs the rope to cross the bridge to the Lighthouse
    if destination == "Lighthouse" and "Rope" not in player["inventory"]:
        return False, "You need the rope to cross the Old Bridge."
    
    # This checks whether the player has enough energy
    if player["energy"] <= 0:
        player["game_over"] = True
        return False, "You have run out of energy. Game over!"

    # This moves the player and reduces energy by one
    player["location"] = destination
    player["energy"] -= 1

    # This checks whether the player has completed the task
    if destination == "Lighthouse" and "Lantern" in player["inventory"]:
        player["won"] = True
        player["game_over"] = True 
        return True, "Congratulations! You have lit the lighthouse and won!"

    # if energy reaches zro before winning, the player loses
    if player["energy"] == 0:
        player["game_over"] = True 
        return True, "You have run out of energy. Game over"

    return True, f"You moved to {destination}. Energy remaining: {player['energy']}."

def show_inventory(player):
    """Displays the items collected by the player."""

    if not player["inventory"]:
        return "Your inventory is empty."

    return f"Your inventory: {', '.join(player['inventory'])}" 

def make_decision(player, location, choice):
    """
    Processes a player's decision at the Jungle, Cave or Old Bridge.
    Returns whether the decision was accepted and a message.
    """

    # Check whether the game has ended
    if player["game_over"]:
        return False, "The game is already over."

    # Make sure the player is at the correct location
    if player["location"] != location:
        return False, "You are not at this location."

    # Check whether this decision has already been made
    if location in player["decisions_made"]:
        return False, "You have already made this decision."

    choice = str(choice).strip()

    # JUNGLE DECISION
    if location == "Jungle":

        if choice == "1":
            player["decisions_made"].add("Jungle")
            return True, "You carefully take the safe route."

        elif choice == "2":
            if player["energy"] <= 0:
                player["game_over"] = True
                return False, "You have no energy left."

            player["energy"] -= 1
            player["decisions_made"].add("Jungle")

            if player["energy"] == 0:
                player["game_over"] = True
                return True, "You take the shortcut but run out of energy!"

            return True, "You take the shortcut and lose 1 extra energy point."

        return False, "Invalid choice. Enter 1 or 2."

    # CAVE DECISION
    elif location == "Cave":

        if choice == "1":
            success, message = collect_item(player)

            if success:
                player["decisions_made"].add("Cave")

            return success, message

        elif choice == "2":
            player["decisions_made"].add("Cave")
            return True, "You leave the cave without collecting the Lantern."

        return False, "Invalid choice. Enter 1 or 2."

    # OLD BRIDGE DECISION
    elif location == "Old Bridge":

        if choice == "1":
            player["decisions_made"].add("Old Bridge")
            return True, "You carefully cross the bridge."

        elif choice == "2":
            if player["energy"] <= 0:
                player["game_over"] = True
                return False, "You have no energy left."

            player["energy"] -= 1
            player["decisions_made"].add("Old Bridge")

            if player["energy"] == 0:
                player["game_over"] = True
                return True, "You rush across the bridge but run out of energy!"

            return True, "You rush across the bridge and lose 1 extra energy point."

        return False, "Invalid choice. Enter 1 or 2."

    return False, "There is no decision to make at this location."