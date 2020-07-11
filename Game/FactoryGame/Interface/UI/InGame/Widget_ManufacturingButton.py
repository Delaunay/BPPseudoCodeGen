
from codegen.ue4_stub import *

from Script.Engine import Default__KismetInputLibrary
from Script.AkAudio import PostAkEvent
from Script.Engine import Texture2D
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Manufacturing import Widget_Manufacturing
from Script.Engine import EqualEqual_ClassClass
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Interface.UI.InGame.Widget_ManufacturingButton import ExecuteUbergraph_Widget_ManufacturingButton
from Script.Engine import Pawn
from Script.InputCore import Key
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_MouseOver import Play_UI_WorkBench_MouseOver
from Script.FactoryGame import SetButton
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_Select import Play_UI_WorkBench_Select
from Script.FactoryGame import GetProducts
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Player.BP_PlayerState import BP_PlayerState
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import Handled
from Script.UMG import Unhandled
from Script.Engine import PointerEvent_IsMouseButtonDown
from Script.Engine import TimerHandle
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import SetColorAndOpacity
from Script.FactoryGame import GetSmallIcon
from Script.Engine import IsInputKeyDown
from Script.Engine import BooleanOR
from Script.UMG import Construct
from Script.FactoryGame import Default__FGRecipe
from Script.FactoryGame import FGButtonWidget
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Interface.UI.InGame.Widget_ManufacturingButton import ExecuteUbergraph_Widget_ManufacturingButton.K2Node_Event_IsDesignTime
from Script.UMG import GetOwningPlayerPawn
from Script.FactoryGame import GetRecipeName
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import FGRecipe
from Script.Engine import Array_IsValidIndex
from Script.FactoryGame import ItemAmount
from Script.AkAudio import AkComponent
from Script.Engine import IsValidClass
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.UMG import EventReply
from Script.CoreUObject import LinearColor

class Widget_ManufacturingButton(FGButtonWidget):
    mRecipeClass: TSubclassOf[FGRecipe]
    mManufacturingWidget: Ptr[Widget_Manufacturing]
    OnManufacturingRecipeClicked: FMulticastScriptDelegate
    OnManufacturingRecipeHovered: FMulticastScriptDelegate
    OnStopHoveringManufacturingRecipe: FMulticastScriptDelegate
    mUpdateButtonTimer: TimerHandle
    bIsFocusable = True
    
    def GetByProductIcon(self):
        ReturnValue: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mRecipeClass, False)
        
        ReturnValue_0: bool = Default__KismetArrayLibrary.Array_IsValidIndex(1, Ref[ReturnValue])
        if not ReturnValue_0:
            goto('L736')
        ReturnValue = Default__FGRecipe.GetProducts(self.mRecipeClass, False)
        ReturnValue_1: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(ReturnValue[1].ItemClass)
        SlateBrush.ImageSize = self.mByProductIcon.Brush.ImageSize
        SlateBrush.Margin = self.mByProductIcon.Brush.Margin
        SlateBrush.TintColor = self.mByProductIcon.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue_1
        SlateBrush.DrawAs = self.mByProductIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mByProductIcon.Brush.Tiling
        SlateBrush.Mirroring = self.mByProductIcon.Brush.Mirroring
        
        SlateBrush = None
        self.mByProductIcon.SetBrush(Ref[SlateBrush])
        # End
        # Label 736
        self.mByProduct_Overlay.SetVisibility(1)
    

    def UpdateButtonStyle(self):
        
        mIsSelected = None
        self.CheckIsSelected(Ref[mIsSelected])
        Variable3: LinearColor = LinearColor(R = 0.13286800682544708, G = 0.13286800682544708, B = 0.13563300669193268, A = 1)
        Variable4: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 0)
        Variable5: LinearColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.057805001735687256, A = 1)
        ReturnValue1: bool = self.IsHovered()
        Variable2: bool = ReturnValue1
        Variable3_0: bool = mIsSelected
        
        switch = {
            False: Variable4,
            True: Variable3
        }
        
        switch_0 = {
            False: switch.get(Variable2, None),
            True: Variable5
        }
        self.mButtonColor.SetColorAndOpacity(switch_0.get(Variable3_0, None))
        Variable: LinearColor = LinearColor(R = 0.13286800682544708, G = 0.13286800682544708, B = 0.13563300669193268, A = 1)
        Variable1: LinearColor = LinearColor(R = 0.6038280129432678, G = 0.5972020030021667, B = 0.5972020030021667, A = 1)
        Variable2_0: LinearColor = LinearColor(R = 0.13286800682544708, G = 0.13286800682544708, B = 0.13563300669193268, A = 1)
        ReturnValue: bool = self.IsHovered()
        Variable_0: bool = ReturnValue
        Variable1_0: bool = mIsSelected
        
        switch_1 = {
            False: Variable1,
            True: Variable
        }
        
        switch_2 = {
            False: switch_1.get(Variable_0, None),
            True: Variable2_0
        }
        self.mByProductBG.SetColorAndOpacity(switch_2.get(Variable1_0, None))
    

    def CheckIsSelected(self):
        ReturnValue: bool = EqualEqual_ClassClass(self.mManufacturingWidget.mActivatedRecipe, self.mRecipeClass)
        mIsSelected = ReturnValue
    

    def GetRecipeName(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mRecipeClass)
        if not ReturnValue:
            goto('L169')
        ReturnValue_0: FText = Default__FGRecipe.GetRecipeName(self.mRecipeClass)
        self.mProductName.SetText(ReturnValue_0)
    

    def GetRecipeIcon(self):
        ReturnValue: List[ItemAmount] = Default__FGRecipe.GetProducts(self.mRecipeClass, False)
        
        Item = None
        Item = ReturnValue[0]
        # Label 115
        ReturnValue_0: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(Item.ItemClass)
        SlateBrush.ImageSize = self.mIcon.Brush.ImageSize
        SlateBrush.Margin = self.mIcon.Brush.Margin
        SlateBrush.TintColor = self.mIcon.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue_0
        SlateBrush.DrawAs = self.mIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mIcon.Brush.Tiling
        SlateBrush.Mirroring = self.mIcon.Brush.Mirroring
        
        SlateBrush = None
        self.mIcon.SetBrush(Ref[SlateBrush])
    

    def OnMouseButtonDown(self):
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue: bool = ReturnValue1.IsInputKeyDown(Key(KeyName = "RightShift"))
        ReturnValue1_0: bool = ReturnValue1.IsInputKeyDown(Key(KeyName = "LeftShift"))
        ReturnValue_0: bool = BooleanOR(ReturnValue1_0, ReturnValue)
        if not ReturnValue_0:
            goto('L563')
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[BP_PlayerState] = Cast[BP_PlayerState](ReturnValue_1.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
            goto('L645')
        
        ReturnValue_2: bool = Default__KismetInputLibrary.PointerEvent_IsMouseButtonDown(Key(KeyName = "RightMouseButton"), Ref[MouseEvent])
        if not ReturnValue_2:
            goto('L727')
        State.RemoveRecipeFromShoppingList(self.mRecipeClass, 0)
        ReturnValue_3: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_4: EventReply = ReturnValue_3
        goto('L804')
        # Label 563
        ReturnValue2: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_4 = ReturnValue2
        goto('L804')
        # Label 645
        ReturnValue_5: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_4 = ReturnValue_5
        goto('L804')
        # Label 727
        ReturnValue1_1: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_4 = ReturnValue1_1
    

    def BndEvt__mRecipeButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ManufacturingButton(267)
    

    def BndEvt__mRecipeButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ManufacturingButton(305)
    

    def BndEvt__mRecipeButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ManufacturingButton(310)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ManufacturingButton(315)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_ManufacturingButton.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManufacturingButton(464)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_ManufacturingButton(497)
    

    def ExecuteUbergraph_Widget_ManufacturingButton(self):
        # Label 10
        self.GetByProductIcon()
        # End
        # Label 29
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_Select, ReturnValue, True)
        # End
        # Label 115
        ReturnValue1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_MouseOver, ReturnValue1, True)
        # End
        # Label 201
        self.OnManufacturingRecipeClicked.ProcessMulticastDelegate(self.mRecipeClass)
        goto('L29')
        # Label 234
        self.OnManufacturingRecipeHovered.ProcessMulticastDelegate(self.mRecipeClass)
        goto('L115')
        goto('L201')
        # Label 272
        self.OnStopHoveringManufacturingRecipe.ProcessMulticastDelegate(self.mRecipeClass)
        # End
        goto('L234')
        goto('L272')
        self.Construct()
        self.SetButton(self.mRecipeButton)
        OutputDelegate.BindUFunction(self, UpdateButtonStyle)
        ReturnValue_1: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.004999999888241291, True)
        self.mUpdateButtonTimer = ReturnValue_1
        # End
        self.GetRecipeName()
        self.GetRecipeIcon()
        goto('L10')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mUpdateButtonTimer])
    

    def OnStopHoveringManufacturingRecipe__DelegateSignature(self, UnhoveredRecipe: TSubclassOf[FGRecipe]):
        pass
    

    def OnManufacturingRecipeHovered__DelegateSignature(self, RecipeHover: TSubclassOf[FGRecipe]):
        pass
    

    def OnManufacturingRecipeClicked__DelegateSignature(self, Recipe: TSubclassOf[FGRecipe]):
        pass
    
