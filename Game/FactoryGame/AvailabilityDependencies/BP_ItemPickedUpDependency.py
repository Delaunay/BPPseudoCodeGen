
from codegen.ue4_stub import *

from Script.Engine import Texture2D
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import GetItemName
from Script.FactoryGame import FGItemDescriptor
from Script.FactoryGame import GetBigIcon
from Script.FactoryGame import GetItems
from Script.FactoryGame import FGItemPickedUpDependency

class BP_ItemPickedUpDependency(FGItemPickedUpDependency):
    
    
    def GetDependecyData(self):
        ExecutionFlow.Push("L632")
        items: List[TSubclassOf[FGItemDescriptor]] = []
        
        self.GetItems(Ref[items])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 81
        ReturnValue: int32 = len(items)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L526')
        Variable_0 = Variable
        ExecutionFlow.Push("L558")
        
        Item = None
        Item = items[Variable_0]
        ReturnValue_1: Ptr[Texture2D] = Default__FGItemDescriptor.GetBigIcon(Item)
        ReturnValue_2: FText = Default__FGItemDescriptor.GetItemName(Item)
        FAvailabilityDependencyData.DependencyName_27_490383D6421D4A92D86E1F835769488A = ReturnValue_2
        FAvailabilityDependencyData.DependencyIcon_28_3E3B124C41C68907A6EB9FAD36C04BC4 = ReturnValue_1
        
        FAvailabilityDependencyData = None
        ReturnValue_3: int32 = localDependencyData.append(FAvailabilityDependencyData)
        goto(ExecutionFlow.Pop())
        # Label 526
        DependecyData = localDependencyData
        # End
        # Label 558
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L81')
    
