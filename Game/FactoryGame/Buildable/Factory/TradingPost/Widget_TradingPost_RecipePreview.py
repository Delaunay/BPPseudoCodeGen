
from codegen.ue4_stub import *

from Script.UMG import AddChildToUniformGrid
from Script.Engine import Delay
from Script.UMG import GetChildrenCount
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Unlocks.BPI_UnlockableInterface import BPI_UnlockableInterface
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import SetColumn
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.UMG import GetChildAt
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicRewardItem import Widget_SchematicRewardItem
from Script.Engine import GameStateBase
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Script.FactoryGame import FGUnlock
from Script.Engine import Array_Append
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import Widget_CostSlotWrapper
from Script.Engine import IsValid
from Script.FactoryGame import GetUnlocks
from Script.UMG import UniformGridSlot
from Script.Engine import Divide_IntInt
from Script.UMG import SetRow
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGGameState
from Script.UMG import Widget
from Script.Engine import Percent_IntInt
from Script.UMG import UserWidget
from Script.FactoryGame import IsShipAtTradingPost
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import FGSchematicManager
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_RecipePreview import ExecuteUbergraph_Widget_TradingPost_RecipePreview
from Script.Engine import GetGameState
from Script.FactoryGame import Default__FGSchematic
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost import Widget_TradingPost
from Script.Engine import Array_Clear
from Script.FactoryGame import Default__FGSchematicManager
from Script.Engine import IsValidClass

class Widget_TradingPost_RecipePreview(UserWidget):
    mTradingPostWidget: Ptr[Widget_TradingPost]
    mAllRewardItems: List[Ptr[UserWidget]]
    Visibility = ESlateVisibility::HitTestInvisible
    
    def GetLightGrayColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Graphics
    

    def GetLightGrayText(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Text
    

    def GetCostVisibility(self):
        ReturnValue: int32 = self.Widget_TradingPostSchematicCostInfo.mCostGrid.GetChildrenCount()
        ReturnValue_0: bool = ReturnValue > 0
        if not ReturnValue_0:
            goto('L145')
        ReturnValue_1: uint8 = 0
        goto('L165')
        # Label 145
        ReturnValue_1 = 1
    

    def GetRewardsVisibility(self):
        ReturnValue: int32 = self.mRecipesGrid.GetChildrenCount()
        ReturnValue_0: bool = ReturnValue > 0
        if not ReturnValue_0:
            goto('L123')
        ReturnValue_1: uint8 = 0
        goto('L143')
        # Label 123
        ReturnValue_1 = 1
    

    def ClearSchematicContents(self):
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mAllRewardItems])
        self.mRecipesGrid.ClearChildren()
        self.mRecipeInfoBox.SetItemTitle()
        self.mRecipeInfoBox.SetItemDescriptionText()
        SlateBrush.ImageSize = self.mRecipeInfoBox.mIcon.Brush.ImageSize
        SlateBrush.Margin = self.mRecipeInfoBox.mIcon.Brush.Margin
        SlateBrush.TintColor = self.mRecipeInfoBox.mIcon.Brush.TintColor
        SlateBrush.ResourceObject = None
        SlateBrush.DrawAs = self.mRecipeInfoBox.mIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mRecipeInfoBox.mIcon.Brush.Tiling
        SlateBrush.Mirroring = self.mRecipeInfoBox.mIcon.Brush.Mirroring
        
        SlateBrush = None
        self.mRecipeInfoBox.mIcon.SetBrush(Ref[SlateBrush])
        self.mRecipeInfoBox.mCategoryIcon.SetVisibility(2)
        self.Widget_TradingPostSchematicCostInfo.mCostGrid.ClearChildren()
        self.mTradingPostWidget.mSchematicOverlay.SetVisibility(0)
        self.mTradingPostWidget.Widget_TradingPost_ActivateSchematicButton.SetVisibility(2)
    

    def PositionRewards(self):
        ExecutionFlow.Push("L933")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(self.mAllRewardItems)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L844')
        Variable_0 = Variable
        ExecutionFlow.Push("L859")
        
        Item = None
        Item = self.mAllRewardItems[Variable_0]
        Item: Ptr[Widget_SchematicRewardItem] = Cast[Widget_SchematicRewardItem](Item)
        bSuccess: bool = Item
        
        isValid = None
        Item.IsValidRewardItem(Ref[isValid])
        if not isValid:
           goto(ExecutionFlow.Pop())
        
        Item = self.mAllRewardItems[Variable_0]
        ReturnValue_1: Ptr[UniformGridSlot] = self.mRecipesGrid.AddChildToUniformGrid(Item)
        ReturnValue_2: int32 = Divide_IntInt(LocalIndex, 5)
        ReturnValue_1.SetRow(ReturnValue_2)
        ReturnValue_3: int32 = Percent_IntInt(LocalIndex, 5)
        ReturnValue_1.SetColumn(ReturnValue_3)
        ReturnValue2: int32 = LocalIndex + 1
        Variable1: int32 = ReturnValue2
        LocalIndex = Variable1
        if not True:
           goto(ExecutionFlow.Pop())
        ReturnValue1: int32 = localRow + 1
        Variable_1: int32 = ReturnValue1
        localRow = Variable_1
        goto(ExecutionFlow.Pop())
        # Label 844
        self.AnimateRewards()
        goto(ExecutionFlow.Pop())
        # Label 859
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L51')
    

    def GetActivateButtonVisibility(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L498')
        ReturnValue = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue)
        bSuccess: bool = State
        if not bSuccess:
            goto('L498')
        ReturnValue_1: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(State)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_1)
        if not ReturnValue1:
            goto('L498')
        ReturnValue_1 = Default__FGSchematicManager.Get(State)
        ReturnValue_2: bool = ReturnValue_1.IsShipAtTradingPost()
        if not ReturnValue_2:
            goto('L478')
        ReturnValue_3: uint8 = 0
        goto('L498')
        # Label 478
        ReturnValue_3 = 2
    

    def SetupSchematicContents(self, mSchematic: TSubclassOf[FGSchematic]):
        ExecutionFlow.Push("L1035")
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(mSchematic)
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue1)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        ReturnValue_2: bool = ReturnValue and ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mAllRewardItems])
        self.mRecipesGrid.ClearChildren()
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 353
        ReturnValue_3: List[Ptr[FGUnlock]] = Default__FGSchematic.GetUnlocks(mSchematic)
        
        ReturnValue_4: int32 = len(ReturnValue_3)
        ReturnValue_5: bool = Variable <= ReturnValue_4
        if not ReturnValue_5:
            goto('L900')
        Variable_0 = Variable
        ExecutionFlow.Push("L915")
        ReturnValue_3 = Default__FGSchematic.GetUnlocks(mSchematic)
        
        Item = None
        Item = ReturnValue_3[Variable_0]
        Interface: TScriptInterface[BPI_UnlockableInterface] = QueryInterface[BPI_UnlockableInterface](Item)
        bSuccess: bool = Interface
        if not bSuccess:
            goto('L989')
        ReturnValue_6: Ptr[PlayerController] = self.GetOwningPlayer()
        
        Widgets = None
        GetInterfaceUObject(Interface).GetUnlockRewardWidgets(ReturnValue_6, mSchematic, self.mTradingPostWidget, Ref[Widgets])
        
        Widgets = None
        # Label 849
        Default__KismetArrayLibrary.Array_Append(Ref[self.mAllRewardItems], Ref[Widgets])
        goto(ExecutionFlow.Pop())
        # Label 900
        self.PositionRewards()
        goto(ExecutionFlow.Pop())
        # Label 915
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L353')
        
        Widgets = None
        # Label 989
        Default__KismetArrayLibrary.Array_Clear(Ref[Widgets])
        goto('L849')
    

    def AnimateRewards(self):
        self.ExecuteUbergraph_Widget_TradingPost_RecipePreview(1033)
    

    def AnimateCostSlots(self):
        self.ExecuteUbergraph_Widget_TradingPost_RecipePreview(1066)
    

    def ExecuteUbergraph_Widget_TradingPost_RecipePreview(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.AnimateCostSlots()
        Variable: int32 = 0
        # Label 52
        ReturnValue1: int32 = self.mRecipesGrid.GetChildrenCount()
        ReturnValue1_0: bool = Variable <= ReturnValue1
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, 0.019999999552965164, LatentActionInfo(Linkage = 227, UUID = 1773550656, ExecutionFunction = "ExecuteUbergraph_Widget_TradingPost_RecipePreview", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L449")
        ReturnValue1_1: Ptr[Widget] = self.mRecipesGrid.GetChildAt(Variable)
        Item: Ptr[Widget_SchematicRewardItem] = Cast[Widget_SchematicRewardItem](ReturnValue1_1)
        bSuccess1: bool = Item
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue1_2: Ptr[UMGSequencePlayer] = Item.PlayAnimation(Item.FadeAnim, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 449
        ReturnValue: int32 = Variable + 1
        Variable = ReturnValue
        goto('L52')
        ExecutionFlow.Push("L767")
        ReturnValue_0: Ptr[Widget] = self.Widget_TradingPostSchematicCostInfo.mCostGrid.GetChildAt(Variable1)
        Wrapper: Ptr[Widget_CostSlotWrapper] = Cast[Widget_CostSlotWrapper](ReturnValue_0)
        bSuccess: bool = Wrapper
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_1: Ptr[UMGSequencePlayer] = Wrapper.PlayAnimation(Wrapper.FadeAnim, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 767
        ReturnValue1_3: int32 = Variable1 + 1
        Variable1: int32 = ReturnValue1_3
        # Label 836
        ReturnValue_2: int32 = self.Widget_TradingPostSchematicCostInfo.mCostGrid.GetChildrenCount()
        ReturnValue_3: bool = Variable1 <= ReturnValue_2
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, 0.019999999552965164, LatentActionInfo(Linkage = 523, UUID = -1050853647, ExecutionFunction = "ExecuteUbergraph_Widget_TradingPost_RecipePreview", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L15')
        # Label 1038
        Variable1 = 0
        goto('L836')
        goto('L1038')
    
