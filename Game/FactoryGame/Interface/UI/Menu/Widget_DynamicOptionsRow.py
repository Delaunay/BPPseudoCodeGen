
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.FactoryGame import GetOptionRowData
from Script.FactoryGame import GetValueControllerWidget
from Game.FactoryGame.Interface.UI.Menu.Widget_DynamicOptionsRow import ExecuteUbergraph_Widget_DynamicOptionsRow.K2Node_Event_IsDesignTime
from Script.Engine import PlayerController
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_MouseOver import Play_UI_MainMenu_MouseOver
from Script.UMG import GetContent
from Game.FactoryGame.Interface.UI.Menu.Widget_DynamicOptionsRow import ExecuteUbergraph_Widget_DynamicOptionsRow.K2Node_Event_MouseEvent1
from Game.FactoryGame.Interface.UI.Menu.Widget_OptionSelection import Widget_OptionSelection
from Script.UMG import Widget
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import FGDynamicOptionsRow
from Script.FactoryGame import OptionRowData
from Game.FactoryGame.Interface.UI.Menu.Widget_DynamicOptionsRow import ExecuteUbergraph_Widget_DynamicOptionsRow
from Script.AkAudio import AkComponent
from Game.FactoryGame.Interface.UI.Menu.Widget_DynamicOptionsRow import ExecuteUbergraph_Widget_DynamicOptionsRow.K2Node_Event_MouseEvent
from Game.FactoryGame.Interface.UI.Menu.Widget_DynamicOptionsRow import ExecuteUbergraph_Widget_DynamicOptionsRow.K2Node_Event_MyGeometry
from Script.FactoryGame import FGOptionsValueController

class Widget_DynamicOptionsRow(FGDynamicOptionsRow):
    mText: FText = NSLOCTEXT("", "049701054A0384F5F64FAB86E044BF2A", "Title")
    OnClicked: FMulticastScriptDelegate
    
    def InitOptionRow(self):
        ReturnValue: Ptr[FGOptionsValueController] = self.GetValueControllerWidget()
        ReturnValue_0: Ptr[PanelSlot] = self.mOptionSlot.AddChild(ReturnValue)
        ReturnValue_1: OptionRowData = self.GetOptionRowData()
        self.mTitle.SetText(ReturnValue_1.OptionName)
    

    def OnMouseEnter(self):
        ExecuteUbergraph_Widget_DynamicOptionsRow.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_DynamicOptionsRow.K2Node_Event_MouseEvent1 = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_DynamicOptionsRow(71)
    

    def OnMouseLeave(self):
        ExecuteUbergraph_Widget_DynamicOptionsRow.K2Node_Event_MouseEvent = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_DynamicOptionsRow(197)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_DynamicOptionsRow.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_DynamicOptionsRow(323)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_DynamicOptionsRow(373)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_DynamicOptionsRow(519)
    

    def OnOptionRowInit(self):
        self.ExecuteUbergraph_Widget_DynamicOptionsRow(580)
    

    def OnOptionValueUpdated(self):
        self.ExecuteUbergraph_Widget_DynamicOptionsRow(599)
    

    def ExecuteUbergraph_Widget_DynamicOptionsRow(self):
        # Label 10
        ReturnValue: Ptr[FGOptionsValueController] = self.GetValueControllerWidget()
        ReturnValue.OnOptionValueUpdated()
        # End
        ReturnValue_0: Ptr[Widget] = self.mOptionSlot.GetContent()
        Selection1: Ptr[Widget_OptionSelection] = Cast[Widget_OptionSelection](ReturnValue_0)
        bSuccess1: bool = Selection1
        if not bSuccess1:
            goto('L604')
        # End
        ReturnValue_0 = self.mOptionSlot.GetContent()
        Selection: Ptr[Widget_OptionSelection] = Cast[Widget_OptionSelection](ReturnValue_0)
        bSuccess: bool = Selection
        if not bSuccess:
            goto('L604')
        # End
        self.mTitle.SetText(self.mText)
        # End
        ReturnValue1: Ptr[FGOptionsValueController] = self.GetValueControllerWidget()
        ReturnValue1.OnRowHovered()
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_MouseOver, ReturnValue_1, True)
        # End
        ReturnValue2: Ptr[FGOptionsValueController] = self.GetValueControllerWidget()
        ReturnValue2.OnRowUnhovered()
        # End
        self.InitOptionRow()
        # End
        goto('L10')
    

    def OnClicked__DelegateSignature(self):
        pass
    
