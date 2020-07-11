
from codegen.ue4_stub import *

from Script.FactoryGame import BreakInventoryStack
from Script.FactoryGame import SetNumItems
from Game.FactoryGame.World.Environment.Particle.PickupFoliage import PickupFoliage
from Script.FactoryGame import Default__FGInventoryLibrary
from Game.FactoryGame.World.Environment.Audio.Play_W_Pickup_Consumable_Nut import Play_W_Pickup_Consumable_Nut
from Game.FactoryGame.World.Benefit.NutBush.BP_NutBush import ExecuteUbergraph_BP_NutBush
from Script.Engine import SetHiddenInGame
from Script.Engine import HasAuthority
from Script.FactoryGame import GetItemState
from Script.FactoryGame import IsPickedUp
from Script.FactoryGame import GetPickupItems
from Script.FactoryGame import EItemState
from Script.FactoryGame import SharedInventoryStatePtr
from Script.Engine import EqualEqual_IntInt
from Game.FactoryGame.World.Benefit.BP_Edible import BP_Edible
from Game.FactoryGame.World.Benefit.NutBush.Mesh.NutBush_02 import NutBush_02
from Game.FactoryGame.World.Benefit.BP_Edible import ReceiveBeginPlay
from Script.FactoryGame import GetSavedNumItems
from Script.FactoryGame import InventoryItem
from Script.Engine import StaticMesh
from Script.FactoryGame import InventoryStack

class BP_NutBush(BP_Edible):
    mPickupEvent = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Audio/Play_W_Pickup_Consumable_Nut.Play_W_Pickup_Consumable_Nut')
    mPickupItems = Namespace(Item={'ItemClass': '/Game/FactoryGame/Resource/Environment/Nut/Desc_Nut.Desc_Nut_C', 'ItemState': {'ActorPtr': {'$Empty': True}}}, NumItems=5)
    mRespawnTimeIndays = 3
    mUpdatedOnDayNr = -1
    mItemState = EItemState::ES_NORMAL
    mGrowTimeInDays = 3
    mSavedNumItems = -1
    mMaxRespawns = -1
    bReplicates = True
    NetCullDistanceSquared = 100000
    
    def GetDestroyAudioEvent(self):
        ReturnValue = Play_W_Pickup_Consumable_Nut
    

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
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_NutBush(236)
    

    def UpdateVisiblityState(self):
        self.ExecuteUbergraph_BP_NutBush(265)
    

    def SetupItem(self):
        self.ExecuteUbergraph_BP_NutBush(659)
    

    def ExecuteUbergraph_BP_NutBush(self):
        # Label 10
        ReturnValue: int32 = self.GetSavedNumItems()
        ReturnValue_0: bool = EqualEqual_IntInt(ReturnValue, -1)
        if not ReturnValue_0:
            goto('L664')
        ReturnValue_1: InventoryStack = self.GetPickupItems()
        
        numItems = None
        item = None
        Default__FGInventoryLibrary.BreakInventoryStack(Ref[ReturnValue_1], Ref[numItems], Ref[item])
        self.SetNumItems(numItems)
        # End
        # Label 197
        ReturnValue_2: bool = self.HasAuthority()
        if not ReturnValue_2:
            goto('L664')
        goto('L10')
        self.ReceiveBeginPlay()
        self.SetupItem()
        # End
        self.StaticMesh.SetMobility(2)
        self.BushMesh.SetMobility(2)
        Variable: Ptr[StaticMesh] = NutBush_02
        ReturnValue_3: uint8 = self.GetItemState()
        Variable_0: uint8 = ReturnValue_3
        
        switch = {
            0: self.mSeedMesh,
            1: Variable
        }
        ReturnValue_4: bool = self.BushMesh.SetStaticMesh(switch.get(Variable_0, None))
        ReturnValue_5: bool = self.IsPickedUp()
        self.StaticMesh.SetHiddenInGame(ReturnValue_5, False)
        self.StaticMesh.SetMobility(0)
        self.BushMesh.SetMobility(0)
        # End
        goto('L197')
    
