
from codegen.ue4_stub import *

from Script.FactoryGame import FGLadderComponent

class BP_LadderComponent(FGLadderComponent):
    mClimbableLookAngle = 20
    mEndClimbingLookAngle = 70
    PrimaryComponentTick = Namespace(EndTickGroup=0, TickGroup=2, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    
