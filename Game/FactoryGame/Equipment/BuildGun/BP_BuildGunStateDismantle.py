
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.BuildGun.BP_BuildGunStateDismantle import ExecuteUbergraph_BP_BuildGunStateDismantle.K2Node_Event_recipe
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Buildable.-Shared.Audio.BuildEffect_2018-05.Play_Dismantle_Bleeps_Stereo import Play_Dismantle_Bleeps_Stereo
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Script.FactoryGame import SetCrosshairState
from Script.FactoryGame import GetInstigatorCharacter
from Script.Engine import Pawn
from Script.Engine import SetObjectPropertyByName
from Script.Engine import GetInstigator
from Script.FactoryGame import GetBuildGunDelayPercentage
from Script.Engine import HUD
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Script.FactoryGame import OnRecipeSampled
from Game.FactoryGame.Equipment.BuildGun.BP_BuildGunStateDismantle import ExecuteUbergraph_BP_BuildGunStateDismantle
from Script.Engine import GetController
from Script.Engine import GreaterEqual_FloatFloat
from Script.Engine import IsValid
from Script.FactoryGame import IsLocalInstigator
from Script.Engine import GetHUD
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import GetMesh1P
from Script.Engine import Montage_Stop
from Script.FactoryGame import TickState
from Game.FactoryGame.Character.Player.Animation.FirstPerson.BuildGunDismantle_01_Montage import BuildGunDismantle_01_Montage
from Game.FactoryGame.Buildable.-Shared.Audio.BuildEffect_2018-05.Stop_Dismantle_Bleeps_Stereo import Stop_Dismantle_Bleeps_Stereo
from Script.FactoryGame import ToggleBuildGun
from Game.FactoryGame.Equipment.BuildGun.Animation.BuildgunDismantle_01_Montage import BuildGunDismantle_01_Montage
from Script.FactoryGame import EndState
from Game.FactoryGame.Interface.UI.InGame.Widget_DismantleMode import Widget_DismantleMode
from Script.FactoryGame import GetBuildGun
from Script.Engine import Montage_Play
from Game.FactoryGame.Buildable.-Shared.Audio.Play_Dismantle_Bleeps_Cancel import Play_Dismantle_Bleeps_Cancel
from Script.FactoryGame import FGHUD
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import FGBuildGunStateDismantle
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import Actor
from Game.FactoryGame.Equipment.BuildGun.BP_BuildGun import BP_BuildGun
from Script.FactoryGame import FGBuildGun
from Script.UMG import Create
from Script.Engine import GetOwner
from Game.FactoryGame.Interface.UI.Audio.Play_UI_CloneBuilding import Play_UI_CloneBuilding
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.FactoryGame import SecondaryFire
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Equipment.BuildGun.BP_BuildGunStateDismantle import ExecuteUbergraph_BP_BuildGunStateDismantle.K2Node_Event_deltaTime
from Script.FactoryGame import BeginState

class BP_BuildGunStateDismantle(FGBuildGunStateDismantle):
    mDismantleUI: Ptr[Widget_DismantleMode]
    mActionDelay = 0.75
    mActionMessage = NSLOCTEXT("", "325F54B74E58D3A1A87EEB97CDD98AD8", "Dismantling...")
    
    def TickState(self):
        ExecuteUbergraph_BP_BuildGunStateDismantle.K2Node_Event_deltaTime = DeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_BuildGunStateDismantle(2251)
    

    def SecondaryFire(self):
        self.ExecuteUbergraph_BP_BuildGunStateDismantle(15)
    

    def BeginState(self):
        self.ExecuteUbergraph_BP_BuildGunStateDismantle(316)
    

    def EndState(self):
        self.ExecuteUbergraph_BP_BuildGunStateDismantle(919)
    

    def OnStartDismantle(self):
        self.ExecuteUbergraph_BP_BuildGunStateDismantle(1166)
    

    def OnStopDismantle(self):
        self.ExecuteUbergraph_BP_BuildGunStateDismantle(1703)
    

    def OnRecipeSampled(self):
        ExecuteUbergraph_BP_BuildGunStateDismantle.K2Node_Event_recipe = Recipe #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_BuildGunStateDismantle(2271)
    

    def ExecuteUbergraph_BP_BuildGunStateDismantle(self):
        goto(ComputedJump("EntryPoint"))
        self.SecondaryFire()
        ReturnValue7: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue1: bool = ReturnValue7.IsLocalInstigator()
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        ReturnValue7 = self.GetBuildGun()
        ReturnValue1_0: Ptr[FGCharacterPlayer] = ReturnValue7.GetInstigatorCharacter()
        ReturnValue1_0.ToggleBuildGun()
        goto(ExecutionFlow.Pop())
        # Label 192
        ReturnValue: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue_0: Ptr[Actor] = ReturnValue.GetOwner()
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_CloneBuilding, ReturnValue_0, True)
        goto(ExecutionFlow.Pop())
        self.BeginState()
        ReturnValue1_1: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue_2: bool = ReturnValue1_1.IsLocalInstigator()
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        ReturnValue1_1 = self.GetBuildGun()
        ReturnValue_3: Ptr[Pawn] = ReturnValue1_1.GetInstigator()
        ReturnValue_4: Ptr[Controller] = ReturnValue_3.GetController()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_4)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_5: Ptr[Widget_DismantleMode] = Default__WidgetBlueprintLibrary.Create(self, Widget_DismantleMode, Controller)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_5, "mOwningState", self)
        self.mDismantleUI = ReturnValue_5
        Default__BPHUDHelpers.PushStackWidget(Controller, self.mDismantleUI, self)
        ReturnValue_6: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_6)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        AsFGHUD.SetCrosshairState(6)
        goto(ExecutionFlow.Pop())
        self.EndState()
        ReturnValue_7: bool = Default__KismetSystemLibrary.IsValid(self.mDismantleUI)
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        ReturnValue6: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue1_2: Ptr[Controller] = ReturnValue6.Instigator.GetController()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue1_2, self, Ref[gameUI])
        gameUI.PopAllWidgets()
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1471")
        ReturnValue2: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue_8: Ptr[FGCharacterPlayer] = ReturnValue2.GetInstigatorCharacter()
        ReturnValue_9: Ptr[SkeletalMeshComponent] = ReturnValue_8.GetMesh1P()
        ReturnValue_10: Ptr[AnimInstance] = ReturnValue_9.GetAnimInstance()
        ReturnValue1_3: float = ReturnValue_10.Montage_Play(BuildGunDismantle_01_Montage, 1, 1, 0, True)
        ReturnValue4: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue1_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_Dismantle_Bleeps_Stereo, ReturnValue4, True)
        goto(ExecutionFlow.Pop())
        # Label 1471
        ReturnValue3: Ptr[FGBuildGun] = self.GetBuildGun()
        Gun: Ptr[BP_BuildGun] = Cast[BP_BuildGun](ReturnValue3)
        bSuccess2: bool = Gun
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        ReturnValue1_5: Ptr[AnimInstance] = Gun.BuildGun_Skl_01.GetAnimInstance()
        ReturnValue_11: float = ReturnValue1_5.Montage_Play(BuildGunDismantle_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        ReturnValue_12: float = self.GetBuildGunDelayPercentage()
        ReturnValue_13: bool = GreaterEqual_FloatFloat(ReturnValue_12, 1)
        if not ReturnValue_13:
            goto('L1780')
        goto(ExecutionFlow.Pop())
        # Label 1780
        ExecutionFlow.Push("L2140")
        ReturnValue2 = self.GetBuildGun()
        ReturnValue_8 = ReturnValue2.GetInstigatorCharacter()
        ReturnValue_9 = ReturnValue_8.GetMesh1P()
        ReturnValue_10 = ReturnValue_9.GetAnimInstance()
        ReturnValue_10.Montage_Stop(0.5, BuildGunDismantle_01_Montage)
        ReturnValue5: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue3_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_Dismantle_Bleeps_Stereo, ReturnValue5, True)
        ReturnValue5 = self.GetBuildGun()
        ReturnValue2_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_Dismantle_Bleeps_Cancel, ReturnValue5, True)
        goto(ExecutionFlow.Pop())
        # Label 2140
        ReturnValue1_5 = Gun.BuildGun_Skl_01.GetAnimInstance()
        ReturnValue1_5.Montage_Stop(0.5, BuildGunDismantle_01_Montage)
        goto(ExecutionFlow.Pop())
        self.TickState(deltaTime)
        goto(ExecutionFlow.Pop())
        self.OnRecipeSampled(recipe)
        goto('L192')
    
