
from codegen.ue4_stub import *

from Script.FactoryGame import ERepresentationType
from Script.Engine import Default__KismetInputLibrary
from Script.UMG import EventReply
from Script.Engine import Texture2D
from Script.Engine import Lerp
from Script.UMG import CanvasPanelSlot
from Script.FactoryGame import GetRepresentationType
from Script.Engine import FClamp
from Game.FactoryGame.Interface.UI.Minimap.Widget_Map import ExecuteUbergraph_Widget_Map
from Game.FactoryGame.Interface.UI.Minimap.Widget_Map import ExecuteUbergraph_Widget_Map.K2Node_Event_actorRepresentation
from Script.Engine import SetObjectPropertyByName
from Script.FactoryGame import FGMapObjectWidget
from Game.FactoryGame.Interface.UI.Minimap.Widget_Map import ExecuteUbergraph_Widget_Map.K2Node_Event_normalizedWorldLocation
from Script.UMG import GetChildrenCount
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import SlotAsCanvasSlot
from Game.FactoryGame.Interface.UI.Minimap.Widget_Map import ExecuteUbergraph_Widget_Map.K2Node_Event_InFocusEvent
from Script.Engine import MaterialInstanceDynamic
from Script.Engine import SetTextureParameterValue
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.Minimap.Widget_Map import ExecuteUbergraph_Widget_Map.K2Node_Event_actorRepresentation2
from Script.Engine import PlayerController
from Script.UMG import GetChildAt
from Script.UMG import SetRenderScale
from Script.Engine import Divide_Vector2DFloat
from Script.UMG import SetRenderTranslation
from Script.UMG import Handled
from Script.Engine import TimerHandle
from Game.FactoryGame.Interface.UI.Minimap.Widget_Map import ExecuteUbergraph_Widget_Map.K2Node_Event_InDeltaTime
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Interface.UI.Minimap.Widget_Map import ExecuteUbergraph_Widget_Map.K2Node_Event_MyGeometry
from Script.UMG import StopListeningForAllInputActions
from Script.Engine import BreakVector2D
from Script.UMG import Construct
from Script.FactoryGame import GetFogOfWarTexture
from Script.UMG import Widget
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapObject import Widget_MapObject
from Script.UMG import ListenForInputAction
from Script.Engine import EqualEqual_ObjectObject
from Script.Engine import SetIntPropertyByName
from Game.FactoryGame.Interface.UI.Minimap.Widget_Map import ExecuteUbergraph_Widget_Map.K2Node_Event_actorRepresentation1
from Script.Engine import Divide_Vector2DVector2D
from Script.FactoryGame import FGMapWidget
from Script.Engine import Subtract_Vector2DVector2D
from Script.Engine import Multiply_Vector2DFloat
from Script.UMG import Create
from Script.CoreUObject import Vector2D
from Game.FactoryGame.Interface.UI.Minimap.Widget_Map import ExecuteUbergraph_Widget_Map.K2Node_Event_MouseEvent
from Script.UMG import GetDynamicMaterial
from Script.UMG import AddChildToCanvas
from Script.UMG import RemoveChild
from Script.Engine import PointerEvent_GetWheelDelta
from Script.UMG import GetMousePositionScaledByDPI
from Script.UMG import SetZOrder

class Widget_Map(FGMapWidget):
    mMoveMapHandle: TimerHandle
    mMapOrigin: Vector2D
    mMouseOrigin: Vector2D
    mIsMapMoving: bool
    mMaxZoom: float = 8
    mMinZoom: float = 0.5
    ZoomChanged: FMulticastScriptDelegate
    OnObjectAddedToMapDispatch: FMulticastScriptDelegate
    OnObjectUpdatedOnMapDispatch: FMulticastScriptDelegate
    OnObjectRemovedFromMapDispatch: FMulticastScriptDelegate
    
    def StartScrollMap(self):
        self.mIsMapMoving = True
        self.mMapOrigin = self.mMapScrollContainer.RenderTransform.Translation
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        LocationX = None
        LocationY = None
        ReturnValue_0: bool = Default__WidgetLayoutLibrary.GetMousePositionScaledByDPI(ReturnValue, Ref[LocationX], Ref[LocationY])
        ReturnValue_1: Vector2D = Vector2D(LocationX, LocationY)
        self.mMouseOrigin = ReturnValue_1
    

    def DiscardInput(self):
        pass
    

    def ListenForInputActions(self, InteractWidget: Ptr[FGInteractWidget]):
        OutputDelegate.BindUFunction(self, StartScrollMap)
        InteractWidget.ListenForInputAction("PrimaryFire", 0, True, OutputDelegate)
        OutputDelegate2.BindUFunction(self, ClearScrollMap)
        InteractWidget.ListenForInputAction("PrimaryFire", 1, True, OutputDelegate2)
        OutputDelegate1.BindUFunction(self, DiscardInput)
        InteractWidget.ListenForInputAction("PrimaryFire", 0, True, OutputDelegate1)
        OutputDelegate1.BindUFunction(self, DiscardInput)
        InteractWidget.ListenForInputAction("PrimaryFire", 2, True, OutputDelegate1)
    

    def UpdateObjectOnMap(self, actorRepresentation: Ptr[FGActorRepresentation]):
        ExecutionFlow.Push("L480")
        Variable: int32 = 0
        # Label 28
        ReturnValue: int32 = self.mMapObjectPanel.GetChildrenCount()
        ReturnValue_0: int32 = ReturnValue - 1
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L406")
        ReturnValue_2: Ptr[Widget] = self.mMapObjectPanel.GetChildAt(Variable)
        Widget: Ptr[FGMapObjectWidget] = Cast[FGMapObjectWidget](ReturnValue_2)
        bSuccess: bool = Widget
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_3: bool = EqualEqual_ObjectObject(Widget.mActorRepresentation, actorRepresentation)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Widget.OnActorRepresentationUpdated()
        goto(ExecutionFlow.Pop())
        # Label 406
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L28')
    

    def CenterMapOnPlayer(self, normalizedWorldLocation: Vector2D):
        
        X = None
        Y = None
        BreakVector2D(normalizedWorldLocation, Ref[X], Ref[Y])
        ReturnValue: Vector2D = Vector2D(self.mMapSizeBox.WidthOverride, self.mMapSizeBox.HeightOverride)
        ReturnValue_0: Vector2D = Divide_Vector2DFloat(ReturnValue, -2)
        ReturnValue1: Vector2D = Divide_Vector2DFloat(ReturnValue, 2)
        
        X1 = None
        Y1 = None
        BreakVector2D(ReturnValue_0, Ref[X1], Ref[Y1])
        
        X2 = None
        Y2 = None
        BreakVector2D(ReturnValue1, Ref[X2], Ref[Y2])
        ReturnValue_1: float = Lerp(X2, X1, X)
        ReturnValue1_0: float = Lerp(Y2, Y1, Y)
        ReturnValue1_1: Vector2D = Vector2D(ReturnValue_1, ReturnValue1_0)
        self.mMapScrollContainer.SetRenderTranslation(ReturnValue1_1)
    

    def OnIconUnhover(self, MapObject: Ptr[Widget_MapObject]):
        ReturnValue: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(MapObject)
        ReturnValue.SetZOrder(MapObject.mZOrder)
    

    def OnIconHover(self, MapObject: Ptr[Widget_MapObject]):
        ReturnValue: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(MapObject)
        ReturnValue.SetZOrder(100)
    

    def AddObjectToMap(self, actorRepresentation: Ptr[FGActorRepresentation]):
        LocalRepresenation = actorRepresentation
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_MapObject] = Default__WidgetBlueprintLibrary.Create(self, Widget_MapObject, ReturnValue)
        Variable: int32 = 0
        Variable1: int32 = 9
        Variable2: int32 = 0
        Variable3: int32 = 0
        Variable4: int32 = 0
        Variable5: int32 = 2
        Variable6: int32 = 8
        Variable7: int32 = 0
        Variable8: int32 = 10
        Variable9: int32 = 15
        Variable10: int32 = 1
        Variable11: int32 = 6
        Variable12: int32 = 7
        Variable13: int32 = 0
        ReturnValue_1: uint8 = LocalRepresenation.GetRepresentationType()
        Variable_0: uint8 = ReturnValue_1
        
        switch = {
            0: Variable13,
            1: Variable12,
            2: Variable11,
            3: Variable10,
            4: Variable9,
            5: Variable8,
            6: Variable7,
            7: Variable6,
            8: Variable5,
            9: Variable4,
            10: Variable3,
            11: Variable2,
            12: Variable1,
            13: Variable
        }
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_0, "mZOrder", switch.get(Variable_0, None))
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_0, "mActorRepresentation", LocalRepresenation)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_0, "mMapWidget", self)
        LocalWidget = ReturnValue_0
        ReturnValue_2: Ptr[CanvasPanelSlot] = self.mMapObjectPanel.AddChildToCanvas(LocalWidget)
        Variable = 0
        Variable1 = 9
        Variable2 = 0
        Variable3 = 0
        Variable4 = 0
        Variable5 = 2
        Variable6 = 8
        Variable7 = 0
        Variable8 = 10
        Variable9 = 15
        Variable10 = 1
        Variable11 = 6
        Variable12 = 7
        Variable13 = 0
        ReturnValue_1 = LocalRepresenation.GetRepresentationType()
        Variable_0 = ReturnValue_1
        
        switch_0 = {
            0: Variable13,
            1: Variable12,
            2: Variable11,
            3: Variable10,
            4: Variable9,
            5: Variable8,
            6: Variable7,
            7: Variable6,
            8: Variable5,
            9: Variable4,
            10: Variable3,
            11: Variable2,
            12: Variable1,
            13: Variable
        }
        ReturnValue_2.SetZOrder(switch_0.get(Variable_0, None))
        OutputDelegate1.BindUFunction(self, OnIconHover)
        LocalWidget.OnHovered.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, OnIconUnhover)
        LocalWidget.OnUnhovered.AddUnique(OutputDelegate)
        WidgetMapObject = LocalWidget
    

    def RemoveObjectFromMap(self, ActorRepresentationToRemove: Ptr[FGActorRepresentation]):
        ExecutionFlow.Push("L546")
        Variable: int32 = 0
        # Label 28
        ReturnValue: int32 = self.mMapObjectPanel.GetChildrenCount()
        ReturnValue_0: int32 = ReturnValue - 1
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L472")
        ReturnValue_2: Ptr[Widget] = self.mMapObjectPanel.GetChildAt(Variable)
        Widget: Ptr[FGMapObjectWidget] = Cast[FGMapObjectWidget](ReturnValue_2)
        bSuccess: bool = Widget
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_3: bool = EqualEqual_ObjectObject(Widget.mActorRepresentation, ActorRepresentationToRemove)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        ReturnValue_2 = self.mMapObjectPanel.GetChildAt(Variable)
        ReturnValue_4: bool = self.mMapObjectPanel.RemoveChild(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 472
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L28')
    

    def ClearScrollMap(self):
        self.mIsMapMoving = False
    

    def ScrollMap(self, MouseOrigin: Vector2D, MapOrigin: Vector2D):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        LocationX = None
        LocationY = None
        ReturnValue_0: bool = Default__WidgetLayoutLibrary.GetMousePositionScaledByDPI(ReturnValue, Ref[LocationX], Ref[LocationY])
        ReturnValue_1: Vector2D = Vector2D(LocationX, LocationY)
        ReturnValue_2: Vector2D = Subtract_Vector2DVector2D(MouseOrigin, ReturnValue_1)
        ReturnValue_3: Vector2D = Divide_Vector2DVector2D(ReturnValue_2, self.mMapZoomContainer.RenderTransform.Scale)
        ReturnValue1: Vector2D = Subtract_Vector2DVector2D(MapOrigin, ReturnValue_3)
        self.mMapScrollContainer.SetRenderTranslation(ReturnValue1)
    

    def ZoomMap(self, ZoomValue: Vector2D):
        
        X = None
        Y = None
        BreakVector2D(ZoomValue, Ref[X], Ref[Y])
        ReturnValue: float = FClamp(Y, self.mMinZoom, self.mMaxZoom)
        ReturnValue1: float = FClamp(X, self.mMinZoom, self.mMaxZoom)
        ReturnValue_0: Vector2D = Vector2D(ReturnValue1, ReturnValue)
        self.mMapZoomContainer.SetRenderScale(ReturnValue_0)
        self.ZoomChanged.ProcessMulticastDelegate()
    

    def OnMouseWheel(self):
        
        ReturnValue: float = Default__KismetInputLibrary.PointerEvent_GetWheelDelta(Ref[MouseEvent])
        ReturnValue_0: bool = ReturnValue > 0
        Variable: bool = ReturnValue_0
        ReturnValue_1: Vector2D = Multiply_Vector2DFloat(self.mMapZoomContainer.RenderTransform.Scale, 0.8999999761581421)
        ReturnValue1: Vector2D = Multiply_Vector2DFloat(self.mMapZoomContainer.RenderTransform.Scale, 1.100000023841858)
        
        switch = {
            False: ReturnValue_1,
            True: ReturnValue1
        }
        self.ZoomMap(switch.get(Variable, None))
        ReturnValue_2: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_3: EventReply = ReturnValue_2
    

    def OnMouseLeave(self):
        ExecuteUbergraph_Widget_Map.K2Node_Event_MouseEvent = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Map(77)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Map(82)
    

    def OnFocusLost(self):
        ExecuteUbergraph_Widget_Map.K2Node_Event_InFocusEvent = InFocusEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Map(213)
    

    def Tick(self):
        ExecuteUbergraph_Widget_Map.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Map.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Map(232)
    

    def OnObjectAddedToMap(self):
        ExecuteUbergraph_Widget_Map.K2Node_Event_actorRepresentation2 = actorRepresentation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Map(237)
    

    def OnObjectRemovedFromMap(self):
        ExecuteUbergraph_Widget_Map.K2Node_Event_actorRepresentation1 = actorRepresentation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Map(311)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_Map(367)
    

    def OnObjectUpdatedOnMap(self):
        ExecuteUbergraph_Widget_Map.K2Node_Event_actorRepresentation = actorRepresentation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Map(418)
    

    def OnMapCentered(self):
        ExecuteUbergraph_Widget_Map.K2Node_Event_normalizedWorldLocation = normalizedWorldLocation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Map(474)
    

    def ExecuteUbergraph_Widget_Map(self):
        # Label 10
        self.mIsMapMoving = False
        # End
        # Label 26
        if not self.mIsMapMoving:
            goto('L497')
        self.ScrollMap(self.mMouseOrigin, self.mMapOrigin)
        # End
        # End
        self.Construct()
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.Image_0.GetDynamicMaterial()
        ReturnValue_0: Ptr[Texture2D] = self.GetFogOfWarTexture()
        ReturnValue.SetTextureParameterValue("Content", ReturnValue_0)
        # End
        self.ClearScrollMap()
        # End
        goto('L26')
        
        WidgetMapObject = None
        self.AddObjectToMap(actorRepresentation2, Ref[WidgetMapObject])
        self.OnObjectAddedToMapDispatch.ProcessMulticastDelegate(actorRepresentation2, WidgetMapObject)
        # End
        self.RemoveObjectFromMap(actorRepresentation1)
        self.OnObjectRemovedFromMapDispatch.ProcessMulticastDelegate(actorRepresentation1)
        # End
        self.mMapObjectPanel.ClearChildren()
        self.StopListeningForAllInputActions()
        goto('L10')
        self.UpdateObjectOnMap(actorRepresentation)
        self.OnObjectUpdatedOnMapDispatch.ProcessMulticastDelegate(actorRepresentation)
        # End
        self.CenterMapOnPlayer(normalizedWorldLocation)
    

    def OnObjectRemovedFromMapDispatch__DelegateSignature(self, ActorRespresentation: Ptr[FGActorRepresentation]):
        pass
    

    def OnObjectUpdatedOnMapDispatch__DelegateSignature(self, actorRepresentation: Ptr[FGActorRepresentation]):
        pass
    

    def OnObjectAddedToMapDispatch__DelegateSignature(self, actorRepresentation: Ptr[FGActorRepresentation], WidgetMapObject: Ptr[Widget_MapObject]):
        pass
    

    def ZoomChanged__DelegateSignature(self):
        pass
    
