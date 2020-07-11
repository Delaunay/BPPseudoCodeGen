
from codegen.ue4_stub import *

from Script.Engine import Default__KismetInputLibrary
from Script.Engine import Texture
from Script.InputCore import Key
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import ToggleOpen
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.BPW_BuildMenuButton_Base import ExecuteUbergraph_BPW_BuildMenuButton_Base
from Script.UMG import Handled
from Script.UMG import PlayAnimation
from Script.UMG import Unhandled
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import Widget
from Script.Engine import Conv_BoolToString
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import WidgetAnimation
from Script.Engine import PointerEvent_GetEffectingButton
from Script.Engine import EqualEqual_KeyKey
from Script.UMG import Close
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.BPW_BuildMenuButton_Base import ExecuteUbergraph_BPW_BuildMenuButton_Base.K2Node_Event_IsDesignTime
from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer
from Script.Engine import PrintString
from Script.UMG import EventReply
from Script.CoreUObject import LinearColor

class BPW_BuildMenuButton_Base(UserWidget):
    OnHover: Ptr[WidgetAnimation]
    OnButtonHovered: FMulticastScriptDelegate
    OnButtonUnhovered: FMulticastScriptDelegate
    OnButtonClicked: FMulticastScriptDelegate
    OnMenuOpened: FMulticastScriptDelegate
    mMenuContentWidget: Ptr[Widget]
    mName: FText
    mIcon: Ptr[Texture]
    
    def Cleanup(self):
        self.OnButtonHovered.Clear()
        # Label 10
        self.OnButtonUnhovered.Clear()
        self.OnButtonClicked.Clear()
        self.OnMenuOpened.Clear()
    

    def SetIcon(self, mIcon: Ptr[Texture]):
        self.mIcon = mIcon
        SlateBrush.ImageSize = self.mIconObject.Brush.ImageSize
        SlateBrush.Margin = self.mIconObject.Brush.Margin
        SlateBrush.TintColor = self.mIconObject.Brush.TintColor
        SlateBrush.ResourceObject = self.mIcon
        SlateBrush.DrawAs = self.mIconObject.Brush.DrawAs
        SlateBrush.Tiling = self.mIconObject.Brush.Tiling
        SlateBrush.Mirroring = self.mIconObject.Brush.Mirroring
        
        SlateBrush = None
        self.mIconObject.SetBrush(Ref[SlateBrush])
    

    def SetName(self, mName: FText):
        self.mName = mName
        self.mProductName.SetText(self.mName)
    

    def OnMouseButtonUp(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.PointerEvent_GetEffectingButton(Ref[MouseEvent])
        ReturnValue_0: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "RightMouseButton"))
        if not ReturnValue_0:
            goto('L266')
        self.mRightClickMenu.ToggleOpen(False)
        ReturnValue_1: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_2: EventReply = ReturnValue_1
        goto('L343')
        # Label 266
        ReturnValue_3: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_2 = ReturnValue_3
    

    def SetMenuContentWidget(self, mMenuContentWidget: Ptr[Widget]):
        self.mMenuContentWidget = mMenuContentWidget
    

    def OnGetMenuContent_Binding(self):
        self.OnMenuOpened.ProcessMulticastDelegate()
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mMenuContentWidget)
        ReturnValue_0: FString = Default__KismetStringLibrary.Conv_BoolToString(ReturnValue)
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_0, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        ReturnValue_1: Ptr[Widget] = self.mMenuContentWidget
    

    def PreConstruct(self):
        ExecuteUbergraph_BPW_BuildMenuButton_Base.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_BuildMenuButton_Base(29)
    

    def BndEvt__mRecipeButton_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_BuildMenuButton_Base(80)
    

    def BndEvt__mRecipeButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_BuildMenuButton_Base(182)
    

    def BndEvt__mRecipeButton_K2Node_ComponentBoundEvent_3_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_BuildMenuButton_Base(252)
    

    def Destruct(self):
        self.ExecuteUbergraph_BPW_BuildMenuButton_Base(276)
    

    def ExecuteUbergraph_BPW_BuildMenuButton_Base(self):
        # Label 10
        self.Cleanup()
        # End
        self.SetName(self.mName)
        self.SetIcon(self.mIcon)
        # End
        self.mRightClickMenu.Close()
        self.OnButtonUnhovered.ProcessMulticastDelegate()
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OnHover, 0, 1, 1, 1)
        # End
        self.OnButtonHovered.ProcessMulticastDelegate()
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OnHover, 0, 1, 0, 1)
        # End
        self.OnButtonClicked.ProcessMulticastDelegate()
        # End
        goto('L10')
    

    def OnMenuOpened__DelegateSignature(self):
        pass
    

    def OnButtonClicked__DelegateSignature(self):
        pass
    

    def OnButtonUnhovered__DelegateSignature(self):
        pass
    

    def OnButtonHovered__DelegateSignature(self):
        pass
    
