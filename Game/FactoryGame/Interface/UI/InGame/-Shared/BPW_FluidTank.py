
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import SetScalarParameterValue
from Game.FactoryGame.Interface.UI.InGame.-Shared.BPW_FluidTank import ExecuteUbergraph_BPW_FluidTank.K2Node_Event_IsDesignTime
from Script.UMG import SetRenderScale
from Script.CoreUObject import Vector2D
from Script.Engine import Ease
from Script.Engine import SetVectorParameterValue
from Script.Engine import IsValid
from Script.Engine import MaterialInstanceDynamic
from Script.UMG import SetColorAndOpacity
from Game.FactoryGame.Interface.UI.InGame.-Shared.BPW_FluidTank import ExecuteUbergraph_BPW_FluidTank
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor
from Script.UMG import GetEffectMaterial

class BPW_FluidTank(UserWidget):
    mFluidFilledOffset: float = 0.5350000262260437
    mTint: LinearColor = Namespace(A=1, B=0.556863009929657, G=0.3803919851779938, R=0.10588199645280838)
    mCurrentValue: float
    mAliasingDensity: float = 50
    
    def SetAliasingDensity(self, Value: float):
        self.mAliasingDensity = Value
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.mRetainBox.GetEffectMaterial()
        ReturnValue.SetScalarParameterValue("AliasingDensity", self.mAliasingDensity)
    

    def SetFluidFilledOffset(self, mFluidFilledOffset: float):
        self.mFluidFilledOffset = mFluidFilledOffset
        ReturnValue: Vector2D = Vector2D(1, self.mFluidFilledOffset)
        self.mFluidFilled.SetRenderScale(ReturnValue)
    

    def UpdateTankValue(self, Value: float):
        self.mCurrentValue = Value
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.mRetainBox.GetEffectMaterial()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L837')
        ReturnValue1: Ptr[MaterialInstanceDynamic] = self.mRetainBox.GetEffectMaterial()
        EffectMaterial = ReturnValue1
        EffectMaterial.SetScalarParameterValue("FillAmount", self.mCurrentValue)
        ReturnValue_1: float = self.mCurrentValue * 2
        ReturnValue_2: float = 2 - ReturnValue_1
        ReturnValue_3: bool = ReturnValue_1 > 1
        Variable: bool = ReturnValue_3
        
        switch = {
            False: ReturnValue_1,
            True: ReturnValue_2
        }
        ReturnValue1_0: float = Ease(0, 1, switch.get(Variable, None), 12, 2, 2)
        EffectMaterial.SetScalarParameterValue("XScale", ReturnValue1_0)
        ReturnValue_1 = self.mCurrentValue * 2
        ReturnValue_2 = 2 - ReturnValue_1
        ReturnValue_3 = ReturnValue_1 > 1
        Variable = ReturnValue_3
        
        switch_0 = {
            False: ReturnValue_1,
            True: ReturnValue_2
        }
        ReturnValue_4: float = Ease(0.10000000149011612, 1, switch_0.get(Variable, None), 12, 2, 2)
        EffectMaterial.SetScalarParameterValue("YScale", ReturnValue_4)
    

    def SetTint(self, Tint: LinearColor):
        self.mTint = Tint
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.mRetainBox.GetEffectMaterial()
        ReturnValue.SetVectorParameterValue("Tint", self.mTint)
        self.mFluidFilled.SetColorAndOpacity(self.mTint)
    

    def PreConstruct(self):
        ExecuteUbergraph_BPW_FluidTank.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_FluidTank(38)
    

    def ExecuteUbergraph_BPW_FluidTank(self):
        # Label 10
        self.SetAliasingDensity(self.mAliasingDensity)
        # End
        self.SetTint(self.mTint)
        self.SetFluidFilledOffset(self.mFluidFilledOffset)
        goto('L10')
    
