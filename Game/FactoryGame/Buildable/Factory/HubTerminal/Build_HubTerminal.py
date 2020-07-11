
from codegen.ue4_stub import *

from Script.Engine import ActorHasTag
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.FactoryGame import GetLookAtDecription
from Script.FactoryGame import FGBuildableHubTerminal
from Script.FactoryGame import UpdateUseState
from Game.FactoryGame.Buildable.Factory.TradingPost.UseState_TradingPostTerminal import UseState_TradingPostTerminal
from Script.Engine import Not_PreBool

class Build_HubTerminal(FGBuildableHubTerminal):
    mHologramClass = NewObject[FGFactoryHologram]()
    mDisplayName = NSLOCTEXT("", "F6727D9446D0E5E2F9C171B61C1776F9", "Hub terminal")
    MaxRenderDistance = -1
    mHighlightVector = Namespace(X=0, Y=70, Z=370)
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=False, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/TradingPost/BP_MaterialEffect_Build_Hub.BP_MaterialEffect_Build_Hub_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mHighlightParticleSystemTemplate = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing')
    mShouldShowHighlight = True
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_TradingPost]()
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
    

    def UpdateUseState(self):
        
        useState = None
        Default__FGBlueprintFunctionLibrary.UpdateUseState(UseState_TradingPostTerminal, Ref[useState])
    

    def GetLookAtDecription(self):
        
        ReturnValue: FText = self.GetLookAtDecription(byCharacter, Ref[State])
        ReturnValue_0: FText = ReturnValue
    
