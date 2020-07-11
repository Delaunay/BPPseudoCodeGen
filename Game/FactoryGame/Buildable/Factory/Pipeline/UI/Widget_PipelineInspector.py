
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.Engine import Conv_TextToString
from Game.FactoryGame.Buildable.Factory.Pipeline.UI.Widget_PipelineInspector import ExecuteUbergraph_Widget_PipelineInspector.K2Node_ComponentBoundEvent_DrainDuration
from Script.Engine import Texture2D
from Script.FactoryGame import GetPipeConnection1
from Script.Engine import Delay
from Game.FactoryGame.Buildable.Factory.Pipeline.UI.Widget_PipelineInspector import ExecuteUbergraph_Widget_PipelineInspector.K2Node_Event_MyGeometry
from Script.FactoryGame import GetFluidDescriptor
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Ease
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.FactoryGame import GetConnection
from Script.FactoryGame import GetItemName
from Script.Engine import Conv_FloatToText
from Script.FactoryGame import GetIndicatorContentPct
from Script.Engine import IsValid
from Script.FactoryGame import FGPipeConnectionComponent
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Buildable.Factory.Pipeline.UI.Widget_PipelineInspector import ExecuteUbergraph_Widget_PipelineInspector
from Script.FactoryGame import GetSmallIcon
from Script.Engine import Conv_StringToText
from Script.FactoryGame import GetIndicatorFlow
from Game.FactoryGame.Buildable.Factory.Pipeline.UI.Widget_PipelineInspector import ExecuteUbergraph_Widget_PipelineInspector.K2Node_Event_InDeltaTime
from Script.FactoryGame import IsConnected
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import Init
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import GetPipeConnection0
from Script.FactoryGame import GetFluidColorLinear
from Script.FactoryGame import GetMaxContent
from Script.FactoryGame import GetFlowLimit
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.Engine import Actor
from Game.FactoryGame.Buildable.Factory.Pipeline.UI.Widget_PipelineInspector import ExecuteUbergraph_Widget_PipelineInspector.K2Node_ComponentBoundEvent_FlushNetwork
from Script.FactoryGame import Default__FGItemDescriptor
from Game.FactoryGame.Buildable.Factory.Pipeline.UI.Widget_PipelineInspector import ExecuteUbergraph_Widget_PipelineInspector.K2Node_Event_UpdateTime
from Game.FactoryGame.Buildable.Factory.Pipeline.UI.Widget_PipelineInspector import ExecuteUbergraph_Widget_PipelineInspector.K2Node_ComponentBoundEvent_DrainDuration1
from Script.FactoryGame import FGItemDescriptor
from Script.Engine import Abs
from Game.FactoryGame.Buildable.Factory.Pipeline.UI.Widget_PipelineInspector import ExecuteUbergraph_Widget_PipelineInspector.K2Node_ComponentBoundEvent_Alpha
from Script.FactoryGame import FGBuildablePipeline
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Script.FactoryGame import FGPipeConnectionComponentBase
from Script.Engine import GetOwner
from Script.Engine import Concat_StrStr
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class Widget_PipelineInspector(Widget_UseableBase):
    mCurrentPipe: Ptr[FGBuildablePipeline]
    mPipe1: Ptr[FGBuildablePipeline]
    mPipe2: Ptr[FGBuildablePipeline]
    WWiseNameConverter: List[FText] = ['NSLOCTEXT("", "E00D51984FA337273C56F79358874C55", "Crude Oil")', 'NSLOCTEXT("", "CD6B6D804FFE11259C38A4910ABD4F61", "Fuel")', 'NSLOCTEXT("", "6D040C984BC380133D1B33B554D08758", "Heavy Oil Residue")', 'NSLOCTEXT("", "AB504CB34FDC4290E236798711DB4BA4", "Water")', 'NSLOCTEXT("", "F612F35149A8DD06A1F45698B45B7067", "N/A")']
    mOutflowSmoothed: float
    mInflowSmoothed: float
    mSmoothingCounter: int32
    mCurrentBarValue: float
    mFlushNetwork: bool
    mIsFlushing: bool
    mUseKeyboard = True
    mUseMouse = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCustomTickRate = 0.019999999552965164
    mCallCustomTickOnConstruct = True
    bHasScriptImplementedTick = True
    
    def InitFluid(self):
        ReturnValue1: TSubclassOf[FGItemDescriptor] = self.mCurrentPipe.GetFluidDescriptor()
        fluidDescriptor = ReturnValue1
        ReturnValue: LinearColor = Default__FGItemDescriptor.GetFluidColorLinear(fluidDescriptor)
        self.BPW_WaterTank.SetTint(ReturnValue)
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
        ReturnValue_2: float = self.mCurrentPipe.GetMaxContent()
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_2, 0, False, True, 1, 324, 0, 1)
        self.mMaxAmountInPipe.SetText(ReturnValue_3)
        ReturnValue_4: float = self.mCurrentPipe.GetFlowLimit()
        ReturnValue_5: float = ReturnValue_4 * 60
        ReturnValue1_0: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_5, 0, False, True, 1, 324, 0, 0)
        self.mMaxFlowRateText.SetText(ReturnValue1_0)
        ReturnValue_6: TSubclassOf[FGItemDescriptor] = self.mCurrentPipe.GetFluidDescriptor()
        self.BPW_FlushHandle.mFluidDescriptor = ReturnValue_6
    

    def UpdateGauge(self, NewValue: float):
        range = 134
    

    def UpdateTank(self, mNewValue: float):
        self.mCurrentBarValue = mNewValue
        self.BPW_WaterTank.UpdateTankValue(self.mCurrentBarValue)
        ReturnValue: float = self.mCurrentPipe.GetMaxContent()
        ReturnValue_0: float = ReturnValue * self.mCurrentBarValue
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_0, 0, False, True, 1, 324, 0, 1)
        self.mCurrentAmountInPipeText.SetText(ReturnValue_1)
    

    def UpdateFlowRate(self):
        SmoothingWeight = 0.30000001192092896
        ReturnValue: float = self.mCurrentPipe.GetIndicatorFlow()
        ReturnValue_0: float = Abs(ReturnValue)
        ReturnValue_1: float = SmoothingWeight * ReturnValue_0 + 1 - SmoothingWeight * self.mOutflowSmoothed
        self.mOutflowSmoothed = ReturnValue_1
        ReturnValue_2: float = self.mOutflowSmoothed * 60
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_2, 0, False, True, 1, 324, 0, 0)
        self.mFlowRateText.SetText(ReturnValue_3)
        ReturnValue_4: float = self.mCurrentPipe.GetFlowLimit()
        ReturnValue_5: float = self.mOutflowSmoothed / ReturnValue_4
        self.mFlowRateGauge.UpdateGaugeValue(ReturnValue_5)
    

    def FormatFlow(self, Flow: float):
        ReturnValue: FText = Default__KismetTextLibrary.Conv_FloatToText(Flow, 0, False, True, 1, 324, 0, 2)
        
        ReturnValue_0: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue])
        ReturnValue_1: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_0, " m³/s")
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_1)
        text = ReturnValue_2
    

    def FormatContentPct(self, Content: float):
        ReturnValue: float = Content * 100
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue, 0, False, True, 1, 324, 0, 2)
        
        ReturnValue_1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_0])
        ReturnValue_2: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_1, " %")
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_2)
        text = ReturnValue_3
    

    def SetTexts(self):
        ExecutionFlow.Push("L1179")
        mMaxAmount = 50000
        ReturnValue: TSubclassOf[FGItemDescriptor] = self.mCurrentPipe.GetFluidDescriptor()
        ReturnValue_0: FText = Default__FGItemDescriptor.GetItemName(ReturnValue)
        self.mTypeText.SetText(ReturnValue_0)
        ExecutionFlow.Push("L616")
        ExecutionFlow.Push("L400")
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mPipe1)
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        ReturnValue2: float = self.mPipe1.GetIndicatorFlow()
        LocalFlow1 = ReturnValue2
        ReturnValue2_0: float = self.mPipe1.GetIndicatorContentPct()
        LocalContent1 = ReturnValue2_0
        goto(ExecutionFlow.Pop())
        # Label 400
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(self.mPipe1)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue1_0: float = self.mPipe1.GetIndicatorFlow()
        LocalFlow2 = ReturnValue1_0
        ReturnValue1_1: float = self.mPipe1.GetIndicatorContentPct()
        LocalFlow2 = ReturnValue1_1
        goto(ExecutionFlow.Pop())
        
        Text1 = None
        # Label 616
        self.FormatFlow(LocalFlow1, Ref[Text1])
        self.mRate1Text.SetText(Text1)
        ReturnValue_2: float = self.mCurrentPipe.GetIndicatorFlow()
        
        Text2 = None
        self.FormatFlow(ReturnValue_2, Ref[Text2])
        self.mRateText.SetText(Text2)
        
        Text = None
        self.FormatFlow(LocalFlow2, Ref[Text])
        self.mRate2Text.SetText(Text)
        
        Text1 = None
        self.FormatContentPct(LocalContent1, Ref[Text1])
        self.mContent1Text.SetText(Text1)
        ReturnValue_3: float = self.mCurrentPipe.GetIndicatorContentPct()
        
        Text2 = None
        self.FormatContentPct(ReturnValue_3, Ref[Text2])
        self.mContentText.SetText(Text2)
        
        Text = None
        self.FormatContentPct(LocalContent2, Ref[Text])
        self.mContent2Text.SetText(Text)
        goto(ExecutionFlow.Pop())
    

    def Init(self):
        self.ExecuteUbergraph_Widget_PipelineInspector(892)
    

    def BndEvt__Widget_Window_DarkMode_K2Node_ComponentBoundEvent_0_OnClose__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PipelineInspector(1698)
    

    def Tick(self):
        ExecuteUbergraph_Widget_PipelineInspector.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_PipelineInspector.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PipelineInspector(2140)
    

    def BndEvt__Button_1629_K2Node_ComponentBoundEvent_1_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PipelineInspector(2155)
    

    def OnCustomTick(self):
        ExecuteUbergraph_Widget_PipelineInspector.K2Node_Event_UpdateTime = UpdateTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PipelineInspector(2170)
    

    def BndEvt__BPW_PipeModule_K2Node_ComponentBoundEvent_2_OnFlush__DelegateSignature(self, FlushNetwork: bool, DrainDuration: float):
        ExecuteUbergraph_Widget_PipelineInspector.K2Node_ComponentBoundEvent_FlushNetwork = FlushNetwork #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_PipelineInspector.K2Node_ComponentBoundEvent_DrainDuration1 = DrainDuration #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PipelineInspector(2214)
    

    def Flush(self):
        self.ExecuteUbergraph_Widget_PipelineInspector(2229)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_PipelineInspector(2234)
    

    def BndEvt__mPipeNetworkButton_K2Node_ComponentBoundEvent_4_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PipelineInspector(2239)
    

    def BndEvt__mPipeSegmentButton_K2Node_ComponentBoundEvent_5_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PipelineInspector(2325)
    

    def BndEvt__BPW_FlushHandle_K2Node_ComponentBoundEvent_3_OnFlush__DelegateSignature(self, DrainDuration: float):
        ExecuteUbergraph_Widget_PipelineInspector.K2Node_ComponentBoundEvent_DrainDuration = DrainDuration #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PipelineInspector(2411)
    

    def BndEvt__BPW_FlushHandle_K2Node_ComponentBoundEvent_6_OnFluidLerp__DelegateSignature(self, Alpha: float):
        ExecuteUbergraph_Widget_PipelineInspector.K2Node_ComponentBoundEvent_Alpha = Alpha #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PipelineInspector(2427)
    

    def BndEvt__BPW_FlushHandle_K2Node_ComponentBoundEvent_8_OnFluidFilledUp__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PipelineInspector(2576)
    

    def ExecuteUbergraph_Widget_PipelineInspector(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Default__KismetSystemLibrary.PrintString(self, "Error: Failed to get remote call object", True, True, LinearColor(R = 1, G = 0, B = 0, A = 1), 2)
        goto(ExecutionFlow.Pop())
        # Label 131
        ReturnValue3: bool = Default__KismetSystemLibrary.IsValid(self.mCurrentPipe)
        if not ReturnValue3:
            goto('L248')
        self.InitFluid()
        self.mPipeSegmentButton.SetIsSelected(True)
        goto(ExecutionFlow.Pop())
        # Label 248
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 131, UUID = -1295696372, ExecutionFunction = "ExecuteUbergraph_Widget_PipelineInspector", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 325
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L641')
        ReturnValue_0: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue1:
            goto('L641')
        ReturnValue_0 = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_0.Server_FlushPipeNetwork(self.mCurrentPipe)
        goto(ExecutionFlow.Pop())
        # Label 641
        Default__KismetSystemLibrary.PrintString(self, "Error: Failed to get remote call object", True, True, LinearColor(R = 1, G = 0, B = 0, A = 1), 2)
        goto(ExecutionFlow.Pop())
        # Label 757
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(self.mCurrentPipe)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: float = self.mCurrentPipe.GetIndicatorContentPct()
        self.UpdateTank(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        self.Init()
        Pipeline: Ptr[FGBuildablePipeline] = Cast[FGBuildablePipeline](self.mInteractObject)
        bSuccess1: bool = Pipeline
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        self.mCurrentPipe = Pipeline
        self.Widget_Window_DarkMode.SetTitle(self.mCurrentPipe.mDisplayName)
        ExecutionFlow.Push("L1383")
        ReturnValue_3: Ptr[FGPipeConnectionComponent] = self.mCurrentPipe.GetPipeConnection0()
        ReturnValue_4: bool = ReturnValue_3.IsConnected()
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        ReturnValue_3 = self.mCurrentPipe.GetPipeConnection0()
        ReturnValue_5: Ptr[FGPipeConnectionComponentBase] = ReturnValue_3.GetConnection()
        ReturnValue_6: Ptr[Actor] = ReturnValue_5.GetOwner()
        Pipeline1: Ptr[FGBuildablePipeline] = Cast[FGBuildablePipeline](ReturnValue_6)
        bSuccess2: bool = Pipeline1
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        self.mPipe1 = Pipeline1
        goto(ExecutionFlow.Pop())
        # Label 1383
        ReturnValue_7: Ptr[FGPipeConnectionComponent] = self.mCurrentPipe.GetPipeConnection1()
        ReturnValue1_0: bool = ReturnValue_7.IsConnected()
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        ReturnValue_7 = self.mCurrentPipe.GetPipeConnection1()
        ReturnValue1_1: Ptr[FGPipeConnectionComponentBase] = ReturnValue_7.GetConnection()
        ReturnValue1_2: Ptr[Actor] = ReturnValue1_1.GetOwner()
        Pipeline2: Ptr[FGBuildablePipeline] = Cast[FGBuildablePipeline](ReturnValue1_2)
        bSuccess3: bool = Pipeline2
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        self.mPipe2 = Pipeline2
        goto(ExecutionFlow.Pop())
        self.OnEscapePressed()
        goto(ExecutionFlow.Pop())
        # Label 1713
        ReturnValue1_3: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller1: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue1_3)
        bSuccess4: bool = Controller1
        if not bSuccess4:
            goto('L15')
        ReturnValue1_4: Ptr[BP_RemoteCallObject] = Controller1.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_4)
        if not ReturnValue2:
            goto('L15')
        if not self.mFlushNetwork:
            goto('L2043')
        ReturnValue1_4 = Controller1.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue1_4.Server_FlushPipeNetwork(self.mCurrentPipe)
        goto(ExecutionFlow.Pop())
        # Label 2043
        ReturnValue1_4 = Controller1.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue1_4.Server_FlushIntegrant(self.mCurrentPipe)
        goto(ExecutionFlow.Pop())
        self.UpdateFlowRate()
        goto(ExecutionFlow.Pop())
        self.Flush()
        goto(ExecutionFlow.Pop())
        ReturnValue_8: bool = Not_PreBool(self.mIsFlushing)
        if not ReturnValue_8:
           goto(ExecutionFlow.Pop())
        goto('L757')
        self.Flush()
        goto(ExecutionFlow.Pop())
        goto('L325')
        goto('L131')
        self.mPipeNetworkButton.SetIsSelected(True)
        self.mPipeSegmentButton.SetIsSelected(False)
        self.mFlushNetwork = True
        goto(ExecutionFlow.Pop())
        self.mPipeNetworkButton.SetIsSelected(False)
        self.mPipeSegmentButton.SetIsSelected(True)
        self.mFlushNetwork = False
        goto(ExecutionFlow.Pop())
        self.mIsFlushing = True
        goto('L1713')
        ReturnValue1_5: float = self.mCurrentPipe.GetIndicatorContentPct()
        ReturnValue_9: float = Ease(ReturnValue1_5, 0, Alpha, 4, 2, 2)
        self.UpdateTank(ReturnValue_9)
        goto(ExecutionFlow.Pop())
        # Label 2564
        self.mIsFlushing = False
        goto(ExecutionFlow.Pop())
        goto('L2564')
    
