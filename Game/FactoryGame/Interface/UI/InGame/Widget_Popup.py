
from codegen.ue4_stub import *

from Script.UMG import SetUserFocus
from Script.Engine import Default__KismetInputLibrary
from Script.Engine import SetTextPropertyByName
from Game.FactoryGame.Interface.UI.InGame.Widget_PopupDefaultText import Widget_PopupDefaultText
from Script.UMG import SetKeyboardFocus
from Script.FactoryGame import FGBaseUI
from Game.FactoryGame.Interface.UI.InGame.Widget_Popup import ExecuteUbergraph_Widget_Popup
from Script.UMG import HorizontalBoxSlot
from Script.InputCore import Key
from Script.FactoryGame import FGHUDBase
from Script.UMG import OverlaySlot
from Script.UMG import Default__WidgetLayoutLibrary
from Script.SlateCore import Margin
from Script.UMG import SlotAsOverlaySlot
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.Engine import Not_PreBool
from Script.Engine import HUD
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Game.FactoryGame.Interface.UI.Assets.BuildMenu.Cross import Cross
from Script.Engine import SetStructurePropertyByName
from Script.UMG import SetHorizontalAlignment
from Script.UMG import Handled
from Game.FactoryGame.Interface.UI.InGame.Widget_Popup import ExecuteUbergraph_Widget_Popup.K2Node_Event_InDeltaTime
from Script.UMG import Unhandled
from Game.FactoryGame.Interface.UI.InGame.Widget_Popup import ExecuteUbergraph_Widget_Popup.K2Node_Event_MyGeometry
from Script.FactoryGame import GetDefaultFocusWidget
from Script.Engine import IsValid
from Script.Engine import GetHUD
from Script.UMG import GetIsEnabled
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import ClassIsChildOf
from Script.FactoryGame import SetDefaultFocusWidget
from Script.FactoryGame import CallPopupClosedClicked
from Script.UMG import HasFocusedDescendants
from Script.UMG import Construct
from Script.UMG import Tick
from Script.UMG import Widget
from Script.FactoryGame import PopupData
from Script.FactoryGame import Init
from Script.Engine import GetKey
from Script.Engine import NotEqual_ByteByte
from Script.Engine import EqualEqual_KeyKey
from Script.UMG import UserWidget
from Script.FactoryGame import FGPopupWidgetContent
from Script.FactoryGame import FGPopupWidget
from Script.UMG import AddChildToHorizontalBox
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_StandardButton import Widget_StandardButton
from Script.UMG import Create
from Script.CoreUObject import Vector2D
from Script.SlateCore import SlateColor
from Script.UMG import EventReply
from Script.CoreUObject import LinearColor
from Script.FactoryGame import GetBaseUI

class Widget_Popup(FGPopupWidget):
    mPopupData: PopupData
    mIsContentContainerType: bool
    Widget_PopupContent: Ptr[FGPopupWidgetContent]
    mPopupWasConfirmed: bool
    mDefaultDesc: FText
    mRestoreFocusWhenLost = True
    mCallCustomTickOnConstruct = True
    
    def CancelClicked(self):
        self.DoClosePopup(False)
    

    def OkClicked(self):
        self.DoClosePopup(True)
    

    def CheckButtonState(self):
        if not self.mIsContentContainerType:
            goto('L74')
        ReturnValue: bool = self.Widget_PopupContent.GetShouldOkayBeEnabled()
        if not ReturnValue:
            goto('L135')
        # Label 74
        ReturnValue_0: bool = self.mConfrimButton.GetIsEnabled()
        if not ReturnValue_0:
            goto('L233')
        # End
        # Label 135
        ReturnValue_0 = self.mConfrimButton.GetIsEnabled()
        if not ReturnValue_0:
            goto('L270')
        self.mConfrimButton.SetIsEnabled(False)
        # End
        # Label 233
        self.mConfrimButton.SetIsEnabled(True)
    

    def OnKeyUp(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_0: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "Escape"))
        if not ReturnValue_0:
            goto('L248')
        self.DoClosePopup(False)
        ReturnValue_1: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_2: EventReply = ReturnValue_1
        goto('L325')
        # Label 248
        ReturnValue_3: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_2 = ReturnValue_3
    

    def DoClosePopup(self, ConfirmClicked: bool):
        if not self.mIsContentContainerType:
            goto('L50')
        self.Widget_PopupContent.NotifyPopupConfirmed()
        # Label 50
        self.mPopupWasConfirmed = ConfirmClicked
        self.CallPopupClosedClicked(ConfirmClicked)
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[HUD] = ReturnValue.GetHUD()
        AsFGHUDBase: Ptr[FGHUDBase] = Cast[FGHUDBase](ReturnValue_0)
        bSuccess: bool = AsFGHUDBase
        if not bSuccess:
            goto('L311')
        # Label 233
        ReturnValue_1: Ptr[FGBaseUI] = AsFGHUDBase.GetBaseUI()
        ReturnValue_1.ClosePopup()
    

    def Init(self):
        self.ExecuteUbergraph_Widget_Popup(2477)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Popup(2457)
    

    def Tick(self):
        ExecuteUbergraph_Widget_Popup.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Popup.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Popup(1980)
    

    def BndEvt__Widget_StandardButton_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Popup(2284)
    

    def ExecuteUbergraph_Widget_Popup(self):
        # Label 10
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_StandardButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_StandardButton, ReturnValue)
        Variable: Const[FText] = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 115, 'Value': 'Cancel'}"
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_0, "mText", Ref[Variable])
        SlateBrush.ImageSize = Vector2D(X = 20, Y = 20)
        SlateBrush.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush.TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0)
        SlateBrush.ResourceObject = Cross
        SlateBrush.DrawAs = 3
        SlateBrush.Tiling = 0
        SlateBrush.Mirroring = 0
        
        SlateBrush = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_0, "mIconBrush", Ref[SlateBrush])
        ReturnValue_1: Ptr[HorizontalBoxSlot] = self.mButtonBox.AddChildToHorizontalBox(ReturnValue_0)
        OutputDelegate1.BindUFunction(self, CancelClicked)
        ReturnValue_0.OnClicked.AddUnique(OutputDelegate1)
        # End
        # Label 709
        ReturnValue_2: Ptr[OverlaySlot] = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.mConfrimButton)
        ReturnValue_2.SetHorizontalAlignment(2)
        # End
        # Label 799
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1: Ptr[Widget_PopupDefaultText] = Default__WidgetBlueprintLibrary.Create(self, Widget_PopupDefaultText, ReturnValue2)
        
        self.mPopupData.Body = None
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue1, "mBody", Ref[self.mPopupData.Body])
        ReturnValue_3: Ptr[PanelSlot] = self.mSlot.AddChild(ReturnValue1)
        # Label 1007
        self.Widget_Window_DarkMode.SetTitle(self.mPopupData.Title)
        OutputDelegate.BindUFunction(self, CancelClicked)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
        CmpSuccess: bool = NotEqual_ByteByte(self.mPopupData.ID, 0)
        if not CmpSuccess:
            goto('L1292')
        CmpSuccess = NotEqual_ByteByte(self.mPopupData.ID, 1)
        if not CmpSuccess:
            goto('L10')
        CmpSuccess = NotEqual_ByteByte(self.mPopupData.ID, 2)
        if not CmpSuccess:
            goto('L1351')
        # End
        # Label 1292
        self.mConfrimButton.mButton.SetKeyboardFocus()
        goto('L709')
        # Label 1351
        self.mButtonBox.SetVisibility(1)
        # End
        # Label 1394
        self.mInstigator = self.mPopupData.Instigator
        ReturnValue_4: bool = ClassIsChildOf(self.mPopupData.PopupClass, UserWidget)
        if not ReturnValue_4:
            goto('L1964')
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue2_0: Ptr[UserWidget] = Default__WidgetBlueprintLibrary.Create(self, self.mPopupData.PopupClass, ReturnValue1_0)
        Content: Ptr[FGPopupWidgetContent] = Cast[FGPopupWidgetContent](ReturnValue2_0)
        bSuccess: bool = Content
        if not bSuccess:
            goto('L1948')
        self.Widget_PopupContent = Content
        self.mIsContentContainerType = True
        Content.mPopupWidget = self
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValid(self.mInstigator)
        if not ReturnValue1_1:
            goto('L1892')
        
        self.mPopupData.Body = None
        Content.SetOptionalTextElements(Ref[self.mPopupData.Body], Ref[self.mDefaultDesc])
        Content.SetInstigatorAndInitialize(self.mInstigator)
        # Label 1892
        ReturnValue1_2: Ptr[PanelSlot] = self.mSlot.AddChild(ReturnValue2_0)
        goto('L1007')
        # Label 1948
        self.mIsContentContainerType = False
        goto('L1892')
        # Label 1964
        self.mIsContentContainerType = False
        goto('L799')
        self.Tick(MyGeometry, InDeltaTime)
        self.CheckButtonState()
        ReturnValue_5: bool = self.HasFocusedDescendants()
        ReturnValue_6: bool = Not_PreBool(ReturnValue_5)
        ReturnValue1_3: Ptr[Widget] = self.GetDefaultFocusWidget()
        ReturnValue_7: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_3)
        ReturnValue_8: bool = ReturnValue_6 and ReturnValue_7
        if not ReturnValue_8:
            goto('L2482')
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_9: Ptr[Widget] = self.GetDefaultFocusWidget()
        ReturnValue_9.SetUserFocus(ReturnValue3)
        # End
        self.DoClosePopup(True)
        # End
        # Label 2304
        self.SetDefaultFocusWidget(self.mConfrimButton.mButton)
        # End
        # Label 2350
        ReturnValue4: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mConfrimButton.mButton.SetUserFocus(ReturnValue4)
        goto('L2304')
        # Label 2442
        self.Construct()
        goto('L1394')
        goto('L2442')
        # Label 2462
        self.Init()
        goto('L2350')
        goto('L2462')
    
