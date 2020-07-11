
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Vehicle.UseState_WorkBench import UseState_WorkBench
from Script.Engine import EqualEqual_ClassClass
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Script.FactoryGame import SetCrosshairState
from Script.FactoryGame import FGBuildable
from Script.FactoryGame import ECrosshairState
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

class Build_WorkBench(FGBuildable):
    mOccupiedText: FText = NSLOCTEXT("", "D974D9714933D3A8F63459B2E3CA5106", "Craftbench is occupied!")
    mHologramClass = NewObject[FGBuildableHologram]()
    mDisplayName = NSLOCTEXT("", "909BAFD0411132D0C914DCA1317B245F", "Craft Bench")
    mDescription = NSLOCTEXT("", "8D86213447772D233FC197BE8EA51736", "Allows you to manually craft a large range of different parts. \r\nThese parts can then be used in construction of different factory buildings, vehicles and equipment.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=False, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mForceNetUpdateOnRegisterPlayer = True
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_ManualManufacturing_Container]()
    mIsUseable = True
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def CanDismantle(self):
        ReturnValue: Ptr[FGCharacterPlayer] = self.BP_WorkBenchComponent.GetWorkBenchUser()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        ReturnValue_2: bool = ReturnValue_1
    

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
        ReturnValue: Ptr[FGCharacterPlayer] = self.BP_WorkBenchComponent.GetWorkBenchUser()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L674')
        ReturnValue1: Ptr[FGCharacterPlayer] = self.BP_WorkBenchComponent.GetWorkBenchUser()
        ReturnValue_1: bool = EqualEqual_ObjectObject(ReturnValue1, byCharacter)
        ReturnValue_2: bool = Not_PreBool(ReturnValue_1)
        if not ReturnValue_2:
            goto('L674')
        
        useState = None
        Default__FGBlueprintFunctionLibrary.UpdateUseState(None, Ref[useState])
        canUse: bool = False
        # Label 283
        ReturnValue_3: Ptr[Controller] = byCharacter.GetController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue_3)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L740')
        ReturnValue_4: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_4)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
            goto('L669')
        Variable: uint8 = 0
        Variable1: uint8 = 5
        Variable_0: bool = canUse
        
        switch = {
            False: Variable,
            True: Variable1
        }
        AsFGHUD.SetCrosshairState(switch.get(Variable_0, None))
        # Label 669
        # End
        
        useState = None
        # Label 674
        Default__FGBlueprintFunctionLibrary.UpdateUseState(UseState_WorkBench, Ref[useState])
        canUse = True
        goto('L283')
    
