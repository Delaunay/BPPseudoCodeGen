
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SparkParticles import ExecuteUbergraph_Widget_SparkParticles.K2Node_CustomEvent_Position
from Script.UMG import OverlaySlot
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import SetStructurePropertyByName
from Script.UMG import SetRenderScale
from Script.UMG import SetRenderTranslation
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SparkParticles import ExecuteUbergraph_Widget_SparkParticles
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Sparks import Widget_Sparks
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import SetFloatPropertyByName
from Script.Engine import SetBoolPropertyByName
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SparkBounce import Widget_SparkBounce
from Script.UMG import UserWidget
from Script.UMG import Create
from Script.CoreUObject import Vector2D
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SparkParticles import ExecuteUbergraph_Widget_SparkParticles.K2Node_CustomEvent_NumberOfSparks
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SparkParticles import ExecuteUbergraph_Widget_SparkParticles.K2Node_CustomEvent_Scale
from Script.UMG import AddChildToOverlay

class Widget_SparkParticles(UserWidget):
    mBounceOn: bool = True
    mMaxDistance: Vector2D
    Speed: float
    
    def CreateSparks(self, NumberOfSparks: int32):
        ExecuteUbergraph_Widget_SparkParticles.K2Node_CustomEvent_NumberOfSparks = NumberOfSparks #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SparkParticles(15)
    

    def OnSparkBounce(self, Position: Vector2D, Scale: Vector2D):
        ExecuteUbergraph_Widget_SparkParticles.K2Node_CustomEvent_Position = Position #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_SparkParticles.K2Node_CustomEvent_Scale = Scale #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SparkParticles(597)
    

    def ExecuteUbergraph_Widget_SparkParticles(self):
        goto(ComputedJump("EntryPoint"))
        Variable: int32 = 0
        # Label 38
        ReturnValue: int32 = NumberOfSparks - 1
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L523")
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Widget_Sparks] = Default__WidgetBlueprintLibrary.Create(self, Widget_Sparks, ReturnValue_1)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_2, "mBounceOn", self.mBounceOn)
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_2, "mMaxDistance", Ref[self.mMaxDistance])
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue_2, "mSpeed", self.Speed)
        ReturnValue_3: Ptr[OverlaySlot] = self.Container.AddChildToOverlay(ReturnValue_2)
        OutputDelegate.BindUFunction(self, OnSparkBounce)
        ReturnValue_2.OnParticleBounce.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 523
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L38')
        ReturnValue1: Ptr[Widget_SparkBounce] = Default__WidgetBlueprintLibrary.Create(self, Widget_SparkBounce, None)
        ReturnValue1_0: Ptr[OverlaySlot] = self.Container.AddChildToOverlay(ReturnValue1)
        ReturnValue1.SetRenderTranslation(Position)
        ReturnValue1.SetRenderScale(Scale)
        goto(ExecutionFlow.Pop())
    
