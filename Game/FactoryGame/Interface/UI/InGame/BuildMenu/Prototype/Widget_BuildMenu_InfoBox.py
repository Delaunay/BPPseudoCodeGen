
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.UMG import UMGSequencePlayer
from Script.UMG import HasAnyChildren
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu_InfoBox import ExecuteUbergraph_Widget_BuildMenu_InfoBox
from Script.UMG import Widget
from Script.UMG import PlayAnimation
from Script.Engine import Delay
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu_InfoBox import ExecuteUbergraph_Widget_BuildMenu_InfoBox.K2Node_Event_IsDesignTime
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import Widget_CostSlotWrapper
from Script.UMG import GetChildrenCount
from Script.UMG import WidgetAnimation
from Script.Engine import LatentActionInfo
from Script.UMG import UserWidget

class Widget_BuildMenu_InfoBox(UserWidget):
    IconAnim: Ptr[WidgetAnimation]
    mOverwriteInfo: bool
    
    def GetByProductIconVisibility(self, IsValid: bool):
        if not IsValid:
            goto('L57')
        self.mByProductOverlay.SetVisibility(0)
        # End
        # Label 57
        self.mByProductOverlay.SetVisibility(1)
    

    def GetStatsVisibility(self):
        ReturnValue: bool = self.mStatContainer.HasAnyChildren()
        if not ReturnValue:
            goto('L99')
        self.mStatsBox.SetVisibility(0)
        # End
        # Label 99
        self.mStatsBox.SetVisibility(1)
    

    def AnimateCostSlots(self):
        self.ExecuteUbergraph_Widget_BuildMenu_InfoBox(509)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_BuildMenu_InfoBox.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_BuildMenu_InfoBox(528)
    

    def ExecuteUbergraph_Widget_BuildMenu_InfoBox(self):
        goto(ComputedJump("EntryPoint"))
        ExecutionFlow.Push("L237")
        ReturnValue: Ptr[Widget] = self.mCostContainer.GetChildAt(Variable)
        Wrapper: Ptr[Widget_CostSlotWrapper] = Cast[Widget_CostSlotWrapper](ReturnValue)
        bSuccess: bool = Wrapper
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_0: Ptr[UMGSequencePlayer] = Wrapper.PlayAnimation(Wrapper.FadeAnim, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 237
        ReturnValue_1: int32 = Variable + 1
        Variable: int32 = ReturnValue_1
        # Label 306
        ReturnValue_2: int32 = self.mCostContainer.GetChildrenCount()
        ReturnValue_3: bool = Variable <= ReturnValue_2
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, 0.019999999552965164, LatentActionInfo(Linkage = 15, UUID = -1663413554, ExecutionFunction = "ExecuteUbergraph_Widget_BuildMenu_InfoBox", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 481
        Variable = 0
        goto('L306')
        self.GetStatsVisibility()
        goto('L481')
        Variable_0: uint8 = 1
        Variable1: uint8 = 4
        Variable_1: bool = self.mOverwriteInfo
        
        switch = {
            False: Variable1,
            True: Variable_0
        }
        self.mStandardInfo_1.SetVisibility(switch.get(Variable_1, None))
        
        switch_0 = {
            False: Variable1,
            True: Variable_0
        }
        self.mStandardInfo_2.SetVisibility(switch_0.get(Variable_1, None))
        Variable1_0: bool = self.mOverwriteInfo
        Variable2: uint8 = 4
        Variable3: uint8 = 1
        
        switch_1 = {
            False: Variable3,
            True: Variable2
        }
        self.mOverwriteSlot.SetVisibility(switch_1.get(Variable1_0, None))
        goto(ExecutionFlow.Pop())
    
