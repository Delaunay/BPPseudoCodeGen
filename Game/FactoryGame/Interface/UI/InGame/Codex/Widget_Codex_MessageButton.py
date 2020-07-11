
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import EqualEqual_ClassClass
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_MessageButton import ExecuteUbergraph_Widget_Codex_MessageButton
from Script.Engine import Pawn
from Script.FactoryGame import FGPlayerState
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_MouseOver import Play_UI_WorkBench_MouseOver
from Script.Engine import Not_PreBool
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_Select import Play_UI_WorkBench_Select
from Script.Engine import PlayerController
from Script.UMG import ESlateVisibility
from Script.FactoryGame import FGMessageBase
from Script.Engine import BooleanOR
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import UserWidget
from Script.FactoryGame import ReadMessage
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import Widget_Codex_Container
from Script.AkAudio import AkComponent
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_MessageButton import ExecuteUbergraph_Widget_Codex_MessageButton.K2Node_Event_IsDesignTime
from Script.CoreUObject import LinearColor

class Widget_Codex_MessageButton(UserWidget):
    OnClicked: FMulticastScriptDelegate
    mOwningCodex: Ptr[Widget_Codex_Container]
    mMessage: TSubclassOf[FGMessageBase]
    mMessageHasBeenRead: bool
    
    def CheckIsSelected(self):
        ReturnValue: bool = EqualEqual_ClassClass(self.mMessage, self.mOwningCodex.mSelectedMessage)
        mIsSelected = ReturnValue
    

    def WasMessageReadColorFeedback(self):
        ReturnValue: bool = EqualEqual_ClassClass(self.mMessage, self.mOwningCodex.mSelectedMessage)
        ReturnValue_0: bool = self.IsHovered()
        ReturnValue_1: bool = BooleanOR(ReturnValue_0, ReturnValue)
        if not ReturnValue_1:
            goto('L223')
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_2: LinearColor = GraphicsWhite
        goto('L376')
        # Label 223
        if not self.mMessageHasBeenRead:
            goto('L294')
        ReturnValue_2 = LinearColor(R = 0.09530699998140335, G = 0.09530699998140335, B = 0.09530699998140335, A = 1)
        goto('L376')
        
        Text = None
        Graphics = None
        # Label 294
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_2 = Graphics
    

    def WasMessageReadFeedbackVisibility(self):
        Variable: uint8 = 2
        Variable1: uint8 = 0
        Variable_0: bool = self.mMessageHasBeenRead
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue = switch.get(Variable_0, None)
    

    def GetSelectedMessageFeedbackVisibility(self):
        Variable: uint8 = 0
        Variable1: uint8 = 1
        ReturnValue: bool = EqualEqual_ClassClass(self.mMessage, self.mOwningCodex.mSelectedMessage)
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_0: uint8 = switch.get(Variable_0, None)
    

    def MessageWasClicked(self):
        self.mOwningCodex.mSelectedMessage = self.mMessage
        self.mOwningCodex.mMessage.AddContent(self.mMessage)
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](ReturnValue.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
            goto('L322')
        State.ReadMessage(self.mMessage)
        self.mMessageHasBeenRead = True
        self.mOwningCodex.UpdateNotifications(None)
    

    def GetMessageName(self):
        self.mMessageName.SetText(self.mMessage.ClassDefaultObject.mTitle)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_Codex_MessageButton.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Codex_MessageButton(29)
    

    def BndEvt__mMessageButton_K2Node_ComponentBoundEvent_1_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Codex_MessageButton(34)
    

    def BndEvt__mMessageButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Codex_MessageButton(231)
    

    def ExecuteUbergraph_Widget_Codex_MessageButton(self):
        # Label 10
        self.GetMessageName()
        # End
        goto('L10')
        self.MessageWasClicked()
        ReturnValue1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_Select, ReturnValue1, True)
        ReturnValue: bool = Not_PreBool(Variable)
        Variable: bool = ReturnValue
        if not Variable:
            goto('L215')
        self.mMessageHasBeenRead = Variable
        # End
        # Label 215
        self.mMessageHasBeenRead = True
        # End
        ReturnValue_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_MouseOver, ReturnValue_0, True)
    

    def OnClicked__DelegateSignature(self):
        pass
    
