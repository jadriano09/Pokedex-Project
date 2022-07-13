# This program will decide which Pokedex you'll work on today
# COMPLETED: Prints out which Pokedex you'll work on today

# WIP1: Parsing out each reagional dex
# IDEA WIP1: displays entires in intervals in 6, once each 6 is completed, dex will print next 6 for user to search in their given game

# WIP2: Once region is complete, remove's game from game_library list

import random

game_library = [
    "Pokemon Yellow: KANTO REGION",
    "Pokemon Platinum: SINNOH REGION EXTENDED",
    "Pokemon SoulSilver: JOHTO AND KANTO REGION",
    "Pokemon Black: UNOVA REGION",
    "Pokemon White 2: UNOVA REGION EXTENDED",
    "Pokemon Y: KALOS REGION",
    "Pokemon Alpha Saphire: HOENN REGION",
    "Pokemon Sword: GALAR REGION",
    "Pokemon Shining Pearl: SINNOH REGION",
    "Pokemon Legends Arceus: HISUI REGION"
]




todays_adventure = random.choice(game_library)
print("Today, you'll be working on", todays_adventure)
