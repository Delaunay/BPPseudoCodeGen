
from codegen.ue4_stub import *

from Script.UMG import SetUserFocus
from Script.Engine import Delay
from Script.Engine import FClamp
from Script.FactoryGame import FGPlayerController
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Interface.UI.InGame.CursorParticles.CursorParticleStruct import CursorParticleStruct
from Script.UMG import OverlaySlot
from Script.UMG import GetChildrenCount
from Script.Engine import Array_Set
from Script.FactoryGame import SetShowInventory
from Script.Engine import TextIsEmpty
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import HUD
from Script.Engine import Ease
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import GetChildAt
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import Handled
from Game.FactoryGame.Interface.UI.InGame.Widget_TitleButton_DarkMode import Widget_TitleButton_DarkMode
from Script.UMG import Unhandled
from Script.UMG import ESlateVisibility
from Script.Engine import TimerHandle
from Script.FactoryGame import GetWindowWantsInventoryAddon
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.InGame.InventorySlots.Widget_InventorySlot import Widget_InventorySlot
from Script.Engine import GetHUD
from Script.Engine import GreaterEqual_FloatFloat
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Interface.UI.Widget_Window_DarkMode import ExecuteUbergraph_Widget_Window_DarkMode.K2Node_ComponentBoundEvent_ButtonIndex
from Game.FactoryGame.Interface.UI.InGame.-Shared.ImageAndText import ImageAndText
from Script.UMG import GetDesiredSize
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Interface.UI.Widget_Window_DarkMode import ExecuteUbergraph_Widget_Window_DarkMode.K2Node_Event_InDeltaTime
from Game.FactoryGame.Interface.UI.Widget_Window_DarkMode import ExecuteUbergraph_Widget_Window_DarkMode.K2Node_Event_IsDesignTime
from Script.UMG import Destruct
from Script.Engine import BreakVector2D
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SlidingTabs import Widget_SlidingTabs
from Script.FactoryGame import GetShowInventory
from Script.UMG import Construct
from Game.FactoryGame.Interface.UI.Widget_Window_DarkMode import ExecuteUbergraph_Widget_Window_DarkMode
from Script.FactoryGame import GetShortcutIndexFromKey
from Script.UMG import Widget
from Script.FactoryGame import GetGameUI
from Script.UMG import ForceLayoutPrepass
from Script.FactoryGame import FGHUD
from Script.FactoryGame import FGGameUI
from Game.FactoryGame.Character.Player.Widget_PlayerInventoryAddon import Widget_PlayerInventoryAddon
from Script.UMG import SetWidthOverride
from Game.FactoryGame.Interface.UI.Widget_Window_DarkMode import ExecuteUbergraph_Widget_Window_DarkMode.K2Node_Event_MyGeometry
from Script.UMG import HasUserFocusedDescendants
from Script.FactoryGame import FGWindow
from Game.FactoryGame.Interface.UI.InGame.-Shared.Struct_KeybindingHint import Struct_KeybindingHint
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.Widget_Window_DarkMode import ExecuteUbergraph_Widget_Window_DarkMode.K2Node_CustomEvent_RelevantClasses
from Script.UMG import HasAnyChildren
from Script.UMG import Create
from Script.CoreUObject import Vector2D
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import BP_GameUI
from Script.UMG import BindToAnimationFinished
from Script.UMG import SetVerticalAlignment
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.UMG import EventReply
from Script.UMG import AddChildToOverlay

class Widget_Window_DarkMode(FGWindow):
    mTitleText: FText = NSLOCTEXT("", "6453760C4ADD79C424BAFB8E6342603B", "Title")
    OnClose: FMulticastScriptDelegate
    mShowCloseButton: bool = True
    mCanShowInventory: bool = True
    mShowInventory: bool
    mShowFicsitLogo: bool
    mOverrideCloseButton: bool
    mOverwriteTabButtonFunctions: bool
    mIsOverrideWidthSet: bool
    mShowInventoryT: float
    mLerpUpdateTime: float = 0.009999999776482582
    mLerpSlideTime: float = 0.25
    mStartLerpSize: float
    mShowInventoryTimer: TimerHandle
    mTabs: List[ImageAndText]
    OnTabButtonClicked: FMulticastScriptDelegate
    mParticleWidgets: List[CursorParticleStruct]
    mCachedPlayerInventoryAddon: Ptr[Widget_PlayerInventoryAddon]
    OnRelevantShortcutPressed: FMulticastScriptDelegate
    mRelevantItemsText: FText = NSLOCTEXT("", "6E8068CF4CF2F2D8AAE3D9A5CB550353", "Relevant Items:")
    mKeyBindingHints: List[Struct_KeybindingHint]
    
    def OnMouseButtonUp(self):
        self.Widget_UI_ParticleManager.CreateParticle()
        ReturnValue: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_0: EventReply = ReturnValue
    

    def OnNumKeyDown(self, KeyEvent: KeyEvent):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: bool = self.HasUserFocusedDescendants(ReturnValue)
        if not ReturnValue_0:
            goto('L874')
        # Label 67
        ReturnValue_1: bool = self.InventorySlot.HasAnyChildren()
        if not ReturnValue_1:
            goto('L922')
        ReturnValue1: Ptr[Widget] = self.InventorySlot.GetChildAt(0)
        Addon: Ptr[Widget_PlayerInventoryAddon] = Cast[Widget_PlayerInventoryAddon](ReturnValue1)
        bSuccess2: bool = Addon
        if not bSuccess2:
            goto('L1004')
        InventoryAddon = Addon
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue2)
        bSuccess1: bool = Controller
        
        ReturnValue_2: int32 = Controller.GetShortcutIndexFromKey(Ref[KeyEvent])
        LocalIndex = ReturnValue_2
        ReturnValue_3: int32 = InventoryAddon.mRelevantInventory.GetChildrenCount()
        ReturnValue_4: bool = LocalIndex <= ReturnValue_3
        # Label 553
        if not ReturnValue_4:
            goto('L1086')
        ReturnValue_5: Ptr[Widget] = InventoryAddon.mRelevantInventory.GetChildAt(LocalIndex)
        Slot: Ptr[Widget_InventorySlot] = Cast[Widget_InventorySlot](ReturnValue_5)
        bSuccess: bool = Slot
        if not bSuccess:
            goto('L1168')
        InventoryAddon.OnInventorySlotMoveStack(Slot)
        self.OnRelevantShortcutPressed.ProcessMulticastDelegate(Slot)
        ReturnValue_6: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_7: EventReply = ReturnValue_6
        goto('L1245')
        # Label 874
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        self.SetUserFocus(ReturnValue1_0)
        goto('L67')
        # Label 922
        ReturnValue_8: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_7 = ReturnValue_8
        goto('L1245')
        # Label 1004
        ReturnValue1_1: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_7 = ReturnValue1_1
        goto('L1245')
        # Label 1086
        ReturnValue2_0: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_7 = ReturnValue2_0
        goto('L1245')
        # Label 1168
        ReturnValue3: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_7 = ReturnValue3
    

    def OnKeyUp(self):
        ReturnValue: EventReply = self.OnNumKeyDown(InKeyEvent)
        ReturnValue_0: EventReply = ReturnValue
    

    def OnMouseButtonDown(self):
        pass
    

    def InitTabs(self):
        
        ReturnValue: int32 = len(self.mTabs)
        ReturnValue_0: bool = ReturnValue > 0
        if not ReturnValue_0:
            goto('L462')
        # Label 107
        self.Widget_TabsContainer.mButtons = self.mTabs
        ReturnValue_1: int32 = self.WindowBody.GetChildrenCount()
        ReturnValue1: bool = ReturnValue_1 > 0
        if not ReturnValue1:
            goto('L421')
        ReturnValue_2: Ptr[Widget] = self.WindowBody.GetChildAt(0)
        Tabs: Ptr[Widget_SlidingTabs] = Cast[Widget_SlidingTabs](ReturnValue_2)
        bSuccess: bool = Tabs
        if not bSuccess:
            goto('L421')
        self.Widget_TabsContainer.mSlidingTabsWidget = Tabs
        # Label 421
        self.Widget_TabsContainer.Init()
        # End
        # Label 462
        ImageAndText.Texture_4_7082C106445A08AB1E68E496718E5427 = None
        ImageAndText.Text_5_FD671CE446AF05CA543E228C049AB0F9 = self.mTitleText
        
        ImageAndText = None
        ReturnValue_3: int32 = self.mTabs.append(ImageAndText)
        goto('L107')
    

    def SetInventoryVisibility(self, mShowInventory: bool, Animate: bool):
        self.mShowInventory = mShowInventory
        LocalAnimate = Animate
        if not self.mShowInventory:
            goto('L520')
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[HUD] = ReturnValue1.GetHUD()
        AsFGHUD1: Ptr[FGHUD] = Cast[FGHUD](ReturnValue1_0)
        bSuccess1: bool = AsFGHUD1
        ReturnValue1_1: Ptr[FGGameUI] = AsFGHUD1.GetGameUI()
        ReturnValue1_1.SetShowInventory(True)
        if not LocalAnimate:
            goto('L801')
        
        # Label 272
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mShowInventoryTimer])
        self.ForceLayoutPrepass()
        self.mShowInventoryT = 0
        self.mStartLerpSize = self.mInventorySizeBox.WidthOverride
        OutputDelegate.BindUFunction(self, LerpShowInventory)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mLerpUpdateTime, True)
        self.mShowInventoryTimer = ReturnValue
        # End
        # Label 520
        if not LocalAnimate:
            goto('L553')
        if not self.mIsOverrideWidthSet:
            goto('L1088')
        goto('L272')
        # Label 553
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[HUD] = ReturnValue_0.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_1)
        bSuccess: bool = AsFGHUD
        ReturnValue_2: Ptr[FGGameUI] = AsFGHUD.GetGameUI()
        ReturnValue_2.SetShowInventory(False)
        self.mInventorySizeBox.SetWidthOverride(0)
        # End
        # Label 801
        ReturnValue2: Vector2D = self.InventorySlot.GetDesiredSize()
        
        X2 = None
        Y2 = None
        BreakVector2D(ReturnValue2, Ref[X2], Ref[Y2])
        ReturnValue_3: bool = X2 > 0
        # Label 922
        self.mIsOverrideWidthSet = ReturnValue_3
        if not self.mIsOverrideWidthSet:
            goto('L1232')
        ReturnValue1_2: Vector2D = self.InventorySlot.GetDesiredSize()
        
        X1 = None
        Y1 = None
        BreakVector2D(ReturnValue1_2, Ref[X1], Ref[Y1])
        self.mInventorySizeBox.SetWidthOverride(X1)
        # End
        # Label 1088
        ReturnValue_4: Vector2D = self.InventorySlot.GetDesiredSize()
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_4, Ref[X], Ref[Y])
        self.mInventorySizeBox.SetWidthOverride(X)
        self.mIsOverrideWidthSet = True
        goto('L272')
    

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
        self.Widget_TitleLabel_DarkMode.SetTitle(self.mTitleText)
        
        ReturnValue: int32 = len(self.mTabs)
        ReturnValue_0: bool = EqualEqual_IntInt(ReturnValue, 1)
        if not ReturnValue_0:
            goto('L377')
        
        Item = None
        Item = self.mTabs[0]
        ImageAndText.Texture_4_7082C106445A08AB1E68E496718E5427 = Item.Texture_4_7082C106445A08AB1E68E496718E5427
        ImageAndText.Text_5_FD671CE446AF05CA543E228C049AB0F9 = self.mTitleText
        
        ImageAndText = None
        Default__KismetArrayLibrary.Array_Set(0, False, Ref[self.mTabs], Ref[ImageAndText])
        self.InitTabs()
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Window_DarkMode(944)
    

    def OnEscapePressed(self):
        self.ExecuteUbergraph_Widget_Window_DarkMode(1099)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_Window_DarkMode(1199)
    

    def Tick(self):
        ExecuteUbergraph_Widget_Window_DarkMode.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Window_DarkMode.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Window_DarkMode(1210)
    

    def OnConstructAnimFinished(self):
        self.ExecuteUbergraph_Widget_Window_DarkMode(1452)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_Window_DarkMode.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Window_DarkMode(1489)
    

    def OnCloseButtonClicked(self):
        self.ExecuteUbergraph_Widget_Window_DarkMode(1966)
    

    def LerpShowInventory(self):
        self.ExecuteUbergraph_Widget_Window_DarkMode(1971)
    

    def BndEvt__Widget_TabsContainer_K2Node_ComponentBoundEvent_2_OnButtonClicked__DelegateSignature(self, ButtonIndex: int32):
        ExecuteUbergraph_Widget_Window_DarkMode.K2Node_ComponentBoundEvent_ButtonIndex = ButtonIndex #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Window_DarkMode(2750)
    

    def BndEvt__Widget_TabsContainer_K2Node_ComponentBoundEvent_0_OnNoTabsGenerated__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Window_DarkMode(2779)
    

    def BndEvt__Widget_TabsContainer_K2Node_ComponentBoundEvent_1_OnTabsGenerated__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Window_DarkMode(2818)
    

    def SetupRelevantInventory(self, relevantClasses: Const[Ref[List[TSubclassOf[FGItemDescriptor]]]]):
        ExecuteUbergraph_Widget_Window_DarkMode.K2Node_CustomEvent_RelevantClasses = relevantClasses #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Window_DarkMode(2857)
    

    def ExecuteUbergraph_Widget_Window_DarkMode(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: bool = self.InventorySlot.HasAnyChildren()
        if not ReturnValue:
            goto('L288')
        ReturnValue_0: Ptr[Widget] = self.InventorySlot.GetChildAt(0)
        Addon: Ptr[Widget_PlayerInventoryAddon] = Cast[Widget_PlayerInventoryAddon](ReturnValue_0)
        bSuccess: bool = Addon
        if not bSuccess:
            goto('L288')
        
        RelevantClasses = None
        Addon.SetupRelevantInventory(Ref[RelevantClasses])
        Addon.SetRelevantItemsText(self.mRelevantItemsText)
        goto(ExecutionFlow.Pop())
        # Label 288
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 15, UUID = 611849551, ExecutionFunction = "ExecuteUbergraph_Widget_Window_DarkMode", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 365
        ReturnValue_1: int32 = self.InventorySlot.GetChildrenCount()
        ReturnValue_2: bool = EqualEqual_IntInt(ReturnValue_1, 0)
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        gameUI1 = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue1, self, Ref[gameUI1])
        ReturnValue_3: bool = gameUI1.GetWindowWantsInventoryAddon()
        ReturnValue_4: bool = ReturnValue_3 and ReturnValue_2
        ReturnValue1_0: bool = ReturnValue_4 and self.mCanShowInventory
        if not ReturnValue1_0:
            goto('L675')
        if not Variable:
            goto('L713')
        goto(ExecutionFlow.Pop())
        # Label 675
        Variable: bool = False
        if not Variable2:
            goto('L701')
        goto(ExecutionFlow.Pop())
        # Label 701
        Variable2: bool = True
        goto(ExecutionFlow.Pop())
        # Label 713
        Variable = True
        Variable2 = False
        ReturnValue1 = self.GetOwningPlayer()
        
        gameUI1 = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue1, self, Ref[gameUI1])
        UI: Ptr[BP_GameUI] = Cast[BP_GameUI](gameUI1)
        bSuccess1: bool = UI
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        
        CachedPlayerInventoryAddon = None
        UI.CreateAddOnPlayerInventory(self.InventorySlot, Ref[CachedPlayerInventoryAddon])
        goto(ExecutionFlow.Pop())
        self.Construct()
        OutputDelegate.BindUFunction(self, OnConstructAnimFinished)
        self.Widget_Anim_Up_Slide.BindToAnimationFinished(self.Widget_Anim_Up_Slide.EnableAnim, OutputDelegate)
        self.Widget_UI_ParticleManager.mParticleWidgets = self.mParticleWidgets
        goto(ExecutionFlow.Pop())
        # Label 1099
        ReturnValue_5: bool = Not_PreBool(self.mOverrideCloseButton)
        if not ReturnValue_5:
            goto('L1179')
        self.Widget_Anim_Up_Slide.CloseAnim()
        goto(ExecutionFlow.Pop())
        # Label 1179
        self.OnClose.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
        self.Destruct()
        goto(ExecutionFlow.Pop())
        ReturnValue_6: uint8 = self.GetInventoryBodyVisibility()
        self.InventorySlot.SetVisibility(ReturnValue_6)
        ReturnValue_7: Ptr[PlayerController] = self.GetOwningPlayer()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue_7, self, Ref[gameUI])
        ReturnValue_8: bool = Default__KismetSystemLibrary.IsValid(gameUI)
        if not ReturnValue_8:
           goto(ExecutionFlow.Pop())
        goto('L365')
        # Label 1432
        self.OnClose.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
        if not self.Widget_Anim_Up_Slide.CloseAnimStarted:
           goto(ExecutionFlow.Pop())
        goto('L1432')
        self.SetTitle(self.mTitleText)
        ExecutionFlow.Push("L1881")
        ExecutionFlow.Push("L1580")
        ExecutionFlow.Push("L1636")
        if not self.mShowFicsitLogo:
            goto('L1927')
        self.FicsItLogo.SetVisibility(0)
        goto(ExecutionFlow.Pop())
        # Label 1580
        self.Widget_TabsContainer.mOverrideButtonFunctions = self.mOverwriteTabButtonFunctions
        self.InitTabs()
        goto(ExecutionFlow.Pop())
        # Label 1636
        if not self.mShowCloseButton:
           goto(ExecutionFlow.Pop())
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_9: Ptr[Widget_TitleButton_DarkMode] = Default__WidgetBlueprintLibrary.Create(self, Widget_TitleButton_DarkMode, ReturnValue2)
        OutputDelegate1.BindUFunction(self, OnCloseButtonClicked)
        ReturnValue_9.OnClicked.AddUnique(OutputDelegate1)
        ReturnValue_10: Ptr[OverlaySlot] = self.CloseButtonOverlay.AddChildToOverlay(ReturnValue_9)
        ReturnValue_10.SetVerticalAlignment(0)
        goto(ExecutionFlow.Pop())
        
        # Label 1881
        self.mHintContainer.SetKeybindingHints(Ref[self.mKeyBindingHints])
        goto(ExecutionFlow.Pop())
        # Label 1927
        self.FicsItLogo.SetVisibility(2)
        goto(ExecutionFlow.Pop())
        goto('L1099')
        ReturnValue_11: float = self.mLerpUpdateTime / self.mLerpSlideTime
        ReturnValue_12: float = ReturnValue_11 + self.mShowInventoryT
        ReturnValue_13: float = FClamp(ReturnValue_12, 0, 1)
        self.mShowInventoryT = ReturnValue_13
        Variable_0: float = 0
        ReturnValue_14: Vector2D = self.InventorySlot.GetDesiredSize()
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_14, Ref[X], Ref[Y])
        Variable1: bool = self.mShowInventory
        
        switch = {
            False: Variable_0,
            True: X
        }
        ReturnValue_15: float = Ease(self.mStartLerpSize, switch.get(Variable1, None), self.mShowInventoryT, 6, 4, 2)
        self.mInventorySizeBox.SetWidthOverride(ReturnValue_15)
        ReturnValue_16: bool = GreaterEqual_FloatFloat(self.mShowInventoryT, 1)
        if not ReturnValue_16:
           goto(ExecutionFlow.Pop())
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mShowInventoryTimer])
        ReturnValue1_1: bool = Not_PreBool(self.mShowInventory)
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_17: Ptr[HUD] = ReturnValue3.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_17)
        bSuccess2: bool = AsFGHUD
        ReturnValue_18: Ptr[FGGameUI] = AsFGHUD.GetGameUI()
        ReturnValue_18.SetShowInventory(False)
        goto(ExecutionFlow.Pop())
        self.OnTabButtonClicked.ProcessMulticastDelegate(ButtonIndex)
        goto(ExecutionFlow.Pop())
        self.mTabsDivider.SetVisibility(1)
        goto(ExecutionFlow.Pop())
        self.mTabsDivider.SetVisibility(4)
        goto(ExecutionFlow.Pop())
        goto('L15')
    

    def OnRelevantShortcutPressed__DelegateSignature(self, InventorySlot: Ptr[Widget_InventorySlot]):
        pass
    

    def OnTabButtonClicked__DelegateSignature(self, ButtonIndex: int32):
        pass
    

    def OnClose__DelegateSignature(self):
        pass
    
