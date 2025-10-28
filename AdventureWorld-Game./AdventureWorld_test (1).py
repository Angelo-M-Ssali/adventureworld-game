# ------------------------------------------------------------
# Demonstration of AdventureWorld class usage
# ------------------------------------------------------------
# Assumes: from AdventureWorld import AdventureWorld
from AdventureWorld import *

def main():
    """Demonstrate AdventureWorld methods grouped by naming pattern, with return types."""

    seed = 1121
    W = AdventureWorld(seed)

    print("=== AdventureWorld Demonstration ===\n")

    # ---------- World summary ----------
    print("print(world) shows a summary of world data, useful for debugging during development):")
    print(W)

    # We'll test everything from the perspective of one location
    loc = 1
    print(f"\n--- Testing from location {loc} ---")

    # ---------- HAS_[THING] --> bool methods ----------
    print("\nHAS_[THING] --> bool methods (check if something is *at* this location):")
    print(f"  has_hazard1({loc})  --> bool: {W.has_hazard1(loc)}")
    print(f"  has_hazard2({loc})  --> bool: {W.has_hazard2(loc)}")
    print(f"  has_treasure({loc}) --> bool: {W.has_treasure(loc)}")
    print(f"  has_map({loc})      --> bool: {W.has_map(loc)}")
    print(f"  has_device({loc})   --> bool: {W.has_device(loc)}")

    # ---------- NEIGHBOR_HAS_[THING] --> bool methods ----------
    print("\nNEIGHBOR_HAS_[THING] --> bool methods (check if something is *one location away*):")
    print(f"  neighbor_has_hazard1({loc})  --> bool: {W.neighbor_has_hazard1(loc)}")
    print(f"  neighbor_has_hazard2({loc})  --> bool: {W.neighbor_has_hazard2(loc)}")
    print(f"  neighbor_has_treasure({loc}) --> bool: {W.neighbor_has_treasure(loc)}")
    print(f"  neighbor_has_map({loc})      --> bool: {W.neighbor_has_map(loc)}")
    print(f"  neighbor_has_device({loc})   --> bool: {W.neighbor_has_device(loc)}")

    # ---------- GET_[THING] --> int or list[int] ----------
    print("\nGET_[THING] --> int or list[int] methods (direct lookup or retrieve information):")
    print(f"  get_treasure_location() --> int: {W.get_treasure_location()}")
    print(f"  get_map_location()      --> int: {W.get_map_location()}")
    print(f"  get_device_location()   --> int: {W.get_device_location()}")
    print(f"  get_neighbor_locations({loc}) --> list[int]: {W.get_neighbor_locations(loc)}")
    print(f"  get_unoccupied_locations()     --> list[int]: {W.get_unoccupied_locations()}")

    # ---------- GET_[MAP] --> str methods ----------
    print("\nGET_[MAP] methods (return a string representation of the map):")
    print("  get_map_ascii() --> str:")
    print(W.get_map_ascii())
    print("\n  get_map_ansi() --> str (with colors and symbols):")
    print(W.get_map_ansi())

    # ---------- SET Treasure location---
    print("\nset_treasure_location(loc) allows you to move the treasure.")
    print(f"  BEFORE get_treasure_location() --> int: {W.get_treasure_location()}")
    locs = W.get_unoccupied_locations()
    W.set_treasure_location(random.choice(locs))
    print(f"  AFTER get_treasure_location() --> int: {W.get_treasure_location()}")
    print("\n=== End of Demonstration ===")


if __name__ == "__main__":
    main()