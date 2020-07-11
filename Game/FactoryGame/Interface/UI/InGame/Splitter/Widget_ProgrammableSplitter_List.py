
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Assets.Shared.SortRule_AnyUndefined import SortRule_AnyUndefined
from Script.FactoryGame import FGWildCardDescriptor
from Script.Engine import SetTextPropertyByName
from Script.Engine import Texture2D
from Script.Engine import SetObjectPropertyByName
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Game.FactoryGame.Interface.UI.InGame.Splitter.Widget_ProgrammableSplitter_List import ExecuteUbergraph_Widget_ProgrammableSplitter_List.K2Node_CustomEvent_button
from Script.FactoryGame import GetAllDescriptorsSorted
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import GetItemName
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import GetSmallIcon
from Script.FactoryGame import FGBuildableSplitterSmart
from Game.FactoryGame.Interface.UI.InGame.Splitter.Widget_ProgrammableSplitter_List import ExecuteUbergraph_Widget_ProgrammableSplitter_List.K2Node_CustomEvent_ButtonIndex
from Game.FactoryGame.Interface.UI.Assets.Shared.Reset_Icon import Reset_Icon
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ListButton import Widget_ListButton
from Game.FactoryGame.Interface.UI.Assets.Shared.SortRule_None import SortRule_None
from Script.UMG import WidgetAnimation
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.UMG import UserWidget
from Script.UMG import Create
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import FGItemDescriptor
from Script.Engine import Array_Insert
from Script.FactoryGame import FGNoneDescriptor
from Game.FactoryGame.Interface.UI.InGame.Splitter.Widget_ProgrammableSplitter_List import ExecuteUbergraph_Widget_ProgrammableSplitter_List
from Script.FactoryGame import FGAnyUndefinedDescriptor

class Widget_ProgrammableSplitter_List(UserWidget):
    FadeInList: Ptr[WidgetAnimation]
    mItemDescriptor: List[TSubclassOf[FGItemDescriptor]]
    mSmartSplitter: Ptr[FGBuildableSplitterSmart]
    mSelectedInt: int32
    mSelectedDescriptor: TSubclassOf[FGItemDescriptor]
    OnSelectionChanged: FMulticastScriptDelegate
    
    def GenerateDescriptorList(self, SmartSplitter: Ptr[FGBuildableSplitterSmart]):
        ExecutionFlow.Push("L2549")
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(SmartSplitter)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        self.mSmartSplitter = SmartSplitter
        
        Default__FGBlueprintFunctionLibrary.GetAllDescriptorsSorted(self.mSmartSplitter, Ref[self.mItemDescriptor])
        Variable2: Const[TSubclassOf[FGItemDescriptor]] = FGAnyUndefinedDescriptor
        
        Default__KismetArrayLibrary.Array_Insert(0, Ref[self.mItemDescriptor], Ref[Variable2])
        Variable1: Const[TSubclassOf[FGItemDescriptor]] = FGWildCardDescriptor
        
        Default__KismetArrayLibrary.Array_Insert(0, Ref[self.mItemDescriptor], Ref[Variable1])
        Variable: Const[TSubclassOf[FGItemDescriptor]] = FGNoneDescriptor
        
        Default__KismetArrayLibrary.Array_Insert(0, Ref[self.mItemDescriptor], Ref[Variable])
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        
        # Label 403
        ReturnValue_0: int32 = len(self.mItemDescriptor)
        ReturnValue_1: bool = Variable_0 <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable_1 = Variable_0
        ExecutionFlow.Push("L1323")
        CmpSuccess: bool = Variable_1 != 0
        if not CmpSuccess:
            goto('L1397')
        CmpSuccess = Variable_1 != 1
        if not CmpSuccess:
            goto('L1781')
        CmpSuccess = Variable_1 != 2
        if not CmpSuccess:
            goto('L2165')
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue3: Ptr[Widget_ListButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_ListButton, ReturnValue_2)
        
        Item = None
        Item = self.mItemDescriptor[Variable_1]
        ReturnValue_3: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(Item)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue3, "mIcon", ReturnValue_3)
        
        Item = None
        Item = self.mItemDescriptor[Variable_1]
        ReturnValue_4: FText = Default__FGItemDescriptor.GetItemName(Item)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue3, "mTitle", Ref[ReturnValue_4])
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue3, "mListWidget", self.mList)
        localButton = ReturnValue3
        # Label 1207
        ReturnValue_5: Ptr[PanelSlot] = self.mList.AddChild(localButton)
        OutputDelegate.BindUFunction(self, GetSelectedDescriptor)
        localButton.OnClicked.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 1323
        ReturnValue_6: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_6
        goto('L403')
        # Label 1397
        ReturnValue_7: Ptr[Widget_ListButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_ListButton, None)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_7, "mIcon", SortRule_None)
        
        Item = None
        Item = self.mItemDescriptor[Variable_1]
        ReturnValue1: FText = Default__FGItemDescriptor.GetItemName(Item)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_7, "mTitle", Ref[ReturnValue1])
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_7, "mListWidget", self.mList)
        localButton = ReturnValue_7
        goto('L1207')
        # Label 1781
        ReturnValue2: Ptr[Widget_ListButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_ListButton, None)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue2, "mIcon", Reset_Icon)
        
        Item = None
        Item = self.mItemDescriptor[Variable_1]
        ReturnValue1 = Default__FGItemDescriptor.GetItemName(Item)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue2, "mTitle", Ref[ReturnValue1])
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue2, "mListWidget", self.mList)
        localButton = ReturnValue2
        goto('L1207')
        # Label 2165
        ReturnValue1_0: Ptr[Widget_ListButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_ListButton, None)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue1_0, "mIcon", SortRule_AnyUndefined)
        
        Item = None
        Item = self.mItemDescriptor[Variable_1]
        ReturnValue1 = Default__FGItemDescriptor.GetItemName(Item)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue1_0, "mTitle", Ref[ReturnValue1])
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue1_0, "mListWidget", self.mList)
        localButton = ReturnValue1_0
        goto('L1207')
    

    def GetSelectedDescriptor(self, ButtonIndex: int32, Button: Ptr[Widget_ListButton]):
        ExecuteUbergraph_Widget_ProgrammableSplitter_List.K2Node_CustomEvent_ButtonIndex = ButtonIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ProgrammableSplitter_List.K2Node_CustomEvent_button = Button #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ProgrammableSplitter_List(43)
    

    def ExecuteUbergraph_Widget_ProgrammableSplitter_List(self):
        # Label 10
        self.OnSelectionChanged.ProcessMulticastDelegate(self.mSelectedDescriptor)
        # End
        self.mSelectedInt = ButtonIndex
        
        Item = None
        Item = self.mItemDescriptor[self.mSelectedInt]
        self.mSelectedDescriptor = Item
        goto('L10')
    

    def onSelectionChanged__DelegateSignature(self, Descriptor: TSubclassOf[FGItemDescriptor]):
        pass
    
