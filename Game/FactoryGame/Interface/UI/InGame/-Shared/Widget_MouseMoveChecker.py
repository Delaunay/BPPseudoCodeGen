
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_MouseMoveChecker import ExecuteUbergraph_Widget_MouseMoveChecker
from Script.Engine import K2_SetTimerDelegate
from Script.CoreUObject import Vector2D
from Script.Engine import TimerHandle
from Script.Engine import GetMousePosition
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import NotEqual_Vector2DVector2D
from Script.UMG import UserWidget

class Widget_MouseMoveChecker(UserWidget):
    mLastMousePos: Vector2D
    TimerHandle: TimerHandle
    mUpdateTime: float = 0.10000000149011612
    OnMouseMoved: FMulticastScriptDelegate
    Visibility = ESlateVisibility::HitTestInvisible
    
    def CheckIfMouseMove(self):
        self.ExecuteUbergraph_Widget_MouseMoveChecker(453)
    

    def StopCheckMouse(self):
        self.ExecuteUbergraph_Widget_MouseMoveChecker(664)
    

    def StartCheckMouse(self):
        self.ExecuteUbergraph_Widget_MouseMoveChecker(711)
    

    def ExecuteUbergraph_Widget_MouseMoveChecker(self):
        # Label 10
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        LocationX = None
        LocationY = None
        ReturnValue_0: bool = ReturnValue.GetMousePosition(Ref[LocationX], Ref[LocationY])
        ReturnValue_1: Vector2D = Vector2D(LocationX, LocationY)
        self.mLastMousePos = ReturnValue_1
        OutputDelegate.BindUFunction(self, CheckIfMouseMove)
        ReturnValue_2: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mUpdateTime, True)
        self.TimerHandle = ReturnValue_2
        # End
        # Label 291
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        LocationX1 = None
        LocationY1 = None
        ReturnValue1_0: bool = ReturnValue1.GetMousePosition(Ref[LocationX1], Ref[LocationY1])
        ReturnValue1_1: Vector2D = Vector2D(LocationX1, LocationY1)
        self.mLastMousePos = ReturnValue1_1
        # End
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        
        LocationX2 = None
        LocationY2 = None
        ReturnValue2_0: bool = ReturnValue2.GetMousePosition(Ref[LocationX2], Ref[LocationY2])
        ReturnValue2_1: Vector2D = Vector2D(LocationX2, LocationY2)
        ReturnValue_3: bool = NotEqual_Vector2DVector2D(self.mLastMousePos, ReturnValue2_1, 9.999999747378752e-05)
        if not ReturnValue_3:
            goto('L716')
        self.OnMouseMoved.ProcessMulticastDelegate()
        goto('L291')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.TimerHandle])
        # End
        goto('L10')
    

    def OnMouseMoved__DelegateSignature(self):
        pass
    
