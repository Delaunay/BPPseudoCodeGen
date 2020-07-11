
from codegen.ue4_stub import *

from Game.FactoryGame.Prototype.WAT.Audio.Play_WeirdAlienThing_VO import Play_WeirdAlienThing_VO
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Resource.BP_Pickup import BP_Pickup
from Game.FactoryGame.Prototype.WAT.BP_WAT1 import ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_OtherComp1
from Game.FactoryGame.Prototype.WAT.BP_WAT1 import ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_OtherComp
from Game.FactoryGame.Prototype.WAT.BP_WAT1 import ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_OverlappedComponent1
from Game.FactoryGame.Prototype.WAT.BP_WAT1 import ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_OverlappedComponent
from Game.FactoryGame.Prototype.WAT.BP_WAT1 import ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_OtherBodyIndex
from Script.FactoryGame import FGVehicle
from Game.FactoryGame.Prototype.WAT.BP_WAT1 import ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_OtherActor
from Game.FactoryGame.Prototype.WAT.Audio.Stop_WeirdAlienThing_VO import Stop_WeirdAlienThing_VO
from Game.FactoryGame.Prototype.WAT.BP_WAT1 import ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_OtherActor1
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Prototype.WAT.BP_WAT1 import ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_bFromSweep
from Script.FactoryGame import LostSignificance
from Game.FactoryGame.Prototype.WAT.BP_WAT1 import ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_SweepResult
from Game.FactoryGame.Prototype.WAT.BP_WAT1 import ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_OtherBodyIndex1
from Script.AkAudio import AkComponent
from Script.FactoryGame import GainedSignificance
from Game.FactoryGame.Prototype.WAT.BP_WAT1 import ExecuteUbergraph_BP_WAT1

class BP_WAT1(BP_Pickup):
    mPickupEvent = Namespace(AssetPath='/Game/FactoryGame/Prototype/WAT/Audio/Play_ResourcePickup_WAT.Play_ResourcePickup_WAT')
    mAddToSignificanceManager = True
    mTimeToPickUp = 5
    mPickupItems = Namespace(Item={'ItemClass': '/Game/FactoryGame/Prototype/WAT/Desc_WAT1.Desc_WAT1_C', 'ItemState': {'ActorPtr': {'$Empty': True}}}, NumItems=1)
    mDestroyOnPickup = True
    mAudioEvent = Namespace(AssetPath='/Game/FactoryGame/Prototype/WAT/Audio/Play_WeirdAlienThing_Loop.Play_WeirdAlienThing_Loop')
    mRespawnTimeIndays = -1
    mUpdatedOnDayNr = -1
    mItemState = EItemState::ES_NORMAL
    mGrowTimeInDays = 3
    mSavedNumItems = -1
    mMaxRespawns = -1
    bReplicates = True
    RemoteRole = 1
    
    def BndEvt__Sphere1_K2Node_ComponentBoundEvent_0_ComponentBeginOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32, bFromSweep: bool, SweepResult: Const[Ref[HitResult]]):
        ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_OverlappedComponent1 = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_OtherActor1 = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_OtherComp1 = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_OtherBodyIndex1 = OtherBodyIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_bFromSweep = bFromSweep #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_SweepResult = SweepResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WAT1(289)
    

    def BndEvt__Sphere1_K2Node_ComponentBoundEvent_1_ComponentEndOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32):
        ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_OverlappedComponent = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_OtherActor = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_WAT1.K2Node_ComponentBoundEvent_OtherBodyIndex = OtherBodyIndex #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WAT1(10)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_BP_WAT1(457)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_BP_WAT1(510)
    

    def ExecuteUbergraph_BP_WAT1(self):
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](OtherActor)
        bSuccess1: bool = Player
        if not bSuccess1:
            goto('L147')
        # Label 89
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_WeirdAlienThing_VO, self, True)
        # End
        # Label 147
        AsFGVehicle: Ptr[FGVehicle] = Cast[FGVehicle](OtherActor)
        bSuccess: bool = AsFGVehicle
        if not bSuccess:
            goto('L558')
        goto('L89')
        # Label 231
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_WeirdAlienThing_VO, self, True)
        # End
        Player1: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](OtherActor1)
        bSuccess3: bool = Player1
        if not bSuccess3:
            goto('L373')
        goto('L231')
        # Label 373
        AsFGVehicle1: Ptr[FGVehicle] = Cast[FGVehicle](OtherActor1)
        bSuccess2: bool = AsFGVehicle1
        if not bSuccess2:
            goto('L558')
        goto('L231')
        self.GainedSignificance()
        self.Sphere1.SetCollisionEnabled(1)
        # End
        self.LostSignificance()
        self.Sphere1.SetCollisionEnabled(0)
    
