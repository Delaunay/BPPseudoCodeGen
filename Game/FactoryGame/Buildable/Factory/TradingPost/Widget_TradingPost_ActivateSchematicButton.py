
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import FClamp
from Script.Engine import Pawn
from Game.FactoryGame.Interface.UI.Audio.WorkBench.Play_UI_WorkBench_MouseOver import Play_UI_WorkBench_MouseOver
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Game.FactoryGame.Interface.UI.Assets.ShoppingList.ficsit_checkmark_64 import ficsit_checkmark_64
from Script.UMG import ESlateVisibility
from Script.Engine import GetWorldDeltaSeconds
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicList import Widget_SchematicList
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost_ActivateSchematicButton import ExecuteUbergraph_Widget_TradingPost_ActivateSchematicButton
from Script.Engine import BooleanOR
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGButtonWidget
from Script.Engine import LinearColorLerp
from Script.FactoryGame import FGSchematic
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import GetOwningPlayerPawn
from Script.FactoryGame import IsSchematicPurchased
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import FGSchematicManager
from Game.FactoryGame.Interface.UI.Assets.Shared.Launch_Icon import Launch_Icon
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost import Widget_TradingPost
from Script.AkAudio import AkComponent
from Game.FactoryGame.-Shared.Blueprint.BP_SchematicHelper import Default__BP_SchematicHelper
from Script.FactoryGame import Default__FGSchematicManager
from Script.CoreUObject import LinearColor

class Widget_TradingPost_ActivateSchematicButton(FGButtonWidget):
    mSchematicList: Ptr[Widget_SchematicList]
    onSchematicActivateButtonClicked: FMulticastScriptDelegate
    mTradingPost: Ptr[Widget_TradingPost]
    T: float
    LerpGoingUp: bool
    LerpSpeed: float = 0.5
    LerpHold: float = 0.5
    IsSelectedSchematicLocked: bool
    IsSelectedSchematicPurchased: bool
    mSelectedSchematicClass: TSubclassOf[FGSchematic]
    bIsFocusable = True
    
    def SetSelectedSchematic(self, SelectedSchematic: TSubclassOf[FGSchematic]):
        self.mSelectedSchematicClass = SelectedSchematic
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        IsSchematicLockedByTutorial = None
        Default__BP_SchematicHelper.IsSchematicLockedByTutorial(ReturnValue1, self.mSelectedSchematicClass, self, Ref[IsSchematicLockedByTutorial])
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        
        IsSchematicPhaseLocked = None
        Default__BP_SchematicHelper.IsSchematicPhaseLocked(ReturnValue2, self.mSelectedSchematicClass, self, Ref[IsSchematicPhaseLocked])
        # Label 219
        ReturnValue: bool = BooleanOR(IsSchematicPhaseLocked, IsSchematicLockedByTutorial)
        
        IsSchematicDependentLocked = None
        Default__BP_SchematicHelper.IsSchematicDependentLocked(ReturnValue3, self.mSelectedSchematicClass, self, Ref[IsSchematicDependentLocked])
        ReturnValue1_0: bool = BooleanOR(ReturnValue, IsSchematicDependentLocked)
        self.IsSelectedSchematicLocked = ReturnValue1_0
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue_0)
        ReturnValue_2: bool = ReturnValue_1.IsSchematicPurchased(self.mSelectedSchematicClass)
        self.IsSelectedSchematicPurchased = ReturnValue_2
    

    def GetClickable(self):
        ReturnValue: bool = BooleanOR(self.IsSelectedSchematicLocked, self.IsSelectedSchematicPurchased)
        if not ReturnValue:
            goto('L77')
        ReturnValue_0: uint8 = 3
        goto('L97')
        # Label 77
        ReturnValue_0 = 0
    

    def GetText(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_1: bool = ReturnValue_0.IsSchematicPurchased(self.mSelectedSchematicClass)
        if not ReturnValue_1:
            goto('L219')
        ReturnValue_2: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 160, 'Value': 'Already Unlocked'}"
        goto('L376')
        # Label 219
        if not self.IsSelectedSchematicLocked:
            goto('L302')
        ReturnValue_2 = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 253, 'Value': 'Locked'}"
        goto('L376')
        # Label 302
        ReturnValue_2 = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 322, 'Value': 'Select Milestone'}"
    

    def GetColor(self):
        ReturnValue: bool = BooleanOR(self.IsSelectedSchematicLocked, self.IsSelectedSchematicPurchased)
        if not ReturnValue:
            goto('L139')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_0: LinearColor = Graphics
        goto('L1077')
        # Label 139
        ReturnValue_1: bool = self.IsHovered()
        if not ReturnValue_1:
            goto('L264')
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue_0 = Orange
        goto('L1077')
        # Label 264
        if not self.LerpGoingUp:
            goto('L797')
        ReturnValue1: float = Default__GameplayStatics.GetWorldDeltaSeconds(self)
        ReturnValue1_0: float = ReturnValue1 / self.LerpSpeed
        ReturnValue1_1: float = ReturnValue1_0 + self.T
        self.T = ReturnValue1_1
        ReturnValue_2: float = self.LerpHold + 1
        ReturnValue_3: bool = self.T > ReturnValue_2
        if not ReturnValue_3:
            goto('L553')
        self.LerpGoingUp = False
        # Label 553
        ReturnValue_4: float = FClamp(self.T, 0, 1)
        
        Orange1 = None
        OrangeText1 = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange1], Ref[OrangeText1])
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_5: LinearColor = LinearColorLerp(Graphics, Orange1, ReturnValue_4)
        ReturnValue_0 = ReturnValue_5
        goto('L1077')
        # Label 797
        ReturnValue_6: float = Default__GameplayStatics.GetWorldDeltaSeconds(self)
        ReturnValue_7: float = ReturnValue_6 / self.LerpSpeed
        ReturnValue1_2: float = self.T - ReturnValue_7
        self.T = ReturnValue1_2
        ReturnValue_8: float = 0 - self.LerpHold
        ReturnValue_9: bool = self.T <= ReturnValue_8
        if not ReturnValue_9:
            goto('L553')
        self.LerpGoingUp = True
        goto('L553')
    

    def BndEvt__Button_26_K2Node_ComponentBoundEvent_100_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TradingPost_ActivateSchematicButton(60)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TradingPost_ActivateSchematicButton(166)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_TradingPost_ActivateSchematicButton(297)
    

    def ExecuteUbergraph_Widget_TradingPost_ActivateSchematicButton(self):
        # Label 10
        self.Widget_SwitchingImage.SwitchImage(Launch_Icon)
        # End
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mTradingPost)
        if not ReturnValue:
            goto('L302')
        self.mTradingPost.ActivateSelectedSchematic()
        # End
        ReturnValue_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_WorkBench_MouseOver, ReturnValue_0, True)
        self.Widget_SwitchingImage.SwitchImage(ficsit_checkmark_64)
        # End
        goto('L10')
    

    def onSchematicActivateButtonClicked__DelegateSignature(self):
        pass
    
