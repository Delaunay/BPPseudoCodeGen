
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Script.UMG import GetParent
from Script.Engine import Texture2D
from Script.Engine import SetClassPropertyByName
from Script.FactoryGame import GetCost
from Script.UMG import GetChildIndex
from Script.FactoryGame import GetItemIcon
from Script.UMG import GetChildrenCount
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Game.FactoryGame.Interface.UI.InGame.Widget_PopupContentImageButton import ExecuteUbergraph_Widget_PopupContentImageButton.K2Node_CustomEvent_Title
from Script.Engine import Not_PreBool
from Game.FactoryGame.Buildable.Factory.FoundryMk1.Build_FoundryMk1 import Build_FoundryMk1
from Script.FactoryGame import GetProducts
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Interface.UI.InGame.Widget_PopupContentImageButton import ExecuteUbergraph_Widget_PopupContentImageButton.K2Node_CustomEvent_ImageBrush
from Script.CoreUObject import Object
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.InGame.Widget_PopupContentImageButton import ExecuteUbergraph_Widget_PopupContentImageButton
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Replace
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Script.Engine import Conv_StringToText
from Game.FactoryGame.Interface.UI.InGame.Widget_PopupContentImageButton import Widget_PopupContentImageButton
from Script.Engine import BooleanOR
from Script.FactoryGame import GetProducedIn
from Script.UMG import Widget
from Script.FactoryGame import Default__FGRecipe
from Script.UMG import PanelWidget
from Script.FactoryGame import FGButtonWidget
from Game.FactoryGame.Interface.UI.InGame.Widget_TooltipInventorySlots import Widget_TooltipInventorySlots
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import FGSchematic
from Script.UMG import UserWidget
from Game.FactoryGame.Buildable.Factory.SmelterMk1.Build_SmelterMk1 import Build_SmelterMk1
from Game.FactoryGame.Interface.UI.InGame.Widget_TooltipRecipe import Widget_TooltipRecipe
from Script.Engine import NotEqual_ObjectObject
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import Default__FGSchematic
from Script.UMG import Create
from Script.Engine import Array_IsValidIndex
from Game.FactoryGame.Interface.UI.Assets.Shared.ThumbsUp_64 import ThumbsUp_64
from Script.SlateCore import SlateBrush
from Script.FactoryGame import ItemAmount
from Game.FactoryGame.-Shared.Blueprint.BP_SchematicHelper import Default__BP_SchematicHelper
from Script.FactoryGame import GetSchematicDisplayName
from Game.FactoryGame.Interface.UI.InGame.Widget_PopupContentImageButton import ExecuteUbergraph_Widget_PopupContentImageButton.K2Node_Event_IsDesignTime

class Widget_PopupContentImageButton(FGButtonWidget):
    mSchematicTitle: FText = NSLOCTEXT("", "B8B30D1B44FB826DBE545FAF9C59C059", "Schematic Name")
    mIsDisabled: bool
    mIsSelected: bool
    mListWidget: Ptr[PanelWidget]
    mParentWidget: Ptr[UserWidget]
    NotifyPopupContentIndexSelect: FMulticastScriptDelegate
    mImageBrush: SlateBrush
    mSchematicCost: List[ItemAmount]
    mItemTexture: Ptr[Texture2D]
    mSchematic: TSubclassOf[FGSchematic]
    mTooltipRecipe: Ptr[Widget_TooltipRecipe]
    
    def CacheDataFromReward(self):
        ReturnValue: FText = Default__FGSchematic.GetSchematicDisplayName(self.mSchematic)
        self.mSchematicTitle = ReturnValue
        ReturnValue_0: SlateBrush = Default__FGSchematic.GetItemIcon(self.mSchematic)
        self.mImageBrush = ReturnValue_0
        ReturnValue_1: List[ItemAmount] = Default__FGSchematic.GetCost(self.mSchematic)
        self.mSchematicCost = ReturnValue_1
        
        Recipes = None
        Default__BP_SchematicHelper.GetRecipesFromSchematic(self.mSchematic, self, Ref[Recipes])
        localRecipes = Recipes
        
        ReturnValue_2: int32 = len(localRecipes)
        ReturnValue_3: bool = ReturnValue_2 > 0
        if not ReturnValue_3:
            goto('L888')
        if not True:
            goto('L707')
        
        Item = None
        Item = localRecipes[0]
        ReturnValue_4: List[ItemAmount] = Default__FGRecipe.GetProducts(Item, False)
        
        Item1 = None
        Item1 = ReturnValue_4[0]
        ReturnValue_5: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(Item1.ItemClass)
        self.mItemTexture = ReturnValue_5
        # End
        
        Result = None
        # Label 707
        Default__BP_SchematicHelper.GetUnlocksInventorySlot(self.mSchematic, self, Ref[Result])
        
        Result = None
        Default__BP_SchematicHelper.GetUnlocksHandSlots(self.mSchematic, self, Ref[Result])
        ReturnValue_6: bool = BooleanOR(Result, Result)
        if not ReturnValue_6:
            goto('L888')
        self.mItemTexture = ThumbsUp_64
    

    def GetIsSmeltable(self, inClass: TSubclassOf[FGRecipe]):
        ExecutionFlow.Push("L732")
        LocalIsSmeltable = False
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 73
        ReturnValue: List[TSubclassOf[Object]] = Default__FGRecipe.GetProducedIn(inClass)
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Not_PreBool(Variable)
        ReturnValue_2: bool = Variable_0 <= ReturnValue_0
        ReturnValue_3: bool = ReturnValue_1 and ReturnValue_2
        if not ReturnValue_3:
            goto('L562')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L586")
        ReturnValue = Default__FGRecipe.GetProducedIn(inClass)
        
        Item = None
        Item = ReturnValue[Variable_1]
        1: TSubclassOf[Build_FoundryMk1] = ClassCast[Build_FoundryMk1](Item)
        bSuccess: bool = 1
        if not bSuccess:
            goto('L660')
        # Label 539
        LocalIsSmeltable = True
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 562
        IsSmeltable = LocalIsSmeltable
        # End
        # Label 586
        ReturnValue_4: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_4
        goto('L73')
        # Label 660
        1_0: TSubclassOf[Build_SmelterMk1] = ClassCast[Build_SmelterMk1](None)
        bSuccess1: bool = 1_0
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        goto('L539')
    

    def ClearSelectionList(self):
        ExecutionFlow.Push("L468")
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mListWidget)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        # Label 89
        ReturnValue_0: int32 = self.mListWidget.GetChildrenCount()
        ReturnValue_1: int32 = ReturnValue_0 - 1
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L394")
        ReturnValue_3: Ptr[Widget] = self.mListWidget.GetChildAt(Variable)
        Button: Ptr[Widget_PopupContentImageButton] = Cast[Widget_PopupContentImageButton](ReturnValue_3)
        bSuccess: bool = Button
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Button.mIsSelected = False
        goto(ExecutionFlow.Pop())
        # Label 394
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L89')
    

    def GetIndexInList(self):
        ReturnValue: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_0: bool = NotEqual_ObjectObject(self.mListWidget, ReturnValue)
        if not ReturnValue_0:
            goto('L163')
        ReturnValue_1: int32 = self.mListWidget.GetChildIndex(self.mParentWidget)
        index = ReturnValue_1
        # End
        # Label 163
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(self.mListWidget)
        if not ReturnValue_2:
            goto('L311')
        ReturnValue1: int32 = self.mListWidget.GetChildIndex(self)
        index = ReturnValue1
        # End
        # Label 311
        index = 0
    

    def GetTextColor(self):
        if not self.mIsDisabled:
            goto('L101')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Text
        goto('L346')
        # Label 101
        ReturnValue_0: bool = self.IsHovered()
        ReturnValue_1: bool = BooleanOR(self.mIsSelected, ReturnValue_0)
        # Label 163
        if not ReturnValue_1:
            goto('L264')
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue = TextWhite
        goto('L346')
        
        TextWhite = None
        GraphicsWhite = None
        # Label 264
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue = TextWhite
    

    def GetBackgroundColor(self):
        if not self.mIsSelected:
            goto('L101')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Graphics
        goto('L256')
        # Label 101
        LinearColor.R = 0
        LinearColor.G = 0
        LinearColor.B = 0
        LinearColor.A = 0
        ReturnValue = LinearColor
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_PopupContentImageButton.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PopupContentImageButton(512)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_PopupContentImageButton(1377)
    

    def UpdateButton(self, Title: FText, ImageBrush: SlateBrush):
        ExecuteUbergraph_Widget_PopupContentImageButton.K2Node_CustomEvent_Title = Title #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_PopupContentImageButton.K2Node_CustomEvent_ImageBrush = ImageBrush #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PopupContentImageButton(1483)
    

    def BndEvt__mPopupContentButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PopupContentImageButton(1574)
    

    def BndEvt__mPopupContentButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PopupContentImageButton(1651)
    

    def BndEvt__mPopupContentButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PopupContentImageButton(1688)
    

    def ExecuteUbergraph_Widget_PopupContentImageButton(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: Ptr[Widget_TooltipInventorySlots] = Default__WidgetBlueprintLibrary.Create(self, Widget_TooltipInventorySlots, None)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue, "mSchematic", self.mSchematic)
        ReturnValue1: Ptr[PanelSlot] = self.VerticalBox_1.AddChild(ReturnValue)
        goto(ExecutionFlow.Pop())
        
        Recipes = None
        # Label 183
        Default__BP_SchematicHelper.GetRecipesFromSchematic(self.mSchematic, self, Ref[Recipes])
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[Widget_TooltipRecipe] = Default__WidgetBlueprintLibrary.Create(self, Widget_TooltipRecipe, ReturnValue_0)
        
        Recipes = None
        Item = None
        Item = Recipes[0]
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue1_0, "mRecipe", Item)
        self.mTooltipRecipe = ReturnValue1_0
        ReturnValue_1: Ptr[PanelSlot] = self.VerticalBox_1.AddChild(self.mTooltipRecipe)
        goto(ExecutionFlow.Pop())
        self.CacheDataFromReward()
        
        ReturnValue_2: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[self.mSchematicTitle])
        ReturnValue_3: FString = Default__KismetStringLibrary.Replace(ReturnValue_2, "Alternate:", "Alternate Blueprint:", 1)
        ReturnValue_4: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_3)
        self.UpdateButton(ReturnValue_4, self.mImageBrush)
        SlateBrush.ImageSize = self.mBlueprintYealdImage.Brush.ImageSize
        SlateBrush.Margin = self.mBlueprintYealdImage.Brush.Margin
        SlateBrush.TintColor = self.mBlueprintYealdImage.Brush.TintColor
        SlateBrush.ResourceObject = self.mItemTexture
        SlateBrush.DrawAs = self.mBlueprintYealdImage.Brush.DrawAs
        SlateBrush.Tiling = self.mBlueprintYealdImage.Brush.Tiling
        SlateBrush.Mirroring = self.mBlueprintYealdImage.Brush.Mirroring
        
        SlateBrush = None
        self.mBlueprintYealdImage.SetBrush(Ref[SlateBrush])
        ExecutionFlow.Push("L15")
        
        Recipes1 = None
        Default__BP_SchematicHelper.GetRecipesFromSchematic(self.mSchematic, self, Ref[Recipes1])
        
        Recipes1 = None
        ReturnValue_5: bool = Default__KismetArrayLibrary.Array_IsValidIndex(0, Ref[Recipes1])
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        goto('L183')
        ReturnValue_6: bool = Default__KismetSystemLibrary.IsValid(self.mListWidget)
        if not ReturnValue_6:
            goto('L1443')
        goto(ExecutionFlow.Pop())
        # Label 1443
        ReturnValue_7: Ptr[PanelWidget] = self.GetParent()
        self.mListWidget = ReturnValue_7
        goto(ExecutionFlow.Pop())
        self.mSchematicName.SetText(Title)
        
        ImageBrush = None
        self.mItemImageBrush.SetBrush(Ref[ImageBrush])
        goto(ExecutionFlow.Pop())
        self.ClearSelectionList()
        self.mIsSelected = True
        
        index = None
        self.GetIndexInList(Ref[index])
        self.NotifyPopupContentIndexSelect.ProcessMulticastDelegate(index)
        goto(ExecutionFlow.Pop())
        self.mTooltipRecipe.OnHovered()
        goto(ExecutionFlow.Pop())
        self.mTooltipRecipe.OnUnhovered()
        goto(ExecutionFlow.Pop())
    

    def NotifyPopupContentIndexSelect__DelegateSignature(self, ChildIndex: int32):
        pass
    
