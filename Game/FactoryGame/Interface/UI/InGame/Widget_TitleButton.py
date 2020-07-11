
from codegen.ue4_stub import *

from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGTitleButton
from Script.UMG import IsPressed
from Script.UMG import Destruct
from Script.Engine import Pawn
from Game.FactoryGame.Interface.UI.InGame.Widget_TitleButton import ExecuteUbergraph_Widget_TitleButton
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_MouseOver import Play_UI_WorkBench_MouseOver
from Script.AkAudio import AkComponent
from Script.UMG import WidgetAnimation
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import SetButton
from Script.CoreUObject import LinearColor
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_Select import Play_UI_WorkBench_Select

class Widget_TitleButton(FGTitleButton):
    HoverForList: Ptr[WidgetAnimation]
    hover: Ptr[WidgetAnimation]
    OnClicked: FMulticastScriptDelegate
    OnPressed: FMulticastScriptDelegate
    OnReleased: FMulticastScriptDelegate
    bIsFocusable = True
    
    def GetButtonHoverColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue: bool = self.mButton.IsHovered()
        Variable: bool = ReturnValue
        
        switch = {
            False: Graphics,
            True: Orange
        }
        ReturnValue_0: LinearColor = switch.get(Variable, None)
    

    def GetCrossHoverColor(self):
        ReturnValue: bool = self.mButton.IsHovered()
        if not ReturnValue:
            goto('L60')
        # Label 60
        ReturnValue_0: bool = self.mButton.IsPressed()
        if not ReturnValue_0:
            goto('L116')
        
        TextWhite = None
        GraphicsWhite = None
        # Label 116
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_1: LinearColor = GraphicsWhite
    

    def BndEvt__Button_26_K2Node_ComponentBoundEvent_100_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TitleButton(15)
    

    def BndEvt__Button_26_K2Node_ComponentBoundEvent_597_OnButtonPressedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TitleButton(120)
    

    def BndEvt__Button_26_K2Node_ComponentBoundEvent_642_OnButtonReleasedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TitleButton(144)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_TitleButton(168)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_4_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TitleButton(192)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_TitleButton(278)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_3_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TitleButton(10)
    

    def ExecuteUbergraph_Widget_TitleButton(self):
        # End
        self.OnClicked.ProcessMulticastDelegate()
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_Select, ReturnValue, True)
        # End
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
    

    def OnReleased__DelegateSignature(self):
        pass
    

    def OnPressed__DelegateSignature(self):
        pass
    

    def OnClicked__DelegateSignature(self):
        pass
    
