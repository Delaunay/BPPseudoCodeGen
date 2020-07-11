
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Default__FGGameUserSettings
from Script.Engine import GetPlayerController
from Script.Engine import PlayerController
from Script.Engine import Default__GameplayStatics
from Script.Engine import Actor
from Script.Engine import AnimNotifyState
from Script.FactoryGame import GetGameUI
from Script.FactoryGame import GetFGGameUserSettings
from Script.Engine import GetOwner
from Script.FactoryGame import GetBoolOptionValue
from Script.Engine import IsValid
from Script.FactoryGame import FGGameUI
from Script.FactoryGame import FGGameUserSettings
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers

class SubtitleNotifyEvent(AnimNotifyState):
    mSubtitle: FText
    
    def Received_NotifyBegin(self):
        ReturnValue: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        ReturnValue_0: bool = ReturnValue.GetBoolOptionValue("FG.UseDirectionalSubtitle")
        if not ReturnValue_0:
            goto('L540')
        ReturnValue_1: Ptr[PlayerController] = Default__GameplayStatics.GetPlayerController(MeshComp, 0)
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_1)
        if not ReturnValue_2:
            goto('L529')
        ReturnValue_1 = Default__GameplayStatics.GetPlayerController(MeshComp, 0)
        
        AsFGHUD = None
        Default__BPHUDHelpers.GetFGHud(ReturnValue_1, MeshComp, Ref[AsFGHUD])
        ReturnValue_3: Ptr[FGGameUI] = AsFGHUD.GetGameUI()
        ReturnValue_4: Ptr[Actor] = MeshComp.GetOwner()
        
        ReturnValue_3.ShowDirectionalSubtitle(ReturnValue_4, TotalDuration, True, Ref[self.mSubtitle])
        ReturnValue_5: bool = True
        goto('L540')
        # Label 529
        ReturnValue_5 = False
    
