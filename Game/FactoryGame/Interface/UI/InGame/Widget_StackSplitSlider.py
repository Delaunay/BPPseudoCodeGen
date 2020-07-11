
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.Widget_StackSplitSlider import ExecuteUbergraph_Widget_StackSplitSlider.K2Node_ComponentBoundEvent_Text1
from Script.Engine import Conv_TextToString
from Script.Engine import FFloor
from Script.Engine import Conv_IntToFloat
from Script.Engine import PlayerController
from Script.UMG import Handled
from Script.UMG import SetText
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import Widget_InventorySlot
from Game.FactoryGame.Interface.UI.InGame.Widget_StackSplitSlider import ExecuteUbergraph_Widget_StackSplitSlider.K2Node_ComponentBoundEvent_CommitMethod
from Script.UMG import SetValue
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Replace
from Script.Engine import Conv_IntToText
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Interface.UI.InGame.EDirection import EDirection
from Script.FactoryGame import FGInteractWidget
from Script.SlateCore import FocusEvent
from Script.Engine import Conv_StringToInt
from Script.Engine import IsNumeric
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import WidgetAnimation
from Script.Engine import NotEqual_ByteByte
from Script.UMG import GetValue
from Script.UMG import Close
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Game.FactoryGame.Interface.UI.InGame.Widget_StackSplitSlider import ExecuteUbergraph_Widget_StackSplitSlider.K2Node_ComponentBoundEvent_Value
from Game.FactoryGame.Interface.UI.InGame.Widget_StackSplitSlider import ExecuteUbergraph_Widget_StackSplitSlider
from Game.FactoryGame.Interface.UI.InGame.Widget_StackSplitSlider import ExecuteUbergraph_Widget_StackSplitSlider.K2Node_ComponentBoundEvent_CommitMethod1
from Script.Engine import MapRangeClamped
from Script.Engine import Round
from Script.Engine import Clamp
from Game.FactoryGame.Interface.UI.InGame.Widget_StackSplitSlider import ExecuteUbergraph_Widget_StackSplitSlider.K2Node_ComponentBoundEvent_Text
from Script.UMG import EventReply

class Widget_StackSplitSlider(FGInteractWidget):
    Intro: Ptr[WidgetAnimation]
    mSourceSlot: Ptr[Widget_InventorySlot]
    NewVar_0: FocusEvent
    mRestoreFocusWhenLost = True
    mCallCustomTickOnConstruct = True
    
    def ClampToValidRange(self, Value: int32):
        
        Num = None
        self.mSourceSlot.GetNumItems(Ref[Num])
        ReturnValue: int32 = Num - 1
        ReturnValue_0: int32 = Clamp(Value, 1, ReturnValue)
        ReturnValue_1: int32 = ReturnValue_0
    

    def OnKeyUp(self):
        ReturnValue: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_0: EventReply = ReturnValue
    

    def SetSliderAfterText(self, text: FText, CommitMethod: uint8, LeftOrRight: uint8):
        CmpSuccess: bool = NotEqual_ByteByte(CommitMethod, 0)
        if not CmpSuccess:
            goto('L185')
        CmpSuccess = NotEqual_ByteByte(CommitMethod, 1)
        if not CmpSuccess:
            goto('L185')
        CmpSuccess = NotEqual_ByteByte(CommitMethod, 2)
        if not CmpSuccess:
            goto('L185')
        CmpSuccess = NotEqual_ByteByte(CommitMethod, 3)
        if not CmpSuccess:
            goto('L1118')
        # End
        
        # Label 185
        ReturnValue: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[text])
        ReturnValue_0: FString = Default__KismetStringLibrary.Replace(ReturnValue, ",", ".", 1)
        ReturnValue_1: bool = Default__KismetStringLibrary.IsNumeric(ReturnValue_0)
        if not ReturnValue_1:
            goto('L1099')
        
        ReturnValue = Default__KismetTextLibrary.Conv_TextToString(Ref[text])
        ReturnValue_0 = Default__KismetStringLibrary.Replace(ReturnValue, ",", ".", 1)
        ReturnValue_2: int32 = Default__KismetStringLibrary.Conv_StringToInt(ReturnValue_0)
        mLocalNumItems = ReturnValue_2
        Variable: float = 0
        Variable1: float = 0
        Variable2: float = 0
        
        Num = None
        self.mSourceSlot.GetNumItems(Ref[Num])
        ReturnValue_3: int32 = Num - 1
        ReturnValue_4: float = Conv_IntToFloat(ReturnValue_3)
        ReturnValue1: float = Conv_IntToFloat(mLocalNumItems)
        ReturnValue_5: float = MapRangeClamped(ReturnValue1, 1, ReturnValue_4, 0, 1)
        Variable_0: uint8 = LeftOrRight
        ReturnValue_6: float = 1 - ReturnValue_5
        
        switch = {
            0: Variable2,
            1: Variable1,
            2: Variable,
            3: ReturnValue_5,
            4: ReturnValue_6
        }
        self.mSlider.SetValue(switch.get(Variable_0, None))
        self.UpdateText()
        # End
        # Label 1099
        self.UpdateText()
        # End
        # Label 1118
        self.UpdateText()
    

    def UpdateText(self):
        
        NumLeft1 = None
        self.GetNumLeftAtSlot(Ref[NumLeft1])
        ReturnValue: FText = Default__KismetTextLibrary.Conv_IntToText(NumLeft1, False, True, 1, 324)
        self.mLeftText.SetText(ReturnValue)
        
        NumLeft = None
        self.GetNumLeftAtSlot(Ref[NumLeft])
        
        Num = None
        self.mSourceSlot.GetNumItems(Ref[Num])
        ReturnValue_0: int32 = Num - NumLeft
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_0, False, True, 1, 324)
        self.mRightText.SetText(ReturnValue1)
    

    def SnapSliderValue(self, NormalizedValue: float):
        Variable: float = 0.5
        
        Num = None
        self.mSourceSlot.GetNumItems(Ref[Num])
        ReturnValue: int32 = Num - 2
        ReturnValue_0: bool = EqualEqual_IntInt(Num, 2)
        ReturnValue_1: float = Conv_IntToFloat(ReturnValue)
        Variable_0: bool = ReturnValue_0
        ReturnValue1: float = Conv_IntToFloat(ReturnValue)
        ReturnValue_2: float = NormalizedValue * ReturnValue1
        ReturnValue_3: int32 = FFloor(ReturnValue_2)
        ReturnValue2: float = Conv_IntToFloat(ReturnValue_3)
        ReturnValue_4: float = ReturnValue2 / ReturnValue_1
        
        switch = {
            False: ReturnValue_4,
            True: Variable
        }
        SnappedValue = switch.get(Variable_0, None)
    

    def OnPaint(self):
        maxNumLines = 11
    

    def UpdateSliderValue(self, MyGeometry: Geometry):
        pass
    

    def GetProgressBarPercentage(self):
        ReturnValue: float = self.mSlider.GetValue()
        ReturnValue_0: float = ReturnValue
    

    def GetNumInNewStackText(self):
        
        NumLeft = None
        self.GetNumLeftAtSlot(Ref[NumLeft])
        
        Num = None
        self.mSourceSlot.GetNumItems(Ref[Num])
        ReturnValue: int32 = Num - NumLeft
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue, False, True, 1, 324)
        # Label 185
        ReturnValue_1: FText = ReturnValue_0
    

    def GetNumLeftAtSlot(self):
        
        Num = None
        self.mSourceSlot.GetNumItems(Ref[Num])
        ReturnValue: float = self.mSlider.GetValue()
        ReturnValue_0: int32 = Num - 1
        ReturnValue_1: float = Conv_IntToFloat(ReturnValue_0)
        ReturnValue_2: float = MapRangeClamped(ReturnValue, 0, 1, 1, ReturnValue_1)
        ReturnValue_3: int32 = Round(ReturnValue_2)
        NumLeft = ReturnValue_3
    

    def GetNumLeftAtSlotText(self):
        
        NumLeft = None
        self.GetNumLeftAtSlot(Ref[NumLeft])
        ReturnValue: FText = Default__KismetTextLibrary.Conv_IntToText(NumLeft, False, True, 1, 324)
        ReturnValue_0: FText = ReturnValue
    

    def SplitResource(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        RCO = None
        Default__BPHUDHelpers.GetDefaultRCO(ReturnValue, self, Ref[RCO])
        
        NumLeft = None
        self.GetNumLeftAtSlot(Ref[NumLeft])
        
        Num = None
        self.mSourceSlot.GetNumItems(Ref[Num])
        ReturnValue_0: int32 = Num - NumLeft
        RCO.Server_SplitResource(self.mSourceSlot.mCachedInventoryComponent, self.mSourceSlot.mSlotIdx, ReturnValue_0)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_StackSplitSlider(51)
    

    def BndEvt__mSlider_K2Node_ComponentBoundEvent_0_OnFloatValueChangedEvent__DelegateSignature(self, Value: float):
        ExecuteUbergraph_Widget_StackSplitSlider.K2Node_ComponentBoundEvent_Value = Value #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_StackSplitSlider(139)
    

    def BndEvt__mToSlot_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_StackSplitSlider(231)
    

    def BndEvt__mCancel_K2Node_ComponentBoundEvent_2_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_StackSplitSlider(304)
    

    def BndEvt__mLeftText_K2Node_ComponentBoundEvent_3_OnEditableTextCommittedEvent__DelegateSignature(self, text: Const[Ref[FText]], CommitMethod: uint8):
        ExecuteUbergraph_Widget_StackSplitSlider.K2Node_ComponentBoundEvent_Text1 = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_StackSplitSlider.K2Node_ComponentBoundEvent_CommitMethod1 = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_StackSplitSlider(309)
    

    def BndEvt__mRightText_K2Node_ComponentBoundEvent_4_OnEditableTextCommittedEvent__DelegateSignature(self, text: Const[Ref[FText]], CommitMethod: uint8):
        ExecuteUbergraph_Widget_StackSplitSlider.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_StackSplitSlider.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_StackSplitSlider(348)
    

    def CloseStackSplitSlider(self):
        self.ExecuteUbergraph_Widget_StackSplitSlider(10)
    

    def ExecuteUbergraph_Widget_StackSplitSlider(self):
        # Label 10
        self.mSourceSlot.CloseSplitStack()
        # End
        
        SnappedValue1 = None
        self.SnapSliderValue(0.5, Ref[SnappedValue1])
        self.mSlider.SetValue(SnappedValue1)
        self.UpdateText()
        # End
        
        SnappedValue = None
        self.SnapSliderValue(Value, Ref[SnappedValue])
        self.mSlider.SetValue(SnappedValue)
        self.UpdateText()
        # End
        self.SplitResource()
        self.mSourceSlot.mSplitMenuAnchor.Close()
        # End
        goto('L10')
        self.SetSliderAfterText(Text1, CommitMethod1, 3)
        # End
        self.SetSliderAfterText(Text, CommitMethod, 4)
    
