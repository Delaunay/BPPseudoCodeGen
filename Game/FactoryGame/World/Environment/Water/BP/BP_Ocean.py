
from codegen.ue4_stub import *

from Script.Engine import SetScalarParameterValue
from Script.Engine import Actor
from Script.CoreUObject import Vector
from Script.Engine import SetVectorParameterValue
from Script.Engine import K2_GetComponentLocation
from Script.Engine import MaterialInterface
from Script.Engine import MaterialInstanceDynamic
from Script.CoreUObject import LinearColor

class BP_Ocean(Actor):
    Ocean_Material: Ptr[MaterialInterface] = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Water/Material/MI_Ocean.MI_Ocean')
    Water_Scale_X: float = 50
    Water_Scale_Y: float = 50
    Wave_Speed: float = 1
    Water_Material: Ptr[MaterialInstanceDynamic]
    Variation_Amount: float = 0.8500000238418579
    Primary_Water_Color: LinearColor = Namespace(A=1, B=0.35416701436042786, G=0.23517300188541412, R=0.1977050006389618)
    Secondary_Water_Color: LinearColor = Namespace(A=1, B=0.6866859793663025, G=0.715694010257721, R=0.5583410263061523)
    Base_Opacity: float = 1
    Shore_Depth: float = 70
    Depth_Scale: float = 580
    Deep_Water_Color: LinearColor = Namespace(A=1, B=1, G=0.8796229958534241, R=0.8069519996643066)
    Shallow_Water_Color: LinearColor = Namespace(A=1, B=0.7908610105514526, G=1, R=0.5980460047721863)
    Displacement: float
    
    def UserConstructionScript(self):
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.WaterSurface.CreateDynamicMaterialInstance(0, self.Ocean_Material, "None")
        self.Water_Material = ReturnValue
        ReturnValue_0: Vector = Vector(self.Water_Scale_X, self.Water_Scale_Y, 1)
        self.WaterSurface.SetRelativeScale3D(ReturnValue_0)
        self.Water_Material.SetScalarParameterValue("Shore Depth", self.Shore_Depth)
        self.Water_Material.SetScalarParameterValue("Wave Speed", self.Wave_Speed)
        self.Water_Material.SetScalarParameterValue("BaseOpacity", self.Base_Opacity)
        ReturnValue_1: Vector = self.WaterSurface.K2_GetComponentLocation()
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_1)
        self.Water_Material.SetScalarParameterValue("Water Height", Z)
        self.Water_Material.SetScalarParameterValue("Variation Amount", self.Variation_Amount)
        self.Water_Material.SetVectorParameterValue("WaterColor A", self.Primary_Water_Color)
        self.Water_Material.SetVectorParameterValue("WaterColor B", self.Secondary_Water_Color)
        self.Water_Material.SetScalarParameterValue("Displacement", self.Displacement)
        self.Water_Material.SetScalarParameterValue("Water Depth", self.Depth_Scale)
        self.Water_Material.SetVectorParameterValue("DeepWater", self.Deep_Water_Color)
        self.Water_Material.SetVectorParameterValue("ShallowWater", self.Shallow_Water_Color)
    
