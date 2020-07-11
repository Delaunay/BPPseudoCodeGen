
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Script.FactoryGame import GetActiveSchematic
from Script.Engine import Pawn
from Script.Engine import GreaterEqual_IntInt
from Game.FactoryGame.Interface.UI.Audio.UpgradeButton.Play_UI_UpgradeButtonMO import Play_UI_UpgradeButtonMO
from Script.Engine import Not_PreBool
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_LanuchButtonPlatform import ExecuteUbergraph_Widget_TradingPost_LanuchButtonPlatform.K2Node_Event_InDeltaTime
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_LanuchButtonPlatform import ExecuteUbergraph_Widget_TradingPost_LanuchButtonPlatform.K2Node_Event_MyGeometry
from Script.Engine import GameStateBase
from Script.UMG import PlayAnimation
from Script.UMG import Unhandled
from Script.UMG import ESlateVisibility
from Script.FactoryGame import GetTechTier
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import Destruct
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGGameState
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_LanuchButtonPlatform import ExecuteUbergraph_Widget_TradingPost_LanuchButtonPlatform
from Game.FactoryGame.Interface.UI.Audio.LaunchButton.Play_UI_LaunchShipReveal import Play_UI_LaunchShipReveal
from Script.UMG import WidgetAnimation
from Script.FactoryGame import FGSchematic
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import UserWidget
from Script.UMG import GetOwningPlayerPawn
from Script.FactoryGame import FGSchematicManager
from Script.UMG import UMGSequencePlayer
from Script.Engine import GetGameState
from Script.FactoryGame import Default__FGSchematic
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost import Widget_TradingPost
from Script.FactoryGame import IsSchematicPaidOff
from Game.FactoryGame.Interface.UI.Audio.UpgradeButton.Play_UI_UpgradeButtonRumble import Play_UI_UpgradeButtonRumble
from Game.FactoryGame.Interface.UI.Audio.LaunchButton.Play_UI_LaunchShipButton import Play_UI_LaunchShipButton
from Game.FactoryGame.Interface.UI.Audio.UpgradeButton.Play_UI_UpgradeButtonReady import Play_UI_UpgradeButtonReady
from Script.AkAudio import AkComponent
from Script.FactoryGame import Default__FGSchematicManager
from Script.Engine import IsValidClass
from Script.Engine import PrintString
from Script.UMG import EventReply
from Script.CoreUObject import LinearColor

class Widget_TradingPost_LanuchButtonPlatform(UserWidget):
    ShowTutorialButton: Ptr[WidgetAnimation]
    TutorialButtonHoverAnim: Ptr[WidgetAnimation]
    TutorialButtonGlow: Ptr[WidgetAnimation]
    ButtonGlowPulse: Ptr[WidgetAnimation]
    ShowButton: Ptr[WidgetAnimation]
    IsButtonVisible: bool
    IsTutorialPhase: bool
    mTradingPost: Ptr[Widget_TradingPost]
    
    def OnMouseButtonDown(self):
        self.Widget_UI_ParticleManager.CreateParticle()
        ReturnValue: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_0: EventReply = ReturnValue
    

    def GetVisibility_0(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue)
        bSuccess: bool = State
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(State)
        ReturnValue_1: TSubclassOf[FGSchematic] = ReturnValue_0.GetActiveSchematic()
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_1)
        if not ReturnValue_2:
            goto('L305')
        if not self.IsTutorialPhase:
            goto('L330')
        ReturnValue_3: uint8 = 0
        goto('L350')
        # Label 305
        ReturnValue_3 = 1
        goto('L350')
        # Label 330
        ReturnValue_3 = 1
    

    def mShowLaunchButton(self):
        self.ExecuteUbergraph_Widget_TradingPost_LanuchButtonPlatform(180)
    

    def Tick(self):
        ExecuteUbergraph_Widget_TradingPost_LanuchButtonPlatform.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_TradingPost_LanuchButtonPlatform.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TradingPost_LanuchButtonPlatform(303)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_63_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TradingPost_LanuchButtonPlatform(2165)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_92_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TradingPost_LanuchButtonPlatform(2303)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_137_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TradingPost_LanuchButtonPlatform(2360)
    

    def OnUpgradeHub(self):
        self.ExecuteUbergraph_Widget_TradingPost_LanuchButtonPlatform(2722)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_TradingPost_LanuchButtonPlatform(2727)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_TradingPost_LanuchButtonPlatform(2814)
    

    def CreateSmoke(self):
        self.ExecuteUbergraph_Widget_TradingPost_LanuchButtonPlatform(2915)
    

    def ExecuteUbergraph_Widget_TradingPost_LanuchButtonPlatform(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ButtonGlowPulse, 0, 0, 0, 1)
        ReturnValue2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue2_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_UpgradeButtonReady, ReturnValue2, True)
        goto(ExecutionFlow.Pop())
        # Label 143
        self.mTradingPost.CreateSmoke()
        goto(ExecutionFlow.Pop())
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ShowButton, 0, 1, 0, 1)
        Default__KismetSystemLibrary.Delay(self, 3, LatentActionInfo(Linkage = 15, UUID = -1170651683, ExecutionFunction = "ExecuteUbergraph_Widget_TradingPost_LanuchButtonPlatform", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue2_1: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State2: Ptr[FGGameState] = Cast[FGGameState](ReturnValue2_1)
        bSuccess2: bool = State2
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        ReturnValue2_2: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(State2)
        ReturnValue2_3: TSubclassOf[FGSchematic] = ReturnValue2_2.GetActiveSchematic()
        ReturnValue2_4: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue2_3)
        if not ReturnValue2_4:
           goto(ExecutionFlow.Pop())
        ReturnValue2_2 = Default__FGSchematicManager.Get(State2)
        ReturnValue2_3 = ReturnValue2_2.GetActiveSchematic()
        ReturnValue_0: int32 = Default__FGSchematic.GetTechTier(ReturnValue2_3)
        ReturnValue_1: bool = GreaterEqual_IntInt(ReturnValue_0, 1)
        ReturnValue_2: bool = Not_PreBool(ReturnValue_1)
        self.IsTutorialPhase = ReturnValue_2
        if not self.IsButtonVisible:
            goto('L824')
        goto(ExecutionFlow.Pop())
        # Label 824
        if not self.IsTutorialPhase:
            goto('L1496')
        ReturnValue1_0: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State1: Ptr[FGGameState] = Cast[FGGameState](ReturnValue1_0)
        bSuccess1: bool = State1
        ReturnValue1_1: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(State1)
        ReturnValue1_2: TSubclassOf[FGSchematic] = ReturnValue1_1.GetActiveSchematic()
        ReturnValue1_3: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue1_2)
        if not ReturnValue1_3:
           goto(ExecutionFlow.Pop())
        ReturnValue1_0 = Default__GameplayStatics.GetGameState(self)
        State1 = Cast[FGGameState](ReturnValue1_0)
        bSuccess1 = State1
        ReturnValue1_1 = Default__FGSchematicManager.Get(State1)
        ReturnValue1_2 = ReturnValue1_1.GetActiveSchematic()
        ReturnValue1_4: bool = ReturnValue1_1.IsSchematicPaidOff(ReturnValue1_2)
        if not ReturnValue1_4:
            goto('L2127')
        self.IsButtonVisible = True
        self.Widget_GlowingFactoryButton.SetEnabled(True)
        ReturnValue3: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue3_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_UpgradeButtonReady, ReturnValue3, True)
        goto(ExecutionFlow.Pop())
        # Label 1496
        ReturnValue_3: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue_3)
        bSuccess: bool = State
        ReturnValue_4: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(State)
        ReturnValue_5: TSubclassOf[FGSchematic] = ReturnValue_4.GetActiveSchematic()
        ReturnValue_6: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_5)
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        ReturnValue_3 = Default__GameplayStatics.GetGameState(self)
        State = Cast[FGGameState](ReturnValue_3)
        bSuccess = State
        ReturnValue_4 = Default__FGSchematicManager.Get(State)
        ReturnValue_5 = ReturnValue_4.GetActiveSchematic()
        ReturnValue_7: bool = ReturnValue_4.IsSchematicPaidOff(ReturnValue_5)
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        self.IsButtonVisible = True
        self.mShowLaunchButton()
        ReturnValue4: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue4_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_LaunchShipReveal, ReturnValue4, True)
        goto(ExecutionFlow.Pop())
        # Label 2127
        self.Widget_GlowingFactoryButton.SetEnabled(False)
        goto(ExecutionFlow.Pop())
        if not self.IsButtonVisible:
           goto(ExecutionFlow.Pop())
        ReturnValue2_5: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.TutorialButtonHoverAnim, 0, 1, 0, 1)
        ReturnValue1_5: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue1_6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_UpgradeButtonMO, ReturnValue1_5, True)
        goto(ExecutionFlow.Pop())
        if not self.IsButtonVisible:
           goto(ExecutionFlow.Pop())
        ReturnValue3_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.TutorialButtonHoverAnim, 0, 1, 1, 1)
        goto(ExecutionFlow.Pop())
        # Label 2360
        self.mTradingPost.mLaunchShipButton.mLaunchShip(True)
        if not self.IsTutorialPhase:
            goto('L2552')
        ReturnValue5: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue5_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_UpgradeButtonRumble, ReturnValue5, True)
        self.Widget_GlowingFactoryButton.SetEnabled(False)
        goto(ExecutionFlow.Pop())
        # Label 2552
        ReturnValue_8: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_9: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_LaunchShipButton, ReturnValue_8, True)
        Default__KismetSystemLibrary.PrintString(self, "launch event", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
        goto('L2360')
        OutputDelegate.BindUFunction(self, OnUpgradeHub)
        self.Widget_GlowingFactoryButton.mButton.OnClicked.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        self.Destruct()
        Default__KismetSystemLibrary.PrintString(self, "event destruct", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
        goto('L143')
    
