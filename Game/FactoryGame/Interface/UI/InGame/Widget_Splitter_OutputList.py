
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.Widget_Splitter_OutputList import ExecuteUbergraph_Widget_Splitter_OutputList
from Script.Engine import Texture
from Script.UMG import SetRenderScale
from Script.UMG import ESlateVisibility
from Script.CoreUObject import Vector2D
from Script.SlateCore import SlateColor
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.InGame.Widget_Splitter_OutputList import ExecuteUbergraph_Widget_Splitter_OutputList.K2Node_Event_IsDesignTime
from Script.SlateCore import Margin
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class Widget_Splitter_OutputList(UserWidget):
    FadeInList: Ptr[WidgetAnimation]
    mIconBrush: Ptr[Texture]
    mTitleText: FText
    OnAddClicked: FMulticastScriptDelegate
    mRenderTransform: Vector2D = Namespace(X=1, Y=1)
    ShouldShowAddButton: bool
    
    def ShowHideAddButton(self, ShouldShowAddButton: bool):
        self.ShouldShowAddButton = ShouldShowAddButton
        Variable: bool = self.ShouldShowAddButton
        Variable_0: uint8 = 0
        Variable1: uint8 = 1
        
        switch = {
            False: Variable1,
            True: Variable_0
        }
        self.mAddContainer.SetVisibility(switch.get(Variable, None))
    

    def GetDescriptorsForSearch(self):
        pass
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_Splitter_OutputList.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Splitter_OutputList(38)
    

    def BndEvt__mAdd_K2Node_ComponentBoundEvent_1_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Splitter_OutputList(457)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Splitter_OutputList(462)
    

    def ExecuteUbergraph_Widget_Splitter_OutputList(self):
        # Label 10
        self.ShowHideAddButton(self.ShouldShowAddButton)
        # End
        SlateBrush.ImageSize = Vector2D(X = 32, Y = 32)
        SlateBrush.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush.TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0)
        SlateBrush.ResourceObject = self.mIconBrush
        SlateBrush.DrawAs = 3
        SlateBrush.Tiling = 0
        SlateBrush.Mirroring = 0
        
        SlateBrush = None
        self.mIcon.SetBrush(Ref[SlateBrush])
        self.mIcon.SetRenderScale(self.mRenderTransform)
        # End
        # Label 433
        self.OnAddClicked.ProcessMulticastDelegate()
        # End
        goto('L433')
        goto('L10')
    

    def OnAddClicked__DelegateSignature(self):
        pass
    
