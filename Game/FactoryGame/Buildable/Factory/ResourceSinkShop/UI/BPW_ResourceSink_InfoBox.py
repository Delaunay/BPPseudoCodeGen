
from codegen.ue4_stub import *

from Game.FactoryGame.Unlocks.BPI_UnlockableInterface import BPI_UnlockableInterface
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import PlayAnimation
from Script.FactoryGame import FGUnlock
from Script.CoreUObject import Object
from Script.FactoryGame import GetUnlocks
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import AddChildToWrapBox
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSink_InfoBox import ExecuteUbergraph_BPW_ResourceSink_InfoBox
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_ResourceSink_InfoBox import ExecuteUbergraph_BPW_ResourceSink_InfoBox.K2Node_Event_IsDesignTime
from Script.FactoryGame import FGSchematic
from Script.UMG import WidgetAnimation
from Script.UMG import WrapBoxSlot
from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Script.FactoryGame import Default__FGSchematic
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_Reward_Card import BPW_Reward_Card
from Script.Engine import Array_Clear

class BPW_ResourceSink_InfoBox(UserWidget):
    ContentAnim: Ptr[WidgetAnimation]
    mTitleText: FText
    mPreviewIconTexture: Ptr[Object]
    mHoveredSchematic: TSubclassOf[FGSchematic]
    
    def UpdateTooltipInfo(self, schematic: TSubclassOf[FGSchematic]):
        ExecutionFlow.Push("L1231")
        localSchematic = schematic
        self.mContentContainer.ClearChildren()
        Variable: int32 = 0
        Variable1: int32 = 0
        # Label 106
        ReturnValue: List[Ptr[FGUnlock]] = Default__FGSchematic.GetUnlocks(self.mHoveredSchematic)
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable1 = Variable
        ExecutionFlow.Push("L1037")
        ReturnValue = Default__FGSchematic.GetUnlocks(self.mHoveredSchematic)
        
        Item = None
        Item = ReturnValue[Variable1]
        Interface: TScriptInterface[BPI_UnlockableInterface] = QueryInterface[BPI_UnlockableInterface](Item)
        bSuccess: bool = Interface
        if not bSuccess:
            goto('L1111')
        
        UnlockDataStruct = None
        GetInterfaceUObject(Interface).GetUnlockDataStruct(Ref[UnlockDataStruct])
        # Label 547
        Variable1_0: int32 = 0
        Variable_0: int32 = 0
        
        UnlockDataStruct = None
        # Label 593
        ReturnValue1: int32 = len(UnlockDataStruct)
        ReturnValue1_0: bool = Variable1_0 <= ReturnValue1
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable1_0
        ExecutionFlow.Push("L1157")
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_3: Ptr[BPW_Reward_Card] = Default__WidgetBlueprintLibrary.Create(self, BPW_Reward_Card, ReturnValue_2)
        
        UnlockDataStruct = None
        Item1 = None
        Item1 = UnlockDataStruct[Variable_0]
        
        Item1 = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_3, "mUnlockDataStruct", Ref[Item1])
        ReturnValue_4: Ptr[WrapBoxSlot] = self.mContentContainer.AddChildToWrapBox(ReturnValue_3)
        ReturnValue_5: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ContentAnim, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 1037
        ReturnValue_6: int32 = Variable + 1
        Variable = ReturnValue_6
        goto('L106')
        
        UnlockDataStruct = None
        # Label 1111
        Default__KismetArrayLibrary.Array_Clear(Ref[UnlockDataStruct])
        goto('L547')
        # Label 1157
        ReturnValue1_1: int32 = Variable1_0 + 1
        Variable1_0 = ReturnValue1_1
        goto('L593')
    

    def PreConstruct(self):
        ExecuteUbergraph_BPW_ResourceSink_InfoBox.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ResourceSink_InfoBox(10)
    

    def ExecuteUbergraph_BPW_ResourceSink_InfoBox(self):
        pass
    
