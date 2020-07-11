
from codegen.ue4_stub import *

from Script.Engine import SetScalarParameterValue
from Script.Engine import Actor
from Script.CoreUObject import Vector
from Script.Engine import K2_GetComponentLocation
from Script.Engine import MaterialInterface
from Script.Engine import MaterialInstanceDynamic
from Script.CoreUObject import LinearColor

class BP_Water(Actor):
    Ocean_Material: Ptr[MaterialInterface] = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Water/Material/Lake_Inst.Lake_Inst')
    Water_Scale_X: float = 50
    Water_Scale_Y: float = 50
    Wave_Speed: float = 1
    Water_Material: Ptr[MaterialInstanceDynamic]
    Variation_Amount: float = 0.8500000238418579
    Primary_Water_Color: LinearColor = Namespace(A=1, B=0.23000000417232513, G=0.1307000070810318, R=0.10000000149011612)
    Secondary_Water_Color: LinearColor = Namespace(A=1, B=0.6274150013923645, G=0.6549999713897705, R=0.5305500030517578)
    Base_Opacity: float = 1
    Shore_Depth: float = 16
    Depth_Scale: float = 580
    Deep_Water_Color: LinearColor = Namespace(A=1, B=0.8849999904632568, G=0.7757059931755066, R=0.7124249935150146)
    Shallow_Water_Color: LinearColor = Namespace(A=1, B=0.7950000166893005, G=0.9316669702529907, R=1)
    UnderWater: Ptr[MaterialInterface] = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Water/Material/UnderWaterSuface_Master.UnderWaterSuface_Master')
    UnderWater_Material: Ptr[MaterialInstanceDynamic]
    
    def UserConstructionScript(self):
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.WaterSurface.CreateDynamicMaterialInstance(0, self.Ocean_Material, "None")
        self.Water_Material = ReturnValue
        ReturnValue_0: Vector = Vector(self.Water_Scale_X, self.Water_Scale_Y, 1)
        self.WaterSurface.SetRelativeScale3D(ReturnValue_0)
        ReturnValue1: Ptr[MaterialInstanceDynamic] = self.WaterPlaneUnderSide_01.CreateDynamicMaterialInstance(0, self.UnderWater, "None")
        self.UnderWater_Material = ReturnValue1
        self.Water_Material.SetScalarParameterValue("Shore Depth", self.Shore_Depth)
        self.Water_Material.SetScalarParameterValue("Wave Speed", self.Wave_Speed)
        self.Water_Material.SetScalarParameterValue("BaseOpacity", self.Base_Opacity)
        ReturnValue1_0: Vector = self.WaterSurface.K2_GetComponentLocation()
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(ReturnValue1_0)
        self.Water_Material.SetScalarParameterValue("Water Height", Z1)
        ReturnValue_1: Vector = self.WaterPlaneUnderSide_01.K2_GetComponentLocation()
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_1)
        self.UnderWater_Material.SetScalarParameterValue("Water Height", Z)
        self.Water_Material.SetScalarParameterValue("Variation Amount", self.Variation_Amount)
        self.Water_Material.SetScalarParameterValue("Water Depth", self.Depth_Scale)
    
