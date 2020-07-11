
from codegen.ue4_stub import *

from Script.Engine import ReceiveDestroyed
from Script.Engine import Delay
from Script.Engine import SetVisibility
from Script.FactoryGame import CreateAndAddNewRepresentation
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import K2_SetTimerDelegate
from Script.FactoryGame import UpdateGeneratorVisibility
from Script.Engine import GreaterEqual_IntInt
from Script.FactoryGame import GetTradingPostLevel
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_Icon_hub import MapCompass_Icon_hub
from Script.Engine import ReceiveBeginPlay
from Script.Engine import LatentActionInfo
from Script.Engine import HasAuthority
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import AreChildBuildingsLoaded
from Script.FactoryGame import Get
from Game.FactoryGame.Buildable.Factory.TradingPost.Build_TradingPost import ExecuteUbergraph_Build_TradingPost.K2Node_Event_level
from Game.FactoryGame.Buildable.Factory.TradingPost.Build_TradingPost import ExecuteUbergraph_Build_TradingPost.K2Node_ComponentBoundEvent_OverlappedComponent
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Script.FactoryGame import FGTutorialIntroManager
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.FactoryGame import Default__FGActorRepresentationManager
from Game.FactoryGame.Buildable.Factory.TradingPost.Build_TradingPost import ExecuteUbergraph_Build_TradingPost.K2Node_ComponentBoundEvent_OtherActor
from Script.FactoryGame import ReapplyColorSlot
from Game.FactoryGame.Buildable.Factory.TradingPost.Build_TradingPost import ExecuteUbergraph_Build_TradingPost.K2Node_ComponentBoundEvent_SweepResult
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGGameState
from Script.Engine import FlushNetDormancy
from Game.FactoryGame.Buildable.Factory.TradingPost.Anim_Tradingpost import Anim_Tradingpost
from Script.CoreUObject import Vector
from Game.FactoryGame.Buildable.Factory.TradingPost.Build_TradingPost import ExecuteUbergraph_Build_TradingPost.K2Node_Event_newColor
from Script.FactoryGame import FGActorRepresentationManager
from Script.Engine import MaterialInterface
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import FlagReevaluateMaterialOnColored
from Game.FactoryGame.Buildable.Factory.TradingPost.Build_TradingPost import ExecuteUbergraph_Build_TradingPost.K2Node_ComponentBoundEvent_OtherBodyIndex
from Script.FactoryGame import FGBuildableTradingPost
from Game.FactoryGame.Buildable.Factory.TradingPost.Build_TradingPost import ExecuteUbergraph_Build_TradingPost.K2Node_ComponentBoundEvent_OtherComp
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Buildable.Factory.TradingPost.Mesh.Tradingpost_skl import Tradingpost_skl
from Script.Engine import K2_GetActorLocation
from Script.Engine import GetMaterial
from Script.Engine import GetGameState
from Script.FactoryGame import RemoveRepresentationOfActor
from Script.FactoryGame import UpdateStorageVisibility
from Script.Engine import Min
from Game.FactoryGame.Buildable.Factory.TradingPost.Build_TradingPost import ExecuteUbergraph_Build_TradingPost.K2Node_ComponentBoundEvent_bFromSweep
from Game.FactoryGame.Buildable.Factory.TradingPost.Build_TradingPost import ExecuteUbergraph_Build_TradingPost
from Game.FactoryGame.Buildable.Factory.TradingPost.Build_TradingPost import ExecuteUbergraph_Build_TradingPost.K2Node_Event_suppressBuildEffects
from Script.FactoryGame import Default__FGTutorialIntroManager
from Script.Engine import Concat_StrStr
from Script.Engine import PrintString
from Script.Engine import StaticMesh
from Script.CoreUObject import LinearColor

class Build_TradingPost(FGBuildableTradingPost):
    mWorkBenchOccupied: FText = NSLOCTEXT("", "6555ACFB425387FB996FDC8C02D8106A", "Craft Bench occupied")
    mWorkBenchFree: FText = NSLOCTEXT("", "7BD46F4D473DA7FCAA83B7838BF59943", "Use Craft Bench")
    meshes: List[Ptr[StaticMesh]] = [{'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/Mesh/Tradingpost_Stage_1.Tradingpost_Stage_1'}, {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/Mesh/Tradingpost_Stage_2.Tradingpost_Stage_2'}, {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/Mesh/Tradingpost_Stage_3.Tradingpost_Stage_3'}, {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/Mesh/Tradingpost_Stage_4.Tradingpost_Stage_4'}, {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/Mesh/Tradingpost_Stage_5.Tradingpost_Stage_5'}, {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/Mesh/Tradingpost_Stage_6.Tradingpost_Stage_6'}]
    mShipUpgradeLevel: int32 = 6
    mStorageText: FText = NSLOCTEXT("", "8296CA87498ACBD949532BAE8DDBC6A6", "Open Storage")
    mMamFreeText: FText = NSLOCTEXT("", "38E3965D46DDE94D017333A4F36B1266", "Use M.A.M.")
    mMamOccupiedText: FText = NSLOCTEXT("", "A3CAE9674C139C2A8DF07CB40D113B32", "M.A.M. is occupied")
    mLastTradingPostUser: Ptr[FGCharacterPlayer]
    mMapText: FText = NSLOCTEXT("", "82C5B03E49463BF27715CCBD386BDE96", "The HUB")
    mDefaultGeneratorRecipe = NewObject[Recipe_GeneratorIntegratedBiomass]()
    mDefaultStorageRecipe = NewObject[Recipe_StorageIntegrated]()
    mDefaultHubTerminalRecipe = NewObject[Recipe_HubTerminal]()
    mDefaultWorkBenchRecipe = NewObject[Recipe_WorkBenchIntegrated]()
    mGeneratorVisibilityLevels = [2, 5]
    mStorageInventorySize = 10
    mStorageVisibilityLevel = 1
    mSpawningGroundZOffset = 5
    mGroundSearchZDistance = 250
    mGenerator1Location = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='Generator1Location', RelativeLocation={'X': 190, 'Y': -1098.483642578125, 'Z': 90})
    mGenerator2Location = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='Generator2Location', RelativeLocation={'X': -190, 'Y': -1098.482421875, 'Z': 90})
    mStorageLocation = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='StorageLocation', RelativeLocation={'X': -340, 'Y': 60, 'Z': 70})
    mHubTerminalLocation = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='HubTerminalLocation', RelativeLocation={'X': 0, 'Y': 0, 'Z': -66.59500122070312})
    mWorkBenchLocation = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='WorkBenchLocation', RelativeLocation={'X': 10, 'Y': 540, 'Z': 40})
    mPowerConsumptionExponent = 1.600000023841858
    mPowerInfoClass = NewObject[FGPowerInfoComponent]()
    mMinimumProducingTime = 2
    mMinimumStoppedTime = 5
    mNumCyclesForProductivity = 20
    mCurrentPotential = 1
    mPendingPotential = 1
    mMinPotential = 0.009999999776482582
    mMaxPotential = 1
    mMaxPotentialIncreasePerCrystal = 0.5
    mFluidStackSizeDefault = EStackSize::SS_FLUID
    mFluidStackSizeMultiplier = 1
    mAddToSignificanceManager = True
    mSignificanceRange = 18000
    mHologramClass = NewObject[FGTradingPostHologram]()
    mDisplayName = NSLOCTEXT("", "94FECF5B45FE9DB38A19248BBD383958", "The HUB")
    mDescription = NSLOCTEXT("", "5C2BA8414CB9AD297AD01697325DE3E8", "The heart of your factory. This is where you complete FICSIT milestones to unlock additional blueprints of buildings, vehicles, parts, equipment etc.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/TradingPost/BP_MaterialEffect_Build_Hub.BP_MaterialEffect_Build_Hub_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_TradingPost]()
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def GetActorCompassViewDistance(self):
        ReturnValue = 4
    

    def SetActorCompassViewDistance(self):
        ReturnValue = 0
    

    def SetActorRepresentationText(self):
        self.FlushNetDormancy()
        self.mMapText = newText
        ReturnValue = self.mMapText
    

    def UpdateRepresentation(self):
        ReturnValue = False
    

    def GetActorRepresentationColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Graphics
    

    def GetActorRepresentationText(self):
        ReturnValue = self.mMapText
    

    def GetActorRepresentationTexture(self):
        ReturnValue = MapCompass_Icon_hub
    

    def GetActorRepresentationType(self):
        ReturnValue = 3
    

    def GetActorShouldShowInCompass(self):
        ReturnValue = True
    

    def GetActorFogOfWarRevealRadius(self):
        ReturnValue = 80000
    

    def GetActorFogOfWarRevealType(self):
        ReturnValue = 1
    

    def RemoveAsRepresentation(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L144')
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = ReturnValue_0.RemoveRepresentationOfActor(self)
        ReturnValue_2: bool = ReturnValue_1
        goto('L155')
        # Label 144
        ReturnValue_2 = False
    

    def GetRealActorRotation(self):
        ReturnValue = Rotator::FromPitchYawRoll(0, 0, 0)
    

    def GetRealActorLocation(self):
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue_0: Vector = ReturnValue
    

    def GetActorShouldShowOnMap(self):
        ReturnValue = True
    

    def AddAsRepresentation(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L145')
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = ReturnValue_0.CreateAndAddNewRepresentation(self, False)
        ReturnValue_2: bool = ReturnValue_1
        goto('L156')
        # Label 145
        ReturnValue_2 = False
    

    def IsActorStatic(self):
        ReturnValue = True
    

    def UpdateTradingPostVisibility(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue)
        # Label 79
        bSuccess: bool = State
        if not bSuccess:
            goto('L563')
        ReturnValue_0: Ptr[FGTutorialIntroManager] = Default__FGTutorialIntroManager.Get(State)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L311')
        ReturnValue_2: bool = self.AreChildBuildingsLoaded()
        if not ReturnValue_2:
            goto('L475')
        self.UpdateGeneratorVisibility()
        self.UpdateStorageVisibility()
        self.UpdateMainMesh()
        # End
        # Label 311
        ReturnValue_3: FString = Default__KismetStringLibrary.Concat_StrStr("could not find intromanager", "")
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_3, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        # Label 475
        OutputDelegate.BindUFunction(self, UpdateTradingPostVisibility)
        ReturnValue_4: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.10000000149011612, False)
    

    def UpdateMainMesh(self):
        ExecutionFlow.Push("L1421")
        self.FlagReevaluateMaterialOnColored()
        # Label 15
        ReturnValue1: int32 = self.GetTradingPostLevel()
        
        ReturnValue: int32 = len(self.meshes)
        ReturnValue_0: int32 = ReturnValue - 1
        # Label 144
        ReturnValue_1: int32 = Min(ReturnValue1, ReturnValue_0)
        
        Item = None
        Item = self.meshes[ReturnValue_1]
        ReturnValue_2: bool = self.MainMesh.SetStaticMesh(Item)
        ReturnValue_3: int32 = self.GetTradingPostLevel()
        ReturnValue_4: bool = GreaterEqual_IntInt(ReturnValue_3, 4)
        self.SM_KorolevPoster.SetVisibility(ReturnValue_4, False)
        if not True:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 456
        ReturnValue_5: List[Ptr[MaterialInterface]] = self.MainMesh.GetMaterials()
        
        ReturnValue1_0: int32 = len(ReturnValue_5)
        ReturnValue_6: bool = Variable <= ReturnValue1_0
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L1347")
        ReturnValue1 = self.GetTradingPostLevel()
        
        ReturnValue = len(self.meshes)
        ReturnValue_0 = ReturnValue - 1
        ReturnValue_1 = Min(ReturnValue1, ReturnValue_0)
        
        Item = None
        Item = self.meshes[ReturnValue_1]
        ReturnValue_7: Ptr[MaterialInterface] = Item.GetMaterial(Variable_0)
        self.MainMesh.SetMaterial(Variable_0, ReturnValue_7)
        ReturnValue_8: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue_8)
        bSuccess: bool = State
        ReturnValue_9: Ptr[FGTutorialIntroManager] = Default__FGTutorialIntroManager.Get(State)
        ReturnValue2: int32 = ReturnValue_9.GetTradingPostLevel()
        ReturnValue1_1: bool = GreaterEqual_IntInt(ReturnValue2, self.mShipUpgradeLevel)
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        self.MainMesh_skl.K2_SetAnimInstanceClass(Anim_Tradingpost)
        self.MainMesh_skl.SetSkeletalMesh(Tradingpost_skl, False)
        self.ReapplyColorSlot()
        goto(ExecutionFlow.Pop())
        # Label 1347
        ReturnValue_10: int32 = Variable + 1
        Variable = ReturnValue_10
        goto('L456')
    

    def BndEvt__WhatIsThis?_K2Node_ComponentBoundEvent_0_ComponentBeginOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32, bFromSweep: bool, SweepResult: Const[Ref[HitResult]]):
        ExecuteUbergraph_Build_TradingPost.K2Node_ComponentBoundEvent_OverlappedComponent = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_TradingPost.K2Node_ComponentBoundEvent_OtherActor = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_TradingPost.K2Node_ComponentBoundEvent_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_TradingPost.K2Node_ComponentBoundEvent_OtherBodyIndex = OtherBodyIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_TradingPost.K2Node_ComponentBoundEvent_bFromSweep = bFromSweep #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_TradingPost.K2Node_ComponentBoundEvent_SweepResult = SweepResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_TradingPost(242)
    

    def OnTradingPostUpgraded(self):
        ExecuteUbergraph_Build_TradingPost.K2Node_Event_level = Level #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_TradingPost.K2Node_Event_suppressBuildEffects = suppressBuildEffects #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_TradingPost(186)
    

    def SetActorRepresentationColor(self):
        ExecuteUbergraph_Build_TradingPost.K2Node_Event_newColor = NewColor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_TradingPost(191)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Build_TradingPost(192)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_Build_TradingPost(237)
    

    def ExecuteUbergraph_Build_TradingPost(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.ReceiveBeginPlay()
        ReturnValue: bool = self.AddAsRepresentation()
        self.UpdateTradingPostVisibility()
        goto(ExecutionFlow.Pop())
        if not suppressBuildEffects:
            goto('L79')
        goto(ExecutionFlow.Pop())
        # Label 79
        self.PlayBuildEffects(None)
        goto(ExecutionFlow.Pop())
        # Label 95
        self.UpdateTradingPostVisibility()
        Default__KismetSystemLibrary.Delay(self, 0.019999999552965164, LatentActionInfo(Linkage = 64, UUID = 1877753389, ExecutionFunction = "ExecuteUbergraph_Build_TradingPost", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L95')
        goto(ExecutionFlow.Pop())
        goto('L15')
        # Label 197
        ReturnValue_0: bool = self.RemoveAsRepresentation()
        goto(ExecutionFlow.Pop())
        # Label 222
        self.ReceiveDestroyed()
        goto('L197')
        goto('L222')
        goto(ExecutionFlow.Pop())
    
