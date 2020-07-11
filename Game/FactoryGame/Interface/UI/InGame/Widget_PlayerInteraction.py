
from codegen.ue4_stub import *

from Script.UMG import GetOwningPlayerPawn
from Script.FactoryGame import FGUseableInterface
from Script.Engine import Actor
from Script.Engine import Default__KismetTextLibrary
from Script.UMG import UserWidget
from Script.UMG import Tick
from Script.UMG import ESlateVisibility
from Script.FactoryGame import FGCharacterPlayer
from Script.UMG import SetText
from Game.FactoryGame.Interface.UI.InGame.Widget_PlayerInteraction import ExecuteUbergraph_Widget_PlayerInteraction.K2Node_Event_MyGeometry
from Script.Engine import Pawn
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.InGame.Widget_PlayerInteraction import ExecuteUbergraph_Widget_PlayerInteraction
from Script.Engine import TextIsEmpty
from Script.FactoryGame import GetBestUsableActor
from Game.FactoryGame.Interface.UI.InGame.Widget_PlayerInteraction import ExecuteUbergraph_Widget_PlayerInteraction.K2Node_Event_InDeltaTime

class Widget_PlayerInteraction(UserWidget):
    ToggleInteract: Ptr[WidgetAnimation]
    
    def GetInteractionText(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L374')
        ReturnValue_0: Ptr[Actor] = Player.GetBestUsableActor()
        Interface: TScriptInterface[FGUseableInterface] = QueryInterface[FGUseableInterface](ReturnValue_0)
        bSuccess1: bool = Interface
        if not bSuccess1:
            goto('L399')
        
        Player.mCachedUseState = None
        ReturnValue_1: FText = GetInterfaceUObject(Interface).GetLookAtDecription(Player, Ref[Player.mCachedUseState])
        Variable: FText = ReturnValue_1
        # Label 342
        ReturnValue_2: FText = Variable
        goto('L424')
        # Label 374
        ReturnValue_2 = 
        goto('L424')
        # Label 399
        Variable = 
        goto('L342')
    

    def Tick(self):
        ExecuteUbergraph_Widget_PlayerInteraction.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_PlayerInteraction.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayerInteraction(10)
    

    def ExecuteUbergraph_Widget_PlayerInteraction(self):
        self.Tick(MyGeometry, InDeltaTime)
        ReturnValue: FText = self.GetInteractionText()
        
        self.mInteractionText.SetText(Ref[ReturnValue])
        Variable: uint8 = 2
        Variable1: uint8 = 4
        ReturnValue1: FText = self.GetInteractionText()
        
        ReturnValue_0: bool = Default__KismetTextLibrary.TextIsEmpty(Ref[ReturnValue1])
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.Overlay_0.SetVisibility(switch.get(Variable_0, None))
    
