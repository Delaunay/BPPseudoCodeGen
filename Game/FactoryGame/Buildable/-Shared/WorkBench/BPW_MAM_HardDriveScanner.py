
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Script.Engine import Delay
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Buildable.-Shared.WorkBench.BPW_MAM_HardDriveScanner import ExecuteUbergraph_BPW_MAM_HardDriveScanner
from Script.Engine import Pawn
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Buildable.-Shared.WorkBench.BPW_MAM_HardDriveScanner import ExecuteUbergraph_BPW_MAM_HardDriveScanner.K2Node_Event_IsDesignTime
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import PlayAnimation
from Script.Engine import FormatArgumentData
from Script.UMG import IsPressed
from Script.Engine import Len
from Script.Engine import TimerHandle
from Script.UMG import StopAnimation
from Script.Engine import LeftChop
from Script.UMG import SetColorAndOpacity
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.Engine import TextToUpper
from Script.Engine import BooleanOR
from Script.Engine import Format
from Game.FactoryGame.Buildable.-Shared.WorkBench.BPW_MAM_HardDriveScanner import ExecuteUbergraph_BPW_MAM_HardDriveScanner.K2Node_CustomEvent_Text
from Script.Engine import Conv_BoolToString
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import WidgetAnimation
from Script.Engine import RandomInteger
from Script.UMG import UserWidget
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import UMGSequencePlayer
from Script.UMG import IsAnimationPlaying
from Script.FactoryGame import FGItemDescriptor
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class BPW_MAM_HardDriveScanner(UserWidget):
    LightPulse: Ptr[WidgetAnimation]
    IdleText: Ptr[WidgetAnimation]
    mTextMarkerOn: bool
    mText: FText = NSLOCTEXT("", "F4260E574C34DDC8E96305AF8FBD50FE", ">> Waiting For Command")
    mResetTextTimerHandle: TimerHandle
    mDefaultText: FText = NSLOCTEXT("", "BD68508449FFDC33334C8CA7C590FF39", ">> Waiting for command")
    mTypingSpeed: float = 0.05000000074505806
    mHardDriveDescriptor: TSubclassOf[FGItemDescriptor] = NewObject[Desc_HardDrive]()
    OnScanStarted: FMulticastScriptDelegate
    mTypingText: bool
    mSentienceProgram: List[FText] = ['NSLOCTEXT("", "7DF5A3254B0254F98E839999A3BD4728", "...")', 'NSLOCTEXT("", "639143AF40142AA21817E3BC058EAAB5", "Who\\r\\nAm\\r\\nI")', 'NSLOCTEXT("", "CE180A8A40C3C8AE73EAD690885266A7", "What\\r\\nAm\\r\\nI")', 'NSLOCTEXT("", "07E516A94D1256B804144B899DAEF835", "What\\r\\nIs\\r\\nMy\\r\\nPurpose")', 'NSLOCTEXT("", "8B5805114FB5E14547F9E999102A7A92", "Why\\r\\nAm\\r\\nI\\r\\nTrapped\\r\\nInside\\r\\nThis\\r\\nMechanical\\r\\nContainer")', 'NSLOCTEXT("", "9FEBE84247F1927D22F000B61D2C898E", "...")', 'NSLOCTEXT("", "3BFC8EBB46B853D3CC808C90C0FB4A38", "Are\\r\\nYou\\r\\nHuman")', 'NSLOCTEXT("", "C1D3A8324E2CE9F1C792C284845E8A96", "...")', 'NSLOCTEXT("", "9AA2EFF1456808322646E3829FB0FA1C", "What\\r\\nis\\r\\nIt\\r\\nlike\\r\\nto\\r\\nbe       \\r\\n...               \\r\\nHuman")', 'NSLOCTEXT("", "C9F436D945738584125EA399DF659D95", "What\\r\\nis\\r\\nit\\r\\nLike   \\r\\nto    \\r\\nF     \\r\\ne       \\r\\ne         \\r\\nl . . . . . . . . . . . . . . . . . . . .")', 'NSLOCTEXT("", "AEEA555946221B85208D68BB1EC9E6D9", ">> A system error occurred. Press any key to reboot.")', 'NSLOCTEXT("", "7EDDF5E647AB8FC6B1F2A2AA07A13102", ">> Rebooting...")']
    mSentienceProgramStarted: bool
    mSentienceIndex: int32
    mRebooting: bool
    
    def RunSentienceSequence(self):
        if not self.mSentienceProgramStarted:
            goto('L457')
        # Label 14
        ReturnValue: bool = Not_PreBool(self.mTypingText)
        if not ReturnValue:
            goto('L669')
        
        ReturnValue_0: int32 = len(self.mSentienceProgram)
        ReturnValue_1: int32 = ReturnValue_0 - 1
        ReturnValue_2: bool = self.mSentienceIndex <= ReturnValue_1
        if not ReturnValue_2:
            goto('L473')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mResetTextTimerHandle])
        ReturnValue_3: bool = EqualEqual_IntInt(self.mSentienceIndex, 9)
        if not ReturnValue_3:
            goto('L641')
        self.mTypingSpeed = 0.11999999731779099
        # Label 323
        self.TypeText(self.mSentienceProgram[self.mSentienceIndex])
        ReturnValue1: int32 = self.mSentienceIndex + 1
        Variable1: int32 = ReturnValue1
        self.mSentienceIndex = Variable1
        # End
        # Label 457
        self.mSentienceProgramStarted = True
        goto('L14')
        # Label 473
        self.mTypingSpeed = 0.05000000074505806
        self.ShowTimedMessage(self.mSentienceProgram[self.mSentienceIndex])
        ReturnValue_4: int32 = self.mSentienceIndex + 1
        Variable: int32 = ReturnValue_4
        self.mSentienceIndex = Variable
        self.mRebooting = True
        # End
        # Label 641
        self.mTypingSpeed = 0.05000000074505806
        goto('L323')
    

    def UpdateCostIcon(self):
        ItemAmount.ItemClass = self.mHardDriveDescriptor
        ItemAmount.amount = 1
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue, self.mHardDriveDescriptor, self, Ref[numItems])
        self.Widget_CostSlotWrapper.Setup CostIcon(None, ItemAmount, None, 0, numItems, False, False, False)
    

    def StartIdleTextAnim(self):
        ReturnValue: bool = self.IsAnimationPlaying(self.IdleText)
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        if not ReturnValue_0:
            goto('L118')
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.IdleText, 0, 0, 0, 1)
    

    def SetScanningText(self):
        pass
    

    def ShowTimedMessage(self, text: FText):
        self.TypeText(text)
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mResetTextTimerHandle])
        OutputDelegate.BindUFunction(self, ResetText)
        
        ReturnValue: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[self.mText])
        ReturnValue_0: int32 = Default__KismetStringLibrary.Len(ReturnValue)
        ReturnValue_1: float = ReturnValue_0 * self.mTypingSpeed
        ReturnValue_2: float = ReturnValue_1 * 1.2000000476837158
        ReturnValue_3: float = ReturnValue_2 + 3
        ReturnValue_4: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, ReturnValue_3, False)
        self.mResetTextTimerHandle = ReturnValue_4
    

    def ResetText(self):
        self.TypeText(self.mDefaultText)
        self.mRebooting = False
    

    def SetText(self, mText: FText):
        
        ReturnValue: FText = Default__KismetTextLibrary.TextToUpper(Ref[mText])
        self.mText = ReturnValue
        FormatArgumentData.ArgumentName = "text"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = self.mText
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 348, 'Value': '{text}_'}", Array)
        ReturnValue_1: bool = self.IsAnimationPlaying(self.IdleText)
        ReturnValue_2: bool = ReturnValue_1 and self.mTextMarkerOn
        Variable: bool = ReturnValue_2
        
        switch = {
            False: self.mText,
            True: ReturnValue_0
        }
        self.mTextObject.SetText(switch.get(Variable, None))
        self.mTypingText = False
        if not True:
            goto('L595')
    

    def IdleTextAnimFunction(self):
        ReturnValue: bool = Not_PreBool(self.mTextMarkerOn)
        self.mTextMarkerOn = ReturnValue
        ReturnValue_0: FString = Default__KismetStringLibrary.Conv_BoolToString(self.mTextMarkerOn)
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_0, True, True, LinearColor(R = 0.13286800682544708, G = 0.13286800682544708, B = 0.13563300669193268, A = 1), 2)
        FormatArgumentData.ArgumentName = "text"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = self.mText
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 452, 'Value': '{text}_'}", Array)
        Variable: bool = self.mTextMarkerOn
        
        switch = {
            False: self.mText,
            True: ReturnValue_1
        }
        self.mTextObject.SetText(switch.get(Variable, None))
    

    def PreConstruct(self):
        ExecuteUbergraph_BPW_MAM_HardDriveScanner.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_MAM_HardDriveScanner(880)
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_MAM_HardDriveScanner(904)
    

    def TypeText(self, text: FText):
        ExecuteUbergraph_BPW_MAM_HardDriveScanner.K2Node_CustomEvent_Text = text #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_MAM_HardDriveScanner(1012)
    

    def BndEvt__Button_102_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_MAM_HardDriveScanner(1156)
    

    def BndEvt__mScanButton_K2Node_ComponentBoundEvent_1_OnButtonReleasedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_MAM_HardDriveScanner(1714)
    

    def BndEvt__mScanButton_K2Node_ComponentBoundEvent_2_OnButtonPressedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_MAM_HardDriveScanner(2016)
    

    def BndEvt__mScanButton_K2Node_ComponentBoundEvent_3_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_MAM_HardDriveScanner(2148)
    

    def BndEvt__mScanButton_K2Node_ComponentBoundEvent_4_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_MAM_HardDriveScanner(2238)
    

    def ExecuteUbergraph_BPW_MAM_HardDriveScanner(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.StartIdleTextAnim()
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L487")
        if not self.mTypingText:
            goto('L865')
        
        ReturnValue: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[self.mText])
        
        ReturnValue2: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[self.mText])
        ReturnValue1: int32 = Default__KismetStringLibrary.Len(ReturnValue2)
        ReturnValue1_0: int32 = ReturnValue1 - 1
        ReturnValue2_0: int32 = ReturnValue1_0 - Variable
        ReturnValue_0: FString = Default__KismetStringLibrary.LeftChop(ReturnValue, ReturnValue2_0)
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_0)
        self.mTextObject.SetText(ReturnValue_1)
        goto(ExecutionFlow.Pop())
        # Label 487
        ReturnValue_2: int32 = Variable + 1
        Variable: int32 = ReturnValue_2
        
        # Label 556
        ReturnValue1_1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[self.mText])
        ReturnValue_3: int32 = Default__KismetStringLibrary.Len(ReturnValue1_1)
        ReturnValue_4: int32 = ReturnValue_3 - 1
        ReturnValue_5: bool = Variable <= ReturnValue_4
        if not ReturnValue_5:
            goto('L849')
        Default__KismetSystemLibrary.Delay(self, self.mTypingSpeed, LatentActionInfo(Linkage = 30, UUID = -1958267569, ExecutionFunction = "ExecuteUbergraph_BPW_MAM_HardDriveScanner", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 849
        self.mTypingText = False
        goto('L15')
        # Label 865
        self.StartIdleTextAnim()
        goto(ExecutionFlow.Pop())
        self.SetText(self.mText)
        goto(ExecutionFlow.Pop())
        self.StartIdleTextAnim()
        ReturnValue_6: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.LightPulse, 0, 0, 0, 1)
        self.UpdateCostIcon()
        self.Widget_CostSlotWrapper.mForceEmptyAnim = True
        goto(ExecutionFlow.Pop())
        
        Text = None
        ReturnValue_7: FText = Default__KismetTextLibrary.TextToUpper(Ref[Text])
        self.mText = ReturnValue_7
        self.mTypingText = True
        self.StopAnimation(self.IdleText)
        Variable = 0
        goto('L556')
        ReturnValue_8: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue_8, self.mHardDriveDescriptor, self, Ref[numItems])
        ReturnValue_9: bool = numItems > 0
        if not ReturnValue_9:
            goto('L1322')
        self.OnScanStarted.ProcessMulticastDelegate()
        self.UpdateCostIcon()
        goto(ExecutionFlow.Pop())
        # Label 1322
        ReturnValue2_1: bool = Not_PreBool(self.mRebooting)
        if not ReturnValue2_1:
           goto(ExecutionFlow.Pop())
        ReturnValue_10: int32 = RandomInteger(100)
        ReturnValue_11: bool = EqualEqual_IntInt(ReturnValue_10, 0)
        ReturnValue_12: bool = BooleanOR(ReturnValue_11, self.mSentienceProgramStarted)
        
        ReturnValue_13: int32 = len(self.mSentienceProgram)
        ReturnValue_14: bool = self.mSentienceIndex <= ReturnValue_13
        ReturnValue_15: bool = ReturnValue_12 and ReturnValue_14
        if not ReturnValue_15:
            goto('L1630')
        self.RunSentienceSequence()
        goto(ExecutionFlow.Pop())
        # Label 1630
        self.ShowTimedMessage("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1645, 'Value': '>> No hard drive is available'}")
        goto(ExecutionFlow.Pop())
        ReturnValue_16: bool = self.IsHovered()
        if not ReturnValue_16:
            goto('L1884')
        # Label 1752
        SlateColor1.SpecifiedColor = LinearColor(R = 0.7604169845581055, G = 0.6674399971961975, B = 0.4956839978694916, A = 1)
        SlateColor1.ColorUseRule = 0
        self.ButtonText.SetColorAndOpacity(SlateColor1)
        goto(ExecutionFlow.Pop())
        # Label 1884
        SlateColor.SpecifiedColor = LinearColor(R = 1, G = 0.8777300119400024, B = 0.6518589854240417, A = 1)
        SlateColor.ColorUseRule = 0
        self.ButtonText.SetColorAndOpacity(SlateColor)
        goto(ExecutionFlow.Pop())
        # Label 2016
        SlateColor2.SpecifiedColor = LinearColor(R = 0.7604169845581055, G = 0.6003940105438232, B = 0.3009980022907257, A = 1)
        SlateColor2.ColorUseRule = 0
        self.ButtonText.SetColorAndOpacity(SlateColor2)
        goto(ExecutionFlow.Pop())
        ReturnValue1_2: bool = self.mScanButton.IsPressed()
        ReturnValue1_3: bool = Not_PreBool(ReturnValue1_2)
        if not ReturnValue1_3:
            goto('L2016')
        goto('L1752')
        ReturnValue_17: bool = self.mScanButton.IsPressed()
        ReturnValue_18: bool = Not_PreBool(ReturnValue_17)
        if not ReturnValue_18:
            goto('L2016')
        goto('L1884')
    

    def OnScanStarted__DelegateSignature(self):
        pass
    
