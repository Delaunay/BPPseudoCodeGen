
from codegen.ue4_stub import *

from Script.FactoryGame import ERepresentationType
from Script.Engine import SetScalarParameterValue
from Script.UMG import GetParent
from Script.UMG import CanvasPanelSlot
from Script.FactoryGame import GetRepresentationType
from Script.Engine import Lerp
from Script.FactoryGame import GetRealActor
from Script.Engine import EqualEqual_ByteByte
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Parent import Widget_ActorDetails_Parent
from Script.Engine import SetObjectPropertyByName
from Script.FactoryGame import FGMinimapCaptureActor
from Script.Slate import Anchors
from Script.FactoryGame import FGMapObjectWidget
from Script.FactoryGame import Default__FGMapFunctionLibrary
from Script.FactoryGame import GetMapDistance
from Script.Engine import MaterialInstanceDynamic
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import SlotAsCanvasSlot
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.Engine import Not_PreBool
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_TrainStation import Widget_ActorDetails_TrainStation
from Script.CoreUObject import Rotator
from Script.UMG import SetAutoSize
from Script.SlateCore import Margin
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_DockingStation import Widget_ActorDetails_DockingStation
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.Engine import LatentActionInfo
from Script.UMG import SetRenderScale
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapObject import ExecuteUbergraph_Widget_MapObject.K2Node_Event_MyGeometry
from Script.UMG import ESlateVisibility
from Script.UMG import GetLocalSize
from Script.UMG import StopAnimation
from Script.FactoryGame import GetMinimapCaptureActor
from Script.FactoryGame import Default__FGActorRepresentationManager
from Script.FactoryGame import GetDistanceValueFromCompassViewDistance
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapObject import ExecuteUbergraph_Widget_MapObject
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import SetBrushSize
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Hub import Widget_ActorDetails_Hub
from Script.Engine import BreakVector2D
from Script.UMG import Default__SlateBlueprintLibrary
from Script.UMG import GetAbsoluteSize
from Script.FactoryGame import IsActorStatic
from Script.Engine import BreakRotator
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_SpaceElevator import Widget_ActorDetails_SpaceElevator
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_RadarTower import Widget_ActorDetails_RadarTower
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapObject import ExecuteUbergraph_Widget_MapObject.K2Node_Event_visible
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapObject import ExecuteUbergraph_Widget_MapObject.K2Node_CustomEvent_Time
from Script.UMG import PanelWidget
from Script.FactoryGame import FGActorRepresentationManager
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapObject import ExecuteUbergraph_Widget_MapObject.K2Node_Event_InDeltaTime
from Script.UMG import WidgetAnimation
from Script.Engine import K2_GetActorRotation
from Script.Engine import NotEqual_ByteByte
from Script.SlateCore import Geometry
from Script.Engine import RetriggerableDelay
from Script.Engine import Divide_Vector2DVector2D
from Script.Engine import Multiply_Vector2DFloat
from Script.Engine import Actor
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapObject import ExecuteUbergraph_Widget_MapObject.K2Node_Event_normalizedLocation
from Script.UMG import Create
from Script.UMG import IsAnimationPlaying
from Script.CoreUObject import Vector2D
from Script.UMG import SetPosition
from Script.UMG import GetDynamicMaterial
from Script.UMG import GetCachedGeometry
from Script.UMG import SetLayout
from Script.UMG import SetZOrder

class Widget_MapObject(FGMapObjectWidget):
    ani_ViewDistancePulse: Ptr[WidgetAnimation]
    ani_Highlight: Ptr[WidgetAnimation]
    OnHovered: FMulticastScriptDelegate
    OnUnhovered: FMulticastScriptDelegate
    mZOrder: int32
    mPositionOnCanvas: Vector2D
    NewVar_0: Vector2D
    
    def HideViewDistanceIndicator(self):
        self.mViewDistanceIndicator.SetVisibility(1)
        self.StopAnimation(self.ani_ViewDistancePulse)
    

    def ShowViewDistanceIndicator(self, viewDistance: uint8):
        self.mViewDistancePulse.SetVisibility(3)
        
        X1 = None
        Y1 = None
        BreakVector2D(self.RenderTransform.Scale, Ref[X1], Ref[Y1])
        ReturnValue1: float = 1 / X1
        ReturnValue: Vector2D = Vector2D(ReturnValue1, ReturnValue1)
        self.mViewDistanceIndicator.SetRenderScale(ReturnValue)
        self.mViewDistancePulse.SetRenderScale(ReturnValue)
        ReturnValue2: bool = EqualEqual_ByteByte(viewDistance, 4)
        if not ReturnValue2:
            goto('L2159')
        # Label 299
        self.mViewDistanceIndicator.SetVisibility(1)
        # Label 337
        Variable: float = 750000
        ReturnValue1_0: bool = EqualEqual_ByteByte(viewDistance, 4)
        Variable_0: bool = ReturnValue1_0
        ReturnValue2_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue2_1: float = ReturnValue2_0.GetDistanceValueFromCompassViewDistance(viewDistance)
        ReturnValue_0: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_1: Ptr[FGMinimapCaptureActor] = Default__FGMapFunctionLibrary.GetMinimapCaptureActor(ReturnValue_0)
        ReturnValue1_1: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_2: Const[Geometry] = ReturnValue1_1.GetCachedGeometry()
        
        ReturnValue_3: Vector2D = Default__SlateBlueprintLibrary.GetLocalSize(Ref[ReturnValue_2])
        
        X4 = None
        Y4 = None
        BreakVector2D(ReturnValue_3, Ref[X4], Ref[Y4])
        
        switch = {
            False: ReturnValue2_1,
            True: Variable
        }
        ReturnValue_4: float = Default__FGMapFunctionLibrary.GetMapDistance(ReturnValue_1, switch.get(Variable_0, None), X4)
        ReturnValue3: float = ReturnValue_4 * 2
        ReturnValue1_2: Vector2D = Vector2D(ReturnValue3, ReturnValue3)
        self.mViewDistanceIndicator.SetBrushSize(ReturnValue1_2)
        self.mViewDistancePulse.SetBrushSize(ReturnValue1_2)
        ReturnValue_5: Ptr[MaterialInstanceDynamic] = self.mViewDistancePulse.GetDynamicMaterial()
        ReturnValue1_3: Ptr[MaterialInstanceDynamic] = self.mViewDistanceIndicator.GetDynamicMaterial()
        
        X2 = None
        Y2 = None
        BreakVector2D(self.RenderTransform.Scale, Ref[X2], Ref[Y2])
        ReturnValue2_2: float = 1 / X2
        
        X3 = None
        Y3 = None
        BreakVector2D(self.mViewDistanceIndicator.Brush.ImageSize, Ref[X3], Ref[Y3])
        ReturnValue2_3: float = X3 * ReturnValue2_2
        ReturnValue1_3.SetScalarParameterValue("MaxSize", ReturnValue2_3)
        ReturnValue_5.SetScalarParameterValue("MaxSize", ReturnValue2_3)
        ReturnValue_6: bool = EqualEqual_ByteByte(viewDistance, 4)
        Variable1: float = 750000
        Variable1_0: bool = ReturnValue_6
        ReturnValue_7: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue1_4: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_8: float = ReturnValue_7.GetDistanceValueFromCompassViewDistance(1)
        ReturnValue1_5: float = ReturnValue1_4.GetDistanceValueFromCompassViewDistance(viewDistance)
        
        X = None
        Y = None
        BreakVector2D(self.RenderTransform.Scale, Ref[X], Ref[Y])
        ReturnValue_9: float = X * 0.05000000074505806
        
        switch_0 = {
            False: ReturnValue1_5,
            True: Variable1
        }
        ReturnValue_10: float = ReturnValue_8 / switch_0.get(Variable1_0, None)
        ReturnValue1_6: float = ReturnValue_9 * ReturnValue_10
        ReturnValue1_3.SetScalarParameterValue("StrokeWidth", ReturnValue1_6)
        ReturnValue_5.SetScalarParameterValue("StrokeWidth", ReturnValue1_6)
        ReturnValue_11: bool = self.IsAnimationPlaying(self.ani_ViewDistancePulse)
        ReturnValue_12: bool = Not_PreBool(ReturnValue_11)
        if not ReturnValue_12:
            goto('L2202')
        ReturnValue_13: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ani_ViewDistancePulse, 0, 0, 0, 1)
        # End
        # Label 2159
        self.mViewDistanceIndicator.SetVisibility(3)
        goto('L337')
    

    def UnhighlightOnMap(self):
        self.mMapHighlightOverlay.SetVisibility(1)
        ReturnValue: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self)
        ReturnValue.SetZOrder(self.mZOrder)
    

    def HighlightOnMap(self):
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ani_Highlight, 0, 1, 0, 1)
        ReturnValue_0: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self)
        ReturnValue_0.SetZOrder(1000)
    

    def mShowActorDetails(self):
        ReturnValue: uint8 = self.mActorRepresentation.GetRepresentationType()
        CmpSuccess: bool = NotEqual_ByteByte(ReturnValue, 3)
        if not CmpSuccess:
            goto('L280')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 6)
        if not CmpSuccess:
            goto('L652')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 8)
        if not CmpSuccess:
            goto('L676')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 11)
        if not CmpSuccess:
            goto('L700')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 13)
        if not CmpSuccess:
            goto('L724')
        # End
        # Label 280
        ActorDetailsWidget = Widget_ActorDetails_Hub
        # Label 299
        ReturnValue_0: Ptr[Actor] = self.mActorRepresentation.GetRealActor()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L748')
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_3: Ptr[Widget_ActorDetails_Parent] = Default__WidgetBlueprintLibrary.Create(self, ActorDetailsWidget, ReturnValue_2)
        ReturnValue_0 = self.mActorRepresentation.GetRealActor()
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_3, "mActor", ReturnValue_0)
        ReturnValue_4: Ptr[PanelSlot] = self.mActorDetailsContainer.AddChild(ReturnValue_3)
        # End
        # Label 652
        ActorDetailsWidget = Widget_ActorDetails_RadarTower
        goto('L299')
        # Label 676
        ActorDetailsWidget = Widget_ActorDetails_SpaceElevator
        goto('L299')
        # Label 700
        ActorDetailsWidget = Widget_ActorDetails_TrainStation
        goto('L299')
        # Label 724
        ActorDetailsWidget = Widget_ActorDetails_DockingStation
        goto('L299')
    

    def Tick(self):
        ExecuteUbergraph_Widget_MapObject.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_MapObject.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapObject(101)
    

    def OnObjectFiltered(self):
        ExecuteUbergraph_Widget_MapObject.K2Node_Event_visible = visible #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapObject(397)
    

    def OnObjectMoved(self):
        ExecuteUbergraph_Widget_MapObject.K2Node_Event_normalizedLocation = normalizedLocation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapObject(524)
    

    def OnActorRepresentationUpdated(self):
        self.ExecuteUbergraph_Widget_MapObject(1382)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_MapObject(2027)
    

    def DestructionTimer(self, Time: float):
        ExecuteUbergraph_Widget_MapObject.K2Node_CustomEvent_Time = Time #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapObject(2032)
    

    def BndEvt__Widget_MapCompass_Icon_K2Node_ComponentBoundEvent_0_OnUnhovered__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_MapObject(2113)
    

    def BndEvt__Widget_MapCompass_Icon_K2Node_ComponentBoundEvent_1_OnHovered__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_MapObject(2170)
    

    def ShowActorDetailsEvent(self):
        self.ExecuteUbergraph_Widget_MapObject(2205)
    

    def ExecuteUbergraph_Widget_MapObject(self):
        goto(ComputedJump("EntryPoint"))
        self.RemoveFromParent()
        goto(ExecutionFlow.Pop())
        ReturnValue: bool = self.Widget_MapCompass_Icon.IsHovered()
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        self.mShowActorDetails()
        goto(ExecutionFlow.Pop())
        ReturnValue1: Ptr[PanelWidget] = self.GetParent()
        ReturnValue1_0: Const[Geometry] = ReturnValue1.GetCachedGeometry()
        
        ReturnValue1_1: Vector2D = Default__SlateBlueprintLibrary.GetLocalSize(Ref[ReturnValue1_0])
        
        ReturnValue_0: Vector2D = Default__SlateBlueprintLibrary.GetAbsoluteSize(Ref[ReturnValue1_0])
        ReturnValue_1: Vector2D = Divide_Vector2DVector2D(ReturnValue1_1, ReturnValue_0)
        ReturnValue_2: Vector2D = Multiply_Vector2DFloat(ReturnValue_1, 0.800000011920929)
        self.SetRenderScale(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        Variable: uint8 = 0
        Variable1: uint8 = 2
        Variable_0: bool = visible
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.SetVisibility(switch.get(Variable_0, None))
        goto(ExecutionFlow.Pop())
        
        X = None
        Y = None
        BreakVector2D(normalizedLocation, Ref[X], Ref[Y])
        ReturnValue_3: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_4: Const[Geometry] = ReturnValue_3.GetCachedGeometry()
        
        ReturnValue_5: Vector2D = Default__SlateBlueprintLibrary.GetLocalSize(Ref[ReturnValue_4])
        
        X1 = None
        Y1 = None
        BreakVector2D(ReturnValue_5, Ref[X1], Ref[Y1])
        ReturnValue_6: float = Lerp(0, Y1, Y)
        ReturnValue1_2: float = Lerp(0, X1, X)
        ReturnValue_7: Vector2D = Vector2D(ReturnValue1_2, ReturnValue_6)
        self.mPositionOnCanvas = ReturnValue_7
        ReturnValue_8: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self)
        ReturnValue_8.SetPosition(self.mPositionOnCanvas)
        ReturnValue_9: Ptr[Actor] = self.mActorRepresentation.GetRealActor()
        ReturnValue_10: bool = self.mActorRepresentation.IsActorStatic()
        ReturnValue_11: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_9)
        ReturnValue_12: bool = Not_PreBool(ReturnValue_10)
        ReturnValue_13: bool = ReturnValue_12 and ReturnValue_11
        if not ReturnValue_13:
           goto(ExecutionFlow.Pop())
        ReturnValue1_3: Ptr[Actor] = self.mActorRepresentation.GetRealActor()
        ReturnValue_14: Rotator = ReturnValue1_3.K2_GetActorRotation()
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_14, Ref[Roll], Ref[Pitch], Ref[Yaw])
        self.Widget_MapCompass_Icon.SetRotation(Yaw)
        goto(ExecutionFlow.Pop())
        self.Widget_MapCompass_Icon.UpdateActor(self.mActorRepresentation, False)
        goto(ExecutionFlow.Pop())
        # Label 1429
        ReturnValue1_4: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self)
        ReturnValue1_4.SetAutoSize(True)
        ReturnValue1_4 = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self)
        AnchorData.Offsets = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        AnchorData.Anchors = Anchors(Minimum = Vector2D(X = 0, Y = 0), Maximum = Vector2D(X = 0, Y = 0))
        AnchorData.Alignment = Vector2D(X = 0.5, Y = 0.5)
        
        AnchorData = None
        ReturnValue1_4.SetLayout(Ref[AnchorData])
        Variable2: uint8 = 0
        Variable3: uint8 = 2
        Variable1_0: bool = self.mFilteredVisibility
        
        switch_0 = {
            False: Variable3,
            True: Variable2
        }
        self.SetVisibility(switch_0.get(Variable1_0, None))
        ReturnValue_15: uint8 = self.mActorRepresentation.GetRepresentationType()
        ReturnValue_16: bool = EqualEqual_ByteByte(ReturnValue_15, 0)
        if not ReturnValue_16:
           goto(ExecutionFlow.Pop())
        self.DestructionTimer(10)
        goto(ExecutionFlow.Pop())
        goto('L1429')
        Default__KismetSystemLibrary.RetriggerableDelay(self, Time, LatentActionInfo(Linkage = 15, UUID = -1604952896, ExecutionFunction = "ExecuteUbergraph_Widget_MapObject", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.OnUnhovered.ProcessMulticastDelegate(self)
        self.mActorDetailsContainer.ClearChildren()
        goto(ExecutionFlow.Pop())
        self.OnHovered.ProcessMulticastDelegate(self)
        self.ShowActorDetailsEvent()
        goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.RetriggerableDelay(self, 0.5, LatentActionInfo(Linkage = 30, UUID = -1292680761, ExecutionFunction = "ExecuteUbergraph_Widget_MapObject", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
    

    def OnUnhovered__DelegateSignature(self, MapObject: Ptr[Widget_MapObject]):
        pass
    

    def OnHovered__DelegateSignature(self, MapObject: Ptr[Widget_MapObject]):
        pass
    
