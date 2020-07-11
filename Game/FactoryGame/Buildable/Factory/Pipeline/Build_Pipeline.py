
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildablePipeline

class Build_Pipeline(FGBuildablePipeline):
    mRadius = 65
    mFlowLimit = 5
    mFlowIndicatorClass = NewObject[BP_PipeFlowIndicatorComponent]()
    mFlowIndicatorMinimumPipeLength = 400
    mSplineAudioEvent = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/Pipeline/Audio/Play_Pipeline.Play_Pipeline')
    mMaxIndicatorTurnAngle = 3
    mFluidNames = [{'WwiseSafeName': 'Crude_Oil', 'ActualName': 'Crude Oil'}, {'WwiseSafeName': 'Fuel', 'ActualName': 'Fuel'}, {'WwiseSafeName': 'Heavy_Oil_Residue', 'ActualName': 'Heavy Oil Residue'}, {'WwiseSafeName': 'Water', 'ActualName': 'Water'}, {'WwiseSafeName': 'No_Fluid', 'ActualName': 'N/A'}]
    mRattleLimit = 0.5
    mStartRattleSoundEvent = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/Pipeline/Audio/Play_Pipeline_Rattle.Play_Pipeline_Rattle')
    mStopRattleSoundEvent = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/Pipeline/Audio/Stop_Pipeline_Rattle.Stop_Pipeline_Rattle')
    mMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/Pipeline/Mesh/SM_Pipe.SM_Pipe')
    mMeshLength = 100
    mSplineComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/Engine.SplineComponent', ObjectFlags=2883617, ObjectName='SplineComponent')
    mInstancedSplineComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, ObjectClass='/Script/InstancedSplines.FGInstancedSplineMeshComponent', ObjectFlags=2883617, ObjectName='InstancedSplineComponent')
    mHologramClass = NewObject[Holo_Pipeline]()
    mDisplayName = NSLOCTEXT("", "B235BEFC41C74A2EAC8E4CB51796D3A6", "Pipeline")
    mDescription = NSLOCTEXT("", "F342E9104323D0072DC923A20E32C89D", "Outside indicators show volume, flow rate and direction.\r\nTransports up to 300m³ of fluid per minute.\r\nUsed to transport fluids.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mColorSlot = 17
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_PipelineBuild.BP_MaterialEffect_PipelineBuild_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_PipelineInspector]()
    mIsUseable = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0.10000000149011612, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def UserConstructionScript(self):
        self.mConnection0 = self.PipelineConnection0
        self.mConnection1 = self.PipelineConnection1
    
