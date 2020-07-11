
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Game.FactoryGame.Interface.UI.Audio.StandbyButton.Play_UI_StandBy_Hover_UnPowered import Play_UI_StandBy_Hover_UnPowered
from Game.FactoryGame.Interface.UI.Assets.Shared.StandbyButtonPressed import StandbyButtonPressed
from Script.Engine import Pawn
from Script.SlateCore import Margin
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import SetRenderTranslation
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.Audio.StandbyButton.Play_UI_StandBy_UnTicked import Play_UI_StandBy_UnTicked
from Script.Engine import IsValid
from Script.FactoryGame import IsProductionPaused
from Script.FactoryGame import FGBuildableFactory
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_StandbyButton import ExecuteUbergraph_Widget_StandbyButton.K2Node_CustomEvent_productionIsPaused
from Game.FactoryGame.Interface.UI.Assets.Shared.StandbyButtonUnpressed import StandbyButtonUnpressed
from Script.UMG import WidgetAnimation
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import UserWidget
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.UMG import GetOwningPlayerPawn
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_StandbyButton import ExecuteUbergraph_Widget_StandbyButton
from Script.CoreUObject import Vector2D
from Script.SlateCore import SlateColor
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Game.FactoryGame.Interface.UI.Audio.StandbyButton.Play_UI_StandBy_Ticked import Play_UI_StandBy_Ticked
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_StandbyButton import ExecuteUbergraph_Widget_StandbyButton.K2Node_Event_IsDesignTime
from Script.AkAudio import AkComponent
from Game.FactoryGame.Interface.UI.Audio.StandbyButton.Play_UI_StandBy_Hover_Powered import Play_UI_StandBy_Hover_Powered
from Script.CoreUObject import LinearColor

class Widget_StandbyButton(UserWidget):
    hover_noPower: Ptr[WidgetAnimation]
    hover: Ptr[WidgetAnimation]
    OnStandbyClicked: FMulticastScriptDelegate
    mSoundButtonOnOff: bool
    mIsProductionPaused: bool
    mBuildableFactory: Ptr[FGBuildableFactory]
    mUseLegacyImplementation: bool
    
    def SetIsProductionPaused(self, IsPaused: bool):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mBuildableFactory)
        if not ReturnValue:
            goto('L296')
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_0)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L296')
        ReturnValue_1: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_1.Server_SetIsProductionPausedOnFactory(self.mBuildableFactory, IsPaused)
        self.SetStandbyButtonBrush(IsPaused)
    

    def BndEvt__mStandbyButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_StandbyButton(1656)
    

    def SetStandbyButtonBrush(self, productionIsPaused: bool):
        ExecuteUbergraph_Widget_StandbyButton.K2Node_CustomEvent_productionIsPaused = productionIsPaused #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_StandbyButton(1293)
    

    def BndEvt__mStandbyButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_StandbyButton(1057)
    

    def BndEvt__mStandbyButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_StandbyButton(1675)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_StandbyButton.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_StandbyButton(1775)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_StandbyButton(1776)
    

    def ExecuteUbergraph_Widget_StandbyButton(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mBuildableFactory)
        if not ReturnValue:
            goto('L146')
        ReturnValue_0: bool = self.mBuildableFactory.IsProductionPaused()
        self.SetStandbyButtonBrush(ReturnValue_0)
        goto(ExecutionFlow.Pop())
        # Label 146
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 15, UUID = 852787722, ExecutionFunction = "ExecuteUbergraph_Widget_StandbyButton", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 223
        SlateBrush.ImageSize = Vector2D(X = 18, Y = 37)
        SlateBrush.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush.TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0)
        SlateBrush.ResourceObject = StandbyButtonPressed
        SlateBrush.DrawAs = 3
        SlateBrush.Tiling = 0
        SlateBrush.Mirroring = 0
        
        SlateBrush = None
        self.mButtonImage.SetBrush(Ref[SlateBrush])
        self.mButtonOverlay.SetRenderTranslation(Vector2D(X = 0, Y = -12))
        self.mSoundButtonOnOff = True
        goto(ExecutionFlow.Pop())
        # Label 640
        SlateBrush1.ImageSize = Vector2D(X = 18, Y = 37)
        SlateBrush1.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush1.TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0)
        SlateBrush1.ResourceObject = StandbyButtonUnpressed
        SlateBrush1.DrawAs = 3
        SlateBrush1.Tiling = 0
        SlateBrush1.Mirroring = 0
        
        SlateBrush1 = None
        self.mButtonImage.SetBrush(Ref[SlateBrush1])
        self.mButtonOverlay.SetRenderTranslation(Vector2D(X = 0, Y = -12))
        self.mSoundButtonOnOff = False
        goto(ExecutionFlow.Pop())
        if not self.mIsProductionPaused:
            goto('L1118')
        ReturnValue3: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.hover_noPower, 0, 1, 1, 1)
        goto(ExecutionFlow.Pop())
        # Label 1118
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.hover, 0, 1, 1, 1)
        goto(ExecutionFlow.Pop())
        # Label 1165
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.hover, 0, 1, 0, 1)
        ReturnValue1_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_StandBy_Hover_Powered, ReturnValue1_0, True)
        goto(ExecutionFlow.Pop())
        self.mIsProductionPaused = productionIsPaused
        if not self.mIsProductionPaused:
            goto('L223')
        goto('L640')
        # Label 1331
        self.OnStandbyClicked.ProcessMulticastDelegate()
        if not self.mSoundButtonOnOff:
            goto('L1446')
        ReturnValue_2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_StandBy_UnTicked, ReturnValue_2, True)
        goto(ExecutionFlow.Pop())
        # Label 1446
        ReturnValue_2 = self.GetOwningPlayerPawn()
        ReturnValue3_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_StandBy_Ticked, ReturnValue_2, True)
        goto(ExecutionFlow.Pop())
        # Label 1528
        ReturnValue2_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.hover_noPower, 0, 1, 0, 1)
        ReturnValue1_0 = self.GetOwningPlayerPawn()
        ReturnValue1_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_StandBy_Hover_UnPowered, ReturnValue1_0, True)
        goto(ExecutionFlow.Pop())
        if not self.mIsProductionPaused:
            goto('L1165')
        goto('L1528')
        ReturnValue2_1: bool = Not_PreBool(self.mUseLegacyImplementation)
        if not ReturnValue2_1:
            goto('L1331')
        ReturnValue1_2: bool = Not_PreBool(self.mIsProductionPaused)
        self.SetIsProductionPaused(ReturnValue1_2)
        goto('L1331')
        goto(ExecutionFlow.Pop())
        ReturnValue_4: bool = Not_PreBool(self.mUseLegacyImplementation)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        goto('L15')
    

    def OnStandbyClicked__DelegateSignature(self):
        pass
    
