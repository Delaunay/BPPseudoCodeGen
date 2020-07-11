
from codegen.ue4_stub import *

from Script.FactoryGame import SetNumItems
from Game.FactoryGame.World.Environment.Particle.PickupFoliage import PickupFoliage
from Script.Engine import K2_SetTimer
from Script.Engine import SetHiddenInGame
from Script.Engine import HasAuthority
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetItemState
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import IsPickedUp
from Script.Engine import TimerHandle
from Script.FactoryGame import EItemState
from Script.FactoryGame import SharedInventoryStatePtr
from Script.Engine import EqualEqual_IntInt
from Game.FactoryGame.World.Environment.Audio.Play_W_Pickup_Consumable_Foliage_Leaf import Play_W_Pickup_Consumable_Foliage_Leaf
from Game.FactoryGame.World.Benefit.BP_Edible import BP_Edible
from Script.Engine import FlushNetDormancy
from Game.FactoryGame.World.Benefit.BP_Edible import ReceiveBeginPlay
from Game.FactoryGame.World.Benefit.BerryBush.BerryAlternatives import BerryAlternatives
from Script.Engine import RandomIntegerInRange
from Script.FactoryGame import InventoryItem
from Game.FactoryGame.World.Benefit.BerryBush.BP_BerryBush import ExecuteUbergraph_BP_BerryBush
from Script.FactoryGame import InventoryStack

class BP_BerryBush(BP_Edible):
    mBerryVariation: List[BerryAlternatives] = [{'NumBerries_3_04E44FA44B4EA4BA85E390AD49D0182C': 2, 'BushMesh_5_7036F8324BB7951F7ADED7B09E41EE3B': {'$AssetPath': '/Game/FactoryGame/World/Benefit/BerryBush/Mesh/BerryFlower.BerryFlower'}, 'BerryMesh_7_592ECE8B4AB42BAD1230AEB74FF3C661': {'$AssetPath': '/Game/FactoryGame/World/Benefit/BerryBush/Mesh/Berries_01.Berries_01'}}, {'NumBerries_3_04E44FA44B4EA4BA85E390AD49D0182C': 1, 'BushMesh_5_7036F8324BB7951F7ADED7B09E41EE3B': {'$AssetPath': '/Game/FactoryGame/World/Benefit/BerryBush/Mesh/BerryFlower_02.BerryFlower_02'}, 'BerryMesh_7_592ECE8B4AB42BAD1230AEB74FF3C661': {'$AssetPath': '/Game/FactoryGame/World/Benefit/BerryBush/Mesh/Berries_02.Berries_02'}}, {'NumBerries_3_04E44FA44B4EA4BA85E390AD49D0182C': 3, 'BushMesh_5_7036F8324BB7951F7ADED7B09E41EE3B': {'$AssetPath': '/Game/FactoryGame/World/Benefit/BerryBush/Mesh/BerryFlower_03.BerryFlower_03'}, 'BerryMesh_7_592ECE8B4AB42BAD1230AEB74FF3C661': {'$AssetPath': '/Game/FactoryGame/World/Benefit/BerryBush/Mesh/Berries_03.Berries_03'}}]
    mLockVariation: bool
    mBerryIndex: int32 = -1
    mPickupEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/Play_W_Pickup_Consumable_Berries.Play_W_Pickup_Consumable_Berries')
    mPickupItems = Namespace(Item={'ItemClass': '/Game/FactoryGame/Resource/Environment/Berry/Desc_Berry.Desc_Berry_C', 'ItemState': {'ActorPtr': {'$Empty': True}}}, NumItems=3)
    mRespawnTimeIndays = 3
    mUpdatedOnDayNr = -1
    mItemState = EItemState::ES_NORMAL
    mGrowTimeInDays = 3
    mSavedNumItems = -1
    mMaxRespawns = -1
    bReplicates = True
    
    def GetDestroyAudioEvent(self):
        ReturnValue = Play_W_Pickup_Consumable_Foliage_Leaf
    

    def GetDestroyEffect(self):
        ReturnValue = PickupFoliage
    

    def GetForceThreshold(self):
        ReturnValue = 500
    

    def GetActorChainsawReturn(self):
        ReturnValue = InventoryStack(Item = InventoryItem(ItemClass = None, ItemState = SharedInventoryStatePtr(ActorPtr = None)), NumItems = 0)
    

    def GetMeshComponent(self):
        ReturnValue = self.BushMesh
    

    def IsChainsawable(self):
        ReturnValue = True
    

    def SetupNumBerries(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L326')
        ReturnValue_0: bool = EqualEqual_IntInt(self.mBerryIndex, -1)
        if not ReturnValue_0:
            goto('L307')
        self.FlushNetDormancy()
        
        ReturnValue_1: int32 = len(self.mBerryVariation) - 1
        ReturnValue_2: int32 = RandomIntegerInRange(0, ReturnValue_1)
        self.mBerryIndex = ReturnValue_2
        
        Item = None
        Item = self.mBerryVariation[self.mBerryIndex]
        self.SetNumItems(Item.NumBerries_3_04E44FA44B4EA4BA85E390AD49D0182C)
        # Label 307
        self.SetupMesh()
        # End
        # Label 326
        ReturnValue_3: bool = self.mBerryIndex != -1
        if not ReturnValue_3:
            goto('L379')
        goto('L307')
        # Label 379
        ReturnValue_4: TimerHandle = Default__KismetSystemLibrary.K2_SetTimer(self, "SetupNumBerries", 0.10000000149011612, False)
    

    def SetupMesh(self):
        self.StaticMesh.SetMobility(2)
        self.BushMesh.SetMobility(2)
        
        Item = None
        Item = self.mBerryVariation[self.mBerryIndex]
        ReturnValue: uint8 = self.GetItemState()
        Variable: uint8 = ReturnValue
        
        switch = {
            0: self.mSeedMesh,
            1: Item.BushMesh_5_7036F8324BB7951F7ADED7B09E41EE3B
        }
        ReturnValue_0: bool = self.BushMesh.SetStaticMesh(switch.get(Variable, None))
        
        Item1 = None
        Item1 = self.mBerryVariation[self.mBerryIndex]
        ReturnValue1: bool = self.StaticMesh.SetStaticMesh(Item1.BerryMesh_7_592ECE8B4AB42BAD1230AEB74FF3C661)
        self.StaticMesh.SetMobility(0)
        self.BushMesh.SetMobility(0)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_BerryBush(91)
    

    def UpdateVisiblityState(self):
        self.ExecuteUbergraph_BP_BerryBush(120)
    

    def ExecuteUbergraph_BP_BerryBush(self):
        # Label 10
        self.SetupMesh()
        ReturnValue: bool = self.IsPickedUp()
        self.StaticMesh.SetHiddenInGame(ReturnValue, False)
        # End
        self.ReceiveBeginPlay()
        self.SetupNumBerries()
        # End
        goto('L10')
    
