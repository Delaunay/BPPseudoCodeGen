
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ButtonSpotLight import ExecuteUbergraph_Widget_ButtonSpotLight.K2Node_Event_MouseEvent
from Script.UMG import CanvasPanelSlot
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import SlotAsCanvasSlot
from Script.UMG import Unhandled
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ButtonSpotLight import ExecuteUbergraph_Widget_ButtonSpotLight.K2Node_Event_MyGeometry
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import SetHeightOverride
from Script.UMG import Default__SlateBlueprintLibrary
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ButtonSpotLight import ExecuteUbergraph_Widget_ButtonSpotLight.K2Node_Event_MouseEvent1
from Script.UMG import SetWidthOverride
from Script.SlateCore import Geometry
from Script.UMG import UserWidget
from Script.Engine import Subtract_Vector2DVector2D
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ButtonSpotLight import ExecuteUbergraph_Widget_ButtonSpotLight
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ButtonSpotLight import ExecuteUbergraph_Widget_ButtonSpotLight.K2Node_Event_IsDesignTime
from Script.UMG import GetMousePositionOnViewport
from Script.CoreUObject import Vector2D
from Script.UMG import SetPosition
from Script.UMG import LocalToViewport
from Script.UMG import GetCachedGeometry
from Script.UMG import EventReply

class Widget_ButtonSpotLight(UserWidget):
    mShineSize: float = 150
    
    def UpdateMousePosition(self):
        ReturnValue: Vector2D = Default__WidgetLayoutLibrary.GetMousePositionOnViewport(self)
        MousePosition = ReturnValue
        ReturnValue_0: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self.mLightContainer)
        ReturnValue_1: Const[Geometry] = self.GetCachedGeometry()
        
        PixelPosition = None
        ViewportPosition = None
        Default__SlateBlueprintLibrary.LocalToViewport(self, Vector2D(X = 0, Y = 0), Ref[ReturnValue_1], Ref[PixelPosition], Ref[ViewportPosition])
        ReturnValue_2: Vector2D = Subtract_Vector2DVector2D(MousePosition, ViewportPosition)
        ReturnValue_0.SetPosition(ReturnValue_2)
    

    def OnMouseMove(self):
        self.UpdateMousePosition()
        ReturnValue: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_0: EventReply = ReturnValue
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_ButtonSpotLight.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ButtonSpotLight(53)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ButtonSpotLight(140)
    

    def OnMouseLeave(self):
        ExecuteUbergraph_Widget_ButtonSpotLight.K2Node_Event_MouseEvent1 = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ButtonSpotLight(145)
    

    def OnMouseEnter(self):
        ExecuteUbergraph_Widget_ButtonSpotLight.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ButtonSpotLight.K2Node_Event_MouseEvent = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ButtonSpotLight(188)
    

    def ExecuteUbergraph_Widget_ButtonSpotLight(self):
        # Label 10
        self.mLightContainer.SetVisibility(3)
        # End
        self.mLightContainer.SetWidthOverride(self.mShineSize)
        self.mLightContainer.SetHeightOverride(self.mShineSize)
        # End
        # End
        self.mLightContainer.SetVisibility(1)
        # End
        goto('L10')
    
