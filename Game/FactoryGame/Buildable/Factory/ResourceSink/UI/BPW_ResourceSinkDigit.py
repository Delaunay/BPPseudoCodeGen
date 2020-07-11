
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.BPW_ResourceSinkDigit import ExecuteUbergraph_BPW_ResourceSinkDigit
from Script.UMG import UserWidget
from Script.Engine import FormatArgumentData
from Script.UMG import SetRenderTranslation
from Script.Engine import K2_SetTimerDelegate
from Script.CoreUObject import Vector2D
from Script.Engine import Format
from Script.Engine import TimerHandle
from Script.Engine import GreaterEqual_FloatFloat
from Script.UMG import WidgetAnimation
from Script.Engine import NotEqual_TextText
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.BPW_ResourceSinkDigit import ExecuteUbergraph_BPW_ResourceSinkDigit.K2Node_Event_IsDesignTime
from Script.UMG import SetFont
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import FTrunc
from Script.Engine import Ease

class BPW_ResourceSinkDigit(UserWidget):
    SwitchTextAnim: Ptr[WidgetAnimation]
    mNewText: FText = NSLOCTEXT("", "CCB1ADD14E0B783BBEDCA58876ACA31E", "T")
    mOldText: FText = NSLOCTEXT("", "560B91ED4B35E788862530A3C3A59377", " ")
    mT: float
    mDuration: float = 0.20000000298023224
    mUpdateTime: float = 0.009999999776482582
    mLerpTimerHandle: TimerHandle
    mSize: float
    
    def SwitchText(self):
        self.mOldText = self.mNewText
        FormatArgumentData.ArgumentName = "new"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = self.mNewText
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "old"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = self.mOldText
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData, FormatArgumentData1]
        ReturnValue: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 487, 'Value': '{new}\r\n{old}'}", Array)
        self.mTextObject.SetText(ReturnValue)
        ReturnValue_0: float = self.mSize * -1
        ReturnValue_1: Vector2D = Vector2D(0, ReturnValue_0)
        self.mTextObject.SetRenderTranslation(ReturnValue_1)
    

    def SetText(self, mText: FText):
        
        ReturnValue: bool = Default__KismetTextLibrary.NotEqual_TextText(Ref[mText], Ref[self.mOldText])
        if not ReturnValue:
            goto('L808')
        self.mNewText = mText
        FormatArgumentData.ArgumentName = "new"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = self.mNewText
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "old"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = self.mOldText
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData, FormatArgumentData1]
        ReturnValue_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 561, 'Value': '{new}\r\n{old}'}", Array)
        self.mTextObject.SetText(ReturnValue_0)
        self.mT = 0
        OutputDelegate.BindUFunction(self, LerpDigit)
        ReturnValue_1: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mUpdateTime, True)
        self.mLerpTimerHandle = ReturnValue_1
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_ResourceSinkDigit(500)
    

    def LerpDigit(self):
        self.ExecuteUbergraph_BPW_ResourceSinkDigit(585)
    

    def Destruct(self):
        self.ExecuteUbergraph_BPW_ResourceSinkDigit(1001)
    

    def PreConstruct(self):
        ExecuteUbergraph_BPW_ResourceSinkDigit.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ResourceSinkDigit(10)
    

    def ExecuteUbergraph_BPW_ResourceSinkDigit(self):
        ReturnValue1: float = self.mSize / 100
        ReturnValue: float = self.mTextObject.Font.Size * ReturnValue1
        ReturnValue_0: int32 = FTrunc(ReturnValue)
        SlateFontInfo.FontObject = self.mTextObject.Font.FontObject
        SlateFontInfo.FontMaterial = self.mTextObject.Font.FontMaterial
        SlateFontInfo.OutlineSettings = self.mTextObject.Font.OutlineSettings
        SlateFontInfo.TypefaceFontName = self.mTextObject.Font.TypefaceFontName
        SlateFontInfo.Size = ReturnValue_0
        self.mTextObject.SetFont(SlateFontInfo)
        # End
        self.mTextObject.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 537, 'Value': 'X\r\n '}")
        # End
        ReturnValue_1: float = self.mUpdateTime / self.mDuration
        ReturnValue_2: float = ReturnValue_1 + self.mT
        self.mT = ReturnValue_2
        ReturnValue_3: float = self.mSize * -1
        ReturnValue_4: float = Ease(ReturnValue_3, 0, self.mT, 7, 3, 2)
        ReturnValue_5: Vector2D = Vector2D(0, ReturnValue_4)
        self.mTextObject.SetRenderTranslation(ReturnValue_5)
        ReturnValue_6: bool = GreaterEqual_FloatFloat(self.mT, 1)
        if not ReturnValue_6:
            goto('L1043')
        self.SwitchText()
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mLerpTimerHandle])
        # End
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mLerpTimerHandle])
    
