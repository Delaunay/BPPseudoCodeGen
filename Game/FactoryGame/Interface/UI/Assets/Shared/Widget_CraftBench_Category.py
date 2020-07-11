
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Script.Engine import Pawn
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_MouseOver import Play_UI_WorkBench_MouseOver
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.FactoryGame import SetButton
from Game.FactoryGame.Interface.UI.Assets.Shared.Widget_CraftBench_Category import ExecuteUbergraph_Widget_CraftBench_Category
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_Select import Play_UI_WorkBench_Select
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import SetHorizontalAlignment
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.Assets.Shared.Widget_CraftBench_Category import ExecuteUbergraph_Widget_CraftBench_Category.K2Node_Event_IsDesignTime
from Script.UMG import SetColorAndOpacity
from Script.UMG import Destruct
from Script.UMG import AddChildToWrapBox
from Script.SlateCore import SlateFontInfo
from Script.FactoryGame import FGButtonWidget
from Script.UMG import SetFont
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import WrapBoxSlot
from Game.FactoryGame.Interface.UI.Assets.BuildMenu.Minus import Minus
from Game.FactoryGame.Interface.UI.Assets.BuildMenu.Plus import Plus
from Script.UMG import GetOwningPlayerPawn
from Script.UMG import SetStyle
from Script.AkAudio import AkComponent
from Script.CoreUObject import LinearColor

class Widget_CraftBench_Category(FGButtonWidget):
    OnClicked: FMulticastScriptDelegate
    mText: FText = NSLOCTEXT("", "7CBE572F439FDED4F73BD88C1E4405BE", "Enter Text Here")
    OnPressed: FMulticastScriptDelegate
    OnReleased: FMulticastScriptDelegate
    mIsCollapsed: bool
    mHasAffordableRecipes: bool
    Font: SlateFontInfo = Namespace(FontMaterial={'$Empty': True}, FontObject={'$AssetPath': '/Game/FactoryGame/Interface/Font/DescriptionText.DescriptionText'}, OutlineSettings={'OutlineSize': 0, 'bSeparateFillAlpha': False, 'bApplyOutlineToDropShadows': False, 'OutlineMaterial': {'$Empty': True}, 'OutlineColor': {'R': 0, 'G': 0, 'B': 0, 'A': 1}}, Size=0, TypefaceFontName='Bold')
    mHideIfUnaffordable: bool
    bIsFocusable = True
    
    def AddChildToContentWrapped(self, Child: Ptr[Widget]):
        ReturnValue: Ptr[WrapBoxSlot] = self.mContentWrapped.AddChildToWrapBox(Child)
        ReturnValue.SetHorizontalAlignment(1)
        self.mContentWrapped.SetVisibility(0)
    

    def SetHasAffordableRecipes(self, mHasAffordableRecipes: bool):
        self.mHasAffordableRecipes = mHasAffordableRecipes
        Variable: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        Variable1: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 0.5)
        Variable2: bool = self.mHasAffordableRecipes
        
        switch = {
            False: Variable1,
            True: Variable
        }
        SlateColor.SpecifiedColor = switch.get(Variable2, None)
        SlateColor.ColorUseRule = 0
        self.mButtonText.SetColorAndOpacity(SlateColor)
        Variable_0: FName = "SemiBold"
        Variable1_0: FName = "Regular"
        Variable1_1: bool = self.mHasAffordableRecipes
        SlateFontInfo.FontObject = self.mButtonText.Font.FontObject
        SlateFontInfo.FontMaterial = self.mButtonText.Font.FontMaterial
        SlateFontInfo.OutlineSettings = self.mButtonText.Font.OutlineSettings
        
        switch_0 = {
            False: Variable1_0,
            True: Variable_0
        }
        SlateFontInfo.TypefaceFontName = switch_0.get(Variable1_1, None)
        SlateFontInfo.Size = self.mButtonText.Font.Size
        self.mButtonText.SetFont(SlateFontInfo)
        Variable_1: uint8 = 1
        Variable1_2: uint8 = 4
        ReturnValue: bool = Not_PreBool(self.mHasAffordableRecipes)
        ReturnValue_0: bool = self.mHideIfUnaffordable and ReturnValue
        Variable_2: bool = ReturnValue_0
        
        switch_1 = {
            False: Variable1_2,
            True: Variable_1
        }
        self.mContainer.SetVisibility(switch_1.get(Variable_2, None))
    

    def SetIsCollapsed(self, mIsCollapsed: bool):
        self.mIsCollapsed = mIsCollapsed
        if not self.mIsCollapsed:
            goto('L207')
        self.mContentVertical.SetVisibility(1)
        self.mContentWrapped.SetVisibility(1)
        self.mExpandIcon.SwitchImage(Plus)
        self.UpdateButtonColor(LinearColor(R = 0.09530699998140335, G = 0.09530699998140335, B = 0.09530699998140335, A = 0.5))
        # End
        # Label 207
        self.mContentVertical.SetVisibility(4)
        self.mContentWrapped.SetVisibility(4)
        self.mExpandIcon.SwitchImage(Minus)
        self.UpdateButtonColor(LinearColor(R = 0.09530699998140335, G = 0.09530699998140335, B = 0.09530699998140335, A = 1))
    

    def UpdateButtonColor(self, Color: LinearColor):
        SlateColor.SpecifiedColor = Color
        SlateColor.ColorUseRule = 0
        SlateBrush.ImageSize = self.mButton.WidgetStyle.Normal.ImageSize
        SlateBrush.Margin = self.mButton.WidgetStyle.Normal.Margin
        SlateBrush.TintColor = SlateColor
        SlateBrush.ResourceObject = self.mButton.WidgetStyle.Normal.ResourceObject
        SlateBrush.DrawAs = self.mButton.WidgetStyle.Normal.DrawAs
        SlateBrush.Tiling = self.mButton.WidgetStyle.Normal.Tiling
        SlateBrush.Mirroring = self.mButton.WidgetStyle.Normal.Mirroring
        ButtonStyle.Normal = SlateBrush
        ButtonStyle.Hovered = self.mButton.WidgetStyle.Hovered
        ButtonStyle.Pressed = self.mButton.WidgetStyle.Pressed
        ButtonStyle.Disabled = self.mButton.WidgetStyle.Disabled
        ButtonStyle.NormalPadding = self.mButton.WidgetStyle.NormalPadding
        ButtonStyle.PressedPadding = self.mButton.WidgetStyle.PressedPadding
        ButtonStyle.PressedSlateSound = self.mButton.WidgetStyle.PressedSlateSound
        ButtonStyle.HoveredSlateSound = self.mButton.WidgetStyle.HoveredSlateSound
        
        ButtonStyle = None
        self.mButton.SetStyle(Ref[ButtonStyle])
    

    def AddChildToContentVertical(self, Child: Ptr[Widget]):
        ReturnValue: Ptr[PanelSlot] = self.mContentVertical.AddChild(Child)
        self.mContentVertical.SetVisibility(0)
    

    def BndEvt__Button_26_K2Node_ComponentBoundEvent_100_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_CraftBench_Category(116)
    

    def BndEvt__Button_26_K2Node_ComponentBoundEvent_597_OnButtonPressedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_CraftBench_Category(270)
    

    def BndEvt__Button_26_K2Node_ComponentBoundEvent_642_OnButtonReleasedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_CraftBench_Category(290)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_CraftBench_Category(310)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_4_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_CraftBench_Category(330)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_CraftBench_Category(412)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_CraftBench_Category.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_CraftBench_Category(423)
    

    def ExecuteUbergraph_Widget_CraftBench_Category(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 92, UUID = -1723378143, ExecutionFunction = "ExecuteUbergraph_Widget_CraftBench_Category", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.SetIsCollapsed(self.mIsCollapsed)
        goto(ExecutionFlow.Pop())
        ReturnValue: bool = Not_PreBool(self.mIsCollapsed)
        self.SetIsCollapsed(ReturnValue)
        self.OnClicked.ProcessMulticastDelegate(self)
        ReturnValue_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_Select, ReturnValue_0, True)
        goto(ExecutionFlow.Pop())
        self.OnPressed.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
        self.OnReleased.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
        self.SetButton(self.mButton)
        goto(ExecutionFlow.Pop())
        ReturnValue1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_MouseOver, ReturnValue1, True)
        goto(ExecutionFlow.Pop())
        self.Destruct()
        goto(ExecutionFlow.Pop())
        self.mButtonText.SetText(self.mText)
        goto('L15')
    

    def OnReleased__DelegateSignature(self):
        pass
    

    def OnPressed__DelegateSignature(self):
        pass
    

    def OnClicked__DelegateSignature(self, Instigator: Ptr[Widget_CraftBench_Category]):
        pass
    
