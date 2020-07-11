
from codegen.ue4_stub import *

from Script.Engine import SetColorParameter
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGColorGun
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Script.FactoryGame import GetInstigatorCharacter
from Script.Engine import SpawnEmitterAttached
from Script.Engine import GetInstigator
from Script.FactoryGame import PlayFireEffect
from Game.FactoryGame.Equipment.ColorGun.Widget_ColorGunUI import Widget_ColorGunUI
from Game.FactoryGame.Equipment.ColorGun.Animation.ColorGun_Reload_01_Montage import ColorGun_Reload_01_Montage
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Equipment.ColorGun.Animation.ColorGun_Primary_01_Montage import ColorGun_Primary_01_Montage
from Script.Engine import PlayerController
from Game.FactoryGame.Character.Player.CameraShake.ColorGunReload_01_Camera import ColorGunReload_01_Camera
from Script.Engine import GetController
from Game.FactoryGame.Equipment.ColorGun.Audio.Play_ColorGun_Equip import Play_ColorGun_Equip
from Script.FactoryGame import PlayReloadEffects
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import GetMesh1P
from Game.FactoryGame.Equipment.ColorGun.Equip_ColorGun import ExecuteUbergraph_Equip_ColorGun
from Game.FactoryGame.Character.Player.Animation.FirstPerson.ColorGun_Primary_01_Montage import ColorGun_Primary_01_Montage
from Game.FactoryGame.Character.Player.Animation.FirstPerson.ColorGun_Reload_01_Montage import ColorGun_Reload_01_Montage
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import GetPrimaryColorForSlot
from Script.Engine import Montage_Play
from Game.FactoryGame.VFX.Equipment.ColorGun.P_Colorgun_coloring_01 import P_Colorgun_coloring_01
from Game.FactoryGame.Character.Player.Animation.FirstPerson.ColorGun_Equip_02_Montage import ColorGun_Equip_02_Montage
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.Engine import ParticleSystemComponent
from Game.FactoryGame.Character.Player.CameraShake.ColorGunEquip_02_CameraAnim import ColorGunEquip_02_CameraAnim
from Script.UMG import Create
from Game.FactoryGame.Character.Player.CameraShake.ColorGunPrimary_01_CameraAnim import ColorGunPrimary_01_CameraAnim
from Script.FactoryGame import GetColorSlotIndex
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.Engine import SkeletalMeshComponent
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class Equip_ColorGun(FGColorGun):
    mColorWidget: Ptr[Widget_ColorGunUI]
    mPrimaryColor = Namespace(A=1, B=0, G=0, R=1)
    mSecondaryColor = Namespace(A=1, B=0, G=1, R=0)
    mRedundantTargetCrosshairColor = Namespace(A=1, B=1, G=1, R=1)
    mRedundantTargetCrosshairTexture = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/ColorGun/UI/ColorGun_AlreadyPainted.ColorGun_AlreadyPainted')
    mNoTargetCrosshairColor = Namespace(A=0.6000000238418579, B=1, G=1, R=1)
    mNoTargetCrosshairTexture = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/ColorGun/UI/ColorGun_Invalid.ColorGun_Invalid')
    mNonColorableTargetCrosshairColor = Namespace(A=0.6000000238418579, B=1, G=1, R=1)
    mNonColorableTargetCrosshairTexture = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/ColorGun/UI/ColorGun_Invalid.ColorGun_Invalid')
    mValidTargetCrosshairTexture = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/ColorGun/UI/ColorGun_Valid.ColorGun_Valid')
    mColorSlot = 1
    mInstantHitDamage = 10
    mWeaponTraceLength = 10000
    mMagSize = 100
    mAmmunitionClass = NewObject[Desc_ColorCartridge]()
    mDamageTypeClass = NewObject[FGDamageType]()
    mReloadTime = 0.10000000149011612
    mFireRate = 0.5
    mAttachmentClass = NewObject[Attach_ColorGun]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_ColorGun
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def ToggleColorPickerUI(self):
        self.ExecuteUbergraph_Equip_ColorGun(723)
    

    def PlayFireEffect(self):
        self.ExecuteUbergraph_Equip_ColorGun(807)
    

    def PlayReloadEffects(self):
        self.ExecuteUbergraph_Equip_ColorGun(1853)
    

    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_ColorGun(2657)
    

    def Event Clear Color Picker UI(self):
        self.ExecuteUbergraph_Equip_ColorGun(3441)
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_Equip_ColorGun(3541)
    

    def ExecuteUbergraph_Equip_ColorGun(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mColorWidget)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        ReturnValue5: Ptr[Pawn] = self.GetInstigator()
        ReturnValue5_0: Ptr[Controller] = ReturnValue5.GetController()
        Default__BPHUDHelpers.PopStackWidget(ReturnValue5_0, self.mColorWidget, self)
        self.mColorWidget = None
        goto(ExecutionFlow.Pop())
        # Label 205
        ReturnValue_0: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_1: Ptr[Controller] = ReturnValue_0.GetController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue_1)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: Ptr[Widget_ColorGunUI] = Default__WidgetBlueprintLibrary.Create(self, Widget_ColorGunUI, Controller)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mColorGun", self)
        self.mColorWidget = ReturnValue_2
        Default__BPHUDHelpers.PushStackWidget(Controller, self.mColorWidget, self)
        goto(ExecutionFlow.Pop())
        # Label 533
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mColorWidget)
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        ReturnValue4: Ptr[Pawn] = self.GetInstigator()
        ReturnValue4_0: Ptr[Controller] = ReturnValue4.GetController()
        Default__BPHUDHelpers.PopStackWidget(ReturnValue4_0, self.mColorWidget, self)
        self.mColorWidget = None
        goto(ExecutionFlow.Pop())
        ReturnValue2: bool = Default__KismetSystemLibrary.IsValid(self.mColorWidget)
        if not ReturnValue2:
            goto('L205')
        self.Event Clear Color Picker UI()
        goto('L205')
        self.PlayFireEffect()
        ExecutionFlow.Push("L1501")
        ExecutionFlow.Push("L935")
        ReturnValue_3: Ptr[AnimInstance] = self.Colorgun_skl.GetAnimInstance()
        ReturnValue_4: bool = ReturnValue_3.Montage_IsPlaying(ColorGun_Primary_01_Montage)
        if not ReturnValue_4:
            goto('L1738')
        goto(ExecutionFlow.Pop())
        # Label 935
        ReturnValue_5: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_6: Ptr[SkeletalMeshComponent] = ReturnValue_5.GetMesh1P()
        ReturnValue2_0: Ptr[AnimInstance] = ReturnValue_6.GetAnimInstance()
        ReturnValue3: bool = ReturnValue2_0.Montage_IsPlaying(ColorGun_Primary_01_Montage)
        if not ReturnValue3:
            goto('L1105')
        goto(ExecutionFlow.Pop())
        # Label 1105
        ReturnValue_5 = self.GetInstigatorCharacter()
        ReturnValue_6 = ReturnValue_5.GetMesh1P()
        ReturnValue2_0 = ReturnValue_6.GetAnimInstance()
        ReturnValue2_1: float = ReturnValue2_0.Montage_Play(ColorGun_Primary_01_Montage, 1, 0, 0, True)
        ReturnValue2_2: Ptr[Pawn] = self.GetInstigator()
        ReturnValue2_3: Ptr[Controller] = ReturnValue2_2.GetController()
        Controller2: Ptr[PlayerController] = Cast[PlayerController](ReturnValue2_3)
        bSuccess2: bool = Controller2
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        Controller2.ClientPlayCameraAnim(ColorGunPrimary_01_CameraAnim, 1, 1, 0, 0.10000000149011612, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        goto(ExecutionFlow.Pop())
        # Label 1501
        ReturnValue_7: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_Colorgun_coloring_01, self.Colorgun_skl, "muzzleVfxSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        ReturnValue_8: uint8 = self.GetColorSlotIndex()
        ReturnValue_9: LinearColor = self.GetPrimaryColorForSlot(ReturnValue_8)
        ReturnValue_7.SetColorParameter("Cd", ReturnValue_9)
        goto(ExecutionFlow.Pop())
        # Label 1738
        ReturnValue_3 = self.Colorgun_skl.GetAnimInstance()
        ReturnValue_10: float = ReturnValue_3.Montage_Play(ColorGun_Primary_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        self.PlayReloadEffects()
        ExecutionFlow.Push("L2091")
        ReturnValue1_0: Ptr[AnimInstance] = self.Colorgun_skl.GetAnimInstance()
        ReturnValue1_1: bool = ReturnValue1_0.Montage_IsPlaying(ColorGun_Reload_01_Montage)
        if not ReturnValue1_1:
            goto('L1976')
        goto(ExecutionFlow.Pop())
        # Label 1976
        ReturnValue1_0 = self.Colorgun_skl.GetAnimInstance()
        ReturnValue1_2: float = ReturnValue1_0.Montage_Play(ColorGun_Reload_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 2091
        ReturnValue1_3: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_4: Ptr[SkeletalMeshComponent] = ReturnValue1_3.GetMesh1P()
        ReturnValue3_0: Ptr[AnimInstance] = ReturnValue1_4.GetAnimInstance()
        ReturnValue2_4: bool = ReturnValue3_0.Montage_IsPlaying(ColorGun_Reload_01_Montage)
        if not ReturnValue2_4:
            goto('L2261')
        goto(ExecutionFlow.Pop())
        # Label 2261
        ReturnValue1_3 = self.GetInstigatorCharacter()
        ReturnValue1_4 = ReturnValue1_3.GetMesh1P()
        ReturnValue3_0 = ReturnValue1_4.GetAnimInstance()
        ReturnValue3_1: float = ReturnValue3_0.Montage_Play(ColorGun_Reload_01_Montage, 1, 0, 0, True)
        ReturnValue1_5: Ptr[Pawn] = self.GetInstigator()
        ReturnValue1_6: Ptr[Controller] = ReturnValue1_5.GetController()
        Controller1: Ptr[PlayerController] = Cast[PlayerController](ReturnValue1_6)
        bSuccess1: bool = Controller1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Controller1.ClientPlayCameraAnim(ColorGunReload_01_Camera, 1, 1, 0, 0.10000000149011612, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        goto(ExecutionFlow.Pop())
        ReturnValue2_5: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue2_6: Ptr[SkeletalMeshComponent] = ReturnValue2_5.GetMesh1P()
        ReturnValue4_1: Ptr[AnimInstance] = ReturnValue2_6.GetAnimInstance()
        ReturnValue3_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue4_1)
        if not ReturnValue3_2:
           goto(ExecutionFlow.Pop())
        ReturnValue2_5 = self.GetInstigatorCharacter()
        ReturnValue2_6 = ReturnValue2_5.GetMesh1P()
        ReturnValue4_1 = ReturnValue2_6.GetAnimInstance()
        ReturnValue4_2: bool = ReturnValue4_1.Montage_IsPlaying(ColorGun_Equip_02_Montage)
        if not ReturnValue4_2:
            goto('L2992')
        goto(ExecutionFlow.Pop())
        # Label 2992
        ReturnValue_11: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_ColorGun_Equip, self, True)
        ReturnValue2_5 = self.GetInstigatorCharacter()
        ReturnValue2_6 = ReturnValue2_5.GetMesh1P()
        ReturnValue4_1 = ReturnValue2_6.GetAnimInstance()
        ReturnValue4_3: float = ReturnValue4_1.Montage_Play(ColorGun_Equip_02_Montage, 1, 0, 0, True)
        ReturnValue3_3: Ptr[Pawn] = self.GetInstigator()
        ReturnValue3_4: Ptr[Controller] = ReturnValue3_3.GetController()
        Controller3: Ptr[PlayerController] = Cast[PlayerController](ReturnValue3_4)
        bSuccess3: bool = Controller3
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        Controller3.ClientPlayCameraAnim(ColorGunEquip_02_CameraAnim, 1, 1, 0, 0.10000000149011612, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.PrintString(self, "Closed Color Picker", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto('L533')
        goto('L15')
    
