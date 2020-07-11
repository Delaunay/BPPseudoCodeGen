
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Buildable.Factory.CA_SplitterSmart.Build_ConveyorAttachmentSplitterSmart import ExecuteUbergraph_Build_ConveyorAttachmentSplitterSmart
from Script.FactoryGame import FGBuildableSplitterSmart
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.Factory.ConveyorBeltMk1.Audio.Play_F_Construction_ConveyorBelt import Play_F_Construction_ConveyorBelt

class Build_ConveyorAttachmentSplitterSmart(FGBuildableSplitterSmart):
    mSortRules = [{'ItemClass': '/Script/FactoryGame.FGWildCardDescriptor', 'OutputIndex': 0}, {'ItemClass': 'None', 'OutputIndex': 2}, {'ItemClass': 'None', 'OutputIndex': 1}]
    mCurrentOutputIndex = -1
    mPowerConsumptionExponent = 1.600000023841858
    mMinimumProducingTime = -1
    mMinimumStoppedTime = -1
    mNumCyclesForProductivity = 20
    mCurrentPotential = 1
    mPendingPotential = 1
    mMinPotential = 0.009999999776482582
    mMaxPotential = 1
    mMaxPotentialIncreasePerCrystal = 0.5
    mFluidStackSizeDefault = EStackSize::SS_FLUID
    mFluidStackSizeMultiplier = 1
    mSignificanceRange = 18000
    mHologramClass = NewObject[Holo_ConveyorAttachment]()
    mDisplayName = NSLOCTEXT("", "DDCEE94042483A5C6F947DA5BC2EFCCA", "Smart Splitter")
    mDescription = NSLOCTEXT("", "4EBA72A247B94BBDBD22B284B6887FE2", "Splits conveyor belts in three. \r\nYou can set a rule for which part should go to the left and which part should go to the right.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_SplitterSmart]()
    mIsUseable = True
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def PlayConstructSound(self):
        self.ExecuteUbergraph_Build_ConveyorAttachmentSplitterSmart(10)
    

    def ExecuteUbergraph_Build_ConveyorAttachmentSplitterSmart(self):
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_F_Construction_ConveyorBelt, self, True)
    
