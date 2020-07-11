
from codegen.ue4_stub import *

from Script.Engine import Delay
from Script.Engine import SetClassPropertyByName
from Script.Engine import EqualEqual_ByteByte
from Script.UMG import GetEndTime
from Script.FactoryGame import GetItemIcon
from Script.Engine import Default__KismetNodeHelperLibrary
from Script.Engine import SetBytePropertyByName
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import GetEnumeratorUserFriendlyName
from Game.FactoryGame.Interface.UI.InGame.MAMTree.MAMTree_NodeData_Struct import MAMTree_NodeData_Struct
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import EqualEqual_BoolBool
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.InGame.MAMTree.EMamTree_NodeStates import EMamTree_NodeStates
from Script.UMG import ESlateVisibility
from Script.UMG import SetRenderTranslation
from Game.FactoryGame.Interface.UI.InGame.MAMTree.Widget_MAMTree_Node import ExecuteUbergraph_Widget_MAMTree_Node
from Script.UMG import StopAnimation
from Script.Engine import IsValid
from Script.UMG import Open
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.Engine import SetBoolPropertyByName
from Script.Engine import BooleanOR
from Game.FactoryGame.Interface.UI.InGame.MAMTree.Widget_MAMTree_NodeInfo import Widget_MAMTree_NodeInfo
from Script.UMG import Widget
from Game.FactoryGame.Interface.UI.InGame.MAMTree.Widget_MAMTree_Node import ExecuteUbergraph_Widget_MAMTree_Node.K2Node_Event_IsDesignTime
from Script.UMG import WidgetAnimation
from Script.Engine import NotEqual_ByteByte
from Script.UMG import Close
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.InGame.MAMTree.Widget_MAMTree_Node import ExecuteUbergraph_Widget_MAMTree_Node.K2Node_ComponentBoundEvent_bIsOpen
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Script.FactoryGame import Default__FGSchematic
from Script.CoreUObject import Vector2D
from Script.SlateCore import SlateBrush
from Script.UMG import SetStyle
from Script.Engine import IsValidClass
from Script.CoreUObject import LinearColor

class Widget_MAMTree_Node(UserWidget):
    AvailableAnim: Ptr[WidgetAnimation]
    KeyAnim: Ptr[WidgetAnimation]
    UnlockAnim: Ptr[WidgetAnimation]
    mNodeData: MAMTree_NodeData_Struct
    OnClicked: FMulticastScriptDelegate
    mNodeState: uint8
    mIsSelected: bool
    OnHovered: FMulticastScriptDelegate
    OnUnhovered: FMulticastScriptDelegate
    mInfoWidget: Ptr[Widget_MAMTree_NodeInfo]
    mIsOtherSelected: bool
    OnResearchStarted: FMulticastScriptDelegate
    mShowUnlockIcon: bool
    mIsEditor: bool
    
    def Shine(self):
        self.Widget_ButtonShine.PlayShineAnim()
    

    def ShowHideKeyIcon(self, Show: bool):
        Variable: uint8 = 0
        Variable1: uint8 = 2
        Variable_0: bool = Show
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mKeyContainer.SetVisibility(switch.get(Variable_0, None))
        if not Show:
            goto('L213')
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.KeyAnim, 0, 0, 0, 1)
        # End
        # Label 213
        self.StopAnimation(self.KeyAnim)
    

    def ShowHideUnlockIcon(self, Show: bool):
        ReturnValue: bool = EqualEqual_BoolBool(Show, False)
        if not ReturnValue:
            goto('L55')
        self.mShowUnlockIcon = False
        # Label 55
        Variable: uint8 = 0
        Variable1: uint8 = 2
        ReturnValue1: bool = Show and self.mShowUnlockIcon
        Variable_0: bool = ReturnValue1
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mUnlockContainer.SetVisibility(switch.get(Variable_0, None))
        ReturnValue_0: bool = Show and self.mShowUnlockIcon
        if not ReturnValue_0:
            goto('L339')
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.UnlockAnim, 0, 1, 0, 1)
    

    def SetButtonNormalColor(self, Color: LinearColor):
        SlateColor.SpecifiedColor = Color
        SlateColor.ColorUseRule = 0
        # Label 65
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
    

    def SetNodeState(self, State: uint8):
        if not self.mIsEditor:
            goto('L436')
        self.mNodeState = 0
        # Label 34
        ReturnValue: FString = Default__KismetNodeHelperLibrary.GetEnumeratorUserFriendlyName(EMamTree_NodeStates, self.mNodeState)
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue)
        self.mState.SetText(ReturnValue_0)
        CmpSuccess: bool = NotEqual_ByteByte(self.mNodeState, 0)
        if not CmpSuccess:
            goto('L468')
        CmpSuccess = NotEqual_ByteByte(self.mNodeState, 1)
        if not CmpSuccess:
            goto('L813')
        CmpSuccess = NotEqual_ByteByte(self.mNodeState, 2)
        if not CmpSuccess:
            goto('L1234')
        CmpSuccess = NotEqual_ByteByte(self.mNodeState, 3)
        if not CmpSuccess:
            goto('L1542')
        CmpSuccess = NotEqual_ByteByte(self.mNodeState, 4)
        if not CmpSuccess:
            goto('L1860')
        # End
        # Label 436
        self.mNodeState = State
        goto('L34')
        # Label 468
        self.mIcon.SetVisibility(0)
        self.mGlow.SetVisibility(0)
        self.mNodeBorder.SetVisibility(0)
        self.mNodeShadow.SetVisibility(0)
        self.mInProgressBackground.SetVisibility(2)
        self.mContainer.SetRenderTranslation(Vector2D(X = -1, Y = -1))
        self.SetButtonNormalColor(LinearColor(R = 0.6038280129432678, G = 0.5972020030021667, B = 0.5972020030021667, A = 1))
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.AvailableAnim, 0, 0, 0, 1)
        # End
        # Label 813
        self.mIcon.SetVisibility(0)
        self.mNodeBorder.SetVisibility(0)
        self.mNodeShadow.SetVisibility(2)
        self.mGlow.SetVisibility(2)
        self.mInProgressBackground.SetVisibility(2)
        self.mContainer.SetRenderTranslation(Vector2D(X = 0, Y = 0))
        LinearColor.R = 0.15000000596046448
        LinearColor.G = 0.15000000596046448
        LinearColor.B = 0.15000000596046448
        LinearColor.A = 1
        self.SetButtonNormalColor(LinearColor)
        self.StopAnimation(self.AvailableAnim)
        # End
        # Label 1234
        self.mButton.SetVisibility(2)
        self.mGlow.SetVisibility(2)
        self.mNodeShadow.SetVisibility(2)
        self.mNodeBorder.SetVisibility(2)
        self.mInProgressBackground.SetVisibility(2)
        self.mResearchedButton.SetVisibility(0)
        self.mContainer.SetRenderTranslation(Vector2D(X = 0, Y = 0))
        self.StopAnimation(self.AvailableAnim)
        # End
        # Label 1542
        self.mIcon.SetVisibility(2)
        self.mGlow.SetVisibility(2)
        self.mNodeShadow.SetVisibility(2)
        self.mInProgressBackground.SetVisibility(2)
        self.mNodeBorder.SetVisibility(0)
        self.mContainer.SetRenderTranslation(Vector2D(X = 0, Y = 0))
        self.SetButtonNormalColor(LinearColor(R = 0.05729199945926666, G = 0.05666299909353256, B = 0.05666299909353256, A = 1))
        self.StopAnimation(self.AvailableAnim)
        # End
        # Label 1860
        self.mInProgressBackground.SetVisibility(0)
        self.mNodeShadow.SetVisibility(0)
        self.mIcon.SetVisibility(0)
        self.mGlow.SetVisibility(0)
        self.mNodeBorder.SetVisibility(0)
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        self.SetButtonNormalColor(Orange)
        self.mContainer.SetRenderTranslation(Vector2D(X = -1, Y = -1))
    

    def OnMenuOpen(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_MAMTree_NodeInfo] = Default__WidgetBlueprintLibrary.Create(self, Widget_MAMTree_NodeInfo, ReturnValue)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_0, "mSchematic", self.mNodeData.Schematic_27_3663A42446FDB4387D0C81AFC23E225B)
        Default__KismetSystemLibrary.SetBytePropertyByName(ReturnValue_0, "mNodeState", self.mNodeState)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_0, "mIsNodeSelected", self.mIsSelected)
        ReturnValue_0.SetVisibility(0)
        OutputDelegate.BindUFunction(self, OnResearchButtonPressed)
        ReturnValue_0.OnClicked.AddUnique(OutputDelegate)
        self.mInfoWidget = ReturnValue_0
        ReturnValue_1: Ptr[Widget] = self.mInfoWidget
    

    def SetIsSelected(self, mIsSelected: bool):
        self.mIsSelected = mIsSelected
        Variable2: uint8 = 3
        Variable3: uint8 = 2
        Variable1: bool = self.mIsSelected
        
        switch = {
            False: Variable3,
            True: Variable2
        }
        self.mSelectedBorder.SetVisibility(switch.get(Variable1, None))
        Variable: uint8 = 0
        Variable1_0: uint8 = 3
        Variable_0: bool = self.mIsSelected
        
        switch_0 = {
            False: Variable1_0,
            True: Variable
        }
        self.mHoverMenuAnchor.SetVisibility(switch_0.get(Variable_0, None))
        if not self.mIsSelected:
            goto('L334')
        # End
        # Label 334
        self.CloseMenu()
    

    def UpdateNodeIcon(self, mNodeData: MAMTree_NodeData_Struct):
        self.mNodeData = mNodeData
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mNodeData.Schematic_27_3663A42446FDB4387D0C81AFC23E225B)
        if not ReturnValue:
            goto('L696')
        ReturnValue_0: SlateBrush = Default__FGSchematic.GetItemIcon(self.mNodeData.Schematic_27_3663A42446FDB4387D0C81AFC23E225B)
        SlateBrush.ImageSize = self.mIcon.Brush.ImageSize
        SlateBrush.Margin = self.mIcon.Brush.Margin
        SlateBrush.TintColor = self.mIcon.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue_0.ResourceObject
        SlateBrush.DrawAs = self.mIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mIcon.Brush.Tiling
        SlateBrush.Mirroring = self.mIcon.Brush.Mirroring
        
        SlateBrush = None
        self.mIcon.SetBrush(Ref[SlateBrush])
        self.mIcon.SetVisibility(3)
        # End
        # Label 696
        self.mIcon.SetVisibility(2)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_MAMTree_Node.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MAMTree_Node(570)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_MAMTree_Node(65)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_MAMTree_Node(347)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_MAMTree_Node(499)
    

    def BndEvt__mHoverMenuAnchor_K2Node_ComponentBoundEvent_3_OnMenuOpenChangedEvent__DelegateSignature(self, bIsOpen: bool):
        ExecuteUbergraph_Widget_MAMTree_Node.K2Node_ComponentBoundEvent_bIsOpen = bIsOpen #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MAMTree_Node(575)
    

    def CloseMenu(self):
        self.ExecuteUbergraph_Widget_MAMTree_Node(640)
    

    def OnResearchButtonPressed(self):
        self.ExecuteUbergraph_Widget_MAMTree_Node(1042)
    

    def BndEvt__mResearchedButton_K2Node_ComponentBoundEvent_4_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_MAMTree_Node(1047)
    

    def BndEvt__mResearchedButton_K2Node_ComponentBoundEvent_5_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_MAMTree_Node(1052)
    

    def BndEvt__mResearchedButton_K2Node_ComponentBoundEvent_6_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_MAMTree_Node(1057)
    

    def ExecuteUbergraph_Widget_MAMTree_Node(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.SetNodeState(4)
        goto(ExecutionFlow.Pop())
        self.mHoverMenuAnchor.Close()
        goto(ExecutionFlow.Pop())
        # Label 65
        ReturnValue: bool = EqualEqual_ByteByte(self.mNodeState, 0)
        ReturnValue1: bool = EqualEqual_ByteByte(self.mNodeState, 4)
        ReturnValue_0: bool = BooleanOR(ReturnValue, ReturnValue1)
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        self.OnClicked.ProcessMulticastDelegate(self.mNodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292)
        self.mHoverMenuAnchor.Open(False)
        self.mInfoWidget.mIsNodeSelected = self.mIsSelected
        self.mInfoWidget.UpdateState()
        goto(ExecutionFlow.Pop())
        # Label 323
        self.UpdateNodeIcon(self.mNodeData)
        goto(ExecutionFlow.Pop())
        # Label 347
        ReturnValue_1: bool = Not_PreBool(self.mIsOtherSelected)
        if not ReturnValue_1:
            goto('L461')
        self.mHoverMenuAnchor.Open(False)
        self.OnHovered.ProcessMulticastDelegate(self.mNodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292)
        goto(ExecutionFlow.Pop())
        # Label 461
        self.OnHovered.ProcessMulticastDelegate(self.mNodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292)
        goto(ExecutionFlow.Pop())
        # Label 499
        if not self.mIsSelected:
            goto('L551')
        # Label 513
        self.OnUnhovered.ProcessMulticastDelegate(self.mNodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292)
        goto(ExecutionFlow.Pop())
        # Label 551
        self.CloseMenu()
        goto('L513')
        goto('L323')
        if not bIsOpen:
            goto('L590')
        goto(ExecutionFlow.Pop())
        # Label 590
        self.mInfoWidget = None
        goto(ExecutionFlow.Pop())
        # Label 602
        self.OnResearchStarted.ProcessMulticastDelegate()
        self.CloseMenu()
        goto('L15')
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(self.mInfoWidget)
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        self.mInfoWidget.OnClicked.Clear()
        ReturnValue_3: Ptr[UMGSequencePlayer] = self.mInfoWidget.BPW_MAMTreeInfoBox.PlayAnimation(self.mInfoWidget.BPW_MAMTreeInfoBox.SpawnAnim, 0, 1, 1, 1)
        ReturnValue_4: float = self.mInfoWidget.BPW_MAMTreeInfoBox.SpawnAnim.GetEndTime()
        Default__KismetSystemLibrary.Delay(self, ReturnValue_4, LatentActionInfo(Linkage = 32, UUID = -1878934772, ExecutionFunction = "ExecuteUbergraph_Widget_MAMTree_Node", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L602')
        goto('L65')
        goto('L347')
        goto('L499')
    

    def OnResearchStarted__DelegateSignature(self):
        pass
    

    def OnUnhovered__DelegateSignature(self, Coordinates: IntVector2D):
        pass
    

    def OnHovered__DelegateSignature(self, Coordinates: IntVector2D):
        pass
    

    def OnClicked__DelegateSignature(self, Coordinates: IntVector2D):
        pass
    
