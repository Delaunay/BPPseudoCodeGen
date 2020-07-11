
from codegen.ue4_stub import *

from Script.Engine import SetScalarParameterValue
from Script.FactoryGame import GetIndicatorFlowPct
from Script.Engine import MaterialInstanceDynamic
from Script.Engine import Default__KismetSystemLibrary
from Script.CoreUObject import Color
from Game.FactoryGame.Buildable.Factory.Pipeline.FlowIndicator.BP_PipeFlowIndicatorComponent import ExecuteUbergraph_BP_PipeFlowIndicatorComponent
from Script.Engine import SetVectorParameterValue
from Script.FactoryGame import GetIndicatorContentPct
from Script.FactoryGame import GetPipeline
from Script.Engine import Conv_ColorToLinearColor
from Game.FactoryGame.Buildable.Factory.Pipeline.FlowIndicator.BP_PipeFlowIndicatorComponent import ExecuteUbergraph_BP_PipeFlowIndicatorComponent.K2Node_Event_DeltaSeconds
from Script.Engine import MaterialInterface
from Game.FactoryGame.Buildable.Factory.Pipeline.FlowIndicator.BP_PipeFlowIndicatorComponent import ExecuteUbergraph_BP_PipeFlowIndicatorComponent.K2Node_Event_fluidDescriptor
from Script.FactoryGame import FGPipelineFlowIndicatorComponent
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import FGItemDescriptor
from Script.FactoryGame import FGBuildablePipeline
from Script.FactoryGame import GetFluidColor
from Script.Engine import IsValidClass
from Script.CoreUObject import LinearColor

class BP_PipeFlowIndicatorComponent(FGPipelineFlowIndicatorComponent):
    Instance: Ptr[MaterialInstanceDynamic]
    NewColor: Color
    mEmptyColor: Color = Namespace(A=255, B=0, G=0, R=0)
    mCurrentFluidDescriptor: TSubclassOf[FGItemDescriptor]
    StaticMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/Pipeline/FlowIndicator/SM_StatusInd_01.SM_StatusInd_01')
    OverrideMaterials = [{'$AssetPath': '/Game/FactoryGame/Buildable/Factory/Pipeline/FlowIndicator/IM_PipeInducator_01.IM_PipeInducator_01'}]
    PrimaryComponentTick = Namespace(EndTickGroup=0, TickGroup=2, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    
    def ApplyFlowData(self):
        ReturnValue: Ptr[FGBuildablePipeline] = self.GetPipeline()
        ReturnValue_0: float = ReturnValue.GetIndicatorFlowPct()
        self.Instance.SetScalarParameterValue("FlowDirection", ReturnValue_0)
        ReturnValue = self.GetPipeline()
        ReturnValue_1: float = ReturnValue.GetIndicatorContentPct()
        self.Instance.SetScalarParameterValue("Content", ReturnValue_1)
    

    def ApplyFluidDescriptorColor(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mCurrentFluidDescriptor)
        if not ReturnValue:
            goto('L247')
        ReturnValue_0: Color = Default__FGItemDescriptor.GetFluidColor(self.mCurrentFluidDescriptor)
        self.NewColor = ReturnValue_0
        # Label 151
        ReturnValue_1: LinearColor = Conv_ColorToLinearColor(self.NewColor)
        self.Instance.SetVectorParameterValue("LiquidColour", ReturnValue_1)
        # End
        # Label 247
        self.NewColor = self.mEmptyColor
        goto('L151')
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_PipeFlowIndicatorComponent.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PipeFlowIndicatorComponent(10)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_PipeFlowIndicatorComponent(43)
    

    def OnFluidDescriptorSet(self):
        ExecuteUbergraph_BP_PipeFlowIndicatorComponent.K2Node_Event_fluidDescriptor = fluidDescriptor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PipeFlowIndicatorComponent(217)
    

    def OnMaterialInstanceUpdated(self):
        self.ExecuteUbergraph_BP_PipeFlowIndicatorComponent(255)
    

    def ExecuteUbergraph_BP_PipeFlowIndicatorComponent(self):
        self.ApplyFlowData()
        self.ApplyFluidDescriptorColor()
        # End
        ReturnValue1: Ptr[MaterialInterface] = self.GetMaterial(0)
        Dynamic1: Ptr[MaterialInstanceDynamic] = Cast[MaterialInstanceDynamic](ReturnValue1)
        bSuccess1: bool = Dynamic1
        if not bSuccess1:
            goto('L410')
        # Label 151
        self.Instance = Dynamic1
        self.SetMaterial(0, self.Instance)
        # End
        self.mCurrentFluidDescriptor = fluidDescriptor
        self.ApplyFluidDescriptorColor()
        # End
        ReturnValue: Ptr[MaterialInterface] = self.GetMaterial(0)
        Dynamic: Ptr[MaterialInstanceDynamic] = Cast[MaterialInstanceDynamic](ReturnValue)
        bSuccess: bool = Dynamic
        if not bSuccess:
            goto('L410')
        self.Instance = Dynamic
        self.ApplyFlowData()
        self.ApplyFluidDescriptorColor()
    
