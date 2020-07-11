
from codegen.ue4_stub import *

from Script.Engine import Delay
from Script.Engine import SetVisibility
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Script.FactoryGame import GetInstigatorCharacter
from Script.Engine import Pawn
from Script.FactoryGame import WasEquipped
from Script.FactoryGame import WasUnEquipped
from Script.Engine import GetInstigator
from Script.FactoryGame import IsLocallyHumanControlled
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Character.Player.Animation.FirstPerson.BuildgunEquip_01_Montage import BuildgunEquip_01_Montage
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Script.Engine import PlayerController
from Script.Engine import GetController
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.InGame.Widget_BuildGunDelay import Widget_BuildGunDelay
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import GetMesh1P
from Script.Engine import Montage_Stop
from Script.Engine import GetPlayerController
from Script.Engine import Default__GameplayStatics
from Script.Engine import Montage_Play
from Game.FactoryGame.Equipment.BuildGun.Animation.BuildgunEquip_01_Montage import BuildgunEquip_01_Montage
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.UMG import Create
from Script.FactoryGame import FGBuildGun
from Script.Engine import AnimInstance
from Script.UMG import AddToViewport
from Game.FactoryGame.Equipment.BuildGun.BP_BuildGun import ExecuteUbergraph_BP_BuildGun
from Script.Engine import SkeletalMeshComponent

class BP_BuildGun(FGBuildGun):
    ActionDelayWidget: Ptr[Widget_BuildGunDelay]
    mBuildDistanceMax = 10000
    mMenuStateClass = NewObject[BP_BuildGunStateMenu]()
    mBuildStateClass = NewObject[BP_BuildGunStateBuild]()
    mDismantleStateClass = NewObject[BP_BuildGunStateDismantle]()
    mAttachmentClass = NewObject[Attach_BuildGun]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mEquipSound = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/Play_P_ResourcePickUp.Play_P_ResourcePickUp')
    mAttachSocket = buildgun_Socket
    mArmAnimation = EArmEquipment::AE_BuildGun
    mHasPersistentOwner = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def GetInstigatorPlayerController(self):
        ReturnValue: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_0: Ptr[Controller] = ReturnValue.GetController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue_0)
        bSuccess: bool = Controller
        PlayerController = Controller
    

    def WasEquipped(self):
        self.ExecuteUbergraph_BP_BuildGun(974)
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_BP_BuildGun(989)
    

    def ExecuteUbergraph_BP_BuildGun(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.Hologram.SetVisibility(True, False)
        self.hologramBeam_01.SetActive(True, False)
        goto(ExecutionFlow.Pop())
        # Label 88
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_0: bool = Default__FGBlueprintFunctionLibrary.IsLocallyHumanControlled(ReturnValue)
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ReturnValue_1: Ptr[PlayerController] = Default__GameplayStatics.GetPlayerController(self, 0)
        ReturnValue_2: Ptr[Widget_BuildGunDelay] = Default__WidgetBlueprintLibrary.Create(self, Widget_BuildGunDelay, ReturnValue_1)
        ReturnValue_2.AddToViewport(0)
        self.ActionDelayWidget = ReturnValue_2
        ReturnValue4: bool = Default__KismetSystemLibrary.IsValid(self.ActionDelayWidget)
        if not ReturnValue4:
           goto(ExecutionFlow.Pop())
        self.ActionDelayWidget.mBuildGun = self
        ExecutionFlow.Push("L859")
        ReturnValue2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1: Ptr[SkeletalMeshComponent] = ReturnValue2.GetMesh1P()
        ReturnValue1_0: Ptr[AnimInstance] = ReturnValue1.GetAnimInstance()
        ReturnValue2_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_0)
        if not ReturnValue2_0:
            goto('L15')
        ReturnValue2 = self.GetInstigatorCharacter()
        ReturnValue1 = ReturnValue2.GetMesh1P()
        ReturnValue1_0 = ReturnValue1.GetAnimInstance()
        ReturnValue1_1: float = ReturnValue1_0.Montage_Play(BuildgunEquip_01_Montage, 1, 1, 0, True)
        Default__KismetSystemLibrary.Delay(self, ReturnValue1_1, LatentActionInfo(Linkage = 15, UUID = -2131797795, ExecutionFunction = "ExecuteUbergraph_BP_BuildGun", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 859
        ReturnValue_3: Ptr[AnimInstance] = self.BuildGun_Skl_01.GetAnimInstance()
        ReturnValue_4: float = ReturnValue_3.Montage_Play(BuildgunEquip_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        self.WasEquipped()
        goto('L88')
        self.WasUnEquipped()
        ReturnValue1_2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_5: Ptr[SkeletalMeshComponent] = ReturnValue1_2.GetMesh1P()
        ReturnValue1_3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_5)
        if not ReturnValue1_3:
            goto('L1445')
        ReturnValue1_2 = self.GetInstigatorCharacter()
        ReturnValue_5 = ReturnValue1_2.GetMesh1P()
        ReturnValue2_1: Ptr[AnimInstance] = ReturnValue_5.GetAnimInstance()
        ReturnValue3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue2_1)
        if not ReturnValue3:
            goto('L1445')
        ReturnValue1_2 = self.GetInstigatorCharacter()
        ReturnValue_5 = ReturnValue1_2.GetMesh1P()
        ReturnValue2_1 = ReturnValue_5.GetAnimInstance()
        ReturnValue2_1.Montage_Stop(0, BuildgunEquip_01_Montage)
        # Label 1445
        ReturnValue_6: bool = Default__KismetSystemLibrary.IsValid(self.ActionDelayWidget)
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        self.ActionDelayWidget.RemoveFromParent()
        self.ActionDelayWidget = None
        self.Hologram.SetVisibility(False, False)
        self.hologramBeam_01.SetActive(False, False)
        goto(ExecutionFlow.Pop())
    
