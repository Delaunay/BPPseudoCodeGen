
from codegen.ue4_stub import *

from Script.Engine import PlayFromStart
from Script.Engine import AddComponent
from Script.CoreUObject import Rotator
from Script.Engine import SplineMeshComponent
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import ETimelineDirection
from Script.Engine import MaterialInstance
from Script.Engine import SetScalarParameterValueOnMaterials
from Game.FactoryGame.Buildable.Factory.-Shared.BP_BuildEffect_PipelineSegment import ExecuteUbergraph_BP_BuildEffect_PipelineSegment
from Script.Engine import SetStartAndEnd
from Script.CoreUObject import Vector
from Script.Engine import K2_GetActorRotation
from Script.Engine import LessLess_VectorRotator
from Script.Engine import SetStartScale
from Script.Engine import SetEndScale
from Script.Engine import Actor
from Script.Engine import GetLocationAtSplinePoint
from Script.CoreUObject import Vector2D
from Script.CoreUObject import Transform
from Script.Engine import PrintString
from Script.Engine import StaticMesh
from Script.CoreUObject import LinearColor

class BP_BuildEffect_PipelineSegment(Actor):
    Finalize_Glow_Power_402F7B5743D35B44BEF02CB897B8A7D1: float
    Finalize_Width_Lower_402F7B5743D35B44BEF02CB897B8A7D1: float
    Finalize__Direction_402F7B5743D35B44BEF02CB897B8A7D1: uint8
    Materialize_MaterializeAmount_FEA0B9D541A0830F53AC54B70A9C2612: float
    Materialize__Direction_FEA0B9D541A0830F53AC54B70A9C2612: uint8
    mStartTangent: Vector
    mEndTangent: Vector
    mMesh: Ptr[StaticMesh]
    mPipeMaterial: Ptr[MaterialInstance]
    MeshComponent: Ptr[SplineMeshComponent]
    
    def Materialize__FinishedFunc(self):
        self.ExecuteUbergraph_BP_BuildEffect_PipelineSegment(10)
    

    def Materialize__UpdateFunc(self):
        self.ExecuteUbergraph_BP_BuildEffect_PipelineSegment(1132)
    

    def Finalize__FinishedFunc(self):
        self.ExecuteUbergraph_BP_BuildEffect_PipelineSegment(1127)
    

    def Finalize__UpdateFunc(self):
        self.ExecuteUbergraph_BP_BuildEffect_PipelineSegment(1122)
    

    def AddMesh(self):
        self.ExecuteUbergraph_BP_BuildEffect_PipelineSegment(122)
    

    def PlayFinishEffect(self):
        self.ExecuteUbergraph_BP_BuildEffect_PipelineSegment(1026)
    

    def ExecuteUbergraph_BP_BuildEffect_PipelineSegment(self):
        # End
        # Label 15
        Default__KismetSystemLibrary.PrintString(self, "Failed setting static mesh", True, True, LinearColor(R = 1, G = 0, B = 0.071772001683712, A = 1), 5)
        # End
        Variable: Const[Transform] = Transform(Rotator(0, 0, 0, 1), Vector(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue: Ptr[SplineMeshComponent] = self.AddComponent("NODE_AddSplineMeshComponent-0", False, self, Ref[Variable])
        self.MeshComponent = ReturnValue
        ReturnValue_0: bool = self.MeshComponent.SetStaticMesh(self.mMesh)
        self.MeshComponent.SetMaterial(0, self.mPipeMaterial)
        self.MeshComponent.SetMaterial(1, self.mPipeMaterial)
        if not ReturnValue_0:
            goto('L15')
        self.MeshComponent.SetScalarParameterValueOnMaterials("Width_Lower", 100)
        self.MeshComponent.SetScalarParameterValueOnMaterials("Glow Power", 2)
        ReturnValue_1: Vector = self.Spline.GetLocationAtSplinePoint(1, 0)
        ReturnValue1: Vector = self.Spline.GetLocationAtSplinePoint(0, 0)
        ReturnValue_2: Rotator = self.K2_GetActorRotation()
        ReturnValue_3: Vector = LessLess_VectorRotator(self.mEndTangent, ReturnValue_2)
        ReturnValue1_0: Vector = LessLess_VectorRotator(self.mStartTangent, ReturnValue_2)
        self.MeshComponent.SetStartAndEnd(ReturnValue1, ReturnValue1_0, ReturnValue_1, ReturnValue_3, True)
        self.MeshComponent.SetStartScale(Vector2D(X = 1, Y = 1), True)
        self.MeshComponent.SetEndScale(Vector2D(X = 1, Y = 1), True)
        self.Materialize.PlayFromStart()
        # End
        # Label 967
        self.MeshComponent.SetScalarParameterValueOnMaterials("MaterializeAmount", self.Materialize_MaterializeAmount_FEA0B9D541A0830F53AC54B70A9C2612)
        # End
        self.Finalize.PlayFromStart()
        # End
        # Label 1063
        self.MeshComponent.SetScalarParameterValueOnMaterials("Glow Power", self.Finalize_Glow_Power_402F7B5743D35B44BEF02CB897B8A7D1)
        # End
        goto('L1063')
        # End
        goto('L967')
    
