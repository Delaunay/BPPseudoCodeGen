
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Menu.Widget_OptionsRow import ExecuteUbergraph_Widget_OptionsRow.K2Node_Event_MouseEvent
from Game.FactoryGame.Interface.UI.Menu.Widget_OptionsRow import ExecuteUbergraph_Widget_OptionsRow
from Game.FactoryGame.Interface.UI.Menu.Widget_OptionsRow import ExecuteUbergraph_Widget_OptionsRow.K2Node_Event_MouseEvent1
from Script.UMG import GetChildAt
from Script.Engine import PlayerController
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Interface.UI.Menu.Widget_OptionsRow import ExecuteUbergraph_Widget_OptionsRow.K2Node_Event_MyGeometry
from Script.UMG import Widget
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_MouseOver import Play_UI_MainMenu_MouseOver
from Game.FactoryGame.Interface.UI.Menu.Widget_OptionsRow import ExecuteUbergraph_Widget_OptionsRow.K2Node_Event_IsDesignTime
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import GetContent
from Script.FactoryGame import FGOptionsValueController
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.Menu.Widget_OptionSelection import Widget_OptionSelection

class Widget_OptionsRow(UserWidget):
    mText: FText = NSLOCTEXT("", "D7A93C784EE53997BE8BA8A32DB9EDB4", "Title")
    OnClicked: FMulticastScriptDelegate
    OptionSlotContent: Ptr[FGOptionsValueController]
    
    def OnMouseEnter(self):
        ExecuteUbergraph_Widget_OptionsRow.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_OptionsRow.K2Node_Event_MouseEvent1 = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_OptionsRow(10)
    

    def OnMouseLeave(self):
        ExecuteUbergraph_Widget_OptionsRow.K2Node_Event_MouseEvent = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_OptionsRow(286)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_OptionsRow.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_OptionsRow(412)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_OptionsRow(462)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_OptionsRow(588)
    

    def ExecuteUbergraph_Widget_OptionsRow(self):
        ReturnValue: Ptr[Widget] = self.mOptionSlot.GetContent()
        Selection1: Ptr[Widget_OptionSelection] = Cast[Widget_OptionSelection](ReturnValue)
        bSuccess2: bool = Selection1
        if not bSuccess2:
            goto('L624')
        # End
        # Label 136
        ReturnValue_0: Ptr[Widget] = self.mOptionSlot.GetChildAt(0)
        Controller: Ptr[FGOptionsValueController] = Cast[FGOptionsValueController](ReturnValue_0)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L624')
        self.OptionSlotContent = Controller
        # End
        ReturnValue = self.mOptionSlot.GetContent()
        Selection: Ptr[Widget_OptionSelection] = Cast[Widget_OptionSelection](ReturnValue)
        bSuccess1: bool = Selection
        if not bSuccess1:
            goto('L624')
        # End
        self.mTitle.SetText(self.mText)
        goto('L136')
        self.OptionSlotContent.OnRowHovered()
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_MouseOver, ReturnValue_1, True)
        # End
        self.OptionSlotContent.OnRowUnhovered()
    

    def OnClicked__DelegateSignature(self):
        pass
    
