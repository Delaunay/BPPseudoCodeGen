
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_4-2(FGSchematic):
    mType = ESchematicType::EST_Milestone
    mDisplayName = NSLOCTEXT("", "E406F9054F8F6719B22B86A8CBF4D082", "Improved Melee Combat")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 4
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Rotor/Desc_Rotor.Desc_Rotor_C', 'amount': 25}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 1500}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 200}]
    mTimeToComplete = 180
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Equipment/Recipe_XenoBasher.Recipe_XenoBasher_C']}, {'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockInventorySlot.BP_UnlockInventorySlot_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockInventorySlot_C_0', 'mNumInventorySlotsToUnlock': 5}, {'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockArmEquipmentSlot.BP_UnlockArmEquipmentSlot_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockArmEquipmentSlot_C_0', 'mNumArmEquipmentSlotsToUnlock': 1}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Equipment.SchematicIcon_Equipment'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
