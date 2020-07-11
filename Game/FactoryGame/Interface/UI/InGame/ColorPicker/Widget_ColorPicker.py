
from codegen.ue4_stub import *

from Script.UMG import AddChildToUniformGrid
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorSquare import Widget_ColorSquare
from Script.Engine import Lerp
from Script.Engine import FClamp
from Script.Engine import SetObjectPropertyByName
from Script.UMG import GetChildrenCount
from Script.Engine import Conv_IntToFloat
from Script.Engine import Array_Set
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Player.BP_PlayerState import BP_PlayerState
from Script.UMG import SetColumn
from Script.Engine import PlayerController
from Script.UMG import GetChildAt
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import ESlateVisibility
from Script.Engine import IsValid
from Script.Engine import HSVToRGB
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import UniformGridSlot
from Script.UMG import SetRow
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker import ExecuteUbergraph_Widget_ColorPicker.K2Node_Event_MyGeometry
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker import ExecuteUbergraph_Widget_ColorPicker.K2Node_Event_InDeltaTime
from Script.FactoryGame import FGInteractWidget
from Script.Engine import RGBToHSV
from Script.UMG import Tick
from Script.UMG import Widget
from Script.FactoryGame import Init
from Script.Engine import SetIntPropertyByName
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.Engine import NearlyEqual_FloatFloat
from Script.UMG import Create
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker import ExecuteUbergraph_Widget_ColorPicker
from Script.CoreUObject import LinearColor

class Widget_ColorPicker(FGInteractWidget):
    mNumColors: int32 = 10
    mNumShades: int32 = 5
    mShadeExtremeCutoff: float = 0.20000000298023224
    mHueValue: float
    mSaturationValue: float = 1
    mValueValue: float = 1
    mLastClickedColorSquare: Ptr[Widget_ColorSquare]
    mPlayerState: Ptr[BP_PlayerState]
    mOnColorPicked: FMulticastScriptDelegate
    mUseKeyboard = True
    mUseMouse = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mDesiredAlignmentSize = Namespace(SizeRule=0, Value=1)
    mCallCustomTickOnConstruct = True
    
    def GetResetButtonVisibility(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mLastClickedColorSquare)
        if not ReturnValue:
            goto('L645')
        Variable: uint8 = 2
        Variable1: uint8 = 0
        ReturnValue_0: bool = NearlyEqual_FloatFloat(self.mLastClickedColorSquare.mDefaultColor.SpecifiedColor.R, self.mLastClickedColorSquare.mColor.SpecifiedColor.R, 9.999999974752427e-07)
        ReturnValue1: bool = NearlyEqual_FloatFloat(self.mLastClickedColorSquare.mDefaultColor.SpecifiedColor.B, self.mLastClickedColorSquare.mColor.SpecifiedColor.B, 9.999999974752427e-07)
        ReturnValue2: bool = NearlyEqual_FloatFloat(self.mLastClickedColorSquare.mDefaultColor.SpecifiedColor.G, self.mLastClickedColorSquare.mColor.SpecifiedColor.G, 9.999999974752427e-07)
        ReturnValue_1: bool = ReturnValue_0 and ReturnValue2
        ReturnValue1_0: bool = ReturnValue_1 and ReturnValue1
        Variable_0: bool = ReturnValue1_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_2: uint8 = switch.get(Variable_0, None)
        goto('L665')
        # Label 645
        ReturnValue_2 = 2
    

    def GetOneDimensionalIndex(self, ColorIndex: int32, ShadeIndex: int32):
        ReturnValue: int32 = ShadeIndex * self.mNumColors
        ReturnValue_0: int32 = ColorIndex + ReturnValue
        index = ReturnValue_0
    

    def GetSavedColorFromIndexes(self, ColorIndex: int32, ShadeIndex: int32):
        
        Index = None
        self.GetOneDimensionalIndex(ColorIndex, ShadeIndex, Ref[Index])
        
        self.mPlayerState.mSavedColorPickerColors = None
        Item = None
        Item = self.mPlayerState.mSavedColorPickerColors[Index]
        SlateColor.SpecifiedColor = Item
        SlateColor.ColorUseRule = 0
        SavedColor = SlateColor
    

    def CalculateSaturationAndValueFromIndex(self, index: int32):
        ReturnValue: float = Conv_IntToFloat(index)
        ReturnValue_0: float = 1 - self.mShadeExtremeCutoff
        ReturnValue_1: int32 = self.mNumShades - 1
        ReturnValue1: float = Conv_IntToFloat(ReturnValue_1)
        ReturnValue_2: float = ReturnValue / ReturnValue1
        ReturnValue_3: float = Lerp(self.mShadeExtremeCutoff, ReturnValue_0, ReturnValue_2)
        ReturnValue_4: float = ReturnValue_3 * 2
        ReturnValue_5: float = FClamp(ReturnValue_4, 0, 1)
        ReturnValue1_0: float = FClamp(ReturnValue_4, 1, 2)
        ReturnValue1_1: float = ReturnValue1_0 - 1
        ReturnValue2: float = 1 - ReturnValue1_1
        Saturation = ReturnValue_5
        Value = ReturnValue2
    

    def CalculateHueFromIndex(self, index: int32):
        ReturnValue: float = Conv_IntToFloat(index)
        ReturnValue1: float = Conv_IntToFloat(self.mNumColors)
        ReturnValue_0: float = 360 / ReturnValue1
        ReturnValue_1: float = ReturnValue * ReturnValue_0
        Hue = ReturnValue_1
    

    def FirstTimeFillColors(self):
        ExecutionFlow.Push("L613")
        Variable: int32 = 0
        # Label 28
        ReturnValue1: int32 = self.mNumShades - 1
        ReturnValue1_0: bool = Variable <= ReturnValue1
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L465")
        Variable1: int32 = 0
        # Label 146
        ReturnValue: int32 = self.mNumColors - 1
        ReturnValue_0: bool = Variable1 <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L539")
        
        Saturation = None
        Value = None
        self.CalculateSaturationAndValueFromIndex(Variable, Ref[Saturation], Ref[Value])
        
        Hue = None
        self.CalculateHueFromIndex(Variable1, Ref[Hue])
        ReturnValue_1: LinearColor = HSVToRGB(Hue, Saturation, Value, 1)
        
        self.mPlayerState.mSavedColorPickerColors = None
        ReturnValue_2: int32 = self.mPlayerState.mSavedColorPickerColors.append(ReturnValue_1)
        goto(ExecutionFlow.Pop())
        # Label 465
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L28')
        # Label 539
        ReturnValue1_1: int32 = Variable1 + 1
        Variable1 = ReturnValue1_1
        goto('L146')
    

    def GetFinalColor(self):
        ReturnValue: LinearColor = HSVToRGB(self.mHueValue, self.mSaturationValue, self.mValueValue, 1)
        ReturnValue_0: LinearColor = ReturnValue
    

    def CloseColorPicker(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__BPHUDHelpers.PopStackWidget(ReturnValue, self, self)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ColorPicker(1538)
    

    def Init(self):
        self.ExecuteUbergraph_Widget_ColorPicker(2041)
    

    def ExitColorPicker(self):
        self.ExecuteUbergraph_Widget_ColorPicker(2151)
    

    def BndEvt__mCancelButton_K2Node_ComponentBoundEvent_36_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorPicker(2166)
    

    def Tick(self):
        ExecuteUbergraph_Widget_ColorPicker.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ColorPicker.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorPicker(2181)
    

    def BndEvt__mResetButton_K2Node_ComponentBoundEvent_31_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorPicker(2445)
    

    def BndEvt__mAcceptButton_K2Node_ComponentBoundEvent_331_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorPicker(2846)
    

    def BndEvt__Widget_Window_K2Node_ComponentBoundEvent_0_OnClose__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorPicker(2851)
    

    def BndEvt__mCancel_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorPicker(2856)
    

    def BndEvt__mReset_K2Node_ComponentBoundEvent_2_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorPicker(2861)
    

    def BndEvt__mAccept_K2Node_ComponentBoundEvent_3_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorPicker(15)
    

    def ExecuteUbergraph_Widget_ColorPicker(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Variable: int32 = 0
        # Label 38
        ReturnValue: int32 = self.mColorSquaresGrid.GetChildrenCount()
        ReturnValue2: int32 = ReturnValue - 1
        ReturnValue3: bool = Variable <= ReturnValue2
        if not ReturnValue3:
            goto('L449')
        ExecutionFlow.Push("L552")
        ReturnValue_0: Ptr[Widget] = self.mColorSquaresGrid.GetChildAt(Variable)
        Square: Ptr[Widget_ColorSquare] = Cast[Widget_ColorSquare](ReturnValue_0)
        bSuccess1: bool = Square
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        
        self.mPlayerState.mSavedColorPickerColors = None
        Square.mColor.SpecifiedColor = None
        Default__KismetArrayLibrary.Array_Set(Square.mIndex, False, Ref[self.mPlayerState.mSavedColorPickerColors], Ref[Square.mColor.SpecifiedColor])
        goto(ExecutionFlow.Pop())
        # Label 449
        self.CloseColorPicker()
        ReturnValue2_0: LinearColor = HSVToRGB(self.mHueValue, self.mSaturationValue, self.mValueValue, 1)
        self.mOnColorPicked.ProcessMulticastDelegate(ReturnValue2_0)
        goto(ExecutionFlow.Pop())
        # Label 552
        ReturnValue_1: int32 = Variable + 1
        Variable = ReturnValue_1
        goto('L38')
        # Label 626
        ExecutionFlow.Push("L1374")
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_3: Ptr[Widget_ColorSquare] = Default__WidgetBlueprintLibrary.Create(self, Widget_ColorSquare, ReturnValue_2)
        
        Hue = None
        self.CalculateHueFromIndex(Variable1, Ref[Hue])
        
        Saturation = None
        Value = None
        self.CalculateSaturationAndValueFromIndex(Variable2, Ref[Saturation], Ref[Value])
        ReturnValue1: LinearColor = HSVToRGB(Hue, Saturation, Value, 1)
        SlateColor1.SpecifiedColor = ReturnValue1
        SlateColor1.ColorUseRule = 0
        
        SlateColor1 = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_3, "mDefaultColor", Ref[SlateColor1])
        
        SavedColor = None
        self.GetSavedColorFromIndexes(Variable1, Variable2, Ref[SavedColor])
        
        SavedColor = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_3, "mColor", Ref[SavedColor])
        
        Index = None
        self.GetOneDimensionalIndex(Variable1, Variable2, Ref[Index])
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_3, "mIndex", Index)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_3, "mColorPicker", self)
        ReturnValue_4: Ptr[UniformGridSlot] = self.mColorSquaresGrid.AddChildToUniformGrid(ReturnValue_3)
        ReturnValue_4.SetColumn(Variable1)
        ReturnValue_4.SetRow(Variable2)
        goto(ExecutionFlow.Pop())
        # Label 1374
        ReturnValue1_0: int32 = Variable1 + 1
        Variable1: int32 = ReturnValue1_0
        # Label 1443
        ReturnValue_5: int32 = self.mNumColors - 1
        ReturnValue_6: bool = Variable1 <= ReturnValue_5
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        goto('L626')
        ReturnValue1_1: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[BP_PlayerState] = Cast[BP_PlayerState](ReturnValue1_1.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        self.mPlayerState = State
        
        self.mPlayerState.mSavedColorPickerColors = None
        ReturnValue_7: int32 = len(self.mPlayerState.mSavedColorPickerColors)
        ReturnValue1_2: bool = ReturnValue_7 <= 0
        if not ReturnValue1_2:
            goto('L1821')
        self.FirstTimeFillColors()
        # Label 1821
        Variable2: int32 = 0
        # Label 1844
        ReturnValue1_3: int32 = self.mNumShades - 1
        ReturnValue2_1: bool = Variable2 <= ReturnValue1_3
        if not ReturnValue2_1:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1967")
        Variable1 = 0
        goto('L1443')
        # Label 1967
        ReturnValue2_2: int32 = Variable2 + 1
        Variable2 = ReturnValue2_2
        goto('L1844')
        self.Init()
        self.mHueSlider.mColorPicker = self
        self.mSaturationSlider.mColorPicker = self
        self.mValueSlider.mColorPicker = self
        goto(ExecutionFlow.Pop())
        self.CloseColorPicker()
        goto(ExecutionFlow.Pop())
        # Label 2166
        self.OnEscapePressed()
        goto(ExecutionFlow.Pop())
        self.Tick(MyGeometry, InDeltaTime)
        ReturnValue_8: bool = Default__KismetSystemLibrary.IsValid(self.mLastClickedColorSquare)
        if not ReturnValue_8:
           goto(ExecutionFlow.Pop())
        ReturnValue_9: LinearColor = HSVToRGB(self.mHueValue, self.mSaturationValue, self.mValueValue, 1)
        SlateColor.SpecifiedColor = ReturnValue_9
        SlateColor.ColorUseRule = 0
        self.mLastClickedColorSquare.mColor = SlateColor
        goto(ExecutionFlow.Pop())
        # Label 2445
        ReturnValue1_4: bool = Default__KismetSystemLibrary.IsValid(self.mLastClickedColorSquare)
        if not ReturnValue1_4:
           goto(ExecutionFlow.Pop())
        
        H = None
        S = None
        V = None
        A = None
        RGBToHSV(self.mLastClickedColorSquare.mDefaultColor.SpecifiedColor, Ref[H], Ref[S], Ref[V], Ref[A])
        self.mHueValue = H
        
        H = None
        S = None
        V = None
        A = None
        RGBToHSV(self.mLastClickedColorSquare.mDefaultColor.SpecifiedColor, Ref[H], Ref[S], Ref[V], Ref[A])
        self.mSaturationValue = S
        
        H = None
        S = None
        V = None
        A = None
        RGBToHSV(self.mLastClickedColorSquare.mDefaultColor.SpecifiedColor, Ref[H], Ref[S], Ref[V], Ref[A])
        self.mValueValue = V
        goto(ExecutionFlow.Pop())
        goto('L15')
        goto('L2166')
        goto('L2166')
        goto('L2445')
    

    def mOnColorPicked__DelegateSignature(self, Color: LinearColor):
        pass
    
