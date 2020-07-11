
from codegen.ue4_stub import *

from Script.UMG import CanvasPanelSlot
from Script.UMG import SetAlignment
from Game.FactoryGame.Interface.UI.InGame.CursorParticles.CursorParticleStruct import CursorParticleStruct
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import SlotAsCanvasSlot
from Script.UMG import SetAutoSize
from Script.UMG import GetAlignment
from Script.Engine import Not_PreBool
from Game.FactoryGame.Interface.UI.InGame.CursorParticles.BP_CursorParticle import BP_CursorParticle
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import Unhandled
from Script.UMG import GetLocalSize
from Script.Engine import GreaterEqual_FloatFloat
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import GetPosition
from Script.UMG import Default__SlateBlueprintLibrary
from Script.Engine import BreakVector2D
from Script.UMG import Widget
from Script.Engine import EqualEqual_ObjectObject
from Script.Engine import SetIntPropertyByName
from Script.SlateCore import Geometry
from Script.UMG import UserWidget
from Script.Engine import Subtract_Vector2DVector2D
from Script.UMG import GetCachedGeometry
from Script.UMG import Create
from Script.UMG import GetMousePositionOnViewport
from Script.CoreUObject import Vector2D
from Script.UMG import SetPosition
from Script.UMG import LocalToViewport
from Script.Engine import IsValidClass
from Script.UMG import ForceLayoutPrepass
from Script.Engine import Add_Vector2DVector2D
from Script.UMG import AddChildToCanvas
from Script.UMG import EventReply

class Widget_UI_ParticleManager(UserWidget):
    mParticleWidgets: List[CursorParticleStruct]
    mLastClickedParticleWidget: Ptr[Widget]
    mParticleWidgetClickCount: int32
    Visibility = ESlateVisibility::HitTestInvisible
    
    def OnMouseButtonUp(self):
        self.CreateParticle()
        ReturnValue: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_0: EventReply = ReturnValue
    

    def CreateParticle(self):
        ExecutionFlow.Push("L3047")
        self.ForceLayoutPrepass()
        ReturnValue: Vector2D = Default__WidgetLayoutLibrary.GetMousePositionOnViewport(self)
        MousePosition = ReturnValue
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 150
        ReturnValue_0: bool = Not_PreBool(Variable)
        
        ReturnValue_1: int32 = len(self.mParticleWidgets)
        ReturnValue_2: bool = Variable_0 <= ReturnValue_1
        ReturnValue3: bool = ReturnValue_0 and ReturnValue_2
        if not ReturnValue3:
           goto(ExecutionFlow.Pop())
        Variable_1 = Variable_0
        ExecutionFlow.Push("L2926")
        
        Item = None
        Item = self.mParticleWidgets[Variable_1]
        LocalTestWidget = Item
        LocalLastClickedParticleWidget = LocalTestWidget.Widget_4_DCFEA59542A26364F5554A970029AEE9
        ReturnValue_3: Const[Geometry] = LocalTestWidget.Widget_4_DCFEA59542A26364F5554A970029AEE9.GetCachedGeometry()
        
        PixelPosition = None
        ViewportPosition = None
        Default__SlateBlueprintLibrary.LocalToViewport(self, Vector2D(X = 0, Y = 0), Ref[ReturnValue_3], Ref[PixelPosition], Ref[ViewportPosition])
        
        ReturnValue_4: Vector2D = Default__SlateBlueprintLibrary.GetLocalSize(Ref[ReturnValue_3])
        
        PixelPosition1 = None
        ViewportPosition1 = None
        Default__SlateBlueprintLibrary.LocalToViewport(self, Vector2D(X = 0, Y = 0), Ref[ReturnValue_3], Ref[PixelPosition1], Ref[ViewportPosition1])
        ReturnValue_5: Vector2D = Add_Vector2DVector2D(ReturnValue_4, ViewportPosition)
        
        X = None
        Y = None
        BreakVector2D(ViewportPosition1, Ref[X], Ref[Y])
        
        X1 = None
        Y1 = None
        BreakVector2D(ReturnValue_5, Ref[X1], Ref[Y1])
        
        X2 = None
        Y2 = None
        BreakVector2D(MousePosition, Ref[X2], Ref[Y2])
        ReturnValue_6: bool = Y2 <= Y1
        ReturnValue_7: bool = GreaterEqual_FloatFloat(Y2, Y)
        ReturnValue1: bool = X2 <= X1
        ReturnValue1_0: bool = GreaterEqual_FloatFloat(X2, X)
        ReturnValue_8: bool = ReturnValue1_0 and ReturnValue_7
        ReturnValue1_1: bool = ReturnValue_8 and ReturnValue1
        ReturnValue2: bool = ReturnValue1_1 and ReturnValue_6
        if not ReturnValue2:
           goto(ExecutionFlow.Pop())
        ReturnValue_9: bool = EqualEqual_ObjectObject(LocalLastClickedParticleWidget, self.mLastClickedParticleWidget)
        if not ReturnValue_9:
            goto('L3000')
        ReturnValue1_2: int32 = self.mParticleWidgetClickCount + 1
        Variable_2: int32 = ReturnValue1_2
        self.mParticleWidgetClickCount = Variable_2
        # Label 1337
        ReturnValue_10: bool = Default__KismetSystemLibrary.IsValidClass(LocalTestWidget.Particle_8_297A42C2474861AFE1EAF283EF29DB4A)
        if not ReturnValue_10:
            goto('L2914')
        ReturnValue_11: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_12: Ptr[BP_CursorParticle] = Default__WidgetBlueprintLibrary.Create(self, LocalTestWidget.Particle_8_297A42C2474861AFE1EAF283EF29DB4A, ReturnValue_11)
        ReturnValue_3 = LocalTestWidget.Widget_4_DCFEA59542A26364F5554A970029AEE9.GetCachedGeometry()
        
        PixelPosition1 = None
        ViewportPosition1 = None
        Default__SlateBlueprintLibrary.LocalToViewport(self, Vector2D(X = 0, Y = 0), Ref[ReturnValue_3], Ref[PixelPosition1], Ref[ViewportPosition1])
        ReturnValue1_3: Const[Geometry] = self.mParticleContainer.GetCachedGeometry()
        
        PixelPosition2 = None
        ViewportPosition2 = None
        Default__SlateBlueprintLibrary.LocalToViewport(self, Vector2D(X = 0, Y = 0), Ref[ReturnValue1_3], Ref[PixelPosition2], Ref[ViewportPosition2])
        ReturnValue_13: Vector2D = Subtract_Vector2DVector2D(ViewportPosition1, ViewportPosition2)
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_12, "mWidgetPosition", Ref[ReturnValue_13])
        ReturnValue_3 = LocalTestWidget.Widget_4_DCFEA59542A26364F5554A970029AEE9.GetCachedGeometry()
        
        ReturnValue_4 = Default__SlateBlueprintLibrary.GetLocalSize(Ref[ReturnValue_3])
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_12, "mWidgetSize", Ref[ReturnValue_4])
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_12, "mClickCount", self.mParticleWidgetClickCount)
        LocalParticleWidget = ReturnValue_12
        ReturnValue_14: Ptr[CanvasPanelSlot] = self.mParticleContainer.AddChildToCanvas(LocalParticleWidget)
        ReturnValue1_4: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(LocalParticleWidget)
        Variable_3: bool = LocalParticleWidget.mForceAlignment
        ReturnValue_15: Vector2D = ReturnValue1_4.GetAlignment()
        Variable_4: Vector2D = Vector2D(X = 0.5, Y = 0.5)
        
        switch = {
            False: Variable_4,
            True: ReturnValue_15
        }
        ReturnValue_14.SetAlignment(switch.get(Variable_3, None))
        ReturnValue_14.SetAutoSize(True)
        ReturnValue_16: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(LocalParticleWidget)
        ReturnValue_17: Vector2D = ReturnValue_16.GetPosition()
        Variable1: bool = LocalParticleWidget.mForcePosition
        ReturnValue2_0: Const[Geometry] = self.mParticleContainer.GetCachedGeometry()
        
        PixelPosition3 = None
        ViewportPosition3 = None
        Default__SlateBlueprintLibrary.LocalToViewport(self, Vector2D(X = 0, Y = 0), Ref[ReturnValue2_0], Ref[PixelPosition3], Ref[ViewportPosition3])
        ReturnValue1_5: Vector2D = Subtract_Vector2DVector2D(MousePosition, ViewportPosition3)
        
        switch_0 = {
            False: ReturnValue1_5,
            True: ReturnValue_17
        }
        ReturnValue_14.SetPosition(switch_0.get(Variable1, None))
        # Label 2914
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 2926
        ReturnValue_18: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_18
        goto('L150')
        # Label 3000
        self.mParticleWidgetClickCount = 0
        self.mLastClickedParticleWidget = LocalLastClickedParticleWidget
        goto('L1337')
    

    def OnMouseButtonDown(self):
        pass
    
