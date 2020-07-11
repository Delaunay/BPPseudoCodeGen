
from codegen.ue4_stub import *

from Script.UMG import UserWidget
from Script.Engine import Texture2D
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import GetItemName
from Game.FactoryGame.Interface.UI.InGame.BPW_FluidModule import ExecuteUbergraph_BPW_FluidModule.K2Node_Event_IsDesignTime
from Script.Engine import Conv_FloatToText
from Script.Engine import TimerHandle
from Game.FactoryGame.Interface.UI.InGame.BPW_FluidModule import ExecuteUbergraph_BPW_FluidModule
from Script.FactoryGame import GetFluidColorLinear
from Script.Engine import Default__KismetTextLibrary
from Script.CoreUObject import LinearColor
from Script.FactoryGame import GetSmallIcon

class BPW_FluidModule(UserWidget):
    mLerpTimer: TimerHandle
    mBarUpdateTimer: TimerHandle
    mTint: LinearColor = Namespace(A=1, B=0.556863009929657, G=0.3803919851779938, R=0.10588199645280838)
    
    def SetFluidType(self, fluidDescriptor: TSubclassOf[FGItemDescriptor]):
        ReturnValue: LinearColor = Default__FGItemDescriptor.GetFluidColorLinear(fluidDescriptor)
        self.BPW_FluidTank.SetTint(ReturnValue)
        ReturnValue_0: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(fluidDescriptor)
        SlateBrush.ImageSize = self.mFluidIcon.Brush.ImageSize
        SlateBrush.Margin = self.mFluidIcon.Brush.Margin
        SlateBrush.TintColor = self.mFluidIcon.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue_0
        SlateBrush.DrawAs = self.mFluidIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mFluidIcon.Brush.Tiling
        SlateBrush.Mirroring = self.mFluidIcon.Brush.Mirroring
        
        SlateBrush = None
        self.mFluidIcon.SetBrush(Ref[SlateBrush])
        ReturnValue_1: FText = Default__FGItemDescriptor.GetItemName(fluidDescriptor)
        self.mFluidName.SetText(ReturnValue_1)
    

    def UpdateValues(self, MaxAmount: float, CurrentAmount: float, ConsumptionValue: float):
        ReturnValue: float = ConsumptionValue * 60
        ReturnValue2: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue, 0, False, True, 1, 324, 0, 0)
        self.mConsumptionValue.SetText(ReturnValue2)
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_FloatToText(CurrentAmount, 0, False, True, 1, 324, 0, 1)
        self.mCurrentAmountInPipeText.SetText(ReturnValue1)
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_FloatToText(MaxAmount, 0, False, True, 1, 324, 0, 0)
        self.mMaxAmountInPipe.SetText(ReturnValue_0)
        ReturnValue_1: float = CurrentAmount / MaxAmount
        self.BPW_FluidTank.UpdateTankValue(ReturnValue_1)
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_FluidModule(15)
    

    def PreConstruct(self):
        ExecuteUbergraph_BPW_FluidModule.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_FluidModule(10)
    

    def ExecuteUbergraph_BPW_FluidModule(self):
        # End
    
