
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Actor
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import TimerHandle
from Script.UMG import WidgetAnimation
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Parent import ExecuteUbergraph_Widget_ActorDetails_Parent

class Widget_ActorDetails_Parent(UserWidget):
    SpawnAnim: Ptr[WidgetAnimation]
    mActor: Ptr[Actor]
    ShowPointer: bool = True
    mActorDetailsUpdateTimer: TimerHandle
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_ActorDetails_Parent(57)
    

    def ActorDetailsUpdate(self):
        self.ExecuteUbergraph_Widget_ActorDetails_Parent(177)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_ActorDetails_Parent(182)
    

    def ExecuteUbergraph_Widget_ActorDetails_Parent(self):
        
        # Label 10
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mActorDetailsUpdateTimer])
        # End
        OutputDelegate.BindUFunction(self, ActorDetailsUpdate)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.30000001192092896, True)
        self.mActorDetailsUpdateTimer = ReturnValue
        # End
        # End
        goto('L10')
    
