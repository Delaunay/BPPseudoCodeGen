
from codegen.ue4_stub import *

from Script.UMG import RemoveChildAt
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ActiveSchematicContainer import ExecuteUbergraph_Widget_ActiveSchematicContainer.K2Node_CustomEvent_activeSchematic
from Script.Engine import Delay
from Script.FactoryGame import GetActiveSchematic
from Script.Engine import SetObjectPropertyByName
from Script.FactoryGame import GetCost
from Script.UMG import HorizontalBoxSlot
from Script.UMG import GetChildrenCount
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ActiveSchematicContainer import ExecuteUbergraph_Widget_ActiveSchematicContainer
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Player.BP_PlayerState import BP_PlayerState
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.UMG import SetHorizontalAlignment
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Script.UMG import ESlateVisibility
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Game.FactoryGame.Interface.UI.InGame.ShoppingList.Widget_ActiveSchematicCost import Widget_ActiveSchematicCost
from Script.Engine import Format
from Script.FactoryGame import GetTimeUntilShipReturn
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import FGSchematic
from Script.UMG import UserWidget
from Script.FactoryGame import IsShipAtTradingPost
from Script.UMG import AddChildToHorizontalBox
from Script.FactoryGame import FGSchematicManager
from Script.UMG import Create
from Script.FactoryGame import Default__FGSchematic
from Script.Engine import Min
from Script.FactoryGame import ItemAmount
from Script.FactoryGame import Default__FGSchematicManager
from Script.Engine import IsValidClass
from Script.FactoryGame import GetSchematicDisplayName
from Script.Engine import TimeSecondsToString
from Script.Engine import LocalPlayer

class Widget_ActiveSchematicContainer(UserWidget):
    mCachedActiveSchematic: TSubclassOf[FGSchematic]
    
    def GetPodTimerText(self):
        ReturnValue: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L313')
        ReturnValue = self.GetOwningLocalPlayer()
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_2: float = ReturnValue_0.GetTimeUntilShipReturn()
        ReturnValue_3: bool = ReturnValue_2 <= 0
        if not ReturnValue_3:
            goto('L338')
        # Label 313
        ReturnValue_4: FText = 
        goto('L944')
        # Label 338
        ReturnValue = self.GetOwningLocalPlayer()
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        # Label 413
        ReturnValue_2 = ReturnValue_0.GetTimeUntilShipReturn()
        ReturnValue_5: FString = Default__KismetStringLibrary.TimeSecondsToString(ReturnValue_2)
        ReturnValue_6: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_5)
        FormatArgumentData.ArgumentName = "Time"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_6
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_7: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 843, 'Value': 'Pod will return in: {Time}'}", Array)
        ReturnValue_4 = ReturnValue_7
    

    def ShowPodTimerText(self):
        ReturnValue: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L392')
        Variable: uint8 = 1
        Variable1: uint8 = 3
        ReturnValue = self.GetOwningLocalPlayer()
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_2: bool = ReturnValue_0.IsShipAtTradingPost()
        Variable_0: bool = ReturnValue_2
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_3: uint8 = switch.get(Variable_0, None)
        goto('L412')
        # Label 392
        ReturnValue_3 = 1
    

    def RemoveSchematicCostWidget(self):
        ReturnValue: int32 = self.mSchematicCostBox.GetChildrenCount()
        ReturnValue_0: int32 = ReturnValue - 1
        ReturnValue_1: int32 = Min(ReturnValue_0, 0)
        ReturnValue_2: bool = self.mSchematicCostBox.RemoveChildAt(ReturnValue_1)
    

    def AddSchematicCostWidget(self):
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[BP_PlayerState] = Cast[BP_PlayerState](ReturnValue1.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
            goto('L413')
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_ActiveSchematicCost] = Default__WidgetBlueprintLibrary.Create(self, Widget_ActiveSchematicCost, ReturnValue)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_0, "mPlayerState", State)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_0, "mActiveSchematicContainer", self)
        # Label 328
        ReturnValue_1: Ptr[HorizontalBoxSlot] = self.mSchematicCostBox.AddChildToHorizontalBox(ReturnValue_0)
        ReturnValue_1.SetHorizontalAlignment(2)
    

    def MatchWidgetWithSchematicCost(self):
        ExecutionFlow.Push("L716")
        self.mSchematicCostBox.ClearChildren()
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_1: TSubclassOf[FGSchematic] = ReturnValue_0.GetActiveSchematic()
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_1)
        if not ReturnValue_2:
            goto('L618')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_1 = ReturnValue_0.GetActiveSchematic()
        ReturnValue_3: List[ItemAmount] = Default__FGSchematic.GetCost(ReturnValue_1)
        
        ReturnValue_4: int32 = len(ReturnValue_3)
        costLength = ReturnValue_4
        Variable: int32 = 0
        # Label 508
        ReturnValue_5: int32 = costLength - 1
        ReturnValue_6: bool = Variable <= ReturnValue_5
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L642")
        self.AddSchematicCostWidget()
        goto(ExecutionFlow.Pop())
        # Label 618
        costLength = 0
        goto(ExecutionFlow.Pop())
        # Label 642
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L508')
    

    def ShowSchematicWidget(self):
        
        ShouldShow = None
        self.ShouldShowSchematic(Ref[ShouldShow])
        Variable: uint8 = 0
        Variable1: uint8 = 1
        Variable_0: bool = ShouldShow
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue = switch.get(Variable_0, None)
    

    def ShouldShowSchematic(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L474')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_2: TSubclassOf[FGSchematic] = ReturnValue_0.GetActiveSchematic()
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_2)
        if not ReturnValue_3:
            goto('L490')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_2 = ReturnValue_0.GetActiveSchematic()
        self.mCachedActiveSchematic = ReturnValue_2
        ShouldShow = True
        # End
        # Label 474
        ShouldShow = False
        # End
        # Label 490
        ShouldShow = False
    

    def GetSchematicName(self):
        
        ShouldShow = None
        self.ShouldShowSchematic(Ref[ShouldShow])
        if not ShouldShow:
            goto('L211')
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mCachedActiveSchematic)
        if not ReturnValue:
            goto('L254')
        ReturnValue_0: FText = Default__FGSchematic.GetSchematicDisplayName(self.mCachedActiveSchematic)
        self.mSchematicName.SetText(ReturnValue_0)
        # End
        # Label 211
        self.mSchematicName.SetText()
        # End
        # Label 254
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue_1)
        ReturnValue_3: TSubclassOf[FGSchematic] = ReturnValue_2.GetActiveSchematic()
        ReturnValue1: FText = Default__FGSchematic.GetSchematicDisplayName(ReturnValue_3)
        self.mSchematicName.SetText(ReturnValue1)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ActiveSchematicContainer(405)
    

    def UpdateSchematic(self, activeSchematic: TSubclassOf[FGSchematic]):
        ExecuteUbergraph_Widget_ActiveSchematicContainer.K2Node_CustomEvent_activeSchematic = activeSchematic #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ActiveSchematicContainer(410)
    

    def ExecuteUbergraph_Widget_ActiveSchematicContainer(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.GetSchematicName()
        goto(ExecutionFlow.Pop())
        # Label 30
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L328')
        OutputDelegate.BindUFunction(self, UpdateSchematic)
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_0.mOnActiveSchematicChanged.AddUnique(OutputDelegate)
        self.MatchWidgetWithSchematicCost()
        goto('L15')
        # Label 328
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 30, UUID = -964581872, ExecutionFunction = "ExecuteUbergraph_Widget_ActiveSchematicContainer", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L30')
        self.MatchWidgetWithSchematicCost()
        self.GetSchematicName()
        goto(ExecutionFlow.Pop())
    
