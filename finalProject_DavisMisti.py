# ----------------------------------------------------------
# Name: Misti Davis
# Date: April 22, 2026
# Assignment: Calm Quest - A text-based python game
# Description:
# This program is a calm, text-based exploration game where
# the player manages energy and calm levels while exploring,
# resting, and using items. The game uses dictionaries to
# store player data and inventory, and includes randomness
# and time delays to enhance gameplay.
# ----------------------------------------------------------

# Import required libraries
import random   # Used for random events during exploration
import time     # Used to slow down output for a calm experience


# ----------------------------------------------------------
# FUNCTION: create_player
# Description: Creates and returns the player dictionary
# ----------------------------------------------------------
def create_player():
    return {
        "name": "Player",     # Player name
        "energy": 10,         # Energy level (changes during game)
        "calm": 10,           # Calm level (changes during game)
        "location": "Home"    # Current location
    }


# ----------------------------------------------------------
# FUNCTION: create_inventory
# Description: Creates and returns the inventory dictionary
# ----------------------------------------------------------
def create_inventory():
    return {
        "tea": 2,     # Helps increase calm
        "book": 1,    # Slight calm boost
        "shell": 0    # Found during exploration
    }


# ----------------------------------------------------------
# FUNCTION: show_status
# Description: Displays the player's current stats
# ----------------------------------------------------------
def show_status(player):
    print("\n🌿 STATUS 🌿")
    print(f"Location: {player['location']}")
    print(f"Energy: {player['energy']}")
    print(f"Calm: {player['calm']}")
    time.sleep(1)  # Pause for readability


# ----------------------------------------------------------
# FUNCTION: show_inventory
# Description: Displays all items in the inventory
# ----------------------------------------------------------
def show_inventory(inventory):
    print("\n🎒 INVENTORY 🎒")
    for item, amount in inventory.items():
        print(f"{item}: {amount}")
    time.sleep(1)


# ----------------------------------------------------------
# FUNCTION: explore
# Description: Allows the player to explore and triggers
# random events that affect stats and inventory
# ----------------------------------------------------------
def explore(player, inventory):
    print("\n🚶 Exploring...")
    time.sleep(1)

    # Change location randomly
    locations = ["Forest", "Beach", "Home"]
    player["location"] = random.choice(locations)
    print(f"📍 You are now at the {player['location']}")

    # Random event with weighted probability
    event = random.choices(
        ["find_item", "tiring", "peaceful"],
        weights=[40, 20, 40]
    )[0]

    # Event outcomes
    if event == "find_item":
        item = random.choice(list(inventory.keys()))
        inventory[item] += 1
        print(f"✨ You found a {item}!")
        player["calm"] += 1

    elif event == "tiring":
        print("😴 That took some energy.")
        player["energy"] -= 2

    elif event == "peaceful":
        print("🌊 You found a peaceful moment.")
        player["calm"] += 2


# ----------------------------------------------------------
# FUNCTION: rest
# Description: Resting restores energy and slightly increases calm
# ----------------------------------------------------------
def rest(player):
    print("\n🛌 Resting...")
    time.sleep(1)
    player["energy"] += 3
    player["calm"] += 1


# ----------------------------------------------------------
# FUNCTION: use_item
# Description: Allows the player to use an item from inventory
# ----------------------------------------------------------
def use_item(player, inventory):
    print("\nChoose an item to use:")

    # Display available items
    for item in inventory:
        print(f"- {item}")

    choice = input("> ").lower()

    # Check if item exists and player has at least one
    if choice in inventory and inventory[choice] > 0:
        inventory[choice] -= 1  # Use the item

        # Apply item effects
        if choice == "tea":
            print("🍵 You feel relaxed.")
            player["calm"] += 2

        elif choice == "book":
            print("📖 Reading is calming.")
            player["calm"] += 1

        elif choice == "shell":
            print("🐚 Listening to the ocean sound.")
            player["calm"] += 2

    else:
        print("❌ You don't have that item.")

    time.sleep(1)


# ----------------------------------------------------------
# FUNCTION: describe_calm
# Description: Gives feedback based on calm level
# ----------------------------------------------------------
def describe_calm(player):
    if player["calm"] >= 12:
        print("✨ You feel very peaceful.")
    elif player["calm"] >= 6:
        print("🙂 You feel okay.")
    else:
        print("😟 You feel a bit overwhelmed.")


# ----------------------------------------------------------
# FUNCTION: main
# Description: Controls the main game loop
# ----------------------------------------------------------
def main():
    player = create_player()         # Create player dictionary
    inventory = create_inventory()   # Create inventory dictionary
    turn = 0                         # Track number of turns

    print("🌿 Welcome to Calm Quest 🌿")

    # Main game loop
    while True:
        turn += 1
        print(f"\n🕒 Day {turn}")

        show_status(player)      # Show stats
        describe_calm(player)    # Show mood feedback

        # Menu options
        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. Rest")
        print("3. Use Item")
        print("4. Inventory")
        print("5. Quit")

        choice = input("> ")

        # Process player choice
        if choice == "1":
            explore(player, inventory)

        elif choice == "2":
            rest(player)

        elif choice == "3":
            use_item(player, inventory)

        elif choice == "4":
            show_inventory(inventory)

        elif choice == "5":
            print("🌙 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please choose 1–5.")
            continue

        # Keep stats within safe limits (0–15)
        player["energy"] = max(0, min(player["energy"], 15))
        player["calm"] = max(0, min(player["calm"], 15))

        # Win condition (goal-based ending)
        if player["calm"] >= 15:
            print("\n🌟 You reached maximum calm. You win!")
            break


# ----------------------------------------------------------
# PROGRAM ENTRY POINT
# ----------------------------------------------------------
if __name__ == "__main__":
    main()
