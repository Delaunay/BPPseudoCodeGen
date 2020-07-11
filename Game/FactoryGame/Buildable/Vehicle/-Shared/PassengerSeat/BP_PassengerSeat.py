
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.Engine import ReceivePossessed
from Script.FactoryGame import FGPlayerController
from Script.Engine import Controller
from Script.Engine import GetInputAxisValue
from Script.CoreUObject import Rotator
from Script.Engine import Not_PreBool
from Game.FactoryGame.Buildable.Vehicle.-Shared.PassengerSeat.BP_PassengerSeat import ExecuteUbergraph_BP_PassengerSeat
from Game.FactoryGame.Buildable.Vehicle.-Shared.PassengerSeat.BP_PassengerSeat import ExecuteUbergraph_BP_PassengerSeat.K2Node_InputActionEvent_Key
from Script.Engine import GetController
from Script.FactoryGame import FGPassengerSeat
from Script.FactoryGame import GetDisabledInputGate
from Script.FactoryGame import DisabledInputGate
from Game.FactoryGame.Buildable.Vehicle.-Shared.PassengerSeat.BP_PassengerSeat import ExecuteUbergraph_BP_PassengerSeat.K2Node_Event_OldController
from Script.Engine import BreakRotator
from Game.FactoryGame.Buildable.Vehicle.Widget_PassengerSeat import Widget_PassengerSeat
from Script.Engine import ReceiveUnpossessed
from Script.Engine import MakeRotator
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.Engine import K2_SetRelativeRotation
from Game.FactoryGame.Buildable.Vehicle.-Shared.PassengerSeat.BP_PassengerSeat import ExecuteUbergraph_BP_PassengerSeat.K2Node_Event_NewController

class BP_PassengerSeat(FGPassengerSeat):
    mShouldAttachDriver = True
    mDriverSeatAnimation = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Animation/ThirdPerson/VehicleSitIdle.VehicleSitIdle')
    
    def InpActEvt_Use_K2Node_InputActionEvent_0(self, Key: Key):
        ExecuteUbergraph_BP_PassengerSeat.K2Node_InputActionEvent_Key = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PassengerSeat(750)
    

    def UpdateCamera(self):
        self.ExecuteUbergraph_BP_PassengerSeat(10)
    

    def ReceivePossessed(self):
        ExecuteUbergraph_BP_PassengerSeat.K2Node_Event_NewController = NewController #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PassengerSeat(360)
    

    def ReceiveUnpossessed(self):
        ExecuteUbergraph_BP_PassengerSeat.K2Node_Event_OldController = OldController #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PassengerSeat(560)
    

    def Server_Leave(self):
        self.ExecuteUbergraph_BP_PassengerSeat(970)
    

    def ExecuteUbergraph_BP_PassengerSeat(self):
        ReturnValue: float = self.GetInputAxisValue("Turn")
        ReturnValue1: float = self.GetInputAxisValue("LookUp")
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(self.SpringArm.RelativeRotation, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_0: float = Yaw + ReturnValue
        ReturnValue1_0: float = ReturnValue1 + Pitch
        ReturnValue_1: Rotator = MakeRotator(0, ReturnValue1_0, ReturnValue_0)
        
        SweepHitResult = None
        self.SpringArm.K2_SetRelativeRotation(ReturnValue_1, False, False, Ref[SweepHitResult])
        # End
        self.ReceivePossessed(NewController)
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](NewController)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L995')
        ReturnValue_2: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_2.Client_AddPawnHUD(Widget_PassengerSeat, self)
        # End
        self.ReceiveUnpossessed(OldController)
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](OldController)
        bSuccess1: bool = Controller1
        if not bSuccess1:
            goto('L995')
        ReturnValue1_1: Ptr[BP_RemoteCallObject] = Controller1.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue1_1.Client_RemovePawnHUD()
        # End
        ReturnValue_3: Ptr[Controller] = self.GetController()
        Controller2: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_3)
        bSuccess2: bool = Controller2
        if not bSuccess2:
            goto('L995')
        ReturnValue_4: DisabledInputGate = Controller2.GetDisabledInputGate()
        ReturnValue_5: bool = Not_PreBool(ReturnValue_4.mUse)
        if not ReturnValue_5:
            goto('L995')
        self.Server_Leave()
        # End
        ReturnValue_6: bool = self.DriverLeave(False)
    
