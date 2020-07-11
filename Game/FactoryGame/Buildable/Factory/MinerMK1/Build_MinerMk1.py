
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildableResourceExtractor
from Script.Engine import ReceiveDestroyed
from Script.FactoryGame import FGResourceDescriptor
from Script.FactoryGame import GetExtractableResource
from Game.FactoryGame.Buildable.Factory.MinerMk2.ParticleMap import ParticleMap
from Script.Engine import EqualEqual_ClassClass
from Script.Engine import SpawnEmitterAtLocation
from Script.Engine import SpawnEmitterAttached
from Game.FactoryGame.Buildable.Factory.MinerMK1.Audio.Resume_Miner_MK1_Dirt import Resume_Miner_MK1_Dirt
from Script.FactoryGame import TryStopProductionLoopEffects
from Script.Engine import Conv_SoftClassReferenceToClass
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import IsStartupComplete
from Script.FactoryGame import StartProductionLoopEffects
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import TryStartProductionLoopEffects
from Script.CoreUObject import Object
from Script.Engine import IsValid
from Script.FactoryGame import FGExtractableResourceInterface
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.Buildable.Factory.MinerMK1.Audio.Stop_Miner_MK1_Engine import Stop_Miner_MK1_Engine
from Script.Engine import ParticleSystem
from Script.CoreUObject import Vector
from Script.AkAudio import Default__AkGameplayStatics
from Script.AkAudio import PostAkEventAttached
from Game.FactoryGame.Buildable.Factory.MinerMK1.Audio.Resume_Miner_MK1_Engine import Resume_Miner_MK1_Engine
from Script.Engine import K2_DestroyComponent
from Game.FactoryGame.Buildable.Factory.MinerMK1.Audio.Stop_Miner_MK1_Dirt import Stop_Miner_MK1_Dirt
from Script.FactoryGame import LostSignificance
from Script.Engine import ParticleSystemComponent
from Game.FactoryGame.Buildable.Factory.MinerMK1.Build_MinerMk1 import ExecuteUbergraph_Build_MinerMk1
from Game.FactoryGame.Buildable.Factory.MinerMK1.Build_MinerMk1 import ExecuteUbergraph_Build_MinerMk1.K2Node_Event_didStartProducing
from Game.FactoryGame.Buildable.Factory.MinerMK1.Build_MinerMk1 import ExecuteUbergraph_Build_MinerMk1.K2Node_Event_didStopProducing
from Script.FactoryGame import GainedSignificance
from Script.AkAudio import AkComponent
from Script.FactoryGame import StopProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.MinerMk2.Particle.Ventilationsmoke import Ventilationsmoke

class Build_MinerMk1(FGBuildableResourceExtractor):
    mParticleMap: List[ParticleMap] = [{'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/Coal/Desc_Coal.Desc_Coal_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Coal_01.P_Mining_Coal_01'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/Stone/Desc_Stone.Desc_Stone_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Iron_01.P_Mining_Iron_01'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/OreIron/Desc_OreIron.Desc_OreIron_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Iron_01.P_Mining_Iron_01'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/OreBauxite/Desc_OreBauxite.Desc_OreBauxite_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Bauxite_01.P_Mining_Bauxite_01'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/OreCopper/Desc_OreCopper.Desc_OreCopper_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Copper_01.P_Mining_Copper_01'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/CrudeOil/Desc_LiquidOil.Desc_LiquidOil_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/MinerMk2/Particle/Mining.Mining'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/OreGold/Desc_OreGold.Desc_OreGold_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Gold_01.P_Mining_Gold_01'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/RawQuartz/Desc_RawQuartz.Desc_RawQuartz_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Quartz_01.P_Mining_Quartz_01'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/Sulfur/Desc_Sulfur.Desc_Sulfur_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Sulfur_01.P_Mining_Sulfur_01'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/OreUranium/Desc_OreUranium.Desc_OreUranium_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Uranium_01.P_Mining_Uranium_01'}}]
    mDrillingVfx01: Ptr[ParticleSystemComponent]
    mVentFfx01: Ptr[ParticleSystemComponent]
    mVentFfx02: Ptr[ParticleSystemComponent]
    mExtractStartupTime = 15
    mExtractStartupTimer = 10
    mExtractCycleTime = 1
    mItemsPerCycle = 1
    mAllowedResourceForms = ['EResourceForm::RF_SOLID']
    mMustPlaceOnResourceDisqualifier = NewObject[FGCDNeedsResourceNode]()
    mExtractorTypeName = Miner
    mPowerConsumption = 5
    mPowerConsumptionExponent = 1.600000023841858
    mPowerInfoClass = NewObject[FGPowerInfoComponent]()
    mMinimumProducingTime = 2
    mMinimumStoppedTime = 5
    mNumCyclesForProductivity = 20
    mCanChangePotential = True
    mCurrentPotential = 1
    mPendingPotential = 1
    mMinPotential = 0.009999999776482582
    mMaxPotential = 1
    mMaxPotentialIncreasePerCrystal = 0.5
    mFluidStackSizeDefault = EStackSize::SS_FLUID
    mFluidStackSizeMultiplier = 1
    mAddToSignificanceManager = True
    mSignificanceRange = 18000
    mHologramClass = NewObject[FGResourceExtractorHologram]()
    mDisplayName = NSLOCTEXT("", "A3AFD2EC45F35991F592229EB62527CF", "Miner Mk1")
    mDescription = NSLOCTEXT("", "91DECFAB424C19A9AC3C349C51F7BA4B", "Extracts solid resources from the resource node it is built on. \r\nThe normal extraction rate is 60 resources per minute. \r\nThe extraction rate is modified depending on resource node purity. Outputs all extracted resources onto connected conveyor belts.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_ResourceExtractorUI]()
    mIsUseable = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def GetExtractedResource(self):
        ReturnValue: TScriptInterface[FGExtractableResourceInterface] = self.GetExtractableResource()
        ReturnValue_0: TSubclassOf[FGResourceDescriptor] = GetInterfaceUObject(ReturnValue).GetResourceClass()
        Resource = ReturnValue_0
    

    def GetMiningParticles(self):
        ExecutionFlow.Push("L995")
        
        Resource = None
        self.GetExtractedResource(Ref[Resource])
        
        outputClasses = None
        Resource = None
        ReturnValue: int32 = outputClasses.append(Resource)
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 153
        ReturnValue_0: bool = Not_PreBool(Variable)
        
        ReturnValue_1: int32 = len(self.mParticleMap)
        ReturnValue_2: bool = Variable_0 <= ReturnValue_1
        ReturnValue_3: bool = ReturnValue_0 and ReturnValue_2
        if not ReturnValue_3:
            goto('L859')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L921")
        
        Item = None
        Item = self.mParticleMap[Variable_1]
        ParticleMapInstance: ParticleMap = Item
        
        outputClasses = None
        ReturnValue1: int32 = len(outputClasses)
        ReturnValue_4: bool = ReturnValue1 > 0
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        
        outputClasses = None
        Item1 = None
        Item1 = outputClasses[0]
        
        ParticleMapInstance.ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3 = None
        ReturnValue_5: TSubclassOf[Object] = Default__KismetSystemLibrary.Conv_SoftClassReferenceToClass(Ref[ParticleMapInstance.ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3])
        Descriptor: TSubclassOf[FGResourceDescriptor] = ClassCast[FGResourceDescriptor](ReturnValue_5)
        bSuccess: bool = Descriptor
        ReturnValue_6: bool = EqualEqual_ClassClass(Descriptor, Item1)
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        FirstParticle: Ptr[ParticleSystem] = ParticleMapInstance.ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD
        SecondParticle: Ptr[ParticleSystem] = ParticleMapInstance.ParticleSystem2_12_9CB1B6054B443457EF842EA10A375BF2
        FoundParticles: bool = True
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 859
        FirstParticle_0: Ptr[ParticleSystem] = FirstParticle
        SecondParticle_0: Ptr[ParticleSystem] = SecondParticle
        foundParticle = FoundParticles
        # End
        # Label 921
        ReturnValue_7: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_7
        goto('L153')
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_MinerMk1(27)
    

    def StartProductionLoopEffects(self):
        ExecuteUbergraph_Build_MinerMk1.K2Node_Event_didStartProducing = didStartProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_MinerMk1(141)
    

    def StopProductionLoopEffects(self):
        ExecuteUbergraph_Build_MinerMk1.K2Node_Event_didStopProducing = didStopProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_MinerMk1(898)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Build_MinerMk1(1232)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_Build_MinerMk1(1281)
    

    def ExecuteUbergraph_Build_MinerMk1(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.TryStopProductionLoopEffects(False)
        goto(ExecutionFlow.Pop())
        self.GainedSignificance()
        ReturnValue: bool = self.IsProducing()
        ReturnValue_0: bool = self.IsStartupComplete()
        ReturnValue_1: bool = ReturnValue_0 and ReturnValue
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        self.TryStartProductionLoopEffects(False)
        goto(ExecutionFlow.Pop())
        self.StartProductionLoopEffects(didStartProducing)
        ReturnValue1: bool = self.IsStartupComplete()
        if not ReturnValue1:
            goto('L342')
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Resume_Miner_MK1_Engine, self.MainMesh_skl, "AudioSocket_Drill_StartStop", True)
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Resume_Miner_MK1_Dirt, self.MainMesh_skl, "Root", True)
        # Label 342
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(self.mDrillingVfx01)
        if not ReturnValue_2:
            goto('L408')
        goto(ExecutionFlow.Pop())
        
        FirstParticle = None
        SecondParticle = None
        foundParticle = None
        # Label 408
        self.GetMiningParticles(Ref[FirstParticle], Ref[SecondParticle], Ref[foundParticle])
        ReturnValue_3: Vector = self.MainMesh_skl.GetSocketLocation("drillVfxSocket")
        ReturnValue_4: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, FirstParticle, ReturnValue_3, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        self.mDrillingVfx01 = ReturnValue_4
        ReturnValue_5: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(Ventilationsmoke, self.MainMesh_skl, "ventVfxSocket_01", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mVentFfx01 = ReturnValue_5
        ReturnValue1_0: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(Ventilationsmoke, self.MainMesh_skl, "ventVfxSocket_02", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mVentFfx02 = ReturnValue1_0
        goto(ExecutionFlow.Pop())
        self.StopProductionLoopEffects(didStopProducing)
        ExecutionFlow.Push("L1071")
        ReturnValue_6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_Miner_MK1_Engine, self.MainMesh_skl, "AudioSocket_Drill_StartStop", True)
        ReturnValue1_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_Miner_MK1_Dirt, self.MainMesh_skl, "Root", True)
        goto(ExecutionFlow.Pop())
        # Label 1071
        ReturnValue1_2: bool = Default__KismetSystemLibrary.IsValid(self.mDrillingVfx01)
        if not ReturnValue1_2:
           goto(ExecutionFlow.Pop())
        self.mDrillingVfx01.K2_DestroyComponent(self)
        self.mVentFfx01.K2_DestroyComponent(self)
        self.mVentFfx02.K2_DestroyComponent(self)
        goto(ExecutionFlow.Pop())
        self.LostSignificance()
        ReturnValue1_3: bool = self.IsProducing()
        if not ReturnValue1_3:
           goto(ExecutionFlow.Pop())
        goto('L15')
        self.ReceiveDestroyed()
        ReturnValue2_0: bool = Default__KismetSystemLibrary.IsValid(self.mDrillingVfx01)
        if not ReturnValue2_0:
           goto(ExecutionFlow.Pop())
        self.mDrillingVfx01.K2_DestroyComponent(self)
        goto(ExecutionFlow.Pop())
    
