
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import SetFloatPropertyByName
from Script.Engine import PlayerController
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_GenericParticleSpawner import ExecuteUbergraph_Widget_GenericParticleSpawner
from Script.Engine import Texture
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import SetStructurePropertyByName
from Script.UMG import UserWidget
from Script.UMG import Create
from Script.CoreUObject import Vector2D
from Script.Engine import SetObjectPropertyByName
from Script.UMG import OverlaySlot
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_GenericParticle import Widget_GenericParticle
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_GenericParticleSpawner import ExecuteUbergraph_Widget_GenericParticleSpawner.K2Node_CustomEvent_NumberOfParticles
from Script.Engine import RandomInteger
from Script.UMG import AddChildToOverlay
from Script.CoreUObject import LinearColor

class Widget_GenericParticleSpawner(UserWidget):
    mParticleTexture: List[Ptr[Texture]]
    mParticleSize: Vector2D
    Speed: float
    mMaxDistance: Vector2D
    mStartTint: LinearColor = Namespace(A=1, B=0.05951099842786789, G=0.2917709946632385, R=0.7835379838943481)
    mEndTint: LinearColor = Namespace(A=1, B=0, G=0, R=1)
    mRotation: float
    
    def CreateParticles(self, NumberOfParticles: int32):
        ExecuteUbergraph_Widget_GenericParticleSpawner.K2Node_CustomEvent_NumberOfParticles = NumberOfParticles #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_GenericParticleSpawner(945)
    

    def ExecuteUbergraph_Widget_GenericParticleSpawner(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L753")
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_GenericParticle] = Default__WidgetBlueprintLibrary.Create(self, Widget_GenericParticle, ReturnValue)
        
        ReturnValue_1: int32 = len(self.mParticleTexture)
        ReturnValue_2: int32 = RandomInteger(ReturnValue_1)
        
        Item = None
        Item = self.mParticleTexture[ReturnValue_2]
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_0, "mParticleTexture", Item)
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_0, "mParticleSize", Ref[self.mParticleSize])
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue_0, "mSpeed", self.Speed)
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_0, "mMaxDistance", Ref[self.mMaxDistance])
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_0, "mStartTint", Ref[self.mStartTint])
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_0, "mEndTint", Ref[self.mEndTint])
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue_0, "mRotation", self.mRotation)
        ReturnValue_3: Ptr[OverlaySlot] = self.mContainer.AddChildToOverlay(ReturnValue_0)
        goto(ExecutionFlow.Pop())
        # Label 753
        ReturnValue_4: int32 = Variable + 1
        Variable: int32 = ReturnValue_4
        # Label 822
        ReturnValue_5: int32 = NumberOfParticles - 1
        ReturnValue_6: bool = Variable <= ReturnValue_5
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        goto('L15')
        # Label 917
        Variable = 0
        goto('L822')
        goto('L917')
    
