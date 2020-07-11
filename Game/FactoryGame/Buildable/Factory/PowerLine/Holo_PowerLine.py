
from codegen.ue4_stub import *

from Script.Engine import SetVisibility
from Script.FactoryGame import FGWireHologram
from Game.FactoryGame.Buildable.Factory.PowerLine.Holo_PowerLine import ExecuteUbergraph_Holo_PowerLine
from Game.FactoryGame.Buildable.Factory.PowerLine.Holo_PowerLine import ExecuteUbergraph_Holo_PowerLine.K2Node_Event_disabled

class Holo_PowerLine(FGWireHologram):
    mDefaultPowerPoleRecipe = NewObject[Recipe_PowerPoleMk1]()
    mMaxPlacementFloorAngle = 35
    mValidHitClasses = ['/Script/FactoryGame.FGBuildableFoundation', '/Script/FactoryGame.FGBuildableRailroadTrack', '/Script/FactoryGame.FGBuildableRoad', '/Script/FactoryGame.FGBuildable']
    mLoopSound = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent'}, ObjectClass='/Script/AkAudio.AkComponent', ObjectFlags=2883617, ObjectName='LoopSound')
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bHidden = True
    bReplicates = True
    RemoteRole = 1
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def OnAutomaticPoleDisableToggle(self):
        ExecuteUbergraph_Holo_PowerLine.K2Node_Event_disabled = Disabled #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Holo_PowerLine(10)
    

    def ExecuteUbergraph_Holo_PowerLine(self):
        self.ConnectionMesh.SetVisibility(disabled, False)
    
