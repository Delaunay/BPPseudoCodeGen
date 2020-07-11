﻿
from codegen.ue4_stub import *

from Script.FactoryGame import FGResearchTree

class BPD_ResearchTree_FlowerPetals(FGResearchTree):
    mPreUnlockDisplayName = NSLOCTEXT("", "541D66E04673583E82938891E04327A4", "Colored Vegetation")
    mDisplayName = NSLOCTEXT("", "0FF6E3954D6FA4A3B41F5783982EADE8", "Flower Petals")
    mPreUnlockDescription = NSLOCTEXT("", "D0EBC2C748539AC0DC5098B7805C7C50", "Initial planetary-scans have revealed that vegetation with coloring properties might be present on the plant. Field research is needed to acquire samples.")
    mPostUnlockDescription = NSLOCTEXT("", "B1EE024148492249E3CBA4A7E6827A23", "The Flower Petals, found in a variety of vegetation on Massage-2(AB)b, were found to have strong coloring properties which might be used to produce dyes.")
    mUnlockDependencies = [{'$ObjectClass': '/Game/FactoryGame/AvailabilityDependencies/BP_ItemPickedUpDependency.BP_ItemPickedUpDependency_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_ItemPickedUpDependency_C_0', 'mItems': ['/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_FlowerPetals.Desc_FlowerPetals_C']}]
    mNodes = [{'$ObjectClass': '/Game/FactoryGame/Schematics/Research/BPD_ResearchTreeNode.BPD_ResearchTreeNode_C', '$ObjectFlags': 2621442, '$ObjectName': 'BPD_ResearchTreeNode_C_0', 'mNodeDataStruct': {'Schematic_27_3663A42446FDB4387D0C81AFC23E225B': '/Game/FactoryGame/Schematics/Research/FlowerPetals_RS/Research_FlowerPetals_3.Research_FlowerPetals_3_C', 'Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292': {'X_2_3FF107F84D30EB52DD50898C7D2CAD67': 3, 'Y_4_F18C5B824136D7759146338CAA496F0A': 2}, 'Parents_20_7A099B96409362536B743BA1CC77C234': [{'X_2_3FF107F84D30EB52DD50898C7D2CAD67': 3, 'Y_4_F18C5B824136D7759146338CAA496F0A': 1}], 'UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63': [{'X_2_3FF107F84D30EB52DD50898C7D2CAD67': 3}]}}, {'$ObjectClass': '/Game/FactoryGame/Schematics/Research/BPD_ResearchTreeNode.BPD_ResearchTreeNode_C', '$ObjectFlags': 2621442, '$ObjectName': 'BPD_ResearchTreeNode_C_1', 'mNodeDataStruct': {'Schematic_27_3663A42446FDB4387D0C81AFC23E225B': '/Game/FactoryGame/Schematics/Research/FlowerPetals_RS/Research_FlowerPetals_1.Research_FlowerPetals_1_C', 'Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292': {'X_2_3FF107F84D30EB52DD50898C7D2CAD67': 3}, 'ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A': [{'Key': {'X_2_3FF107F84D30EB52DD50898C7D2CAD67': 3, 'Y_4_F18C5B824136D7759146338CAA496F0A': 1}, 'Value': {'Points_10_9533B9104470D8E053E7ACA5C4C9F865': [{'X_2_3FF107F84D30EB52DD50898C7D2CAD67': 3, 'Y_4_F18C5B824136D7759146338CAA496F0A': 1}]}}], 'NodesToUnhide_33_A6E465554D49C98EE2A0ECB493BE5CBA': [{'X_2_3FF107F84D30EB52DD50898C7D2CAD67': 3, 'Y_4_F18C5B824136D7759146338CAA496F0A': 1}, {'X_2_3FF107F84D30EB52DD50898C7D2CAD67': 3, 'Y_4_F18C5B824136D7759146338CAA496F0A': 2}]}}, {'$ObjectClass': '/Game/FactoryGame/Schematics/Research/BPD_ResearchTreeNode.BPD_ResearchTreeNode_C', '$ObjectFlags': 2621442, '$ObjectName': 'BPD_ResearchTreeNode_C_2', 'mNodeDataStruct': {'Schematic_27_3663A42446FDB4387D0C81AFC23E225B': '/Game/FactoryGame/Schematics/Research/FlowerPetals_RS/Research_FlowerPetals_2.Research_FlowerPetals_2_C', 'Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292': {'X_2_3FF107F84D30EB52DD50898C7D2CAD67': 3, 'Y_4_F18C5B824136D7759146338CAA496F0A': 1}, 'Parents_20_7A099B96409362536B743BA1CC77C234': [{'X_2_3FF107F84D30EB52DD50898C7D2CAD67': 3}], 'ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A': [{'Key': {'X_2_3FF107F84D30EB52DD50898C7D2CAD67': 3, 'Y_4_F18C5B824136D7759146338CAA496F0A': 2}, 'Value': {'Points_10_9533B9104470D8E053E7ACA5C4C9F865': [{'X_2_3FF107F84D30EB52DD50898C7D2CAD67': 3, 'Y_4_F18C5B824136D7759146338CAA496F0A': 2}]}}], 'UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63': [{'X_2_3FF107F84D30EB52DD50898C7D2CAD67': 3}]}}]
    
