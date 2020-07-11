
from codegen.ue4_stub import *

from Script.Engine import Default__KismetInputLibrary
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu_RightClickMenu import Widget_BuildMenu_RightClickMenu
from Script.Engine import Texture2D
from Script.Engine import Delay
from Script.Engine import SetClassPropertyByName
from Script.FactoryGame import FGPlayerController
from Script.UMG import GetEndTime
from Script.Engine import Array_Contains
from Script.FactoryGame import FGPlayerState
from Script.InputCore import Key
from Script.FactoryGame import GetLanguage
from Script.FactoryGame import RemoveRecipe
from Script.Engine import LatentActionInfo
from Script.FactoryGame import GetNewRecipes
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import ToggleOpen
from Script.FactoryGame import GetProducts
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import Handled
from Script.UMG import PlayAnimation
from Script.UMG import Unhandled
from Script.UMG import ESlateVisibility
from Script.Engine import PointerEvent_IsMouseButtonDown
from Script.UMG import IsOpen
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ShoppingListButton import Widget_ShoppingListButton
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Conv_IntToText
from Script.UMG import SetStretch
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Script.Engine import BooleanOR
from Script.UMG import Construct
from Script.Engine import NotEqual_StrStr
from Script.UMG import Widget
from Script.FactoryGame import Default__FGRecipe
from Script.FactoryGame import FGButtonWidget
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import WidgetAnimation
from Script.Engine import GetKey
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.Engine import EqualEqual_KeyKey
from Script.UMG import Close
from Script.FactoryGame import GetRecipeShortcutIndex
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenuRecipeButton import ExecuteUbergraph_Widget_BuildMenuRecipeButton
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import GetRecipeName
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenuRecipeButton import ExecuteUbergraph_Widget_BuildMenuRecipeButton.K2Node_Event_IsDesignTime
from Script.UMG import Create
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import FGRecipe
from Script.SlateCore import SlateColor
from Script.FactoryGame import ItemAmount
from Script.Engine import IsValidClass
from Script.UMG import EventReply
from Script.CoreUObject import LinearColor

class Widget_BuildMenuRecipeButton(FGButtonWidget):
    HideNewOverlay: Ptr[WidgetAnimation]
    OnHover: Ptr[WidgetAnimation]
    mRecipe: TSubclassOf[FGRecipe]
    OnRecipeClicked: FMulticastScriptDelegate
    OnRecipeHovered: FMulticastScriptDelegate
    OnStopHoveringRecipe: FMulticastScriptDelegate
    mHotkeyIndex: int32 = -1
    mShoppingListWidget: Ptr[Widget_ShoppingListButton]
    mForceHover: bool
    mCanAfford: bool
    bIsFocusable = True
    
    def SetFontScaleForLanguage(self):
        ReturnValue: FString = Default__FGBlueprintFunctionLibrary.GetLanguage()
        ReturnValue_0: bool = Default__KismetStringLibrary.NotEqual_StrStr(ReturnValue, "en-US-POSIX")
        if not ReturnValue_0:
            goto('L167')
        self.ScaleBox_2.SetStretch(0)
        # End
        # Label 167
        self.ScaleBox_2.SetStretch(2)
    

    def UpdateNewItemOverlayVisibility(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](ReturnValue.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
            goto('L385')
        newRecipes: List[TSubclassOf[FGRecipe]] = []
        
        State.GetNewRecipes(Ref[newRecipes])
        Variable: uint8 = 4
        Variable1: uint8 = 2
        
        ReturnValue_0: bool = Default__KismetArrayLibrary.Array_Contains(Ref[newRecipes], Ref[self.mRecipe])
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.NewItemOverlay.SetVisibility(switch.get(Variable_0, None))
    

    def OnKeyDown(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_0: bool = self.mRecipeButton.IsHovered()
        ReturnValue1: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "Add"))
        ReturnValue_1: bool = ReturnValue_0 and ReturnValue1
        if not ReturnValue_1:
            goto('L389')
        self.mShoppingListWidget.mPlayerState.AddRecipeToShoppingList(self.mRecipe, 1)
        # Label 307
        ReturnValue_2: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_3: EventReply = ReturnValue_2
        goto('L694')
        
        # Label 389
        ReturnValue = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_4: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "Subtract"))
        if not ReturnValue_4:
            goto('L617')
        self.mShoppingListWidget.mPlayerState.RemoveRecipeFromShoppingList(self.mRecipe, 1)
        goto('L307')
        # Label 617
        ReturnValue_5: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_3 = ReturnValue_5
    

    def GetRightClickMenuVisibility(self):
        ReturnValue: bool = self.mRightClickMenu.IsOpen()
        if not ReturnValue:
            goto('L81')
        ReturnValue_0: uint8 = 0
        goto('L101')
        # Label 81
        ReturnValue_0 = 3
    

    def CreateRightClickMenu(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_BuildMenu_RightClickMenu] = Default__WidgetBlueprintLibrary.Create(self, Widget_BuildMenu_RightClickMenu, ReturnValue)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_0, "mRecipe", self.mRecipe)
        ReturnValue_1: Ptr[Widget] = ReturnValue_0
    

    def OnMouseButtonDown(self):
        localMouseEvent = MouseEvent
        
        ReturnValue: bool = Default__KismetInputLibrary.PointerEvent_IsMouseButtonDown(Key(KeyName = "RightMouseButton"), Ref[localMouseEvent])
        if not ReturnValue:
            goto('L234')
        self.mRightClickMenu.ToggleOpen(False)
        ReturnValue_0: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_1: EventReply = ReturnValue_0
        goto('L343')
        # Label 234
        self.mRightClickMenu.Close()
        ReturnValue_2: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_1 = ReturnValue_2
    

    def GetTextHoverColor(self):
        ReturnValue: bool = self.IsHovered()
        ReturnValue_0: bool = BooleanOR(ReturnValue, self.mForceHover)
        if not ReturnValue_0:
            goto('L196')
        self.Widget_ShoppingListButton.mParentIsHovered = True
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_1: SlateColor = TextWhite
        goto('L311')
        # Label 196
        self.Widget_ShoppingListButton.mParentIsHovered = False
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_1 = Text
    

    def GetGraphicsHoverColor(self):
        ReturnValue: bool = self.IsHovered()
        ReturnValue_0: bool = BooleanOR(ReturnValue, self.mForceHover)
        if not ReturnValue_0:
            goto('L163')
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue_1: LinearColor = Orange
        goto('L318')
        # Label 163
        LinearColor.R = 0
        LinearColor.G = 0
        LinearColor.B = 0
        LinearColor.A = 0
        ReturnValue_1 = LinearColor
    

    def ResolveHotkeyIndex(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        ReturnValue_0: int32 = Controller.GetRecipeShortcutIndex(self.mRecipe)
        ReturnValue_1: int32 = ReturnValue_0 + 1
        self.mHotkeyIndex = ReturnValue_1
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_IntToText(self.mHotkeyIndex, False, True, 1, 324)
        self.HotkeyText.SetText(ReturnValue_2)
    

    def CreateShoppingListButtons(self):
        self.Widget_ShoppingListButton.mRecipe = self.mRecipe
        self.mShoppingListWidget = self.Widget_ShoppingListButton
    

    def GetBuildingIcon(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mRecipe)
        if not ReturnValue:
            goto('L715')
        ReturnValue_0: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mRecipe, True)
        
        Item = None
        Item = ReturnValue_0[0]
        ReturnValue_1: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(Item.ItemClass)
        SlateBrush.ImageSize = self.mIcon.Brush.ImageSize
        # Label 307
        SlateBrush.Margin = self.mIcon.Brush.Margin
        SlateBrush.TintColor = self.mIcon.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue_1
        SlateBrush.DrawAs = self.mIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mIcon.Brush.Tiling
        SlateBrush.Mirroring = self.mIcon.Brush.Mirroring
        
        SlateBrush = None
        self.mIcon.SetBrush(Ref[SlateBrush])
    

    def OnFocusReceived(self):
        ReturnValue: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_0: EventReply = ReturnValue
    

    def GetRecipeName(self):
        ReturnValue: FText = Default__FGRecipe.GetRecipeName(self.mRecipe)
        self.mProductName.SetText(ReturnValue)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_BuildMenuRecipeButton(15)
    

    def BndEvt__mRecipeOverlay_K2Node_ComponentBoundEvent_35_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_BuildMenuRecipeButton(485)
    

    def BndEvt__mRecipeOverlay_K2Node_ComponentBoundEvent_439_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_BuildMenuRecipeButton(706)
    

    def BndEvt__mRecipeOverlay_K2Node_ComponentBoundEvent_16_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_BuildMenuRecipeButton(711)
    

    def SimulateOnHovered(self):
        self.ExecuteUbergraph_Widget_BuildMenuRecipeButton(888)
    

    def SimulateOnUnhovered(self):
        self.ExecuteUbergraph_Widget_BuildMenuRecipeButton(904)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_BuildMenuRecipeButton.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_BuildMenuRecipeButton(920)
    

    def ExecuteUbergraph_Widget_BuildMenuRecipeButton(self):
        goto(ComputedJump("EntryPoint"))
        self.Construct()
        self.CreateShoppingListButtons()
        self.ResolveHotkeyIndex()
        self.UpdateNewItemOverlayVisibility()
        goto(ExecutionFlow.Pop())
        ReturnValue: bool = self.IsHovered()
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](ReturnValue_0.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        State.RemoveRecipe(self.mRecipe)
        ReturnValue2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.HideNewOverlay, 0, 1, 0, 1)
        ReturnValue_1: float = self.HideNewOverlay.GetEndTime()
        Default__KismetSystemLibrary.Delay(self, ReturnValue_1, LatentActionInfo(Linkage = 441, UUID = 8015938, ExecutionFunction = "ExecuteUbergraph_Widget_BuildMenuRecipeButton", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.UpdateNewItemOverlayVisibility()
        goto(ExecutionFlow.Pop())
        # Label 456
        self.OnRecipeClicked.ProcessMulticastDelegate(self.mRecipe)
        goto(ExecutionFlow.Pop())
        self.mShoppingListWidget.mParentIsHovered = True
        # Label 518
        self.OnRecipeHovered.ProcessMulticastDelegate(self.mRecipe, self)
        ReturnValue_2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OnHover, 0, 1, 0, 1)
        self.Widget_AutoScrollingContainer.StartAutoScroll()
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 68, UUID = 1752585476, ExecutionFunction = "ExecuteUbergraph_Widget_BuildMenuRecipeButton", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L456')
        self.mShoppingListWidget.mParentIsHovered = False
        # Label 744
        self.OnStopHoveringRecipe.ProcessMulticastDelegate(self.mRecipe, self)
        self.mRightClickMenu.Close()
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OnHover, 0, 1, 1, 1)
        self.Widget_AutoScrollingContainer.StopAutoScroll()
        goto(ExecutionFlow.Pop())
        self.mForceHover = True
        goto('L518')
        self.mForceHover = False
        goto('L744')
        self.GetRecipeName()
        self.GetBuildingIcon()
        goto(ExecutionFlow.Pop())
    

    def OnStopHoveringRecipe__DelegateSignature(self, Recipe: TSubclassOf[FGRecipe], RecipeButton: Ptr[Widget_BuildMenuRecipeButton]):
        pass
    

    def OnRecipeHovered__DelegateSignature(self, RecipeHover: TSubclassOf[FGRecipe], RecipeButton: Ptr[Widget_BuildMenuRecipeButton]):
        pass
    

    def OnRecipeClicked__DelegateSignature(self, Recipe: TSubclassOf[FGRecipe]):
        pass
    
