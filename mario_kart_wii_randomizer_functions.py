from random import choice


def Small_Med_Heavy_Class_Picker():

    classes = ["Light_Weight", "Medium_Weight", "Heavy_Weight"]
    classy = choice(classes)

    # Light Characters and Vehicle Lists =======================================================================

    light_characters = ["Baby Mario", "Baby Luigi", "Baby Peach", "Baby Daisy", "Toad", "Toadette", "Koopa Troopa", "Dry Bones"]

    light_vehicles = ["Standard Bike S (Light Bike)", "Magikruiser (Bike)", "Quacker (Bike)", "Jet Bubble (Bike)", "Bit Bike",
                      "Bullet Bike (Bike)", "Standard Kart S (Kart)", "Mini Beast (Kart)", "Tiny Titan (Kart)", "Blue Falcon (Kart)",
                      "Cheep Charger (Kart)", "Booster Seat (Kart)"]

    # === Medium Characters and Vehicle Lists =================================================================

    medium_characters = ["Mario", "Luigi", "Peach", "Daisy", "Yoshi", "Birdo", "Diddy Kong", "Bowser Jr."]

    medium_vehicles = ["Standard Bike M (Medium Bike)", "Sugarscoot (Bike)", "Sneakster (Bike)", "Dolphin Dasher (Bike)", "Zip Zip (Bike)",
                       "Mach Bike (Bike)", "Standard Kart M (Medium Kart)", "Sprinter (Kart)", "Daytripper (Kart)", "Wild Wing (Kart)",
                       "Super Blooper (Kart)", "Classic Dragster (Kart)"]

    # === Heavy Characters and Vehicle Lists ===================================================================

    heavy_characters = ["Wario", "Waluigi", "Donkey Kong", "Bowser", "King Boo", "Rosalina", "Funky Kong", "Dry Bowser"]

    heavy_vehicles = ["Standard Bike L (Heavy Bike)", "Wario Bike (Bike)", "Shooting Star (Bike)", "Flame Runner (Bike)",
                      "Spear (Bike)", "Phantom (Bike)", "Standard Kart L (Heavy Kart)", "Offroader (Kart)", "Flame Flyer (Kart)",
                      "Jetsetter (Kart)", "Honeycoupe (Kart)", "Piranha Prowler (Kart)"]

    if classy == "Light_Weight":
        character_picked = choice(light_characters)
        vehicle_picked = choice(light_vehicles)
        print(character_picked)
        print(vehicle_picked)

    elif classy == "Medium_Weight":
        character_picked = choice(medium_characters)
        vehicle_picked = choice(medium_vehicles)
        print(character_picked)
        print(vehicle_picked)

    elif classy == "Heavy_Weight":
        character_picked = choice(heavy_characters)
        vehicle_picked = choice(heavy_vehicles)
        print(character_picked)
        print(vehicle_picked)
