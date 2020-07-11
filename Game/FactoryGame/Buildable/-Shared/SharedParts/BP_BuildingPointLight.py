
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.-Shared.SharedParts.BP_BuildingPointLight import ExecuteUbergraph_BP_BuildingPointLight.K2Node_CustomEvent_state
from Script.Engine import Actor
from Script.Engine import SetVisibility
from Script.Engine import GetOwner
from Game.FactoryGame.Buildable.-Shared.SharedParts.BP_BuildingPointLight import ExecuteUbergraph_BP_BuildingPointLight
from Script.Engine import PointLightComponent
from Script.Engine import ReceiveBeginPlay
from Script.FactoryGame import FGBuildableFactory

class BP_BuildingPointLight(PointLightComponent):
    SourceRadius = 200
    AttenuationRadius = 500
    LightGuid = Namespace(A=928822274, B=1184417401, C=1556996520, D=37844629)
    Intensity = 1500
    LightColor = Namespace(A=255, B=181, G=241, R=255)
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_BuildingPointLight(188)
    

    def HasPowerChanged(self, State: bool):
        ExecuteUbergraph_BP_BuildingPointLight.K2Node_CustomEvent_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_BuildingPointLight(193)
    

    def ExecuteUbergraph_BP_BuildingPointLight(self):
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
    
