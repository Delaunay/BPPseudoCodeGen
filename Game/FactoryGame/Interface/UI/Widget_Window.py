
from codegen.ue4_stub import *

from Script.UMG import GetChildrenCount
from Script.Engine import TextIsEmpty
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import ESlateVisibility
from Script.FactoryGame import GetWindowWantsInventoryAddon
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.Widget_Window import ExecuteUbergraph_Widget_Window
from Script.UMG import Destruct
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetShowInventory
from Script.UMG import Construct
from Game.FactoryGame.Interface.UI.Widget_Window import ExecuteUbergraph_Widget_Window.K2Node_Event_InDeltaTime
from Game.FactoryGame.Interface.UI.Widget_Window import ExecuteUbergraph_Widget_Window.K2Node_Event_MyGeometry
from Script.FactoryGame import FGWindow
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import HasAnyChildren
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import BP_GameUI
from Script.UMG import BindToAnimationFinished

class Widget_Window(FGWindow):
    mTitleText: FText
    OnClose: FMulticastScriptDelegate
    mShowCloseButton: bool = True
    mCanShowInventory: bool = True
    
    def GetDividerButtonSlotVisibility(self):
        ReturnValue: bool = self.ButtonSlot.HasAnyChildren()
        if not ReturnValue:
            goto('L81')
        ReturnValue_0: uint8 = 3
        goto('L101')
        # Label 81
        ReturnValue_0 = 1
    

    def GetNavigationVisibiliy(self):
        Variable: uint8 = 1
        Variable1: uint8 = 4
        
        self.mNavigationWidget.mNavigationText = None
        ReturnValue: bool = Default__KismetTextLibrary.TextIsEmpty(Ref[self.mNavigationWidget.mNavigationText])
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_0: uint8 = switch.get(Variable_0, None)
    

    def GetCloseButtonVisibility(self):
        Variable: uint8 = 4
        Variable1: uint8 = 1
        Variable_0: bool = self.mShowCloseButton
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue = switch.get(Variable_0, None)
    

    def GetInventoryBodyVisibility(self):
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        gameUI1 = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue1, self, Ref[gameUI1])
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(gameUI1)
        if not ReturnValue:
            goto('L522')
        Variable: uint8 = 4
        Variable1: uint8 = 1
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue_0, self, Ref[gameUI])
        ReturnValue_1: bool = gameUI.GetShowInventory()
        ReturnValue_2: int32 = self.InventorySlot.GetChildrenCount()
        ReturnValue_3: bool = ReturnValue_2 > 0
        ReturnValue_4: bool = ReturnValue_3 and ReturnValue_1
        Variable_0: bool = ReturnValue_4
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_5: uint8 = switch.get(Variable_0, None)
        goto('L542')
        # Label 522
        ReturnValue_5 = 1
    

    def GetTopButtonSlotVisibility(self):
        ReturnValue: bool = self.ButtonSlot.HasAnyChildren()
        if not ReturnValue:
            goto('L81')
        ReturnValue_0: uint8 = 0
        goto('L101')
        # Label 81
        ReturnValue_0 = 1
    

    def OnDrop(self):
        ReturnValue = True
    

    def SetTitle(self, Title: FText):
        self.mTitleText = Title
        self.mTitleLabel.SetTitle(self.mTitleText)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Window(10)
    

    def OnEscapePressed(self):
        self.ExecuteUbergraph_Widget_Window(121)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_Window(162)
    

    def BndEvt__mCloseButton_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Window(177)
    

    def Tick(self):
        ExecuteUbergraph_Widget_Window.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Window.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Window(182)
    

    def OnConstructAnimFinished(self):
        self.ExecuteUbergraph_Widget_Window(939)
    

    def ExecuteUbergraph_Widget_Window(self):
        self.Construct()
        self.SetTitle(self.mTitleText)
        OutputDelegate.BindUFunction(self, OnConstructAnimFinished)
        self.BindToAnimationFinished(self.Widget_Anim_Up_Slide.EnableAnim, OutputDelegate)
        # End
        # Label 121
        self.Widget_Anim_Up_Slide.CloseAnim()
        # End
        self.Destruct()
        # End
        goto('L121')
        ReturnValue: uint8 = self.GetInventoryBodyVisibility()
        self.InventorySlot.SetVisibility(ReturnValue)
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue_0, self, Ref[gameUI])
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(gameUI)
        if not ReturnValue_1:
            goto('L980')
        ReturnValue_2: int32 = self.InventorySlot.GetChildrenCount()
        ReturnValue_3: bool = EqualEqual_IntInt(ReturnValue_2, 0)
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        gameUI1 = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue1, self, Ref[gameUI1])
        ReturnValue_4: bool = gameUI1.GetWindowWantsInventoryAddon()
        ReturnValue_5: bool = ReturnValue_4 and ReturnValue_3
        ReturnValue1_0: bool = ReturnValue_5 and self.mCanShowInventory
        if not ReturnValue1_0:
            goto('L980')
        ReturnValue1 = self.GetOwningPlayer()
        
        gameUI1 = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue1, self, Ref[gameUI1])
        UI: Ptr[BP_GameUI] = Cast[BP_GameUI](gameUI1)
        bSuccess: bool = UI
        if not bSuccess:
            goto('L980')
        
        CachedPlayerInventoryAddon = None
        UI.CreateAddOnPlayerInventory(self.InventorySlot, Ref[CachedPlayerInventoryAddon])
        # End
        # Label 915
        self.OnClose.ProcessMulticastDelegate()
        # End
        if not self.Widget_Anim_Up_Slide.CloseAnimStarted:
            goto('L980')
        goto('L915')
    

    def OnClose__DelegateSignature(self):
        pass
    
