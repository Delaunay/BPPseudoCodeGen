
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_AttentionPingActor import ExecuteUbergraph_BP_AttentionPingActor
from Script.FactoryGame import CreateAndAddNewRepresentationNoActor
from Script.AkAudio import PostAkEventAtLocation
from Script.Engine import SpawnEmitterAtLocation
from Script.FactoryGame import FGPlayerState
from Script.CoreUObject import Rotator
from Script.FactoryGame import GetOwningPlayerState
from Script.FactoryGame import FGAttentionPingActor
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_Icon_ping import MapCompass_Icon_ping
from Script.FactoryGame import Get
from Game.FactoryGame.VFX.Misc.Ping.P_PingAttention_01 import P_PingAttention_01
from Script.FactoryGame import Default__FGActorRepresentationManager
from Script.FactoryGame import GetNametagColor
from Script.Engine import Default__GameplayStatics
from Script.Engine import Conv_LinearColorToVector
from Script.CoreUObject import Vector
from Script.FactoryGame import FGActorRepresentationManager
from Script.Engine import K2_GetActorRotation
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.ResourceScanner.Audio.Play_EQ_Resource_Ping_Hit import Play_EQ_Resource_Ping_Hit
from Script.Engine import ParticleSystemComponent
from Script.Engine import K2_GetActorLocation
from Script.Engine import SetVectorParameter
from Script.FactoryGame import GetPingColor
from Script.AkAudio import AkComponent
from Script.CoreUObject import LinearColor

class BP_AttentionPingActor(FGAttentionPingActor):
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bAlwaysRelevant = True
    bReplicateMovement = True
    bReplicates = True
    RemoteRole = 1
    
    def SpawnAttentionPingEffects(self):
        self.ExecuteUbergraph_BP_AttentionPingActor(669)
    

    def ExecuteUbergraph_BP_AttentionPingActor(self):
        # Label 10
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue_0: Rotator = self.K2_GetActorRotation()
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_EQ_Resource_Ping_Hit, ReturnValue, ReturnValue_0)
        ReturnValue = self.K2_GetActorLocation()
        ReturnValue_2: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue1: Ptr[FGPlayerState] = self.GetOwningPlayerState()
        ReturnValue_3: LinearColor = ReturnValue1.GetNametagColor()
        ReturnValue_4: bool = ReturnValue_2.CreateAndAddNewRepresentationNoActor(ReturnValue, MapCompass_Icon_ping, ReturnValue_3, 4.800000190734863, True, True, 4, True)
        # End
        # Label 361
        ReturnValue = self.K2_GetActorLocation()
        ReturnValue_0 = self.K2_GetActorRotation()
        ReturnValue_5: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_PingAttention_01, ReturnValue, ReturnValue_0, Vector(1, 1, 1), True, 0)
        ReturnValue_6: Ptr[FGPlayerState] = self.GetOwningPlayerState()
        ReturnValue_7: LinearColor = ReturnValue_6.GetPingColor()
        ReturnValue_8: Vector = Conv_LinearColorToVector(ReturnValue_7)
        ReturnValue_5.SetVectorParameter("Color", ReturnValue_8)
        goto('L10')
        goto('L361')
    
