
from codegen.ue4_stub import *

from Script.Engine import SetTextPropertyByName
from Script.Engine import Delay
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.BPW_ResourceSink_ScrollingCounter import ExecuteUbergraph_BPW_ResourceSink_ScrollingCounter.K2Node_CustomEvent_TextToAnimate
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.BPW_ResourceSinkDigit import BPW_ResourceSinkDigit
from Script.UMG import HorizontalBoxSlot
from Script.UMG import GetChildrenCount
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import Len
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import SetHeightOverride
from Script.Engine import SetFloatPropertyByName
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.BPW_ResourceSink_ScrollingCounter import ExecuteUbergraph_BPW_ResourceSink_ScrollingCounter
from Script.UMG import Widget
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import Conv_IntToString
from Script.UMG import UserWidget
from Script.UMG import AddChildToHorizontalBox
from Script.UMG import Create
from Script.UMG import SetVerticalAlignment
from Script.Engine import GetCharacterArrayFromString
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.BPW_ResourceSink_ScrollingCounter import ExecuteUbergraph_BPW_ResourceSink_ScrollingCounter.K2Node_Event_IsDesignTime

class BPW_ResourceSink_ScrollingCounter(UserWidget):
    mSize: float = 100
    mLatestNumber: int32 = -1
    
    def UpdateCounter(self, NewNumber: int32):
        ExecutionFlow.Push("L1358")
        ReturnValue: bool = NewNumber != self.mLatestNumber
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        self.mLatestNumber = NewNumber
        ReturnValue_0: FString = Default__KismetStringLibrary.Conv_IntToString(self.mLatestNumber)
        LocalTextToANimate = ReturnValue_0
        ReturnValue_1: int32 = Default__KismetStringLibrary.Len(LocalTextToANimate)
        NumOfDigits = ReturnValue_1
        ReturnValue1: int32 = self.mContainer.GetChildrenCount()
        ReturnValue1_0: int32 = NumOfDigits - 1
        ReturnValue2: int32 = ReturnValue1_0 - ReturnValue1
        DidgitsToAdd = ReturnValue2
        ReturnValue_2: int32 = self.mContainer.GetChildrenCount()
        ReturnValue_3: int32 = ReturnValue_2 - 1
        ReturnValue3: int32 = ReturnValue_3 - NumOfDigits
        DidgitsToRemove = ReturnValue3
        Variable: int32 = 0
        # Label 605
        ReturnValue_4: bool = Variable <= DidgitsToRemove
        if not ReturnValue_4:
            goto('L750')
        ExecutionFlow.Push("L1210")
        ReturnValue_5: Ptr[Widget] = self.mContainer.GetChildAt(Variable)
        ReturnValue_5.RemoveFromParent()
        goto(ExecutionFlow.Pop())
        # Label 750
        Variable1: int32 = 0
        # Label 773
        ReturnValue1_1: bool = Variable1 <= DidgitsToAdd
        if not ReturnValue1_1:
            goto('L1186')
        ExecutionFlow.Push("L1284")
        ReturnValue_6: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_7: Ptr[BPW_ResourceSinkDigit] = Default__WidgetBlueprintLibrary.Create(self, BPW_ResourceSinkDigit, ReturnValue_6)
        Variable_0: Const[FText] = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 935, 'Value': '0'}"
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_7, "mNewText", Ref[Variable_0])
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue_7, "mSize", self.mSize)
        ReturnValue_8: Ptr[HorizontalBoxSlot] = self.mContainer.AddChildToHorizontalBox(ReturnValue_7)
        ReturnValue_8.SetVerticalAlignment(2)
        goto(ExecutionFlow.Pop())
        # Label 1186
        self.AnimateDigits(LocalTextToANimate)
        goto(ExecutionFlow.Pop())
        # Label 1210
        ReturnValue_9: int32 = Variable + 1
        Variable = ReturnValue_9
        goto('L605')
        # Label 1284
        ReturnValue1_2: int32 = Variable1 + 1
        Variable1 = ReturnValue1_2
        goto('L773')
    

    def PreConstruct(self):
        ExecuteUbergraph_BPW_ResourceSink_ScrollingCounter.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ResourceSink_ScrollingCounter(958)
    

    def AnimateDigits(self, TextToAnimate: FString):
        ExecuteUbergraph_BPW_ResourceSink_ScrollingCounter.K2Node_CustomEvent_TextToAnimate = TextToAnimate #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ResourceSink_ScrollingCounter(1000)
    

    def ExecuteUbergraph_BPW_ResourceSink_ScrollingCounter(self):
        goto(ComputedJump("EntryPoint"))
        ExecutionFlow.Push("L663")
        ReturnValue: int32 = Default__KismetStringLibrary.Len(TextToAnimate)
        ReturnValue_0: int32 = ReturnValue - 1
        ReturnValue1: int32 = ReturnValue_0 - Variable
        ReturnValue_1: Ptr[Widget] = self.mContainer.GetChildAt(ReturnValue1)
        Digit: Ptr[BPW_ResourceSinkDigit] = Cast[BPW_ResourceSinkDigit](ReturnValue_1)
        bSuccess: bool = Digit
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: List[FString] = Default__KismetStringLibrary.GetCharacterArrayFromString(TextToAnimate)
        ReturnValue = Default__KismetStringLibrary.Len(TextToAnimate)
        ReturnValue_0 = ReturnValue - 1
        ReturnValue1 = ReturnValue_0 - Variable
        
        Item = None
        Item = ReturnValue_2[ReturnValue1]
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_StringToText(Item)
        Digit.SetText(ReturnValue_3)
        goto(ExecutionFlow.Pop())
        # Label 663
        ReturnValue_4: int32 = Variable + 1
        Variable: int32 = ReturnValue_4
        # Label 732
        ReturnValue = Default__KismetStringLibrary.Len(TextToAnimate)
        ReturnValue_0 = ReturnValue - 1
        ReturnValue_5: bool = Variable <= ReturnValue_0
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, 0.05000000074505806, LatentActionInfo(Linkage = 15, UUID = -2027353807, ExecutionFunction = "ExecuteUbergraph_BPW_ResourceSink_ScrollingCounter", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.mSizeBox.SetHeightOverride(self.mSize)
        goto(ExecutionFlow.Pop())
        Variable = 0
        goto('L732')
    
