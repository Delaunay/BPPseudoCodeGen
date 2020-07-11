
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.MinerMk2.Audio.Resume_Miner_MK2_Engine import Resume_Miner_MK2_Engine
from Script.Engine import ReceiveDestroyed
from Script.FactoryGame import FGBuildableResourceExtractor
from Script.FactoryGame import FGResourceDescriptor
from Game.FactoryGame.Buildable.Factory.MinerMk2.ParticleMap import ParticleMap
from Script.Engine import EqualEqual_ClassClass
from Script.FactoryGame import GetExtractableResource
from Script.Engine import SpawnEmitterAtLocation
from Script.Engine import SpawnEmitterAttached
from Script.FactoryGame import TryStopProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.MinerMk2.Build_MinerMk2 import ExecuteUbergraph_Build_MinerMk2.K2Node_Event_didStartProducing
from Script.Engine import Conv_SoftClassReferenceToClass
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import IsStartupComplete
from Script.FactoryGame import StartProductionLoopEffects
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Buildable.Factory.MinerMk2.Audio.Play_Miner_MK2_Startup_Dirt import Play_Miner_MK2_Startup_Dirt
from Script.FactoryGame import TryStartProductionLoopEffects
from Script.CoreUObject import Object
from Script.Engine import IsValid
from Script.FactoryGame import FGExtractableResourceInterface
from Script.Engine import Default__GameplayStatics
from Script.Engine import ParticleSystem
from Script.FactoryGame import GetIsSignificant
from Script.CoreUObject import Vector
from Game.FactoryGame.Buildable.Factory.MinerMk2.Audio.Stop_Miner_MK2_Engine import Stop_Miner_MK2_Engine
from Script.AkAudio import Default__AkGameplayStatics
from Script.AkAudio import PostAkEventAttached
from Script.Engine import K2_DestroyComponent
from Game.FactoryGame.Buildable.Factory.MinerMk2.Build_MinerMk2 import ExecuteUbergraph_Build_MinerMk2.K2Node_Event_didStopProducing
from Game.FactoryGame.Buildable.Factory.MinerMk2.Build_MinerMk2 import ExecuteUbergraph_Build_MinerMk2.K2Node_Event_newIsProducing
from Game.FactoryGame.Buildable.Factory.MinerMk2.Build_MinerMk2 import ExecuteUbergraph_Build_MinerMk2
from Script.Engine import ParticleSystemComponent
from Script.FactoryGame import LostSignificance
from Script.FactoryGame import OnIsProducingChanged
from Game.FactoryGame.Buildable.Factory.MinerMk2.Audio.Stop_Miner_MK2_Dirt import Stop_Miner_MK2_Dirt
from Script.AkAudio import AkComponent
from Script.FactoryGame import GainedSignificance
from Script.FactoryGame import StopProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.MinerMk2.Audio.Resume_Miner_MK2_Dirt import Resume_Miner_MK2_Dirt
from Game.FactoryGame.Buildable.Factory.MinerMk2.Particle.Ventilationsmoke import Ventilationsmoke

class Build_MinerMk2(FGBuildableResourceExtractor):
    mParticleMap: List[ParticleMap] = [{'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/Coal/Desc_Coal.Desc_Coal_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Coal_01.P_Mining_Coal_01'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/Stone/Desc_Stone.Desc_Stone_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Iron_01.P_Mining_Iron_01'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/OreIron/Desc_OreIron.Desc_OreIron_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Iron_01.P_Mining_Iron_01'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/OreBauxite/Desc_OreBauxite.Desc_OreBauxite_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Bauxite_01.P_Mining_Bauxite_01'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/OreCopper/Desc_OreCopper.Desc_OreCopper_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Copper_01.P_Mining_Copper_01'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/CrudeOil/Desc_LiquidOil.Desc_LiquidOil_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/MinerMk2/Particle/Mining.Mining'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/OreGold/Desc_OreGold.Desc_OreGold_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Gold_01.P_Mining_Gold_01'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/RawQuartz/Desc_RawQuartz.Desc_RawQuartz_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Quartz_01.P_Mining_Quartz_01'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/Sulfur/Desc_Sulfur.Desc_Sulfur_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Sulfur_01.P_Mining_Sulfur_01'}}, {'ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3': '/Game/FactoryGame/Resource/RawResources/OreUranium/Desc_OreUranium.Desc_OreUranium_C', 'ParticleSystem1_9_F0CF81514E1E1C5007AC99B0C59C63CD': {'$AssetPath': '/Game/FactoryGame/VFX/Factory/Miner/P_Mining_Uranium_01.P_Mining_Uranium_01'}}]
    mVentVfx01: Ptr[ParticleSystemComponent]
    mVentVfx02: Ptr[ParticleSystemComponent]
    mDrillingVfx01: Ptr[ParticleSystemComponent]
    mCanPlayAfterStartUpStopped: bool
    mIsPlayingDirtSFX: Ptr[AkComponent]
    mExtractStartupTime = 15
    mExtractStartupTimer = 10
    mExtractCycleTime = 0.5
    mItemsPerCycle = 1
    mAllowedResourceForms = ['EResourceForm::RF_SOLID']
    mMustPlaceOnResourceDisqualifier = NewObject[FGCDNeedsResourceNode]()
    mExtractorTypeName = Miner
    mPowerConsumption = 12
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
    mDisplayName = NSLOCTEXT("", "9FFDB8E242D774A194E8318F78719EAD", "Miner Mk.2")
    mDescription = NSLOCTEXT("", "4C6C2C674EB7BC00A768248C760ABA61", "Extracts solid resources from the resource node it is built on. \r\nThe normal extraction rate is 120 resources per minute. \r\nThe extraction rate is modified depending on resource node purity. Outputs all extracted resources onto connected conveyor belts.")
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
        
        ReturnValue1: int32 = len(self.mParticleMap)
        ReturnValue_1: bool = Variable_0 <= ReturnValue1
        ReturnValue_2: bool = ReturnValue_0 and ReturnValue_1
        if not ReturnValue_2:
            goto('L859')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L921")
        
        Item1 = None
        Item1 = self.mParticleMap[Variable_1]
        ParticleMapInstance: ParticleMap = Item1
        
        outputClasses = None
        ReturnValue_3: int32 = len(outputClasses)
        ReturnValue_4: bool = ReturnValue_3 > 0
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        
        outputClasses = None
        Item = None
        Item = outputClasses[0]
        
        ParticleMapInstance.ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3 = None
        ReturnValue_5: TSubclassOf[Object] = Default__KismetSystemLibrary.Conv_SoftClassReferenceToClass(Ref[ParticleMapInstance.ResourceNode_16_2100B5C34EE8DF7958D78A974512F3C3])
        Descriptor: TSubclassOf[FGResourceDescriptor] = ClassCast[FGResourceDescriptor](ReturnValue_5)
        bSuccess: bool = Descriptor
        ReturnValue_6: bool = EqualEqual_ClassClass(Descriptor, Item)
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
    

    def GetExtractedResource(self):
        ReturnValue: TScriptInterface[FGExtractableResourceInterface] = self.GetExtractableResource()
        ReturnValue_0: TSubclassOf[FGResourceDescriptor] = GetInterfaceUObject(ReturnValue).GetResourceClass()
        Resource = ReturnValue_0
    

    def SetDisplayText(self, newText: FText):
        pass
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_MinerMk2(2030)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Build_MinerMk2(1918)
    

    def StartProductionLoopEffects(self):
        ExecuteUbergraph_Build_MinerMk2.K2Node_Event_didStartProducing = didStartProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_MinerMk2(1270)
    

    def StopProductionLoopEffects(self):
        ExecuteUbergraph_Build_MinerMk2.K2Node_Event_didStopProducing = didStopProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_MinerMk2(936)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_Build_MinerMk2(1294)
    

    def OnIsProducingChanged(self):
        ExecuteUbergraph_Build_MinerMk2.K2Node_Event_newIsProducing = newIsProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_MinerMk2(1810)
    

    def ExecuteUbergraph_Build_MinerMk2(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: bool = self.IsProducing()
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        ReturnValue4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_Miner_MK2_Startup_Dirt, self.MainMesh, "Root", True)
        # Label 123
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mDrillingVfx01)
        if not ReturnValue_0:
            goto('L189')
        goto(ExecutionFlow.Pop())
        
        FirstParticle = None
        SecondParticle = None
        foundParticle = None
        # Label 189
        self.GetMiningParticles(Ref[FirstParticle], Ref[SecondParticle], Ref[foundParticle])
        ReturnValue_1: Vector = self.MainMesh.GetSocketLocation("drillVfxSocket")
        ReturnValue_2: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, FirstParticle, ReturnValue_1, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        self.mDrillingVfx01 = ReturnValue_2
        ReturnValue_3: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(Ventilationsmoke, self.MainMesh, "ventVfxSocket_01", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mVentVfx01 = ReturnValue_3
        ReturnValue1: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(Ventilationsmoke, self.MainMesh, "ventVfxSocket_02", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mVentVfx02 = ReturnValue1
        goto(ExecutionFlow.Pop())
        # Label 679
        ReturnValue_4: bool = self.IsStartupComplete()
        if not ReturnValue_4:
            goto('L866')
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Resume_Miner_MK2_Engine, self.MainMesh, "AudioSocket_Drill_StartStop", True)
        ReturnValue_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Resume_Miner_MK2_Dirt, self.MainMesh, "Root", True)
        goto('L123')
        # Label 866
        ReturnValue3_0: bool = Default__KismetSystemLibrary.IsValid(self.mIsPlayingDirtSFX)
        if not ReturnValue3_0:
            goto('L15')
        goto('L123')
        self.StopProductionLoopEffects(didStopProducing)
        ExecutionFlow.Push("L1109")
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_Miner_MK2_Engine, self.MainMesh, "AudioSocket_Drill_StartStop", True)
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_Miner_MK2_Dirt, self.MainMesh, "Root", True)
        goto(ExecutionFlow.Pop())
        # Label 1109
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValid(self.mDrillingVfx01)
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        self.mDrillingVfx01.K2_DestroyComponent(self)
        self.mVentVfx01.K2_DestroyComponent(self)
        self.mVentVfx02.K2_DestroyComponent(self)
        goto(ExecutionFlow.Pop())
        self.StartProductionLoopEffects(didStartProducing)
        goto('L679')
        self.ReceiveDestroyed()
        ReturnValue2_0: bool = Default__KismetSystemLibrary.IsValid(self.mDrillingVfx01)
        if not ReturnValue2_0:
           goto(ExecutionFlow.Pop())
        self.mDrillingVfx01.K2_DestroyComponent(self)
        goto(ExecutionFlow.Pop())
        # Label 1399
        self.TryStartProductionLoopEffects(False)
        goto(ExecutionFlow.Pop())
        # Label 1411
        self.TryStopProductionLoopEffects(False)
        goto(ExecutionFlow.Pop())
        # Label 1423
        ReturnValue1_2: bool = self.IsStartupComplete()
        if not ReturnValue1_2:
            goto('L1458')
        goto(ExecutionFlow.Pop())
        # Label 1458
        if not newIsProducing:
            goto('L1650')
        if not self.mCanPlayAfterStartUpStopped:
           goto(ExecutionFlow.Pop())
        ReturnValue7: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Resume_Miner_MK2_Engine, self.MainMesh, "AudioSocket_Drill_StartStop", True)
        ReturnValue5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Resume_Miner_MK2_Dirt, self.MainMesh, "Root", True)
        self.mIsPlayingDirtSFX = ReturnValue5
        goto(ExecutionFlow.Pop())
        # Label 1650
        ReturnValue8: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_Miner_MK2_Engine, self.MainMesh, "AudioSocket_Drill_StartStop", True)
        ReturnValue6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_Miner_MK2_Dirt, self.MainMesh, "Root", True)
        self.mCanPlayAfterStartUpStopped = True
        goto(ExecutionFlow.Pop())
        self.OnIsProducingChanged(newIsProducing)
        ReturnValue_6: bool = self.GetIsSignificant()
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        goto('L1423')
        # Label 1864
        ReturnValue1_3: bool = self.IsProducing()
        if not ReturnValue1_3:
           goto(ExecutionFlow.Pop())
        goto('L1411')
        # Label 1903
        self.LostSignificance()
        goto('L1864')
        goto('L1903')
        # Label 1923
        self.GainedSignificance()
        ReturnValue2_1: bool = self.IsStartupComplete()
        ReturnValue2_2: bool = self.IsProducing()
        ReturnValue_7: bool = ReturnValue2_2 and ReturnValue2_1
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        goto('L1399')
        goto('L1923')
    
