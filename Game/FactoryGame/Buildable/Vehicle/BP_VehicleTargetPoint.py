
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Vehicle.BP_VehicleTargetPoint import ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_state
from Script.FactoryGame import ShowOutline
from Script.FactoryGame import FGPlayerController
from Script.Engine import Controller
from Game.FactoryGame.Equipment.BuildGun.Mesh.Pause import Pause
from Script.Engine import K2_SetText
from Game.FactoryGame.Buildable.Vehicle.Widget_VehicleTargetPoint import Widget_VehicleTargetPoint
from Script.CoreUObject import Rotator
from Script.Engine import ReceiveBeginPlay
from Script.Engine import HUD
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Vehicle.BP_VehicleTargetPoint import ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_byCharacter1
from Script.Engine import GetController
from Script.Engine import FormatArgumentData
from Game.FactoryGame.Buildable.Vehicle.BP_VehicleTargetPoint import ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_byCharacter
from Game.FactoryGame.Buildable.Vehicle.BP_VehicleTargetPoint import ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_byCharacter3
from Game.FactoryGame.Equipment.BuildGun.Material.Hologram_Blue_Inst import Hologram_Blue_Inst
from Script.CoreUObject import Object
from Script.Engine import IsValid
from Script.Engine import GetHUD
from Game.FactoryGame.Buildable.Vehicle.BP_VehicleTargetPoint import ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_byCharacter2
from Game.FactoryGame.Buildable.Vehicle.BP_VehicleTargetPoint import ExecuteUbergraph_BP_VehicleTargetPoint
from Script.FactoryGame import HideOutline
from Script.FactoryGame import FGTargetPoint
from Game.FactoryGame.Buildable.Vehicle.BP_VehicleTargetPoint import ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_state1
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Game.FactoryGame.Buildable.Vehicle.BP_VehicleTargetPoint import ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_player1
from Game.FactoryGame.Buildable.Vehicle.BP_VehicleTargetPoint import ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_player
from Game.FactoryGame.Buildable.Vehicle.BP_VehicleTargetPoint import ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_state3
from Script.Engine import Format
from Script.FactoryGame import GetOwningVehicle
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import FGHUD
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.Engine import Conv_IntToString
from Script.Engine import K2_GetActorRotation
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Buildable.Vehicle.BP_VehicleTargetPoint import ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_state2
from Script.FactoryGame import GetTargetSpeed
from Game.FactoryGame.Equipment.BuildGun.Mesh.Arrow import Arrow
from Script.FactoryGame import FGUseState_Valid
from Script.Engine import K2_SetWorldRotation
from Script.Engine import SetActorScale3D
from Script.FactoryGame import UpdateUseState
from Script.FactoryGame import IsTargetSpeedStill
from Script.FactoryGame import FGWheeledVehicle

class BP_VehicleTargetPoint(FGTargetPoint):
    mUseText: FText = NSLOCTEXT("", "F851F9A949CDC663A01638AB377A35BE", "Press [{BUTTON}] to edit this node")
    mWaitTime = 3
    mDefaultWaitTime = 3
    mTargetSpeed = -1
    bReplicates = True
    
    def GetLookAtDecription(self):
        ReturnValue: Ptr[Controller] = byCharacter.GetController()
        
        button = None
        Default__HUDHelpers.GetKeyNameForActionSimple(ReturnValue, "Use", self, Ref[button])
        FormatArgumentData.ArgumentName = "BUTTON"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = button
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_0: FText = Default__KismetTextLibrary.Format(self.mUseText, Array)
        ReturnValue_1: FText = ReturnValue_0
    

    def IsUseable(self):
        ReturnValue = True
    

    def UpdateUseState(self):
        
        useState = None
        Default__FGBlueprintFunctionLibrary.UpdateUseState(FGUseState_Valid, Ref[useState])
    

    def ShouldSave(self):
        ReturnValue = True
    

    def NeedTransform(self):
        ReturnValue = True
    

    def GatherDependencies(self):
        Array: List[Ptr[Object]] = []
        dependentObjects: List[Ptr[Object]] = Array
    

    def OnUseStop(self):
        ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_byCharacter3 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_state3 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_VehicleTargetPoint(264)
    

    def RegisterInteractingPlayer(self):
        ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_player1 = Player #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_VehicleTargetPoint(269)
    

    def UnregisterInteractingPlayer(self):
        ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_player = Player #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_VehicleTargetPoint(274)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_VehicleTargetPoint(279)
    

    def OnUse(self):
        ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_byCharacter2 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_state2 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_VehicleTargetPoint(504)
    

    def StartIsLookedAt(self):
        ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_byCharacter1 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_state1 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_VehicleTargetPoint(904)
    

    def StopIsLookedAt(self):
        ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_byCharacter = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_VehicleTargetPoint.K2Node_Event_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_VehicleTargetPoint(952)
    

    def SetMeshRotation(self):
        self.ExecuteUbergraph_BP_VehicleTargetPoint(998)
    

    def ExecuteUbergraph_BP_VehicleTargetPoint(self):
        # Label 10
        ReturnValue: bool = self.IsTargetSpeedStill()
        if not ReturnValue:
            goto('L154')
        self.ArrowMesh.SetMaterial(0, Hologram_Blue_Inst)
        ReturnValue1: bool = self.ArrowMesh.SetStaticMesh(Pause)
        # End
        # Label 154
        self.ArrowMesh.SetMaterial(0, Hologram_Blue_Inst)
        ReturnValue_0: bool = self.ArrowMesh.SetStaticMesh(Arrow)
        # End
        # End
        # End
        # End
        self.ReceiveBeginPlay()
        self.SetActorScale3D(Vector(1, 1, 1))
        ReturnValue_1: int32 = self.GetTargetSpeed()
        ReturnValue_2: FString = Default__KismetStringLibrary.Conv_IntToString(ReturnValue_1)
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_2)
        
        self.TextRender.K2_SetText(Ref[ReturnValue_3])
        goto('L10')
        ReturnValue_4: Ptr[Controller] = byCharacter2.GetController()
        ReturnValue_5: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_4)
        if not ReturnValue_5:
            goto('L1120')
        ReturnValue_4 = byCharacter2.GetController()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_4)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L1120')
        ReturnValue_6: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_6)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
            goto('L1120')
        AsFGHUD.OpenInteractUI(Widget_VehicleTargetPoint, self)
        # End
        Default__FGBlueprintFunctionLibrary.ShowOutline(self.ArrowMesh, 252)
        # End
        Default__FGBlueprintFunctionLibrary.HideOutline(self.ArrowMesh)
        # End
        ReturnValue_7: Ptr[FGWheeledVehicle] = self.GetOwningVehicle()
        ReturnValue_8: Rotator = ReturnValue_7.K2_GetActorRotation()
        
        SweepHitResult = None
        self.ArrowMesh.K2_SetWorldRotation(ReturnValue_8, False, False, Ref[SweepHitResult])
    
