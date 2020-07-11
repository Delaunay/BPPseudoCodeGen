
from codegen.ue4_stub import *

from Script.FactoryGame import FGConveyorAttachmentHologram
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import BreakRotator
from Script.Engine import K2_SetRelativeRotation
from Script.Engine import StaticMeshComponent
from Game.FactoryGame.Buildable.Factory.-Shared.Holo_ConveyorAttachment import ExecuteUbergraph_Holo_ConveyorAttachment.K2Node_Event_inBuildable
from Game.FactoryGame.Buildable.Factory.-Shared.Holo_ConveyorAttachment import ExecuteUbergraph_Holo_ConveyorAttachment
from Script.CoreUObject import Rotator
from Script.Engine import K2_GetActorRotation
from Script.Engine import GetComponentsByTag
from Script.Engine import MakeRotator

class Holo_ConveyorAttachment(FGConveyorAttachmentHologram):
    mMaxValidTurnOffset = 240
    mMaxValidTurnAngle = 3
    mMaxPlacementFloorAngle = 35
    mValidHitClasses = ['/Script/FactoryGame.FGBuildableFoundation', '/Script/FactoryGame.FGBuildableRailroadTrack', '/Script/FactoryGame.FGBuildableRoad', '/Script/FactoryGame.FGBuildableConveyorBelt', '/Script/FactoryGame.FGBuildableConveyorAttachment']
    mLoopSound = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent'}, ObjectClass='/Script/AkAudio.AkComponent', ObjectFlags=2883617, ObjectName='LoopSound')
    bHidden = True
    bReplicates = True
    RemoteRole = 1
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def ReceiveConfigureComponents(self):
        ExecuteUbergraph_Holo_ConveyorAttachment.K2Node_Event_inBuildable = inBuildable #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Holo_ConveyorAttachment(15)
    

    def ExecuteUbergraph_Holo_ConveyorAttachment(self):
        goto(ComputedJump("EntryPoint"))
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 61
        ReturnValue: List[Ptr[StaticMeshComponent]] = inBuildable.GetComponentsByTag(StaticMeshComponent, "Sides")
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L641")
        ReturnValue_2: Rotator = inBuildable.K2_GetActorRotation()
        ReturnValue = inBuildable.GetComponentsByTag(StaticMeshComponent, "Sides")
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_2, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_3: float = 0 - Pitch
        ReturnValue_4: Rotator = MakeRotator(0, ReturnValue_3, 0)
        
        Item = None
        Item = ReturnValue[Variable_0]
        
        SweepHitResult = None
        Item.K2_SetRelativeRotation(ReturnValue_4, False, False, Ref[SweepHitResult])
        goto(ExecutionFlow.Pop())
        # Label 641
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L61')
    
