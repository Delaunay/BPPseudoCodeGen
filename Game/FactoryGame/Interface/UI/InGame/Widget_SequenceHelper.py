
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.Widget_SequenceHelper import ExecuteUbergraph_Widget_SequenceHelper
from Script.Engine import Default__KismetInputLibrary
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Script.InputCore import Key
from Script.UMG import AddChildToVerticalBox
from Script.MovieScene import Play
from Script.MovieScene import MovieSceneSequencePlaybackSettings
from Game.FactoryGame.Interface.UI.InGame.Widget_SequenceButton import Widget_SequenceButton
from Script.UMG import SetInputMode_GameOnly
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import GetObjectName
from Script.UMG import GetChildAt
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import Handled
from Script.UMG import SetInputMode_UIOnlyEx
from Script.UMG import Unhandled
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.LevelSequence import GetSequencePlayer
from Script.LevelSequence import LevelSequencePlayer
from Script.LevelSequence import Default__LevelSequencePlayer
from Script.UMG import Widget
from Game.FactoryGame.Character.Player.Char_Player import Char_Player
from Script.LevelSequence import CreateLevelSequencePlayer
from Script.Engine import GetKey
from Script.Engine import EqualEqual_KeyKey
from Script.UMG import UserWidget
from Script.UMG import GetOwningPlayerPawn
from Script.MovieScene import MovieSceneSequenceLoopCount
from Script.UMG import VerticalBoxSlot
from Script.UMG import Create
from Game.FactoryGame.Interface.UI.InGame.Widget_SequenceHelper import ExecuteUbergraph_Widget_SequenceHelper.K2Node_CustomEvent_ClickedButton
from Script.UMG import EventReply

class Widget_SequenceHelper(UserWidget):
    
    
    def OnKeyDown(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_0: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "Escape"))
        if not ReturnValue_0:
            goto('L247')
        self.RemoveFromParent()
        ReturnValue_1: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_2: EventReply = ReturnValue_1
        goto('L324')
        # Label 247
        ReturnValue_3: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_2 = ReturnValue_3
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SequenceHelper(1553)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_SequenceHelper(1638)
    

    def OnClickedWithRef_Event_0(self, ClickedButton: Ptr[Widget_Button]):
        ExecuteUbergraph_Widget_SequenceHelper.K2Node_CustomEvent_ClickedButton = ClickedButton #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SequenceHelper(1761)
    

    def CustomEvent_0(self):
        self.ExecuteUbergraph_Widget_SequenceHelper(2060)
    

    def ExecuteUbergraph_Widget_SequenceHelper(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.RemoveFromParent()
        goto(ExecutionFlow.Pop())
        # Label 30
        ExecutionFlow.Push("L798")
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue: Ptr[Widget_SequenceButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_SequenceButton, ReturnValue2)
        ReturnValue_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[Char_Player] = Cast[Char_Player](ReturnValue_0)
        bSuccess: bool = Player
        
        Player.mSequences = None
        Item = None
        Item = Player.mSequences[Variable]
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue, "mSequence", Item)
        ReturnValue_1: Ptr[VerticalBoxSlot] = self.mBox.AddChildToVerticalBox(ReturnValue)
        ReturnValue_0 = self.GetOwningPlayerPawn()
        Player = Cast[Char_Player](ReturnValue_0)
        bSuccess = Player
        
        Player.mSequences = None
        Item = None
        Item = Player.mSequences[Variable]
        ReturnValue_2: FString = Default__KismetSystemLibrary.GetObjectName(Item)
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_2)
        ReturnValue.mText = ReturnValue_3
        OutputDelegate1.BindUFunction(self, OnClickedWithRef_Event_0)
        ReturnValue.OnClickedWithRef.AddUnique(OutputDelegate1)
        goto(ExecutionFlow.Pop())
        # Label 798
        ReturnValue_4: int32 = Variable + 1
        Variable: int32 = ReturnValue_4
        # Label 867
        ReturnValue_0 = self.GetOwningPlayerPawn()
        Player = Cast[Char_Player](ReturnValue_0)
        bSuccess = Player
        
        Player.mSequences = None
        ReturnValue_5: int32 = len(Player.mSequences)
        ReturnValue_6: bool = Variable <= ReturnValue_5
        if not ReturnValue_6:
            goto('L1117')
        Variable = Variable
        goto('L30')
        # Label 1117
        ReturnValue2 = self.GetOwningPlayer()
        ReturnValue1: Ptr[Widget_SequenceButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_SequenceButton, ReturnValue2)
        ReturnValue1_0: Ptr[VerticalBoxSlot] = self.mBox.AddChildToVerticalBox(ReturnValue1)
        ReturnValue1.mText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1295, 'Value': 'Exit'}"
        OutputDelegate.BindUFunction(self, CustomEvent_0)
        ReturnValue1.OnClicked.AddUnique(OutputDelegate)
        ReturnValue_7: Ptr[Widget] = self.mBox.GetChildAt(0)
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__WidgetBlueprintLibrary.SetInputMode_UIOnlyEx(ReturnValue3, ReturnValue_7, 0)
        goto(ExecutionFlow.Pop())
        # Label 1525
        Variable = 0
        goto('L867')
        ReturnValue_8: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_8.bShowMouseCursor = True
        Variable = 0
        goto('L1525')
        ReturnValue1_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_1.bShowMouseCursor = False
        ReturnValue1_1 = self.GetOwningPlayer()
        Default__WidgetBlueprintLibrary.SetInputMode_GameOnly(ReturnValue1_1)
        goto(ExecutionFlow.Pop())
        Button: Ptr[Widget_SequenceButton] = Cast[Widget_SequenceButton](ClickedButton)
        bSuccess1: bool = Button
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        
        OutActor = None
        ReturnValue_9: Ptr[LevelSequencePlayer] = Default__LevelSequencePlayer.CreateLevelSequencePlayer(self, Button.mSequence, MovieSceneSequencePlaybackSettings(bAutoPlay = False, LoopCount = MovieSceneSequenceLoopCount(Value = 0), PlayRate = 1, StartTime = 0, bRandomStartTime = False, bRestoreState = False, bDisableMovementInput = False, bDisableLookAtInput = False, bHidePlayer = False, bHideHud = False, bDisableCameraCuts = False, bPauseAtEnd = False), Ref[OutActor])
        ReturnValue_10: Ptr[LevelSequencePlayer] = OutActor.GetSequencePlayer()
        ReturnValue_10.Play()
        self.RemoveFromParent()
        goto(ExecutionFlow.Pop())
        goto('L15')
    
