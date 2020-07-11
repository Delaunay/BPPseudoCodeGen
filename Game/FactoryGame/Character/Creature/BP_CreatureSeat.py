
from codegen.ue4_stub import *

from Script.Engine import ReceivePossessed
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Controller_SpaceGiraffe import Controller_SpaceGiraffe
from Script.Engine import GetInputAxisValue
from Script.CoreUObject import Rotator
from Script.FactoryGame import FGCreature
from Script.Engine import Not_PreBool
from Script.FactoryGame import SetPersistent
from Script.Engine import HUD
from Script.FactoryGame import FGCreatureSeat
from Script.Engine import GetAnimInstance
from Script.Engine import ReceiveTick
from Script.Engine import GetController
from Script.FactoryGame import GetDisabledInputGate
from Game.FactoryGame.Character.Creature.BP_CreatureSeat import ExecuteUbergraph_BP_CreatureSeat.K2Node_InputActionEvent_Key1
from Script.FactoryGame import DisabledInputGate
from Script.Engine import GetHUD
from Script.FactoryGame import GetDriver
from Game.FactoryGame.Character.Creature.BP_CreatureSeat import ExecuteUbergraph_BP_CreatureSeat.K2Node_Event_DeltaSeconds
from Script.Engine import BreakRotator
from Script.CoreUObject import Vector
from Script.Engine import ClampAngle
from Game.FactoryGame.Character.Creature.BP_CreatureSeat import ExecuteUbergraph_BP_CreatureSeat.K2Node_InputActionEvent_Key
from Script.Engine import Montage_Play
from Script.FactoryGame import FGHUD
from Script.Engine import MakeRotator
from Game.FactoryGame.Character.Creature.BP_CreatureSeat import ExecuteUbergraph_BP_CreatureSeat.K2Node_Event_NewController
from Game.FactoryGame.Character.Creature.BP_CreatureSeat import ExecuteUbergraph_BP_CreatureSeat
from Game.FactoryGame.Character.Creature.BP_CreatureSeat import ExecuteUbergraph_BP_CreatureSeat.K2Node_CustomEvent_controller
from Script.FactoryGame import SetShowCrossHair
from Script.Engine import GetForwardVector
from Script.Engine import AnimInstance
from Script.Engine import K2_SetRelativeRotation
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.Clap_01_Montage import Clap_01_Montage
from Game.FactoryGame.Character.Creature.BP_CreatureSeat import ExecuteUbergraph_BP_CreatureSeat.K2Node_InputAxisEvent_AxisValue
from Script.FactoryGame import GetMountedCreature

class BP_CreatureSeat(FGCreatureSeat):
    mShouldAttachDriver = True
    mIsDriverVisible = True
    mDriverSeatSocket = RideSocket
    mDriverSeatAnimation = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Animation/ThirdPerson/Mounted_01.Mounted_01')
    
    def InpActEvt_Use_K2Node_InputActionEvent_1(self, Key: Key):
        ExecuteUbergraph_BP_CreatureSeat.K2Node_InputActionEvent_Key1 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_CreatureSeat(1945)
    

    def InpActEvt_Jump_Drift_K2Node_InputActionEvent_0(self, Key: Key):
        ExecuteUbergraph_BP_CreatureSeat.K2Node_InputActionEvent_Key = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_CreatureSeat(1283)
    

    def InpAxisEvt_MoveForward_K2Node_InputAxisEvent_0(self, AxisValue: float):
        ExecuteUbergraph_BP_CreatureSeat.K2Node_InputAxisEvent_AxisValue = AxisValue #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_CreatureSeat(933)
    

    def UpdateCamera(self):
        self.ExecuteUbergraph_BP_CreatureSeat(230)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_CreatureSeat.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_CreatureSeat(716)
    

    def ReceivePossessed(self):
        ExecuteUbergraph_BP_CreatureSeat.K2Node_Event_NewController = NewController #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_CreatureSeat(754)
    

    def ClientSetupHUD(self, Controller: Ptr[FGPlayerController]):
        ExecuteUbergraph_BP_CreatureSeat.K2Node_CustomEvent_controller = Controller #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_CreatureSeat(1124)
    

    def Server_Leave(self):
        self.ExecuteUbergraph_BP_CreatureSeat(1316)
    

    def Server_DoAction(self):
        self.ExecuteUbergraph_BP_CreatureSeat(1360)
    

    def Multicast_PlayClap(self):
        self.ExecuteUbergraph_BP_CreatureSeat(1542)
    

    def Server_PlayClap(self):
        self.ExecuteUbergraph_BP_CreatureSeat(1727)
    

    def PlayClap(self):
        self.ExecuteUbergraph_BP_CreatureSeat(1746)
    

    def ExecuteUbergraph_BP_CreatureSeat(self):
        # Label 10
        ReturnValue: Ptr[Controller] = self.GetController()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L1950')
        ReturnValue_0: DisabledInputGate = Controller.GetDisabledInputGate()
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0.mUse)
        if not ReturnValue_1:
            goto('L1950')
        self.Server_Leave()
        # End
        ReturnValue_2: float = self.GetInputAxisValue("Turn")
        ReturnValue1: float = self.GetInputAxisValue("LookUp")
        ReturnValue_3: float = ReturnValue1 * -1
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(self.SpringArm.RelativeRotation, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_4: float = Yaw + ReturnValue_2
        ReturnValue_5: float = ClampAngle(ReturnValue_4, -179, 179)
        ReturnValue1_0: float = ReturnValue_3 + Pitch
        ReturnValue1_1: float = ClampAngle(ReturnValue1_0, -89, 89)
        ReturnValue_6: Rotator = MakeRotator(0, ReturnValue1_1, ReturnValue_5)
        
        SweepHitResult = None
        self.SpringArm.K2_SetRelativeRotation(ReturnValue_6, False, False, Ref[SweepHitResult])
        # End
        self.ReceiveTick(DeltaSeconds)
        self.UpdateCamera()
        # End
        self.ReceivePossessed(NewController)
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](NewController)
        bSuccess1: bool = Controller1
        if not bSuccess1:
            goto('L1950')
        self.ClientSetupHUD(Controller1)
        ReturnValue1_2: Ptr[FGCreature] = self.GetMountedCreature()
        ReturnValue1_2.SetPersistent(True)
        # End
        
        OutLocation = None
        OutRotation = None
        self.GetActorEyesViewPoint(Ref[OutLocation], Ref[OutRotation])
        ReturnValue_7: Vector = GetForwardVector(OutRotation)
        ReturnValue_8: Ptr[FGCreature] = self.GetMountedCreature()
        ReturnValue_9: Vector = ReturnValue_7 * AxisValue
        ReturnValue_8.AddMovementInput(ReturnValue_9, 800, True)
        # End
        ReturnValue_10: Ptr[HUD] = controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_10)
        bSuccess2: bool = AsFGHUD
        if not bSuccess2:
            goto('L1950')
        AsFGHUD.SetShowCrossHair(False)
        # End
        self.PlayClap()
        self.Server_DoAction()
        # End
        ReturnValue_11: bool = self.DriverLeave(False)
        self.K2_DestroyActor()
        # End
        ReturnValue2: Ptr[FGCreature] = self.GetMountedCreature()
        ReturnValue1_3: Ptr[Controller] = ReturnValue2.GetController()
        Giraffe: Ptr[Controller_SpaceGiraffe] = Cast[Controller_SpaceGiraffe](ReturnValue1_3)
        bSuccess3: bool = Giraffe
        if not bSuccess3:
            goto('L1950')
        Giraffe.StartPanic()
        # End
        ReturnValue_12: Ptr[FGCharacterPlayer] = self.GetDriver()
        ReturnValue_13: Ptr[SkeletalMeshComponent] = ReturnValue_12.GetMesh3P()
        ReturnValue_14: Ptr[AnimInstance] = ReturnValue_13.GetAnimInstance()
        ReturnValue_15: float = ReturnValue_14.Montage_Play(Clap_01_Montage, 1, 0, 0, True)
        # End
        self.Multicast_PlayClap()
        # End
        ReturnValue1_4: Ptr[FGCharacterPlayer] = self.GetDriver()
        ReturnValue1_5: Ptr[SkeletalMeshComponent] = ReturnValue1_4.GetMesh3P()
        ReturnValue1_6: Ptr[AnimInstance] = ReturnValue1_5.GetAnimInstance()
        ReturnValue1_7: float = ReturnValue1_6.Montage_Play(Clap_01_Montage, 1, 0, 0, True)
        self.Server_PlayClap()
        # End
        goto('L10')
    
