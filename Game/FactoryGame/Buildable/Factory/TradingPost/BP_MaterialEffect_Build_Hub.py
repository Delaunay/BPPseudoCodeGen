
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.TradingPost.BP_MaterialEffect_Build_Hub import ExecuteUbergraph_BP_MaterialEffect_Build_Hub
from Game.FactoryGame.Buildable.Factory.-Shared.BP_MaterialEffect_Build import BP_MaterialEffect_Build

class BP_MaterialEffect_Build_Hub(BP_MaterialEffect_Build):
    mAutoDestroy = True
    PrimaryComponentTick = Namespace(EndTickGroup=0, TickGroup=2, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bAutoActivate = True
    
    def PlayThumpSound(self):
        self.ExecuteUbergraph_BP_MaterialEffect_Build_Hub(10)
    

    def ExecuteUbergraph_BP_MaterialEffect_Build_Hub(self):
        pass
    
