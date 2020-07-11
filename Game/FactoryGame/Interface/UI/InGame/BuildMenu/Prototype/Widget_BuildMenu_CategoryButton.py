
from codegen.ue4_stub import *

from Script.Engine import EqualEqual_ClassClass
from Script.Engine import K2_SetTimerDelegate
from Script.FactoryGame import GetCategoryName
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Script.FactoryGame import GetCategoryIcon
from Script.Engine import TimerHandle
from Script.UMG import SetColorAndOpacity
from Script.Engine import BooleanOR
from Script.FactoryGame import FGButtonWidget
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu_CategoryButton import ExecuteUbergraph_Widget_BuildMenu_CategoryButton
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import Default__FGBuildCategory
from Script.FactoryGame import FGBuildCategory
from Script.SlateCore import SlateBrush
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu import Widget_BuildMenu
from Script.CoreUObject import LinearColor

class Widget_BuildMenu_CategoryButton(FGButtonWidget):
    OnHover: Ptr[WidgetAnimation]
    mText: FText
    BuildMenu_Prototype: Ptr[Widget_BuildMenu]
    mBuildCategoryIsUnlocked: bool
    mBuildCategory: TSubclassOf[FGBuildCategory]
    mUpdateButtonTimer: TimerHandle
    OnCategoryButtonClicked: FMulticastScriptDelegate
    bIsFocusable = True
    
    def UpdateButtonStyle(self):
        
        mIsSelected = None
        self.CheckIsSelected(Ref[mIsSelected])
        Variable: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 0)
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue: bool = self.IsHovered()
        ReturnValue_0: bool = BooleanOR(mIsSelected, ReturnValue)
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable,
            True: Orange
        }
        self.mButtonColor.SetColorAndOpacity(switch.get(Variable_0, None))
        
        switch_0 = {
            False: Variable,
            True: Orange
        }
        self.mTabArrow.SetColorAndOpacity(switch_0.get(Variable_0, None))
        Variable_1: uint8 = 3
        Variable1: uint8 = 1
        Variable1_0: bool = mIsSelected
        
        switch_1 = {
            False: Variable1,
            True: Variable_1
        }
        self.mTabArrow.SetVisibility(switch_1.get(Variable1_0, None))
    

    def CheckIsSelected(self):
        ReturnValue: bool = EqualEqual_ClassClass(self.mBuildCategory, self.BuildMenu_Prototype.mSelectedBuildCategory)
        mIsSelected = ReturnValue
    

    def GetBuildCategoryIcon(self):
        ReturnValue: SlateBrush = Default__FGBuildCategory.GetCategoryIcon(self.mBuildCategory)
        
        self.mCatIcon.SetBrush(Ref[ReturnValue])
    

    def GetBuildCategoryName(self):
        ReturnValue: FText = Default__FGBuildCategory.GetCategoryName(self.mBuildCategory)
        self.mCategoryName.SetText(ReturnValue)
    

    def BndEvt__Button_26_K2Node_ComponentBoundEvent_100_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_BuildMenu_CategoryButton(70)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_BuildMenu_CategoryButton(75)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_BuildMenu_CategoryButton(126)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_BuildMenu_CategoryButton(177)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_BuildMenu_CategoryButton(297)
    

    def ExecuteUbergraph_Widget_BuildMenu_CategoryButton(self):
        # Label 10
        self.OnCategoryButtonClicked.ProcessMulticastDelegate()
        self.Widget_ButtonShine.PlayShineAnim()
        # End
        goto('L10')
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OnHover, 0, 1, 0, 1)
        # End
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OnHover, 0, 1, 1, 1)
        # End
        OutputDelegate.BindUFunction(self, UpdateButtonStyle)
        ReturnValue_0: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.10000000149011612, True)
        self.mUpdateButtonTimer = ReturnValue_0
        # End
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mUpdateButtonTimer])
    

    def OnCategoryButtonClicked__DelegateSignature(self):
        pass
    
