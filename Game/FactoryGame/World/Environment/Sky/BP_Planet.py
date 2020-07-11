
from codegen.ue4_stub import *

from Script.FactoryGame import GetTimeOfDayHours
from Script.Engine import SetScalarParameterValue
from Game.FactoryGame.World.Environment.Sky.BP_Planet import ExecuteUbergraph_BP_Planet.K2Node_Event_gameVersion1
from Script.Engine import SetPosition
from Game.FactoryGame.World.Environment.Sky.BP_Planet import ExecuteUbergraph_BP_Planet.K2Node_Event_gameVersion2
from Script.Engine import MaterialInstanceDynamic
from Game.FactoryGame.World.Environment.Sky.BP_Planet import ExecuteUbergraph_BP_Planet.K2Node_Event_DeltaSeconds
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Game.FactoryGame.World.Environment.Sky.BP_Planet import ExecuteUbergraph_BP_Planet.K2Node_Event_saveVersion3
from Game.FactoryGame.World.Environment.Sky.BP_Planet import ExecuteUbergraph_BP_Planet.K2Node_Event_saveVersion1
from Game.FactoryGame.World.Environment.Sky.BP_Planet import ExecuteUbergraph_BP_Planet.K2Node_Event_saveVersion2
from Script.CoreUObject import Object
from Script.Engine import IsValid
from Script.FactoryGame import FGPlanet
from Game.FactoryGame.World.Environment.Sky.BP_Planet import ExecuteUbergraph_BP_Planet.K2Node_Event_gameVersion
from Script.Engine import CurveFloat
from Script.FactoryGame import FGTimeOfDaySubsystem
from Script.Engine import AnimSequence
from Script.Engine import MaterialInterface
from Game.FactoryGame.World.Environment.Sky.BP_Planet import ExecuteUbergraph_BP_Planet.K2Node_Event_gameVersion3
from Script.Engine import GetPosition
from Game.FactoryGame.World.Environment.Sky.BP_Planet import ExecuteUbergraph_BP_Planet.K2Node_Event_saveVersion
from Script.FactoryGame import Default__FGTimeOfDaySubsystem
from Game.FactoryGame.World.Environment.Sky.BP_Planet import ExecuteUbergraph_BP_Planet
from Script.Engine import GetFloatValue

class BP_Planet(FGPlanet):
    mMaterial: Ptr[MaterialInterface]
    mMaterialInstance: Ptr[MaterialInstanceDynamic]
    mOpacityCurve: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Sky/Curve_PlanetOpacity.Curve_PlanetOpacity')
    mInitialLocation: float
    mAnimToPlay: Ptr[AnimSequence] = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Sky/Mesh/BackgroundPlanet_02_Skeletal_Anim.BackgroundPlanet_02_Skeletal_Anim')
    FadeOutRim: bool
    FadeInRim: bool
    mRimLightCurve: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Sky/Curve_RimLightFade.Curve_RimLightFade')
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    
    def ShouldSave(self):
        ReturnValue = False
    

    def GatherDependencies(self):
        dependentObjects: List[Ptr[Object]] = List[ObjectProperty /Game/FactoryGame/World/Environment/Sky/BP_Planet.BP_Planet_C:GatherDependencies.out_dependentObjects.out_dependentObjects]([])
    

    def NeedTransform(self):
        ReturnValue = False
    

    def UpdateMaterialParameters(self):
        ReturnValue: Ptr[FGTimeOfDaySubsystem] = Default__FGTimeOfDaySubsystem.Get(self)
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L314')
        ReturnValue = Default__FGTimeOfDaySubsystem.Get(self)
        ReturnValue_1: float = ReturnValue.GetTimeOfDayHours()
        ReturnValue_2: float = self.mOpacityCurve.GetFloatValue(ReturnValue_1)
        self.mMaterialInstance.SetScalarParameterValue("DayNightFade", ReturnValue_2)
    

    def UserConstructionScript(self):
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.SkeletalMesh.CreateDynamicMaterialInstance(0, self.mMaterial, "None")
        self.mMaterialInstance = ReturnValue
        SingleAnimationPlayData.AnimToPlay = self.mAnimToPlay
        SingleAnimationPlayData.bSavedLooping = True
        SingleAnimationPlayData.bSavedPlaying = True
        SingleAnimationPlayData.SavedPosition = self.mInitialLocation
        SingleAnimationPlayData.SavedPlayRate = 0.019999999552965164
        self.SkeletalMesh.AnimationData = SingleAnimationPlayData
    

    def PostSaveGame(self):
        ExecuteUbergraph_BP_Planet.K2Node_Event_saveVersion3 = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Planet.K2Node_Event_gameVersion3 = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Planet(10)
    

    def PreLoadGame(self):
        ExecuteUbergraph_BP_Planet.K2Node_Event_saveVersion2 = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Planet.K2Node_Event_gameVersion2 = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Planet(379)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_Planet(15)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_Planet.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Planet(62)
    

    def UpdatePreview(self):
        self.ExecuteUbergraph_BP_Planet(287)
    

    def PreSaveGame(self):
        ExecuteUbergraph_BP_Planet.K2Node_Event_saveVersion1 = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Planet.K2Node_Event_gameVersion1 = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Planet(292)
    

    def PostLoadGame(self):
        ExecuteUbergraph_BP_Planet.K2Node_Event_saveVersion = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_Planet.K2Node_Event_gameVersion = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Planet(374)
    

    def ExecuteUbergraph_BP_Planet(self):
        # End
        self.SkeletalMesh.SetPosition(self.mInitialLocation, False)
        # End
        # Label 62
        self.UpdateMaterialParameters()
        ReturnValue: Ptr[FGTimeOfDaySubsystem] = Default__FGTimeOfDaySubsystem.Get(self)
        ReturnValue_0: float = ReturnValue.GetTimeOfDayHours()
        ReturnValue_1: float = self.mRimLightCurve.GetFloatValue(ReturnValue_0)
        self.mMaterialInstance.SetScalarParameterValue("Fade_Alpha", ReturnValue_1)
        # End
        goto('L62')
        ReturnValue_2: float = self.SkeletalMesh.GetPosition()
        self.mInitialLocation = ReturnValue_2
        # End
        # End
    
