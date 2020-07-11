
from codegen.ue4_stub import *

from Script.FactoryGame import PreStarted
from Script.FactoryGame import GetFloatCurveValue
from Script.Engine import FClamp
from Script.FactoryGame import FGMaterialEffect_Build
from Script.FactoryGame import GetSpeed
from Script.Engine import GetTransform
from Script.FactoryGame import SetDuration
from Script.Engine import BreakTransform
from Script.Engine import FMin
from Script.FactoryGame import SetMeshes
from Game.FactoryGame.Buildable.Factory.-Shared.BP_MaterialEffect_Dismantle import ExecuteUbergraph_BP_MaterialEffect_Dismantle.K2Node_Event_deltaTime
from Game.FactoryGame.Buildable.Factory.-Shared.BP_MaterialEffect_Dismantle import ExecuteUbergraph_BP_MaterialEffect_Dismantle
from Script.Engine import RuntimeFloatCurve
from Script.FactoryGame import Default__FGSkySphere
from Script.FactoryGame import SetMaterialScalarParameterValue
from Script.FactoryGame import OnUpdate
from Script.Engine import Actor
from Script.FactoryGame import GetMeshesBounds
from Script.FactoryGame import OnStarted
from Script.Engine import GetOwner
from Script.FactoryGame import FGBuildableSpaceElevator
from Script.CoreUObject import Transform
from Script.Engine import GetComponentsByClass
from Script.Engine import MeshComponent

class BP_MaterialEffect_Dismantle(FGMaterialEffect_Build):
    mElapsedTime: float
    mMaterializeDuration: float
    mMaterializeCurve: RuntimeFloatCurve = Namespace(EditorCurveData={'Keys': [{'InterpMode': 2, 'TangentMode': 1, 'TangentWeightMode': 0, 'Time': 0, 'Value': 1, 'ArriveTangent': -0.011613549664616585, 'ArriveTangentWeight': 0, 'LeaveTangent': -0.01161355059593916, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 1, 'TangentWeightMode': 0, 'Time': 1, 'Value': 0, 'ArriveTangent': -1.620108962059021, 'ArriveTangentWeight': 0, 'LeaveTangent': -1.6201057434082031, 'LeaveTangentWeight': 0}], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$Empty': True})
    mMaterial = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Material/Factory_Materialize_Inst.Factory_Materialize_Inst')
    mAutoDestroy = True
    PrimaryComponentTick = Namespace(EndTickGroup=0, TickGroup=2, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bAutoActivate = True
    
    def OnStarted(self):
        self.ExecuteUbergraph_BP_MaterialEffect_Dismantle(752)
    

    def OnUpdate(self):
        ExecuteUbergraph_BP_MaterialEffect_Dismantle.K2Node_Event_deltaTime = DeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_MaterialEffect_Dismantle(1337)
    

    def PreStarted(self):
        self.ExecuteUbergraph_BP_MaterialEffect_Dismantle(1681)
    

    def ExecuteUbergraph_BP_MaterialEffect_Dismantle(self):
        # Label 10
        self.SetDuration(self.mMaterializeDuration)
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(boxExtent)
        ReturnValue: float = Z * 2.799999952316284
        ReturnValue1: float = ReturnValue + 30
        self.SetMaterialScalarParameterValue("HeightZ", ReturnValue1)
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(boxExtent)
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(origin)
        ReturnValue_0: float = Z1 - Z
        ReturnValue1_0: float = ReturnValue_0 - 10
        self.SetMaterialScalarParameterValue("OriginZ", ReturnValue1_0)
        self.SetMaterialScalarParameterValue("BuildOffset", 0)
        # End
        # Label 436
        self.SetDuration(self.mMaterializeDuration)
        self.SetMaterialScalarParameterValue("HeightZ", 7000)
        ReturnValue_1: Ptr[Actor] = self.GetOwner()
        ReturnValue_2: Transform = ReturnValue_1.GetTransform()
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_2], Ref[Location], Ref[Rotation], Ref[Scale])
        
        X2 = None
        Y2 = None
        Z2 = None
        X2, Y2, Z2 = BreakVector(Location)
        ReturnValue2: float = Z2 + -114
        self.SetMaterialScalarParameterValue("OriginZ", ReturnValue2)
        self.SetMaterialScalarParameterValue("BuildOffset", 0)
        # End
        self.OnStarted()
        self.mElapsedTime = 0
        # Label 785
        ReturnValue_1 = self.GetOwner()
        Elevator: Ptr[FGBuildableSpaceElevator] = Cast[FGBuildableSpaceElevator](ReturnValue_1)
        bSuccess: bool = Elevator
        if not bSuccess:
            goto('L1010')
        ReturnValue_1 = self.GetOwner()
        ReturnValue_3: List[Ptr[MeshComponent]] = ReturnValue_1.GetComponentsByClass(MeshComponent)
        self.SetMeshes(ReturnValue_3)
        self.mMaterializeDuration = 8
        goto('L436')
        # Label 1010
        ReturnValue_1 = self.GetOwner()
        ReturnValue_3 = ReturnValue_1.GetComponentsByClass(MeshComponent)
        self.SetMeshes(ReturnValue_3)
        
        origin = None
        boxExtent = None
        self.GetMeshesBounds(False, False, Ref[origin], Ref[boxExtent])
        ReturnValue_4: float = self.GetSpeed()
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(boxExtent)
        ReturnValue1_1: float = Z / ReturnValue_4
        ReturnValue_5: float = FClamp(ReturnValue1_1, 0.4000000059604645, 8)
        self.mMaterializeDuration = ReturnValue_5
        goto('L10')
        self.OnUpdate(deltaTime)
        ReturnValue_6: float = self.mElapsedTime + deltaTime
        self.mElapsedTime = ReturnValue_6
        ReturnValue_7: bool = self.mElapsedTime <= self.mMaterializeDuration
        if not ReturnValue_7:
            goto('L1647')
        ReturnValue_8: float = FMin(self.mElapsedTime / self.mMaterializeDuration, 1)
        
        ReturnValue_9: float = Default__FGSkySphere.GetFloatCurveValue(ReturnValue_8, Ref[self.mMaterializeCurve])
        self.SetMaterialScalarParameterValue("MaterializeAmount", ReturnValue_9)
        # End
        # Label 1647
        self.Deactivate()
        # End
        # Label 1666
        self.PreStarted()
        goto('L785')
        goto('L1666')
    
