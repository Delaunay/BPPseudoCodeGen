
from codegen.ue4_stub import *

from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Interface.UI.InGame.DirectionalSubtitles.Widget_DirectionalSubtitles import ExecuteUbergraph_Widget_DirectionalSubtitles.K2Node_CustomEvent_Duration
from Script.Engine import Pawn
from Game.FactoryGame.Interface.UI.InGame.DirectionalSubtitles.Widget_DirectionalSubtitles import ExecuteUbergraph_Widget_DirectionalSubtitles.K2Node_CustomEvent_Actor
from Game.FactoryGame.Interface.UI.InGame.DirectionalSubtitles.Widget_DirectionalSubtitles import ExecuteUbergraph_Widget_DirectionalSubtitles.K2Node_CustomEvent_EndPlayReason
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Script.Engine import TimerHandle
from Script.UMG import StopAnimation
from Script.Engine import IsValid
from Script.Engine import DegAtan2
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.Engine import Normal
from Game.FactoryGame.Interface.UI.InGame.DirectionalSubtitles.Widget_DirectionalSubtitles import ExecuteUbergraph_Widget_DirectionalSubtitles
from Script.UMG import WidgetAnimation
from Script.Engine import RetriggerableDelay
from Script.UMG import UserWidget
from Script.UMG import GetOwningPlayerPawn
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Script.UMG import UMGSequencePlayer
from Script.Engine import Multiply_VectorVector
from Script.UMG import SetRenderOpacity
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import GetActorForwardVector

class Widget_DirectionalSubtitles(UserWidget):
    Pop: Ptr[WidgetAnimation]
    FadeOut: Ptr[WidgetAnimation]
    mSubtitle: FText
    mInstigator: Ptr[Actor]
    mDuration: float
    mCenterSensititivity: float = 40
    OnDestruct: FMulticastScriptDelegate
    mDirectionTimer: TimerHandle
    mUseDuration: bool
    mForceDestroySubtitle: bool
    padding = Namespace(Bottom=2, Left=0, Right=0, Top=2)
    
    def ForceDestroySubtitle(self):
        self.mForceDestroySubtitle = True
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.FadeOut, 0, 1, 0, 1)
    

    def OnAnimDestruct(self):
        self.RemoveFromParent()
    

    def SetSubtitleText(self, mSubtitle: FText):
        self.mSubtitle = mSubtitle
        self.mSubtitleObject.SetText(self.mSubtitle)
    

    def UpdateSubtitle(self, mSubtitle: FText, Duration: float, UseDuration: bool):
        self.SetSubtitleText(mSubtitle)
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.Pop, 0, 1, 0, 1)
        self.mUseDuration = UseDuration
        if not self.mUseDuration:
            goto('L125')
        self.Event UpdateDestructionTimer(Duration)
    

    def SetDirectionVisibility(self):
        LocalAngle = 0
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mInstigator)
        if not ReturnValue:
            goto('L566')
        ReturnValue_0: float = self.GetInstigatorAngle()
        LocalAngle = ReturnValue_0
        Variable2: uint8 = 0
        Variable3: uint8 = 2
        ReturnValue_1: float = self.mCenterSensititivity * -1
        ReturnValue_2: bool = LocalAngle <= ReturnValue_1
        Variable1: bool = ReturnValue_2
        
        switch = {
            False: Variable3,
            True: Variable2
        }
        self.mLeft.SetVisibility(switch.get(Variable1, None))
        Variable: uint8 = 0
        Variable1_0: uint8 = 2
        ReturnValue_3: bool = LocalAngle > self.mCenterSensititivity
        Variable_0: bool = ReturnValue_3
        
        switch_0 = {
            False: Variable1_0,
            True: Variable
        }
        self.mRight.SetVisibility(switch_0.get(Variable_0, None))
        # End
        
        # Label 566
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mDirectionTimer])
        ReturnValue_4: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.FadeOut, 0, 1, 0, 1)
    

    def GetInstigatorAngle(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L1086')
        ReturnValue1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_1: Vector = ReturnValue1.K2_GetActorLocation()
        ReturnValue_2: Vector = Multiply_VectorVector(ReturnValue_1, Vector(1, 1, 0))
        ReturnValue2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue1_0: Vector = self.mInstigator.K2_GetActorLocation()
        ReturnValue_3: Vector = ReturnValue2.GetActorForwardVector()
        ReturnValue1_1: Vector = Multiply_VectorVector(ReturnValue1_0, Vector(1, 1, 0))
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_3)
        ReturnValue_4: Vector = Subtract_VectorVector(ReturnValue1_1, ReturnValue_2)
        ReturnValue_5: float = DegAtan2(Y, X)
        ReturnValue_6: Vector = Normal(ReturnValue_4, 9.999999747378752e-05)
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(ReturnValue_6)
        ReturnValue1_2: float = DegAtan2(Y1, X1)
        ReturnValue_7: float = ReturnValue1_2 - ReturnValue_5
        ReturnValue_8: float = ReturnValue_7 + 360
        ReturnValue_9: bool = ReturnValue_7 <= 0
        Variable1: bool = ReturnValue_9
        
        switch = {
            False: ReturnValue_7,
            True: ReturnValue_8
        }
        ReturnValue_10: bool = switch.get(Variable1, None) > 180
        
        switch_0 = {
            False: ReturnValue_7,
            True: ReturnValue_8
        }
        ReturnValue1_3: float = switch_0.get(Variable1, None) - 360
        Variable: bool = ReturnValue_10
        
        switch_1 = {
            False: ReturnValue_7,
            True: ReturnValue_8
        }
        
        switch_2 = {
            False: switch_1.get(Variable1, None),
            True: ReturnValue1_3
        }
        ReturnValue_11: float = switch_2.get(Variable, None)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_DirectionalSubtitles(302)
    

    def Event UpdateDestructionTimer(self, Duration: float):
        ExecuteUbergraph_Widget_DirectionalSubtitles.K2Node_CustomEvent_Duration = Duration #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_DirectionalSubtitles(537)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_DirectionalSubtitles(664)
    

    def On Instigator End Play(self, Actor: Ptr[Actor], EndPlayReason: uint8):
        ExecuteUbergraph_Widget_DirectionalSubtitles.K2Node_CustomEvent_Actor = Actor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_DirectionalSubtitles.K2Node_CustomEvent_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_DirectionalSubtitles(759)
    

    def ExecuteUbergraph_Widget_DirectionalSubtitles(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue1: bool = Not_PreBool(self.mForceDestroySubtitle)
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.FadeOut, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 101
        ReturnValue_0: bool = self.mDuration <= 3
        Variable: bool = ReturnValue_0
        Variable_0: float = 3
        
        switch = {
            False: self.mDuration,
            True: Variable_0
        }
        Default__KismetSystemLibrary.RetriggerableDelay(self, switch.get(Variable, None), LatentActionInfo(Linkage = 15, UUID = -523131293, ExecutionFunction = "ExecuteUbergraph_Widget_DirectionalSubtitles", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.UpdateSubtitle(self.mSubtitle, self.mDuration, self.mUseDuration)
        self.SetDirectionVisibility()
        OutputDelegate1.BindUFunction(self, SetDirectionVisibility)
        ReturnValue_1: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate1, 0.10000000149011612, True)
        self.mDirectionTimer = ReturnValue_1
        OutputDelegate.BindUFunction(self, On Instigator End Play)
        self.mInstigator.OnEndPlay.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        self.mDuration = Duration
        ReturnValue_2: bool = Not_PreBool(self.mForceDestroySubtitle)
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        self.StopAnimation(self.FadeOut)
        self.mContainer.SetRenderOpacity(1)
        goto('L101')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mDirectionTimer])
        self.mInstigator.OnEndPlay.Clear()
        self.OnDestruct.ProcessMulticastDelegate(self)
        goto(ExecutionFlow.Pop())
        self.ForceDestroySubtitle()
        goto(ExecutionFlow.Pop())
    

    def OnDestruct__DelegateSignature(self, InstigatingSubtitle: Ptr[Widget_DirectionalSubtitles]):
        pass
    
