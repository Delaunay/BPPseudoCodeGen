
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.Anim_3p import Anim_3p
from Script.Engine import Delay
from Script.Engine import SetVisibility
from Script.Engine import K2_SetTimerDelegate
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import EqualEqual_ByteByte
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.BuildgunScan_02_Montage import BuildgunScan_02_Montage
from Game.FactoryGame.Equipment.BuildGun.Animation.BuildgunScan_03_Montage import BuildgunScan_03_Montage
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.FactoryGame import FGEquipmentAttachment
from Script.Engine import BooleanOR
from Script.FactoryGame import GetBuildGun
from Game.FactoryGame.Equipment.ResourceScanner.Attach_ResourceScanner import ExecuteUbergraph_Attach_ResourceScanner.K2Node_Event_useLocation
from Script.Engine import Montage_Play
from Script.FactoryGame import PlayUseEffect
from Game.FactoryGame.Equipment.BuildGun.BP_BuildGun import BP_BuildGun
from Script.FactoryGame import GetAttachedTo
from Script.FactoryGame import FGBuildGun
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.BuildgunScan_01_Montage import BuildgunScan_01_Montage
from Script.Engine import AnimInstance
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Equipment.ResourceScanner.Attach_ResourceScanner import ExecuteUbergraph_Attach_ResourceScanner

class Attach_ResourceScanner(FGEquipmentAttachment):
    mAttachSocket = buildgun_Socket
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def PlayUseEffect(self):
        ExecuteUbergraph_Attach_ResourceScanner.K2Node_Event_useLocation = UseLocation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Attach_ResourceScanner(1623)
    

    def CustomEvent_0(self):
        self.ExecuteUbergraph_Attach_ResourceScanner(2066)
    

    def ExecuteUbergraph_Attach_ResourceScanner(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Default__KismetSystemLibrary.Delay(self, 1.7000000476837158, LatentActionInfo(Linkage = 92, UUID = -517171160, ExecutionFunction = "ExecuteUbergraph_Attach_ResourceScanner", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        3p.mResourceScannerIK = False
        goto(ExecutionFlow.Pop())
        3p.mResourceScannerIK = False
        goto(ExecutionFlow.Pop())
        3p.mResourceScannerIK = False
        goto(ExecutionFlow.Pop())
        # Label 194
        ExecutionFlow.Push("L728")
        ReturnValue1: bool = EqualEqual_ByteByte(3p.mArmSlotType, 1)
        ReturnValue2: bool = EqualEqual_ByteByte(3p.mArmSlotType, 4)
        ReturnValue: bool = BooleanOR(ReturnValue1, ReturnValue2)
        if not ReturnValue:
            goto('L817')
        ReturnValue1_0: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_0: Ptr[SkeletalMeshComponent] = ReturnValue1_0.GetMesh3P()
        ReturnValue1_1: Ptr[AnimInstance] = ReturnValue_0.GetAnimInstance()
        ReturnValue2_0: float = ReturnValue1_1.Montage_Play(BuildgunScan_01_Montage, 1, 0, 0, True)
        ReturnValue_1: Ptr[AnimInstance] = self.Buildgun_skl.GetAnimInstance()
        ReturnValue_2: float = ReturnValue_1.Montage_Play(BuildgunScan_03_Montage, 1, 1, 0, True)
        Default__KismetSystemLibrary.Delay(self, 1.7000000476837158, LatentActionInfo(Linkage = 160, UUID = -1578741659, ExecutionFunction = "ExecuteUbergraph_Attach_ResourceScanner", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 728
        OutputDelegate.BindUFunction(self, CustomEvent_0)
        ReturnValue_3: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 1.899999976158142, False)
        goto(ExecutionFlow.Pop())
        # Label 817
        ReturnValue_4: bool = EqualEqual_ByteByte(3p.mArmSlotType, 3)
        if not ReturnValue_4:
            goto('L1438')
        self.Buildgun_skl.SetVisibility(False, False)
        ReturnValue1_0 = self.GetAttachedTo()
        ReturnValue_0 = ReturnValue1_0.GetMesh3P()
        ReturnValue1_1 = ReturnValue_0.GetAnimInstance()
        ReturnValue4: float = ReturnValue1_1.Montage_Play(BuildgunScan_01_Montage, 1, 0, 0, True)
        ReturnValue_5: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_6: Ptr[FGBuildGun] = ReturnValue_5.GetBuildGun()
        Gun: Ptr[BP_BuildGun] = Cast[BP_BuildGun](ReturnValue_6)
        bSuccess: bool = Gun
        ReturnValue2_1: Ptr[AnimInstance] = Gun.BuildGun_Skl_01.GetAnimInstance()
        ReturnValue3: float = ReturnValue2_1.Montage_Play(BuildgunScan_03_Montage, 1, 1, 0, True)
        Default__KismetSystemLibrary.Delay(self, 1.7000000476837158, LatentActionInfo(Linkage = 126, UUID = 61535369, ExecutionFunction = "ExecuteUbergraph_Attach_ResourceScanner", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1438
        ReturnValue1_0 = self.GetAttachedTo()
        ReturnValue_0 = ReturnValue1_0.GetMesh3P()
        ReturnValue1_1 = ReturnValue_0.GetAnimInstance()
        ReturnValue1_2: float = ReturnValue1_1.Montage_Play(BuildgunScan_02_Montage, 1, 0, 0, True)
        goto('L15')
        self.PlayUseEffect(useLocation)
        ReturnValue2_2: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue1_3: Ptr[SkeletalMeshComponent] = ReturnValue2_2.GetMesh3P()
        ReturnValue3_0: Ptr[AnimInstance] = ReturnValue1_3.GetAnimInstance()
        ReturnValue_7: bool = Default__KismetSystemLibrary.IsValid(ReturnValue3_0)
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        self.Buildgun_skl.SetVisibility(True, False)
        ReturnValue1_0 = self.GetAttachedTo()
        ReturnValue_0 = ReturnValue1_0.GetMesh3P()
        ReturnValue1_1 = ReturnValue_0.GetAnimInstance()
        3p: Ptr[Anim_3p] = Cast[Anim_3p](ReturnValue1_1)
        bSuccess1: bool = 3p
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        3p.mResourceScannerIK = True
        goto('L194')
        self.Buildgun_skl.SetVisibility(False, False)
        goto(ExecutionFlow.Pop())
    
