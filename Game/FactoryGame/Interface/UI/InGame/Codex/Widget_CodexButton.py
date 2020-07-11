
from codegen.ue4_stub import *

from Script.FactoryGame import EMessageType
from Script.UMG import GetParent
from Script.Engine import Texture
from Script.AkAudio import PostAkEvent
from Script.Engine import Pawn
from Script.UMG import GetChildIndex
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_MouseOver import Play_UI_WorkBench_MouseOver
from Script.UMG import GetChildrenCount
from Script.Engine import TextIsEmpty
from Script.FactoryGame import SetButton
from Game.FactoryGame.Interface.UI.Assets.Shared.Tutorial_Icon import Tutorial_Icon
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_Select import Play_UI_WorkBench_Select
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_CodexButton import ExecuteUbergraph_Widget_CodexButton
from Script.UMG import GetChildAt
from Game.FactoryGame.Interface.UI.Assets.BuildMenu.Cross import Cross
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.Assets.Shared.Inbox_Icon import Inbox_Icon
from Script.UMG import Destruct
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.UMG import Widget
from Script.UMG import PanelWidget
from Script.FactoryGame import FGButtonWidget
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import NotEqual_ByteByte
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_CodexButton import Widget_CodexButton
from Script.SlateCore import SlateColor
from Script.AkAudio import AkComponent

class Widget_CodexButton(FGButtonWidget):
    OnClicked: FMulticastScriptDelegate
    mText: FText = NSLOCTEXT("", "A71FF4D44AC33FDC2A3FF2919308B01D", "Enter Text Here")
    OnPressed: FMulticastScriptDelegate
    OnReleased: FMulticastScriptDelegate
    mType: uint8
    ButtonTexture: Ptr[Texture]
    bIsFocusable = True
    
    def GetTextHoverColor(self):
        ReturnValue: bool = self.IsHovered()
        if not ReturnValue:
            goto('L125')
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_0: SlateColor = TextWhite
        goto('L207')
        
        Text = None
        Graphics = None
        # Label 125
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_0 = Text
    

    def GetMessageNotificationVisibility(self):
        Variable: uint8 = 2
        Variable1: uint8 = 4
        
        self.mMessageNotification.mText = None
        ReturnValue: bool = Default__KismetTextLibrary.TextIsEmpty(Ref[self.mMessageNotification.mText])
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_0: uint8 = switch.get(Variable_0, None)
    

    def BndEvt__Button_26_K2Node_ComponentBoundEvent_100_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_CodexButton(1551)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_CodexButton(1566)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_4_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_CodexButton(1690)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_CodexButton(1772)
    

    def Clicked(self):
        self.ExecuteUbergraph_Widget_CodexButton(1811)
    

    def ExecuteUbergraph_Widget_CodexButton(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L222")
        ReturnValue1: Ptr[PanelWidget] = self.GetParent()
        ReturnValue: Ptr[Widget] = ReturnValue1.GetChildAt(Variable)
        Button: Ptr[Widget_CodexButton] = Cast[Widget_CodexButton](ReturnValue)
        bSuccess: bool = Button
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Button.Widget_ImageTabButton.mForceActiveButton = False
        goto(ExecutionFlow.Pop())
        # Label 222
        ReturnValue_0: int32 = Variable + 1
        Variable: int32 = ReturnValue_0
        # Label 291
        ReturnValue_1: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_2: int32 = ReturnValue_1.GetChildrenCount()
        ReturnValue_3: bool = Variable <= ReturnValue_2
        if not ReturnValue_3:
            goto('L418')
        goto('L15')
        # Label 418
        self.Widget_ImageTabButton.mForceActiveButton = True
        self.OnClicked.ProcessMulticastDelegate(self)
        ReturnValue_4: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_Select, ReturnValue_4, True)
        goto(ExecutionFlow.Pop())
        # Label 553
        self.Widget_ImageTabButton.mForceActiveButton = True
        # Label 586
        self.SetButton(self.mButton)
        self.Widget_ImageTabButton.mButtonText = self.mText
        CmpSuccess: bool = NotEqual_ByteByte(self.mType, 0)
        if not CmpSuccess:
            goto('L790')
        CmpSuccess = NotEqual_ByteByte(self.mType, 1)
        if not CmpSuccess:
            goto('L1503')
        CmpSuccess = NotEqual_ByteByte(self.mType, 2)
        if not CmpSuccess:
            goto('L1527')
        goto(ExecutionFlow.Pop())
        # Label 790
        self.ButtonTexture = Inbox_Icon
        # Label 809
        SlateBrush.ImageSize = self.Widget_ImageTabButton.mIcon.Brush.ImageSize
        SlateBrush.Margin = self.Widget_ImageTabButton.mIcon.Brush.Margin
        SlateBrush.TintColor = self.Widget_ImageTabButton.mIcon.Brush.TintColor
        SlateBrush.ResourceObject = self.ButtonTexture
        SlateBrush.DrawAs = self.Widget_ImageTabButton.mIcon.Brush.DrawAs
        SlateBrush.Tiling = self.Widget_ImageTabButton.mIcon.Brush.Tiling
        SlateBrush.Mirroring = self.Widget_ImageTabButton.mIcon.Brush.Mirroring
        
        SlateBrush = None
        self.Widget_ImageTabButton.mIcon.SetBrush(Ref[SlateBrush])
        OutputDelegate.BindUFunction(self, Clicked)
        self.Widget_ImageTabButton.TabButtonClicked.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 1503
        self.ButtonTexture = Tutorial_Icon
        goto('L809')
        # Label 1527
        self.ButtonTexture = Cross
        goto('L809')
        self.Clicked()
        goto(ExecutionFlow.Pop())
        ReturnValue2: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_6: int32 = ReturnValue2.GetChildIndex(self)
        ReturnValue_7: bool = EqualEqual_IntInt(ReturnValue_6, 0)
        if not ReturnValue_7:
            goto('L586')
        goto('L553')
        ReturnValue1_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue1_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_MouseOver, ReturnValue1_0, True)
        goto(ExecutionFlow.Pop())
        self.Destruct()
        goto(ExecutionFlow.Pop())
        # Label 1783
        Variable = 0
        goto('L291')
        goto('L1783')
    

    def OnReleased__DelegateSignature(self):
        pass
    

    def OnPressed__DelegateSignature(self):
        pass
    

    def OnClicked__DelegateSignature(self, ButtonPressed: Ptr[Widget_CodexButton]):
        pass
    
