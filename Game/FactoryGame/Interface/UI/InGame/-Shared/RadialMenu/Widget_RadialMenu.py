
from codegen.ue4_stub import *

from Script.Engine import GetInputAnalogStickState
from Script.UMG import GetViewportSize
from Script.Engine import Conv_TextToString
from Script.Engine import Texture
from Script.Engine import FClamp
from Script.Engine import SetObjectPropertyByName
from Script.UMG import GetChildrenCount
from Script.CoreUObject import Rotator
from Script.UMG import Default__WidgetLayoutLibrary
from Script.Engine import Conv_IntToFloat
from Script.UMG import PanelSlot
from Script.Engine import MakeRotFromY
from Game.FactoryGame.Interface.UI.InGame.-Shared.RadialMenu.Widget_RadialMenu import ExecuteUbergraph_Widget_RadialMenu.K2Node_Event_InDeltaTime
from Script.UMG import AddChild
from Script.Engine import FTrunc
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import PlayAnimation
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import SetFloatPropertyByName
from Game.FactoryGame.Interface.UI.InGame.-Shared.RadialMenu.Widget_RadialMenu import ExecuteUbergraph_Widget_RadialMenu.K2Node_Event_MyGeometry
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Divide_IntInt
from Script.FactoryGame import GetIsUsingGamepad
from Script.Engine import BreakVector2D
from Script.Engine import BooleanOR
from Script.Engine import SetBoolPropertyByName
from Script.Engine import BreakRotator
from Game.FactoryGame.Interface.UI.InGame.-Shared.RadialMenu.Widget_RadialMenuButton import Widget_RadialMenuButton
from Script.UMG import SetRenderAngle
from Script.CoreUObject import Vector
from Script.Engine import SetMouseLocation
from Script.Engine import SetIntPropertyByName
from Script.UMG import WidgetAnimation
from Script.Engine import GetInputMouseDelta
from Script.UMG import UserWidget
from Script.Engine import SetNamePropertyByName
from Script.Engine import Multiply_Vector2DFloat
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.InGame.-Shared.RadialMenu.Widget_RadialMenu import ExecuteUbergraph_Widget_RadialMenu
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Script.CoreUObject import Vector2D
from Script.Engine import Abs
from Script.UMG import SetContentColorAndOpacity
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Script.Engine import Normal2D
from Script.UMG import SetRenderOpacity
from Script.Engine import Add_Vector2DVector2D
from Script.Engine import Conv_NameToText
from Script.CoreUObject import LinearColor

class Widget_RadialMenu(UserWidget):
    SpawnAnimation: Ptr[WidgetAnimation]
    Buttons: List[FName]
    Name: FName
    ButtonSpacing: float
    Angle: float
    ActiveName: FName
    OutsideDeadSpace: bool
    SelectedInt: int32
    AngleOffset: float = 0.25
    mClampedMousePos: Vector2D
    mSensitivity: float = 0.10000000149011612
    MouseDelta: Vector2D
    mIconTextures: List[Ptr[Texture]]
    mDescText: FText
    mMonochromeIcons: bool
    
    def Update Button Angles(self, MenuAngle: float):
        Variable: int32 = 0
        # Label 23
        ReturnValue: int32 = self.mContent.GetChildrenCount()
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L199')
        ReturnValue_1: int32 = Variable + 1
        Variable = ReturnValue_1
        goto('L23')
    

    def Set Angle(self):
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue2)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L2714')
        ReturnValue: bool = Controller.GetIsUsingGamepad()
        if not ReturnValue:
            goto('L1306')
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        StickX = None
        StickY = None
        ReturnValue1.GetInputAnalogStickState(1, Ref[StickX], Ref[StickY])
        ReturnValue_0: bool = StickY <= 0
        ReturnValue_1: bool = StickY > 0
        ReturnValue1_0: bool = StickX <= 0
        ReturnValue1_1: bool = StickX > 0
        ReturnValue_2: bool = BooleanOR(ReturnValue1_1, ReturnValue1_0)
        ReturnValue1_2: bool = BooleanOR(ReturnValue_2, ReturnValue_1)
        ReturnValue2_0: bool = BooleanOR(ReturnValue1_2, ReturnValue_0)
        self.OutsideDeadSpace = ReturnValue2_0
        ReturnValue1 = self.GetOwningPlayer()
        
        StickX = None
        StickY = None
        ReturnValue1.GetInputAnalogStickState(1, Ref[StickX], Ref[StickY])
        ReturnValue1_3: Vector = Vector(StickX, StickY, 0)
        
        ReturnValue1_4: Rotator = MakeRotFromY(Ref[ReturnValue1_3])
        
        Roll1 = None
        Pitch1 = None
        Yaw1 = None
        BreakRotator(ReturnValue1_4, Ref[Roll1], Ref[Pitch1], Ref[Yaw1])
        ReturnValue_3: float = Roll1 + 90
        ReturnValue1_5: float = ReturnValue_3 / 360
        ReturnValue2_1: float = ReturnValue1_5 - self.AngleOffset
        ReturnValue2_2: bool = ReturnValue2_1 <= 0
        if not ReturnValue2_2:
            goto('L2347')
        ReturnValue1 = self.GetOwningPlayer()
        
        StickX = None
        StickY = None
        ReturnValue1.GetInputAnalogStickState(1, Ref[StickX], Ref[StickY])
        ReturnValue1_3 = Vector(StickX, StickY, 0)
        
        ReturnValue1_4 = MakeRotFromY(Ref[ReturnValue1_3])
        
        Roll1 = None
        Pitch1 = None
        Yaw1 = None
        BreakRotator(ReturnValue1_4, Ref[Roll1], Ref[Pitch1], Ref[Yaw1])
        ReturnValue_3 = Roll1 + 90
        ReturnValue1_5 = ReturnValue_3 / 360
        ReturnValue2_1 = ReturnValue1_5 - self.AngleOffset
        ReturnValue1_6: float = 1 + ReturnValue2_1
        self.Angle = ReturnValue1_6
        # End
        # Label 1306
        self.OutsideDeadSpace = True
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        
        DeltaX = None
        DeltaY = None
        ReturnValue_4.GetInputMouseDelta(Ref[DeltaX], Ref[DeltaY])
        ReturnValue_5: Vector2D = Vector2D(DeltaX, DeltaY)
        ReturnValue_6: Vector2D = Multiply_Vector2DFloat(ReturnValue_5, self.mSensitivity)
        ReturnValue_7: Vector2D = Add_Vector2DVector2D(ReturnValue_6, self.mClampedMousePos)
        
        X1 = None
        Y1 = None
        BreakVector2D(ReturnValue_7, Ref[X1], Ref[Y1])
        ReturnValue1_7: Vector2D = Normal2D(ReturnValue_7)
        
        X2 = None
        Y2 = None
        BreakVector2D(ReturnValue1_7, Ref[X2], Ref[Y2])
        ReturnValue_8: float = Abs(Y2)
        ReturnValue_9: float = ReturnValue_8 * -1
        ReturnValue_10: float = FClamp(Y1, ReturnValue_9, ReturnValue_8)
        ReturnValue1_8: float = Abs(X2)
        ReturnValue1_9: float = ReturnValue1_8 * -1
        ReturnValue1_10: float = FClamp(X1, ReturnValue1_9, ReturnValue1_8)
        ReturnValue1_11: Vector2D = Vector2D(ReturnValue1_10, ReturnValue_10)
        self.mClampedMousePos = ReturnValue1_11
        ReturnValue_11: Vector2D = Normal2D(self.mClampedMousePos)
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_11, Ref[X], Ref[Y])
        ReturnValue_12: Vector = Vector(X, Y, 0)
        
        ReturnValue_13: Rotator = MakeRotFromY(Ref[ReturnValue_12])
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_13, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_14: float = Roll / 360
        ReturnValue_15: float = 1 - ReturnValue_14
        ReturnValue1_12: float = ReturnValue_15 - 0.5
        self.Angle = ReturnValue1_12
        # End
        # Label 2347
        ReturnValue1 = self.GetOwningPlayer()
        
        StickX = None
        StickY = None
        ReturnValue1.GetInputAnalogStickState(1, Ref[StickX], Ref[StickY])
        ReturnValue1_3 = Vector(StickX, StickY, 0)
        
        ReturnValue1_4 = MakeRotFromY(Ref[ReturnValue1_3])
        
        Roll1 = None
        Pitch1 = None
        Yaw1 = None
        BreakRotator(ReturnValue1_4, Ref[Roll1], Ref[Pitch1], Ref[Yaw1])
        ReturnValue_3 = Roll1 + 90
        ReturnValue1_5 = ReturnValue_3 / 360
        ReturnValue2_1 = ReturnValue1_5 - self.AngleOffset
        self.Angle = ReturnValue2_1
    

    def Close Radial Menu(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue.SetIgnoreLookInput(False)
        ReturnValue = self.GetOwningPlayer()
        ReturnValue.bShowMouseCursor = False
    

    def Open Radial Menu(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue.SetIgnoreLookInput(True)
        ReturnValue = self.GetOwningPlayer()
        ReturnValue.bShowMouseCursor = False
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0: Vector2D = Default__WidgetLayoutLibrary.GetViewportSize(self)
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_0, Ref[X], Ref[Y])
        ReturnValue_1: int32 = FTrunc(Y)
        ReturnValue1: int32 = FTrunc(X)
        ReturnValue_2: int32 = Divide_IntInt(ReturnValue_1, 2)
        ReturnValue1_0: int32 = Divide_IntInt(ReturnValue1, 2)
        ReturnValue.SetMouseLocation(ReturnValue1_0, ReturnValue_2)
    

    def Generate Radial Menu(self):
        self.ExecuteUbergraph_Widget_RadialMenu(2209)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_RadialMenu(2429)
    

    def Tick(self):
        ExecuteUbergraph_Widget_RadialMenu.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_RadialMenu.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_RadialMenu(2444)
    

    def Create Radial Menu(self):
        self.ExecuteUbergraph_Widget_RadialMenu(2948)
    

    def ExecuteUbergraph_Widget_RadialMenu(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.mTitleText.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 52, 'Value': 'None'}")
        self.mInfoContainer.SetRenderOpacity(0)
        goto(ExecutionFlow.Pop())
        # Label 133
        Variable: int32 = 0
        
        # Label 156
        ReturnValue: int32 = len(self.Buttons) - 1
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L2135")
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Widget_RadialMenuButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_RadialMenuButton, ReturnValue_1)
        ReturnValue_3: float = Conv_IntToFloat(Variable)
        
        ReturnValue_4: int32 = len(self.Buttons)
        ReturnValue1: float = Conv_IntToFloat(ReturnValue_4)
        ReturnValue1_0: float = ReturnValue_3 / ReturnValue1
        ReturnValue1_1: float = ReturnValue1_0 + self.ButtonSpacing
        ReturnValue2: float = ReturnValue1_1 + self.AngleOffset
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue_2, "startPoint", ReturnValue2)
        
        ReturnValue_4 = len(self.Buttons)
        ReturnValue1 = Conv_IntToFloat(ReturnValue_4)
        ReturnValue_5: float = 1 / ReturnValue1
        ReturnValue_6: float = ReturnValue_5 - self.ButtonSpacing
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue_2, "endPoint", ReturnValue_6)
        ReturnValue_3 = Conv_IntToFloat(Variable)
        
        ReturnValue_4 = len(self.Buttons)
        ReturnValue1 = Conv_IntToFloat(ReturnValue_4)
        ReturnValue1_0 = ReturnValue_3 / ReturnValue1
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue_2, "MinValue", ReturnValue1_0)
        ReturnValue_3 = Conv_IntToFloat(Variable)
        ReturnValue_7: float = ReturnValue_3 + 1
        
        ReturnValue_4 = len(self.Buttons)
        ReturnValue1 = Conv_IntToFloat(ReturnValue_4)
        ReturnValue_5 = 1 / ReturnValue1
        ReturnValue_8: float = ReturnValue_7 * ReturnValue_5
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue_2, "MaxValue", ReturnValue_8)
        
        Item = None
        Item = self.Buttons[Variable]
        
        Item = None
        Default__KismetSystemLibrary.SetNamePropertyByName(ReturnValue_2, "Name", Ref[Item])
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mRadialMenu", self)
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_2, "ButtonInteger", Variable)
        
        ReturnValue_4 = len(self.Buttons)
        ReturnValue_9: bool = ReturnValue_4 <= 2
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_2, "SingleButton", ReturnValue_9)
        
        Item1 = None
        Item1 = self.mIconTextures[Variable]
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mInputTextureIcon", Item1)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_2, "mMonochromeIcon", self.mMonochromeIcons)
        ReturnValue_10: Ptr[PanelSlot] = self.mContent.AddChild(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 2135
        ReturnValue_11: int32 = Variable + 1
        Variable = ReturnValue_11
        goto('L156')
        
        ReturnValue_12: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[self.mDescText])
        self.Widget_LetterSpacedText.SetTitle(ReturnValue_12)
        self.mContent.ClearChildren()
        goto('L133')
        # Label 2354
        self.Generate Radial Menu()
        self.Open Radial Menu()
        ReturnValue_13: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnimation, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        self.Close Radial Menu()
        goto(ExecutionFlow.Pop())
        self.Set Angle()
        if not self.OutsideDeadSpace:
            goto('L2877')
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        self.Pointer.SetContentColorAndOpacity(GraphicsWhite)
        ReturnValue1_2: float = 1 - self.Angle
        ReturnValue1_3: float = ReturnValue1_2 * 360
        ReturnValue3: float = ReturnValue1_3 + 180
        self.Pointer.SetRenderAngle(ReturnValue3)
        ReturnValue_14: FText = Default__KismetTextLibrary.Conv_NameToText(self.ActiveName)
        self.mTitleText.SetText(ReturnValue_14)
        self.mInfoContainer.SetRenderOpacity(1)
        goto(ExecutionFlow.Pop())
        # Label 2877
        self.Pointer.SetContentColorAndOpacity(LinearColor(R = 1, G = 1, B = 1, A = 0))
        goto('L15')
        goto('L2354')
    
