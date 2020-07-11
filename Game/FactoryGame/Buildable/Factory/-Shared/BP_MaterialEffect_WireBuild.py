
from codegen.ue4_stub import *

from Script.Engine import Actor
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.Buildable.Factory.-Shared.BP_MaterialEffect_WireBuild import ExecuteUbergraph_BP_MaterialEffect_WireBuild
from Script.Engine import FinishSpawningActor
from Script.FactoryGame import OnStarted
from Script.Engine import GetOwner
from Game.FactoryGame.Buildable.Factory.-Shared.BP_BuildEffect_Wire import BP_BuildEffect_Wire
from Script.FactoryGame import FGMaterialEffect_Build
from Script.Engine import GetTransform
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.CoreUObject import Transform

class BP_MaterialEffect_WireBuild(FGMaterialEffect_Build):
    mAutoDestroy = True
    PrimaryComponentTick = Namespace(EndTickGroup=0, TickGroup=2, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bAutoActivate = True
    
    def OnStarted(self):
        self.ExecuteUbergraph_BP_MaterialEffect_WireBuild(10)
    

    def ExecuteUbergraph_BP_MaterialEffect_WireBuild(self):
        self.OnStarted()
        ReturnValue: Ptr[Actor] = self.GetOwner()
        ReturnValue_0: Transform = ReturnValue.GetTransform()
        
        ReturnValue_1: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_BuildEffect_Wire, 0, ReturnValue, Ref[ReturnValue_0])
        ReturnValue = self.GetOwner()
        ReturnValue_0 = ReturnValue.GetTransform()
        
        ReturnValue_2: Ptr[BP_BuildEffect_Wire] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_1, Ref[ReturnValue_0])
    
