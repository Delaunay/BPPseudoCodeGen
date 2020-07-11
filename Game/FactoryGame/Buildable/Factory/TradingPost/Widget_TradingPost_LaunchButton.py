
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Script.FactoryGame import GetActiveSchematic
from Script.Engine import Pawn
from Script.Engine import GreaterEqual_IntInt
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Interface.UI.Audio.Play_UI_LaunchButtonExplosion import Play_UI_LaunchButtonExplosion
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_LaunchButton import ExecuteUbergraph_Widget_TradingPost_LaunchButton.K2Node_CustomEvent_IsTutorialPhase
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_LaunchButton import ExecuteUbergraph_Widget_TradingPost_LaunchButton
from Script.Engine import PlayerController
from Script.Engine import GameStateBase
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Script.FactoryGame import GetTechTier
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_LaunchButton import ExecuteUbergraph_Widget_TradingPost_LaunchButton.K2Node_Event_MyGeometry
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import EqualEqual_IntInt
from Script.Engine import SetMouseCursorWidget
from Script.AkAudio import AkAudioEvent
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGGameState
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_LaunchButton import ExecuteUbergraph_Widget_TradingPost_LaunchButton.K2Node_Event_InDeltaTime
from Script.FactoryGame import FGButtonWidget
from Script.FactoryGame import FGBuildableTradingPost
from Script.UMG import WidgetAnimation
from Script.FactoryGame import FGSchematic
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import IsShipAtTradingPost
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.UMG import GetOwningPlayerPawn
from Script.Engine import RandomIntegerInRange
from Script.FactoryGame import FGSchematicManager
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Script.Engine import GetGameState
from Script.FactoryGame import Default__FGSchematic
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost import Widget_TradingPost
from Script.FactoryGame import IsSchematicPaidOff
from Game.FactoryGame.Interface.UI.InGame.Cursor.Widget_DefaultCursor import Widget_DefaultCursor
from Game.FactoryGame.Interface.UI.Audio.LaunchButton.Play_UI_LaunchShipButton import Play_UI_LaunchShipButton
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Game.FactoryGame.Interface.UI.Audio.UpgradeButton.Play_UI_UpgradeButtonRumble import Play_UI_UpgradeButtonRumble
from Script.AkAudio import AkComponent
from Script.FactoryGame import Default__FGSchematicManager
from Script.Engine import IsValidClass
from Game.FactoryGame.Interface.UI.InGame.Cursor.Widget_HandSlamCursorHard import Widget_HandSlamCursorHard

class Widget_TradingPost_LaunchButton(FGButtonWidget):
    PressAnim: Ptr[WidgetAnimation]
    HoverAnim: Ptr[WidgetAnimation]
    mTradingPost: Ptr[FGBuildableTradingPost]
    mTradingPostWidget: Ptr[Widget_TradingPost]
    IsClicked: bool
    padding = Namespace(Bottom=2, Left=2, Right=2, Top=2)
    bIsFocusable = True
    
    def Test(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue)
        bSuccess: bool = State
        if not bSuccess:
            goto('L356')
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(State)
        ReturnValue_1: TSubclassOf[FGSchematic] = ReturnValue_0.GetActiveSchematic()
        ReturnValue_2: int32 = Default__FGSchematic.GetTechTier(ReturnValue_1)
        ReturnValue_3: bool = GreaterEqual_IntInt(ReturnValue_2, 1)
        ReturnValue_4: bool = Not_PreBool(ReturnValue_3)
        NewParam = ReturnValue_4
    

    def IsTutorialPhase(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue)
        bSuccess: bool = State
        if not bSuccess:
            goto('L356')
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(State)
        ReturnValue_1: TSubclassOf[FGSchematic] = ReturnValue_0.GetActiveSchematic()
        ReturnValue_2: int32 = Default__FGSchematic.GetTechTier(ReturnValue_1)
        ReturnValue_3: bool = GreaterEqual_IntInt(ReturnValue_2, 1)
        ReturnValue_4: bool = Not_PreBool(ReturnValue_3)
        IsTutorialPhase = ReturnValue_4
    

    def GetButtonClickedVisibility(self):
        if not self.IsClicked:
            goto('L39')
        ReturnValue = 2
        goto('L59')
        # Label 39
        ReturnValue = 0
    

    def IsSchematicPaidOff(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue)
        bSuccess: bool = State
        if not bSuccess:
            goto('L459')
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(State)
        ReturnValue_1: TSubclassOf[FGSchematic] = ReturnValue_0.GetActiveSchematic()
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_1)
        if not ReturnValue_2:
            goto('L448')
        ReturnValue_0 = Default__FGSchematicManager.Get(State)
        ReturnValue_1 = ReturnValue_0.GetActiveSchematic()
        ReturnValue_3: bool = ReturnValue_0.IsSchematicPaidOff(ReturnValue_1)
        ReturnValue_4: bool = ReturnValue_3
        goto('L459')
        # Label 448
        ReturnValue_4 = False
    

    def GetTextFeedback(self):
        ReturnValue: bool = self.IsSchematicPaidOff()
        if not ReturnValue:
            goto('L80')
        ReturnValue_0: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 58, 'Value': 'Ready To Launch'}"
        goto('L387')
        # Label 80
        ReturnValue_1: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue_1)
        bSuccess: bool = State
        ReturnValue_2: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(State)
        ReturnValue_3: bool = ReturnValue_2.IsShipAtTradingPost()
        ReturnValue_4: bool = Not_PreBool(ReturnValue_3)
        if not ReturnValue_4:
            goto('L349')
        ReturnValue_0 = 
        goto('L387')
        # Label 349
        ReturnValue_0 = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 369, 'Value': 'Resources Needed'}"
    

    def GetLaunchButtonVisibility(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue)
        bSuccess: bool = State
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(State)
        ReturnValue_1: bool = ReturnValue_0.IsShipAtTradingPost()
        if not ReturnValue_1:
            goto('L240')
        ReturnValue_2: uint8 = 0
        goto('L260')
        # Label 240
        ReturnValue_2 = 1
    

    def GetLaunchButtonEnabled(self):
        ReturnValue: bool = self.IsSchematicPaidOff()
        ReturnValue_0: bool = ReturnValue
    

    def Tick(self):
        ExecuteUbergraph_Widget_TradingPost_LaunchButton.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_TradingPost_LaunchButton.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TradingPost_LaunchButton(402)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_65_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TradingPost_LaunchButton(403)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_75_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TradingPost_LaunchButton(602)
    

    def BndEvt__Button_26_K2Node_ComponentBoundEvent_100_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TradingPost_LaunchButton(816)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_TradingPost_LaunchButton(1061)
    

    def mLaunchShip(self, IsTutorialPhase: bool):
        ExecuteUbergraph_Widget_TradingPost_LaunchButton.K2Node_CustomEvent_IsTutorialPhase = IsTutorialPhase #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TradingPost_LaunchButton(1161)
    

    def ExecuteUbergraph_Widget_TradingPost_LaunchButton(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_LaunchButtonExplosion, ReturnValue, True)
        self.mTradingPostWidget.mShakeWindow()
        self.IsClicked = True
        Default__KismetSystemLibrary.Delay(self, 1, LatentActionInfo(Linkage = 220, UUID = -1834158604, ExecutionFunction = "ExecuteUbergraph_Widget_TradingPost_LaunchButton", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 220
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_1)
        bSuccess: bool = Controller
        ReturnValue_2: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_2.Server_LaunchShip()
        goto(ExecutionFlow.Pop())
        goto('L220')
        goto(ExecutionFlow.Pop())
        ReturnValue_3: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.HoverAnim, 0, 1, 0, 1)
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue2: Ptr[Widget_DefaultCursor] = Default__WidgetBlueprintLibrary.Create(self, Widget_DefaultCursor, ReturnValue3)
        ReturnValue3 = self.GetOwningPlayer()
        ReturnValue3.SetMouseCursorWidget(1, ReturnValue2)
        goto(ExecutionFlow.Pop())
        if not self.IsClicked:
            goto('L617')
        goto(ExecutionFlow.Pop())
        # Label 617
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.HoverAnim, 0, 1, 1, 1)
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_4: Ptr[Widget_DefaultCursor] = Default__WidgetBlueprintLibrary.Create(self, Widget_DefaultCursor, ReturnValue1_0)
        ReturnValue1_0 = self.GetOwningPlayer()
        ReturnValue1_0.SetMouseCursorWidget(1, ReturnValue_4)
        goto(ExecutionFlow.Pop())
        self.mLaunchShip(False)
        goto(ExecutionFlow.Pop())
        # Label 832
        ReturnValue2_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_1: Ptr[Widget_HandSlamCursorHard] = Default__WidgetBlueprintLibrary.Create(self, Widget_HandSlamCursorHard, ReturnValue2_0)
        ReturnValue2_0 = self.GetOwningPlayer()
        ReturnValue2_0.SetMouseCursorWidget(1, ReturnValue1_1)
        Default__KismetSystemLibrary.Delay(self, 0.5, LatentActionInfo(Linkage = 15, UUID = 839296579, ExecutionFunction = "ExecuteUbergraph_Widget_TradingPost_LaunchButton", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.IsClicked = False
        goto(ExecutionFlow.Pop())
        # Label 1073
        self.IsClicked = True
        Default__KismetSystemLibrary.Delay(self, 1, LatentActionInfo(Linkage = 397, UUID = -774958235, ExecutionFunction = "ExecuteUbergraph_Widget_TradingPost_LaunchButton", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        if not IsTutorialPhase:
            goto('L1385')
        # Label 1175
        Variable: Ptr[AkAudioEvent] = Play_UI_LaunchShipButton
        ReturnValue = self.GetOwningPlayerPawn()
        Variable1: Ptr[AkAudioEvent] = Play_UI_UpgradeButtonRumble
        
        IsTutorialPhase = None
        self.IsTutorialPhase(Ref[IsTutorialPhase])
        Variable_0: bool = IsTutorialPhase
        
        switch = {
            False: Variable,
            True: Variable1
        }
        ReturnValue1_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(switch.get(Variable_0, None), ReturnValue, True)
        goto('L1073')
        # Label 1385
        ReturnValue_5: int32 = RandomIntegerInRange(0, 100)
        ReturnValue_6: bool = EqualEqual_IntInt(ReturnValue_5, 1)
        if not ReturnValue_6:
            goto('L1476')
        goto('L832')
        # Label 1476
        self.mTradingPostWidget.mShakeWindow()
        goto('L1175')
    
