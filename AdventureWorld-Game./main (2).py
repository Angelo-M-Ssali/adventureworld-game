from AdventureWorld import *
import random

# ---------- Global Variables ----------
world = None
player_location = -1
has_map = False     #Does player have the map? No = False
has_device = False  #Does player have the device? No = False
game_over = False   #Is the game done? No = False


def setup():
    """Initialize the game world and player starting position."""
    global world, player_location, has_map, has_device, game_over
    
    seed = 1121
    random.seed(seed)
    world = AdventureWorld(seed)

    unoccupied = world.get_unoccupied_locations()
    player_location = random.choice(unoccupied)

    #When the game starts, the player has nothing so the variables are set to False
    has_map = False
    has_device = False
    game_over = False

    print("=" * 60)
    print("WELCOME TO THE HUNGER GAMES ARENA")
    print("=" * 60)
    print("You have been dropped into the arena.")
    print("Find the Victory Token and capture it to win!")
    print("=" * 60)

def display_player_status():
    """Display current location, possible steps to take, and nearby warnings"""
    global world, player_location, has_map, has_device
    
    print("\n" + "-" * 60)
    print(f"📍 Current Location: District {player_location}")
    print("-" * 60)
    
    # Show inventory
    if has_map:
        print("🎒 You have: Arena Map")
    if has_device:
        print("🎒 You have: Capture Device")
    if not has_map and not has_device:
        print("🎒 Inventory: Empty")
    
    # Show available paths
    neighbors = world.get_neighbor_locations(player_location)
    print(f"\n🚶 You can move to: {neighbors}")
    
    # Show warnings
    print()  # Blank line before warnings
    if world.neighbor_has_hazard1(player_location):
        print("⚠️  WARNING: You sense deadly danger nearby!")
    
    if world.neighbor_has_hazard2(player_location):
        print("⚡ CAUTION: Something feels off about a nearby area...")
    
    if world.neighbor_has_map(player_location) and not has_map:
        print("📜 You sense something useful nearby...")
    
    if world.neighbor_has_device(player_location) and not has_device:
        print("🔧 You detect equipment nearby...")
    
    if world.neighbor_has_treasure(player_location) and has_device:
        print("🏆 You feel the Victory Token is close!")
    
    print("-" * 60)

    
    
def get_user_choice():
    """Displays menu and gets a valid user input."""

    print("\nWhat would you want to do?")
    print("1. Move")
    print("2. View Map")
    print("3. Capture Treasure")
    print("4. Quit")

    while True:
        choice = input("Enter 1-4: ")

        if choice == "1":
            return 1
        elif choice == "2":
            return 2
        elif choice == "3":
            return 3
        elif choice == "4":
            return 4
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4")

    
def process_user_choice(choice):
    """Call the right function based on user choice."""
    if choice == 1:
        do_move()
    elif choice == 2:
        show_map()
    elif choice == 3:
        capture_treasure()
    elif choice == 4:
        do_quit()


def do_move():
    global world, player_location
    
    neighbors = world.get_neighbor_locations(player_location)
    print(f"\nYou can move to: {neighbors}")
    
    user_input = input("Enter district number: ")
    
    # Check if it's a number
    if user_input.isdigit():
        destination = int(user_input)
        
        # Checks if it's a valid neighbor
        if destination in neighbors:
            player_location = destination
            print(f"\nYou move to District {player_location}...")
            check_location_effects()
        else:
            print(f"\nInvalid! You can only move to: {neighbors}")
    else:
        print("\nPlease enter a valid number!")
 


def check_location_effects():
    """Check for hazards, items, and treasure at current location."""
    global world, player_location, has_map, has_device, game_over
    
    # ============ CHECK HAZARD TYPE 1 (DEADLY) ============
    # This is checked FIRST - if true, game ends immediately
    if world.has_hazard1(player_location):
        print("\n" + "=" * 60)
        print("💀 GAME OVER - YOU DIED 💀")
        print("=" * 60)
        print("You triggered a deadly trap!")
        print("Perhaps it was tracker jackers, or poisonous gas,")
        print("or a land mine... Either way, you're dead.")
        print("The Hunger Games are over for you.")
        print("=" * 60)
        game_over = True
        return  # EXIT immediately - don't check anything else!
    
    # ============ CHECK HAZARD TYPE 2 (DISRUPTIVE) ============
    # Gamemakers interfere - teleport player and remove items
    if world.has_hazard2(player_location):
        print("\n⚡ THE GAMEMAKERS INTERVENED! ⚡")
        print("A sudden explosion rocks the arena!")
        print("You wake up confused in a different location...")
        print("Your map and device are destroyed in the explosion!")
        
        # Teleport to a random SAFE location
        safe_locations = world.get_unoccupied_locations()
        player_location = random.choice(safe_locations)
        
        # Remove ALL items
        has_map = False
        has_device = False
        
        print(f"You find yourself in District {player_location}.")
        return  # EXIT - don't check for items at this location
    
    # ============ CHECK FOR MAP ============
    # Only pick up if we don't already have it
    if world.has_map(player_location) and not has_map:
        print("\n📜 You found an ARENA MAP!")
        print("This will help you navigate and find the Victory Token.")
        has_map = True
    
    # ============ CHECK FOR CAPTURE DEVICE ============
    # Only pick up if we don't already have it
    if world.has_device(player_location) and not has_device:
        print("\n🔧 You found a CAPTURE DEVICE!")
        print("You can now detect when the Victory Token is nearby.")
        print("You'll need this to capture the token and win!")
        has_device = True
    
    # ============ CHECK FOR TREASURE (VICTORY TOKEN) ============
    if world.has_treasure(player_location):
        if has_device:
            # YOU WIN!
            print("\n" + "=" * 60)
            print("🏆 VICTORY! YOU WIN! 🏆")
            print("=" * 60)
            print("You found the Victory Token and captured it!")
            print("The cannon fires - the Games are over!")
            print("You survived the Hunger Games!")
            print("You are the VICTOR!")
            print("=" * 60)
            game_over = True
        else:
            # Can't capture without device
            print("\n✨ You sense something powerful here...")
            print("But you can't quite grasp it.")
            print("You need a Capture Device to secure the Victory Token!")


def show_map():
    """Displays the arena map IF player has it"""
    global has_map, world

    if has_map:
        print("\n" + "=" * 60)
        print("📜 ARENA MAP")
        print("=" * 60)

        print(world.get_map_ansi())

        treasure_loc = world.get_treasure_location()
        print(f"\n🏆 Victory Token Location: District {treasure_loc}")
        print("=" * 60)
    else:
        # Player doesn't have map yet
        print("\n✗ You don't have an Arena Map yet!")
        print("Explore the districts to find one.")

def capture_treasure():
    """Attempt to capture the Victory Token."""
    global has_device, world, player_location, game_over
    
    # First, check if player has the capture device
    if not has_device:
        print("\n✗ You need a Capture Device first!")
        print("Keep exploring to find one.")
        return  # Exit function early
    
    # Player has device, now check if treasure is at current location
    if world.has_treasure(player_location):
        # SUCCESS! You win!
        print("\n" + "=" * 60)
        print("🏆 VICTORY! YOU WIN! 🏆")
        print("=" * 60)
        print("You successfully captured the Victory Token!")
        print("The cannon fires - the Games are over!")
        print("You survived the Hunger Games!")
        print("You are the VICTOR!")
        print("=" * 60)
        game_over = True
    else:
        # Not at treasure location
        print("\n✗ There's no Victory Token here.")
        print("Keep exploring. Use your device to sense when you're close!")


def do_quit():
    """End the game gracefully."""
    global game_over

    print("\n" + "=" * 60)
    print("You have chosen to abandon the Hunger Games.")
    print("The gamemakers automatically execute you for cowardice...")
    print("GAME OVER")
    print("=" * 60)

    game_over = True


def main():
    """
    The main game loop.
    Give the player a simple menu to either move or quit.
    """
    global game_over
    
    setup()
    
    while not game_over:
        display_player_status()
        choice = get_user_choice()
        process_user_choice(choice)
    
    print("\nGame ended. Thanks for playing!")    
   
   
    


# ---------- Run the Program ----------
if __name__ == "__main__":
    main()
