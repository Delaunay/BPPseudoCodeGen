
from codegen.ue4_stub import *

from Script.Engine import PlayFromStart
from Script.Engine import AddComponent
from Game.FactoryGame.Buildable.Factory.-Shared.BP_BuildEffect_ConveyorBeltSegment import ExecuteUbergraph_BP_BuildEffect_ConveyorBeltSegment
from Script.CoreUObject import Rotator
from Script.Engine import SplineMeshComponent
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import ETimelineDirection
from Script.Engine import MaterialInstance
from Script.Engine import SetScalarParameterValueOnMaterials
from Script.Engine import SetStartAndEnd
from Script.CoreUObject import Vector
from Script.Engine import MaterialInterface
from Script.Engine import K2_GetActorRotation
from Script.Engine import SetForcedLodModel
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

class BP_BuildEffect_ConveyorBeltSegment(Actor):
    Finalize_Glow_Power_B40707AE49467F261979CEB8628D7242: float
    Finalize_Width_Lower_B40707AE49467F261979CEB8628D7242: float
    Finalize__Direction_B40707AE49467F261979CEB8628D7242: uint8
    Materialize_MaterializeAmount_033AF93841C8F0855E90EA8FAC2A42A9: float
    Materialize__Direction_033AF93841C8F0855E90EA8FAC2A42A9: uint8
    mStartTangent: Vector
    mEndTangent: Vector
    mMesh: Ptr[StaticMesh]
    mMaterialBelt: Ptr[MaterialInstance]
    mMaterialSides: Ptr[MaterialInstance]
    MeshComponent: Ptr[SplineMeshComponent]
    mMaterialFinish_Sides: Ptr[MaterialInterface] = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Material/ConveyorSidesFinnishEffect_Inst.ConveyorSidesFinnishEffect_Inst')
    mMaterialFinish_Belt: Ptr[MaterialInterface] = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Material/ConveyorBeltFinnishEffect_Inst.ConveyorBeltFinnishEffect_Inst')
    
    def Materialize__FinishedFunc(self):
        self.ExecuteUbergraph_BP_BuildEffect_ConveyorBeltSegment(1239)
    

    def Materialize__UpdateFunc(self):
        self.ExecuteUbergraph_BP_BuildEffect_ConveyorBeltSegment(1234)
    

    def Finalize__FinishedFunc(self):
        self.ExecuteUbergraph_BP_BuildEffect_ConveyorBeltSegment(1229)
    

    def Finalize__UpdateFunc(self):
        self.ExecuteUbergraph_BP_BuildEffect_ConveyorBeltSegment(1224)
    

    def PlayFinishEffect(self):
        self.ExecuteUbergraph_BP_BuildEffect_ConveyorBeltSegment(850)
    

    def AddMesh(self):
        self.ExecuteUbergraph_BP_BuildEffect_ConveyorBeltSegment(887)
    

    def ExecuteUbergraph_BP_BuildEffect_ConveyorBeltSegment(self):
        # Label 10
        Default__KismetSystemLibrary.PrintString(self, "Failed setting static mesh", True, True, LinearColor(R = 1, G = 0, B = 0.071772001683712, A = 1), 5)
        # End
        # Label 117
        self.MeshComponent.SetEndScale(Vector2D(X = 1, Y = 1), True)
        self.Materialize.PlayFromStart()
        # End
        # Label 211
        self.MeshComponent.SetMaterial(2, self.mMaterialSides)
        if not ReturnValue:
            goto('L10')
        self.MeshComponent.SetScalarParameterValueOnMaterials("Width_Lower", 100)
        self.MeshComponent.SetScalarParameterValueOnMaterials("Glow Power", 2)
        ReturnValue: Vector = self.Spline.GetLocationAtSplinePoint(1, 0)
        ReturnValue1: Vector = self.Spline.GetLocationAtSplinePoint(0, 0)
        ReturnValue_0: Rotator = self.K2_GetActorRotation()
        ReturnValue_1: Vector = LessLess_VectorRotator(self.mEndTangent, ReturnValue_0)
        ReturnValue1_0: Vector = LessLess_VectorRotator(self.mStartTangent, ReturnValue_0)
        self.MeshComponent.SetStartAndEnd(ReturnValue1, ReturnValue1_0, ReturnValue, ReturnValue_1, True)
        self.MeshComponent.SetStartScale(Vector2D(X = 1, Y = 1), True)
        goto('L117')
        # Label 740
        self.MeshComponent.SetMaterial(1, self.mMaterialBelt)
        goto('L211')
        # Label 795
        self.MeshComponent.SetMaterial(0, self.mMaterialSides)
        goto('L740')
        self.Finalize.PlayFromStart()
        # End
        Variable: Const[Transform] = Transform(Rotator(0, 0, 0, 1), Vector(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_2: Ptr[SplineMeshComponent] = self.AddComponent("NODE_AddSplineMeshComponent-0", False, self, Ref[Variable])
        self.MeshComponent = ReturnValue_2
        self.MeshComponent.SetForcedLodModel(0)
        ReturnValue = self.MeshComponent.SetStaticMesh(self.mMesh)
        goto('L795')
        # Label 1106
        self.MeshComponent.SetScalarParameterValueOnMaterials("Glow Power", self.Finalize_Glow_Power_B40707AE49467F261979CEB8628D7242)
        # End
        # Label 1165
        self.MeshComponent.SetScalarParameterValueOnMaterials("MaterializeAmount", self.Materialize_MaterializeAmount_033AF93841C8F0855E90EA8FAC2A42A9)
        # End
        goto('L1106')
        # End
        goto('L1165')
    
