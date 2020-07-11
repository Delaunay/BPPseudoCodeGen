
from codegen.ue4_stub import *

from Script.Engine import ReceiveDestroyed
from Game.FactoryGame.Character.Player.BP_DeathMarker import ExecuteUbergraph_BP_DeathMarker.K2Node_ComponentBoundEvent_bFromSweep
from Game.FactoryGame.Character.Player.BP_DeathMarker import ExecuteUbergraph_BP_DeathMarker.K2Node_ComponentBoundEvent_SweepResult
from Script.FactoryGame import CreateAndAddNewRepresentation
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Character.Player.BP_DeathMarker import ExecuteUbergraph_BP_DeathMarker.K2Node_Event_saveVersion2
from Game.FactoryGame.Character.Player.BP_DeathMarker import ExecuteUbergraph_BP_DeathMarker.K2Node_Event_saveVersion1
from Script.Engine import ReceiveBeginPlay
from Script.FactoryGame import IsAliveAndWell
from Game.FactoryGame.Character.Player.BP_DeathMarker import ExecuteUbergraph_BP_DeathMarker.K2Node_Event_saveVersion3
from Script.Engine import HasAuthority
from Script.FactoryGame import Get
from Game.FactoryGame.Character.Player.BP_DeathMarker import ExecuteUbergraph_BP_DeathMarker.K2Node_ComponentBoundEvent_OtherActor
from Game.FactoryGame.Character.Player.BP_DeathMarker import ExecuteUbergraph_BP_DeathMarker.K2Node_ComponentBoundEvent_OtherBodyIndex
from Game.FactoryGame.Character.Player.BP_DeathMarker import ExecuteUbergraph_BP_DeathMarker.K2Node_Event_gameVersion2
from Game.FactoryGame.Character.Player.BP_DeathMarker import ExecuteUbergraph_BP_DeathMarker.K2Node_ComponentBoundEvent_OverlappedComponent
from Script.CoreUObject import Object
from Script.FactoryGame import Default__FGActorRepresentationManager
from Game.FactoryGame.Character.Player.BP_DeathMarker import ExecuteUbergraph_BP_DeathMarker.K2Node_ComponentBoundEvent_OtherComp
from Game.FactoryGame.Character.Player.BP_DeathMarker import ExecuteUbergraph_BP_DeathMarker.K2Node_Event_saveVersion
from Game.FactoryGame.Character.Player.BP_DeathMarker import ExecuteUbergraph_BP_DeathMarker.K2Node_Event_gameVersion
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_Icon_deathcrate import MapCompass_Icon_deathcrate
from Script.Engine import FlushNetDormancy
from Script.CoreUObject import Vector
from Script.FactoryGame import FGActorRepresentationManager
from Game.FactoryGame.Character.Player.BP_DeathMarker import ExecuteUbergraph_BP_DeathMarker.K2Node_Event_gameVersion3
from Game.FactoryGame.Character.Player.BP_DeathMarker import ExecuteUbergraph_BP_DeathMarker.K2Node_Event_gameVersion1
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Script.FactoryGame import RemoveRepresentationOfActor
from Game.FactoryGame.Character.Player.BP_DeathMarker import ExecuteUbergraph_BP_DeathMarker
from Game.FactoryGame.Character.Player.BP_DeathMarker import ExecuteUbergraph_BP_DeathMarker.K2Node_Event_newColor
from Script.CoreUObject import LinearColor

class BP_DeathMarker(Actor):
    mMapText: FText
    
    def ShouldSave(self):
        ReturnValue = True
    

    def GatherDependencies(self):
        Array: List[Ptr[Object]] = [None]
        dependentObjects: List[Ptr[Object]] = Array
    

    def NeedTransform(self):
        ReturnValue = True
    

    def GetActorCompassViewDistance(self):
        ReturnValue = 4
    

    def SetActorCompassViewDistance(self):
        ReturnValue = 0
    

    def SetActorRepresentationText(self):
        self.FlushNetDormancy()
        # Label 10
        self.mMapText = newText
        ReturnValue = self.mMapText
    

    def UpdateRepresentation(self):
        ReturnValue = False
    

    def GetActorFogOfWarRevealRadius(self):
        ReturnValue = 0
    

    def GetActorFogOfWarRevealType(self):
        ReturnValue = 0
    

    def GetActorRepresentationColor(self):
        ReturnValue = LinearColor(R = 1, G = 0.3855229914188385, B = 0, A = 1)
    

    def GetActorRepresentationText(self):
        ReturnValue = self.mMapText
    

    def GetActorRepresentationTexture(self):
        ReturnValue = MapCompass_Icon_deathcrate
    

    def GetActorRepresentationType(self):
        ReturnValue = 5
    

    def GetActorShouldShowInCompass(self):
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
    

    def GetActorShouldShowOnMap(self):
        ReturnValue = True
    

    def GetRealActorLocation(self):
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue_0: Vector = ReturnValue
    

    def GetRealActorRotation(self):
        ReturnValue = Rotator::FromPitchYawRoll(0, 0, 0)
    

    def IsActorStatic(self):
        ReturnValue = True
    

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
    

    def PostLoadGame(self):
        ExecuteUbergraph_BP_DeathMarker.K2Node_Event_saveVersion3 = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_DeathMarker.K2Node_Event_gameVersion3 = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_DeathMarker(49)
    

    def PostSaveGame(self):
        ExecuteUbergraph_BP_DeathMarker.K2Node_Event_saveVersion2 = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_DeathMarker.K2Node_Event_gameVersion2 = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_DeathMarker(54)
    

    def PreLoadGame(self):
        ExecuteUbergraph_BP_DeathMarker.K2Node_Event_saveVersion1 = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_DeathMarker.K2Node_Event_gameVersion1 = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_DeathMarker(59)
    

    def PreSaveGame(self):
        ExecuteUbergraph_BP_DeathMarker.K2Node_Event_saveVersion = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_DeathMarker.K2Node_Event_gameVersion = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_DeathMarker(64)
    

    def SetActorRepresentationColor(self):
        ExecuteUbergraph_BP_DeathMarker.K2Node_Event_newColor = NewColor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_DeathMarker(69)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_DeathMarker(74)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_BP_DeathMarker(79)
    

    def BndEvt__Sphere_K2Node_ComponentBoundEvent_0_ComponentBeginOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32, bFromSweep: bool, SweepResult: Const[Ref[HitResult]]):
        ExecuteUbergraph_BP_DeathMarker.K2Node_ComponentBoundEvent_OverlappedComponent = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_DeathMarker.K2Node_ComponentBoundEvent_OtherActor = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_DeathMarker.K2Node_ComponentBoundEvent_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_DeathMarker.K2Node_ComponentBoundEvent_OtherBodyIndex = OtherBodyIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_DeathMarker.K2Node_ComponentBoundEvent_bFromSweep = bFromSweep #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_DeathMarker.K2Node_ComponentBoundEvent_SweepResult = SweepResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_DeathMarker(118)
    

    def ExecuteUbergraph_BP_DeathMarker(self):
        # Label 10
        self.ReceiveBeginPlay()
        ReturnValue: bool = self.AddAsRepresentation()
        # End
        # End
        # End
        # End
        # End
        # End
        goto('L10')
        self.ReceiveDestroyed()
        ReturnValue_0: bool = self.RemoveAsRepresentation()
        # End
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](OtherActor)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L267')
        ReturnValue_1: bool = Player.IsAliveAndWell()
        if not ReturnValue_1:
            goto('L267')
        self.K2_DestroyActor()
    
