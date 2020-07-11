
from codegen.ue4_stub import *

from Script.Engine import CurveFloat
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Vehicle.UseState_WorkBench import UseState_WorkBench
from Script.FactoryGame import UpdateUseState
from Script.Engine import EqualEqual_ClassClass
from Script.FactoryGame import SetResearchMeshCurveScale
from Script.FactoryGame import GetMachineUser
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import EqualEqual_ObjectObject
from Script.FactoryGame import SetResearchMeshComponent
from Script.Engine import IsValid
from Script.FactoryGame import FGBuildable
from Script.FactoryGame import GetLookAtDecription
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.Engine import Not_PreBool

class Build_Mam(FGBuildable):
    mOccupiedText: FText = NSLOCTEXT("", "D8FD9559496EEF55DE77D1A2A16BFC55", "The Molecular Analysis Machine is occupied!")
    mResearchMeshScale: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/Mam/C_MamResearchMeshScale.C_MamResearchMeshScale')
    mHologramClass = NewObject[FGBuildableHologram]()
    mDisplayName = NSLOCTEXT("", "42111D1146F0DCFA899A6292AF4C2AA4", "M.A.M.")
    mDescription = NSLOCTEXT("", "545F4AC14D8E3A6C5A080BABF0D32C44", "The Molecular Analysis Machine is used to analyse new and exotic materials found on alien planets.\r\nR&D will assist Pioneers through the M.A.M to turn any valuable data into usable research options and new technologies.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=False, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[BPW_MAM]()
    mIsUseable = True
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def CanBeSampled(self):
        ReturnValue = False
    

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
        ReturnValue1: Ptr[FGCharacterPlayer] = self.FGResearchMachine.GetMachineUser()
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        if not ReturnValue:
            goto('L277')
        ReturnValue_0: Ptr[FGCharacterPlayer] = self.FGResearchMachine.GetMachineUser()
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
    

    def UserConstructionScript(self):
        self.FGResearchMachine.SetResearchMeshComponent(self.ResearchingMesh_static)
        self.FGResearchMachine.SetResearchMeshCurveScale(self.mResearchMeshScale)
    
