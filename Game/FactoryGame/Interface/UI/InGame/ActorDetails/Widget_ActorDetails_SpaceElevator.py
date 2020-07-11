
from codegen.ue4_stub import *

from Script.FactoryGame import FGGamePhaseManager
from Script.Engine import Delay
from Script.FactoryGame import EGamePhase
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Parent import Widget_ActorDetails_Parent
from Script.Engine import Default__KismetNodeHelperLibrary
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.FactoryGame import GetInputInventory
from Script.FactoryGame import Default__FGGamePhaseManager
from Script.Engine import LatentActionInfo
from Script.Engine import Add_ByteByte
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetBaseCostForGamePhase
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import Widget_CostSlotWrapper
from Script.FactoryGame import FGInventoryComponent
from Script.Engine import GetValidValue
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import GetCostForGamePhase
from Script.Engine import Format
from Script.FactoryGame import GetGamePhase
from Script.Engine import Conv_ByteToText
from Script.FactoryGame import GetGamePhaseName
from Script.UMG import Create
from Script.Engine import GetGameState
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_SpaceElevator import ExecuteUbergraph_Widget_ActorDetails_SpaceElevator
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Parent import Construct
from Script.FactoryGame import FGBuildableSpaceElevator

class Widget_ActorDetails_SpaceElevator(Widget_ActorDetails_Parent):
    mSpaceElevator: Ptr[FGBuildableSpaceElevator]
    mGamePhaseManager: Ptr[FGGamePhaseManager]
    
    def SetupInventory(self):
        ExecutionFlow.Push("L1249")
        ReturnValue1: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue1_0: Ptr[FGGamePhaseManager] = Default__FGGamePhaseManager.Get(ReturnValue1)
        ReturnValue1_1: uint8 = ReturnValue1_0.GetGamePhase()
        ReturnValue1_2: uint8 = Add_ByteByte(ReturnValue1_1, 1)
        ReturnValue1_3: uint8 = Default__KismetNodeHelperLibrary.GetValidValue(EGamePhase, ReturnValue1_2)
        
        ReturnValue1_0.GetBaseCostForGamePhase(ReturnValue1_3, Ref[PhaseCost])
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_0: Ptr[FGGamePhaseManager] = Default__FGGamePhaseManager.Get(ReturnValue)
        ReturnValue_1: uint8 = ReturnValue_0.GetGamePhase()
        ReturnValue_2: uint8 = Add_ByteByte(ReturnValue_1, 1)
        ReturnValue_3: uint8 = Default__KismetNodeHelperLibrary.GetValidValue(EGamePhase, ReturnValue_2)
        
        ReturnValue_0.GetCostForGamePhase(ReturnValue_3, Ref[PaidCost])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 653
        ReturnValue_4: int32 = len(PhaseCost)
        ReturnValue_5: bool = Variable <= ReturnValue_4
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L1175")
        ReturnValue_6: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_7: Ptr[Widget_CostSlotWrapper] = Default__WidgetBlueprintLibrary.Create(self, Widget_CostSlotWrapper, ReturnValue_6)
        
        Item = None
        Item = PaidCost[Variable_0]
        
        Item1 = None
        Item1 = PhaseCost[Variable_0]
        ReturnValue_8: int32 = Item1.amount - Item.amount
        ReturnValue_7.Setup CostIcon(None, Item1, None, 0, ReturnValue_8, True, False, False)
        ReturnValue_9: Ptr[PanelSlot] = self.mCostSlotContainer.AddChild(ReturnValue_7)
        goto(ExecutionFlow.Pop())
        # Label 1175
        ReturnValue_10: int32 = Variable + 1
        Variable = ReturnValue_10
        goto('L653')
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ActorDetails_SpaceElevator(214)
    

    def InitCostSlots(self):
        self.ExecuteUbergraph_Widget_ActorDetails_SpaceElevator(1461)
    

    def ExecuteUbergraph_Widget_ActorDetails_SpaceElevator(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: Ptr[FGInventoryComponent] = self.mSpaceElevator.GetInputInventory()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L137')
        self.SetupInventory()
        goto(ExecutionFlow.Pop())
        # Label 137
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 15, UUID = 1308914589, ExecutionFunction = "ExecuteUbergraph_Widget_ActorDetails_SpaceElevator", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.Construct()
        self.Widget_ActorDetails_Container.SetShowPointer(self.ShowPointer)
        Elevator: Ptr[FGBuildableSpaceElevator] = Cast[FGBuildableSpaceElevator](self.mActor)
        bSuccess: bool = Elevator
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        self.mSpaceElevator = Elevator
        self.Widget_ActorDetails_Container.SetTitle("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 400, 'Value': 'Space Elevator'}")
        self.InitCostSlots()
        ReturnValue_1: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_2: Ptr[FGGamePhaseManager] = Default__FGGamePhaseManager.Get(ReturnValue_1)
        self.mGamePhaseManager = ReturnValue_2
        ReturnValue_3: uint8 = self.mGamePhaseManager.GetGamePhase()
        ReturnValue_4: uint8 = Add_ByteByte(ReturnValue_3, 1)
        ReturnValue_5: uint8 = Default__KismetNodeHelperLibrary.GetValidValue(EGamePhase, ReturnValue_4)
        ReturnValue_6: FText = self.mGamePhaseManager.GetGamePhaseName(ReturnValue_5)
        self.mPhaseName.SetText(ReturnValue_6)
        ReturnValue1: uint8 = self.mGamePhaseManager.GetGamePhase()
        ReturnValue1_0: uint8 = Add_ByteByte(ReturnValue1, 1)
        ReturnValue1_1: uint8 = Default__KismetNodeHelperLibrary.GetValidValue(EGamePhase, ReturnValue1_0)
        ReturnValue_7: FText = Default__KismetTextLibrary.Conv_ByteToText(ReturnValue1_1)
        FormatArgumentData.ArgumentName = "PhaseInt"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_7
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_8: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1323, 'Value': 'Space Elevator Resource Delivery {PhaseInt}:'}", Array)
        self.mSpaceElevatorPhaseInt.SetText(ReturnValue_8)
        goto(ExecutionFlow.Pop())
        goto('L15')
    
