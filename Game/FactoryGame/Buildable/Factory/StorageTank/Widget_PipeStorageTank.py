
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Game.FactoryGame.Buildable.Factory.StorageTank.Widget_PipeStorageTank import ExecuteUbergraph_Widget_PipeStorageTank.K2Node_ComponentBoundEvent_DrainDuration
from Script.FactoryGame import FGBuildablePipeReservoir
from Script.Engine import Delay
from Script.FactoryGame import GetFluidContent
from Script.FactoryGame import GetFluidDescriptor
from Script.FactoryGame import GetFluidContentMax
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.FactoryGame import GetFlowDrain
from Script.FactoryGame import GetItemName
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.StorageTank.Widget_PipeStorageTank import ExecuteUbergraph_Widget_PipeStorageTank.K2Node_ComponentBoundEvent_FlushNetwork
from Game.FactoryGame.Buildable.Factory.StorageTank.Widget_PipeStorageTank import ExecuteUbergraph_Widget_PipeStorageTank.K2Node_Event_MyGeometry
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Game.FactoryGame.Buildable.Factory.StorageTank.Widget_PipeStorageTank import ExecuteUbergraph_Widget_PipeStorageTank
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import Init
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import Conv_IntToString
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.FactoryGame import GetFlowLimit
from Script.FactoryGame import GetFlowFill
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import FGItemDescriptor
from Script.Engine import Round
from Game.FactoryGame.Buildable.Factory.StorageTank.Widget_PipeStorageTank import ExecuteUbergraph_Widget_PipeStorageTank.K2Node_Event_InDeltaTime
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Script.Engine import IsValidClass
from Script.Engine import Concat_StrStr
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class Widget_PipeStorageTank(Widget_UseableBase):
    mPipeResorvoir: Ptr[FGBuildablePipeReservoir]
    mUseKeyboard = True
    mUseMouse = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    bHasScriptImplementedTick = True
    
    def GetContentText(self):
        ReturnValue: float = self.mPipeResorvoir.GetFluidContent()
        ReturnValue_0: float = self.mPipeResorvoir.GetFluidContentMax()
        ReturnValue_1: int32 = Round(ReturnValue)
        ReturnValue1: int32 = Round(ReturnValue_0)
        ReturnValue_2: FString = Default__KismetStringLibrary.Conv_IntToString(ReturnValue_1)
        ReturnValue1_0: FString = Default__KismetStringLibrary.Conv_IntToString(ReturnValue1)
        ReturnValue_3: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_2, "/")
        ReturnValue1_1: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_3, ReturnValue1_0)
        ReturnValue2: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue1_1, " m³")
        ReturnValue_4: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue2)
        ReturnValue_5: FText = ReturnValue_4
    

    def GetTypeText(self):
        ReturnValue: TSubclassOf[FGItemDescriptor] = self.mPipeResorvoir.GetFluidDescriptor()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue)
        if not ReturnValue_0:
            goto('L240')
        ReturnValue = self.mPipeResorvoir.GetFluidDescriptor()
        ReturnValue_1: FText = Default__FGItemDescriptor.GetItemName(ReturnValue)
        ReturnValue_2: FText = ReturnValue_1
        goto('L299')
        # Label 240
        ReturnValue_2 = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 260, 'Value': '-'}"
    

    def Init(self):
        self.ExecuteUbergraph_Widget_PipeStorageTank(788)
    

    def BndEvt__Widget_Window_DarkMode_K2Node_ComponentBoundEvent_0_OnClose__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PipeStorageTank(960)
    

    def Tick(self):
        ExecuteUbergraph_Widget_PipeStorageTank.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_PipeStorageTank.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PipeStorageTank(975)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_PipeStorageTank(1307)
    

    def BndEvt__BPW_PipeModule_K2Node_ComponentBoundEvent_1_OnFlush__DelegateSignature(self, FlushNetwork: bool, DrainDuration: float):
        ExecuteUbergraph_Widget_PipeStorageTank.K2Node_ComponentBoundEvent_FlushNetwork = FlushNetwork #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_PipeStorageTank.K2Node_ComponentBoundEvent_DrainDuration = DrainDuration #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PipeStorageTank(1312)
    

    def ExecuteUbergraph_Widget_PipeStorageTank(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mPipeResorvoir)
        if not ReturnValue:
            goto('L168')
        ReturnValue_0: TSubclassOf[FGItemDescriptor] = self.mPipeResorvoir.GetFluidDescriptor()
        self.BPW_PipeModule.SetFluidType(ReturnValue_0)
        goto(ExecutionFlow.Pop())
        # Label 168
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 15, UUID = -1559627994, ExecutionFunction = "ExecuteUbergraph_Widget_PipeStorageTank", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 245
        Default__KismetSystemLibrary.PrintString(self, "Error: Failed to get remote call object", True, True, LinearColor(R = 1, G = 0, B = 0, A = 1), 2)
        goto(ExecutionFlow.Pop())
        # Label 361
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_1)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L245')
        ReturnValue_2: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_2)
        if not ReturnValue1:
            goto('L245')
        if not FlushNetwork:
            goto('L691')
        ReturnValue_2 = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_2.Server_FlushPipeNetwork(self.mPipeResorvoir)
        goto(ExecutionFlow.Pop())
        # Label 691
        ReturnValue_2 = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_2.Server_FlushIntegrant(self.mPipeResorvoir)
        goto(ExecutionFlow.Pop())
        self.Init()
        Reservoir: Ptr[FGBuildablePipeReservoir] = Cast[FGBuildablePipeReservoir](self.mInteractObject)
        bSuccess1: bool = Reservoir
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        self.mPipeResorvoir = Reservoir
        self.Widget_Window_DarkMode.SetTitle(self.mPipeResorvoir.mDisplayName)
        goto(ExecutionFlow.Pop())
        self.OnEscapePressed()
        goto(ExecutionFlow.Pop())
        ReturnValue_3: float = self.mPipeResorvoir.GetFlowLimit()
        ReturnValue_4: float = self.mPipeResorvoir.GetFlowFill()
        ReturnValue_5: float = self.mPipeResorvoir.GetFlowDrain()
        ReturnValue_6: float = self.mPipeResorvoir.GetFluidContentMax()
        ReturnValue_7: float = self.mPipeResorvoir.GetFluidContent()
        self.BPW_PipeModule.UpdateValues(ReturnValue_7, ReturnValue_6, ReturnValue_4, ReturnValue_5, ReturnValue_3)
        goto(ExecutionFlow.Pop())
        goto('L15')
        goto('L361')
    
