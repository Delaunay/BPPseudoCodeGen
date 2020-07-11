
from codegen.ue4_stub import *

from Script.Engine import PlayerController
from Game.FactoryGame.Interface.UI.InGame.Widget_PhotoMode import ExecuteUbergraph_Widget_PhotoMode
from Script.FactoryGame import GetIsPhotoMode
from Script.FactoryGame import GetPhotoModeFOV
from Script.Engine import FMin
from Script.FactoryGame import FGPlayerController
from Script.UMG import ESlateVisibility
from Script.FactoryGame import FormatStringWithKeyNames
from Script.Engine import EqualEqual_ByteByte
from Script.UMG import GetVisibility
from Script.UMG import SetRenderOpacity
from Game.FactoryGame.Interface.UI.InGame.Widget_PhotoMode import ExecuteUbergraph_Widget_PhotoMode.K2Node_Event_InDeltaTime
from Game.FactoryGame.Interface.UI.InGame.Widget_PhotoMode import ExecuteUbergraph_Widget_PhotoMode.K2Node_Event_MyGeometry
from Script.Engine import Conv_IntToFloat
from Script.FactoryGame import GetHiResPhotoModeEnabled
from Script.UMG import UserWidget
from Script.FactoryGame import Default__FGInputLibrary

class Widget_PhotoMode(UserWidget):
    OwningPlayerController: Ptr[FGPlayerController]
    VirtualTakenPhotoOpacity: float
    TakePhotoTextDuration: float = 5
    mIsGridVisible: bool
    
    def UpdateHiResToggle(self):
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': 'On'}"
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 80, 'Value': 'Off'}"
        ReturnValue: bool = self.OwningPlayerController.GetHiResPhotoModeEnabled()
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.VisibilityOnOffText.SetText(switch.get(Variable_0, None))
    

    def UpdateFOVSlider(self):
        ReturnValue: int32 = self.OwningPlayerController.GetPhotoModeFOV()
        ReturnValue_0: float = Conv_IntToFloat(ReturnValue)
        self.FoVSlider.SetNormalizedValue(ReturnValue_0)
    

    def SetInputKeyTexts(self):
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue3_0: FText = Default__FGInputLibrary.FormatStringWithKeyNames(ReturnValue3, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 84, 'Value': '{PrimaryFire}'}", False)
        self.TakePhotoInputKeyText.SetText(ReturnValue3_0)
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue2_0: FText = Default__FGInputLibrary.FormatStringWithKeyNames(ReturnValue2, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 266, 'Value': '{BuildGunScrollUp_PhotoModeFOVUp} / {BuildGunScrollDown_PhotoModeFOVDown}'}", True)
        self.FoVInputKeyText.SetText(ReturnValue2_0)
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: FText = Default__FGInputLibrary.FormatStringWithKeyNames(ReturnValue1, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 508, 'Value': '{PhotoMode} or ESC'}", False)
        self.ExitPhotoModeInputKeyText.SetText(ReturnValue1_0)
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: FText = Default__FGInputLibrary.FormatStringWithKeyNames(ReturnValue, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 695, 'Value': '{SecondaryFire}'}", False)
        self.ToggleHiResInputKeyText.SetText(ReturnValue_0)
        self.ToggleVisInputKeyText.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 832, 'Value': 'Middle Mouse Button'}")
    

    def ToggleVisibility(self):
        Variable: uint8 = 0
        Variable1: uint8 = 2
        ReturnValue: uint8 = self.GetVisibility()
        ReturnValue_0: bool = self.OwningPlayerController.GetIsPhotoMode()
        ReturnValue_1: bool = EqualEqual_ByteByte(ReturnValue, 2)
        ReturnValue_2: bool = ReturnValue_0 and ReturnValue_1
        Variable_0: bool = ReturnValue_2
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.SetVisibility(switch.get(Variable_0, None))
    

    def FadePhotoTakenText(self, DeltaTime: float):
        ReturnValue: float = self.VirtualTakenPhotoOpacity * 2
        ReturnValue1: float = DeltaTime * ReturnValue
        ReturnValue_0: float = self.VirtualTakenPhotoOpacity - ReturnValue1
        self.VirtualTakenPhotoOpacity = ReturnValue_0
        ReturnValue_1: float = FMin(self.VirtualTakenPhotoOpacity, 1)
        self.photosavedtext.SetRenderOpacity(ReturnValue_1)
    

    def PhotoTaken(self):
        self.VirtualTakenPhotoOpacity = self.TakePhotoTextDuration
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_PhotoMode(29)
    

    def Tick(self):
        ExecuteUbergraph_Widget_PhotoMode.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_PhotoMode.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PhotoMode(170)
    

    def ExecuteUbergraph_Widget_PhotoMode(self):
        # Label 10
        self.UpdateHiResToggle()
        # End
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L212')
        self.OwningPlayerController = Controller
        self.SetInputKeyTexts()
        # End
        self.FadePhotoTakenText(InDeltaTime)
        self.UpdateFOVSlider()
        goto('L10')
    
