
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.InGame.Widget_SplitterRuleButton import ExecuteUbergraph_Widget_SplitterRuleButton
from Script.SlateCore import Margin
from Script.Engine import Texture2D
from Script.UMG import Construct
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import GetItemName
from Script.FactoryGame import FGItemDescriptor
from Script.CoreUObject import Vector2D
from Script.FactoryGame import FGButtonWidget
from Script.SlateCore import SlateColor
from Script.Engine import IsValidClass
from Game.FactoryGame.Interface.UI.InGame.Widget_SplitterProgrammableRule import Widget_SplitterProgrammableRule
from Script.CoreUObject import LinearColor
from Script.FactoryGame import GetSmallIcon

class Widget_SplitterRuleButton(FGButtonWidget):
    mItemDescriptor: TSubclassOf[FGItemDescriptor]
    mWidgetSplitterRule: Ptr[Widget_SplitterProgrammableRule]
    
    def SetUpButton(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mItemDescriptor)
        if not ReturnValue:
            goto('L613')
        ReturnValue_0: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(self.mItemDescriptor)
        SlateBrush.ImageSize = Vector2D(X = 32, Y = 32)
        SlateBrush.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush.TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0)
        SlateBrush.ResourceObject = ReturnValue_0
        SlateBrush.DrawAs = 3
        SlateBrush.Tiling = 0
        SlateBrush.Mirroring = 0
        
        SlateBrush = None
        self.mRuleButton.Icon.SetBrush(Ref[SlateBrush])
        ReturnValue_1: FText = Default__FGItemDescriptor.GetItemName(self.mItemDescriptor)
        self.mRuleButton.ButtonText.SetText(ReturnValue_1)
    

    def GetButtonText(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mItemDescriptor)
        if not ReturnValue:
            goto('L156')
        ReturnValue_0: FText = Default__FGItemDescriptor.GetItemName(self.mItemDescriptor)
        ReturnValue_1: FText = ReturnValue_0
        goto('L218')
        # Label 156
        ReturnValue_1 = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 176, 'Value': 'NONE'}"
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SplitterRuleButton(39)
    

    def BndEvt__Widget_StandardButton_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SplitterRuleButton(94)
    

    def ExecuteUbergraph_Widget_SplitterRuleButton(self):
        # Label 10
        self.Construct()
        self.SetUpButton()
        # End
        goto('L10')
        # Label 44
        self.mWidgetSplitterRule.SetSelectedItemDescriptor(self.mItemDescriptor)
        # End
        goto('L44')
    
