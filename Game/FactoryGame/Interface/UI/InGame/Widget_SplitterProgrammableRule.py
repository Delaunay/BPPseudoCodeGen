
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Assets.Shared.SortRule_AnyUndefined import SortRule_AnyUndefined
from Script.FactoryGame import FGWildCardDescriptor
from Script.Engine import Texture2D
from Game.FactoryGame.Interface.UI.InGame.Widget_SplitterProgrammableRule import ExecuteUbergraph_Widget_SplitterProgrammableRule.K2Node_CustomEvent_Splitter_Rule
from Game.FactoryGame.Interface.UI.InGame.Widget_SplitterProgrammableRule import ExecuteUbergraph_Widget_SplitterProgrammableRule.K2Node_Event_IsDesignTime
from Script.Engine import GreaterEqual_IntInt
from Script.UMG import PreConstruct
from Game.FactoryGame.Interface.UI.Assets.Shared.SortRule_Any import SortRule_Any
from Script.FactoryGame import SplitterSortRule
from Script.FactoryGame import GetAllDescriptorsSorted
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import GetItemName
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.InGame.Widget_SplitterProgrammableRule import ExecuteUbergraph_Widget_SplitterProgrammableRule.K2Node_ComponentBoundEvent_Index
from Game.FactoryGame.Interface.UI.InGame.Widget_SplitterProgrammableRule import ExecuteUbergraph_Widget_SplitterProgrammableRule
from Script.FactoryGame import FGOverflowDescriptor
from Game.FactoryGame.Interface.UI.InGame.Widget_SplitterProgrammableRule import ExecuteUbergraph_Widget_SplitterProgrammableRule.K2Node_ComponentBoundEvent_Text
from Script.FactoryGame import GetSmallIcon
from Script.FactoryGame import FGBuildableSplitterSmart
from Script.UMG import Construct
from Script.FactoryGame import GetNumSortRules
from Game.FactoryGame.Interface.UI.Assets.Shared.SortRule_None import SortRule_None
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.Interface.UI.InGame.Widget_SplitterProgrammableRule import ExecuteUbergraph_Widget_SplitterProgrammableRule.K2Node_ComponentBoundEvent_ListButton
from Script.UMG import UserWidget
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import FGItemDescriptor
from Script.Engine import Array_Insert
from Game.FactoryGame.Interface.UI.Assets.Shared.Rectangle_Border import Rectangle_Border
from Script.Engine import IsValidClass
from Script.FactoryGame import FGNoneDescriptor
from Script.FactoryGame import GetSortRuleAt
from Script.FactoryGame import FGAnyUndefinedDescriptor

class Widget_SplitterProgrammableRule(UserWidget):
    mAllDescriptorsSorted: List[TSubclassOf[FGItemDescriptor]]
    mSplitterSmart: Ptr[FGBuildableSplitterSmart]
    mRuleIndex: int32
    OnRemoved: FMulticastScriptDelegate
    OnUpdated: FMulticastScriptDelegate
    mCachedRule: SplitterSortRule
    mIsStaticRule: bool
    OnClicked: FMulticastScriptDelegate
    mShowDeleteButton: bool = True
    
    def ShowHideDeleteButton(self, ShowDeleteButton: bool):
        Variable: bool = ShowDeleteButton
        Variable_0: uint8 = 0
        Variable1: uint8 = 1
        
        switch = {
            False: Variable1,
            True: Variable_0
        }
        self.mDeleteContainer.SetVisibility(switch.get(Variable, None))
    

    def RemoveRule(self):
        self.OnRemoved.ProcessMulticastDelegate(self)
    

    def SetRuleOutputIndex(self, OutputIndex: int32):
        SplitterSortRule.ItemClass = self.mCachedRule.ItemClass
        SplitterSortRule.OutputIndex = OutputIndex
        self.OnUpdated.ProcessMulticastDelegate(self.mRuleIndex, SplitterSortRule)
    

    def SetRuleItemClass(self, ItemClass: TSubclassOf[FGItemDescriptor]):
        SplitterSortRule.ItemClass = ItemClass
        SplitterSortRule.OutputIndex = self.mCachedRule.OutputIndex
        self.OnUpdated.ProcessMulticastDelegate(self.mRuleIndex, SplitterSortRule)
    

    def GetSortRuleSafe(self):
        ReturnValue: bool = GreaterEqual_IntInt(self.mRuleIndex, 0)
        ReturnValue_0: int32 = self.mSplitterSmart.GetNumSortRules()
        ReturnValue_1: bool = self.mRuleIndex <= ReturnValue_0
        ReturnValue_2: bool = ReturnValue_1 and ReturnValue
        if not ReturnValue_2:
            goto('L265')
        ReturnValue_3: SplitterSortRule = self.mSplitterSmart.GetSortRuleAt(self.mRuleIndex)
        Rule = ReturnValue_3
        # End
        # Label 265
        Rule = SplitterSortRule(ItemClass = None, OutputIndex = -1)
    

    def AddButtonsForDescriptorsContaining(self, textToContain: Ref[FText]):
        pass
    

    def SetSelectedItemDescriptor(self, inDescriptor: TSubclassOf[FGItemDescriptor]):
        self.mSearchbar.SetVisibility(1)
        # Label 38
        self.SetRuleItemClass(inDescriptor)
    

    def RefreshItemClassButton(self):
        tempIconRef = Rectangle_Border
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mCachedRule.ItemClass)
        if not ReturnValue:
            goto('L335')
        Descriptor: TSubclassOf[FGOverflowDescriptor] = ClassCast[FGOverflowDescriptor](self.mCachedRule.ItemClass)
        bSuccess: bool = Descriptor
        if not bSuccess:
            goto('L447')
        tempIconRef = SortRule_AnyUndefined
        # Label 200
        ReturnValue_0: FText = Default__FGItemDescriptor.GetItemName(self.mCachedRule.ItemClass)
        self.mItemClassButton.UpdateButton(tempIconRef, ReturnValue_0, , 2, 0, )
        # End
        # Label 335
        self.mItemClassButton.UpdateButton(Rectangle_Border, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 381, 'Value': 'None Specified'}", , 2, 0, )
        # End
        # Label 447
        Descriptor_0: TSubclassOf[FGAnyUndefinedDescriptor] = ClassCast[FGAnyUndefinedDescriptor](self.mCachedRule.ItemClass)
        bSuccess3: bool = Descriptor_0
        if not bSuccess3:
            goto('L559')
        tempIconRef = SortRule_AnyUndefined
        goto('L200')
        # Label 559
        Descriptor_1: TSubclassOf[FGWildCardDescriptor] = ClassCast[FGWildCardDescriptor](self.mCachedRule.ItemClass)
        bSuccess2: bool = Descriptor_1
        if not bSuccess2:
            goto('L671')
        tempIconRef = SortRule_Any
        goto('L200')
        # Label 671
        Descriptor_2: TSubclassOf[FGNoneDescriptor] = ClassCast[FGNoneDescriptor](self.mCachedRule.ItemClass)
        bSuccess1: bool = Descriptor_2
        if not bSuccess1:
            goto('L783')
        tempIconRef = SortRule_None
        goto('L200')
        # Label 783
        ReturnValue_1: Ptr[Texture2D] = Default__FGItemDescriptor.GetSmallIcon(self.mCachedRule.ItemClass)
        tempIconRef = ReturnValue_1
        goto('L200')
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SplitterProgrammableRule(316)
    

    def BndEvt__Widget_InputBox_K2Node_ComponentBoundEvent_0_OnTextChanged__DelegateSignature(self, text: FText):
        ExecuteUbergraph_Widget_SplitterProgrammableRule.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SplitterProgrammableRule(340)
    

    def BndEvt__mDeleteButton_K2Node_ComponentBoundEvent_6_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SplitterProgrammableRule(368)
    

    def ForceRefreshButton(self, Splitter Rule: SplitterSortRule):
        ExecuteUbergraph_Widget_SplitterProgrammableRule.K2Node_CustomEvent_Splitter_Rule = Splitter Rule #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SplitterProgrammableRule(373)
    

    def BndEvt__mOtherListButton_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self, index: int32, ListButton: Ptr[Widget_ListButton]):
        ExecuteUbergraph_Widget_SplitterProgrammableRule.K2Node_ComponentBoundEvent_Index = index #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_SplitterProgrammableRule.K2Node_ComponentBoundEvent_ListButton = ListButton #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SplitterProgrammableRule(430)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_SplitterProgrammableRule.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SplitterProgrammableRule(435)
    

    def ExecuteUbergraph_Widget_SplitterProgrammableRule(self):
        # Label 10
        self.ShowHideDeleteButton(self.mShowDeleteButton)
        # End
        # Label 38
        self.RefreshItemClassButton()
        # End
        # Label 57
        self.Construct()
        
        Default__FGBlueprintFunctionLibrary.GetAllDescriptorsSorted(self.mSplitterSmart, Ref[self.mAllDescriptorsSorted])
        Variable: Const[TSubclassOf[FGItemDescriptor]] = FGWildCardDescriptor
        
        Default__KismetArrayLibrary.Array_Insert(0, Ref[self.mAllDescriptorsSorted], Ref[Variable])
        Variable1: Const[TSubclassOf[FGItemDescriptor]] = FGNoneDescriptor
        
        Default__KismetArrayLibrary.Array_Insert(0, Ref[self.mAllDescriptorsSorted], Ref[Variable1])
        
        Rule = None
        # Label 265
        self.GetSortRuleSafe(Ref[Rule])
        self.ForceRefreshButton(Rule)
        # End
        goto('L57')
        # Label 321
        self.RemoveRule()
        # Label 335
        # End
        
        Text = None
        self.AddButtonsForDescriptorsContaining(Ref[Text])
        # End
        goto('L321')
        self.mCachedRule = Rule
        goto('L38')
        # Label 405
        self.OnClicked.ProcessMulticastDelegate(self)
        # End
        goto('L405')
        self.PreConstruct(IsDesignTime)
        goto('L10')
    

    def OnClicked__DelegateSignature(self, SplitterRule: Ptr[Widget_SplitterProgrammableRule]):
        pass
    

    def OnUpdated__DelegateSignature(self, RuleIndex: int32, RuleData: SplitterSortRule):
        pass
    

    def OnRemoved__DelegateSignature(self, SplitterRule: Ptr[Widget_SplitterProgrammableRule]):
        pass
    
