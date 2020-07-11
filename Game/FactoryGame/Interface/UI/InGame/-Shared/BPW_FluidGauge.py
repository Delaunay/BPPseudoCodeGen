
from codegen.ue4_stub import *

from Script.Engine import SetScalarParameterValue
from Script.UMG import SlotAsOverlaySlot
from Game.FactoryGame.Interface.UI.InGame.-Shared.BPW_FluidGauge import ExecuteUbergraph_BPW_FluidGauge
from Script.Engine import Lerp
from Game.FactoryGame.Interface.UI.Assets.AnalougeMeter.AnalougeMeter_Indicator import AnalougeMeter_Indicator
from Script.Engine import SetVectorParameterValue
from Script.Engine import Conv_BoolToFloat
from Script.UMG import SetPadding
from Game.FactoryGame.Interface.UI.InGame.-Shared.BPW_FluidGauge import ExecuteUbergraph_BPW_FluidGauge.K2Node_Event_IsDesignTime
from Script.UMG import OverlaySlot
from Script.UMG import Default__WidgetLayoutLibrary
from Script.Engine import MaterialInstanceDynamic
from Script.UMG import GetDynamicMaterial
from Script.UMG import SetColorAndOpacity
from Script.Engine import SetTextureParameterValue
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class BPW_FluidGauge(UserWidget):
    mGaugeBarPadding: float
    mUseBarDivider: bool = True
    mDividerPosition: float
    mPrimaryColor: LinearColor = Namespace(A=1, B=0.417246013879776, G=0.417246013879776, R=0.421875)
    mSecondaryColor: LinearColor = Namespace(A=1, B=0.556863009929657, G=0.3803919851779938, R=0.10588199645280838)
    mMeterColor: LinearColor = Namespace(A=1, B=0.13563300669193268, G=0.13286800682544708, R=0.13286800682544708)
    mGaugeValue: float
    mGaugeName: FText = NSLOCTEXT("", "AECB7BCA4EED5BBD12EBB2A86300F2E3", "Gauge")
    
    def SetGaugeName(self, mGaugeName: FText):
        self.mGaugeName = mGaugeName
        self.mGaugeText.SetText(self.mGaugeName)
    

    def SetDividerPosition(self, mDividerPosition: float):
        self.mDividerPosition = mDividerPosition
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.mGaugeBar.GetDynamicMaterial()
        ReturnValue.SetScalarParameterValue("Angle", self.mDividerPosition)
    

    def SetupMeterTexture(self):
        ReturnValue1: Ptr[MaterialInstanceDynamic] = self.mGaugeMeter.GetDynamicMaterial()
        ReturnValue1.SetTextureParameterValue("Texture", AnalougeMeter_Indicator)
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.mGaugeMeterShadow.GetDynamicMaterial()
        ReturnValue.SetTextureParameterValue("Texture", AnalougeMeter_Indicator)
    

    def UpdateGaugeValue(self, mGaugeValue: float):
        range = 134
        self.mGaugeValue = mGaugeValue
        ReturnValue1: Ptr[MaterialInstanceDynamic] = self.mGaugeMeter.GetDynamicMaterial()
        ReturnValue: float = range / 360
        ReturnValue_0: float = ReturnValue * -1
        ReturnValue_1: float = Lerp(ReturnValue, ReturnValue_0, self.mGaugeValue)
        ReturnValue1.SetScalarParameterValue("Angle", ReturnValue_1)
        ReturnValue_2: Ptr[MaterialInstanceDynamic] = self.mGaugeMeterShadow.GetDynamicMaterial()
        ReturnValue = range / 360
        ReturnValue_0 = ReturnValue * -1
        ReturnValue_1 = Lerp(ReturnValue, ReturnValue_0, self.mGaugeValue)
        ReturnValue_2.SetScalarParameterValue("Angle", ReturnValue_1)
    

    def SetMeterColor(self, mMeterColor: LinearColor):
        self.mMeterColor = mMeterColor
        self.mGaugeMeter.SetColorAndOpacity(self.mMeterColor)
    

    def SetBarColors(self, mPrimaryColor: LinearColor, mSecondaryColor: LinearColor):
        self.mPrimaryColor = mPrimaryColor
        self.mSecondaryColor = mSecondaryColor
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.mGaugeBar.GetDynamicMaterial()
        ReturnValue.SetVectorParameterValue("PrimaryColor", self.mPrimaryColor)
        ReturnValue.SetVectorParameterValue("SecondaryColor", self.mSecondaryColor)
        SlateColor.SpecifiedColor = self.mPrimaryColor
        SlateColor.ColorUseRule = 0
        self.mGaugeText.SetColorAndOpacity(SlateColor)
    

    def SetUseBarDivider(self, mUseBarDivider: bool):
        self.mUseBarDivider = mUseBarDivider
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.mGaugeBar.GetDynamicMaterial()
        ReturnValue_0: float = Conv_BoolToFloat(self.mUseBarDivider)
        ReturnValue.SetScalarParameterValue("UseBarDivider", ReturnValue_0)
    

    def SetGaugeBarPadding(self, mGaugeBarPadding: float):
        self.mGaugeBarPadding = mGaugeBarPadding
        Margin.Left = self.mGaugeBarPadding
        Margin.Top = self.mGaugeBarPadding
        Margin.Right = self.mGaugeBarPadding
        Margin.Bottom = self.mGaugeBarPadding
        ReturnValue: Ptr[OverlaySlot] = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(self.mGaugeBar)
        ReturnValue.SetPadding(Margin)
    

    def PreConstruct(self):
        ExecuteUbergraph_BPW_FluidGauge.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_FluidGauge(38)
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_FluidGauge(204)
    

    def ExecuteUbergraph_BPW_FluidGauge(self):
        # Label 10
        self.SetGaugeName(self.mGaugeName)
        # End
        self.SetGaugeBarPadding(self.mGaugeBarPadding)
        self.SetUseBarDivider(self.mUseBarDivider)
        self.SetBarColors(self.mPrimaryColor, self.mSecondaryColor)
        self.SetMeterColor(self.mMeterColor)
        self.SetupMeterTexture()
        self.UpdateGaugeValue(self.mGaugeValue)
        self.SetDividerPosition(self.mDividerPosition)
        goto('L10')
    
