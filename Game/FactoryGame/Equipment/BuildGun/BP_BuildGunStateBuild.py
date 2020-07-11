
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Game.FactoryGame.Equipment.BuildGun.BP_BuildGunStateBuild import ExecuteUbergraph_BP_BuildGunStateBuild
from Script.FactoryGame import SetCrosshairState
from Script.FactoryGame import GetInstigatorCharacter
from Script.Engine import Pawn
from Script.Engine import SetObjectPropertyByName
from Script.FactoryGame import FGHologram
from Script.Engine import GetInstigator
from Script.Engine import HUD
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Equipment.BuildGun.Animation.BuildGunPrimary_01_Montage import BuildGunPrimary_01_Montage
from Script.Engine import PlayerController
from Script.FactoryGame import OnRecipeSampled
from Script.Engine import GetController
from Script.FactoryGame import GetHologram
from Script.Engine import IsValid
from Script.FactoryGame import IsLocalInstigator
from Script.Engine import GetHUD
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import GetMesh1P
from Game.FactoryGame.Equipment.BuildGun.BP_BuildGunStateBuild import ExecuteUbergraph_BP_BuildGunStateBuild.K2Node_Event_recipe
from Script.AkAudio import AkAudioEvent
from Script.FactoryGame import GetGameUI
from Script.FactoryGame import EndState
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_SplineModeSelectWheel import Widget_SplineModeSelectWheel
from Script.FactoryGame import ResetHologram
from Script.FactoryGame import PrimaryFire
from Script.FactoryGame import GetBuildGun
from Script.FactoryGame import HasAuthority
from Script.Engine import Montage_Play
from Game.FactoryGame.Equipment.BuildGun.BP_BuildGunStateBuild import ExecuteUbergraph_BP_BuildGunStateBuild.K2Node_Event_isFinalStep
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import FGHUD
from Script.FactoryGame import FGGameUI
from Game.FactoryGame.Character.Player.Animation.FirstPerson.BuildGunPrimary_01_Montage import BuildGunPrimary_01_Montage
from Script.FactoryGame import FGBuildGunStateBuild
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.Engine import Actor
from Game.FactoryGame.Equipment.BuildGun.BP_BuildGun import BP_BuildGun
from Script.FactoryGame import FGBuildGun
from Script.UMG import Create
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Widget_BuildMode import Widget_BuildMode
from Script.Engine import GetOwner
from Game.FactoryGame.Interface.UI.Audio.Play_UI_CloneBuilding import Play_UI_CloneBuilding
from Script.FactoryGame import GotoMenuState
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.FactoryGame import SecondaryFire
from Script.Engine import SkeletalMeshComponent
from Script.FactoryGame import BeginState

class BP_BuildGunStateBuild(FGBuildGunStateBuild):
    mMultiStepConstructionSound: Ptr[AkAudioEvent] = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Audio/Hologram/Play_UI_Hologram_HalfPlaced.Play_UI_Hologram_HalfPlaced')
    mCancelHologramSound: Ptr[AkAudioEvent] = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Audio/Hologram/Play_UI_Hologram_Cancel.Play_UI_Hologram_Cancel')
    mSplineModeSelectWheel: Ptr[Widget_SplineModeSelectWheel]
    mSplineModeSelectHoldDownDurationForUI = 0.18000000715255737
    mIsUsingPressAndReleaseAsBuildSteps = True
    mActionMessage = NSLOCTEXT("", "A523F6B24CC1C40D74CBA7B80E07B648", "Building...")
    
    def SecondaryFire(self):
        self.ExecuteUbergraph_BP_BuildGunStateBuild(1767)
    

    def OnMultiStepPlacement(self):
        ExecuteUbergraph_BP_BuildGunStateBuild.K2Node_Event_isFinalStep = isFinalStep #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_BuildGunStateBuild(874)
    

    def OnResetHologram(self):
        self.ExecuteUbergraph_BP_BuildGunStateBuild(1070)
    

    def PrimaryFire(self):
        self.ExecuteUbergraph_BP_BuildGunStateBuild(1732)
    

    def EndState(self):
        self.ExecuteUbergraph_BP_BuildGunStateBuild(1747)
    

    def ShowSplineModeSelectUI(self):
        self.ExecuteUbergraph_BP_BuildGunStateBuild(1797)
    

    def CloseSplineModeSelectUI(self):
        self.ExecuteUbergraph_BP_BuildGunStateBuild(2204)
    

    def BeginState(self):
        self.ExecuteUbergraph_BP_BuildGunStateBuild(2457)
    

    def OpenBuildModeUI(self):
        self.ExecuteUbergraph_BP_BuildGunStateBuild(2911)
    

    def OnRecipeSampled(self):
        ExecuteUbergraph_BP_BuildGunStateBuild.K2Node_Event_recipe = Recipe #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_BuildGunStateBuild(15)
    

    def ExecuteUbergraph_BP_BuildGunStateBuild(self):
        goto(ComputedJump("EntryPoint"))
        self.OnRecipeSampled(recipe)
        ReturnValue8: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue2: Ptr[Actor] = ReturnValue8.GetOwner()
        ReturnValue2_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_CloneBuilding, ReturnValue2, True)
        goto(ExecutionFlow.Pop())
        # Label 158
        self.EndState()
        ReturnValue1: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue1_0: bool = ReturnValue1.IsLocalInstigator()
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        ReturnValue1 = self.GetBuildGun()
        ReturnValue: Ptr[Pawn] = ReturnValue1.GetInstigator()
        ReturnValue_0: Ptr[Controller] = ReturnValue.GetController()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_0)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_1: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_1)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: Ptr[FGGameUI] = AsFGHUD.GetGameUI()
        ReturnValue_2.PopAllWidgets()
        goto(ExecutionFlow.Pop())
        # Label 615
        ReturnValue_3: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue_3.GotoMenuState()
        goto(ExecutionFlow.Pop())
        # Label 668
        ReturnValue_4: Ptr[FGHologram] = self.GetHologram()
        ReturnValue_5: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_4)
        if not ReturnValue_5:
            goto('L615')
        ReturnValue_4 = self.GetHologram()
        ReturnValue_6: bool = ReturnValue_4.IsChanged()
        if not ReturnValue_6:
            goto('L615')
        ReturnValue_7: bool = self.HasAuthority()
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        self.ResetHologram()
        goto(ExecutionFlow.Pop())
        ReturnValue4: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue2_1: bool = ReturnValue4.IsLocalInstigator()
        if not ReturnValue2_1:
           goto(ExecutionFlow.Pop())
        ReturnValue3: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue_8: Ptr[Actor] = ReturnValue3.GetOwner()
        ReturnValue_9: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mMultiStepConstructionSound, ReturnValue_8, True)
        goto(ExecutionFlow.Pop())
        ReturnValue7: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue1_1: Ptr[Actor] = ReturnValue7.GetOwner()
        ReturnValue1_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mCancelHologramSound, ReturnValue1_1, True)
        goto(ExecutionFlow.Pop())
        # Label 1194
        ReturnValue2_2: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue_10: Ptr[FGCharacterPlayer] = ReturnValue2_2.GetInstigatorCharacter()
        ReturnValue_11: Ptr[SkeletalMeshComponent] = ReturnValue_10.GetMesh1P()
        ReturnValue_12: Ptr[AnimInstance] = ReturnValue_11.GetAnimInstance()
        ReturnValue_13: float = ReturnValue_12.Montage_Play(BuildGunPrimary_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 1413
        ReturnValue2_2 = self.GetBuildGun()
        Gun: Ptr[BP_BuildGun] = Cast[BP_BuildGun](ReturnValue2_2)
        bSuccess2: bool = Gun
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1518")
        goto('L1194')
        # Label 1518
        ReturnValue1_3: Ptr[AnimInstance] = Gun.BuildGun_Skl_01.GetAnimInstance()
        ReturnValue1_4: float = ReturnValue1_3.Montage_Play(BuildGunPrimary_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 1655
        ReturnValue2_2 = self.GetBuildGun()
        ReturnValue_14: bool = ReturnValue2_2.IsLocalInstigator()
        if not ReturnValue_14:
           goto(ExecutionFlow.Pop())
        goto('L1413')
        self.PrimaryFire()
        goto('L1655')
        goto('L158')
        # Label 1752
        self.SecondaryFire()
        goto('L668')
        goto('L1752')
        # Label 1772
        self.BeginState()
        self.OpenBuildModeUI()
        goto(ExecutionFlow.Pop())
        ReturnValue5: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue1_5: Ptr[FGCharacterPlayer] = ReturnValue5.GetInstigatorCharacter()
        ReturnValue1_6: Ptr[Controller] = ReturnValue1_5.GetController()
        Controller_0: Ptr[PlayerController] = Cast[PlayerController](ReturnValue1_6)
        bSuccess3: bool = Controller_0
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        ReturnValue_15: Ptr[Widget_SplineModeSelectWheel] = Default__WidgetBlueprintLibrary.Create(self, Widget_SplineModeSelectWheel, Controller_0)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_15, "mBuildGunState", self)
        self.mSplineModeSelectWheel = ReturnValue_15
        Default__BPHUDHelpers.PushStackWidget(Controller_0, self.mSplineModeSelectWheel, self)
        Controller_0.SetIgnoreLookInput(True)
        goto(ExecutionFlow.Pop())
        ReturnValue5 = self.GetBuildGun()
        ReturnValue1_5 = ReturnValue5.GetInstigatorCharacter()
        ReturnValue1_6 = ReturnValue1_5.GetController()
        ReturnValue1_6.SetIgnoreLookInput(False)
        ReturnValue1_7: bool = Default__KismetSystemLibrary.IsValid(self.mSplineModeSelectWheel)
        if not ReturnValue1_7:
           goto(ExecutionFlow.Pop())
        self.mSplineModeSelectWheel.RemoveFromParent()
        self.OpenBuildModeUI()
        goto(ExecutionFlow.Pop())
        goto('L1772')
        # Label 2462
        ReturnValue6: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue3_0: bool = ReturnValue6.IsLocalInstigator()
        if not ReturnValue3_0:
           goto(ExecutionFlow.Pop())
        ReturnValue6 = self.GetBuildGun()
        ReturnValue1_8: Ptr[Pawn] = ReturnValue6.GetInstigator()
        ReturnValue2_3: Ptr[Controller] = ReturnValue1_8.GetController()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue2_3)
        bSuccess4: bool = Controller1
        if not bSuccess4:
           goto(ExecutionFlow.Pop())
        ReturnValue1_9: Ptr[HUD] = Controller1.GetHUD()
        AsFGHUD1: Ptr[FGHUD] = Cast[FGHUD](ReturnValue1_9)
        bSuccess5: bool = AsFGHUD1
        if not bSuccess5:
           goto(ExecutionFlow.Pop())
        AsFGHUD1.OpenInteractUI(Widget_BuildMode, self)
        AsFGHUD1.SetCrosshairState(7)
        goto(ExecutionFlow.Pop())
        goto('L2462')
    
