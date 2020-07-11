
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker_EditPreset import ExecuteUbergraph_Widget_ColorPicker_EditPreset.K2Node_Event_IsDesignTime
from Script.Engine import PlayerController
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker_EditPreset import ExecuteUbergraph_Widget_ColorPicker_EditPreset
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker_EditPreset import ExecuteUbergraph_Widget_ColorPicker_EditPreset.K2Node_CustomEvent_ConfirmClicked
from Script.FactoryGame import AddPopupWithCloseDelegate
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class Widget_ColorPicker_EditPreset(UserWidget):
    mPrimaryColor: LinearColor
    mSecondaryColor: LinearColor
    OnAccept: FMulticastScriptDelegate
    
    def PreConstruct(self):
        ExecuteUbergraph_Widget_ColorPicker_EditPreset.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorPicker_EditPreset(10)
    

    def BndEvt__mEditPresetAccept_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorPicker_EditPreset(203)
    

    def BndEvt__mEditPresetCanel_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorPicker_EditPreset(616)
    

    def OnPopupConfirm(self, ConfirmClicked: bool):
        ExecuteUbergraph_Widget_ColorPicker_EditPreset.K2Node_CustomEvent_ConfirmClicked = ConfirmClicked #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorPicker_EditPreset(635)
    

    def BndEvt__mPrimaryColorPicker_K2Node_ComponentBoundEvent_2_OnValueChanged__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorPicker_EditPreset(673)
    

    def BndEvt__mSecondaryColorPicker_K2Node_ComponentBoundEvent_3_OnValueChanged__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorPicker_EditPreset(776)
    

    def ExecuteUbergraph_Widget_ColorPicker_EditPreset(self):
        self.mPrimaryColorPicker.SetupColorAndSliders(self.mPrimaryColor)
        self.mSecondaryColorPicker.SetupColorAndSliders(self.mSecondaryColor)
        self.Widget_ColorPicker_Preview.SetColors(self.mPrimaryColorPicker.CurrentColor, self.mSecondaryColorPicker.CurrentColor)
        # End
        OutputDelegate.BindUFunction(self, OnPopupConfirm)
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        OutputDelegate = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 292, 'Value': 'Set Preset'}", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 342, 'Value': 'Are you sure you want to update this preset? This will also update the colors on all building using this preset.'}", 1, None, None, Ref[OutputDelegate])
        # End
        # Label 511
        self.RemoveFromParent()
        # End
        # Label 530
        self.OnAccept.ProcessMulticastDelegate(self.mPrimaryColorPicker.CurrentColor, self.mSecondaryColorPicker.CurrentColor)
        goto('L511')
        self.RemoveFromParent()
        # End
        if not ConfirmClicked:
            goto('L654')
        goto('L530')
        # Label 654
        self.RemoveFromParent()
        # End
        # Label 673
        self.Widget_ColorPicker_Preview.SetColors(self.mPrimaryColorPicker.CurrentColor, self.mSecondaryColorPicker.CurrentColor)
        # End
        goto('L673')
    

    def OnAccept__DelegateSignature(self, PrimaryColor: LinearColor, SecondaryColor: LinearColor):
        pass
    
