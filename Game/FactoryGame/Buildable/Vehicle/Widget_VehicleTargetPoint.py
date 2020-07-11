
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.Engine import Conv_TextToString
from Game.FactoryGame.Buildable.Vehicle.BP_VehicleTargetPoint import BP_VehicleTargetPoint
from Script.FactoryGame import FGPlayerController
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import PreConstruct
from Game.FactoryGame.Buildable.Vehicle.Widget_VehicleTargetPoint import ExecuteUbergraph_Widget_VehicleTargetPoint
from Script.Engine import EqualEqual_ByteByte
from Script.FactoryGame import GetWaitTime
from Script.Engine import HUD
from Game.FactoryGame.Buildable.Vehicle.Widget_VehicleTargetPoint import ExecuteUbergraph_Widget_VehicleTargetPoint.K2Node_Event_IsDesignTime
from Script.Engine import PlayerController
from Script.UMG import SetText
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.Engine import Conv_FloatToText
from Script.Engine import GetHUD
from Game.FactoryGame.Buildable.Vehicle.Widget_VehicleTargetPoint import ExecuteUbergraph_Widget_VehicleTargetPoint.K2Node_ComponentBoundEvent_CommitMethod
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Buildable.Vehicle.Widget_VehicleTargetPoint import ExecuteUbergraph_Widget_VehicleTargetPoint.K2Node_ComponentBoundEvent_mPopUpConfirm
from Game.FactoryGame.Buildable.Vehicle.Widget_VehicleTargetPoint import ExecuteUbergraph_Widget_VehicleTargetPoint.K2Node_CustomEvent_ConfirmClicked
from Script.FactoryGame import GetGameUI
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import Init
from Script.FactoryGame import GetOwningVehicle
from Script.UMG import GetText
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import FGHUD
from Script.FactoryGame import FGGameUI
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.Engine import Conv_StringToFloat
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Destruct
from Script.FactoryGame import AddPopupWithCloseDelegate
from Game.FactoryGame.Buildable.Vehicle.Widget_VehicleTargetPoint import ExecuteUbergraph_Widget_VehicleTargetPoint.K2Node_ComponentBoundEvent_Text
from Script.FactoryGame import IsTargetSpeedStill
from Script.FactoryGame import FGWheeledVehicle

class Widget_VehicleTargetPoint(Widget_UseableBase):
    mOwningTargetPoint: Ptr[BP_VehicleTargetPoint]
    mRemoveNode: bool
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    
    def SetNewWaitTime(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: FText = self.Widget_InputBox.mInputBox.GetText()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        
        ReturnValue_1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_0])
        ReturnValue_2: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_3: float = Default__KismetStringLibrary.Conv_StringToFloat(ReturnValue_1)
        ReturnValue_2.ServerSetWaitTime(self.mOwningTargetPoint, ReturnValue_3)
    

    def GetNodeTypeAndSetWindowTitle(self):
        ReturnValue: bool = self.mOwningTargetPoint.IsTargetSpeedStill()
        if not ReturnValue:
            goto('L157')
        self.Widget_Window_DarkMode.SetTitle("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 93, 'Value': 'Vehicle Waiting Node'}")
        # End
        # Label 157
        self.Widget_Window_DarkMode.SetTitle("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 194, 'Value': 'Vehicle Path Node'}")
    

    def Init(self):
        self.ExecuteUbergraph_Widget_VehicleTargetPoint(844)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_VehicleTargetPoint(859)
    

    def BndEvt__Widget_StandardButton_C_0_K2Node_ComponentBoundEvent_3_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_VehicleTargetPoint(1449)
    

    def BndEvt__mDeleteButton2_K2Node_ComponentBoundEvent_5_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_VehicleTargetPoint(1783)
    

    def BndEvt__mWaitButton_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_VehicleTargetPoint(1788)
    

    def SetWaitTimePopup(self, mPopUpConfirm: bool):
        ExecuteUbergraph_Widget_VehicleTargetPoint.K2Node_ComponentBoundEvent_mPopUpConfirm = mPopUpConfirm #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_VehicleTargetPoint(1793)
    

    def DoDeleteNode(self, ConfirmClicked: bool):
        ExecuteUbergraph_Widget_VehicleTargetPoint.K2Node_CustomEvent_ConfirmClicked = ConfirmClicked #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_VehicleTargetPoint(2289)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_VehicleTargetPoint(2323)
    

    def BndEvt__Widget_InputBox_K2Node_ComponentBoundEvent_6_OnTextComitted__DelegateSignature(self, text: FText, CommitMethod: uint8):
        ExecuteUbergraph_Widget_VehicleTargetPoint.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_VehicleTargetPoint.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_VehicleTargetPoint(2328)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_VehicleTargetPoint.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_VehicleTargetPoint(2378)
    

    def ExecuteUbergraph_Widget_VehicleTargetPoint(self):
        # Label 10
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L2397')
        ReturnValue_0: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_0)
        bSuccess2: bool = AsFGHUD
        if not bSuccess2:
            goto('L2397')
        ReturnValue_1: Ptr[FGGameUI] = AsFGHUD.GetGameUI()
        ReturnValue_1.PopAllWidgets()
        # End
        # Label 317
        Point: Ptr[BP_VehicleTargetPoint] = Cast[BP_VehicleTargetPoint](self.mInteractObject)
        bSuccess1: bool = Point
        if not bSuccess1:
            goto('L415')
        self.mOwningTargetPoint = Point
        # Label 415
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
        self.GetNodeTypeAndSetWindowTitle()
        ReturnValue_2: float = self.mOwningTargetPoint.GetWaitTime()
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_2, 0, False, True, 1, 324, 0, 3)
        self.Widget_InputBox.mInputBox.SetText(ReturnValue_3)
        ReturnValue_4: bool = self.mOwningTargetPoint.IsTargetSpeedStill()
        Variable: bool = ReturnValue_4
        
        switch = {
            False: self.mPathNodeWindow,
            True: self.mWaitNodeWindow
        }
        self.mNodeWindowSwitcher.SetActiveWidget(switch.get(Variable, None))
        # End
        self.Init()
        # End
        self.Destruct()
        if not self.mRemoveNode:
            goto('L2397')
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: Ptr[FGWheeledVehicle] = self.mOwningTargetPoint.GetOwningVehicle()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1)
        bSuccess3: bool = Controller1
        ReturnValue_6: Ptr[BP_RemoteCallObject] = Controller1.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_6.ServerRemoveTargetPoint(self.mOwningTargetPoint, ReturnValue_5)
        # End
        # Label 1124
        self.mRemoveNode = True
        goto('L10')
        # Label 1140
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller2: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue2)
        bSuccess4: bool = Controller2
        if not bSuccess4:
            goto('L2397')
        OutputDelegate1.BindUFunction(self, DoDeleteNode)
        
        OutputDelegate1 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(Controller2, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1308, 'Value': 'Delete node?'}", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1360, 'Value': 'Do you want to delete this node?'}", 1, None, None, Ref[OutputDelegate1])
        # End
        goto('L1140')
        # Label 1454
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller3: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue3)
        bSuccess5: bool = Controller3
        if not bSuccess5:
            goto('L2397')
        OutputDelegate2.BindUFunction(self, SetWaitTimePopup)
        
        OutputDelegate2 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(Controller3, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1622, 'Value': 'Set Wait Time'}", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1675, 'Value': 'Confirming will update the wait time for this node.'}", 1, None, None, Ref[OutputDelegate2])
        # End
        goto('L1140')
        goto('L1454')
        ReturnValue_7: FText = self.Widget_InputBox.mInputBox.GetText()
        
        ReturnValue_8: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_7])
        ReturnValue_9: float = Default__KismetStringLibrary.Conv_StringToFloat(ReturnValue_8)
        ReturnValue_10: bool = ReturnValue_9 > 0
        ReturnValue_11: bool = mPopUpConfirm and ReturnValue_10
        if not ReturnValue_11:
            goto('L2088')
        self.SetNewWaitTime()
        # End
        # Label 2088
        ReturnValue1_0: float = self.mOwningTargetPoint.GetWaitTime()
        ReturnValue1_1: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue1_0, 0, False, True, 1, 324, 0, 3)
        self.Widget_InputBox.mInputBox.SetText(ReturnValue1_1)
        # End
        if not ConfirmClicked:
            goto('L2397')
        goto('L1124')
        # Label 2308
        self.Construct()
        goto('L317')
        goto('L2308')
        ReturnValue_12: bool = EqualEqual_ByteByte(CommitMethod, 1)
        if not ReturnValue_12:
            goto('L2397')
        goto('L1454')
        self.PreConstruct(IsDesignTime)
    
