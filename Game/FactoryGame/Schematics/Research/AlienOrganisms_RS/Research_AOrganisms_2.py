
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Research_AOrganisms_2(FGSchematic):
    mType = ESchematicType::EST_MAM
    mDisplayName = NSLOCTEXT("", "BEC109E14F10185B93428B84A389048A", "Hostile Organism Detection")
    mSchematicCategory = NewObject[SC_Organisation]()
    mTechTier = 3
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AnimalParts/Desc_SpitterParts.Desc_SpitterParts_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/AnimalParts/Desc_HogParts.Desc_HogParts_C', 'amount': 5}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Equipment/ObjectScanner/Icons/Monsters_256.Monsters_256'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
