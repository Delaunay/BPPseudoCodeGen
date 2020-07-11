
from codegen.ue4_stub import *

from Script.Engine import SetScalarParameterValue
from Script.Engine import Texture2D
from Script.Engine import FClamp
from Game.FactoryGame.Interface.UI.InGame.BPW_PipeModule import ExecuteUbergraph_BPW_PipeModule.K2Node_ComponentBoundEvent_Alpha
from Script.Engine import MaterialInstanceDynamic
from Script.Engine import Not_PreBool
from Script.UMG import GetEffectMaterial
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Ease
from Script.Engine import FormatArgumentData
from Script.CoreUObject import Color
from Script.FactoryGame import GetItemName
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.InGame.BPW_PipeModule import ExecuteUbergraph_BPW_PipeModule.K2Node_Event_IsDesignTime
from Script.Engine import Conv_FloatToText
from Script.Engine import SetVectorParameterValue
from Game.FactoryGame.Interface.UI.InGame.BPW_PipeModule import ExecuteUbergraph_BPW_PipeModule.K2Node_ComponentBoundEvent_DrainDuration
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.InGame.BPW_PipeModule import ExecuteUbergraph_BPW_PipeModule
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetSmallIcon
from Script.Engine import Conv_ColorToLinearColor
from Script.Engine import Format
from Script.UMG import UserWidget
from Script.UMG import SetBrushTintColor
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import GetFluidColor
from Script.Engine import IsValidClass
from Script.CoreUObject import LinearColor

class BPW_PipeModule(UserWidget):
    OnFlush: FMulticastScriptDelegate
    mTint: LinearColor = Namespace(A=1, B=0.556863009929657, G=0.3803919851779938, R=0.10588199645280838)
    mFlushing: bool
    mFlushNetwork: bool
    mCurrentStorage: float
    mMaxFlowRate: float
    mMaxStorage: float
    mShowBorder: bool = True
    mAllowNetworkFlush: bool = True
    OnDrainCompleted: FMulticastScriptDelegate
    mStorageName: FText = NSLOCTEXT("", "7F5934234BEA0E84D7FA66897955DB9D", "Storage")
    
    def InternalUpdateValues(self, CurrentStorage: float, MaxStorage: float, FlowIn: float, FlowOut: float, MaxFlowRate: float):
        ReturnValue2: float = FlowIn * 60
        ReturnValue4: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue2, 0, False, True, 1, 324, 0, 0)
        self.mFlowInText.SetText(ReturnValue4)
        ReturnValue1: float = FlowOut * 60
        ReturnValue3: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue1, 0, False, True, 1, 324, 0, 0)
        self.mFlowOutText.SetText(ReturnValue3)
        ReturnValue: float = FlowIn - FlowOut
        ReturnValue_0: float = ReturnValue * 60
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_0, 0, False, True, 1, 324, 0, 0)
        ReturnValue_2: bool = ReturnValue_0 > 0
        FormatArgumentData.ArgumentName = "value"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_1
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Variable: bool = ReturnValue_2
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 827, 'Value': '+{value}'}", Array)
        
        switch = {
            False: ReturnValue_1,
            True: ReturnValue_3
        }
        self.mNetFlow.SetText(switch.get(Variable, None))
        ReturnValue1_0: FText = Default__KismetTextLibrary.Conv_FloatToText(MaxStorage, 0, False, True, 1, 324, 0, 1)
        self.mMaxAmountInPipe.SetText(ReturnValue1_0)
        ReturnValue_4: float = FClamp(CurrentStorage, 0, MaxStorage)
        ReturnValue2_0: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_4, 0, False, True, 1, 324, 0, 1)
        self.mCurrentAmountInPipeText.SetText(ReturnValue2_0)
        ReturnValue_5: float = CurrentStorage / MaxStorage
        self.UpdateTank(ReturnValue_5)
    

    def SetFluidType(self, fluidDescriptor: TSubclassOf[FGItemDescriptor]):
        ReturnValue: Color = Default__FGItemDescriptor.GetFluidColor(fluidDescriptor)
        ReturnValue_0: LinearColor = Conv_ColorToLinearColor(ReturnValue)
        self.SetTint(ReturnValue_0)
        ReturnValue_1: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(fluidDescriptor)
        SlateBrush.ImageSize = self.mFluidIcon.Brush.ImageSize
        SlateBrush.Margin = self.mFluidIcon.Brush.Margin
        SlateBrush.TintColor = self.mFluidIcon.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue_1
        SlateBrush.DrawAs = self.mFluidIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mFluidIcon.Brush.Tiling
        SlateBrush.Mirroring = self.mFluidIcon.Brush.Mirroring
        
        SlateBrush = None
        self.mFluidIcon.SetBrush(Ref[SlateBrush])
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 665, 'Value': 'None'}"
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValidClass(fluidDescriptor)
        Variable_0: bool = ReturnValue_2
        ReturnValue_3: FText = Default__FGItemDescriptor.GetItemName(fluidDescriptor)
        
        switch = {
            False: Variable,
            True: ReturnValue_3
        }
        self.mFluidName.SetText(switch.get(Variable_0, None))
        Variable_1: uint8 = 3
        Variable1: uint8 = 2
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValidClass(fluidDescriptor)
        Variable1_0: bool = ReturnValue1
        
        switch_0 = {
            False: Variable1,
            True: Variable_1
        }
        self.mFluidIcon.SetVisibility(switch_0.get(Variable1_0, None))
        self.BPW_FlushHandle.mFluidDescriptor = fluidDescriptor
    

    def SetTint(self, mTint: LinearColor):
        self.mTint = mTint
        SlateColor.SpecifiedColor = self.mTint
        # Label 63
        SlateColor.ColorUseRule = 0
        self.mFluidFilled.SetBrushTintColor(SlateColor)
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.mRetainBox.GetEffectMaterial()
        EffectMaterial = ReturnValue
        EffectMaterial.SetVectorParameterValue("Tint", self.mTint)
    

    def UpdateValues(self, CurrentStorage: float, MaxStorage: float, FlowIn: float, FlowOut: float, MaxFlowRate: float):
        self.mCurrentStorage = CurrentStorage
        self.mMaxStorage = MaxStorage
        self.mMaxFlowRate = MaxFlowRate
        ReturnValue: bool = Not_PreBool(self.mFlushing)
        if not ReturnValue:
            goto('L183')
        self.InternalUpdateValues(CurrentStorage, MaxStorage, FlowIn, FlowOut, MaxFlowRate)
    

    def UpdateTank(self, NewValue: float):
        mCurrentBarValue = NewValue
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.mRetainBox.GetEffectMaterial()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L837')
        ReturnValue1: Ptr[MaterialInstanceDynamic] = self.mRetainBox.GetEffectMaterial()
        EffectMaterial = ReturnValue1
        EffectMaterial.SetScalarParameterValue("FillAmount", mCurrentBarValue)
        ReturnValue_1: float = mCurrentBarValue * 2
        ReturnValue_2: float = 2 - ReturnValue_1
        ReturnValue_3: bool = ReturnValue_1 > 1
        Variable: bool = ReturnValue_3
        
        switch = {
            False: ReturnValue_1,
            True: ReturnValue_2
        }
        ReturnValue1_0: float = Ease(0, 1, switch.get(Variable, None), 12, 2, 2)
        EffectMaterial.SetScalarParameterValue("XScale", ReturnValue1_0)
        ReturnValue_1 = mCurrentBarValue * 2
        ReturnValue_2 = 2 - ReturnValue_1
        ReturnValue_3 = ReturnValue_1 > 1
        Variable = ReturnValue_3
        
        switch_0 = {
            False: ReturnValue_1,
            True: ReturnValue_2
        }
        ReturnValue_4: float = Ease(0.10000000149011612, 1, switch_0.get(Variable, None), 12, 2, 2)
        EffectMaterial.SetScalarParameterValue("YScale", ReturnValue_4)
    

    def BndEvt__BPW_FlushHandle_K2Node_ComponentBoundEvent_1_OnFlush__DelegateSignature(self, DrainDuration: float):
        ExecuteUbergraph_BPW_PipeModule.K2Node_ComponentBoundEvent_DrainDuration = DrainDuration #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_PipeModule(10)
    

    def BndEvt__mPipeNetworkButton_K2Node_ComponentBoundEvent_2_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_PipeModule(79)
    

    def BndEvt__mPipeSegmentButton_K2Node_ComponentBoundEvent_3_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_PipeModule(169)
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_PipeModule(259)
    

    def BndEvt__BPW_FlushHandle_K2Node_ComponentBoundEvent_4_OnFluidFilledUp__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_PipeModule(301)
    

    def BndEvt__BPW_FlushHandle_K2Node_ComponentBoundEvent_5_OnFluidLerp__DelegateSignature(self, Alpha: float):
        ExecuteUbergraph_BPW_PipeModule.K2Node_ComponentBoundEvent_Alpha = Alpha #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_PipeModule(306)
    

    def PreConstruct(self):
        ExecuteUbergraph_BPW_PipeModule.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_PipeModule(425)
    

    def BndEvt__BPW_FlushHandle_K2Node_ComponentBoundEvent_0_OnDrainCompleted__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_PipeModule(1031)
    

    def ExecuteUbergraph_BPW_PipeModule(self):
        self.OnFlush.ProcessMulticastDelegate(self.mFlushNetwork, DrainDuration)
        self.mFlushing = True
        # End
        # Label 63
        self.mFlushing = False
        # End
        self.mPipeNetworkButton.SetIsSelected(True)
        self.mPipeSegmentButton.SetIsSelected(False)
        self.mFlushNetwork = True
        # End
        self.mPipeNetworkButton.SetIsSelected(False)
        self.mPipeSegmentButton.SetIsSelected(True)
        self.mFlushNetwork = False
        # End
        self.mPipeSegmentButton.SetIsSelected(True)
        # End
        goto('L63')
        ReturnValue: float = Ease(self.mCurrentStorage, 0, Alpha, 4, 2, 2)
        self.InternalUpdateValues(ReturnValue, self.mMaxStorage, 0, 0, self.mMaxFlowRate)
        # End
        Variable: uint8 = 3
        Variable1: uint8 = 2
        Variable_0: bool = self.mShowBorder
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mBorder.SetVisibility(switch.get(Variable_0, None))
        ReturnValue_0: bool = Not_PreBool(self.mAllowNetworkFlush)
        self.mPipeNetworkButton.SetIsDisabled(ReturnValue_0)
        FormatArgumentData.ArgumentName = "Name"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = self.mStorageName
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 909, 'Value': 'Current amount in {Name}'}", Array)
        self.mCurrentAmountLabel.SetText(ReturnValue_1)
        # End
        self.OnDrainCompleted.ProcessMulticastDelegate()
    

    def OnDrainCompleted__DelegateSignature(self):
        pass
    

    def OnFlush__DelegateSignature(self, FlushNetwork: bool, DrainDuration: float):
        pass
    
