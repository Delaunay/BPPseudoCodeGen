
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import RestoreAudioSourceToOriginalLocation
from Game.FactoryGame.Equipment.Hookshot.Equip_Hookshot import ExecuteUbergraph_Equip_Hookshot.K2Node_Event_attachedToSomething
from Script.FactoryGame import MoveAudioSourceInFrontOfPlayer
from Script.AkAudio import SetActorRTPCValue
from Game.FactoryGame.Equipment.Hookshot.Equip_Hookshot import ExecuteUbergraph_Equip_Hookshot
from Script.Engine import Pawn
from Game.FactoryGame.Equipment.Hookshot.Equip_Hookshot import ExecuteUbergraph_Equip_Hookshot.K2Node_Event_DeltaSeconds
from Script.Engine import GetInstigator
from Script.Engine import VSize
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import ReceiveTick
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import GetItemName
from Script.Engine import IsValid
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import FGHookshot
from Game.FactoryGame.Equipment.Hookshot.Equip_Hookshot import ExecuteUbergraph_Equip_Hookshot.K2Node_Event_hitResult
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.Equipment.Hookshot.Audio.Stop_EQ_HookShot_Fire import Stop_EQ_HookShot_Fire
from Script.CoreUObject import Vector
from Game.FactoryGame.Equipment.Hookshot.Equip_Hookshot import ExecuteUbergraph_Equip_Hookshot.K2Node_Event_Hit
from Script.Engine import BreakHitResult
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.Hookshot.Audio.Play_EQ_HookShot_Impact import Play_EQ_HookShot_Impact
from Script.FactoryGame import Default__FGItemDescriptor
from Game.FactoryGame.Equipment.Hookshot.Audio.Stop_EQ_HookShot_Wind import Stop_EQ_HookShot_Wind
from Game.FactoryGame.Equipment.Hookshot.Audio.Play_EQ_HookShot_Fire import Play_EQ_HookShot_Fire
from Script.AkAudio import AkComponent
from Script.FactoryGame import OwnerLanded
from Script.Engine import PrintString
from Game.FactoryGame.Equipment.Hookshot.Audio.Play_EQ_HookShot_Wind import Play_EQ_HookShot_Wind
from Script.CoreUObject import LinearColor

class Equip_Hookshot(FGHookshot):
    mMaxHookDistance = 20000
    mAccelRate = 3600
    mBrakeAccelRate = 2500
    mHookshotAudio = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'Scene'}, ObjectClass='/Script/AkAudio.AkComponent', ObjectFlags=2883617, ObjectName='HookshotAudio', RelativeLocation={'X': 120, 'Y': 0, 'Z': 0})
    mAttachmentClass = NewObject[Attach_Hookshot]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mEquipSound = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/Play_P_ResourcePickUp.Play_P_ResourcePickUp')
    mAttachSocket = EquipmentGripR
    mCostToUse = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronScrew/Desc_IronScrew.Desc_IronScrew_C', 'amount': 1}]
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='Scene')
    
    def ReceiveTick(self):
        ExecuteUbergraph_Equip_Hookshot.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_Hookshot(681)
    

    def OnFire(self):
        ExecuteUbergraph_Equip_Hookshot.K2Node_Event_attachedToSomething = attachedToSomething #  PERSISTENT_FRAME(
        ExecuteUbergraph_Equip_Hookshot.K2Node_Event_hitResult = HitResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_Hookshot(1003)
    

    def OwnerLanded(self):
        ExecuteUbergraph_Equip_Hookshot.K2Node_Event_Hit = Hit #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_Hookshot(1410)
    

    def OnWireDetach(self):
        self.ExecuteUbergraph_Equip_Hookshot(1499)
    

    def DidNotAffordUse(self):
        self.ExecuteUbergraph_Equip_Hookshot(1581)
    

    def ExecuteUbergraph_Equip_Hookshot(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L290")
        
        Item = None
        Item = self.mCostToUse[Variable]
        ReturnValue: FText = Default__FGItemDescriptor.GetItemName(Item.ItemClass)
        
        ReturnValue_0: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue])
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_0, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
        # Label 290
        ReturnValue_1: int32 = Variable + 1
        Variable: int32 = ReturnValue_1
        
        # Label 359
        ReturnValue_2: int32 = len(self.mCostToUse)
        ReturnValue_3: bool = Variable <= ReturnValue_2
        if not ReturnValue_3:
            goto('L502')
        Variable = Variable
        goto('L15')
        # Label 502
        Default__KismetSystemLibrary.PrintString(self, "You couldn't afford to use the hookshot.
You need:", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
        # Label 630
        Variable = 0
        Variable = 0
        goto('L359')
        self.ReceiveTick(DeltaSeconds)
        ReturnValue1: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        ReturnValue1 = self.GetInstigator()
        ReturnValue_5: Vector = ReturnValue1.GetVelocity()
        ReturnValue_6: float = VSize(ReturnValue_5)
        ReturnValue_7: float = ReturnValue_6 / 100
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_HookShotWind", ReturnValue_7, 0, ReturnValue1)
        goto(ExecutionFlow.Pop())
        if not attachedToSomething:
           goto(ExecutionFlow.Pop())
        self.MoveAudioSourceInFrontOfPlayer()
        
        hitResult = None
        bBlockingHit = None
        bInitialOverlap = None
        Time = None
        Distance = None
        Location = None
        ImpactPoint = None
        Normal = None
        ImpactNormal = None
        PhysMat = None
        HitActor = None
        HitComponent = None
        HitBoneName = None
        HitItem = None
        FaceIndex = None
        TraceStart = None
        TraceEnd = None
        Default__GameplayStatics.BreakHitResult(Ref[hitResult], Ref[bBlockingHit], Ref[bInitialOverlap], Ref[Time], Ref[Distance], Ref[Location], Ref[ImpactPoint], Ref[Normal], Ref[ImpactNormal], Ref[PhysMat], Ref[HitActor], Ref[HitComponent], Ref[HitBoneName], Ref[HitItem], Ref[FaceIndex], Ref[TraceStart], Ref[TraceEnd])
        ReturnValue_8: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_HookShot_Impact, HitActor, True)
        ReturnValue_9: Ptr[Pawn] = self.GetInstigator()
        ReturnValue4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_HookShot_Fire, ReturnValue_9, True)
        ReturnValue1_0: int32 = self.mHookshotAudio.PostAkEvent(Play_EQ_HookShot_Wind)
        goto(ExecutionFlow.Pop())
        
        Hit = None
        self.OwnerLanded(Ref[Hit])
        self.RestoreAudioSourceToOriginalLocation()
        ReturnValue2: int32 = self.mHookshotAudio.PostAkEvent(Stop_EQ_HookShot_Wind)
        goto(ExecutionFlow.Pop())
        ReturnValue_9 = self.GetInstigator()
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_EQ_HookShot_Fire, ReturnValue_9, True)
        goto(ExecutionFlow.Pop())
        goto('L630')
    
