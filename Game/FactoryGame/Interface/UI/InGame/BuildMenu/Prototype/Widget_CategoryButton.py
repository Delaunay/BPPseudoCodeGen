
from codegen.ue4_stub import *

from Script.UMG import GetChildAt
from Script.UMG import GetParent
from Script.Engine import Texture2D
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_CategoryButton import Widget_CategoryButton
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_CategoryButton import ExecuteUbergraph_Widget_CategoryButton
from Script.UMG import Widget
from Script.UMG import ESlateVisibility
from Script.UMG import PlayAnimation
from Script.UMG import PanelWidget
from Script.Engine import EqualEqual_ObjectObject
from Script.FactoryGame import FGButtonWidget
from Script.UMG import GetChildIndex
from Script.UMG import GetChildrenCount
from Script.UMG import WidgetAnimation
from Script.UMG import SetColorAndOpacity
from Script.CoreUObject import LinearColor

class Widget_CategoryButton(FGButtonWidget):
    OnHover: Ptr[WidgetAnimation]
    mIsCategoryVisible: bool = True
    OnClicked: FMulticastScriptDelegate
    mName: FText = NSLOCTEXT("", "1564FD144E447FEE1B9D939C6CEC2E0D", "None")
    mIcon: Ptr[Texture2D]
    mIsSelected: bool
    
    def SetAsSelected(self):
        self.mIsSelected = True
        self.UnselectOtherCategoryButtons()
    

    def UnselectOtherCategoryButtons(self):
        ExecutionFlow.Push("L569")
        Variable: int32 = 0
        # Label 28
        ReturnValue: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_0: int32 = ReturnValue.GetChildrenCount()
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L495")
        ReturnValue = self.GetParent()
        ReturnValue_2: Ptr[Widget] = ReturnValue.GetChildAt(Variable)
        Button: Ptr[Widget_CategoryButton] = Cast[Widget_CategoryButton](ReturnValue_2)
        bSuccess: bool = Button
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        LocalCategoryButton = Button
        ReturnValue = self.GetParent()
        ReturnValue_2 = ReturnValue.GetChildAt(Variable)
        ReturnValue_3: bool = EqualEqual_ObjectObject(ReturnValue_2, self)
        LocalCategoryButton.mIsSelected = ReturnValue_3
        LocalCategoryButton.UpdateButtonStyle()
        goto(ExecutionFlow.Pop())
        # Label 495
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L28')
    

    def SetCategoryIcon(self, mIcon: Ptr[Texture2D]):
        self.mIcon = mIcon
        self.mCatIcon.SetBrushFromTexture(self.mIcon, False)
    

    def SetCategoryName(self, mName: FText):
        self.mName = mName
        self.mCategoryName.SetText(self.mName)
    

    def UpdateButtonStyle(self):
        Variable: LinearColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.057805001735687256, A = 1)
        Variable1: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 0)
        Variable1_0: bool = self.mIsSelected
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mButtonColor.SetColorAndOpacity(switch.get(Variable1_0, None))
        
        switch_0 = {
            False: Variable1,
            True: Variable
        }
        self.mTabArrow.SetColorAndOpacity(switch_0.get(Variable1_0, None))
        Variable_0: uint8 = 3
        Variable1_1: uint8 = 1
        Variable_1: bool = self.mIsSelected
        
        switch_1 = {
            False: Variable1_1,
            True: Variable_0
        }
        self.mTabArrow.SetVisibility(switch_1.get(Variable_1, None))
    

    def BndEvt__Button_26_K2Node_ComponentBoundEvent_100_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_CategoryButton(26)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_CategoryButton(180)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_CategoryButton(231)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_CategoryButton(282)
    

    def ExecuteUbergraph_Widget_CategoryButton(self):
        # Label 10
        self.bIsFocusable = True
        # End
        self.SetAsSelected()
        ReturnValue: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_0: int32 = ReturnValue.GetChildIndex(self)
        self.OnClicked.ProcessMulticastDelegate(ReturnValue_0)
        self.Widget_ButtonShine.PlayShineAnim()
        # End
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OnHover, 0, 1, 0, 1)
        # End
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OnHover, 0, 1, 1, 1)
        # End
        self.SetCategoryName(self.mName)
        self.SetCategoryIcon(self.mIcon)
        self.UpdateButtonStyle()
        goto('L10')
    

    def OnClicked__DelegateSignature(self, index: int32):
        pass
    
