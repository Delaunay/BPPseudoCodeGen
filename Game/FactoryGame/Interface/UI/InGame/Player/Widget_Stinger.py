
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.Audio.UpgradeVisuals.Play_UI_UnlockUpgradeJuice_Whoosh_Soft import Play_UI_UnlockUpgradeJuice_Whoosh_Soft
from Game.FactoryGame.Interface.UI.Audio.UpgradeVisuals.Play_UI_UnlockUpgradeJuice_Tick import Play_UI_UnlockUpgradeJuice_Tick
from Script.UMG import GetChildAt
from Script.Engine import PlayerController
from Script.AkAudio import PostAkEvent
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_StingerSmallIcon import Widget_StingerSmallIcon
from Script.UMG import PlayAnimation
from Script.UMG import Widget
from Script.Engine import Delay
from Script.UMG import GetChildrenCount
from Script.UMG import WidgetAnimation
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_Stinger import ExecuteUbergraph_Widget_Stinger
from Script.Engine import LatentActionInfo
from Script.UMG import UserWidget

class Widget_Stinger(UserWidget):
    HideSmallIcons: Ptr[WidgetAnimation]
    SpawnAnimation: Ptr[WidgetAnimation]
    
    def ShowSmallIcons(self):
        self.ExecuteUbergraph_Widget_Stinger(914)
    

    def ExecuteUbergraph_Widget_Stinger(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: int32 = self.SmallIconsContainer.GetChildrenCount()
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L424')
        ExecutionFlow.Push("L633")
        ReturnValue_1: Ptr[Widget] = self.SmallIconsContainer.GetChildAt(Variable)
        Icon: Ptr[Widget_StingerSmallIcon] = Cast[Widget_StingerSmallIcon](ReturnValue_1)
        bSuccess: bool = Icon
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: Ptr[UMGSequencePlayer] = Icon.PlayAnimation(Icon.SpawnAnimation, 0, 1, 0, 1.2000000476837158)
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_UnlockUpgradeJuice_Tick, ReturnValue_3, True)
        goto(ExecutionFlow.Pop())
        # Label 424
        Default__KismetSystemLibrary.Delay(self, 2, LatentActionInfo(Linkage = 501, UUID = 706485653, ExecutionFunction = "ExecuteUbergraph_Widget_Stinger", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue1_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.HideSmallIcons, 0, 1, 0, 1)
        ReturnValue_3 = self.GetOwningPlayer()
        ReturnValue_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_UnlockUpgradeJuice_Whoosh_Soft, ReturnValue_3, True)
        goto(ExecutionFlow.Pop())
        # Label 633
        ReturnValue_5: int32 = Variable + 1
        Variable: int32 = ReturnValue_5
        ReturnValue = self.SmallIconsContainer.GetChildrenCount()
        ReturnValue_6: bool = Variable > ReturnValue
        if not ReturnValue_6:
            goto('L809')
        goto('L15')
        # Label 809
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 15, UUID = -1234679614, ExecutionFunction = "ExecuteUbergraph_Widget_Stinger", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        Variable = 0
        goto('L15')
        Default__KismetSystemLibrary.Delay(self, 3.5, LatentActionInfo(Linkage = 886, UUID = 929155702, ExecutionFunction = "ExecuteUbergraph_Widget_Stinger", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
    
