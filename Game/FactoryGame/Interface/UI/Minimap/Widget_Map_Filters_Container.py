
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Minimap.Widget_Map_Filters_Container import ExecuteUbergraph_Widget_Map_Filters_Container.K2Node_ComponentBoundEvent_Text
from Script.Engine import GetEmptyText
from Script.Engine import EqualEqual_TextText
from Script.Engine import BooleanOR
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.Minimap.Widget_Map_Filters_Container import ExecuteUbergraph_Widget_Map_Filters_Container.K2Node_ComponentBoundEvent_Text1
from Game.FactoryGame.Interface.UI.Minimap.Widget_Map_Filters_Container import ExecuteUbergraph_Widget_Map_Filters_Container
from Script.Engine import EqualEqual_ByteByte
from Game.FactoryGame.Interface.UI.Minimap.Widget_Map_Filters_Container import ExecuteUbergraph_Widget_Map_Filters_Container.K2Node_ComponentBoundEvent_CommitMethod
from Script.UMG import WidgetAnimation
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.Engine import NotEqual_TextText
from Script.Engine import Default__KismetTextLibrary

class Widget_Map_Filters_Container(UserWidget):
    SpawnAnim: Ptr[WidgetAnimation]
    OnBeaconSearchChanged: FMulticastScriptDelegate
    OnClearSearchResults: FMulticastScriptDelegate
    
    def AddChildToBeacons(self, Content: Ptr[Widget]):
        ReturnValue: Ptr[PanelSlot] = self.mBeaconContainer.AddChild(Content)
    

    def AddChildToFilters(self, Content: Ptr[Widget]):
        ReturnValue: Ptr[PanelSlot] = self.mFilterContainer.AddChild(Content)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_Map_Filters_Container(10)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Map_Filters_Container(51)
    

    def BndEvt__Widget_InputBox_K2Node_ComponentBoundEvent_1_OnTextChanged__DelegateSignature(self, text: FText):
        ExecuteUbergraph_Widget_Map_Filters_Container.K2Node_ComponentBoundEvent_Text1 = text #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Map_Filters_Container(56)
    

    def BndEvt__Widget_InputBox_K2Node_ComponentBoundEvent_2_OnClearTextClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Map_Filters_Container(237)
    

    def BndEvt__Widget_InputBox_K2Node_ComponentBoundEvent_3_OnTextComitted__DelegateSignature(self, text: FText, CommitMethod: uint8):
        ExecuteUbergraph_Widget_Map_Filters_Container.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Map_Filters_Container.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Map_Filters_Container(261)
    

    def ExecuteUbergraph_Widget_Map_Filters_Container(self):
        self.mFilterContainer.ClearChildren()
        # End
        # End
        ReturnValue1: FText = Default__KismetTextLibrary.GetEmptyText()
        
        Text1 = None
        ReturnValue: bool = Default__KismetTextLibrary.NotEqual_TextText(Ref[Text1], Ref[ReturnValue1])
        if not ReturnValue:
            goto('L213')
        self.OnBeaconSearchChanged.ProcessMulticastDelegate(Text1)
        # End
        # Label 213
        self.OnClearSearchResults.ProcessMulticastDelegate()
        # End
        self.OnClearSearchResults.ProcessMulticastDelegate()
        # End
        ReturnValue_0: FText = Default__KismetTextLibrary.GetEmptyText()
        ReturnValue_1: bool = EqualEqual_ByteByte(CommitMethod, 3)
        
        Text = None
        ReturnValue_2: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[Text], Ref[ReturnValue_0])
        ReturnValue_3: bool = BooleanOR(ReturnValue_2, ReturnValue_1)
        if not ReturnValue_3:
            goto('L473')
        self.OnClearSearchResults.ProcessMulticastDelegate()
    

    def OnClearSearchResults__DelegateSignature(self):
        pass
    

    def OnBeaconSearchChanged__DelegateSignature(self, text: FText):
        pass
    
