
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildableResourceExtractor
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Manufacturing_Warning import ExecuteUbergraph_Widget_Manufacturing_Warning
from Script.UMG import OverlaySlot
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import SlotAsOverlaySlot
from Script.FactoryGame import FGBuildableManufacturer
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import SetHorizontalAlignment
from Script.UMG import PlayAnimation
from Script.Engine import IsValid
from Script.Engine import NotEqual_TextText
from Script.UMG import SetHeightOverride
from Script.FactoryGame import IsProductionPaused
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.UMG import ClearHeightOverride
from Script.UMG import ClearWidthOverride
from Script.UMG import WidgetAnimation
from Script.UMG import SetWidthOverride
from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer
from Script.UMG import SetVerticalAlignment
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Manufacturing_Warning import ExecuteUbergraph_Widget_Manufacturing_Warning.K2Node_Event_IsDesignTime

class Widget_Manufacturing_Warning(UserWidget):
    IdleAnim: Ptr[WidgetAnimation]
    mManufacturer: Ptr[FGBuildableManufacturer]
    mResourceExtractor: Ptr[FGBuildableResourceExtractor]
    mText: FText
    mOverrideSize: bool
    Visibility = ESlateVisibility::HitTestInvisible
    
    def HideWarning(self):
        self.SetVisibility(1)
    

    def UpdateWarning(self, text: FText):
        self.SetText(text)
        self.SetVisibility(3)
    

    def SetText(self, InText: FText):
        self.mText = InText
        self.WarningText.SetText(self.mText)
    

    def GetWarningText(self):
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mManufacturer)
        if not ReturnValue1:
            goto('L189')
        ReturnValue: bool = self.mManufacturer.HasPower()
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        if not ReturnValue_0:
            goto('L409')
        # Label 154
        ReturnValue_1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 174, 'Value': 'NO POWER'}"
        goto('L560')
        # Label 189
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(self.mResourceExtractor)
        if not ReturnValue_2:
            goto('L348')
        ReturnValue1_0: bool = self.mResourceExtractor.HasPower()
        ReturnValue1_1: bool = Not_PreBool(ReturnValue1_0)
        if not ReturnValue1_1:
            goto('L499')
        goto('L154')
        # Label 348
        ReturnValue_1 = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 368, 'Value': 'No valid manufacturer or extractor'}"
        goto('L560')
        # Label 409
        ReturnValue_3: bool = self.mManufacturer.IsProductionPaused()
        if not ReturnValue_3:
            goto('L560')
        # Label 465
        ReturnValue_1 = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 485, 'Value': 'STANDBY'}"
        goto('L560')
        # Label 499
        ReturnValue1_2: bool = self.mResourceExtractor.IsProductionPaused()
        if not ReturnValue1_2:
            goto('L560')
        goto('L465')
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Manufacturing_Warning(712)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_Manufacturing_Warning.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Manufacturing_Warning(10)
    

    def ExecuteUbergraph_Widget_Manufacturing_Warning(self):
        if not self.mOverrideSize:
            goto('L263')
        self.mSizeBox.ClearWidthOverride()
        self.mSizeBox.ClearHeightOverride()
        ReturnValue1: Ptr[OverlaySlot] = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.mSizeBox)
        ReturnValue1.SetHorizontalAlignment(0)
        ReturnValue1 = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.mSizeBox)
        ReturnValue1.SetVerticalAlignment(0)
        # End
        # Label 263
        self.mSizeBox.SetHeightOverride(80)
        self.mSizeBox.SetWidthOverride(128)
        ReturnValue: Ptr[OverlaySlot] = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.mSizeBox)
        ReturnValue.SetHorizontalAlignment(2)
        ReturnValue = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.mSizeBox)
        ReturnValue.SetVerticalAlignment(2)
        # End
        # Label 512
        ReturnValue_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.IdleAnim, 0, 0, 0, 1)
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText("")
        
        ReturnValue_2: bool = Default__KismetTextLibrary.NotEqual_TextText(Ref[self.mText], Ref[ReturnValue_1])
        if not ReturnValue_2:
            goto('L717')
        self.SetText(self.mText)
        # End
        goto('L512')
    
