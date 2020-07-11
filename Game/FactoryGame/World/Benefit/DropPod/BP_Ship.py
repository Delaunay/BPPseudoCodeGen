
from codegen.ue4_stub import *

from Script.Engine import ParticleSystemComponent
from Script.Engine import Actor
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import ReceiveEndPlay
from Game.FactoryGame.World.Benefit.DropPod.BP_Ship import ExecuteUbergraph_BP_Ship
from Script.FactoryGame import RemoveGainSignificanceObjectFromSignificanceManager
from Script.FactoryGame import AddGainSignificanceObjectToSignificanceManager
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.Engine import ReceiveBeginPlay
from Script.Engine import GetComponentsByClass
from Game.FactoryGame.World.Benefit.DropPod.BP_Ship import ExecuteUbergraph_BP_Ship.K2Node_Event_EndPlayReason

class BP_Ship(Actor):
    
    
    def GainedSignificance(self):
        self.ExecuteUbergraph_BP_Ship(1162)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_BP_Ship(1228)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_Ship(1271)
    

    def ReceiveEndPlay(self):
        ExecuteUbergraph_BP_Ship.K2Node_Event_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Ship(1321)
    

    def ExecuteUbergraph_BP_Ship(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L287")
        ReturnValue: List[Ptr[ParticleSystemComponent]] = self.GetComponentsByClass(ParticleSystemComponent)
        
        Item = None
        Item = ReturnValue[Variable1]
        Item.Activate(False)
        ReturnValue = self.GetComponentsByClass(ParticleSystemComponent)
        
        Item = None
        Item = ReturnValue[Variable1]
        Item.SetComponentTickEnabled(True)
        goto(ExecutionFlow.Pop())
        # Label 287
        ReturnValue1: int32 = Variable1 + 1
        Variable1: int32 = ReturnValue1
        # Label 356
        ReturnValue = self.GetComponentsByClass(ParticleSystemComponent)
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable1 <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable1 = Variable1
        goto('L15')
        # Label 532
        Default__FGBlueprintFunctionLibrary.RemoveGainSignificanceObjectFromSignificanceManager(self, self)
        goto(ExecutionFlow.Pop())
        # Label 567
        ExecutionFlow.Push("L838")
        ReturnValue1_0: List[Ptr[ParticleSystemComponent]] = self.GetComponentsByClass(ParticleSystemComponent)
        
        Item1 = None
        Item1 = ReturnValue1_0[Variable]
        Item1.Deactivate()
        ReturnValue1_0 = self.GetComponentsByClass(ParticleSystemComponent)
        
        Item1 = None
        Item1 = ReturnValue1_0[Variable]
        Item1.SetComponentTickEnabled(False)
        goto(ExecutionFlow.Pop())
        # Label 838
        ReturnValue_2: int32 = Variable + 1
        Variable: int32 = ReturnValue_2
        # Label 907
        ReturnValue1_0 = self.GetComponentsByClass(ParticleSystemComponent)
        
        ReturnValue1_1: int32 = len(ReturnValue1_0)
        ReturnValue1_2: bool = Variable <= ReturnValue1_1
        if not ReturnValue1_2:
           goto(ExecutionFlow.Pop())
        Variable = Variable
        goto('L567')
        # Label 1083
        Variable = 0
        Variable = 0
        goto('L907')
        # Label 1134
        Variable1 = 0
        goto('L356')
        self.StaticMesh.SetCollisionEnabled(3)
        Variable1 = 0
        goto('L1134')
        self.StaticMesh.SetCollisionEnabled(0)
        goto('L1083')
        self.ReceiveBeginPlay()
        Default__FGBlueprintFunctionLibrary.AddGainSignificanceObjectToSignificanceManager(self, self, 8000)
        goto(ExecutionFlow.Pop())
        self.ReceiveEndPlay(EndPlayReason)
        goto('L532')
    
