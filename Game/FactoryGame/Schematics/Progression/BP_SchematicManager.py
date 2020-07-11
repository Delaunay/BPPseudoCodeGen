
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematicManager

class BP_SchematicManager(FGSchematicManager):
    mPurchasedSchematics = ['/Game/FactoryGame/Schematics/Schematic_StartingRecipes.Schematic_StartingRecipes_C']
    mShipLandTimeStamp = -1
    mHasTechTierLimit = True
    mMaxAllowedTechTier = 7
    mShipReturnedMessage = NewObject[Widget_ShipReturnMessage]()
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0.10000000149011612, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bAlwaysRelevant = True
    bReplicates = True
    RemoteRole = 1
    
