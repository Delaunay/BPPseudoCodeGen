
from codegen.ue4_stub import *

from Script.Engine import GetDisplayName
from Script.Engine import Default__KismetNodeHelperLibrary
from Script.FactoryGame import EIgnore
from Script.UMG import AddChildToVerticalBox
from Game.FactoryGame.Interface.UI.InGame.Widget_AggroEntry import ExecuteUbergraph_Widget_AggroEntry
from Script.Engine import GetEnumeratorUserFriendlyName
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Array_Find
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.FactoryGame import GetTargetingDesireFromAggroEntry
from Game.FactoryGame.Interface.UI.InGame.Widget_AggroEntry import ExecuteUbergraph_Widget_AggroEntry.K2Node_Event_InDeltaTime
from Script.UMG import UserWidget
from Script.Engine import Actor
from Game.FactoryGame.Interface.UI.InGame.Widget_AggroText import Widget_AggroText
from Script.UMG import VerticalBoxSlot
from Script.UMG import Create
from Game.FactoryGame.Character.Creature.Enemy.BP_EnemyController import BP_EnemyController
from Game.FactoryGame.Interface.UI.InGame.Widget_AggroEntry import ExecuteUbergraph_Widget_AggroEntry.K2Node_Event_MyGeometry

class Widget_AggroEntry(UserWidget):
    AIController: Ptr[BP_EnemyController]
    mUpdateTime: float = 0.03200000151991844
    mTimeSinceUpdate: float = 5
    mEntries: List[Ptr[Widget_AggroText]]
    
    def GetSortedAggroEntries(self, allEntries: Ref[List[AggroEntry]]):
        ExecutionFlow.Push("L978")
        maxAggro = -1
        indexToAdd = -1
        # Label 51
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 97
        ReturnValue: int32 = len(allEntries)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L669')
        Variable_0 = Variable
        ExecutionFlow.Push("L904")
        
        Item = None
        Item = allEntries[Variable_0]
        ReturnValue_1: float = self.AIController.GetTargetingDesireFromAggroEntry(Item)
        
        ReturnValue_2: int32 = Default__KismetArrayLibrary.Array_Find(Ref[indexesAdded], Ref[Variable_0])
        ReturnValue_3: bool = EqualEqual_IntInt(ReturnValue_2, -1)
        ReturnValue_4: bool = ReturnValue_1 > maxAggro
        ReturnValue_5: bool = ReturnValue_4 and ReturnValue_3
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        maxAggro = ReturnValue_1
        indexToAdd = Variable_0
        
        ReturnValue_6: int32 = indexesAdded.append(indexToAdd)
        goto(ExecutionFlow.Pop())
        # Label 669
        ReturnValue_7: bool = indexToAdd != -1
        if not ReturnValue_7:
            goto('L872')
        
        Item1 = None
        Item1 = allEntries[indexToAdd]
        
        Item1 = None
        ReturnValue1: int32 = localSortedEntries.append(Item1)
        indexToAdd = -1
        goto('L51')
        # Label 872
        sortedEntries = localSortedEntries
        # End
        # Label 904
        ReturnValue_8: int32 = Variable + 1
        Variable = ReturnValue_8
        goto('L97')
    

    def UpdateAggroList(self):
        ExecutionFlow.Push("L1268")
        Variable1: int32 = 0
        Variable: int32 = 0
        
        # Label 51
        ReturnValue1: int32 = len(self.mEntries)
        ReturnValue1_0: bool = Variable1 <= ReturnValue1
        if not ReturnValue1_0:
            goto('L314')
        Variable = Variable1
        ExecutionFlow.Push("L1194")
        
        Item1 = None
        Item1 = self.mEntries[Variable]
        Item1.text.SetText()
        goto(ExecutionFlow.Pop())
        
        self.AIController.mAggroEntries = None
        sortedEntries = None
        # Label 314
        self.GetSortedAggroEntries(Ref[self.AIController.mAggroEntries], Ref[sortedEntries])
        Variable_0: int32 = 0
        Variable1_0: int32 = 0
        
        sortedEntries = None
        # Label 414
        ReturnValue2: int32 = len(sortedEntries)
        ReturnValue2_0: bool = Variable_0 <= ReturnValue2
        if not ReturnValue2_0:
           goto(ExecutionFlow.Pop())
        Variable1_0 = Variable_0
        ExecutionFlow.Push("L1120")
        
        ReturnValue: int32 = len(self.mEntries)
        ReturnValue_0: bool = Variable1_0 <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        
        sortedEntries = None
        Item2 = None
        Item2 = sortedEntries[Variable1_0]
        localEntry = Item2
        ReturnValue_1: float = self.AIController.GetTargetingDesireFromAggroEntry(localEntry)
        ReturnValue_2: Ptr[Actor] = GetInterfaceUObject(localEntry.aggroTarget).GetActor()
        
        Item = None
        Item = self.mEntries[Variable1_0]
        ReturnValue_3: FString = Default__KismetNodeHelperLibrary.GetEnumeratorUserFriendlyName(EIgnore, localEntry.Ignore)
        ReturnValue_4: FString = Default__KismetSystemLibrary.GetDisplayName(ReturnValue_2)
        Item.SetAggroData(ReturnValue_1, ReturnValue_4, ReturnValue_3)
        goto(ExecutionFlow.Pop())
        # Label 1120
        ReturnValue_5: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_5
        goto('L414')
        # Label 1194
        ReturnValue1_1: int32 = Variable1 + 1
        Variable1 = ReturnValue1_1
        goto('L51')
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_AggroEntry(15)
    

    def Tick(self):
        ExecuteUbergraph_Widget_AggroEntry.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_AggroEntry.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_AggroEntry(366)
    

    def ExecuteUbergraph_Widget_AggroEntry(self):
        goto(ComputedJump("EntryPoint"))
        Variable: int32 = 0
        # Label 38
        ReturnValue: bool = Variable <= 4
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L292")
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[Widget_AggroText] = Default__WidgetBlueprintLibrary.Create(self, Widget_AggroText, ReturnValue_0)
        ReturnValue_2: Ptr[VerticalBoxSlot] = self.VBox.AddChildToVerticalBox(ReturnValue_1)
        
        ReturnValue_3: int32 = self.mEntries.append(ReturnValue_1)
        goto(ExecutionFlow.Pop())
        # Label 292
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L38')
        ReturnValue_5: bool = Default__KismetSystemLibrary.IsValid(self.AIController)
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        ReturnValue_6: FString = Default__KismetSystemLibrary.GetDisplayName(self.AIController)
        ReturnValue_7: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_6)
        self.text.SetText(ReturnValue_7)
        self.UpdateAggroList()
        goto(ExecutionFlow.Pop())
    
