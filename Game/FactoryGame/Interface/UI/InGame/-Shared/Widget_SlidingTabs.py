
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SlidingTabs import ExecuteUbergraph_Widget_SlidingTabs.K2Node_Event_IsDesignTime
from Script.Engine import FClamp
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SlidingTabs import ExecuteUbergraph_Widget_SlidingTabs
from Script.UMG import GetChildIndex
from Script.UMG import GetChildrenCount
from Script.Engine import Ease
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import SetRenderTranslation
from Script.Engine import TimerHandle
from Script.Engine import GreaterEqual_FloatFloat
from Script.Engine import IsValid
from Script.UMG import GetDesiredSize
from Script.Engine import EqualEqual_IntInt
from Script.Engine import BreakVector2D
from Script.UMG import Widget
from Script.Engine import PrintString
from Script.UMG import ForceLayoutPrepass
from Script.UMG import SetWidthOverride
from Script.UMG import UserWidget
from Script.Engine import Map_Add
from Script.Engine import Map_Find
from Script.UMG import HorizontalBox
from Script.CoreUObject import Vector2D
from Script.Engine import Default__BlueprintMapLibrary
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SlidingTabs_Button import Widget_SlidingTabs_Button
from Script.CoreUObject import LinearColor

class Widget_SlidingTabs(UserWidget):
    mHorizontalBox: Ptr[HorizontalBox]
    mIndexOffset: Dict[int32, float]
    mLerpT: float
    mLerpStartingWidth: float
    mLerpStartingPos: float
    mUpdateTime: float = 0.009999999776482582
    mSlideTime: float = 0.25
    mActiveIndex: int32
    mLerpTimer: TimerHandle
    mButtons: List[Ptr[Widget_SlidingTabs_Button]]
    mStartIndex: int32
    
    def SetActiveButton(self):
        ExecutionFlow.Push("L646")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(self.mButtons)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L572")
        
        Item = None
        Item = self.mButtons[Variable_0]
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(Item.mTargetWidget)
        ReturnValue_2: int32 = self.mHorizontalBox.GetChildIndex(Item.mTargetWidget)
        Variable_1: bool = ReturnValue_1
        
        switch = {
            False: Item.mTargetIndex,
            True: ReturnValue_2
        }
        ReturnValue_3: bool = EqualEqual_IntInt(self.mActiveIndex, switch.get(Variable_1, None))
        Item.SetActive(ReturnValue_3)
        goto(ExecutionFlow.Pop())
        # Label 572
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L51')
    

    def SetupIndexOffset(self):
        ExecutionFlow.Push("L551")
        self.ForceLayoutPrepass()
        LocalOffset = 0
        Variable: int32 = 0
        # Label 61
        ReturnValue: int32 = self.mHorizontalBox.GetChildrenCount()
        ReturnValue_0: int32 = ReturnValue - 1
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L477")
        
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mIndexOffset], Ref[Variable], Ref[LocalOffset])
        ReturnValue_2: Ptr[Widget] = self.mHorizontalBox.GetChildAt(Variable)
        ReturnValue_3: Vector2D = ReturnValue_2.GetDesiredSize()
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_3, Ref[X], Ref[Y])
        ReturnValue_4: float = LocalOffset - X
        LocalOffset = ReturnValue_4
        goto(ExecutionFlow.Pop())
        # Label 477
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L61')
    

    def SetActiveIndex(self, index: int32, Animate: bool):
        self.mActiveIndex = index
        self.SetActiveButton()
        if not Animate:
            goto('L388')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mLerpTimer])
        self.mLerpStartingWidth = self.mSizeBox.WidthOverride
        self.mLerpT = 0
        
        X = None
        Y = None
        BreakVector2D(self.mContent.RenderTransform.Translation, Ref[X], Ref[Y])
        self.mLerpStartingPos = X
        OutputDelegate.BindUFunction(self, SlideLerp)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mUpdateTime, True)
        self.mLerpTimer = ReturnValue
        # End
        # Label 388
        ReturnValue_0: Ptr[Widget] = self.mHorizontalBox.GetChildAt(self.mActiveIndex)
        ReturnValue_1: Vector2D = ReturnValue_0.GetDesiredSize()
        
        X1 = None
        Y1 = None
        BreakVector2D(ReturnValue_1, Ref[X1], Ref[Y1])
        self.mSizeBox.SetWidthOverride(X1)
        
        Value = None
        ReturnValue_2: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mIndexOffset], Ref[self.mActiveIndex], Ref[Value])
        ReturnValue_3: Vector2D = Vector2D(Value, 0)
        self.mContent.SetRenderTranslation(ReturnValue_3)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SlidingTabs(15)
    

    def SlideLerp(self):
        self.ExecuteUbergraph_Widget_SlidingTabs(460)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_SlidingTabs.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SlidingTabs(10)
    

    def ExecuteUbergraph_Widget_SlidingTabs(self):
        # End
        ReturnValue: Ptr[Widget] = self.mContent.GetChildAt(0)
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L311')
        ReturnValue = self.mContent.GetChildAt(0)
        Box: Ptr[HorizontalBox] = Cast[HorizontalBox](ReturnValue)
        bSuccess: bool = Box
        if not bSuccess:
            goto('L311')
        self.mHorizontalBox = Box
        self.SetupIndexOffset()
        self.SetActiveIndex(0, False)
        # End
        # Label 311
        Default__KismetSystemLibrary.PrintString(self, "Horizontalbox not found - Put Horizontal Box into Widget_SlidingTabs", True, True, LinearColor(R = 1, G = 0, B = 0, A = 1), 4)
        # End
        ReturnValue_1: float = self.mUpdateTime / self.mSlideTime
        ReturnValue_2: float = ReturnValue_1 + self.mLerpT
        ReturnValue_3: float = FClamp(ReturnValue_2, 0, 1)
        self.mLerpT = ReturnValue_3
        
        Value = None
        ReturnValue_4: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mIndexOffset], Ref[self.mActiveIndex], Ref[Value])
        ReturnValue_5: float = Ease(self.mLerpStartingPos, Value, self.mLerpT, 6, 4, 2)
        ReturnValue_6: Vector2D = Vector2D(ReturnValue_5, 0)
        self.mContent.SetRenderTranslation(ReturnValue_6)
        ReturnValue1: Ptr[Widget] = self.mHorizontalBox.GetChildAt(self.mActiveIndex)
        ReturnValue_7: Vector2D = ReturnValue1.GetDesiredSize()
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_7, Ref[X], Ref[Y])
        ReturnValue1_0: float = Ease(self.mLerpStartingWidth, X, self.mLerpT, 6, 4, 2)
        self.mSizeBox.SetWidthOverride(ReturnValue1_0)
        ReturnValue_8: bool = GreaterEqual_FloatFloat(self.mLerpT, 1)
        if not ReturnValue_8:
            goto('L1181')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mLerpTimer])
    
