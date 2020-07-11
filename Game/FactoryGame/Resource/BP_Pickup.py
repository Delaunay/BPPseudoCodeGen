
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.FactoryGame import ShowOutline
from Game.FactoryGame.Resource.BP_Pickup import ExecuteUbergraph_BP_Pickup.K2Node_Event_state1
from Script.FactoryGame import StartIsLookedAt
from Game.FactoryGame.Resource.BP_Pickup import ExecuteUbergraph_BP_Pickup.K2Node_Event_byCharacter
from Script.FactoryGame import StopIsLookedAt
from Script.FactoryGame import AddGainSignificanceObjectToSignificanceManager
from Script.Engine import ReceiveBeginPlay
from Game.FactoryGame.Resource.BP_Pickup import ExecuteUbergraph_BP_Pickup.K2Node_Event_state
from Script.FactoryGame import FGItemPickup
from Script.FactoryGame import PlayPickupEffect
from Script.FactoryGame import HideOutline
from Script.AkAudio import AkAudioEvent
from Game.FactoryGame.Resource.BP_Pickup import ExecuteUbergraph_BP_Pickup.K2Node_Event_EndPlayReason
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Resource.BP_Pickup import ExecuteUbergraph_BP_Pickup.K2Node_Event_byCharacter1
from Script.Engine import ReceiveEndPlay
from Game.FactoryGame.Resource.BP_Pickup import ExecuteUbergraph_BP_Pickup
from Script.FactoryGame import RemoveGainSignificanceObjectFromSignificanceManager
from Script.AkAudio import AkComponent

class BP_Pickup(FGItemPickup):
    mPickupEvent: Ptr[AkAudioEvent] = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/Play_P_ResourcePickUp.Play_P_ResourcePickUp')
    mDesiredGainSignificanceDistance: float = 8000
    mAddToSignificanceManager: bool
    mPickupItems = Namespace(Item={'ItemClass': 'None', 'ItemState': {'ActorPtr': {'$Empty': True}}}, NumItems=1)
    mDestroyOnPickup = True
    mRespawnTimeIndays = -1
    mUpdatedOnDayNr = -1
    mItemState = EItemState::ES_NORMAL
    mGrowTimeInDays = 3
    mSavedNumItems = -1
    mMaxRespawns = -1
    bReplicates = True
    
    def PlayPickupEffect(self):
        self.ExecuteUbergraph_BP_Pickup(63)
    

    def StartIsLookedAt(self):
        ExecuteUbergraph_BP_Pickup.K2Node_Event_byCharacter1 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Pickup.K2Node_Event_state1 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Pickup(131)
    

    def StopIsLookedAt(self):
        ExecuteUbergraph_BP_Pickup.K2Node_Event_byCharacter = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Pickup.K2Node_Event_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Pickup(207)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_Pickup(281)
    

    def ReceiveEndPlay(self):
        ExecuteUbergraph_BP_Pickup.K2Node_Event_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Pickup(353)
    

    def ExecuteUbergraph_BP_Pickup(self):
        # Label 10
        if not self.mAddToSignificanceManager:
            goto('L377')
        Default__FGBlueprintFunctionLibrary.RemoveGainSignificanceObjectFromSignificanceManager(self, self)
        # End
        self.PlayPickupEffect()
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mPickupEvent, self, True)
        # End
        
        state1 = None
        self.StartIsLookedAt(byCharacter1, Ref[state1])
        Default__FGBlueprintFunctionLibrary.ShowOutline(self.StaticMesh, 252)
        # End
        
        state = None
        self.StopIsLookedAt(byCharacter, Ref[state])
        Default__FGBlueprintFunctionLibrary.HideOutline(self.StaticMesh)
        # End
        self.ReceiveBeginPlay()
        if not self.mAddToSignificanceManager:
            goto('L377')
        Default__FGBlueprintFunctionLibrary.AddGainSignificanceObjectToSignificanceManager(self, self, self.mDesiredGainSignificanceDistance)
        # End
        self.ReceiveEndPlay(EndPlayReason)
        goto('L10')
    
