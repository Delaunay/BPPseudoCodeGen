
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Vehicle.UseState_WorkBench import UseState_WorkBench
from Script.Engine import EqualEqual_ClassClass
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Script.FactoryGame import SetCrosshairState
from Script.FactoryGame import FGBuildable
from Script.Engine import ActorHasTag
from Script.Engine import Not_PreBool
from Script.Engine import HUD
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import GetController
from Script.Engine import IsValid
from Script.Engine import GetHUD
from Script.FactoryGame import GetWorkBenchUser
from Script.Engine import EqualEqual_ObjectObject
from Script.FactoryGame import GetLookAtDecription
from Script.FactoryGame import FGHUD
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.FactoryGame import UpdateUseState

class Build_WorkBenchIntegrated(FGBuildable):
    mOccupiedText: FText = NSLOCTEXT("", "FDE7AC174F1FAC88566E1C83AF7B391A", "Craftbench is occupied!")
    mHologramClass = NewObject[FGBuildableHologram]()
    mDisplayName = NSLOCTEXT("", "DC88421D451F63FB95AA80861E61AEFC", "Craft Bench")
    mDescription = NSLOCTEXT("", "F94BADFE4C6835FB3D72DBBF3E590C58", "The Craft Bench allows you to manually produce parts to use in constructing buildings.")
    MaxRenderDistance = -1
    mHighlightVector = Namespace(X=0, Y=-110, Z=140)
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=False, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/TradingPost/BP_MaterialEffect_Build_Hub.BP_MaterialEffect_Build_Hub_C', SubPathString='')
    mForceNetUpdateOnRegisterPlayer = True
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mHighlightParticleSystemTemplate = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing')
    mShouldShowHighlight = True
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_ManualManufacturing_Container]()
    mIsUseable = True
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def CanBeSampled(self):
        ReturnValue = False
    

    def CanDismantle(self):
        ReturnValue: bool = self.ActorHasTag("Integrated")
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        ReturnValue_1: bool = ReturnValue_0
    

    def GetLookAtDecription(self):
        ReturnValue: bool = EqualEqual_ClassClass(State.State, UseState_WorkBench)
        if not ReturnValue:
            goto('L161')
        
        byCharacter.mCachedUseState = None
        ReturnValue_0: FText = self.GetLookAtDecription(byCharacter, Ref[byCharacter.mCachedUseState])
        ReturnValue_1: FText = ReturnValue_0
        goto('L188')
        # Label 161
        ReturnValue_1 = self.mOccupiedText
    

    def IsUseable(self):
        ReturnValue = True
    

    def UpdateUseState(self):
        ReturnValue: Ptr[Controller] = byCharacter.GetController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L637')
        ReturnValue_0: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_0)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
            goto('L637')
        ReturnValue_1: Ptr[FGCharacterPlayer] = self.BP_WorkBenchComponent.GetWorkBenchUser()
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_1)
        if not ReturnValue_2:
            goto('L553')
        ReturnValue1: Ptr[FGCharacterPlayer] = self.BP_WorkBenchComponent.GetWorkBenchUser()
        ReturnValue_3: bool = EqualEqual_ObjectObject(ReturnValue1, byCharacter)
        ReturnValue_4: bool = Not_PreBool(ReturnValue_3)
        if not ReturnValue_4:
            goto('L553')
        
        useState = None
        Default__FGBlueprintFunctionLibrary.UpdateUseState(None, Ref[useState])
        AsFGHUD.SetCrosshairState(0)
        # End
        
        useState = None
        # Label 553
        Default__FGBlueprintFunctionLibrary.UpdateUseState(UseState_WorkBench, Ref[useState])
        AsFGHUD.SetCrosshairState(5)
    
