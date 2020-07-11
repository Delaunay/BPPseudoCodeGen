
from codegen.ue4_stub import *

from Script.UMG import SetUserFocus
from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.Engine import Conv_TextToString
from Game.FactoryGame.Interface.UI.InGame.Widget_ColorPicker_SingleColor import Widget_ColorPicker_SingleColor
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import EqualEqual_ByteByte
from Script.Engine import Pawn
from Game.FactoryGame.Equipment.Beacon.UI.Widget_Beacon import ExecuteUbergraph_Widget_Beacon.K2Node_ComponentBoundEvent_Text
from Script.UMG import OverlaySlot
from Script.Engine import TextIsEmpty
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import SetStructurePropertyByName
from Game.FactoryGame.Equipment.Beacon.UI.Widget_Beacon import ExecuteUbergraph_Widget_Beacon.K2Node_ComponentBoundEvent_CommitMethod
from Script.Engine import FormatArgumentData
from Script.UMG import SetText
from Game.FactoryGame.Equipment.Beacon.UI.Widget_Beacon import ExecuteUbergraph_Widget_Beacon
from Game.FactoryGame.Equipment.Beacon.UI.Widget_Beacon import ExecuteUbergraph_Widget_Beacon.K2Node_CustomEvent_Color
from Script.Engine import EqualEqual_StriStri
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.FactoryGame import FGInteractWidget
from Script.UMG import Construct
from Script.Engine import BooleanOR
from Script.Engine import Format
from Script.UMG import GetText
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.UMG import GetOwningPlayerPawn
from Script.Engine import EqualEqual_TextText
from Game.FactoryGame.Equipment.Beacon.UI.Widget_Beacon import ExecuteUbergraph_Widget_Beacon.K2Node_CustomEvent_New_Color
from Script.UMG import Create
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Script.FactoryGame import FGActorRepresentation
from Game.FactoryGame.Equipment.Beacon.BP_Beacon import BP_Beacon
from Script.UMG import AddChildToOverlay

class Widget_Beacon(FGInteractWidget):
    mBeacon: Ptr[BP_Beacon]
    mFinalText: FText
    actorRepresentation: Ptr[FGActorRepresentation]
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    
    def SetBeaconColor(self, Color: LinearColor):
        GetInterfaceUObject(self.mBeacon).SetActorRepresentationColor(Color)
    

    def SetBeaconText(self, text: FText):
        
        ReturnValue: FText = GetInterfaceUObject(self.mBeacon).SetActorRepresentationText(Ref[text])
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Beacon(10)
    

    def BndEvt__mColorButton_K2Node_ComponentBoundEvent_115_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Beacon(1163)
    

    def OnColorPicked(self, Color: LinearColor):
        ExecuteUbergraph_Widget_Beacon.K2Node_CustomEvent_Color = Color #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Beacon(1453)
    

    def BndEvt__Widget_Window_K2Node_ComponentBoundEvent_0_OnClose__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Beacon(1897)
    

    def OnPickup(self):
        self.ExecuteUbergraph_Widget_Beacon(1916)
    

    def BndEvt__mTowerName_K2Node_ComponentBoundEvent_1_OnEditableTextCommittedEvent__DelegateSignature(self, text: Const[Ref[FText]], CommitMethod: uint8):
        ExecuteUbergraph_Widget_Beacon.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Beacon.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Beacon(1921)
    

    def UpdateColor(self, New Color: LinearColor):
        ExecuteUbergraph_Widget_Beacon.K2Node_CustomEvent_New_Color = New Color #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Beacon(3284)
    

    def ExecuteUbergraph_Widget_Beacon(self):
        self.Construct()
        OutputDelegate.BindUFunction(self, OnPickup)
        self.Widget_GlowingFactoryButton.mButton.OnClicked.AddUnique(OutputDelegate)
        OutputDelegate1.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate1)
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mBeaconName.SetUserFocus(ReturnValue2)
        ReturnValue: FText = self.mBeacon.GetActorRepresentationText()
        
        ReturnValue_0: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue])
        ReturnValue_1: bool = Default__KismetStringLibrary.EqualEqual_StriStri(ReturnValue_0, "")
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_StringToText("Beacon")
        
        ReturnValue_3: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[ReturnValue], Ref[ReturnValue_2])
        ReturnValue1: bool = BooleanOR(ReturnValue_1, ReturnValue_3)
        if not ReturnValue1:
            goto('L658')
        self.Widget_Window_DarkMode.SetTitle("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 608, 'Value': 'Beacon'}")
        # End
        # Label 658
        self.mBeaconName.SetText(ReturnValue)
        ReturnValue_4: FText = self.mBeaconName.GetText()
        self.mFinalText = ReturnValue_4
        FormatArgumentData1.ArgumentName = "BeaconName"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = self.mFinalText
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData1]
        ReturnValue1_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1044, 'Value': 'Beacon - {BeaconName}'}", Array1)
        self.Widget_Window_DarkMode.SetTitle(ReturnValue1_0)
        # End
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: Ptr[Widget_ColorPicker_SingleColor] = Default__WidgetBlueprintLibrary.Create(self, Widget_ColorPicker_SingleColor, ReturnValue3)
        
        self.mBeacon.mCompassColor = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_5, "StartColor", Ref[self.mBeacon.mCompassColor])
        ReturnValue_6: Ptr[OverlaySlot] = self.mColorPickerContainer.AddChildToOverlay(ReturnValue_5)
        OutputDelegate2.BindUFunction(self, UpdateColor)
        ReturnValue_5.OnClose.AddUnique(OutputDelegate2)
        # End
        self.SetBeaconColor(Color)
        self.SetVisibility(0)
        # End
        # Label 1511
        ReturnValue_7: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_7)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L3307')
        ReturnValue_8: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_8)
        bSuccess1: bool = Player
        if not bSuccess1:
            goto('L3307')
        ReturnValue_9: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_9.ServerPickUpBeacon(self.mBeacon, Player)
        # End
        # Label 1823
        ReturnValue1_1: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mBeacon.CloseWidget(ReturnValue1_1)
        goto('L1511')
        self.OnEscapePressed()
        # End
        goto('L1823')
        ReturnValue_10: bool = EqualEqual_ByteByte(CommitMethod, 1)
        ReturnValue1_2: bool = EqualEqual_ByteByte(CommitMethod, 2)
        ReturnValue_11: bool = BooleanOR(ReturnValue_10, ReturnValue1_2)
        if not ReturnValue_11:
            goto('L2983')
        self.mFinalText = Text
        Variable2: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2082, 'Value': 'Beacon'}"
        
        ReturnValue_12: bool = Default__KismetTextLibrary.TextIsEmpty(Ref[self.mFinalText])
        Variable2_0: bool = ReturnValue_12
        
        switch = {
            False: self.mFinalText,
            True: Variable2
        }
        self.SetBeaconText(switch.get(Variable2_0, None))
        FormatArgumentData.ArgumentName = "BeaconName"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = self.mFinalText
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_13: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2531, 'Value': 'Beacon: {BeaconName}'}", Array)
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2619, 'Value': 'Beacon'}"
        ReturnValue2_0: FText = Default__KismetTextLibrary.Conv_StringToText("Beacon")
        
        ReturnValue2_1: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[self.mFinalText], Ref[ReturnValue2_0])
        
        ReturnValue_12 = Default__KismetTextLibrary.TextIsEmpty(Ref[self.mFinalText])
        ReturnValue2_2: bool = BooleanOR(ReturnValue_12, ReturnValue2_1)
        Variable1_0: bool = ReturnValue2_2
        
        switch_0 = {
            False: ReturnValue_13,
            True: Variable1
        }
        self.Widget_Window_DarkMode.SetTitle(switch_0.get(Variable1_0, None))
        # End
        # Label 2983
        ReturnValue1_3: FText = self.mBeacon.GetActorRepresentationText()
        Variable: FText = 
        ReturnValue1_4: FText = Default__KismetTextLibrary.Conv_StringToText("Beacon")
        
        ReturnValue1_5: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[ReturnValue1_3], Ref[ReturnValue1_4])
        Variable_0: bool = ReturnValue1_5
        
        switch_1 = {
            False: ReturnValue1_3,
            True: Variable
        }
        self.mBeaconName.SetText(switch_1.get(Variable_0, None))
        # End
        self.SetBeaconColor(Color)
    
