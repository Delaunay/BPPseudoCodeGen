
from codegen.ue4_stub import *

from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Script.UMG import ClearHeightOverride
from Game.FactoryGame.Interface.UI.HUDHelpers.Widget_HUDBox import ExecuteUbergraph_Widget_HUDBox.K2Node_Event_IsDesignTime
from Script.CoreUObject import Object
from Script.UMG import BindToAnimationFinished
from Script.UMG import StopAnimation
from Script.UMG import SetRenderOpacity
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.HUDHelpers.Widget_HUDBox import ExecuteUbergraph_Widget_HUDBox
from Script.UMG import UserWidget

class Widget_HUDBox(UserWidget):
    WarningAnim: Ptr[WidgetAnimation]
    RemoveAnim: Ptr[WidgetAnimation]
    SpawnAnim: Ptr[WidgetAnimation]
    mTitle: FText = NSLOCTEXT("", "F4E03FF04422FE646EBAA08C3AA474C6", "Title")
    mIcon: Ptr[Object]
    mChildWidget: Ptr[UserWidget]
    mShowIcon: bool = True
    mForceHeight: bool = True
    
    def SetIconVisibility(self):
        if not self.mShowIcon:
            goto('L510')
        SlateBrush.ImageSize = self.mIconObject.Brush.ImageSize
        SlateBrush.Margin = self.mIconObject.Brush.Margin
        SlateBrush.TintColor = self.mIconObject.Brush.TintColor
        SlateBrush.ResourceObject = self.mIcon
        SlateBrush.DrawAs = self.mIconObject.Brush.DrawAs
        SlateBrush.Tiling = self.mIconObject.Brush.Tiling
        SlateBrush.Mirroring = self.mIconObject.Brush.Mirroring
        
        SlateBrush = None
        self.mIconObject.SetBrush(Ref[SlateBrush])
        self.SetVisibility(0)
        # End
        # Label 510
        self.mIconObject.SetVisibility(1)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_HUDBox(10)
    

    def RemoveHUDBox(self):
        self.ExecuteUbergraph_Widget_HUDBox(144)
    

    def DestroySelf(self):
        self.ExecuteUbergraph_Widget_HUDBox(246)
    

    def StartWarningSign(self):
        self.ExecuteUbergraph_Widget_HUDBox(265)
    

    def StopWarningSign(self):
        self.ExecuteUbergraph_Widget_HUDBox(354)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_HUDBox.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_HUDBox(453)
    

    def ExecuteUbergraph_Widget_HUDBox(self):
        if not self.mForceHeight:
            goto('L75')
        # Label 24
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnim, 0, 1, 0, 1)
        # End
        # Label 75
        self.mBoxSizeBox.ClearHeightOverride()
        self.mContentSizeBox.ClearHeightOverride()
        goto('L24')
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.RemoveAnim, 0, 1, 0, 1)
        OutputDelegate.BindUFunction(self, DestroySelf)
        self.BindToAnimationFinished(self.RemoveAnim, OutputDelegate)
        # End
        self.RemoveFromParent()
        # End
        self.WarningSign.SetVisibility(0)
        ReturnValue2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.WarningAnim, 0, 0, 0, 1)
        # End
        self.StopAnimation(self.WarningAnim)
        self.WarningSign.SetRenderOpacity(0)
        self.WarningSign.SetVisibility(1)
        # End
        self.SetIconVisibility()
        self.mTitleObject.SetText(self.mTitle)
    
