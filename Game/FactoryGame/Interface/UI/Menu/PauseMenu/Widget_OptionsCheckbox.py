
from codegen.ue4_stub import *

from Script.FactoryGame import Default__FGGameUserSettings
from Script.Engine import PlayerController
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.Widget_OptionsCheckbox import ExecuteUbergraph_Widget_OptionsCheckbox
from Script.FactoryGame import SetBoolOptionValue
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_Click import Play_UI_MainMenu_Click
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.Widget_OptionsCheckbox import ExecuteUbergraph_Widget_OptionsCheckbox.K2Node_Event_IsDesignTime
from Script.UMG import SetColorAndOpacity
from Script.UMG import SetContentColorAndOpacity
from Game.FactoryGame.Interface.UI.Menu.Widget_OptionValueController import Widget_OptionValueController
from Script.FactoryGame import GetFGGameUserSettings
from Script.SlateCore import SlateBrush
from Script.FactoryGame import GetBoolOptionValue
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import FGGameUserSettings
from Script.Engine import Not_PreBool

class Widget_OptionsCheckbox(Widget_OptionValueController):
    mUnchecked: SlateBrush = Namespace(DrawAs=2, ImageSize={'X': 2, 'Y': 2}, ImageType=0, Margin={'Left': 0.5, 'Top': 0.5, 'Right': 0.5, 'Bottom': 0.5}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Interface/UI/Assets/Shared/white_2x2.white_2x2'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mUncheckedPressed: SlateBrush = Namespace(DrawAs=3, ImageSize={'X': 2, 'Y': 2}, ImageType=0, Margin={'Left': 0.5, 'Top': 0.5, 'Right': 0.5, 'Bottom': 0.5}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Interface/UI/Assets/Shared/white_2x2.white_2x2'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mUncheckedHover: SlateBrush = Namespace(DrawAs=2, ImageSize={'X': 2, 'Y': 2}, ImageType=0, Margin={'Left': 0.5, 'Top': 0.5, 'Right': 0.5, 'Bottom': 0.5}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Interface/UI/Assets/Shared/white_2x2.white_2x2'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mChecked: SlateBrush
    mCheckedHover: SlateBrush
    mCheckedPressed: SlateBrush = Namespace(DrawAs=2, ImageSize={'X': 2, 'Y': 2}, ImageType=0, Margin={'Left': 0.5, 'Top': 0.5, 'Right': 0.5, 'Bottom': 0.5}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Interface/UI/Assets/Shared/white_2x2.white_2x2'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mIsChecked: bool
    OnCheckChanged: FMulticastScriptDelegate
    mForceShouldCheckOnConstruct: bool = True
    
    def HandleChecked(self, IsChecked: bool):
        if not self.mIsDynamicOption:
            goto('L151')
        ReturnValue: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        ReturnValue.SetBoolOptionValue(self.mOptionRowData.ConsoleVariable, IsChecked, self.mOptionRowData.UpdateInstantly, self.mOptionRowData.RequireRestart)
    

    def UpdateCheckboxValue(self):
        ReturnValue: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        ReturnValue_0: bool = ReturnValue.GetBoolOptionValue(self.mOptionRowData.ConsoleVariable)
        
        IsChecked = None
        self.SetChecked(ReturnValue_0, False, Ref[IsChecked])
    

    def SetChecked(self, mIsChecked: bool, TriggerCheckedEvent: bool):
        self.mIsChecked = mIsChecked
        if not self.mIsChecked:
            goto('L205')
        
        self.mBG.SetBrush(Ref[self.mChecked])
        self.mCheck.SetVisibility(3)
        # Label 116
        if not TriggerCheckedEvent:
            goto('L181')
        self.OnCheckChanged.ProcessMulticastDelegate(self.mIsChecked)
        self.HandleChecked(self.mIsChecked)
        # Label 181
        IsChecked = self.mIsChecked
        # End
        
        # Label 205
        self.mBG.SetBrush(Ref[self.mUnchecked])
        self.mCheck.SetVisibility(2)
        goto('L116')
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_8_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_OptionsCheckbox(224)
    

    def OnRowHovered(self):
        self.ExecuteUbergraph_Widget_OptionsCheckbox(491)
    

    def OnRowUnhovered(self):
        self.ExecuteUbergraph_Widget_OptionsCheckbox(578)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_OptionsCheckbox.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_OptionsCheckbox(715)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_5_OnButtonPressedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_OptionsCheckbox(753)
    

    def OnInitValueController(self):
        self.ExecuteUbergraph_Widget_OptionsCheckbox(817)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_7_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_OptionsCheckbox(836)
    

    def OnOptionValueUpdated(self):
        self.ExecuteUbergraph_Widget_OptionsCheckbox(841)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_6_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_OptionsCheckbox(860)
    

    def ExecuteUbergraph_Widget_OptionsCheckbox(self):
        
        # Label 10
        self.mBG.SetBrush(Ref[self.mCheckedHover])
        # End
        
        # Label 60
        self.mBG.SetBrush(Ref[self.mUncheckedHover])
        # End
        # Label 110
        if not self.mIsChecked:
            goto('L174')
        
        self.mBG.SetBrush(Ref[self.mChecked])
        # End
        
        # Label 174
        self.mBG.SetBrush(Ref[self.mUnchecked])
        # End
        ReturnValue: bool = Not_PreBool(self.mIsChecked)
        
        IsChecked = None
        self.SetChecked(ReturnValue, True, Ref[IsChecked])
        if not IsChecked:
            goto('L390')
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Click, ReturnValue_0, True)
        # End
        # Label 390
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(None, ReturnValue1, True)
        # End
        # Label 472
        if not self.mIsChecked:
            goto('L60')
        goto('L10')
        self.mTintBorder.SetContentColorAndOpacity(self.mHoveredColor)
        self.mCheck.SetColorAndOpacity(self.mDarkColor)
        # End
        self.mTintBorder.SetContentColorAndOpacity(self.mUnhoveredColor)
        self.mCheck.SetColorAndOpacity(self.mDarkColor)
        # End
        
        # Label 665
        self.mBG.SetBrush(Ref[self.mUncheckedPressed])
        # End
        
        IsChecked1 = None
        self.SetChecked(self.mIsChecked, False, Ref[IsChecked1])
        # End
        if not self.mIsChecked:
            goto('L665')
        
        self.mBG.SetBrush(Ref[self.mCheckedPressed])
        # End
        self.UpdateCheckboxValue()
        # End
        goto('L110')
        self.UpdateCheckboxValue()
        # End
        goto('L472')
    

    def OnCheckChanged__DelegateSignature(self, IsChecked: bool):
        pass
    
