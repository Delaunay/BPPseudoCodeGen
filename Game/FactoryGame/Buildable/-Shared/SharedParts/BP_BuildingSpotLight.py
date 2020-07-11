
from codegen.ue4_stub import *

from Script.Engine import Actor
from Script.Engine import SetVisibility
from Script.Engine import GetOwner
from Game.FactoryGame.Buildable.-Shared.SharedParts.BP_BuildingSpotLight import ExecuteUbergraph_BP_BuildingSpotLight.K2Node_CustomEvent_state
from Game.FactoryGame.Buildable.-Shared.SharedParts.BP_BuildingSpotLight import ExecuteUbergraph_BP_BuildingSpotLight
from Script.Engine import SpotLightComponent
from Script.Engine import ReceiveBeginPlay
from Script.FactoryGame import FGBuildableFactory

class BP_BuildingSpotLight(SpotLightComponent):
    InnerConeAngle = 44
    LightGuid = Namespace(A=1866929874, B=1172740450, C=701779117, D=-99869905)
    Intensity = 1500
    LightColor = Namespace(A=255, B=181, G=241, R=255)
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_BuildingSpotLight(188)
    

    def HasPowerChanged(self, State: bool):
        ExecuteUbergraph_BP_BuildingSpotLight.K2Node_CustomEvent_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_BuildingSpotLight(193)
    

    def ExecuteUbergraph_BP_BuildingSpotLight(self):
        # Label 10
        self.ReceiveBeginPlay()
        ReturnValue: Ptr[Actor] = self.GetOwner()
        Factory: Ptr[FGBuildableFactory] = Cast[FGBuildableFactory](ReturnValue)
        bSuccess: bool = Factory
        if not bSuccess:
            goto('L213')
        OutputDelegate.BindUFunction(self, HasPowerChanged)
        Factory.mOnHasPowerChanged.AddUnique(OutputDelegate)
        # End
        goto('L10')
        self.SetVisibility(state, False)
    
