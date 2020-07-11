
from codegen.ue4_stub import *

from Script.FactoryGame import IsBeeping
from Script.Engine import SetVisibility
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import SetLightColor
from Script.Engine import GetAnimInstance
from Script.Engine import ReceiveTick
from Script.CoreUObject import Color
from Script.FactoryGame import PlayAttachEffects3P
from Script.FactoryGame import GetScannerLightColor
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.ObjectScannerEquip_01_Montage import ObjectScannerEquip_01_Montage
from Script.Engine import Conv_ColorToLinearColor
from Script.Engine import Montage_Play
from Game.FactoryGame.Equipment.ObjectScanner.Attach_ObjectScanner import ExecuteUbergraph_Attach_ObjectScanner
from Game.FactoryGame.Equipment.ObjectScanner.Attach_ObjectScanner import ExecuteUbergraph_Attach_ObjectScanner.K2Node_Event_DeltaSeconds
from Script.FactoryGame import FGObjectScannerAttachment
from Script.FactoryGame import GetAttachedTo
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.Engine import SkeletalMeshComponent
from Script.CoreUObject import LinearColor

class Attach_ObjectScanner(FGObjectScannerAttachment):
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_Generic1Hand
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Attach_ObjectScanner(383)
    

    def ReceiveTick(self):
        ExecuteUbergraph_Attach_ObjectScanner.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Attach_ObjectScanner(388)
    

    def UpdateScannerVisuals(self):
        self.ExecuteUbergraph_Attach_ObjectScanner(412)
    

    def PlayAttachEffects3P(self):
        self.ExecuteUbergraph_Attach_ObjectScanner(586)
    

    def ExecuteUbergraph_Attach_ObjectScanner(self):
        # Label 10
        self.PlayAttachEffects3P()
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_0: Ptr[SkeletalMeshComponent] = ReturnValue.GetMesh3P()
        ReturnValue_1: Ptr[AnimInstance] = ReturnValue_0.GetAnimInstance()
        ReturnValue_2: bool = ReturnValue_1.Montage_IsPlaying(ObjectScannerEquip_01_Montage)
        if not ReturnValue_2:
            goto('L198')
        # End
        # Label 198
        ReturnValue = self.GetAttachedTo()
        ReturnValue_0 = ReturnValue.GetMesh3P()
        ReturnValue_1 = ReturnValue_0.GetAnimInstance()
        ReturnValue_3: float = ReturnValue_1.Montage_Play(ObjectScannerEquip_01_Montage, 1, 0, 0, True)
        # End
        # End
        self.ReceiveTick(DeltaSeconds)
        # End
        ReturnValue_4: bool = self.IsBeeping()
        self.PointLight.SetVisibility(ReturnValue_4, False)
        ReturnValue_5: Color = self.GetScannerLightColor()
        ReturnValue_6: LinearColor = Conv_ColorToLinearColor(ReturnValue_5)
        self.PointLight.SetLightColor(ReturnValue_6, True)
        # End
        goto('L10')
    
