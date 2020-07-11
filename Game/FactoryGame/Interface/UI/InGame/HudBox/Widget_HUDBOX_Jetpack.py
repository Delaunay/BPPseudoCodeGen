
from codegen.ue4_stub import *

from Script.Engine import K2_SetTimerDelegate
from Script.Engine import Pawn
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import TimerHandle
from Game.FactoryGame.Resource.Parts.Fuel.Desc_Fuel import Desc_Fuel
from Script.Engine import IsValid
from Script.UMG import SetPercent
from Script.Engine import GreaterEqual_FloatFloat
from Script.Engine import CurveFloat
from Script.UMG import SetFillColorAndOpacity
from Script.FactoryGame import FGJetPack
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBOX_Jetpack import ExecuteUbergraph_Widget_HUDBox_Jetpack
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBOX_Jetpack import ExecuteUbergraph_Widget_HUDBox_Jetpack.K2Node_Event_MyGeometry
from Script.FactoryGame import FGItemDescriptor
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Equipment_Parent import Widget_HUDBox_Equipment_Parent
from Script.UMG import SetRenderOpacity
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBOX_Jetpack import ExecuteUbergraph_Widget_HUDBox_Jetpack.K2Node_Event_InDeltaTime
from Script.Engine import GetFloatValue
from Script.CoreUObject import LinearColor

class Widget_HUDBox_Jetpack(Widget_HUDBox_Equipment_Parent):
    mFGJetPack: Ptr[FGJetPack]
    CurrentPercent: float
    PulseT: float
    PulseUpdate: float = 0.05000000074505806
    SineCurve: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Curves/SineCurve.SineCurve')
    PulseTimer: TimerHandle
    IsFlying: bool
    PulseDuration: float = 0.4000000059604645
    PulseColor: LinearColor
    LowFuelThreshold: float = 0.30000001192092896
    mFuelClass: TSubclassOf[FGItemDescriptor]
    bHasScriptImplementedTick = True
    
    def StopPulse(self):
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.PulseTimer])
        self.Widget_ProgressBar.mProgressBar.SetRenderOpacity(1)
    

    def StartPulse(self):
        self.PulseT = 0
        OutputDelegate.BindUFunction(self, BarPulse)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.PulseUpdate, True)
        self.PulseTimer = ReturnValue
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_HUDBox_Jetpack(1238)
    

    def Tick(self):
        ExecuteUbergraph_Widget_HUDBox_Jetpack.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_HUDBox_Jetpack.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_HUDBox_Jetpack(1411)
    

    def BarPulse(self):
        self.ExecuteUbergraph_Widget_HUDBox_Jetpack(1416)
    

    def ExecuteUbergraph_Widget_HUDBox_Jetpack(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Variable: bool = False
        self.StartPulse()
        self.mHudBoxParent.StartWarningSign()
        goto(ExecutionFlow.Pop())
        # Label 77
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mFGJetPack)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        ReturnValue_0: float = self.mFGJetPack.GetMaxFuel()
        ReturnValue_1: float = self.mFGJetPack.GetCurrentFuel()
        ReturnValue_2: float = ReturnValue_1 / ReturnValue_0
        self.CurrentPercent = ReturnValue_2
        ExecutionFlow.Push("L435")
        ReturnValue_3: bool = self.CurrentPercent <= self.Widget_ProgressBar.mProgressBar.Percent
        if not ReturnValue_3:
            goto('L903')
        if not Variable1:
            goto('L1070')
        goto(ExecutionFlow.Pop())
        # Label 435
        self.Widget_ProgressBar.mProgressBar.SetPercent(self.CurrentPercent)
        ReturnValue_4: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue_4, self.mFuelClass, self, Ref[numItems])
        ReturnValue_5: bool = numItems > 0
        ItemAmount.ItemClass = self.mFuelClass
        ItemAmount.amount = numItems
        self.FuelSlot.Setup CostIcon(None, ItemAmount, None, 0, 0, False, False, ReturnValue_5)
        ReturnValue1: bool = self.CurrentPercent <= self.LowFuelThreshold
        if not ReturnValue1:
            goto('L815')
        if not Variable2:
            goto('L1222')
        goto(ExecutionFlow.Pop())
        # Label 815
        Variable2: bool = False
        if not Variable:
            goto('L841')
        goto(ExecutionFlow.Pop())
        # Label 841
        Variable = True
        self.StopPulse()
        self.mHudBoxParent.StopWarningSign()
        goto(ExecutionFlow.Pop())
        # Label 903
        Variable1: bool = False
        if not Variable3:
            goto('L929')
        goto(ExecutionFlow.Pop())
        # Label 929
        Variable3: bool = True
        self.IsFlying = False
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        self.Widget_ProgressBar.mProgressBar.SetFillColorAndOpacity(GraphicsWhite)
        goto(ExecutionFlow.Pop())
        # Label 1070
        Variable1 = True
        Variable3 = False
        self.IsFlying = True
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        self.Widget_ProgressBar.mProgressBar.SetFillColorAndOpacity(Orange)
        goto(ExecutionFlow.Pop())
        # Label 1222
        Variable2 = True
        goto('L15')
        Pack: Ptr[FGJetPack] = Cast[FGJetPack](self.mEquipment)
        bSuccess: bool = Pack
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        self.mFGJetPack = Pack
        self.Widget_ProgressBar.mProgressBar.SetPercent(1)
        self.mFuelClass = Desc_Fuel
        goto(ExecutionFlow.Pop())
        goto('L77')
        ReturnValue1_0: float = self.PulseUpdate / self.PulseDuration
        ReturnValue_6: float = ReturnValue1_0 + self.PulseT
        self.PulseT = ReturnValue_6
        ReturnValue_7: float = self.SineCurve.GetFloatValue(self.PulseT)
        ReturnValue_8: float = 1 - ReturnValue_7
        ReturnValue_9: float = ReturnValue_8 * 1 - 0.5 + 0.5
        self.Widget_ProgressBar.mProgressBar.SetRenderOpacity(ReturnValue_9)
        ReturnValue_10: bool = GreaterEqual_FloatFloat(self.PulseT, 1)
        if not ReturnValue_10:
           goto(ExecutionFlow.Pop())
        self.PulseT = 0
        goto(ExecutionFlow.Pop())
    
