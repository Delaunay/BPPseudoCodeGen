
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.-Shared.BP_MaterialEffect_PipelineBuild import ExecuteUbergraph_BP_MaterialEffect_PipelineBuild
from Script.FactoryGame import PreStarted
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Actor
from Script.Engine import Default__GameplayStatics
from Script.Engine import FinishSpawningActor
from Script.Engine import GetOwner
from Script.Engine import SetObjectPropertyByName
from Script.FactoryGame import FGMaterialEffect_Build
from Script.Engine import GetTransform
from Script.FactoryGame import GetInstigator
from Script.FactoryGame import FGPipeBuilderTrail
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.-Shared.BP_BuildEffect_Pipeline import BP_BuildEffect_Pipeline
from Script.CoreUObject import Transform
from Game.FactoryGame.Buildable.Factory.-Shared.BP_MaterialEffect_PipelineBuild import ExecuteUbergraph_BP_MaterialEffect_PipelineBuild.K2Node_Event_deltaTime

class BP_MaterialEffect_PipelineBuild(FGMaterialEffect_Build):
    mBuildEffectPipelineActor: Ptr[BP_BuildEffect_Pipeline]
    mAutoDestroy = True
    PrimaryComponentTick = Namespace(EndTickGroup=0, TickGroup=2, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bAutoActivate = True
    
    def PreStarted(self):
        self.ExecuteUbergraph_BP_MaterialEffect_PipelineBuild(43)
    

    def OnStarted(self):
        self.ExecuteUbergraph_BP_MaterialEffect_PipelineBuild(807)
    

    def OnUpdate(self):
        ExecuteUbergraph_BP_MaterialEffect_PipelineBuild.K2Node_Event_deltaTime = DeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_MaterialEffect_PipelineBuild(845)
    

    def ExecuteUbergraph_BP_MaterialEffect_PipelineBuild(self):
        # Label 10
        self.Deactivate()
        # End
        self.PreStarted()
        ReturnValue: Ptr[Actor] = self.GetInstigator()
        Trail: Ptr[FGPipeBuilderTrail] = Cast[FGPipeBuilderTrail](ReturnValue)
        bSuccess: bool = Trail
        if not bSuccess:
            goto('L511')
        ReturnValue_0: Ptr[Actor] = self.GetOwner()
        ReturnValue_1: Transform = ReturnValue_0.GetTransform()
        
        ReturnValue_2: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_BuildEffect_Pipeline, 0, ReturnValue_0, Ref[ReturnValue_1])
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mAttachment", Trail)
        ReturnValue_0 = self.GetOwner()
        ReturnValue_1 = ReturnValue_0.GetTransform()
        
        ReturnValue_3: Ptr[BP_BuildEffect_Pipeline] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_2, Ref[ReturnValue_1])
        self.mBuildEffectPipelineActor = ReturnValue_3
        # End
        # Label 511
        ReturnValue_0 = self.GetOwner()
        ReturnValue_1 = ReturnValue_0.GetTransform()
        
        ReturnValue1: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_BuildEffect_Pipeline, 0, ReturnValue_0, Ref[ReturnValue_1])
        ReturnValue_0 = self.GetOwner()
        ReturnValue_1 = ReturnValue_0.GetTransform()
        
        ReturnValue1_0: Ptr[BP_BuildEffect_Pipeline] = Default__GameplayStatics.FinishSpawningActor(ReturnValue1, Ref[ReturnValue_1])
        self.mBuildEffectPipelineActor = ReturnValue1_0
        # End
        self.mBuildEffectPipelineActor.mWantToStartEffect = True
        # End
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(self.mBuildEffectPipelineActor)
        if not ReturnValue_4:
            goto('L10')
    
