
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Vehicle.UseState_WorkBench import UseState_WorkBench
from Script.FactoryGame import UpdateUseState
from Script.Engine import EqualEqual_ClassClass
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import GetWorkBenchUser
from Script.Engine import EqualEqual_ObjectObject
from Script.Engine import IsValid
from Script.FactoryGame import FGBuildable
from Script.FactoryGame import GetLookAtDecription
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.Engine import Not_PreBool

class Build_Workshop(FGBuildable):
    mOccupiedText: FText = NSLOCTEXT("", "CBAF5A254ACBD8D5D4055EAC2D499367", "Equipment Workshop is occupied!")
    mHologramClass = NewObject[FGBuildableHologram]()
    mDisplayName = NSLOCTEXT("", "BE3C0E5D44852E9A26F679A7602CA8EC", "Equipment Workshop")
    mDescription = NSLOCTEXT("", "20A5A0EA49D968BB3878B7B7CA7388D2", "Used to manually craft equipment.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=False, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_ManualManufacturing_Container]()
    mIsUseable = True
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
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
        ReturnValue1: Ptr[FGCharacterPlayer] = self.WorkshopComponent.GetWorkBenchUser()
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        if not ReturnValue:
            goto('L277')
        ReturnValue_0: Ptr[FGCharacterPlayer] = self.WorkshopComponent.GetWorkBenchUser()
        ReturnValue_1: bool = EqualEqual_ObjectObject(byCharacter, ReturnValue_0)
        ReturnValue_2: bool = Not_PreBool(ReturnValue_1)
        if not ReturnValue_2:
            goto('L277')
        
        useState = None
        Default__FGBlueprintFunctionLibrary.UpdateUseState(None, Ref[useState])
        # End
        
        useState = None
        # Label 277
        Default__FGBlueprintFunctionLibrary.UpdateUseState(UseState_WorkBench, Ref[useState])
    
