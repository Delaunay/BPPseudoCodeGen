
from codegen.ue4_stub import *

from Script.Engine import GetInputAnalogStickState
from Script.UMG import GetViewportSize
from Script.Engine import SetScalarParameterValue
from Game.FactoryGame.Interface.UI.InGame.-Shared.RadialMenu.Widget_RadialMenuButton import ExecuteUbergraph_Widget_RadialMenuButton.K2Node_Event_MyGeometry
from Script.Engine import Texture
from Script.Engine import Lerp
from Script.Engine import FClamp
from Script.CoreUObject import Rotator
from Script.UMG import Default__WidgetLayoutLibrary
from Script.Engine import MaterialInstanceDynamic
from Script.SlateCore import Margin
from Script.Engine import MakeRotFromY
from Script.Engine import FindLookAtRotation
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import Divide_Vector2DFloat
from Script.UMG import SetRenderTranslation
from Script.UMG import ESlateVisibility
from Script.Engine import Sqrt
from Script.Engine import SetVectorParameterValue
from Script.Engine import Square
from Script.Engine import IsValid
from Script.Engine import InRange_FloatFloat
from Script.UMG import SetColorAndOpacity
from Game.FactoryGame.Interface.UI.InGame.-Shared.RadialMenu.Widget_RadialMenuButton import ExecuteUbergraph_Widget_RadialMenuButton.K2Node_Event_InDeltaTime
from Script.Engine import EqualEqual_NameName
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import BreakVector2D
from Script.FactoryGame import GetIsUsingGamepad
from Script.Engine import BreakRotator
from Game.FactoryGame.Interface.UI.InGame.-Shared.RadialMenu.Radial_Material_Inst import Radial_Material_Inst
from Script.Engine import Default__KismetMaterialLibrary
from Script.CoreUObject import Box2D
from Script.Engine import K2_GetScalarParameterValue
from Script.UMG import SetRenderAngle
from Script.CoreUObject import Vector
from Script.Engine import LinearColorLerp
from Script.Engine import CreateDynamicMaterialInstance
from Script.Engine import Conv_NameToText
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.CoreUObject import Vector2D
from Script.SlateCore import SlateBrush
from Script.SlateCore import SlateColor
from Game.FactoryGame.Interface.UI.InGame.-Shared.RadialMenu.Widget_RadialMenu import Widget_RadialMenu
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Script.SlateCore import SlateSound
from Script.UMG import SetStyle
from Game.FactoryGame.Interface.UI.InGame.-Shared.RadialMenu.Widget_RadialMenuButton import ExecuteUbergraph_Widget_RadialMenuButton
from Script.UMG import GetMousePositionScaledByDPI
from Script.CoreUObject import LinearColor

class Widget_RadialMenuButton(UserWidget):
    Radial_Material: Ptr[MaterialInstanceDynamic]
    startPoint: float
    Angle: float
    endPoint: float
    MinValue: float
    MaxValue: float
    Name: FName
    T: float
    IconMargin: float = 40
    mRadialMenu: Ptr[Widget_RadialMenu]
    ButtonInteger: int32
    InsideRadius: float
    OutsideRadius: float
    SingleButton: bool
    IconOffset: float = -290
    mInputTextureIcon: Ptr[Texture]
    mMonochromeIcon: bool
    
    def Hover Lerp(self, DeltaTime: float):
        ReturnValue: float = DeltaTime / 0.20000000298023224
        ReturnValue2: float = ReturnValue + self.T
        self.T = ReturnValue2
        ReturnValue_0: float = FClamp(self.T, 0, 1)
        
        TextWhite1 = None
        GraphicsWhite1 = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite1], Ref[GraphicsWhite1])
        ReturnValue1: LinearColor = LinearColorLerp(LinearColor(R = 1, G = 1, B = 1, A = 0), GraphicsWhite1, ReturnValue_0)
        self.Radial_Material.SetVectorParameterValue("Color", ReturnValue1)
        ReturnValue_0 = FClamp(self.T, 0, 1)
        ReturnValue2_0: float = Lerp(self.InsideRadius, 0.3149999976158142, ReturnValue_0)
        self.Radial_Material.SetScalarParameterValue("InsideRadius", ReturnValue2_0)
        ReturnValue_0 = FClamp(self.T, 0, 1)
        ReturnValue1_0: float = Lerp(self.OutsideRadius, 0.5, ReturnValue_0)
        self.Radial_Material.SetScalarParameterValue("OutsideRadius", ReturnValue1_0)
        if not self.SingleButton:
            goto('L1486')
        # Label 669
        ReturnValue_0 = FClamp(self.T, 0, 1)
        ReturnValue_1: float = self.IconOffset + -10
        ReturnValue_2: float = Lerp(self.IconOffset, ReturnValue_1, ReturnValue_0)
        ReturnValue_3: Vector2D = Vector2D(ReturnValue_2, 0)
        self.Icon.SetRenderTranslation(ReturnValue_3)
        ReturnValue_0 = FClamp(self.T, 0, 1)
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_4: LinearColor = LinearColorLerp(GraphicsWhite, Graphics, ReturnValue_0)
        SlateColor.SpecifiedColor = ReturnValue_4
        SlateColor.ColorUseRule = 0
        self.IconText.SetColorAndOpacity(SlateColor)
        if not self.mMonochromeIcon:
            goto('L1481')
        ReturnValue_0 = FClamp(self.T, 0, 1)
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_4 = LinearColorLerp(GraphicsWhite, Graphics, ReturnValue_0)
        self.IconImage.SetColorAndOpacity(ReturnValue_4)
        # Label 1481
        # End
        # Label 1486
        ReturnValue1_1: float = self.startPoint + 0.006000000052154064
        self.Radial_Material.SetScalarParameterValue("startPoint", ReturnValue1_1)
        ReturnValue_5: float = self.endPoint - 0.012000000104308128
        self.Radial_Material.SetScalarParameterValue("DegreeInPercent", ReturnValue_5)
        goto('L669')
    

    def Get Screen Position(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Vector2D = Default__WidgetLayoutLibrary.GetViewportSize(self)
        
        LocationX = None
        LocationY = None
        ReturnValue_1: bool = Default__WidgetLayoutLibrary.GetMousePositionScaledByDPI(ReturnValue, Ref[LocationX], Ref[LocationY])
        ReturnValue_2: Vector2D = Divide_Vector2DFloat(ReturnValue_0, 2)
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_2, Ref[X], Ref[Y])
        ReturnValue_3: float = X - LocationX
        ReturnValue1: float = Y - LocationY
        ReturnValue_4: float = Square(ReturnValue_3)
        ReturnValue1_0: float = Square(ReturnValue1)
        ReturnValue_5: float = ReturnValue_4 + ReturnValue1_0
        ReturnValue_6: float = Sqrt(ReturnValue_5)
        ReturnValue_7: float = ReturnValue_6
    

    def Set Angle(self):
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue2)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L1765')
        ReturnValue: bool = Controller.GetIsUsingGamepad()
        if not ReturnValue:
            goto('L869')
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        StickX = None
        StickY = None
        ReturnValue1.GetInputAnalogStickState(1, Ref[StickX], Ref[StickY])
        ReturnValue1_0: Vector = Vector(StickX, StickY, 0)
        
        ReturnValue_0: Rotator = MakeRotFromY(Ref[ReturnValue1_0])
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_0, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_1: float = Roll + 90
        ReturnValue_2: float = ReturnValue_1 / 360
        ReturnValue_3: bool = ReturnValue_2 <= 0
        if not ReturnValue_3:
            goto('L1444')
        ReturnValue1 = self.GetOwningPlayer()
        
        StickX = None
        StickY = None
        ReturnValue1.GetInputAnalogStickState(1, Ref[StickX], Ref[StickY])
        ReturnValue1_0 = Vector(StickX, StickY, 0)
        
        ReturnValue_0 = MakeRotFromY(Ref[ReturnValue1_0])
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_0, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_1 = Roll + 90
        ReturnValue_2 = ReturnValue_1 / 360
        ReturnValue1_1: float = 1 + ReturnValue_2
        self.Angle = ReturnValue1_1
        # End
        # Label 869
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        
        LocationX = None
        LocationY = None
        ReturnValue_5: bool = Default__WidgetLayoutLibrary.GetMousePositionScaledByDPI(ReturnValue_4, Ref[LocationX], Ref[LocationY])
        ReturnValue_6: Vector = Vector(LocationX, LocationY, 0)
        ReturnValue_7: Vector2D = Default__WidgetLayoutLibrary.GetViewportSize(self)
        ReturnValue_8: Vector2D = Divide_Vector2DFloat(ReturnValue_7, 2)
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_8, Ref[X], Ref[Y])
        ReturnValue2_0: Vector = Vector(X, Y, 0)
        
        ReturnValue_9: Rotator = FindLookAtRotation(Ref[ReturnValue2_0], Ref[ReturnValue_6])
        
        Roll1 = None
        Pitch1 = None
        Yaw1 = None
        BreakRotator(ReturnValue_9, Ref[Roll1], Ref[Pitch1], Ref[Yaw1])
        ReturnValue2_1: float = Yaw1 + 180
        ReturnValue1_2: float = ReturnValue2_1 / 360
        ReturnValue_10: float = 1 - ReturnValue1_2
        self.Angle = ReturnValue_10
        # End
        # Label 1444
        ReturnValue1 = self.GetOwningPlayer()
        
        StickX = None
        StickY = None
        ReturnValue1.GetInputAnalogStickState(1, Ref[StickX], Ref[StickY])
        ReturnValue1_0 = Vector(StickX, StickY, 0)
        
        ReturnValue_0 = MakeRotFromY(Ref[ReturnValue1_0])
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_0, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_1 = Roll + 90
        ReturnValue_2 = ReturnValue_1 / 360
        self.Angle = ReturnValue_2
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_RadialMenuButton(1315)
    

    def Create Style(self):
        self.ExecuteUbergraph_Widget_RadialMenuButton(2196)
    

    def Set Icon Position(self):
        self.ExecuteUbergraph_Widget_RadialMenuButton(2229)
    

    def Tick(self):
        ExecuteUbergraph_Widget_RadialMenuButton.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_RadialMenuButton.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_RadialMenuButton(3550)
    

    def ExecuteUbergraph_Widget_RadialMenuButton(self):
        # Label 10
        ReturnValue: Ptr[MaterialInstanceDynamic] = Default__KismetMaterialLibrary.CreateDynamicMaterialInstance(self, Radial_Material_Inst, "None")
        self.Radial_Material = ReturnValue
        self.Radial_Material.SetScalarParameterValue("startPoint", self.startPoint)
        self.Radial_Material.SetScalarParameterValue("DegreeInPercent", self.endPoint)
        SlateColor.SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        SlateColor.ColorUseRule = 0
        SlateBrush.ImageSize = Vector2D(X = 750, Y = 750)
        SlateBrush.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush.TintColor = SlateColor
        SlateBrush.ResourceObject = self.Radial_Material
        ButtonStyle.Normal = SlateBrush
        ButtonStyle.Hovered = SlateBrush
        ButtonStyle.Pressed = SlateBrush
        ButtonStyle.Disabled = SlateBrush(ImageSize = Vector2D(X = 0, Y = 0), Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0), TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0), ResourceObject = None, ResourceName = "None", UVRegion = Box2D(Min = Vector2D(X = 0, Y = 0), Max = Vector2D(X = 0, Y = 0), bIsValid = 0), DrawAs = 0, Tiling = 0, Mirroring = 0, ImageType = 0, bIsDynamicallyLoaded = False, bHasUObject = False)
        ButtonStyle.NormalPadding = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        ButtonStyle.PressedPadding = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        ButtonStyle.PressedSlateSound = SlateSound(ResourceObject = None)
        ButtonStyle.HoveredSlateSound = SlateSound(ResourceObject = None)
        
        ButtonStyle = None
        self.Button_0.SetStyle(Ref[ButtonStyle])
        ReturnValue1: Vector2D = Vector2D(self.IconOffset, 0)
        self.Icon.SetRenderTranslation(ReturnValue1)
        # End
        # Label 1148
        self.Radial_Material.SetVectorParameterValue("Color", LinearColor(R = 1, G = 1, B = 1, A = 0))
        ReturnValue_0: Vector2D = Vector2D(self.IconOffset, 0)
        self.Icon.SetRenderTranslation(ReturnValue_0)
        # End
        self.Create Style()
        ReturnValue_1: float = self.Radial_Material.K2_GetScalarParameterValue("InsideRadius")
        self.InsideRadius = ReturnValue_1
        ReturnValue1_0: float = self.Radial_Material.K2_GetScalarParameterValue("OutsideRadius")
        self.OutsideRadius = ReturnValue1_0
        self.Set Icon Position()
        Variable: uint8 = 0
        Variable1: uint8 = 1
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValid(self.mInputTextureIcon)
        Variable_0: bool = ReturnValue1_1
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.IconImage.SetVisibility(switch.get(Variable_0, None))
        SlateBrush1.ImageSize = self.IconImage.Brush.ImageSize
        SlateBrush1.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush1.TintColor = self.IconImage.Brush.TintColor
        SlateBrush1.ResourceObject = self.mInputTextureIcon
        SlateBrush1.DrawAs = self.IconImage.Brush.DrawAs
        SlateBrush1.Tiling = self.IconImage.Brush.Tiling
        SlateBrush1.Mirroring = self.IconImage.Brush.Mirroring
        
        SlateBrush1 = None
        self.IconImage.SetBrush(Ref[SlateBrush1])
        # End
        goto('L10')
        # Label 2201
        self.T = 0
        goto('L1148')
        ReturnValue_2: float = self.endPoint / 2
        ReturnValue_3: float = ReturnValue_2 + self.startPoint
        ReturnValue_4: float = ReturnValue_3 * 360
        ReturnValue_5: float = 0 - ReturnValue_4
        self.IconContainer.SetRenderAngle(ReturnValue_5)
        ReturnValue_2 = self.endPoint / 2
        ReturnValue_3 = ReturnValue_2 + self.startPoint
        ReturnValue_4 = ReturnValue_3 * 360
        self.Icon.SetRenderAngle(ReturnValue_4)
        ReturnValue_6: FText = Default__KismetTextLibrary.Conv_NameToText(self.Name)
        self.IconText.SetText(ReturnValue_6)
        # End
        # Label 2722
        ReturnValue_7: bool = Default__KismetSystemLibrary.IsValid(self.mRadialMenu)
        if not ReturnValue_7:
            goto('L3555')
        ReturnValue_8: bool = InRange_FloatFloat(self.mRadialMenu.Angle, self.MinValue, self.MaxValue, True, True)
        ReturnValue_9: bool = self.mRadialMenu.OutsideDeadSpace and ReturnValue_8
        if not ReturnValue_9:
            goto('L3034')
        self.Hover Lerp(InDeltaTime)
        ReturnValue_10: bool = EqualEqual_NameName(self.Name, self.mRadialMenu.ActiveName)
        if not ReturnValue_10:
            goto('L3447')
        # End
        
        TextWhite = None
        GraphicsWhite = None
        # Label 3034
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        self.IconText.SetColorAndOpacity(TextWhite)
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        self.IconImage.SetColorAndOpacity(GraphicsWhite)
        self.Radial_Material.SetScalarParameterValue("startPoint", self.startPoint)
        self.Radial_Material.SetScalarParameterValue("DegreeInPercent", self.endPoint)
        self.Radial_Material.SetScalarParameterValue("InsideRadius", self.InsideRadius)
        self.Radial_Material.SetScalarParameterValue("OutsideRadius", self.OutsideRadius)
        goto('L2201')
        # Label 3447
        self.mRadialMenu.ActiveName = self.Name
        self.mRadialMenu.SelectedInt = self.ButtonInteger
        # End
        goto('L2722')
    
