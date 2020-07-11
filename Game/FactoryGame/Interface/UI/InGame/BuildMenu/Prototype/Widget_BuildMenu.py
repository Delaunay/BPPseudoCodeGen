
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.BPW_AddHotbarPreset_Button import BPW_AddHotbarPreset_Button
from Script.Engine import Conv_StringToName
from Script.Engine import Texture2D
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import ChangeNameOfPresetHotbar
from Script.FactoryGame import SetRecipeShortcutOnIndex
from Script.InputCore import Key
from Script.Engine import Conv_ByteToInt
from Script.UMG import AddChild
from Script.Engine import FTrunc
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetProducts
from Script.UMG import GetChildAt
from Script.Engine import NotEqual_ClassClass
from Script.FactoryGame import GetCostForRecipe
from Script.Engine import Array_Find
from Script.UMG import Handled
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.BPW_HobarPreset_Editor_SmallIcon import BPW_HobarPreset_Editor_SmallIcon
from Script.UMG import ESlateVisibility
from Script.UMG import SetText
from Script.FactoryGame import IsCentralStorageBuilt
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu import ExecuteUbergraph_Widget_BuildMenu.K2Node_CustomEvent_ScrollPos
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.FactoryGame import GetAvailableRecipes
from Script.FactoryGame import GetCurrentShortcuts
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu_SubCategoryButton import Widget_BuildMenu_SubCategoryButton
from Script.UMG import Destruct
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu import ExecuteUbergraph_Widget_BuildMenu
from Game.FactoryGame.Recipes.Buildings.TowTruck.Recipe_SpaceElevator import Recipe_SpaceElevator
from Script.UMG import Construct
from Script.FactoryGame import GetNumItemsFromCentralStorage
from Script.FactoryGame import Default__FGBuildingDescriptor
from Script.UMG import HasKeyboardFocus
from Script.Engine import SetIntPropertyByName
from Script.FactoryGame import GetAllPresetHotbars
from Script.Engine import Default__KismetStringLibrary
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.BPW_HotbarPreset_Button import BPW_HotbarPreset_Button
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu import ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_ButtonIndex
from Script.FactoryGame import GetKeyMappingForAction
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import FGBuildGun
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenuRecipeButton import Widget_BuildMenuRecipeButton
from Script.UMG import Create
from Script.Engine import GetGameState
from Script.SlateCore import SlateBrush
from Game.FactoryGame.Recipes.Buildings.Recipe_TradingPost import Recipe_TradingPost
from Script.UMG import HasUserFocus
from Script.Engine import Array_Clear
from Game.FactoryGame.Interface.UI.BPI_GameUI import BPI_GameUI
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.FactoryGame import CanCreateNewPresetHotbar
from Script.CoreUObject import LinearColor
from Script.Engine import EqualEqual_ClassClass
from Script.Engine import SetClassPropertyByName
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import GetAvailableRecipesInSubCategory
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Script.Engine import GreaterEqual_IntInt
from Script.UMG import AddChildToVerticalBox
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import SetHorizontalAlignment
from Script.Engine import GameStateBase
from Script.Engine import InputActionKeyMapping
from Script.FactoryGame import GetInventory
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu import ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_ShouldOverwrite
from Script.CoreUObject import Object
from Script.FactoryGame import FGInventoryComponent
from Script.FactoryGame import PresetHotbar
from Script.FactoryGame import SetDefaultFocusWidget
from Script.FactoryGame import FGInteractWidget
from Script.FactoryGame import FGGameState
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu import ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_Text1
from Script.FactoryGame import GotoBuildState
from Script.FactoryGame import Default__FGRecipe
from Script.Engine import SetMouseLocation
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu import ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_Text
from Script.Engine import InputEvent_IsAltDown
from Script.FactoryGame import FGHotbarShortcut
from Script.Engine import Conv_IntToString
from Script.Engine import GetKey
from Script.UMG import WrapBoxSlot
from Script.Engine import EqualEqual_KeyKey
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu import ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_PresetIndex
from Script.Engine import NotEqual_ByteByte
from Script.UMG import GetBrushResourceAsTexture2D
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.FactoryGame import CreatePresetHotbarFromCurrentHotbar
from Script.UMG import VerticalBoxSlot
from Script.FactoryGame import IsSpaceElevatorBuilt
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import FGRecipe
from Script.FactoryGame import GetAllBuildCategories
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu import ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_CommitMethod
from Script.FactoryGame import ItemAmount
from Script.FactoryGame import GetAvailableSubCategoriesForCategory
from Script.FactoryGame import Default__FGCentralStorageSubsystem
from Script.Engine import PrintString
from Script.UMG import EventReply
from Script.FactoryGame import FGBuildingDescriptor
from Script.UMG import SetUserFocus
from Script.Engine import SetTextPropertyByName
from Script.FactoryGame import CycleToNextHotbar
from Script.Engine import Delay
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu_PowerProduction import Widget_BuildMenu_PowerProduction
from Script.Engine import Array_Contains
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import PanelSlot
from Script.Engine import LatentActionInfo
from Script.FactoryGame import GetCategoryName
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.UMG import PlayAnimation
from Script.UMG import Unhandled
from Script.FactoryGame import GetCategoryIcon
from Script.Engine import EqualEqual_StriStri
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import CopyCurrentHotbarToPresetHotbar
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu import ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_Name
from Script.UMG import AddChildToWrapBox
from Script.FactoryGame import IsTradingPostBuilt
from Script.Engine import BreakVector2D
from Script.Engine import SetBoolPropertyByName
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import ToggleBuildGun
from Script.SlateCore import InputEvent
from Script.FactoryGame import GetShortcutIndexFromKey
from Script.Engine import EqualEqual_ObjectObject
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.UMG import HasUserFocusedDescendants
from Script.FactoryGame import CycleToPreviousHotbar
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu import ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_FocusEvent
from Script.FactoryGame import GetRecipeName
from Script.UMG import HasAnyChildren
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu import ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_IconIndex
from Game.FactoryGame.Equipment.BuildGun.BP_BuildGunStateMenu import BP_BuildGunStateMenu
from Script.CoreUObject import Vector2D
from Script.UMG import GetInputEventFromKeyEvent
from Script.UMG import SetVerticalAlignment
from Script.FactoryGame import RemovePresetHotbar
from Script.FactoryGame import FGCentralStorageSubsystem
from Script.Engine import Default__KismetInputLibrary
from Script.UMG import GetViewportSize
from Script.Engine import Conv_TextToString
from Script.FactoryGame import GetBuildCategory
from Script.Engine import GetDisplayName
from Script.Engine import Not_PreBool
from Script.FactoryGame import GetItemName
from Script.FactoryGame import GetBigIcon
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import Widget_CostSlotWrapper
from Script.FactoryGame import Default__FGBuildDescriptor
from Script.Engine import NotEqual_TextText
from Script.FactoryGame import ChangeIconIndexOfPresetHotbar
from Script.FactoryGame import GetPowerProduction
from Script.FactoryGame import GetNumPresetHotbars
from Script.Engine import BooleanOR
from Script.UMG import IsVisible
from Script.FactoryGame import GetNumItems
from Script.UMG import Widget
from Script.Engine import Array_AddUnique
from Script.FactoryGame import GetBuildGun
from Script.UMG import WidgetAnimation
from Script.FactoryGame import GetItemDescription
from Script.UMG import GetOwningPlayerPawn
from Script.Engine import EqualEqual_TextText
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_CategoryButton import Widget_CategoryButton
from Script.FactoryGame import Default__FGBuildCategory
from Script.FactoryGame import FGBuildCategory
from Script.FactoryGame import GetPresetHotbar
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu_CategoryButton import Widget_BuildMenu_CategoryButton
from Script.FactoryGame import SortByName
from Script.UMG import SetRenderOpacity
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ShoppingList import Widget_ShoppingList
from Script.Engine import IsValidClass
from Script.FactoryGame import GetPowerConsumption
from Script.Engine import Concat_StrStr
from Script.FactoryGame import Default__FGInputLibrary

class Widget_BuildMenu(FGInteractWidget):
    FadeInHotbarPresetSmallIcons: Ptr[WidgetAnimation]
    FadeInCategory: Ptr[WidgetAnimation]
    mOwningBuildGun: Ptr[FGBuildGun]
    mAvailableRecipes: List[TSubclassOf[FGRecipe]]
    OnClicked: FMulticastScriptDelegate
    mOwningState: Ptr[BP_BuildGunStateMenu]
    mSelectedBuildCategory: TSubclassOf[FGBuildCategory]
    mHoveredRecipe: TSubclassOf[FGRecipe]
    mHoveredRecipeButton: Ptr[Widget_BuildMenuRecipeButton]
    mHoveredDismantleButton: Ptr[Object]
    mBuildingWidgets: List[Ptr[Widget_BuildMenuRecipeButton]]
    mShoppingList: Ptr[Widget_ShoppingList]
    mSpecialCategory: Ptr[Widget_BuildMenu_CategoryButton]
    mIsAltDown: bool
    mScrollindex: int32
    LastScrollPos: float
    ScrollPosTarget: float
    ScrollBufferActive: bool
    SearchResultHoveredTimerHandle: TimerHandle
    LastMousePos: Vector2D
    mIsSearchFocused: bool
    mSearchWaitForKeyUp: bool
    mAllBuildCategories: List[TSubclassOf[FGBuildCategory]]
    mMouseMoved: bool
    mUseMouse = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['ToggleBuildGun', 'SecondaryFire', 'ToggleSprint', 'PauseGame', 'VehicleHandbrake', 'CycleToNextHotbar', 'CycleToPreviousHotbar']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mUseGamepadCursor = True
    mCallCustomTickOnConstruct = True
    Priority = 2
    bIsFocusable = True
    
    def HideHotbarPresetInfo(self):
        self.mHotbarPresetInfoBox.SetVisibility(2)
    

    def ShowHotbarPresetInfo(self, index: int32):
        ExecutionFlow.Push("L2177")
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1)
        bSuccess1: bool = Controller1
        
        presetHotbar = None
        Controller1.GetPresetHotbar(index, Ref[presetHotbar])
        LocalPresetHotbar = presetHotbar
        self.mHotbarPresetInfoBox.mItemName.SetText(LocalPresetHotbar.PresetName)
        ReturnValue: int32 = Conv_ByteToInt(LocalPresetHotbar.IconIndex)
        
        LocalPresetHotbar.Hotbar.HotbarShortcuts = None
        Item1 = None
        Item1 = LocalPresetHotbar.Hotbar.HotbarShortcuts[ReturnValue]
        ReturnValue1_0: Ptr[Texture2D] = Item1.GetDisplayImage()
        SlateBrush.ImageSize = self.mHotbarPresetInfoBox.mPreviewIcon.Brush.ImageSize
        SlateBrush.Margin = self.mHotbarPresetInfoBox.mPreviewIcon.Brush.Margin
        SlateBrush.TintColor = self.mHotbarPresetInfoBox.mPreviewIcon.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue1_0
        SlateBrush.DrawAs = self.mHotbarPresetInfoBox.mPreviewIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mHotbarPresetInfoBox.mPreviewIcon.Brush.Tiling
        # Label 889
        SlateBrush.Mirroring = self.mHotbarPresetInfoBox.mPreviewIcon.Brush.Mirroring
        
        SlateBrush = None
        self.mHotbarPresetInfoBox.mPreviewIcon.SetBrush(Ref[SlateBrush])
        self.mHotbarPresetInfoBox.SetVisibility(0)
        ReturnValue1_1: Ptr[UMGSequencePlayer] = self.mHotbarPresetInfoBox.PlayAnimation(self.mHotbarPresetInfoBox.IconAnim, 0, 1, 0, 1)
        self.mHotbarPresetInfo_SmallIconsContainer.ClearChildren()
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        LocalPresetHotbar.Hotbar.HotbarShortcuts = None
        # Label 1255
        ReturnValue_0: int32 = len(LocalPresetHotbar.Hotbar.HotbarShortcuts)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L2056')
        Variable_0 = Variable
        ExecutionFlow.Push("L2103")
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        # Label 1440
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        
        LocalPresetHotbar.Hotbar.HotbarShortcuts = None
        Item = None
        Item = LocalPresetHotbar.Hotbar.HotbarShortcuts[Variable_0]
        ReturnValue_3: bool = Item.IsValidShortcut(Controller)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        ReturnValue_4: Ptr[BPW_HobarPreset_Editor_SmallIcon] = Default__WidgetBlueprintLibrary.Create(self, BPW_HobarPreset_Editor_SmallIcon, None)
        
        LocalPresetHotbar.Hotbar.HotbarShortcuts = None
        Item = None
        Item = LocalPresetHotbar.Hotbar.HotbarShortcuts[Variable_0]
        ReturnValue_5: Ptr[Texture2D] = Item.GetDisplayImage()
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_4, "mIcon", ReturnValue_5)
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_4, "mIndex", Variable_0)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_4, "mSmallIcon", True)
        ReturnValue_6: Ptr[PanelSlot] = self.mHotbarPresetInfo_SmallIconsContainer.AddChild(ReturnValue_4)
        goto(ExecutionFlow.Pop())
        # Label 2056
        ReturnValue_7: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.FadeInHotbarPresetSmallIcons, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 2103
        ReturnValue_8: int32 = Variable + 1
        Variable = ReturnValue_8
        goto('L1255')
    

    def OnHotbarPresetMenuButtonClicked(self, HotbarPresetIndex: int32, MenuItemIndex: int32):
        CmpSuccess: bool = MenuItemIndex != 0
        if not CmpSuccess:
            goto('L149')
        CmpSuccess = MenuItemIndex != 1
        if not CmpSuccess:
            goto('L465')
        CmpSuccess = MenuItemIndex != 2
        # Label 130
        if not CmpSuccess:
            goto('L904')
        # End
        # Label 149
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller2: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue2)
        bSuccess2: bool = Controller2
        
        presetHotbar1 = None
        Controller2.GetPresetHotbar(HotbarPresetIndex, Ref[presetHotbar1])
        LocalShortcuts = presetHotbar1.Hotbar.HotbarShortcuts
        ReturnValue1: int32 = Conv_ByteToInt(presetHotbar1.IconIndex)
        
        self.mHotbarPresetEditor.OnOpen(presetHotbar1.PresetName, ReturnValue1, HotbarPresetIndex, Ref[LocalShortcuts])
        # End
        # Label 465
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        
        presetHotbar = None
        Controller.GetPresetHotbar(HotbarPresetIndex, Ref[presetHotbar])
        ReturnValue = self.GetOwningPlayer()
        # Label 628
        Controller = Cast[FGPlayerController](ReturnValue)
        bSuccess = Controller
        shortcuts: List[Ptr[FGHotbarShortcut]] = []
        
        Controller.GetCurrentShortcuts(Ref[shortcuts])
        LocalShortcuts = shortcuts
        ReturnValue_0: int32 = Conv_ByteToInt(presetHotbar.IconIndex)
        
        self.mHotbarPresetEditor.OnOpen(presetHotbar.PresetName, ReturnValue_0, HotbarPresetIndex, Ref[LocalShortcuts])
        # End
        # Label 904
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1_0)
        bSuccess1: bool = Controller1
        ReturnValue_1: bool = Controller1.RemovePresetHotbar(HotbarPresetIndex)
        if not ReturnValue_1:
            goto('L1072')
        self.InitPresetHotbars()
    

    def OnHotbarPresetUpdated(self, Name: FText, IconIndex: int32, PresetIndex: int32, ShouldOverwrite: bool):
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller3: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue3)
        bSuccess3: bool = Controller3
        ReturnValue: int32 = Controller3.GetNumPresetHotbars()
        ReturnValue_0: bool = GreaterEqual_IntInt(PresetIndex, ReturnValue)
        # Label 177
        if not ReturnValue_0:
            goto('L373')
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        # Label 215
        Controller2: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue2)
        bSuccess2: bool = Controller2
        
        ReturnValue_1: bool = Controller2.CreatePresetHotbarFromCurrentHotbar(IconIndex, Ref[Name])
        if not ReturnValue_1:
            goto('L810')
        # Label 354
        self.InitPresetHotbars()
        # Label 368
        # End
        # Label 373
        if not ShouldOverwrite:
            goto('L527')
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        ReturnValue_3: bool = Controller.CopyCurrentHotbarToPresetHotbar(PresetIndex)
        # Label 527
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1)
        # Label 587
        bSuccess1: bool = Controller1
        
        Controller1.ChangeNameOfPresetHotbar(PresetIndex, Ref[Name])
        ReturnValue1 = self.GetOwningPlayer()
        Controller1 = Cast[FGPlayerController](ReturnValue1)
        bSuccess1 = Controller1
        Controller1.ChangeIconIndexOfPresetHotbar(PresetIndex, IconIndex)
        goto('L354')
    

    def OnAddHotbarPreset(self):
        1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': 'Temp Name'}"
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        ReturnValue_0: bool = Controller.CanCreateNewPresetHotbar()
        if not ReturnValue_0:
            goto('L601')
        ReturnValue = self.GetOwningPlayer()
        Controller = Cast[FGPlayerController](ReturnValue)
        bSuccess = Controller
        shortcuts: List[Ptr[FGHotbarShortcut]] = []
        
        Controller.GetCurrentShortcuts(Ref[shortcuts])
        ReturnValue = self.GetOwningPlayer()
        Controller = Cast[FGPlayerController](ReturnValue)
        bSuccess = Controller
        ReturnValue_1: int32 = Controller.GetNumPresetHotbars()
        
        self.mHotbarPresetEditor.OnOpen("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 529, 'Value': 'New Preset'}", 0, ReturnValue_1, Ref[shortcuts])
    

    def InitPresetHotbars(self):
        ExecutionFlow.Push("L1237")
        self.mHotbarPresetContainer.ClearChildren()
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1)
        bSuccess1: bool = Controller1
        # Label 130
        presetHotbars: List[PresetHotbar] = []
        
        Controller1.GetAllPresetHotbars(Ref[presetHotbars])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 228
        ReturnValue: int32 = len(presetHotbars)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L853')
        Variable_0 = Variable
        # Label 366
        ExecutionFlow.Push("L1163")
        ReturnValue_1: Ptr[BPW_HotbarPreset_Button] = Default__WidgetBlueprintLibrary.Create(self, BPW_HotbarPreset_Button, None)
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_1, "mIndex", Variable_0)
        
        Item = None
        Item = presetHotbars[Variable_0]
        
        Item = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_1, "mPresetHotbar", Ref[Item])
        ReturnValue_2: Ptr[PanelSlot] = self.mHotbarPresetContainer.AddChild(ReturnValue_1)
        OutputDelegate2.BindUFunction(self, OnHotbarPresetMenuButtonClicked)
        ReturnValue_1.OnMenuItemClicked.AddUnique(OutputDelegate2)
        OutputDelegate1.BindUFunction(self, ShowHotbarPresetInfo)
        ReturnValue_1.OnHotbarPresetHovered.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, HideHotbarPresetInfo)
        ReturnValue_1.OnHotbarPresetUnhovered.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 853
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_3)
        bSuccess: bool = Controller
        ReturnValue_4: bool = Controller.CanCreateNewPresetHotbar()
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        ReturnValue1_0: Ptr[BPW_AddHotbarPreset_Button] = Default__WidgetBlueprintLibrary.Create(self, BPW_AddHotbarPreset_Button, None)
        ReturnValue1_1: Ptr[PanelSlot] = self.mHotbarPresetContainer.AddChild(ReturnValue1_0)
        OutputDelegate3.BindUFunction(self, OnAddHotbarPreset)
        ReturnValue1_0.OnAddHotbarPresetClicked.AddUnique(OutputDelegate3)
        goto(ExecutionFlow.Pop())
        # Label 1163
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L228')
    

    def GetShortcutKeys(self):
        ExecutionFlow.Push("L587")
        Variable: int32 = 0
        # Label 28
        ReturnValue: bool = Variable <= 9
        if not ReturnValue:
            goto('L481')
        ExecutionFlow.Push("L513")
        ReturnValue_0: int32 = Variable + 1
        ReturnValue_1: FString = Default__KismetStringLibrary.Conv_IntToString(ReturnValue_0)
        ReturnValue_2: FString = Default__KismetStringLibrary.Concat_StrStr("Shortcut", ReturnValue_1)
        ReturnValue_3: FName = Default__KismetStringLibrary.Conv_StringToName(ReturnValue_2)
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: InputActionKeyMapping = Default__FGInputLibrary.GetKeyMappingForAction(ReturnValue_4, ReturnValue_3, False)
        
        ReturnValue_5.Key = None
        ReturnValue_6: int32 = LocalShorcutKeys.append(ReturnValue_5.Key)
        goto(ExecutionFlow.Pop())
        # Label 481
        ShortcutKeys = LocalShorcutKeys
        # End
        # Label 513
        ReturnValue1: int32 = Variable + 1
        Variable = ReturnValue1
        goto('L28')
    

    def GetShouldSearchResultBeBoundToHotbar(self, KeyEvent: Const[Ref[KeyEvent]]):
        
        ShortcutKeys = None
        self.GetShortcutKeys(Ref[ShortcutKeys])
        
        ReturnValue: Key = Default__KismetInputLibrary.GetKey(Ref[KeyEvent])
        
        ShortcutKeys = None
        ReturnValue_0: bool = Default__KismetArrayLibrary.Array_Contains(Ref[ShortcutKeys], Ref[ReturnValue])
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: bool = self.mSearchResultsContainer.IsHovered()
        ReturnValue_3: bool = self.mSearchbar.HasUserFocusedDescendants(ReturnValue_1)
        ReturnValue_4: bool = ReturnValue_0 and ReturnValue_3
        ReturnValue1: bool = ReturnValue_4 and ReturnValue_2
        ReturnValue2: bool = ReturnValue1 and self.mMouseMoved
        ReturnValue_5: bool = ReturnValue2
    

    def OnMouseMove(self):
        self.mMouseMoved = True
        ReturnValue: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_0: EventReply = ReturnValue
    

    def OnPreviewKeyDown(self):
        ExecutionFlow.Push("L2065")
        Array: List[Key] = [Key(KeyName = "Zero"), Key(KeyName = "One"), Key(KeyName = "Two"), Key(KeyName = "Three"), Key(KeyName = "Four"), Key(KeyName = "Five"), Key(KeyName = "Six"), Key(KeyName = "Seven"), Key(KeyName = "Eight"), Key(KeyName = "Nine")]
        # Label 286
        0: List[Key] = Array
        ExecutionFlow.Push("L405")
        
        ReturnValue: bool = self.GetShouldSearchResultBeBoundToHotbar(Ref[InKeyEvent])
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        self.SetUserFocus(ReturnValue2)
        goto(ExecutionFlow.Pop())
        
        # Label 405
        ReturnValue_0: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_1: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue_0, Key(KeyName = "Down"))
        ReturnValue1: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue_0, Key(KeyName = "Up"))
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: InputActionKeyMapping = Default__FGInputLibrary.GetKeyMappingForAction(ReturnValue1_0, "CycleToPreviousHotbar", False)
        ReturnValue1_1: InputActionKeyMapping = Default__FGInputLibrary.GetKeyMappingForAction(ReturnValue1_0, "CycleToNextHotbar", False)
        ReturnValue2_0: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue_0, ReturnValue_2.Key)
        ReturnValue3: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue_0, ReturnValue1_1.Key)
        ReturnValue_3: bool = ReturnValue2_0 and ReturnValue_1
        # Label 966
        ReturnValue1_2: bool = ReturnValue3 and ReturnValue1
        ReturnValue_4: bool = BooleanOR(ReturnValue1_1.bShift, ReturnValue1_1.bCtrl)
        ReturnValue1_3: bool = BooleanOR(ReturnValue_2.bShift, ReturnValue_2.bCtrl)
        ReturnValue2_1: bool = BooleanOR(ReturnValue_4, ReturnValue1_1.bAlt)
        # Label 1163
        ReturnValue3_0: bool = BooleanOR(ReturnValue1_3, ReturnValue_2.bAlt)
        ReturnValue4: bool = BooleanOR(ReturnValue2_1, ReturnValue1_1.bCmd)
        ReturnValue5: bool = BooleanOR(ReturnValue3_0, ReturnValue_2.bCmd)
        ReturnValue_5: bool = Not_PreBool(ReturnValue4)
        ReturnValue1_4: bool = Not_PreBool(ReturnValue5)
        ReturnValue2_2: bool = ReturnValue1_2 and ReturnValue_5
        ReturnValue3_1: bool = ReturnValue_3 and ReturnValue1_4
        ReturnValue6: bool = BooleanOR(ReturnValue2_2, ReturnValue3_1)
        if not ReturnValue6:
            goto('L1946')
        ReturnValue_6: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_6)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L1946')
        
        ReturnValue_0 = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue1_0 = self.GetOwningPlayer()
        ReturnValue1_1 = Default__FGInputLibrary.GetKeyMappingForAction(ReturnValue1_0, "CycleToNextHotbar", False)
        ReturnValue3 = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue_0, ReturnValue1_1.Key)
        if not ReturnValue3:
            goto('L2028')
        Controller.CycleToNextHotbar()
        # Label 1864
        ReturnValue_7: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_8: EventReply = ReturnValue_7
        goto('L2065')
        # Label 1946
        ReturnValue_9: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_8 = ReturnValue_9
        goto('L2065')
        # Label 2028
        Controller.CycleToPreviousHotbar()
        goto('L1864')
    

    def SaveCategories(self):
        self.mOwningState.mLastSelectedBuildCategory = self.mSelectedBuildCategory
    

    def OnCategoryClicked(self, index: int32):
        
        Item = None
        Item = self.mAllBuildCategories[index]
        ReturnValue: bool = NotEqual_ClassClass(Item, self.mSelectedBuildCategory)
        if not ReturnValue:
            goto('L217')
        
        Item = None
        Item = self.mAllBuildCategories[index]
        self.mSelectedBuildCategory = Item
        self.PopulateBuildings()
        self.SetSearchbarUnfocused()
    

    def SetSearchbarUnfocused(self):
        self.mIsSearchFocused = False
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        self.SetUserFocus(ReturnValue)
        self.ClearAndHideSearchResults()
    

    def SetSearchbarFocused(self):
        self.mIsSearchFocused = True
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mSearchbar.mInputBox.SetUserFocus(ReturnValue)
        self.mSearchbar.mInputBox.SetText()
    

    def IsShortcutSettingAllowed(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mHoveredRecipeButton)
        # Label 51
        if not ReturnValue:
            goto('L357')
        ReturnValue_0: bool = self.mHoveredRecipeButton.Widget_ShoppingListButton.mInputNumberToAdd.IsVisible()
        ReturnValue_1: bool = self.mHoveredRecipeButton.Widget_ShoppingListButton.mInputNumberToAdd.HasKeyboardFocus()
        ReturnValue_2: bool = Not_PreBool(ReturnValue_0)
        ReturnValue1: bool = Not_PreBool(ReturnValue_1)
        ReturnValue_3: bool = BooleanOR(ReturnValue1, ReturnValue_2)
        ReturnValue_4: bool = ReturnValue_3
        goto('L368')
        # Label 357
        ReturnValue_4 = False
    

    def ClearAndHideSearchResults(self):
        self.mSearchResultsContainer.ClearChildren()
        self.mSubCategoriesContainer.SetVisibility(4)
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.SearchResultHoveredTimerHandle])
    

    def OnSearchCreateResults(self, mText: FText):
        ExecutionFlow.Push("L1718")
        localSearchResult = mText
        self.BlockMouse()
        ReturnValue: FText = Default__KismetTextLibrary.Conv_StringToText("")
        
        ReturnValue_0: bool = Default__KismetTextLibrary.NotEqual_TextText(Ref[localSearchResult], Ref[ReturnValue])
        if not ReturnValue_0:
            goto('L1425')
        self.mSubCategoriesContainer.SetVisibility(1)
        OutputDelegate3.BindUFunction(self, CheckSearchResultHover)
        ReturnValue_1: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate3, 0.10000000149011612, True)
        self.SearchResultHoveredTimerHandle = ReturnValue_1
        self.mSearchResultsContainer.ClearChildren()
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 407
        ReturnValue_2: int32 = len(self.mAvailableRecipes)
        ReturnValue_3: bool = Variable <= ReturnValue_2
        if not ReturnValue_3:
            goto('L1440')
        Variable_0 = Variable
        ExecutionFlow.Push("L1644")
        
        Item = None
        Item = self.mAvailableRecipes[Variable_0]
        localRecipe = Item
        # Label 628
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValidClass(localRecipe)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        
        ReturnValue_5: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[localSearchResult])
        ReturnValue_6: bool = Default__KismetStringLibrary.EqualEqual_StriStri(ReturnValue_5, "")
        ReturnValue_7: FText = Default__FGRecipe.GetRecipeName(localRecipe)
        
        ReturnValue1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_7])
        ReturnValue_8: bool = Default__BPHUDHelpers.DoesTextContainSearchWords(ReturnValue1, ReturnValue_5, True, self)
        ReturnValue_9: bool = BooleanOR(ReturnValue_8, ReturnValue_6)
        if not ReturnValue_9:
           goto(ExecutionFlow.Pop())
        ReturnValue_10: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_11: Ptr[Widget_BuildMenuRecipeButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_BuildMenuRecipeButton, ReturnValue_10)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_11, "mRecipe", localRecipe)
        ReturnValue_12: Ptr[VerticalBoxSlot] = self.mSearchResultsContainer.AddChildToVerticalBox(ReturnValue_11)
        OutputDelegate2.BindUFunction(self, OnRecipeClicked)
        # Label 1255
        ReturnValue_11.OnRecipeClicked.AddUnique(OutputDelegate2)
        OutputDelegate1.BindUFunction(self, OnRecipeHovered)
        ReturnValue_11.OnRecipeHovered.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, OnStopHoveringRecipe)
        ReturnValue_11.OnStopHoveringRecipe.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 1425
        self.ClearAndHideSearchResults()
        goto(ExecutionFlow.Pop())
        # Label 1440
        ReturnValue_13: Ptr[Widget] = self.mSearchResultsContainer.GetChildAt(0)
        Button: Ptr[Widget_BuildMenuRecipeButton] = Cast[Widget_BuildMenuRecipeButton](ReturnValue_13)
        bSuccess: bool = Button
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Button.SimulateOnHovered()
        self.CreateInfoBox(Button.mRecipe)
        goto(ExecutionFlow.Pop())
        # Label 1644
        ReturnValue_14: int32 = Variable + 1
        Variable = ReturnValue_14
        goto('L407')
    

    def OnKeyDown(self):
        Array: List[Key] = [Key(KeyName = "Zero"), Key(KeyName = "One"), Key(KeyName = "Two"), Key(KeyName = "Three"), Key(KeyName = "Four"), Key(KeyName = "Five"), Key(KeyName = "Six"), Key(KeyName = "Seven"), Key(KeyName = "Eight"), Key(KeyName = "Nine")]
        LocalNumKeys = Array
        
        ReturnValue: InputEvent = Default__WidgetBlueprintLibrary.GetInputEventFromKeyEvent(Ref[InKeyEvent])
        
        ReturnValue_0: bool = Default__KismetInputLibrary.InputEvent_IsAltDown(Ref[ReturnValue])
        self.mIsAltDown = ReturnValue_0
        ReturnValue_1: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_2: EventReply = ReturnValue_1
    

    def PopulateBuildings(self):
        ExecutionFlow.Push("L2266")
        self.mSubCategoriesContainer.ClearChildren()
        
        Default__FGBlueprintFunctionLibrary.GetAvailableSubCategoriesForCategory(self.mOwningBuildGun, self.mSelectedBuildCategory, Ref[subCategories])
        Variable1: int32 = 0
        Variable1_0: int32 = 0
        
        # Label 146
        ReturnValue: int32 = len(subCategories)
        ReturnValue_0: bool = Variable1 <= ReturnValue
        if not ReturnValue_0:
            goto('L1848')
        Variable1_0 = Variable1
        ExecutionFlow.Push("L1895")
        # Label 289
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[Widget_BuildMenu_SubCategoryButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_BuildMenu_SubCategoryButton, ReturnValue1)
        
        Item1 = None
        Item1 = subCategories[Variable1_0]
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_1, "mSubCategory", Item1)
        ReturnValue_2: Ptr[VerticalBoxSlot] = self.mSubCategoriesContainer.AddChildToVerticalBox(ReturnValue_1)
        ReturnValue_2.SetVerticalAlignment(1)
        
        Item1 = None
        Item1 = subCategories[Variable1_0]
        ReturnValue_1.GetSubcategoryNameTest(Item1)
        ReturnValue_1.mBuildingsContainer.ClearChildren()
        
        Default__KismetArrayLibrary.Array_Clear(Ref[recipesInCategory])
        
        Item1 = None
        Item1 = subCategories[Variable1_0]
        
        Default__FGBlueprintFunctionLibrary.GetAvailableRecipesInSubCategory(self.mOwningBuildGun, self.mSelectedBuildCategory, Item1, Ref[recipesInCategory])
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mBuildingWidgets])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 998
        ReturnValue1_0: int32 = len(recipesInCategory)
        ReturnValue1_1: bool = Variable <= ReturnValue1_0
        if not ReturnValue1_1:
            goto('L1969')
        Variable_0 = Variable
        ExecutionFlow.Push("L2192")
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_2: Ptr[Widget_BuildMenuRecipeButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_BuildMenuRecipeButton, ReturnValue2)
        
        Item = None
        Item = recipesInCategory[Variable_0]
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue1_2, "mRecipe", Item)
        
        Item = None
        Item = recipesInCategory[Variable_0]
        
        CanAfford = None
        self.CanAffordRecipe(Item, Ref[CanAfford])
        ReturnValue1_2.mCanAfford = CanAfford
        ReturnValue_3: Ptr[WrapBoxSlot] = ReturnValue_1.mBuildingsContainer.AddChildToWrapBox(ReturnValue1_2)
        ReturnValue_3.SetHorizontalAlignment(1)
        OutputDelegate1.BindUFunction(self, OnRecipeHovered)
        ReturnValue1_2.OnRecipeHovered.AddUnique(OutputDelegate1)
        OutputDelegate2.BindUFunction(self, OnRecipeClicked)
        ReturnValue1_2.OnRecipeClicked.AddUnique(OutputDelegate2)
        OutputDelegate.BindUFunction(self, OnStopHoveringRecipe)
        ReturnValue1_2.OnStopHoveringRecipe.AddUnique(OutputDelegate)
        
        ReturnValue_4: int32 = self.mBuildingWidgets.append(ReturnValue1_2)
        goto(ExecutionFlow.Pop())
        # Label 1848
        ReturnValue_5: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.FadeInCategory, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 1895
        ReturnValue1_3: int32 = Variable1 + 1
        Variable1 = ReturnValue1_3
        goto('L146')
        # Label 1969
        ReturnValue_6: Ptr[Widget] = ReturnValue_1.mBuildingsContainer.GetChildAt(0)
        # Label 2038
        self.SetDefaultFocusWidget(ReturnValue_6)
        ReturnValue_7: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_6 = ReturnValue_1.mBuildingsContainer.GetChildAt(0)
        ReturnValue_6.SetUserFocus(ReturnValue_7)
        # Label 2191
        goto(ExecutionFlow.Pop())
        # Label 2192
        ReturnValue_8: int32 = Variable + 1
        Variable = ReturnValue_8
        goto('L998')
    

    def UpdateShortcuts(self):
        ExecutionFlow.Push("L360")
        Variable: int32 = 0
        # Label 28
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(self.mBuildingWidgets)
        # Label 110
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L286")
        
        Item = None
        Item = self.mBuildingWidgets[Variable_0]
        Item.ResolveHotkeyIndex()
        goto(ExecutionFlow.Pop())
        # Label 286
        ReturnValue_1: int32 = Variable + 1
        Variable = ReturnValue_1
        goto('L51')
    

    def HandleShortcutPressed(self, shortcutIndex: int32):
        ReturnValue: bool = self.IsShortcutSettingAllowed()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValidClass(self.mHoveredRecipe)
        ReturnValue_1: bool = ReturnValue_0 and ReturnValue
        if not ReturnValue_1:
            goto('L291')
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        Controller.SetRecipeShortcutOnIndex(self.mHoveredRecipe, shortcutIndex)
        self.UpdateShortcuts()
        setupNewShortcut = True
    

    def OnStopHoveringRecipe(self, Recipe: TSubclassOf[FGRecipe], RecipeButton: Ptr[Widget_BuildMenuRecipeButton]):
        ExecutionFlow.Push("L130")
        ExecutionFlow.Push("L70")
        ReturnValue: bool = EqualEqual_ClassClass(Recipe, self.mHoveredRecipe)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        self.mHoveredRecipe = None
        goto(ExecutionFlow.Pop())
        # Label 70
        ReturnValue_0: bool = EqualEqual_ObjectObject(RecipeButton, self.mHoveredRecipeButton)
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        self.mHoveredRecipeButton = None
        goto(ExecutionFlow.Pop())
    

    def OnRecipeHovered(self, Recipe: TSubclassOf[FGRecipe], RecipeButton: Ptr[Widget_BuildMenuRecipeButton]):
        self.mHoveredRecipeButton = RecipeButton
        self.mHoveredRecipe = Recipe
        self.CreateInfoBox(self.mHoveredRecipe)
    

    def OnKeyUp(self):
        KeyEvent = InKeyEvent
        
        ReturnValue: InputEvent = Default__WidgetBlueprintLibrary.GetInputEventFromKeyEvent(Ref[KeyEvent])
        
        ReturnValue_0: bool = Default__KismetInputLibrary.InputEvent_IsAltDown(Ref[ReturnValue])
        self.mIsAltDown = ReturnValue_0
        ReturnValue_1: bool = EqualEqual_IntInt(self.Widget_SlidingTabs.mActiveIndex, 0)
        ReturnValue_2: bool = Not_PreBool(self.mSearchWaitForKeyUp)
        
        ReturnValue_3: Key = Default__KismetInputLibrary.GetKey(Ref[KeyEvent])
        ReturnValue_4: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue_3, Key(KeyName = "SpaceBar"))
        ReturnValue1: bool = Not_PreBool(self.mIsSearchFocused)
        # Label 407
        ReturnValue_5: bool = ReturnValue_4 and ReturnValue1
        ReturnValue1_0: bool = ReturnValue_5 and ReturnValue_2
        ReturnValue2: bool = ReturnValue1_0 and ReturnValue_1
        if not ReturnValue2:
            goto('L873')
        self.SetSearchbarFocused()
        # Label 549
        ReturnValue_6: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_6)
        bSuccess: bool = Controller
        
        ReturnValue_7: int32 = Controller.GetShortcutIndexFromKey(Ref[KeyEvent])
        ReturnValue_8: bool = ReturnValue_7 != -1
        if not ReturnValue_8:
            goto('L889')
        
        setupNewShortcut = None
        self.HandleShortcutPressed(ReturnValue_7, Ref[setupNewShortcut])
        if not setupNewShortcut:
            goto('L889')
        ReturnValue_9: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_10: EventReply = ReturnValue_9
        goto('L966')
        # Label 873
        self.mSearchWaitForKeyUp = False
        goto('L549')
        # Label 889
        ReturnValue_11: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_10 = ReturnValue_11
    

    def IsCentralStorageBuilt(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_0: Ptr[FGCentralStorageSubsystem] = Default__FGCentralStorageSubsystem.Get(ReturnValue)
        ReturnValue_1: bool = ReturnValue_0.IsCentralStorageBuilt()
        IsBuilt = ReturnValue_1
    

    def IsSpaceElevatorBuilt(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue)
        bSuccess: bool = State
        ReturnValue_0: bool = State.IsSpaceElevatorBuilt()
        IsBuilt = ReturnValue_0
    

    def IsTradingPostBuilt(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue)
        bSuccess: bool = State
        ReturnValue_0: bool = State.IsTradingPostBuilt()
        IsBuilt = ReturnValue_0
    

    def GetInfoboxVisiblity(self):
        self.BuildMenu_InfoBox.SetVisibility(2)
    

    def InitBuildMenu(self):
        ReturnValue: Ptr[FGBuildGun] = self.mOwningState.GetBuildGun()
        self.mOwningBuildGun = ReturnValue
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mOwningBuildGun)
        if not ReturnValue_0:
            goto('L265')
        recipes: List[TSubclassOf[FGRecipe]] = []
        
        self.mOwningBuildGun.GetAvailableRecipes(Ref[recipes])
        self.mAvailableRecipes = recipes
        
        Default__FGRecipe.SortByName(Ref[self.mAvailableRecipes])
        self.GetInfoboxVisiblity()
        # End
        # Label 265
        ReturnValue_1: FString = Default__KismetSystemLibrary.GetDisplayName(self)
        ReturnValue_2: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_1, " failed to initialize owning build gun.")
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_2, True, True, LinearColor(R = 1, G = 0, B = 0, A = 1), 2)
    

    def OnRecipeClicked(self, InputPin: TSubclassOf[FGRecipe]):
        self.mOwningBuildGun.GotoBuildState(InputPin)
    

    def CreateInfoBox(self, Recipe: TSubclassOf[FGRecipe]):
        ExecutionFlow.Push("L4295")
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(Recipe)
        Variable: uint8 = 2
        Variable1: uint8 = 0
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable,
            True: Variable1
        }
        self.BuildMenu_InfoBox.SetVisibility(switch.get(Variable_0, None))
        self.BuildMenu_InfoBox.mStatContainer.ClearChildren()
        self.BuildMenu_InfoBox.mCostContainer.ClearChildren()
        Variable_1: int32 = 0
        Variable_2: int32 = 0
        
        # Label 366
        ReturnValue_0: int32 = len(self.mAvailableRecipes)
        ReturnValue_1: bool = Variable_1 <= ReturnValue_0
        if not ReturnValue_1:
            goto('L1471')
        Variable_2 = Variable_1
        ExecutionFlow.Push("L3586")
        
        Item1 = None
        Item1 = self.mAvailableRecipes[Variable_2]
        ReturnValue_2: bool = EqualEqual_ClassClass(Item1, Recipe)
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        Variable1_0: int32 = 0
        Variable1_1: int32 = 0
        
        Item1 = None
        # Label 662
        Item1 = self.mAvailableRecipes[Variable_2]
        ReturnValue_3: List[ItemAmount] = self.mOwningBuildGun.GetCostForRecipe(Item1)
        
        ReturnValue1: int32 = len(ReturnValue_3)
        ReturnValue1_0: bool = Variable1_0 <= ReturnValue1
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        Variable1_1 = Variable1_0
        ExecutionFlow.Push("L3660")
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue2_0: Ptr[Widget_CostSlotWrapper] = Default__WidgetBlueprintLibrary.Create(self, Widget_CostSlotWrapper, ReturnValue2)
        ReturnValue2_1: Ptr[WrapBoxSlot] = self.BuildMenu_InfoBox.mCostContainer.AddChildToWrapBox(ReturnValue2_0)
        ReturnValue_4: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        Item1 = None
        Item1 = self.mAvailableRecipes[Variable_2]
        ReturnValue_3 = self.mOwningBuildGun.GetCostForRecipe(Item1)
        
        Item2 = None
        Item2 = ReturnValue_3[Variable1_1]
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue_4, Item2.ItemClass, self, Ref[numItems])
        ReturnValue2_0.Setup CostIcon(None, Item2, None, 0, numItems, False, False, False)
        ReturnValue2_0.mCostSlotContainer.SetRenderOpacity(0)
        goto(ExecutionFlow.Pop())
        # Label 1471
        ReturnValue_5: List[ItemAmount] = Default__FGRecipe.GetProducts(Recipe, False)
        
        Item = None
        Item = ReturnValue_5[0]
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValidClass(Item.ItemClass)
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L4258")
        ExecutionFlow.Push("L3734")
        ExecutionFlow.Push("L3062")
        ReturnValue_5 = Default__FGRecipe.GetProducts(Recipe, False)
        
        Item = None
        Item = ReturnValue_5[0]
        ReturnValue_6: FText = Default__FGItemDescriptor.GetItemName(Item.ItemClass)
        self.BuildMenu_InfoBox.mItemName.SetText(ReturnValue_6)
        ReturnValue_5 = Default__FGRecipe.GetProducts(Recipe, False)
        
        Item = None
        Item = ReturnValue_5[0]
        ReturnValue_7: FText = Default__FGItemDescriptor.GetItemDescription(Item.ItemClass)
        
        self.BuildMenu_InfoBox.mRichTextBlock.SetText(Ref[ReturnValue_7])
        ReturnValue_5 = Default__FGRecipe.GetProducts(Recipe, False)
        
        Item = None
        Item = ReturnValue_5[0]
        ReturnValue_8: Ptr[Texture2D] = Default__FGItemDescriptor.GetBigIcon(Item.ItemClass)
        SlateBrush.ImageSize = self.BuildMenu_InfoBox.mPreviewIcon.Brush.ImageSize
        SlateBrush.Margin = self.BuildMenu_InfoBox.mPreviewIcon.Brush.Margin
        SlateBrush.TintColor = self.BuildMenu_InfoBox.mPreviewIcon.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue_8
        SlateBrush.DrawAs = self.BuildMenu_InfoBox.mPreviewIcon.Brush.DrawAs
        SlateBrush.Tiling = self.BuildMenu_InfoBox.mPreviewIcon.Brush.Tiling
        SlateBrush.Mirroring = self.BuildMenu_InfoBox.mPreviewIcon.Brush.Mirroring
        
        SlateBrush = None
        self.BuildMenu_InfoBox.mPreviewIcon.SetBrush(Ref[SlateBrush])
        ReturnValue_9: Ptr[UMGSequencePlayer] = self.BuildMenu_InfoBox.PlayAnimation(self.BuildMenu_InfoBox.IconAnim, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 3062
        ReturnValue_5 = Default__FGRecipe.GetProducts(Recipe, False)
        
        Item = None
        Item = ReturnValue_5[0]
        Descriptor1: TSubclassOf[FGBuildingDescriptor] = ClassCast[FGBuildingDescriptor](Item.ItemClass)
        bSuccess1: bool = Descriptor1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue_10: float = Default__FGBuildingDescriptor.GetPowerProduction(Descriptor1)
        ReturnValue1_2: bool = ReturnValue_10 > 0.10000000149011612
        if not ReturnValue1_2:
           goto(ExecutionFlow.Pop())
        ReturnValue1_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_4: Ptr[Widget_BuildMenu_PowerProduction] = Default__WidgetBlueprintLibrary.Create(self, Widget_BuildMenu_PowerProduction, ReturnValue1_3)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue1_4, "mBuildingDesc", Descriptor1)
        ReturnValue1_5: Ptr[WrapBoxSlot] = self.BuildMenu_InfoBox.mStatContainer.AddChildToWrapBox(ReturnValue1_4)
        goto(ExecutionFlow.Pop())
        # Label 3586
        ReturnValue_11: int32 = Variable_1 + 1
        Variable_1 = ReturnValue_11
        goto('L366')
        # Label 3660
        ReturnValue1_6: int32 = Variable1_0 + 1
        Variable1_0 = ReturnValue1_6
        goto('L662')
        # Label 3734
        ReturnValue_5 = Default__FGRecipe.GetProducts(Recipe, False)
        
        Item = None
        Item = ReturnValue_5[0]
        Descriptor: TSubclassOf[FGBuildingDescriptor] = ClassCast[FGBuildingDescriptor](Item.ItemClass)
        bSuccess: bool = Descriptor
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_12: float = Default__FGBuildingDescriptor.GetPowerConsumption(Descriptor)
        ReturnValue_13: bool = ReturnValue_12 > 0.10000000149011612
        if not ReturnValue_13:
           goto(ExecutionFlow.Pop())
        ReturnValue_14: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_15: Ptr[Widget_BuildMenu_PowerProduction] = Default__WidgetBlueprintLibrary.Create(self, Widget_BuildMenu_PowerProduction, ReturnValue_14)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_15, "mBuildingDesc", Descriptor)
        ReturnValue_16: Ptr[WrapBoxSlot] = self.BuildMenu_InfoBox.mStatContainer.AddChildToWrapBox(ReturnValue_15)
        goto(ExecutionFlow.Pop())
        # Label 4258
        self.BuildMenu_InfoBox.AnimateCostSlots()
        goto(ExecutionFlow.Pop())
    

    def CreateCategoryButtons(self):
        ExecutionFlow.Push("L2265")
        
        Default__FGBlueprintFunctionLibrary.GetAllBuildCategories(self.mOwningBuildGun, Ref[self.mAllBuildCategories])
        ExecutionFlow.Push("L931")
        Variable1: int32 = 0
        Variable2: int32 = 0
        
        # Label 106
        ReturnValue2: int32 = len(self.mAvailableRecipes)
        ReturnValue2_0: bool = Variable1 <= ReturnValue2
        if not ReturnValue2_0:
           goto(ExecutionFlow.Pop())
        Variable2 = Variable1
        ExecutionFlow.Push("L2117")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        Item1 = None
        # Label 291
        Item1 = self.mAvailableRecipes[Variable2]
        ReturnValue: List[ItemAmount] = Default__FGRecipe.GetProducts(Item1, False)
        
        ReturnValue1: int32 = len(ReturnValue)
        ReturnValue1_0: bool = Variable <= ReturnValue1
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L2191")
        
        Item1 = None
        # Label 549
        Item1 = self.mAvailableRecipes[Variable2]
        ReturnValue = Default__FGRecipe.GetProducts(Item1, False)
        
        Item2 = None
        Item2 = ReturnValue[Variable_0]
        Descriptor: TSubclassOf[FGBuildingDescriptor] = ClassCast[FGBuildingDescriptor](Item2.ItemClass)
        bSuccess: bool = Descriptor
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_0: TSubclassOf[FGBuildCategory] = Default__FGBuildDescriptor.GetBuildCategory(Descriptor)
        
        ReturnValue_1: int32 = Default__KismetArrayLibrary.Array_AddUnique(Ref[unlockedCategories], Ref[ReturnValue_0])
        goto(ExecutionFlow.Pop())
        # Label 931
        Variable2_0: int32 = 0
        Variable1_0: int32 = 0
        
        # Label 977
        ReturnValue_2: int32 = len(self.mAllBuildCategories)
        ReturnValue_3: bool = Variable2_0 <= ReturnValue_2
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Variable1_0 = Variable2_0
        ExecutionFlow.Push("L2043")
        
        Item = None
        Item = self.mAllBuildCategories[Variable1_0]
        LocalCategory = Item
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: Ptr[Widget_CategoryButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_CategoryButton, ReturnValue_4)
        
        ReturnValue_6: int32 = Default__KismetArrayLibrary.Array_Find(Ref[unlockedCategories], Ref[LocalCategory])
        ReturnValue_7: bool = ReturnValue_6 != -1
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_5, "mIsCategoryVisible", ReturnValue_7)
        ReturnValue_8: FText = Default__FGBuildCategory.GetCategoryName(LocalCategory)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_5, "mName", Ref[ReturnValue_8])
        ReturnValue_9: SlateBrush = Default__FGBuildCategory.GetCategoryIcon(LocalCategory)
        
        ReturnValue_10: Ptr[Texture2D] = Default__WidgetBlueprintLibrary.GetBrushResourceAsTexture2D(Ref[ReturnValue_9])
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_5, "mIcon", ReturnValue_10)
        LocalCategoryButton = ReturnValue_5
        ReturnValue_11: Ptr[VerticalBoxSlot] = self.mCategoryButtonsContainer.Container.AddChildToVerticalBox(LocalCategoryButton)
        OutputDelegate.BindUFunction(self, OnCategoryClicked)
        LocalCategoryButton.OnClicked.AddUnique(OutputDelegate)
        # Label 1895
        ReturnValue_12: bool = EqualEqual_ClassClass(LocalCategory, self.mOwningState.mLastSelectedBuildCategory)
        if not ReturnValue_12:
           goto(ExecutionFlow.Pop())
        LocalCategoryButton.SetAsSelected()
        self.mSelectedBuildCategory = self.mOwningState.mLastSelectedBuildCategory
        goto(ExecutionFlow.Pop())
        # Label 2043
        ReturnValue2_1: int32 = Variable2_0 + 1
        Variable2_0 = ReturnValue2_1
        goto('L977')
        # Label 2117
        ReturnValue1_1: int32 = Variable1 + 1
        Variable1 = ReturnValue1_1
        goto('L106')
        # Label 2191
        ReturnValue_13: int32 = Variable + 1
        Variable = ReturnValue_13
        goto('L291')
    

    def CanAffordRecipe(self, Recipe: TSubclassOf[FGRecipe]):
        ExecutionFlow.Push("L1473")
        ReturnValue1: bool = EqualEqual_ClassClass(Recipe, Recipe_TradingPost)
        if not ReturnValue1:
            goto('L110')
        
        IsBuilt = None
        self.IsTradingPostBuilt(Ref[IsBuilt])
        if not IsBuilt:
            goto('L110')
        CanAfford = False
        # End
        # Label 110
        ReturnValue: bool = EqualEqual_ClassClass(Recipe, Recipe_SpaceElevator)
        if not ReturnValue:
            goto('L215')
        
        IsBuilt = None
        self.IsSpaceElevatorBuilt(Ref[IsBuilt])
        if not IsBuilt:
            goto('L215')
        CanAfford = False
        # End
        # Label 215
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 261
        ReturnValue_0: List[ItemAmount] = self.mOwningBuildGun.GetCostForRecipe(Recipe)
        
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
            goto('L1372')
        Variable_0 = Variable
        ExecutionFlow.Push("L1388")
        ReturnValue_3: Ptr[FGInventoryComponent] = self.mOwningBuildGun.GetInventory()
        ReturnValue_0 = self.mOwningBuildGun.GetCostForRecipe(Recipe)
        
        Item = None
        Item = ReturnValue_0[Variable_0]
        ReturnValue_4: int32 = ReturnValue_3.GetNumItems(Item.ItemClass)
        NumItems = ReturnValue_4
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_6: Ptr[FGCentralStorageSubsystem] = Default__FGCentralStorageSubsystem.Get(ReturnValue_5)
        ReturnValue_7: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_6)
        if not ReturnValue_7:
            goto('L1192')
        ReturnValue_5 = self.GetOwningPlayer()
        ReturnValue_6 = Default__FGCentralStorageSubsystem.Get(ReturnValue_5)
        ReturnValue_0 = self.mOwningBuildGun.GetCostForRecipe(Recipe)
        
        Item = None
        Item = ReturnValue_0[Variable_0]
        ReturnValue_8: int32 = ReturnValue_6.GetNumItemsFromCentralStorage(Item.ItemClass)
        ReturnValue1_0: int32 = ReturnValue_8 + NumItems
        NumItems = ReturnValue1_0
        # Label 1192
        ReturnValue_0 = self.mOwningBuildGun.GetCostForRecipe(Recipe)
        
        Item = None
        Item = ReturnValue_0[Variable_0]
        ReturnValue_9: bool = GreaterEqual_IntInt(NumItems, Item.amount)
        if not ReturnValue_9:
            goto('L1462')
        goto(ExecutionFlow.Pop())
        # Label 1372
        CanAfford = True
        # End
        # Label 1388
        ReturnValue_10: int32 = Variable + 1
        Variable = ReturnValue_10
        goto('L261')
        # Label 1462
        CanAfford = False
    

    def OnScroll(self, ScrollPos: float):
        ExecuteUbergraph_Widget_BuildMenu.K2Node_CustomEvent_ScrollPos = ScrollPos #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_BuildMenu(254)
    

    def RemoveHotbarUpdateListener(self):
        self.ExecuteUbergraph_Widget_BuildMenu(1279)
    

    def ListenForHotbarUpdate(self):
        self.ExecuteUbergraph_Widget_BuildMenu(1690)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_BuildMenu(1724)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_BuildMenu(1875)
    

    def OnEscapePressed(self):
        self.ExecuteUbergraph_Widget_BuildMenu(1880)
    

    def BndEvt__mSearchBar_K2Node_ComponentBoundEvent_1_OnTextChanged__DelegateSignature(self, text: FText):
        ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_Text1 = text #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_BuildMenu(1885)
    

    def BndEvt__mSearchBar_K2Node_ComponentBoundEvent_2_OnTextComitted__DelegateSignature(self, text: FText, CommitMethod: uint8):
        ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_BuildMenu(2062)
    

    def CheckSearchResultHover(self):
        self.ExecuteUbergraph_Widget_BuildMenu(2476)
    

    def UnBlockMouse(self):
        self.ExecuteUbergraph_Widget_BuildMenu(3020)
    

    def BndEvt__Widget_MouseMoveChecker_K2Node_ComponentBoundEvent_0_OnMouseMoved__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_BuildMenu(3100)
    

    def BlockMouse(self):
        self.ExecuteUbergraph_Widget_BuildMenu(3115)
    

    def BndEvt__mSearchBar_K2Node_ComponentBoundEvent_6_OnInputBoxFocusReceived__DelegateSignature(self, FocusEvent: FocusEvent):
        ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_FocusEvent = FocusEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_BuildMenu(3120)
    

    def BndEvt__Widget_Window_DarkMode_K2Node_ComponentBoundEvent_3_OnTabButtonClicked__DelegateSignature(self, ButtonIndex: int32):
        ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_ButtonIndex = ButtonIndex #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_BuildMenu(3132)
    

    def BndEvt__mHotbarPresetEditor_K2Node_ComponentBoundEvent_4_OnPresetUpdated__DelegateSignature(self, Name: FText, IconIndex: int32, PresetIndex: int32, ShouldOverwrite: bool):
        ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_Name = Name #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_IconIndex = IconIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_PresetIndex = PresetIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_BuildMenu.K2Node_ComponentBoundEvent_ShouldOverwrite = ShouldOverwrite #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_BuildMenu(15)
    

    def ExecuteUbergraph_Widget_BuildMenu(self):
        goto(ComputedJump("EntryPoint"))
        self.OnHotbarPresetUpdated(Name, IconIndex, PresetIndex, ShouldOverwrite)
        goto(ExecutionFlow.Pop())
        # Label 66
        ReturnValue4: Ptr[PlayerController] = self.GetOwningPlayer()
        self.SetUserFocus(ReturnValue4)
        ReturnValue5: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue: bool = self.HasUserFocus(ReturnValue5)
        if not ReturnValue:
            goto('L177')
        goto(ExecutionFlow.Pop())
        # Label 177
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 66, UUID = -264114744, ExecutionFunction = "ExecuteUbergraph_Widget_BuildMenu", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        # Label 255
        self.mShoppingList.isShoppingListInteractive = False
        goto(ExecutionFlow.Pop())
        # Label 289
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Vector2D = Default__WidgetLayoutLibrary.GetViewportSize(self)
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_1, Ref[X], Ref[Y])
        ReturnValue_2: float = Y / 2
        ReturnValue1: float = X / 2
        ReturnValue_3: int32 = FTrunc(ReturnValue_2)
        ReturnValue1_0: int32 = FTrunc(ReturnValue1)
        ReturnValue_0.SetMouseLocation(ReturnValue1_0, ReturnValue_3)
        self.BlockMouse()
        goto('L66')
        # Label 628
        OutputDelegate.BindUFunction(self, OnScroll)
        self.Widget_Scrollbox.mScrollBox.OnUserScrolled.AddUnique(OutputDelegate)
        ReturnValue1_1: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1_1)
        bSuccess: bool = Controller
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(Controller, self, Ref[gameUI])
        UI: TScriptInterface[BPI_GameUI] = QueryInterface[BPI_GameUI](gameUI)
        bSuccess2: bool = UI
        if not bSuccess2:
            goto('L1040')
        
        shoppingList = None
        GetInterfaceUObject(UI).GetShoppingList(Ref[shoppingList])
        # Label 983
        self.mShoppingList = shoppingList
        self.mShoppingList.isShoppingListInteractive = True
        goto('L289')
        # Label 1040
        shoppingList: Ptr[Widget_ShoppingList] = None
        goto('L983')
        # Label 1056
        ReturnValue_4: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_4)
        bSuccess1: bool = Player
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Player.ToggleBuildGun()
        goto(ExecutionFlow.Pop())
        # Label 1184
        self.RemoveHotbarUpdateListener()
        goto('L255')
        # Label 1203
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__BPHUDHelpers.PopStackWidget(ReturnValue2, self, self)
        goto('L1056')
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue3)
        bSuccess3: bool = Controller1
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        OutputDelegate1.BindUFunction(self, UpdateShortcuts)
        Controller1.OnShortcutChanged.Remove(OutputDelegate1)
        goto(ExecutionFlow.Pop())
        # Label 1443
        self.ListenForHotbarUpdate()
        OutputDelegate2.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate2)
        goto('L628')
        # Label 1526
        ReturnValue3 = self.GetOwningPlayer()
        Controller2: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue3)
        bSuccess4: bool = Controller2
        if not bSuccess4:
           goto(ExecutionFlow.Pop())
        OutputDelegate1.BindUFunction(self, UpdateShortcuts)
        Controller2.OnShortcutChanged.AddUnique(OutputDelegate1)
        goto(ExecutionFlow.Pop())
        goto('L1526')
        # Label 1695
        self.Destruct()
        self.SaveCategories()
        goto('L1184')
        goto('L1695')
        # Label 1729
        Menu: Ptr[BP_BuildGunStateMenu] = Cast[BP_BuildGunStateMenu](self.mInteractObject)
        bSuccess5: bool = Menu
        self.mOwningState = Menu
        self.InitBuildMenu()
        self.CreateCategoryButtons()
        self.PopulateBuildings()
        goto('L1443')
        # Label 1860
        self.Construct()
        goto('L1729')
        goto('L1860')
        goto('L1203')
        ReturnValue_5: FText = Default__KismetTextLibrary.Conv_StringToText(" ")
        
        Text1 = None
        ReturnValue_6: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[Text1], Ref[ReturnValue_5])
        if not ReturnValue_6:
            goto('L2038')
        self.SetSearchbarUnfocused()
        self.mSearchWaitForKeyUp = True
        goto(ExecutionFlow.Pop())
        # Label 2038
        self.OnSearchCreateResults(Text1)
        goto(ExecutionFlow.Pop())
        CmpSuccess: bool = NotEqual_ByteByte(CommitMethod, 1)
        if not CmpSuccess:
            goto('L2108')
        goto(ExecutionFlow.Pop())
        # Label 2108
        ReturnValue3_0: Ptr[Widget] = self.mSearchResultsContainer.GetChildAt(0)
        ReturnValue_7: bool = Default__KismetSystemLibrary.IsValid(ReturnValue3_0)
        if not ReturnValue_7:
            goto('L2388')
        ReturnValue_8: Ptr[Widget] = self.mSearchResultsContainer.GetChildAt(0)
        Button: Ptr[Widget_BuildMenuRecipeButton] = Cast[Widget_BuildMenuRecipeButton](ReturnValue_8)
        bSuccess6: bool = Button
        if not bSuccess6:
           goto(ExecutionFlow.Pop())
        self.OnRecipeClicked(Button.mRecipe)
        goto(ExecutionFlow.Pop())
        # Label 2388
        ReturnValue6: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mSearchbar.mInputBox.SetUserFocus(ReturnValue6)
        goto(ExecutionFlow.Pop())
        ReturnValue_9: bool = self.mSearchResultsContainer.HasAnyChildren()
        if not ReturnValue_9:
           goto(ExecutionFlow.Pop())
        ReturnValue1_2: Ptr[Widget] = self.mSearchResultsContainer.GetChildAt(0)
        ReturnValue_10: bool = self.mSearchResultsContainer.IsHovered()
        ReturnValue1_3: bool = ReturnValue1_2.IsHovered()
        ReturnValue_11: bool = Not_PreBool(ReturnValue1_3)
        ReturnValue_12: bool = ReturnValue_10 and ReturnValue_11
        if not ReturnValue_12:
           goto(ExecutionFlow.Pop())
        ReturnValue2_0: Ptr[Widget] = self.mSearchResultsContainer.GetChildAt(0)
        Button1: Ptr[Widget_BuildMenuRecipeButton] = Cast[Widget_BuildMenuRecipeButton](ReturnValue2_0)
        bSuccess7: bool = Button1
        if not bSuccess7:
           goto(ExecutionFlow.Pop())
        Button1.SimulateOnUnhovered()
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.SearchResultHoveredTimerHandle])
        goto(ExecutionFlow.Pop())
        # Label 2945
        self.mMouseHoverBlocker.SetVisibility(1)
        self.Widget_MouseMoveChecker.StopCheckMouse()
        goto(ExecutionFlow.Pop())
        goto('L2945')
        # Label 3025
        self.Widget_MouseMoveChecker.StartCheckMouse()
        self.mMouseHoverBlocker.SetVisibility(0)
        goto(ExecutionFlow.Pop())
        self.UnBlockMouse()
        goto(ExecutionFlow.Pop())
        goto('L3025')
        self.mMouseMoved = False
        goto(ExecutionFlow.Pop())
        self.InitPresetHotbars()
        goto(ExecutionFlow.Pop())
    

    def OnClicked__DelegateSignature(self):
        pass
    
