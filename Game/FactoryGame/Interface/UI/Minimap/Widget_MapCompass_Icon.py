
from codegen.ue4_stub import *

from Script.FactoryGame import ERepresentationType
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_StaticActor_Background import MapCompass_StaticActor_Background
from Script.Engine import Texture2D
from Script.FactoryGame import GetRepresentationType
from Script.FactoryGame import GetRealActor
from Script.Engine import FromSeconds
from Script.FactoryGame import GetRepresentationTexture
from Script.FactoryGame import FGBuildableRadarTower
from Script.Engine import EqualEqual_ByteByte
from Script.Engine import GreaterEqual_IntInt
from Script.UMG import GetChildrenCount
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_Icon_beacon import MapCompass_Icon_beacon
from Script.CoreUObject import Timespan
from Script.Engine import Not_PreBool
from Game.FactoryGame.Buildable.Factory.TrainStation.UI.TrainStation import TrainStation
from Script.FactoryGame import GetNumRadarExpansionSteps
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.Engine import FormatArgumentData
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapCompass_Icon import ExecuteUbergraph_Widget_MapCompass_Icon
from Script.UMG import SetUserSpecifiedScale
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_StaticActor_Border import MapCompass_StaticActor_Border
from Script.FactoryGame import GetCurrentExpansionStep
from Script.Engine import TimerHandle
from Script.UMG import StopAnimation
from Script.Engine import IsValid
from Script.Engine import NotEqual_TextText
from Game.FactoryGame.Interface.UI.Minimap.Widget_MapCompass_Icon import ExecuteUbergraph_Widget_MapCompass_Icon.K2Node_Event_IsDesignTime
from Script.Engine import Conv_IntToText
from Script.UMG import SetColorAndOpacity
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.UMG import Widget
from Script.Engine import BreakTimespan
from Script.UMG import SetRenderAngle
from Script.Engine import Format
from Script.Engine import EqualEqual_ObjectObject
from Script.UMG import WidgetAnimation
from Script.Engine import NotEqual_ByteByte
from Script.FactoryGame import GetRepresentationColor
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_Circle_Border import MapCompass_Circle_Border
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_DirectionalActor_Border import MapCompass_DirectionalActor_Border
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.Assets.Shared.Circle_Background import Circle_Background
from Script.Engine import Actor
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import GetRepresentationText
from Script.FactoryGame import GetTimeToNextExpansion
from Script.FactoryGame import FGActorRepresentation
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.CoreUObject import LinearColor

class Widget_MapCompass_Icon(UserWidget):
    BlinkAnim: Ptr[WidgetAnimation]
    ShowDescription: Ptr[WidgetAnimation]
    mColor: LinearColor
    mRepresentationType: uint8
    mDescriptionText: FText
    OnHovered: FMulticastScriptDelegate
    OnUnhovered: FMulticastScriptDelegate
    mActorRepresentation: Ptr[FGActorRepresentation]
    mIsCompassObject: bool
    mScale: float = 1
    mDynamicDescriptionTimerEvent: TimerHandle
    
    def UpdateRadarTowerTime(self):
        ReturnValue: Ptr[Actor] = self.mActorRepresentation.GetRealActor()
        Tower: Ptr[FGBuildableRadarTower] = Cast[FGBuildableRadarTower](ReturnValue)
        bSuccess: bool = Tower
        if not bSuccess:
            goto('L2442')
        FormatArgumentData.ArgumentName = "Description"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = self.mDescriptionText
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        FormatArgumentData1.ArgumentName = "Description"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = self.mDescriptionText
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        ReturnValue_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 588, 'Value': '{Description}\r\n(Scan Completed)'}", Array)
        Array1: List[FormatArgumentData] = [FormatArgumentData1]
        ReturnValue1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 738, 'Value': '{Description}\r\n(NO POWER)'}", Array1)
        FormatArgumentData2.ArgumentName = "Description"
        FormatArgumentData2.ArgumentValueType = 4
        FormatArgumentData2.ArgumentValue = self.mDescriptionText
        FormatArgumentData2.ArgumentValueInt = 0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        ReturnValue_1: float = Tower.GetTimeToNextExpansion()
        ReturnValue_2: bool = Tower.HasPower()
        ReturnValue_3: Timespan = FromSeconds(ReturnValue_1)
        Variable: bool = ReturnValue_2
        
        Days = None
        Hours = None
        Minutes = None
        Seconds = None
        Milliseconds = None
        BreakTimespan(ReturnValue_3, Ref[Days], Ref[Hours], Ref[Minutes], Ref[Seconds], Ref[Milliseconds])
        ReturnValue_4: int32 = Tower.GetNumRadarExpansionSteps()
        ReturnValue_5: FText = Default__KismetTextLibrary.Conv_IntToText(Seconds, False, True, 2, 324)
        ReturnValue_6: int32 = Days * 24
        FormatArgumentData3.ArgumentName = "Sec"
        FormatArgumentData3.ArgumentValueType = 4
        FormatArgumentData3.ArgumentValue = ReturnValue_5
        FormatArgumentData3.ArgumentValueInt = 0
        FormatArgumentData3.ArgumentValueFloat = 0
        FormatArgumentData3.ArgumentValueGender = 0
        ReturnValue_7: int32 = ReturnValue_6 + Hours
        ReturnValue_8: int32 = Tower.GetCurrentExpansionStep()
        ReturnValue1_0: int32 = ReturnValue_7 * 60
        ReturnValue1_1: int32 = ReturnValue_8 + 1
        ReturnValue2: int32 = ReturnValue1_0 + Minutes
        ReturnValue_9: bool = GreaterEqual_IntInt(ReturnValue1_1, ReturnValue_4)
        ReturnValue1_2: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue2, False, True, 2, 324)
        Variable1: bool = ReturnValue_9
        FormatArgumentData4.ArgumentName = "Min"
        FormatArgumentData4.ArgumentValueType = 4
        FormatArgumentData4.ArgumentValue = ReturnValue1_2
        FormatArgumentData4.ArgumentValueInt = 0
        FormatArgumentData4.ArgumentValueFloat = 0
        FormatArgumentData4.ArgumentValueGender = 0
        Array2: List[FormatArgumentData] = [FormatArgumentData2, FormatArgumentData4, FormatArgumentData3]
        ReturnValue2_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2211, 'Value': '{Description}\r\n(Time until next scan: {Min}:{Sec})'}", Array2)
        
        switch = {
            False: ReturnValue1,
            True: ReturnValue2_0
        }
        
        switch_0 = {
            False: switch.get(Variable, None),
            True: ReturnValue_0
        }
        self.mMapDescription.SetText(switch_0.get(Variable1, None))
    

    def SetScale(self, Scale: float):
        self.mScale = Scale
        self.mIconScaleBox.SetUserSpecifiedScale(self.mScale)
    

    def UpdateActor(self, actorRepresentation: Ptr[FGActorRepresentation], mIsCompassObject: bool):
        self.mActorRepresentation = actorRepresentation
        self.mIsCompassObject = mIsCompassObject
        ReturnValue: uint8 = self.mActorRepresentation.GetRepresentationType()
        self.SetRepresentatoinType(ReturnValue)
        ReturnValue_0: Ptr[Texture2D] = self.mActorRepresentation.GetRepresentationTexture()
        self.SetIcon(ReturnValue_0)
        ReturnValue_1: LinearColor = self.mActorRepresentation.GetRepresentationColor()
        self.SetColor(ReturnValue_1)
        ReturnValue_2: FText = self.mActorRepresentation.GetRepresentationText()
        # Label 299
        self.SetDescription(ReturnValue_2)
        Variable2: uint8 = 1
        Variable3: uint8 = 3
        Variable: bool = self.mIsCompassObject
        
        switch = {
            False: Variable3,
            True: Variable2
        }
        self.mShadow.SetVisibility(switch.get(Variable, None))
        
        switch_0 = {
            False: Variable3,
            True: Variable2
        }
        self.mDiamondShadow.SetVisibility(switch_0.get(Variable, None))
        
        switch_1 = {
            False: Variable3,
            True: Variable2
        }
        self.mPingShadow.SetVisibility(switch_1.get(Variable, None))
        
        switch_2 = {
            False: Variable3,
            True: Variable2
        }
        self.mDescContainer.SetVisibility(switch_2.get(Variable, None))
        Variable_0: uint8 = 1
        Variable1: uint8 = 3
        ReturnValue_3: bool = Not_PreBool(self.mIsCompassObject)
        Variable1_0: bool = ReturnValue_3
        
        switch_3 = {
            False: Variable1,
            True: Variable_0
        }
        self.mCompassDescContainer.SetVisibility(switch_3.get(Variable1_0, None))
    

    def SetIconType(self, mRepresentationType: uint8):
        ExecutionFlow.Push("L1269")
        LocalRepresentationType = 0
        LocalRepresentationType = mRepresentationType
        Variable: Ptr[Widget] = None
        Variable1: Ptr[Widget] = None
        Variable2: Ptr[Widget] = None
        Variable3: Ptr[Widget] = None
        Variable4: Ptr[Widget] = None
        Variable2_0: uint8 = LocalRepresentationType
        
        switch = {
            0: Variable4,
            1: self.mDiamondIconContainer,
            2: self.mDiamondIconContainer,
            3: self.mDiamondIconContainer,
            4: self.mPingIconContainer,
            5: Variable3,
            6: self.mDiamondIconContainer,
            7: Variable2,
            8: self.mDiamondIconContainer,
            9: self.mDiamondIconContainer,
            10: Variable1,
            11: self.mDiamondIconContainer,
            12: Variable,
            13: self.mDiamondIconContainer
        }
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(switch.get(Variable2_0, None))
        Variable_0: bool = ReturnValue
        
        switch_0 = {
            0: Variable4,
            1: self.mDiamondIconContainer,
            2: self.mDiamondIconContainer,
            3: self.mDiamondIconContainer,
            4: self.mPingIconContainer,
            5: Variable3,
            6: self.mDiamondIconContainer,
            7: Variable2,
            8: self.mDiamondIconContainer,
            9: self.mDiamondIconContainer,
            10: Variable1,
            11: self.mDiamondIconContainer,
            12: Variable,
            13: self.mDiamondIconContainer
        }
        
        switch_1 = {
            False: self.mCircleIconContainer,
            True: switch_0.get(Variable2_0, None)
        }
        # Label 430
        LocalWidget = switch_1.get(Variable_0, None)
        Variable_1: int32 = 0
        # Label 742
        ReturnValue_0: int32 = self.mIconContainers.GetChildrenCount()
        ReturnValue_1: bool = Variable_1 <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1195")
        ReturnValue_2: Ptr[Widget] = self.mIconContainers.GetChildAt(Variable_1)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_2)
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        Variable_2: uint8 = 0
        Variable1_0: uint8 = 1
        ReturnValue_2 = self.mIconContainers.GetChildAt(Variable_1)
        ReturnValue_3: bool = EqualEqual_ObjectObject(ReturnValue_2, LocalWidget)
        Variable1_1: bool = ReturnValue_3
        
        switch_2 = {
            False: Variable1_0,
            True: Variable_2
        }
        ReturnValue_2.SetVisibility(switch_2.get(Variable1_1, None))
        goto(ExecutionFlow.Pop())
        # Label 1195
        ReturnValue_4: int32 = Variable_1 + 1
        Variable_1 = ReturnValue_4
        goto('L742')
    

    def TestFunction(self, Color: LinearColor, mRepresentationType: uint8, Icon: Ptr[Texture2D]):
        self.SetRepresentatoinType(mRepresentationType)
        self.SetColor(Color)
        self.SetIcon(Icon)
    

    def SetDescription(self, mDescriptionText: FText):
        self.mDescriptionText = mDescriptionText
        self.mMapDescription.SetText(self.mDescriptionText)
        self.mCompassDescription.SetText(self.mDescriptionText)
    

    def SetRepresentatoinType(self, mRepresentationType: uint8):
        self.mRepresentationType = mRepresentationType
        self.SetIconType(self.mRepresentationType)
        Variable: Ptr[Texture2D] = MapCompass_Circle_Border
        Variable16: Ptr[Texture2D] = MapCompass_Circle_Border
        Variable17: Ptr[Texture2D] = None
        Variable18: Ptr[Texture2D] = TrainStation
        Variable19: Ptr[Texture2D] = None
        Variable20: Ptr[Texture2D] = None
        Variable21: Ptr[Texture2D] = MapCompass_StaticActor_Background
        Variable22: Ptr[Texture2D] = None
        Variable23: Ptr[Texture2D] = MapCompass_StaticActor_Border
        Variable24: Ptr[Texture2D] = None
        Variable25: Ptr[Texture2D] = MapCompass_StaticActor_Border
        Variable26: Ptr[Texture2D] = MapCompass_StaticActor_Border
        Variable27: Ptr[Texture2D] = MapCompass_StaticActor_Border
        Variable28: Ptr[Texture2D] = None
        ReturnValue: bool = Not_PreBool(self.mIsCompassObject)
        Variable29: Ptr[Texture2D] = MapCompass_DirectionalActor_Border
        Variable1: uint8 = self.mRepresentationType
        Variable2: bool = ReturnValue
        
        switch = {
            False: Variable,
            True: Variable29
        }
        
        switch_0 = {
            False: Variable,
            True: Variable29
        }
        
        switch_1 = {
            0: Variable28,
            1: Variable27,
            2: Variable26,
            3: Variable25,
            4: Variable24,
            5: switch.get(Variable2, None),
            6: Variable23,
            7: Variable22,
            8: Variable21,
            9: Variable20,
            10: Variable19,
            11: Variable18,
            12: switch_0.get(Variable2, None),
            13: Variable17
        }
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(switch_1.get(Variable1, None))
        Variable1_0: bool = ReturnValue1
        
        switch_2 = {
            False: Variable,
            True: Variable29
        }
        
        switch_3 = {
            False: Variable,
            True: Variable29
        }
        
        switch_4 = {
            0: Variable28,
            1: Variable27,
            2: Variable26,
            3: Variable25,
            4: Variable24,
            5: switch_2.get(Variable2, None),
            6: Variable23,
            7: Variable22,
            8: Variable21,
            9: Variable20,
            10: Variable19,
            11: Variable18,
            12: switch_3.get(Variable2, None),
            13: Variable17
        }
        
        switch_5 = {
            False: Variable16,
            True: switch_4.get(Variable1, None)
        }
        self.mBorder.SetBrushFromTexture(switch_5.get(Variable1_0, None), False)
        
        switch_6 = {
            False: Variable,
            True: Variable29
        }
        
        switch_7 = {
            False: Variable,
            True: Variable29
        }
        
        switch_8 = {
            0: Variable28,
            1: Variable27,
            2: Variable26,
            3: Variable25,
            4: Variable24,
            5: switch_6.get(Variable2, None),
            6: Variable23,
            7: Variable22,
            8: Variable21,
            9: Variable20,
            10: Variable19,
            11: Variable18,
            12: switch_7.get(Variable2, None),
            13: Variable17
        }
        
        switch_9 = {
            False: Variable16,
            True: switch_8.get(Variable1, None)
        }
        self.mShadow.SetBrushFromTexture(switch_9.get(Variable1_0, None), False)
        Variable1_1: Ptr[Texture2D] = Circle_Background
        Variable2_0: Ptr[Texture2D] = None
        Variable3: Ptr[Texture2D] = None
        Variable4: Ptr[Texture2D] = None
        Variable5: Ptr[Texture2D] = None
        Variable6: Ptr[Texture2D] = None
        Variable7: Ptr[Texture2D] = MapCompass_StaticActor_Background
        Variable8: Ptr[Texture2D] = None
        Variable9: Ptr[Texture2D] = MapCompass_StaticActor_Background
        Variable10: Ptr[Texture2D] = None
        Variable11: Ptr[Texture2D] = None
        Variable12: Ptr[Texture2D] = MapCompass_StaticActor_Background
        Variable13: Ptr[Texture2D] = MapCompass_StaticActor_Background
        Variable14: Ptr[Texture2D] = MapCompass_StaticActor_Background
        Variable15: Ptr[Texture2D] = None
        Variable_0: uint8 = self.mRepresentationType
        
        switch_10 = {
            0: Variable15,
            1: Variable14,
            2: Variable13,
            3: Variable12,
            4: Variable11,
            5: Variable10,
            6: Variable9,
            7: Variable8,
            8: Variable7,
            9: Variable6,
            10: Variable5,
            11: Variable4,
            12: Variable3,
            13: Variable2_0
        }
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(switch_10.get(Variable_0, None))
        Variable_1: bool = ReturnValue_0
        
        switch_11 = {
            0: Variable15,
            1: Variable14,
            2: Variable13,
            3: Variable12,
            4: Variable11,
            5: Variable10,
            6: Variable9,
            7: Variable8,
            8: Variable7,
            9: Variable6,
            10: Variable5,
            11: Variable4,
            12: Variable3,
            13: Variable2_0
        }
        
        switch_12 = {
            False: Variable1_1,
            True: switch_11.get(Variable_0, None)
        }
        self.mBackground.SetBrushFromTexture(switch_12.get(Variable_1, None), False)
        ReturnValue_1: bool = EqualEqual_ByteByte(self.mRepresentationType, 4)
        if not ReturnValue_1:
            goto('L2502')
        ReturnValue_2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.BlinkAnim, 0, 0, 0, 1)
        # End
        # Label 2502
        self.StopAnimation(self.BlinkAnim)
    

    def SetRotation(self, Angle: float):
        ReturnValue: float = Angle + 90
        self.mBorder.SetRenderAngle(ReturnValue)
        self.mShadow.SetRenderAngle(ReturnValue)
    

    def SetIcon(self, Texture: Ptr[Texture2D]):
        self.mIcon.SetBrushFromTexture(Texture, False)
        self.mDiamondIcon.SetBrushFromTexture(Texture, False)
    

    def SetColor(self, InColorAndOpacity: LinearColor):
        self.mColor = InColorAndOpacity
        ReturnValue1: bool = EqualEqual_ByteByte(self.mRepresentationType, 1)
        Variable1: bool = ReturnValue1
        
        switch = {
            False: self.mDiamondIcon,
            True: self.mDiamondBackground
        }
        switch.get(Variable1, None).SetColorAndOpacity(self.mColor)
        self.mBackground.SetColorAndOpacity(self.mColor)
        self.mPingBorder.SetColorAndOpacity(self.mColor)
        ReturnValue: bool = EqualEqual_ByteByte(self.mRepresentationType, 1)
        Variable: bool = ReturnValue
        
        switch_0 = {
            False: self.mDiamondBackground,
            True: self.mDiamondIcon
        }
        switch_0.get(Variable, None).SetColorAndOpacity(LinearColor(R = 1, G = 1, B = 1, A = 1))
    

    def BndEvt__Button_1_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_MapCompass_Icon(10)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_MapCompass_Icon.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MapCompass_Icon(454)
    

    def DynamicDescriptionUpdate(self):
        self.ExecuteUbergraph_Widget_MapCompass_Icon(541)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_MapCompass_Icon(610)
    

    def BndEvt__Button_1_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_MapCompass_Icon(763)
    

    def ExecuteUbergraph_Widget_MapCompass_Icon(self):
        self.OnUnhovered.ProcessMulticastDelegate()
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_StringToText("")
        
        ReturnValue1_0: bool = Default__KismetTextLibrary.NotEqual_TextText(Ref[self.mDescriptionText], Ref[ReturnValue1])
        if not ReturnValue1_0:
            goto('L768')
        ReturnValue1_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ShowDescription, 0, 1, 1, 1)
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mDynamicDescriptionTimerEvent])
        # End
        # Label 248
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ShowDescription, 0, 1, 0, 1)
        # End
        # Label 299
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_StringToText("")
        
        ReturnValue_1: bool = Default__KismetTextLibrary.NotEqual_TextText(Ref[self.mDescriptionText], Ref[ReturnValue_0])
        if not ReturnValue_1:
            goto('L768')
        goto('L248')
        # Label 430
        self.OnHovered.ProcessMulticastDelegate()
        goto('L299')
        self.TestFunction(LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.05951099842786789, A = 1), 1, MapCompass_Icon_beacon)
        self.SetScale(self.mScale)
        # End
        CmpSuccess: bool = NotEqual_ByteByte(self.mRepresentationType, 6)
        if not CmpSuccess:
            goto('L591')
        # End
        # Label 591
        self.UpdateRadarTowerTime()
        # End
        Variable: uint8 = 3
        Variable1: uint8 = 0
        Variable_0: bool = self.mIsCompassObject
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mButton.SetVisibility(switch.get(Variable_0, None))
        # End
        goto('L430')
    

    def OnUnhovered__DelegateSignature(self):
        pass
    

    def OnHovered__DelegateSignature(self):
        pass
    
