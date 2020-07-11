
from codegen.ue4_stub import *

from Script.Engine import Default__KismetInputLibrary
from Script.Engine import SetTextPropertyByName
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu_RightClickMenu import Widget_BuildMenu_RightClickMenu
from Game.FactoryGame.Interface.UI.InGame.Codex.BPW_Interactable_Recipe import ExecuteUbergraph_BPW_Interactable_Recipe
from Script.Engine import SetClassPropertyByName
from Script.InputCore import Key
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.Engine import Conv_Vector2dToString
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import Handled
from Script.UMG import PlayAnimation
from Script.UMG import Unhandled
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import Default__SlateBlueprintLibrary
from Script.Engine import SetBoolPropertyByName
from Script.UMG import Widget
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import WidgetAnimation
from Script.Engine import PointerEvent_GetEffectingButton
from Script.Engine import EqualEqual_KeyKey
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.InGame.Widget_TooltipRecipe import Widget_TooltipRecipe
from Script.Engine import Subtract_Vector2DVector2D
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Script.FactoryGame import FGRecipe
from Script.CoreUObject import Vector2D
from Script.UMG import GetMousePositionOnViewport
from Script.UMG import LocalToViewport
from Script.Engine import PrintString
from Script.UMG import EventReply
from Script.CoreUObject import LinearColor

class BPW_Interactable_Recipe(UserWidget):
    HoverFade: Ptr[WidgetAnimation]
    mRecipeNameText: FText
    mHideProductionInfo: bool
    mRecipe: TSubclassOf[FGRecipe]
    
    def GetToDoListMenu(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_BuildMenu_RightClickMenu] = Default__WidgetBlueprintLibrary.Create(self, Widget_BuildMenu_RightClickMenu, ReturnValue)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_0, "mRecipe", self.mRecipe)
        ReturnValue_1: Ptr[Widget] = ReturnValue_0
    

    def OnMouseButtonUp(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.PointerEvent_GetEffectingButton(Ref[MouseEvent])
        ReturnValue_0: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "RightMouseButton"))
        if not ReturnValue_0:
            goto('L640')
        Default__KismetSystemLibrary.PrintString(self, "RMB down", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        ReturnValue_1: Vector2D = Default__WidgetLayoutLibrary.GetMousePositionOnViewport(self)
        
        PixelPosition = None
        ViewportPosition = None
        Default__SlateBlueprintLibrary.LocalToViewport(self, Vector2D(X = 0, Y = 0), Ref[MyGeometry], Ref[PixelPosition], Ref[ViewportPosition])
        ReturnValue_2: Vector2D = Subtract_Vector2DVector2D(ReturnValue_1, ViewportPosition)
        ReturnValue_3: FString = Default__KismetStringLibrary.Conv_Vector2dToString(ReturnValue_2)
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_3, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        ReturnValue_4: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_5: EventReply = ReturnValue_4
        goto('L717')
        # Label 640
        ReturnValue_6: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_5 = ReturnValue_6
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_Interactable_Recipe(61)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_Interactable_Recipe(432)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_Interactable_Recipe(483)
    

    def ExecuteUbergraph_BPW_Interactable_Recipe(self):
        # Label 10
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.HoverFade, 0, 1, 1, 1)
        # End
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[Widget_TooltipRecipe] = Default__WidgetBlueprintLibrary.Create(self, Widget_TooltipRecipe, ReturnValue_0)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_1, "mRecipe", self.mRecipe)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_1, "mRecipeNameText", Ref[self.mRecipeNameText])
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_1, "HideProductionInfo", self.mHideProductionInfo)
        ReturnValue_2: Ptr[PanelSlot] = self.mContainer.AddChild(ReturnValue_1)
        self.Widget_BuildMenu_RightClickMenu.mRecipe = self.mRecipe
        # End
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.HoverFade, 0, 1, 0, 1)
        # End
        goto('L10')
    
