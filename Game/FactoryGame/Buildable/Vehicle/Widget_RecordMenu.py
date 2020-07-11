
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Script.Engine import Conv_StringToName
from Script.Engine import Texture
from Script.Engine import Sin
from Script.Engine import Conv_IntToFloat
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GetTAU
from Script.CoreUObject import Object
from Script.Engine import IsValid
from Script.UMG import Destruct
from Script.Engine import Cos
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import FGInteractWidget
from Script.UMG import Construct
from Script.UMG import Tick
from Game.FactoryGame.Interface.UI.InGame.-Shared.RadialMenu.Widget_RadialMenuButton import Widget_RadialMenuButton
from Script.UMG import Widget
from Game.FactoryGame.Buildable.Vehicle.Vehicle_RadialMenu.Vehicle_Icon_PauseRecoring import Vehicle_Icon_PauseRecoring
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import BP_WheeledVehicle
from Script.UMG import WidgetAnimation
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import GetPathVisibility
from Script.SlateCore import Geometry
from Game.FactoryGame.Buildable.Vehicle.Widget_RecordMenu import ExecuteUbergraph_Widget_RecordMenu.K2Node_Event_MyGeometry
from Game.FactoryGame.Buildable.Vehicle.Widget_RecordMenu import ExecuteUbergraph_Widget_RecordMenu.K2Node_Event_InDeltaTime
from Game.FactoryGame.Buildable.Vehicle.Widget_RecordMenu import ExecuteUbergraph_Widget_RecordMenu
from Script.CoreUObject import Vector2D

class Widget_RecordMenu(FGInteractWidget):
    SceneEnter: Ptr[WidgetAnimation]
    mRecordText: FText = NSLOCTEXT("", "0302F8894D2C0DD888934EBE22244BCE", "Start Recording")
    mStopRecordText: FText = NSLOCTEXT("", "40D24A1546C6329696346EADFC75402F", "Finish Recording")
    mVehicle: Ptr[BP_WheeledVehicle]
    mTitle: FText = NSLOCTEXT("", "F5B16D034BCD2EECA76551AD676E0F5E", "Recording menu")
    mPauseRecordingText: FText = NSLOCTEXT("", "A1181DB449A9BCEA538119AB8D7EE22E", "Pause recording")
    mResumeRecordingText: FText = NSLOCTEXT("", "3CD7B2ED483D47E7A9FFF9993B0141CE", "Resume recording")
    mEnableAutoPilotText: FText = NSLOCTEXT("", "E1F182D242224622D4612AA0608BD0C1", "Enable autopilot")
    mDisableAutoPilotText: FText = NSLOCTEXT("", "DE7897744F449E5A0D9D14B96DB496BF", "Disable autopilot")
    mShowPathText: FText = NSLOCTEXT("", "2E504B7D4B46BCFF140CBA86726865CE", "Show path nodes")
    mHidePathText: FText = NSLOCTEXT("", "CEC7CBAD48EBF8FC035A9EB4CD8E077F", "Hide path nodes")
    mAllButtons: List[Ptr[Object]]
    mCircleRadius: float = 300
    mSensitivity: float = 0.10000000149011612
    mClampedMousePos: Vector2D = Namespace(X=0.5, Y=0.800000011920929)
    mCancelText: FText = NSLOCTEXT("", "50DBD093453CA9739515E79FFAF1E416", "Cancel")
    mClearPathText: FText = NSLOCTEXT("", "90BAD17745F176A9F873B29B1ED68A59", "Clear Path")
    mActive: bool
    mRestoreFocusWhenLost = True
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    
    def SetNameAtIndex(self, Name: FText, int: int32):
        
        ReturnValue: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Name])
        ReturnValue_0: FName = Default__KismetStringLibrary.Conv_StringToName(ReturnValue)
        ReturnValue_1: Ptr[Widget] = self.Widget_RadialMenu.mContent.GetChildAt(int)
        Button: Ptr[Widget_RadialMenuButton] = Cast[Widget_RadialMenuButton](ReturnValue_1)
        bSuccess: bool = Button
        Button.Name = ReturnValue_0
        ReturnValue_1 = self.Widget_RadialMenu.mContent.GetChildAt(int)
        Button = Cast[Widget_RadialMenuButton](ReturnValue_1)
        bSuccess = Button
        Button.IconText.SetText(Name)
    

    def UpdateLabels(self):
        Variable3: bool = self.mVehicle.mIsRecordSessionActive
        
        switch = {
            False: self.mRecordText,
            True: self.mStopRecordText
        }
        self.SetNameAtIndex(switch.get(Variable3, None), 0)
        Variable1: bool = self.mVehicle.mIsAutoPilotEnabled
        
        switch_0 = {
            False: self.mEnableAutoPilotText,
            True: self.mDisableAutoPilotText
        }
        self.SetNameAtIndex(switch_0.get(Variable1, None), 2)
        ReturnValue: bool = self.mVehicle.GetPathVisibility()
        Variable: bool = ReturnValue
        
        switch_1 = {
            False: self.mShowPathText,
            True: self.mHidePathText
        }
        self.SetNameAtIndex(switch_1.get(Variable, None), 3)
        ReturnValue_0: bool = self.GetPauseEnabled()
        if not ReturnValue_0:
            goto('L510')
        Variable2: bool = self.mVehicle.mIsRecording
        
        switch_2 = {
            False: self.mResumeRecordingText,
            True: self.mPauseRecordingText
        }
        self.SetNameAtIndex(switch_2.get(Variable2, None), 5)
    

    def GetPositionInCircle(self, index: int32):
        ReturnValue: float = GetTAU()
        ReturnValue_0: float = Conv_IntToFloat(index)
        
        ReturnValue_1: int32 = len(self.mAllButtons)
        ReturnValue1: float = Conv_IntToFloat(ReturnValue_1)
        ReturnValue_2: float = ReturnValue1 / 4
        ReturnValue_3: float = ReturnValue_0 + ReturnValue_2
        ReturnValue1_0: float = ReturnValue_3 / ReturnValue1
        ReturnValue_4: float = ReturnValue1_0 * ReturnValue
        ReturnValue_5: float = Cos(ReturnValue_4)
        ReturnValue_6: float = Sin(ReturnValue_4)
        ReturnValue1_1: float = ReturnValue_5 * self.mCircleRadius
        ReturnValue2: float = self.mCircleRadius * ReturnValue_6
        ReturnValue_7: Vector2D = Vector2D(ReturnValue1_1, ReturnValue2)
        Translation = ReturnValue_7
    

    def GetPauseEnabled(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mVehicle)
        if not ReturnValue:
            goto('L111')
        ReturnValue_0: bool = self.mVehicle.mIsRecordSessionActive
        goto('L122')
        # Label 111
        ReturnValue_0 = False
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_RecordMenu(10)
    

    def ToggleRecording(self):
        self.ExecuteUbergraph_Widget_RecordMenu(329)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_RecordMenu(370)
    

    def ClearPathRecording(self):
        self.ExecuteUbergraph_Widget_RecordMenu(961)
    

    def PauseClicked(self):
        self.ExecuteUbergraph_Widget_RecordMenu(1125)
    

    def AutoPilotClicked(self):
        self.ExecuteUbergraph_Widget_RecordMenu(1130)
    

    def PathVisibilityClicked(self):
        self.ExecuteUbergraph_Widget_RecordMenu(1135)
    

    def Tick(self):
        ExecuteUbergraph_Widget_RecordMenu.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_RecordMenu.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_RecordMenu(1159)
    

    def ExecuteUbergraph_Widget_RecordMenu(self):
        self.Construct()
        ReturnValue: bool = self.GetPauseEnabled()
        if not ReturnValue:
            goto('L288')
        Variable: Const[FName] = "Resume recording"
        
        self.Widget_RadialMenu.Buttons = None
        ReturnValue1: int32 = self.Widget_RadialMenu.Buttons.append(Variable)
        Variable_0: Const[Ptr[Texture]] = Vehicle_Icon_PauseRecoring
        
        self.Widget_RadialMenu.mIconTextures = None
        ReturnValue_0: int32 = self.Widget_RadialMenu.mIconTextures.append(Variable_0)
        # Label 288
        self.Widget_RadialMenu.Create Radial Menu()
        # End
        self.mVehicle.ServerToggleRecording()
        # End
        self.Destruct()
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1.SetIgnoreLookInput(False)
        self.mVehicle.mIsMenuOpen = False
        self.mVehicle.ServerSetMenuOpen(False)
        CmpSuccess: bool = self.Widget_RadialMenu.SelectedInt != 0
        if not CmpSuccess:
            goto('L866')
        CmpSuccess = self.Widget_RadialMenu.SelectedInt != 2
        if not CmpSuccess:
            goto('L885')
        CmpSuccess = self.Widget_RadialMenu.SelectedInt != 3
        if not CmpSuccess:
            goto('L904')
        CmpSuccess = self.Widget_RadialMenu.SelectedInt != 4
        if not CmpSuccess:
            goto('L923')
        CmpSuccess = self.Widget_RadialMenu.SelectedInt != 5
        if not CmpSuccess:
            goto('L942')
        # End
        # Label 866
        self.ToggleRecording()
        # End
        # Label 885
        self.AutoPilotClicked()
        # End
        # Label 904
        self.PathVisibilityClicked()
        # End
        # Label 923
        self.ClearPathRecording()
        # End
        # Label 942
        self.PauseClicked()
        # End
        self.mVehicle.ServerClearPathRecording()
        # End
        # Label 1002
        self.mVehicle.ServerTogglePauseRecording()
        # End
        # Label 1043
        self.mVehicle.ServerToggleAutoPilot()
        # End
        # Label 1084
        self.mVehicle.ServerTogglePathVisibility()
        # End
        goto('L1002')
        goto('L1043')
        goto('L1084')
        # Label 1140
        self.UpdateLabels()
        # End
        self.Tick(Geometry(), 0)
        goto('L1140')
    
