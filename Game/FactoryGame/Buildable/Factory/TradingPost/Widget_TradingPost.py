
from codegen.ue4_stub import *

from Script.Engine import Texture2D
from Script.FactoryGame import GetCost
from Script.SlateCore import Margin
from Script.UMG import AddChild
from Script.FactoryGame import Default__FGGamePhaseManager
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.UMG import StopAnimation
from Script.Engine import IsValid
from Script.UMG import SetColorAndOpacity
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Script.Engine import Conv_StringToText
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_ImageTabButton import Widget_ImageTabButton
from Script.FactoryGame import Init
from Script.FactoryGame import FGBuildableTradingPost
from Script.FactoryGame import GetGamePhaseForTechTier
from Script.FactoryGame import IsShipAtTradingPost
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Destruct
from Script.UMG import Create
from Script.Engine import GetGameState
from Script.SlateCore import SlateBrush
from Script.SlateCore import SlateColor
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Script.Engine import Clamp
from Script.Engine import Array_Clear
from Script.FactoryGame import GetSchematicDisplayName
from Script.CoreUObject import LinearColor
from Script.FactoryGame import EGamePhase
from Script.UMG import GetChildrenCount
from Script.FactoryGame import GetTradingPost
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost import ExecuteUbergraph_Widget_TradingPost.K2Node_Event_InDeltaTime
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost import ExecuteUbergraph_Widget_TradingPost
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Script.FactoryGame import GetTechTier
from Script.FactoryGame import SetActiveSchematic
from Script.FactoryGame import FGGameState
from Script.Engine import NotEqual_ByteByte
from Script.Engine import GreaterEqual_ByteByte
from Script.FactoryGame import ESchematicType
from Script.UMG import AddChildToHorizontalBox
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import IsSchematicPaidOff
from Script.FactoryGame import ItemAmount
from Script.Engine import PrintString
from Script.FactoryGame import FGGamePhaseManager
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_TierButton import Widget_TradingPost_TierButton
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_RewardProduct import Widget_RewardProduct
from Script.FactoryGame import GetAvailableSchematics
from Script.UMG import PanelSlot
from Script.FactoryGame import GetPurchasedSchematicsOfTypes
from Script.FactoryGame import GetHighestAvailableTechTier
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.UMG import PlayAnimation
from Script.FactoryGame import FGBuildableHubTerminal
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import ClassIsChildOf
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Smoke import Widget_Smoke
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.FactoryGame import IsSchematicPurchased
from Script.FactoryGame import FGSchematicManager
from Script.FactoryGame import FGItemDescriptor
from Script.CoreUObject import Vector2D
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost import ExecuteUbergraph_Widget_TradingPost.K2Node_Event_MyGeometry
from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.Engine import Conv_TextToString
from Script.FactoryGame import GetActiveSchematic
from Script.UMG import HorizontalBoxSlot
from Script.FactoryGame import GetItemIcon
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost import ExecuteUbergraph_Widget_TradingPost.K2Node_ComponentBoundEvent_ButtonIndex
from Script.Engine import Not_PreBool
from Script.FactoryGame import GetItemName
from Script.FactoryGame import GetBigIcon
from Script.Engine import NotEqual_TextText
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost import ExecuteUbergraph_Widget_TradingPost.K2Node_CustomEvent_purchasedSchematic
from Script.Engine import BooleanOR
from Script.UMG import Tick
from Script.UMG import Widget
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost import ExecuteUbergraph_Widget_TradingPost.K2Node_CustomEvent_Schematic
from Script.FactoryGame import GetGamePhase
from Script.FactoryGame import FGSchematic
from Script.UMG import WidgetAnimation
from Script.FactoryGame import GetMaxAllowedTechTier
from Script.FactoryGame import GetItemDescription
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import Default__FGSchematic
from Script.UMG import SetRenderOpacity
from Script.Engine import IsValidClass
from Script.FactoryGame import Default__FGSchematicManager

class Widget_TradingPost(Widget_UseableBase):
    GlowInputAnim: Ptr[WidgetAnimation]
    ShakeAnim: Ptr[WidgetAnimation]
    mTradingPost: Ptr[FGBuildableTradingPost]
    mSelectedSchematic: TSubclassOf[FGSchematic]
    mCachedSchematicManager: Ptr[FGSchematicManager]
    mActiveTabButton: Ptr[Widget_ImageTabButton]
    mActiveTier: int32 = 99999
    mRelevantItems: List[TSubclassOf[FGItemDescriptor]]
    mShouldOpenInventory = True
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mUseGamepadCursor = True
    mCallCustomTickOnConstruct = True
    bHasScriptImplementedTick = True
    
    def SetSelectedSchematic(self, mSelectedSchematic: TSubclassOf[FGSchematic]):
        self.mSelectedSchematic = mSelectedSchematic
        self.Widget_TradingPost_ActivateSchematicButton.SetSelectedSchematic(self.mSelectedSchematic)
    

    def DropInventorySlotStack(self):
        
        Result = None
        self.mPayOffGrid.DropInventorySlotStack(InventorySlot, Ref[Result])
        WasStackMoved = Result
    

    def GetLowestNonFullyResearchedTier(self):
        ExecutionFlow.Push("L1068")
        ReturnValue2: int32 = self.mCachedSchematicManager.GetMaxAllowedTechTier()
        ReturnValue: bool = ReturnValue2 <= 1000
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        Variable: bool = False
        # Label 110
        Variable_0: int32 = 0
        # Label 133
        ReturnValue_0: bool = Not_PreBool(Variable)
        ReturnValue2 = self.mCachedSchematicManager.GetMaxAllowedTechTier()
        ReturnValue_1: bool = Variable_0 <= ReturnValue2
        # Label 250
        ReturnValue_2: bool = ReturnValue_0 and ReturnValue_1
        if not ReturnValue_2:
            goto('L490')
        ExecutionFlow.Push("L634")
        
        IsResearched = None
        self.CheckIfTierIsFullyResearched(Variable_0, Ref[IsResearched])
        if not IsResearched:
            goto('L751')
        ReturnValue1: int32 = self.mCachedSchematicManager.GetMaxAllowedTechTier()
        ReturnValue_3: bool = EqualEqual_IntInt(ReturnValue1, Variable_0)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        tier = 0
        # Label 474
        FoundTier = False
        # End
        # Label 490
        ReturnValue_4: int32 = self.mCachedSchematicManager.GetMaxAllowedTechTier()
        ReturnValue_5: int32 = Clamp(LocalTier, 0, ReturnValue_4)
        tier = ReturnValue_5
        FoundTier = True
        # End
        # Label 634
        ReturnValue_0 = Not_PreBool(Variable)
        if not ReturnValue_0:
            goto('L490')
        ReturnValue_6: int32 = Variable_0 + 1
        # Label 719
        Variable_0 = ReturnValue_6
        goto('L133')
        # Label 751
        ReturnValue_7: Ptr[FGGamePhaseManager] = Default__FGGamePhaseManager.Get(self)
        ReturnValue_8: uint8 = ReturnValue_7.GetGamePhase()
        ReturnValue_9: uint8 = ReturnValue_7.GetGamePhaseForTechTier(Variable_0)
        ReturnValue_10: bool = GreaterEqual_ByteByte(ReturnValue_8, ReturnValue_9)
        if not ReturnValue_10:
            goto('L994')
        LocalTier = Variable_0
        # Label 982
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 994
        ReturnValue_11: int32 = Variable_0 - 1
        LocalTier = ReturnValue_11
        goto('L982')
    

    def CheckIfTierIsFullyResearched(self, tier: int32):
        ExecutionFlow.Push("L719")
        IsReasearched = True
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mCachedSchematicManager)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        schematics: List[TSubclassOf[FGSchematic]] = []
        
        self.mCachedSchematicManager.GetAvailableSchematics(Ref[schematics])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 175
        ReturnValue_0: int32 = len(schematics)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L609')
        Variable_0 = Variable
        # Label 313
        ExecutionFlow.Push("L633")
        
        Item = None
        # Label 318
        Item = schematics[Variable_0]
        ReturnValue_2: int32 = Default__FGSchematic.GetTechTier(Item)
        ReturnValue_3: bool = EqualEqual_IntInt(tier, ReturnValue_2)
        # Label 474
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = schematics[Variable_0]
        ReturnValue_4: bool = self.mCachedSchematicManager.IsSchematicPurchased(Item)
        if not ReturnValue_4:
            goto('L707')
        goto(ExecutionFlow.Pop())
        # Label 609
        IsResearched = IsReasearched
        # End
        # Label 633
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L175')
        # Label 707
        IsReasearched = False
        goto(ExecutionFlow.Pop())
    

    def SetTierAndDeafultSchematic(self, tier: int32):
        self.mActiveTier = tier
        self.mSchematicList.mCurrentDisplayedTier = self.mActiveTier
        self.mSchematicList.CreateSchematicButtons()
    

    def GetSchematicHintTextVisibility(self):
        ReturnValue: uint8 = self.GetTierHintVisibility()
        ReturnValue_0: bool = NotEqual_ByteByte(ReturnValue, 0)
        if not ReturnValue_0:
            goto('L138')
        self.PuslingSchematic.mPlayPulseAnim()
        ReturnValue_1: uint8 = 0
        # Label 133
        goto('L194')
        # Label 138
        self.PuslingSchematic.mStopPulseAnim()
        ReturnValue_1 = 2
    

    def GetSchematicHintVisibility(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mSelectedSchematic)
        if not ReturnValue:
            goto('L90')
        ReturnValue_0: uint8 = 1
        goto('L110')
        # Label 90
        ReturnValue_0 = 0
    

    def GetTierHintVisibility(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mCachedSchematicManager)
        if not ReturnValue:
            goto('L284')
        ReturnValue_0: int32 = self.mCachedSchematicManager.GetHighestAvailableTechTier()
        ReturnValue_1: bool = self.mActiveTier <= ReturnValue_0
        if not ReturnValue_1:
            goto('L228')
        self.PuslingTier.mStopPulseAnim()
        ReturnValue_2: uint8 = 2
        goto('L284')
        # Label 228
        self.PuslingTier.mPlayPulseAnim()
        ReturnValue_2 = 0
    

    def GenerateTierList(self):
        ExecutionFlow.Push("L397")
        ReturnValue: int32 = self.mCachedSchematicManager.GetHighestAvailableTechTier()
        Variable: int32 = 0
        # Label 78
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L318')
        ExecutionFlow.Push("L323")
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Widget_TradingPost_TierButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_TradingPost_TierButton, ReturnValue_1)
        ReturnValue_2.SetTierNumber(Variable, self)
        ReturnValue_3: Ptr[HorizontalBoxSlot] = self.TierList.AddChildToHorizontalBox(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 318
        # End
        # Label 323
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L78')
    

    def UpdateInventoryVisibility(self):
        pass
    

    def GetRewardVisibility(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mCachedSchematicManager)
        if not ReturnValue:
            goto('L205')
        ReturnValue_0: bool = self.mCachedSchematicManager.IsShipAtTradingPost()
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        ReturnValue_2: bool = ReturnValue_1 and False
        # Label 166
        if not ReturnValue_2:
            goto('L230')
        ReturnValue_3: uint8 = 2
        goto('L250')
        # Label 205
        ReturnValue_3 = 2
        goto('L250')
        # Label 230
        ReturnValue_3 = 0
    

    def GetShipAwayFeedback(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mCachedSchematicManager)
        if not ReturnValue:
            goto('L301')
        ReturnValue_0: bool = self.mCachedSchematicManager.IsShipAtTradingPost()
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        ReturnValue_2: bool = ReturnValue_1 and True
        # Label 166
        Variable: uint8 = 3
        Variable_0: bool = ReturnValue_2
        # Label 205
        Variable1: uint8 = 1
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_3: uint8 = switch.get(Variable_0, None)
        goto('L321')
        # Label 301
        ReturnValue_3 = 1
    

    def SetRewardInformation(self, inTitle: FText, inDesc: FText, inIcon: SlateBrush):
        self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.SetItemDescriptionText(inDesc)
        self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.SetItemTitle(inTitle)
        SlateBrush.ImageSize = self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mIcon.Brush.ImageSize
        SlateBrush.Margin = self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mIcon.Brush.Margin
        SlateBrush.TintColor = self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mIcon.Brush.TintColor
        SlateBrush.ResourceObject = inIcon.ResourceObject
        SlateBrush.DrawAs = self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mIcon.Brush.DrawAs
        SlateBrush.Tiling = self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mIcon.Brush.Tiling
        SlateBrush.Mirroring = self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mIcon.Brush.Mirroring
        
        SlateBrush = None
        self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mIcon.SetBrush(Ref[SlateBrush])
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.IconFade, 0, 1, 0, 1)
    

    def GetActiveSchematicTabEnabled(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mCachedSchematicManager)
        if not ReturnValue:
            goto('L376')
        ReturnValue_0: bool = self.mCachedSchematicManager.IsShipAtTradingPost()
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        ReturnValue_2: TSubclassOf[FGSchematic] = self.mCachedSchematicManager.GetActiveSchematic()
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_2)
        Variable1: bool = True
        ReturnValue_4: bool = BooleanOR(ReturnValue_3, ReturnValue_1)
        Variable: bool = ReturnValue_4
        Variable2: bool = False
        
        switch = {
            False: Variable2,
            True: Variable1
        }
        ReturnValue_5: bool = switch.get(Variable, None)
        goto('L387')
        # Label 376
        ReturnValue_5 = False
    

    def SetActiveTab(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mCachedSchematicManager)
        if not ReturnValue:
            goto('L416')
        ReturnValue_0: bool = self.mCachedSchematicManager.IsShipAtTradingPost()
        if not ReturnValue_0:
            goto('L374')
        ReturnValue_1: TSubclassOf[FGSchematic] = self.mCachedSchematicManager.GetActiveSchematic()
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_1)
        Variable: int32 = 1
        Variable_0: bool = ReturnValue_2
        Variable1: int32 = 0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.Widget_SlidingTabs.SetActiveIndex(switch.get(Variable_0, None), False)
        # End
        # Label 374
        self.Widget_SlidingTabs.SetActiveIndex(1, False)
    

    def GetShipInventoryVisibility(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mCachedSchematicManager)
        if not ReturnValue:
            goto('L166')
        ReturnValue_0: bool = self.mCachedSchematicManager.IsShipAtTradingPost()
        if not ReturnValue_0:
            goto('L146')
        ReturnValue_1: uint8 = 0
        goto('L166')
        # Label 146
        ReturnValue_1 = 2
    

    def ActivateSelectedSchematic(self):
        ReturnValue: bool = self.mCachedSchematicManager.SetActiveSchematic(self.mSelectedSchematic)
        if not ReturnValue:
            goto('L394')
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_0)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L474')
        ReturnValue_1: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_1.ServerSetActiveSchematic(self.mSelectedSchematic)
        self.mPayOffGrid.SetUpPayOffSlots(self.mSelectedSchematic)
        self.Widget_SlidingTabs.SetActiveIndex(1, True)
        self.mWindow.SetInventoryVisibility(True, True)
        # End
        # Label 394
        self.Widget_SlidingTabs.SetActiveIndex(1, True)
        self.mWindow.SetInventoryVisibility(True, True)
    

    def GetSelectedRecipeBoxVisibility(self):
        Variable: uint8 = 0
        Variable1: uint8 = 2
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mSelectedSchematic)
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        # Label 110
        ReturnValue_0: uint8 = switch.get(Variable_0, None)
    

    def SetDefaultDescriptionText(self, mSchematicClass: TSubclassOf[FGSchematic]):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(mSchematicClass)
        if not ReturnValue:
            goto('L1283')
        ReturnValue_0: FText = Default__FGSchematic.GetSchematicDisplayName(mSchematicClass)
        self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mProductTitleText.SetText(ReturnValue_0)
        self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mProductDescriptionText.SetText()
        self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mCategoryIcon.SetVisibility(0)
        SlateBrush.ImageSize = self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mIcon.Brush.ImageSize
        SlateBrush.Margin = self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mIcon.Brush.Margin
        SlateBrush.TintColor = self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mIcon.Brush.TintColor
        SlateBrush.ResourceObject = None
        SlateBrush.DrawAs = self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mIcon.Brush.DrawAs
        SlateBrush.Tiling = self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mIcon.Brush.Tiling
        SlateBrush.Mirroring = self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mIcon.Brush.Mirroring
        
        SlateBrush = None
        self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mIcon.SetBrush(Ref[SlateBrush])
        ReturnValue_1: SlateBrush = Default__FGSchematic.GetItemIcon(self.mSelectedSchematic)
        self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.mCategoryIconImage = ReturnValue_1.ResourceObject
    

    def UpdateRewardInfoFromProduct(self, Reward Widget: Ptr[Widget_SchematicRewardItem]):
        ReturnValue: Ptr[UMGSequencePlayer] = self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.PlayAnimation(self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.IconFade, 0, 1, 0, 1)
        Product: Ptr[Widget_RewardProduct] = Cast[Widget_RewardProduct](Reward Widget)
        bSuccess: bool = Product
        if not bSuccess:
            goto('L361')
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_StringToText("")
        
        Reward Widget.mTitle = None
        ReturnValue_1: bool = Default__KismetTextLibrary.NotEqual_TextText(Ref[Reward Widget.mTitle], Ref[ReturnValue_0])
        if not ReturnValue_1:
            goto('L473')
        # Label 361
        self.SetRewardInformation(Reward Widget.mTitle, Reward Widget.mDescription, Reward Widget.mBigIconBrush)
        # End
        
        Product.mProducts = None
        Item = None
        # Label 473
        Item = Product.mProducts[0]
        localProduct = Item
        ReturnValue_2: bool = ClassIsChildOf(localProduct.ItemClass, FGItemDescriptor)
        if not ReturnValue_2:
            goto('L1687')
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValidClass(self.mSelectedSchematic)
        if not ReturnValue_3:
            goto('L1687')
        ReturnValue_4: Ptr[Texture2D] = Default__FGItemDescriptor.GetBigIcon(localProduct.ItemClass)
        ReturnValue_5: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_4)
        if not ReturnValue_5:
            goto('L1603')
        ReturnValue_4 = Default__FGItemDescriptor.GetBigIcon(localProduct.ItemClass)
        localIcon = ReturnValue_4
        # Label 907
        SlateBrush.ImageSize = Vector2D(X = 20, Y = 20)
        SlateBrush.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush.TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0)
        SlateBrush.ResourceObject = localIcon
        SlateBrush.DrawAs = 3
        SlateBrush.Tiling = 0
        SlateBrush.Mirroring = 0
        ReturnValue_6: FText = Default__FGItemDescriptor.GetItemName(localProduct.ItemClass)
        ReturnValue_7: FText = Default__FGItemDescriptor.GetItemDescription(localProduct.ItemClass)
        self.SetRewardInformation(ReturnValue_6, ReturnValue_7, SlateBrush)
        ReturnValue_6 = Default__FGItemDescriptor.GetItemName(localProduct.ItemClass)
        
        ReturnValue_8: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_6])
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_8, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        # End
        # Label 1603
        ReturnValue_9: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(localProduct.ItemClass)
        localIcon = ReturnValue_9
        goto('L907')
    

    def GetTabFeedback(self):
        ExecutionFlow.Push("L617")
        Variable: int32 = 0
        # Label 28
        ReturnValue: int32 = self.mWindow.ButtonSlot.GetChildrenCount()
        ReturnValue_0: bool = Variable <= ReturnValue
        # Label 138
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L446")
        ReturnValue_1: Ptr[Widget] = self.mWindow.ButtonSlot.GetChildAt(Variable)
        Button: Ptr[Widget_ImageTabButton] = Cast[Widget_ImageTabButton](ReturnValue_1)
        bSuccess: bool = Button
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        # Label 301
        ReturnValue_2: bool = EqualEqual_IntInt(Variable, 0)
        if not ReturnValue_2:
            goto('L520')
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        Button.SetColorAndOpacity(GraphicsWhite)
        goto(ExecutionFlow.Pop())
        # Label 446
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L28')
        
        Text = None
        Graphics = None
        # Label 520
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        Button.SetColorAndOpacity(Graphics)
        goto(ExecutionFlow.Pop())
    

    def OnSchematicClicked(self, schematic: TSubclassOf[FGSchematic]):
        ExecutionFlow.Push("L940")
        self.Widget_TradingPost_RecipePreview.SetupSchematicContents(schematic)
        self.Widget_TradingPost_RecipePreview.Widget_TradingPostSchematicCostInfo.UpdateSchematicCosts(schematic)
        self.SetSelectedSchematic(schematic)
        self.SetDefaultDescriptionText(self.mSelectedSchematic)
        self.Widget_TradingPost_ActivateSchematicButton.SetVisibility(0)
        ReturnValue: Ptr[UMGSequencePlayer] = self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.PlayAnimation(self.Widget_TradingPost_RecipePreview.mRecipeInfoBox.CategoryFade, 0, 1, 0, 1)
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mRelevantItems])
        # Label 376
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 422
        ReturnValue_0: List[ItemAmount] = Default__FGSchematic.GetCost(self.mSelectedSchematic)
        
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
            goto('L820')
        Variable_0 = Variable
        ExecutionFlow.Push("L866")
        ReturnValue_0 = Default__FGSchematic.GetCost(self.mSelectedSchematic)
        
        Item = None
        Item = ReturnValue_0[Variable_0]
        
        Item.ItemClass = None
        ReturnValue_3: int32 = self.mRelevantItems.append(Item.ItemClass)
        goto(ExecutionFlow.Pop())
        
        # Label 820
        self.mWindow.SetupRelevantInventory(Ref[self.mRelevantItems])
        goto(ExecutionFlow.Pop())
        # Label 866
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L422')
    

    def GetActiveSchematicInfoVisibility(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mCachedSchematicManager)
        if not ReturnValue:
            goto('L293')
        ReturnValue_0: TSubclassOf[FGSchematic] = self.mCachedSchematicManager.GetActiveSchematic()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_0)
        Variable: bool = ReturnValue_1
        Variable_0: uint8 = 0
        Variable1: uint8 = 2
        
        switch = {
            False: Variable1,
            True: Variable_0
        }
        ReturnValue_2: uint8 = switch.get(Variable, None)
        goto('L313')
        # Label 293
        ReturnValue_2 = 2
    

    def SetActiveSchematicInfo(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mCachedSchematicManager)
        if not ReturnValue:
            goto('L305')
        ReturnValue_0: TSubclassOf[FGSchematic] = self.mCachedSchematicManager.GetActiveSchematic()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_0)
        if not ReturnValue_1:
            goto('L330')
        ReturnValue_0 = self.mCachedSchematicManager.GetActiveSchematic()
        ReturnValue_2: FText = Default__FGSchematic.GetSchematicDisplayName(ReturnValue_0)
        ReturnValue_3: FText = ReturnValue_2
        goto('L350')
        # Label 305
        ReturnValue_3 = 
        goto('L350')
        # Label 330
        ReturnValue_3 = 
    

    def Cleanup(self):
        OutputDelegate.BindUFunction(self, OnActiveSchematicChanged)
        self.mCachedSchematicManager.mOnActiveSchematicChanged.Remove(OutputDelegate)
    

    def CloseTradepost(self):
        self.ExecuteUbergraph_Widget_TradingPost(668)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_TradingPost(697)
    

    def Init(self):
        self.ExecuteUbergraph_Widget_TradingPost(722)
    

    def Tick(self):
        ExecuteUbergraph_Widget_TradingPost.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_TradingPost.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TradingPost(2585)
    

    def OnActiveSchematicChanged(self, schematic: TSubclassOf[FGSchematic]):
        ExecuteUbergraph_Widget_TradingPost.K2Node_CustomEvent_Schematic = schematic #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TradingPost(3221)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_TradingPost(3267)
    

    def purchasedSchematic(self, purchasedSchematic: TSubclassOf[FGSchematic]):
        ExecuteUbergraph_Widget_TradingPost.K2Node_CustomEvent_purchasedSchematic = purchasedSchematic #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TradingPost(3621)
    

    def mShakeWindow(self):
        self.ExecuteUbergraph_Widget_TradingPost(3683)
    

    def BndEvt__mWindow_K2Node_ComponentBoundEvent_0_OnClose__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TradingPost(3688)
    

    def CreateSmoke(self):
        self.ExecuteUbergraph_Widget_TradingPost(3693)
    

    def BndEvt__mWindow_K2Node_ComponentBoundEvent_3_OnTabButtonClicked__DelegateSignature(self, ButtonIndex: int32):
        ExecuteUbergraph_Widget_TradingPost.K2Node_ComponentBoundEvent_ButtonIndex = ButtonIndex #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TradingPost(4102)
    

    def ExecuteUbergraph_Widget_TradingPost(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L258")
        ReturnValue4: TSubclassOf[FGSchematic] = self.mCachedSchematicManager.GetActiveSchematic()
        ReturnValue: List[ItemAmount] = Default__FGSchematic.GetCost(ReturnValue4)
        
        Item = None
        Item = ReturnValue[Variable]
        
        Item.ItemClass = None
        ReturnValue_0: int32 = self.mRelevantItems.append(Item.ItemClass)
        goto(ExecutionFlow.Pop())
        # Label 258
        ReturnValue_1: int32 = Variable + 1
        Variable: int32 = ReturnValue_1
        # Label 327
        ReturnValue4 = self.mCachedSchematicManager.GetActiveSchematic()
        ReturnValue = Default__FGSchematic.GetCost(ReturnValue4)
        
        ReturnValue1: int32 = len(ReturnValue)
        ReturnValue_2: bool = Variable <= ReturnValue1
        if not ReturnValue_2:
            goto('L571')
        Variable = Variable
        goto('L15')
        
        # Label 571
        self.mWindow.SetupRelevantInventory(Ref[self.mRelevantItems])
        goto(ExecutionFlow.Pop())
        # Label 617
        Variable = 0
        Variable = 0
        goto('L327')
        # Label 668
        self.OnEscapePressed()
        goto(ExecutionFlow.Pop())
        self.Destruct()
        # Label 707
        self.Cleanup()
        goto(ExecutionFlow.Pop())
        self.Init()
        ReturnValue_3: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue_3)
        bSuccess: bool = State
        ReturnValue_4: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(State)
        self.mCachedSchematicManager = ReturnValue_4
        Terminal: Ptr[FGBuildableHubTerminal] = Cast[FGBuildableHubTerminal](self.mInteractObject)
        bSuccess1: bool = Terminal
        if not bSuccess1:
            goto('L2180')
        ReturnValue_5: Ptr[FGBuildableTradingPost] = Terminal.GetTradingPost()
        self.mTradingPost = ReturnValue_5
        self.mSchematicList.mTradingPost = self.mTradingPost
        self.mPayOffGrid.mTradingPostWidget = self
        self.mLaunchShipButton.mTradingPost = self.mTradingPost
        self.mLaunchShipButton.mTradingPostWidget = self
        self.mShipAwayFeedback.mTradingPost = self.mTradingPost
        self.mShipAwayFeedback.mTradingPostWidget = self
        ReturnValue_6: TSubclassOf[FGSchematic] = self.mCachedSchematicManager.GetActiveSchematic()
        ReturnValue_7: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_6)
        if not ReturnValue_7:
            goto('L1489')
        ReturnValue_6 = self.mCachedSchematicManager.GetActiveSchematic()
        self.SetSelectedSchematic(ReturnValue_6)
        self.Widget_TradingPost_RecipePreview.SetupSchematicContents(self.mSelectedSchematic)
        # Label 1489
        self.Widget_TradingPost_RecipePreview.Widget_TradingPostSchematicCostInfo.UpdateSchematicCosts(self.mSelectedSchematic)
        self.SetDefaultDescriptionText(self.mSelectedSchematic)
        ReturnValue3: TSubclassOf[FGSchematic] = self.mCachedSchematicManager.GetActiveSchematic()
        self.mPayOffGrid.SetUpPayOffSlots(ReturnValue3)
        self.Widget_TradingPost_RecipePreview.mTradingPostWidget = self
        self.mSchematicList.mTradingPostWidget = self
        self.SetActiveTab()
        self.mSchematicList.CreateSchematicButtons()
        OutputDelegate.BindUFunction(self, OnActiveSchematicChanged)
        self.mCachedSchematicManager.mOnActiveSchematicChanged.AddUnique(OutputDelegate)
        ReturnValue_8: bool = EqualEqual_IntInt(self.Widget_SlidingTabs.mActiveIndex, 1)
        self.mWindow.SetInventoryVisibility(ReturnValue_8, False)
        ReturnValue1_0: TSubclassOf[FGSchematic] = self.mCachedSchematicManager.GetActiveSchematic()
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue1_0)
        if not ReturnValue1_1:
            goto('L2284')
        ReturnValue1_0 = self.mCachedSchematicManager.GetActiveSchematic()
        ReturnValue_9: int32 = Default__FGSchematic.GetTechTier(ReturnValue1_0)
        self.SetTierAndDeafultSchematic(ReturnValue_9)
        goto(ExecutionFlow.Pop())
        # Label 2180
        Default__KismetSystemLibrary.PrintString(self, "did not cast to tradingpost", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
        # Label 2284
        Array: List[uint8] = [2, 3]
        schematics: List[TSubclassOf[FGSchematic]] = []
        
        self.mCachedSchematicManager.GetPurchasedSchematicsOfTypes(Array, Ref[schematics])
        
        ReturnValue_10: int32 = len(schematics)
        ReturnValue_11: bool = ReturnValue_10 > 1
        if not ReturnValue_11:
           goto(ExecutionFlow.Pop())
        
        Tier = None
        FoundTier = None
        self.GetLowestNonFullyResearchedTier(Ref[Tier], Ref[FoundTier])
        if not FoundTier:
            goto('L2565')
        
        Tier = None
        FoundTier = None
        self.GetLowestNonFullyResearchedTier(Ref[Tier], Ref[FoundTier])
        self.SetTierAndDeafultSchematic(Tier)
        goto(ExecutionFlow.Pop())
        # Label 2565
        self.SetTierAndDeafultSchematic(0)
        goto(ExecutionFlow.Pop())
        self.Tick(MyGeometry, InDeltaTime)
        ReturnValue1_2: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State1: Ptr[FGGameState] = Cast[FGGameState](ReturnValue1_2)
        bSuccess2: bool = State1
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        ReturnValue1_3: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(State1)
        ReturnValue2: TSubclassOf[FGSchematic] = ReturnValue1_3.GetActiveSchematic()
        ReturnValue2_0: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue2)
        if not ReturnValue2_0:
           goto(ExecutionFlow.Pop())
        ReturnValue1_3 = Default__FGSchematicManager.Get(State1)
        ReturnValue2 = ReturnValue1_3.GetActiveSchematic()
        ReturnValue_12: bool = ReturnValue1_3.IsSchematicPaidOff(ReturnValue2)
        if not ReturnValue_12:
            goto('L3137')
        if not Variable3:
            goto('L3058')
        goto(ExecutionFlow.Pop())
        # Label 3058
        Variable3: bool = True
        Variable2: bool = False
        self.StopAnimation(self.GlowInputAnim)
        self.GlowInput.SetRenderOpacity(0)
        goto(ExecutionFlow.Pop())
        # Label 3137
        Variable3 = False
        if not Variable2:
            goto('L3163')
        goto(ExecutionFlow.Pop())
        # Label 3163
        Variable2 = True
        ReturnValue1_4: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.GlowInputAnim, 0, 0, 0, 1)
        goto(ExecutionFlow.Pop())
        self.mPayOffGrid.SetUpPayOffSlots(Schematic)
        goto(ExecutionFlow.Pop())
        self.Construct()
        ReturnValue2_1: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue2_2: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue2_1)
        self.mCachedSchematicManager = ReturnValue2_2
        self.Widget_InventorySlot_DropArea.mHudPayOffGrid = self.mPayOffGrid
        OutputDelegate1.BindUFunction(self, purchasedSchematic)
        self.mCachedSchematicManager.PurchasedSchematicDelegate.AddUnique(OutputDelegate1)
        self.GenerateTierList()
        self.Widget_TradingPost_ActivateSchematicButton.mTradingPost = self
        self.Widget_TradingPost_LanuchButtonPlatform.mTradingPost = self
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mRelevantItems])
        goto('L617')
        self.CloseTradepost()
        goto(ExecutionFlow.Pop())
        # Label 3636
        ReturnValue_13: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ShakeAnim, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        goto('L3636')
        goto('L668')
        ReturnValue_14: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_15: Ptr[Widget_Smoke] = Default__WidgetBlueprintLibrary.Create(self, Widget_Smoke, ReturnValue_14)
        ReturnValue_16: Ptr[PanelSlot] = self.mSmokeContainer_BottomRight.AddChild(ReturnValue_15)
        ReturnValue1_5: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_6: Ptr[Widget_Smoke] = Default__WidgetBlueprintLibrary.Create(self, Widget_Smoke, ReturnValue1_5)
        ReturnValue1_7: Ptr[PanelSlot] = self.mSmokeContainer_BottomLeft.AddChild(ReturnValue1_6)
        ReturnValue2_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue2_4: Ptr[Widget_Smoke] = Default__WidgetBlueprintLibrary.Create(self, Widget_Smoke, ReturnValue2_3)
        ReturnValue2_5: Ptr[PanelSlot] = self.mSmokeContainer_TopCenter.AddChild(ReturnValue2_4)
        goto(ExecutionFlow.Pop())
        Variable_0: bool = True
        Variable1: bool = False
        Variable_1: int32 = ButtonIndex
        
        switch = {
            0: Variable1,
            1: Variable_0
        }
        self.mWindow.SetInventoryVisibility(switch.get(Variable_1, None), True)
        goto(ExecutionFlow.Pop())
    
