
from codegen.ue4_stub import *

from Script.UMG import GetParent
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop_CategoryButtons import ExecuteUbergraph_BPW_ResourceSinkShop_CategoryButtons.K2Node_Event_IsDesignTime
from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Script.UMG import PanelWidget
from Script.UMG import GetChildIndex
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSinkShop_CategoryButtons import ExecuteUbergraph_BPW_ResourceSinkShop_CategoryButtons
from Script.UMG import SetColorAndOpacity
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class BPW_ResourceSinkShop_CategoryButtons(UserWidget):
    OnHover: Ptr[WidgetAnimation]
    OnClicked: FMulticastScriptDelegate
    mName: FText = NSLOCTEXT("", "23D49A0F43B1B60029FA7B9BF439E74A", "Name")
    mIsSelected: bool
    
    def SetIsSelected(self, isSelected: bool):
        self.mIsSelected = isSelected
        Variable: uint8 = 3
        Variable1: uint8 = 2
        Variable_0: bool = self.mIsSelected
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mSelectedMarker.SetVisibility(switch.get(Variable_0, None))
    

    def UpdateTextStyling(self):
        Variable: LinearColor = LinearColor(R = 0.13286800682544708, G = 0.13286800682544708, B = 0.13563300669193268, A = 1)
        Variable1: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        ReturnValue: bool = self.IsHovered()
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        SlateColor.SpecifiedColor = switch.get(Variable_0, None)
        SlateColor.ColorUseRule = 0
        self.mNameObject.SetColorAndOpacity(SlateColor)
    

    def SetName(self, mName: FText):
        self.mName = mName
        self.mNameObject.SetText(self.mName)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_CategoryButtons(10)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_CategoryButtons(208)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_CategoryButtons(259)
    

    def PreConstruct(self):
        ExecuteUbergraph_BPW_ResourceSinkShop_CategoryButtons.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ResourceSinkShop_CategoryButtons(264)
    

    def ExecuteUbergraph_BPW_ResourceSinkShop_CategoryButtons(self):
        ReturnValue: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_0: int32 = ReturnValue.GetChildIndex(self)
        self.OnClicked.ProcessMulticastDelegate(ReturnValue_0)
        self.SetIsSelected(True)
        # End
        # Label 129
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OnHover, 0, 1, 1, 1.2000000476837158)
        # End
        # Label 180
        self.SetName(self.mName)
        # End
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OnHover, 0, 1, 0, 1)
        # End
        goto('L129')
        goto('L180')
    

    def OnClicked__DelegateSignature(self, index: int32):
        pass
    
