
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.Parachute.Audio.Play_Parachute_Open import Play_Parachute_Open
from Script.AkAudio import PostAkEvent
from Script.Engine import FClamp
from Script.Engine import Controller
from Script.Engine import Pawn
from Script.Engine import SetHiddenInGame
from Game.FactoryGame.Equipment.Parachute.Equip_Parachute import ExecuteUbergraph_Equip_Parachute
from Script.Engine import PlayerController
from Script.Engine import GetController
from Script.Engine import K2_GetPawn
from Script.FactoryGame import FGParachute
from Script.FactoryGame import FGParachuteCameraShake
from Game.FactoryGame.Equipment.Parachute.Audio.Stop_Parachute import Stop_Parachute
from Game.FactoryGame.LandingShake_Parachute import LandingShake_Parachute
from Game.FactoryGame.Character.Player.Char_Player import Char_Player
from Script.CoreUObject import Vector
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import Actor
from Script.Engine import GetOwner
from Script.AkAudio import AkComponent

class Equip_Parachute(FGParachute):
    mTerminalVelocityZ = 300
    mEquipmentSlot = EEquipmentSlot::ES_BACK
    mCostToUse = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/Beacon/Desc_Parachute.Desc_Parachute_C', 'amount': 1}]
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def OnDeployed(self):
        self.ExecuteUbergraph_Equip_Parachute(10)
    

    def OnDeployStop(self):
        self.ExecuteUbergraph_Equip_Parachute(780)
    

    def ExecuteUbergraph_Equip_Parachute(self):
        ReturnValue1: Ptr[Actor] = self.GetOwner()
        Player: Ptr[Char_Player] = Cast[Char_Player](ReturnValue1)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L1150')
        ReturnValue: Ptr[Controller] = Player.GetController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue)
        bSuccess1: bool = Controller
        if not bSuccess1:
            goto('L1150')
        ReturnValue_0: Ptr[Pawn] = Controller.K2_GetPawn()
        ReturnValue_1: Vector = ReturnValue_0.GetVelocity()
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_1)
        ReturnValue_2: float = Z * -0.0006000000284984708
        ReturnValue_3: float = FClamp(ReturnValue_2, 0.10000000149011612, 1.5)
        Controller.ClientPlayCameraShake(FGParachuteCameraShake, ReturnValue_3, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        self.ParachuteMesh.SetHiddenInGame(False, False)
        ReturnValue3: Ptr[Actor] = self.ParachuteMesh.GetOwner()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_Parachute_Open, ReturnValue3, True)
        # End
        # Label 672
        ReturnValue_4: Ptr[Actor] = self.ParachuteMesh.GetOwner()
        ReturnValue_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_Parachute, ReturnValue_4, True)
        # End
        self.ParachuteMesh.SetHiddenInGame(True, False)
        ReturnValue2: Ptr[Actor] = self.GetOwner()
        Player1: Ptr[Char_Player] = Cast[Char_Player](ReturnValue2)
        bSuccess2: bool = Player1
        if not bSuccess2:
            goto('L1150')
        ReturnValue1_1: Ptr[Controller] = Player1.GetController()
        Controller1: Ptr[PlayerController] = Cast[PlayerController](ReturnValue1_1)
        bSuccess3: bool = Controller1
        if not bSuccess3:
            goto('L1150')
        Controller1.ClientStopCameraShake(FGParachuteCameraShake, True)
        Controller1.ClientPlayCameraShake(LandingShake_Parachute, 1, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        goto('L672')
    
