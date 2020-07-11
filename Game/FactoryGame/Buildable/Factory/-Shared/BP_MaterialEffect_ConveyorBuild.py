
from codegen.ue4_stub import *

from Script.FactoryGame import PreStarted
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Actor
from Script.Engine import Default__GameplayStatics
from Script.Engine import FinishSpawningActor
from Script.Engine import GetOwner
from Script.FactoryGame import FGMaterialEffect_Build
from Script.Engine import GetTransform
from Game.FactoryGame.Buildable.Factory.-Shared.BP_MaterialEffect_ConveyorBuild import ExecuteUbergraph_BP_MaterialEffect_ConveyorBuild.K2Node_Event_deltaTime
from Script.Engine import IsValid
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.CoreUObject import Transform
from Game.FactoryGame.Buildable.Factory.-Shared.BP_BuildEffect_ConveyorBelt import BP_BuildEffect_ConveyorBelt
from Game.FactoryGame.Buildable.Factory.-Shared.BP_MaterialEffect_ConveyorBuild import ExecuteUbergraph_BP_MaterialEffect_ConveyorBuild

class BP_MaterialEffect_ConveyorBuild(FGMaterialEffect_Build):
    mBuildEffectActor: Ptr[BP_BuildEffect_ConveyorBelt]
    mAutoDestroy = True
    PrimaryComponentTick = Namespace(EndTickGroup=0, TickGroup=2, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bAutoActivate = True
    
    def PreStarted(self):
        self.ExecuteUbergraph_BP_MaterialEffect_ConveyorBuild(10)
    

    def OnStarted(self):
        self.ExecuteUbergraph_BP_MaterialEffect_ConveyorBuild(419)
    

    def OnUpdate(self):
        ExecuteUbergraph_BP_MaterialEffect_ConveyorBuild.K2Node_Event_deltaTime = DeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_MaterialEffect_ConveyorBuild(457)
    

    def ExecuteUbergraph_BP_MaterialEffect_ConveyorBuild(self):
        self.PreStarted()
        ReturnValue: Ptr[Actor] = self.GetOwner()
        ReturnValue_0: Transform = ReturnValue.GetTransform()
        
        ReturnValue_1: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_BuildEffect_ConveyorBelt, 0, ReturnValue, Ref[ReturnValue_0])
        ReturnValue = self.GetOwner()
        ReturnValue_0 = ReturnValue.GetTransform()
        
        ReturnValue_2: Ptr[BP_BuildEffect_ConveyorBelt] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_1, Ref[ReturnValue_0])
        self.mBuildEffectActor = ReturnValue_2
        # End
        # Label 316
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(self.mBuildEffectActor)
        if not ReturnValue_3:
            goto('L386')
        # End
        # Label 386
        self.Deactivate()
        # End
        self.mBuildEffectActor.mWantToStartEffect = True
        # End
        goto('L316')
    
