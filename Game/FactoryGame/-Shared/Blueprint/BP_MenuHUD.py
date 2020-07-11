
from codegen.ue4_stub import *

from Script.Engine import PlayerController
from Script.UMG import Create
from Game.FactoryGame.-Shared.Blueprint.BP_MenuHUD import ExecuteUbergraph_BP_MenuHUD
from Game.FactoryGame.Interface.UI.Menu.BP_FrontEnd import BP_FrontEnd
from Script.FactoryGame import FGHUDBase
from Script.UMG import AddToViewport
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import GetOwningPlayerController

class BP_MenuHUD(FGHUDBase):
    mFrontEnd: Ptr[BP_FrontEnd]
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_MenuHUD(93)
    

    def ExecuteUbergraph_BP_MenuHUD(self):
        # Label 10
        self.mFrontEnd.SetupMainMenu()
        # End
        # Label 51
        self.mFrontEnd.AddToViewport(0)
        goto('L10')
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayerController()
        ReturnValue_0: Ptr[BP_FrontEnd] = Default__WidgetBlueprintLibrary.Create(self, BP_FrontEnd, ReturnValue)
        self.mFrontEnd = ReturnValue_0
        goto('L51')
    
