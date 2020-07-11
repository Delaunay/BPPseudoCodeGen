
from codegen.ue4_stub import *

from Script.UMG import SetUserFocus
from Script.Engine import Default__KismetInputLibrary
from Script.Engine import GreaterEqual_IntInt
from Script.InputCore import Key
from Script.FactoryGame import OnMenuEnterDone
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import ExecuteUbergraph_BP_MenuBase.K2Node_Event_prevMenu
from Script.Engine import Max
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import Handled
from Script.UMG import PlayAnimation
from Script.UMG import Unhandled
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import BP_MenuBase
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import ExecuteUbergraph_BP_MenuBase.K2Node_Event_prevMenu1
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import Destruct
from Script.UMG import Construct
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import ExecuteUbergraph_BP_MenuBase.K2Node_CustomEvent_PlayBackgroundAnim
from Script.FactoryGame import FGMenuBase
from Script.Engine import EqualEqual_ObjectObject
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import ExecuteUbergraph_BP_MenuBase.K2Node_Event_Animation
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import ExecuteUbergraph_BP_MenuBase
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.Menu.Widget_SubMenuBackground import Widget_SubMenuBackground
from Script.UMG import GetAllWidgetsOfClass
from Script.Engine import GetKey
from Script.Engine import EqualEqual_KeyKey
from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import ExecuteUbergraph_BP_MenuBase.K2Node_Event_noAnimation
from Script.UMG import EventReply
from Script.FactoryGame import OnMenuExitDone

class BP_MenuBase(FGMenuBase):
    mFocusWidget: Ptr[UserWidget]
    mHandleEscape: bool
    mOwningMenu: Ptr[BP_MenuBase]
    UsesSubmenuBackground: bool
    mOnEnterAnimation: Ptr[WidgetAnimation]
    mSubmenusToAnimate: List[Ptr[Widget_SubMenuBackground]]
    mNeedCustomEnterDone: bool
    
    def GatherBackgrounds(self):
        FoundWidgets: List[Ptr[Widget_SubMenuBackground]] = []
        
        Default__WidgetBlueprintLibrary.GetAllWidgetsOfClass(self, Widget_SubMenuBackground, False, Ref[FoundWidgets])
        self.mSubmenusToAnimate = FoundWidgets
    

    def PlayBackgroundEnterAnimation(self):
        ExecutionFlow.Push("L549")
        
        ReturnValue: int32 = len(self.mSubmenusToAnimate)
        ReturnValue1: int32 = ReturnValue - 1
        Variable: int32 = ReturnValue1
        
        ReturnValue = len(self.mSubmenusToAnimate)
        ReturnValue1 = ReturnValue - 1
        ReturnValue_0: int32 = Max(0, ReturnValue1)
        Variable_0: int32 = ReturnValue_0
        # Label 303
        ReturnValue_1: bool = GreaterEqual_IntInt(Variable, 0)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L475")
        
        Item = None
        Item = self.mSubmenusToAnimate[Variable_0]
        Item.PlayBackgroundSpawnAnim()
        goto(ExecutionFlow.Pop())
        # Label 475
        ReturnValue_2: int32 = Variable - 1
        Variable = ReturnValue_2
        goto('L303')
    

    def PlayEnterAnimation(self, prevMenu: Ptr[Widget]):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mOnEnterAnimation)
        if not ReturnValue:
            goto('L176')
        ReturnValue_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.mOnEnterAnimation, 0, 1, 0, 1)
        
        animate = None
        # Label 111
        self.ShouldAnimateBackground(prevMenu, Ref[animate])
        if not animate:
            goto('L210')
        self.PlayBackgroundEnterAnimation()
        # End
        # Label 176
        if not self.mNeedCustomEnterDone:
            goto('L195')
        goto('L111')
        # Label 195
        self.OnMenuEnterDone()
        goto('L111')
    

    def ShouldAnimateBackground(self, prevMenu: Ptr[Widget]):
        Base: Ptr[BP_MenuBase] = Cast[BP_MenuBase](prevMenu)
        bSuccess: bool = Base
        if not bSuccess:
            goto('L131')
        if not Base.UsesSubmenuBackground:
            goto('L131')
        Animate = False
        # End
        # Label 131
        Animate = True
    

    def RestoreFocusOnPopupClosed(self, confirm: bool):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mFocusWidget.SetUserFocus(ReturnValue)
    

    def OnKeyDown(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_0: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "Escape"))
        ReturnValue_1: bool = ReturnValue_0 and self.mHandleEscape
        if not ReturnValue_1:
            goto('L285')
        self.OnEscape()
        ReturnValue_2: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_3: EventReply = ReturnValue_2
        goto('L362')
        # Label 285
        ReturnValue_4: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_3 = ReturnValue_4
    

    def OnEscape(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mOwningMenu)
        if not ReturnValue:
            goto('L101')
        self.mOwningMenu.OnEscape()
    

    def Destruct(self):
        self.ExecuteUbergraph_BP_MenuBase(29)
    

    def Construct(self):
        self.ExecuteUbergraph_BP_MenuBase(59)
    

    def SpawnAnim(self, PlayBackgroundAnim: bool):
        ExecuteUbergraph_BP_MenuBase.K2Node_CustomEvent_PlayBackgroundAnim = PlayBackgroundAnim #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_MenuBase(64)
    

    def OnMenuEnter(self):
        ExecuteUbergraph_BP_MenuBase.K2Node_Event_prevMenu1 = prevMenu #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_MenuBase(69)
    

    def OnAnimationFinished(self):
        ExecuteUbergraph_BP_MenuBase.K2Node_Event_Animation = Animation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_MenuBase(97)
    

    def OnMenuExit(self):
        ExecuteUbergraph_BP_MenuBase.K2Node_Event_prevMenu = prevMenu #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_MenuBase.K2Node_Event_noAnimation = noAnimation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_MenuBase(164)
    

    def ExecuteUbergraph_BP_MenuBase(self):
        # Label 10
        self.GatherBackgrounds()
        # End
        self.Destruct()
        # End
        # Label 44
        self.Construct()
        goto('L10')
        goto('L44')
        # End
        self.PlayEnterAnimation(prevMenu1)
        # End
        ReturnValue: bool = EqualEqual_ObjectObject(Animation, self.mOnEnterAnimation)
        if not ReturnValue:
            goto('L174')
        self.OnMenuEnterDone()
        # End
        self.OnMenuExitDone()
    
