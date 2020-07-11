
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_SaveCompatibility(FGSchematic):
    mDisplayName = NSLOCTEXT("", "C8ED11FF4CAD2E8D7F6DB1894F5039CA", "Save Compatibility")
    mSchematicCategory = NewObject[SC_Logistics]()
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Fence/Recipe_Fence_01.Recipe_Fence_01_C', '/Game/FactoryGame/Recipes/Buildings/Stairs/Recipe_Stair_1b.Recipe_Stair_1b_C', '/Game/FactoryGame/Recipes/Buildings/Walls/Recipe_Wall_Window_8x4_03.Recipe_Wall_Window_8x4_03_C', '/Game/FactoryGame/Recipes/Buildings/Walls/Recipe_Wall_Window_8x4_03_Steel.Recipe_Wall_Window_8x4_03_Steel_C', '/Game/FactoryGame/Recipes/Buildings/Walls/Recipe_Wall_Conveyor_8x4_04.Recipe_Wall_Conveyor_8x4_04_C', '/Game/FactoryGame/Recipes/Buildings/Walls/Recipe_Wall_Conveyor_8x4_04_Steel.Recipe_Wall_Conveyor_8x4_04_Steel_C']}]
    
