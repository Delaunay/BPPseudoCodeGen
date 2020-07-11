
from codegen.ue4_stub import *

from Script.FactoryGame import FGSuitBaseAttachment

class Attach_HazmatSuit(FGSuitBaseAttachment):
    mSuit3PMeshMaterials = [{'SlotName': 'Body_Details', 'Material': {'$AssetPath': '/Game/FactoryGame/Character/Player/Material/MI_Haz_Body_Details.MI_Haz_Body_Details'}}, {'SlotName': 'Body_01', 'Material': {'$AssetPath': '/Game/FactoryGame/Character/Player/Material/MI_Haz_Body_01.MI_Haz_Body_01'}}, {'SlotName': 'Body_02', 'Material': {'$AssetPath': '/Game/FactoryGame/Character/Player/Material/MI_Haz_Body_02.MI_Haz_Body_02'}}, {'SlotName': 'Body_Hands', 'Material': {'$AssetPath': '/Game/FactoryGame/Character/Player/Material/MI_Haz_Body_Hands.MI_Haz_Body_Hands'}}, {'SlotName': 'Body_Backpack', 'Material': {'$AssetPath': '/Game/FactoryGame/Character/Player/Material/MI_Haz_Body_Backpack.MI_Haz_Body_Backpack'}}, {'SlotName': 'Helmet', 'Material': {'$Empty': True}}]
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
