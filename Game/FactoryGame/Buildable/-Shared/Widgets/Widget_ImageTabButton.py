
from codegen.ue4_stub import *

from Script.UMG import GetParent
from Script.Engine import Texture2D
from Script.AkAudio import PostAkEvent
from Script.Engine import K2_SetTimerDelegate
from Script.UMG import WidgetSwitcher
from Script.Engine import Pawn
from Script.UMG import GetChildIndex
from Script.Engine import Not_PreBool
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_Select import Play_UI_WorkBench_Select
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_ImageTabButton import ExecuteUbergraph_Widget_ImageTabButton.K2Node_Event_IsDesignTime
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.FactoryGame import GetAllWidgetsOfClassInHierarchy
from Script.UMG import GetIsEnabled
from Script.UMG import SetColorAndOpacity
from Game.FactoryGame.Interface.UI.Audio.Play_UI_Inventory_MouseOver import Play_UI_Inventory_MouseOver
from Script.Engine import EqualEqual_IntInt
from Script.Engine import BooleanOR
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_ImageTabButton import ExecuteUbergraph_Widget_ImageTabButton
from Script.UMG import PanelWidget
from Script.FactoryGame import FGButtonWidget
from Script.UMG import GetActiveWidgetIndex
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.AkAudio import AkComponent
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.CoreUObject import LinearColor

class Widget_ImageTabButton(FGButtonWidget):
    mCachedTabSwitcher: Ptr[WidgetSwitcher]
    mIndexAsChild: int32
    mButtonText: FText
    mImageTexture: Ptr[Texture2D]
    TabButtonClicked: FMulticastScriptDelegate
    mForceActiveButton: bool
    mUpdateButtonTimer: TimerHandle
    bIsFocusable = True
    
    def UpdateButtonStyle(self):
        
        isSelected = None
        self.CheckIsSelected(Ref[isSelected])
        Variable: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 0)
        
        Text1 = None
        Graphics1 = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text1], Ref[Graphics1])
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue1: bool = self.IsHovered()
        Variable_0: bool = ReturnValue1
        Variable1: bool = isSelected
        
        switch = {
            False: Variable,
            True: Orange
        }
        
        switch_0 = {
            False: switch.get(Variable_0, None),
            True: Graphics1
        }
        self.mButtonBackground.SetColorAndOpacity(switch_0.get(Variable1, None))
        ReturnValue: bool = self.IsHovered()
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_0: bool = BooleanOR(isSelected, ReturnValue)
        Variable2: bool = ReturnValue_0
        
        switch_1 = {
            False: Text,
            True: TextWhite
        }
        self.ButtonText.SetColorAndOpacity(switch_1.get(Variable2, None))
        ReturnValue = self.IsHovered()
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_0 = BooleanOR(isSelected, ReturnValue)
        Variable3: bool = ReturnValue_0
        
        switch_2 = {
            False: Graphics,
            True: GraphicsWhite
        }
        self.mIcon.SetColorAndOpacity(switch_2.get(Variable3, None))
    

    def CheckIsSelected(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mCachedTabSwitcher)
        if not ReturnValue:
            goto('L210')
        ReturnValue_0: int32 = self.mCachedTabSwitcher.GetActiveWidgetIndex()
        ReturnValue_1: bool = EqualEqual_IntInt(ReturnValue_0, self.mIndexAsChild)
        ReturnValue_2: bool = BooleanOR(ReturnValue_1, self.mForceActiveButton)
        isSelected = ReturnValue_2
    

    def SetIcon(self):
        SlateBrush.ImageSize = self.mIcon.Brush.ImageSize
        SlateBrush.Margin = self.mIcon.Brush.Margin
        SlateBrush.TintColor = self.mIcon.Brush.TintColor
        SlateBrush.ResourceObject = self.mImageTexture
        SlateBrush.DrawAs = self.mIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mIcon.Brush.Tiling
        SlateBrush.Mirroring = self.mIcon.Brush.Mirroring
        
        SlateBrush = None
        self.mIcon.SetBrush(Ref[SlateBrush])
    

    def GetButtonEnabled(self):
        ReturnValue: bool = self.GetIsEnabled()
        ReturnValue_0: bool = ReturnValue
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ImageTabButton(700)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_32_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ImageTabButton(705)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ImageTabButton(851)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_ImageTabButton.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ImageTabButton(952)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_ImageTabButton(957)
    

    def ExecuteUbergraph_Widget_ImageTabButton(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L110")
        
        foundWidgets = None
        Item = None
        Item = foundWidgets[Variable]
        self.mCachedTabSwitcher = Item
        Variable: bool = True
        goto(ExecutionFlow.Pop())
        # Label 110
        ReturnValue: int32 = Variable_0 + 1
        Variable_0: int32 = ReturnValue
        # Label 179
        ReturnValue_0: bool = Not_PreBool(Variable)
        
        foundWidgets = None
        ReturnValue_1: int32 = len(foundWidgets)
        ReturnValue_2: bool = Variable_0 <= ReturnValue_1
        ReturnValue_3: bool = ReturnValue_0 and ReturnValue_2
        if not ReturnValue_3:
            goto('L389')
        Variable = Variable_0
        goto('L15')
        # Label 389
        ReturnValue_4: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_5: int32 = ReturnValue_4.GetChildIndex(self)
        self.mIndexAsChild = ReturnValue_5
        goto(ExecutionFlow.Pop())
        # Label 488
        OutputDelegate.BindUFunction(self, UpdateButtonStyle)
        ReturnValue_6: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.20000000298023224, True)
        foundWidgets: List[Ptr[WidgetSwitcher]] = []
        
        Default__FGBlueprintFunctionLibrary.GetAllWidgetsOfClassInHierarchy(self, WidgetSwitcher, Ref[foundWidgets])
        Variable = False
        Variable_0 = 0
        Variable = 0
        goto('L179')
        goto('L488')
        self.mCachedTabSwitcher.SetActiveWidgetIndex(self.mIndexAsChild)
        self.TabButtonClicked.ProcessMulticastDelegate()
        ReturnValue_7: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_8: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_Select, ReturnValue_7, True)
        goto(ExecutionFlow.Pop())
        ReturnValue_9: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_Inventory_MouseOver, ReturnValue_9, True)
        goto(ExecutionFlow.Pop())
        # Label 937
        self.SetIcon()
        goto(ExecutionFlow.Pop())
        goto('L937')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mUpdateButtonTimer])
        goto(ExecutionFlow.Pop())
    

    def TabButtonClicked__DelegateSignature(self):
        pass
    
