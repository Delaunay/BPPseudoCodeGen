
from codegen.ue4_stub import *

from Script.Engine import SetScalarParameterValue
from Script.Engine import Actor
from Script.CoreUObject import Vector
from Script.Engine import SetVectorParameterValue
from Script.Engine import MaterialInterface
from Script.Engine import MaterialInstanceDynamic
from Script.CoreUObject import LinearColor

class BP_LakeWater(Actor):
    Ocean_Material: Ptr[MaterialInterface] = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Water/Lake/Material/LakeWater_01_Inst.LakeWater_01_Inst')
    Water_Scale_X: float = 1
    Water_Scale_Y: float = 1
    Wave_Speed: float = 1
    Water_Material: Ptr[MaterialInstanceDynamic]
    Overall_Water_Scale: float = 512
    Variation_Amount: float = 0.5
    Primary_Water_Color: LinearColor = Namespace(A=0, B=0.042472999542951584, G=0.04500000178813934, R=0.018449999392032623)
    Secondary_Water_Color: LinearColor = Namespace(A=0, B=0.32499998807907104, G=0.27116599678993225, R=0.16256499290466309)
    
    def UserConstructionScript(self):
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.WaterSurface.CreateDynamicMaterialInstance(0, self.Ocean_Material, "None")
        self.Water_Material = ReturnValue
        ReturnValue_0: Vector = Vector(self.Water_Scale_X, self.Water_Scale_Y, 1)
        self.WaterSurface.SetRelativeScale3D(ReturnValue_0)
        self.Water_Material.SetScalarParameterValue("Water Scale", self.Overall_Water_Scale)
        self.Water_Material.SetScalarParameterValue("Variation Amount", self.Variation_Amount)
        self.Water_Material.SetScalarParameterValue("Wave Speed", self.Wave_Speed)
        self.Water_Material.SetVectorParameterValue("WaterColor A", self.Primary_Water_Color)
        self.Water_Material.SetVectorParameterValue("WaterColor B", self.Secondary_Water_Color)
    
