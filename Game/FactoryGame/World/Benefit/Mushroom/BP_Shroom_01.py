
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import RandomIntegerInRange
from Game.FactoryGame.World.Environment.Audio.Play_W_Pickup_Consumable_Foliage_Leaf import Play_W_Pickup_Consumable_Foliage_Leaf
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.World.Benefit.BP_Edible import BP_Edible
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Game.FactoryGame.World.Environment.Particle.PickupFoliage import PickupFoliage
from Script.Engine import UserConstructionScript
from Script.Engine import K2_SetWorldLocation
from Script.Engine import LineTraceSingle
from Script.Engine import StaticMesh
from Script.CoreUObject import LinearColor

class BP_Shroom_01(BP_Edible):
    mMeshAlternatives: List[Ptr[StaticMesh]] = [{'$AssetPath': '/Game/FactoryGame/World/Environment/Swamp/EdibleMushroom/Mesh/EdibleMushroom_01.EdibleMushroom_01'}, {'$AssetPath': '/Game/FactoryGame/World/Environment/Swamp/EdibleMushroom/Mesh/EdibleMushroom_02.EdibleMushroom_02'}]
    mPickupEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/Play_W_Pickup_Consumable_Shroom.Play_W_Pickup_Consumable_Shroom')
    mPickupItems = Namespace(Item={'ItemClass': '/Game/FactoryGame/Resource/Environment/DesertShroom/Desc_Shroom.Desc_Shroom_C', 'ItemState': {'ActorPtr': {'$Empty': True}}}, NumItems=1)
    mDestroyOnPickup = True
    mRespawnTimeIndays = -1
    mUpdatedOnDayNr = -1
    mItemState = EItemState::ES_NORMAL
    mGrowTimeInDays = 3
    mSavedNumItems = -1
    mMaxRespawns = -1
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=False, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    
    def GetDestroyAudioEvent(self):
        ReturnValue = Play_W_Pickup_Consumable_Foliage_Leaf
    

    def GetDestroyEffect(self):
        ReturnValue = PickupFoliage
    

    def GetForceThreshold(self):
        ReturnValue = 100
    

    def UserConstructionScript(self):
        self.UserConstructionScript()
        
        ReturnValue: int32 = len(self.mMeshAlternatives) - 1
        ReturnValue_0: int32 = RandomIntegerInRange(0, ReturnValue)
        
        Item = None
        Item = self.mMeshAlternatives[ReturnValue_0]
        ReturnValue_1: bool = self.StaticMesh.SetStaticMesh(Item)
        ReturnValue_2: Vector = self.K2_GetActorLocation()
        ReturnValue_3: Vector = Subtract_VectorVector(ReturnValue_2, Vector(0, 0, 100))
        ReturnValue_4: Vector = ReturnValue_2 + Vector(0, 0, 100)
        
        Variable = None
        OutHit = None
        ReturnValue_5: bool = Default__KismetSystemLibrary.LineTraceSingle(self, ReturnValue_4, ReturnValue_3, 0, False, 0, True, LinearColor(R = 1, G = 0, B = 0, A = 1), LinearColor(R = 0, G = 1, B = 0, A = 1), 5, Ref[Variable], Ref[OutHit])
        if not False:
            goto('L573')
        
        SweepHitResult = None
        self.StaticMesh.K2_SetWorldLocation(Vector(0, 0, 0), False, False, Ref[SweepHitResult])
    
