
from codegen.ue4_stub import *

from Script.FactoryGame import FGWindow
from Game.FactoryGame.Interface.UI.Menu.Widget_Menu_Window import ExecuteUbergraph_Widget_Menu_Window
from Script.Engine import PlayerController
from Script.Engine import BooleanOR
from Script.AkAudio import PostAkEvent
from Script.UMG import Construct
from Script.UMG import HasAnyChildren
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_MouseOver import Play_UI_MainMenu_MouseOver
from Script.AkAudio import AkComponent
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_Back import Play_UI_MainMenu_Back
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Interface.UI.Menu.Widget_Menu_Window import ExecuteUbergraph_Widget_Menu_Window.K2Node_Event_IsDesignTime

class Widget_Menu_Window(FGWindow):
    mText: FText
    
    def GetButtonSlotVisibility(self):
        ReturnValue: bool = self.mButtonSlot.HasAnyChildren()
        if not ReturnValue:
            goto('L99')
        self.mButtonSlotOverlay.SetVisibility(0)
        # End
        # Label 99
        self.mButtonSlotOverlay.SetVisibility(1)
    

    def GetVisibility_0(self):
        ReturnValue: bool = self.OptionsContentRight.HasAnyChildren()
        ReturnValue1: bool = self.OptionsContentLeft.HasAnyChildren()
        ReturnValue_0: bool = BooleanOR(ReturnValue1, ReturnValue)
        if not ReturnValue_0:
            goto('L161')
        ReturnValue_1: uint8 = 4
        goto('L181')
        # Label 161
        ReturnValue_1 = 1
    

    def GetContentLeftVisibility(self):
        ReturnValue: bool = self.OptionsContentLeft.HasAnyChildren()
        if not ReturnValue:
            goto('L81')
        ReturnValue_0: uint8 = 0
        goto('L101')
        # Label 81
        ReturnValue_0 = 1
    

    def GetWideContentSlotVisibility(self):
        ReturnValue: bool = self.mWideContentSlot.HasAnyChildren()
        if not ReturnValue:
            goto('L81')
        ReturnValue_0: uint8 = 0
        goto('L101')
        # Label 81
        ReturnValue_0 = 1
    

    def GetContentRightVisibility(self):
        Variable: uint8 = 0
        Variable1: uint8 = 1
        ReturnValue: bool = self.OptionsContentRight.HasAnyChildren()
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        # Label 101
        ReturnValue_0: uint8 = switch.get(Variable_0, None)
    

    def BndEvt__mCloseButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Menu_Window(10)
    

    def BndEvt__mCloseButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Menu_Window(100)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Menu_Window(190)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_Menu_Window.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Menu_Window(219)
    

    def ExecuteUbergraph_Widget_Menu_Window(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Back, ReturnValue, True)
        # End
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_MouseOver, ReturnValue1, True)
        # End
        self.Construct()
        self.GetButtonSlotVisibility()
        # End
        self.Widget_Window_DarkMode.SetTitle(self.mText)
    
