
from codegen.ue4_stub import *

from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.InGame.Widget_Button import ExecuteUbergraph_Widget_Button
from Script.AkAudio import PostAkEvent
from Script.UMG import Destruct
from Script.FactoryGame import FGButtonWidget
from Script.Engine import Pawn
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_MouseOver import Play_UI_WorkBench_MouseOver
from Script.AkAudio import AkComponent
from Script.UMG import WidgetAnimation
from Script.UMG import GetIsEnabled
from Script.FactoryGame import SetButton
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_Select import Play_UI_WorkBench_Select

class Widget_Button(FGButtonWidget):
    HoverForList: Ptr[WidgetAnimation]
    hover: Ptr[WidgetAnimation]
    OnClicked: FMulticastScriptDelegate
    mText: FText = NSLOCTEXT("", "F2CB693C4430FCD8AAF03EB13CDE5185", "Enter Text Here")
    OnPressed: FMulticastScriptDelegate
    OnReleased: FMulticastScriptDelegate
    isTab: bool
    isAccordion: bool
    OnClickedWithRef: FMulticastScriptDelegate
    padding = Namespace(Bottom=2, Left=2, Right=2, Top=2)
    bIsFocusable = True
    
    def GetAccordionFeedbackVisibility(self):
        if not self.isAccordion:
            goto('L39')
        ReturnValue = 0
        goto('L59')
        # Label 39
        ReturnValue = 1
    

    def GetButtonEnabled(self):
        ReturnValue: bool = self.GetIsEnabled()
        ReturnValue_0: bool = ReturnValue
    

    def BndEvt__Button_26_K2Node_ComponentBoundEvent_100_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Button(135)
    

    def BndEvt__Button_26_K2Node_ComponentBoundEvent_597_OnButtonPressedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Button(140)
    

    def BndEvt__Button_26_K2Node_ComponentBoundEvent_642_OnButtonReleasedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Button(164)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Button(188)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_4_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Button(212)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_Button(298)
    

    def ExecuteUbergraph_Widget_Button(self):
        # Label 10
        self.OnClickedWithRef.ProcessMulticastDelegate(self)
        self.OnClicked.ProcessMulticastDelegate()
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_Select, ReturnValue, True)
        # End
        goto('L10')
        self.OnPressed.ProcessMulticastDelegate()
        # End
        self.OnReleased.ProcessMulticastDelegate()
        # End
        self.SetButton(self.mButton)
        # End
        ReturnValue1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_MouseOver, ReturnValue1, True)
        # End
        self.Destruct()
    

    def OnClickedWithRef__DelegateSignature(self, ClickedButton: Ptr[Widget_Button]):
        pass
    

    def OnReleased__DelegateSignature(self):
        pass
    

    def OnPressed__DelegateSignature(self):
        pass
    

    def OnClicked__DelegateSignature(self):
        pass
    
