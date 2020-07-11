
from codegen.ue4_stub import *

from Script.Engine import Delay
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_SplitterProgrammable import ExecuteUbergraph_Widget_SplitterProgrammable.K2Node_CustomEvent_SelectedDescriptor
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import PreConstruct
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_SplitterSmart import Widget_SplitterSmart
from Script.Engine import SetObjectPropertyByName
from Script.UMG import GetChildrenCount
from Script.UMG import PanelSlot
from Game.FactoryGame.Interface.UI.InGame.Widget_SplitterProgrammableRule import Widget_SplitterProgrammableRule
from Script.UMG import AddChild
from Script.Engine import Not_PreBool
from Script.FactoryGame import SplitterSortRule
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_SplitterProgrammable import ExecuteUbergraph_Widget_SplitterProgrammable.K2Node_CustomEvent_SplitterRule1
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_SplitterProgrammable import ExecuteUbergraph_Widget_SplitterProgrammable.K2Node_Event_IsDesignTime
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Interface.UI.InGame.Widget_Splitter_OutputList import Widget_Splitter_OutputList
from Script.FactoryGame import FGBuildableFactory
from Script.Engine import SetBoolPropertyByName
from Script.FactoryGame import FGBuildableSplitterSmart
from Script.FactoryGame import GetMaxNumSortRules
from Script.FactoryGame import GetNumSortRules
from Script.UMG import Widget
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.Engine import SetIntPropertyByName
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_SplitterProgrammable import ExecuteUbergraph_Widget_SplitterProgrammable.K2Node_CustomEvent_RuleData1
from Script.Engine import NotEqual_ObjectObject
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_SplitterProgrammable import ExecuteUbergraph_Widget_SplitterProgrammable.K2Node_CustomEvent_RuleData
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_SplitterProgrammable import ExecuteUbergraph_Widget_SplitterProgrammable.K2Node_CustomEvent_SplitterRule
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_SplitterProgrammable import ExecuteUbergraph_Widget_SplitterProgrammable.K2Node_CustomEvent_RuleIndex
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_SplitterProgrammable import ExecuteUbergraph_Widget_SplitterProgrammable
from Script.UMG import Create
from Script.FactoryGame import AddPopupWithCloseDelegate
from Script.FactoryGame import GetSortRuleAt
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class Widget_SplitterProgrammable(Widget_UseableBase):
    mSplitterSmart: Ptr[FGBuildableSplitterSmart]
    mDefaultRule: SplitterSortRule = Namespace(ItemClass='None', OutputIndex=1)
    mActiveRule: Ptr[Widget_SplitterProgrammableRule]
    mIsSmartSplitter: bool
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mUseGamepadCursor = True
    mCallCustomTickOnConstruct = True
    
    def DeslectAllRules(self):
        ExecutionFlow.Push("L849")
        Variable: int32 = 0
        # Label 28
        ReturnValue: int32 = self.mContainer.GetChildrenCount()
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L701")
        ReturnValue_1: Ptr[Widget] = self.mContainer.GetChildAt(Variable)
        List: Ptr[Widget_Splitter_OutputList] = Cast[Widget_Splitter_OutputList](ReturnValue_1)
        bSuccess: bool = List
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Variable1: int32 = 0
        # Label 280
        ReturnValue1: int32 = List.mOutputContainer.GetChildrenCount()
        ReturnValue1_0: bool = Variable1 <= ReturnValue1
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L775")
        ReturnValue1_1: Ptr[Widget] = List.mOutputContainer.GetChildAt(Variable1)
        Rule: Ptr[Widget_SplitterProgrammableRule] = Cast[Widget_SplitterProgrammableRule](ReturnValue1_1)
        bSuccess1: bool = Rule
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: bool = NotEqual_ObjectObject(Rule.mItemClassButton, self.mActiveRule.mItemClassButton)
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        Rule.mItemClassButton.mIsSelected = False
        goto(ExecutionFlow.Pop())
        # Label 701
        ReturnValue_3: int32 = Variable + 1
        # Label 743
        Variable = ReturnValue_3
        goto('L28')
        # Label 775
        ReturnValue1_2: int32 = Variable1 + 1
        Variable1 = ReturnValue1_2
        goto('L280')
    

    def SetAddButtonVisibility(self):
        ExecutionFlow.Push("L406")
        Variable: int32 = 0
        # Label 28
        ReturnValue: int32 = self.mContainer.GetChildrenCount()
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L332")
        ReturnValue_1: Ptr[Widget] = self.mContainer.GetChildAt(Variable)
        List: Ptr[Widget_Splitter_OutputList] = Cast[Widget_Splitter_OutputList](ReturnValue_1)
        bSuccess: bool = List
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: bool = Not_PreBool(self.mIsSmartSplitter)
        List.ShowHideAddButton(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 332
        ReturnValue_3: int32 = Variable + 1
        # Label 374
        Variable = ReturnValue_3
        goto('L28')
    

    def CheckIfSmartSplitter(self):
        Smart: Ptr[Widget_SplitterSmart] = Cast[Widget_SplitterSmart](self)
        # Label 28
        bSuccess: bool = Smart
        if not bSuccess:
            goto('L87')
        self.mIsSmartSplitter = True
        # End
        # Label 87
        self.mIsSmartSplitter = False
    

    def GetLastRuleIndex(self):
        ReturnValue: int32 = self.mSplitterSmart.GetNumSortRules()
        ReturnValue_0: int32 = ReturnValue - 1
        ReturnValue_1: int32 = ReturnValue_0
    

    def UpdateRuleIndexes(self):
        ExecutionFlow.Push("L1974")
        Variable1: int32 = 0
        # Label 28
        ReturnValue1: int32 = self.mCenterOutputList.mOutputContainer.GetChildrenCount()
        ReturnValue: bool = Variable1 <= ReturnValue1
        if not ReturnValue:
            goto('L374')
        ExecutionFlow.Push("L1752")
        ReturnValue_0: Ptr[Widget] = self.mCenterOutputList.mOutputContainer.GetChildAt(Variable1)
        Rule: Ptr[Widget_SplitterProgrammableRule] = Cast[Widget_SplitterProgrammableRule](ReturnValue_0)
        bSuccess: bool = Rule
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        
        ReturnValue2: int32 = LocalListOfRuleWidgets.append(Rule)
        goto(ExecutionFlow.Pop())
        # Label 374
        Variable: int32 = 0
        # Label 397
        ReturnValue2_0: int32 = self.mLeftOutputList.mOutputContainer.GetChildrenCount()
        ReturnValue1_0: bool = Variable <= ReturnValue2_0
        if not ReturnValue1_0:
            goto('L743')
        ExecutionFlow.Push("L1826")
        ReturnValue1_1: Ptr[Widget] = self.mLeftOutputList.mOutputContainer.GetChildAt(Variable)
        Rule1: Ptr[Widget_SplitterProgrammableRule] = Cast[Widget_SplitterProgrammableRule](ReturnValue1_1)
        bSuccess1: bool = Rule1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        
        ReturnValue1_2: int32 = LocalListOfRuleWidgets.append(Rule1)
        goto(ExecutionFlow.Pop())
        # Label 743
        Variable2: int32 = 0
        # Label 766
        ReturnValue_1: int32 = self.mRightOutputList.mOutputContainer.GetChildrenCount()
        ReturnValue2_1: bool = Variable2 <= ReturnValue_1
        if not ReturnValue2_1:
            goto('L1112')
        ExecutionFlow.Push("L1900")
        ReturnValue2_2: Ptr[Widget] = self.mRightOutputList.mOutputContainer.GetChildAt(Variable2)
        Rule2: Ptr[Widget_SplitterProgrammableRule] = Cast[Widget_SplitterProgrammableRule](ReturnValue2_2)
        bSuccess2: bool = Rule2
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        
        ReturnValue_2: int32 = LocalListOfRuleWidgets.append(Rule2)
        goto(ExecutionFlow.Pop())
        # Label 1112
        Variable3: int32 = 0
        # Label 1135
        ReturnValue_3: int32 = self.mSplitterSmart.GetNumSortRules()
        ReturnValue_4: int32 = ReturnValue_3 - 1
        ReturnValue3: bool = Variable3 <= ReturnValue_4
        if not ReturnValue3:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1678")
        
        Item = None
        Item = LocalListOfRuleWidgets[Variable3]
        LocalRule = Item
        LocalRule.mRuleIndex = Variable3
        ReturnValue_5: SplitterSortRule = self.mSplitterSmart.GetSortRuleAt(LocalRule.mRuleIndex)
        LocalRule.SetRuleItemClass(ReturnValue_5.ItemClass)
        ReturnValue_5 = self.mSplitterSmart.GetSortRuleAt(LocalRule.mRuleIndex)
        LocalRule.SetRuleOutputIndex(ReturnValue_5.OutputIndex)
        goto(ExecutionFlow.Pop())
        # Label 1678
        ReturnValue3_0: int32 = Variable3 + 1
        Variable3 = ReturnValue3_0
        goto('L1135')
        # Label 1752
        ReturnValue1_3: int32 = Variable1 + 1
        Variable1 = ReturnValue1_3
        goto('L28')
        # Label 1826
        ReturnValue_6: int32 = Variable + 1
        Variable = ReturnValue_6
        goto('L397')
        # Label 1900
        ReturnValue2_3: int32 = Variable2 + 1
        Variable2 = ReturnValue2_3
        goto('L766')
    

    def GenerateRules(self):
        ExecutionFlow.Push("L753")
        Variable: int32 = 0
        # Label 28
        ReturnValue: int32 = self.GetNumSortRules()
        ReturnValue_0: int32 = ReturnValue - 1
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L679")
        LocalIndex = Variable
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_3: Ptr[Widget_SplitterProgrammableRule] = Default__WidgetBlueprintLibrary.Create(self, Widget_SplitterProgrammableRule, ReturnValue_2)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_3, "mSplitterSmart", self.mSplitterSmart)
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_3, "mRuleIndex", LocalIndex)
        ReturnValue_4: bool = Not_PreBool(self.mIsSmartSplitter)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_3, "mShowDeleteButton", ReturnValue_4)
        LocalSplitterRule = ReturnValue_3
        ReturnValue_5: SplitterSortRule = self.mSplitterSmart.GetSortRuleAt(LocalIndex)
        
        List = None
        self.GetOutputFromIndex(ReturnValue_5.OutputIndex, Ref[List])
        ReturnValue_6: Ptr[PanelSlot] = List.AddChild(LocalSplitterRule)
        
        self.SetSortRuleWidgetBindings(Ref[LocalSplitterRule])
        goto(ExecutionFlow.Pop())
        # Label 679
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L28')
    

    def GetOutputFromIndex(self, index: int32):
        CmpSuccess: bool = index != 0
        if not CmpSuccess:
            goto('L149')
        CmpSuccess = index != 1
        if not CmpSuccess:
            goto('L214')
        CmpSuccess = index != 2
        if not CmpSuccess:
            goto('L260')
        # End
        # Label 149
        LocalList = self.mCenterOutputList.mOutputContainer
        # Label 190
        List = LocalList
        # End
        # Label 214
        LocalList = self.mRightOutputList.mOutputContainer
        goto('L190')
        # Label 260
        LocalList = self.mLeftOutputList.mOutputContainer
        goto('L190')
    

    def AddRuleToOutput(self, SplitterSortRule: Const[Ref[SplitterSortRule]], RuleIndex: int32):
        ReturnValue: int32 = self.mSplitterSmart.GetNumSortRules()
        ReturnValue_0: int32 = self.mSplitterSmart.GetMaxNumSortRules()
        ReturnValue_1: bool = ReturnValue <= ReturnValue_0
        if not ReturnValue_1:
            goto('L502')
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Widget_SplitterProgrammableRule] = Default__WidgetBlueprintLibrary.Create(self, Widget_SplitterProgrammableRule, ReturnValue1)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mSplitterSmart", self.mSplitterSmart)
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_2, "mRuleIndex", RuleIndex)
        LocalSplitterRule = ReturnValue_2
        
        List = None
        self.GetOutputFromIndex(SplitterSortRule.OutputIndex, Ref[List])
        ReturnValue_3: Ptr[PanelSlot] = List.AddChild(LocalSplitterRule)
        
        self.SetSortRuleWidgetBindings(Ref[LocalSplitterRule])
        # End
        # Label 502
        Default__KismetSystemLibrary.PrintString(self, "maximum rules reached", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        
        Variable = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue_4, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 665, 'Value': 'Maximum Amount Reached'}", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 727, 'Value': "You've reached the maximum amount of rules. Remove some rules or change out the rules to continue."}", 0, None, None, Ref[Variable])
    

    def SetWindowTitle(self):
        Factory: Ptr[FGBuildableFactory] = Cast[FGBuildableFactory](self.mInteractObject)
        bSuccess: bool = Factory
        self.Widget_Window_DarkMode.SetTitle(Factory.mDisplayName)
    

    def SetSortRuleWidgetBindings(self, Widget: Ref[Ptr[Widget_SplitterProgrammableRule]]):
        OutputDelegate2.BindUFunction(self, OnRuleRemoved)
        Widget.OnRemoved.AddUnique(OutputDelegate2)
        OutputDelegate1.BindUFunction(self, OnRuleUpdated)
        # Label 87
        Widget.OnUpdated.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, ShowDescriptors)
        Widget.OnClicked.AddUnique(OutputDelegate)
    

    def GetNumSortRules(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mSplitterSmart)
        if not ReturnValue:
            goto('L147')
        ReturnValue_0: int32 = self.mSplitterSmart.GetNumSortRules()
        ReturnValue_1: int32 = ReturnValue_0
        goto('L170')
        # Label 147
        ReturnValue_1 = 0
    

    def InitWindow(self):
        self.Widget_Window_DarkMode.SetTitle(self.mSplitterSmart.mDisplayName)
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
    

    def OnRuleRemoved(self, SplitterRule: Ptr[Widget_SplitterProgrammableRule]):
        ExecuteUbergraph_Widget_SplitterProgrammable.K2Node_CustomEvent_SplitterRule1 = SplitterRule #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SplitterProgrammable(2193)
    

    def OnRuleUpdated(self, RuleIndex: int32, RuleData: SplitterSortRule):
        ExecuteUbergraph_Widget_SplitterProgrammable.K2Node_CustomEvent_RuleIndex = RuleIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_SplitterProgrammable.K2Node_CustomEvent_RuleData1 = RuleData #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SplitterProgrammable(2188)
    

    def OnRuleAdded(self, RuleData: SplitterSortRule):
        ExecuteUbergraph_Widget_SplitterProgrammable.K2Node_CustomEvent_RuleData = RuleData #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SplitterProgrammable(2027)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_SplitterProgrammable.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SplitterProgrammable(616)
    

    def ShowDescriptors(self, SplitterRule: Ptr[Widget_SplitterProgrammableRule]):
        ExecuteUbergraph_Widget_SplitterProgrammable.K2Node_CustomEvent_SplitterRule = SplitterRule #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SplitterProgrammable(1158)
    

    def HideDescriptors(self):
        self.ExecuteUbergraph_Widget_SplitterProgrammable(1387)
    

    def UpdateRuleFromDescriptorList(self, SelectedDescriptor: TSubclassOf[FGItemDescriptor]):
        ExecuteUbergraph_Widget_SplitterProgrammable.K2Node_CustomEvent_SelectedDescriptor = SelectedDescriptor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SplitterProgrammable(1565)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SplitterProgrammable(2234)
    

    def UpdateListFromServer(self):
        self.ExecuteUbergraph_Widget_SplitterProgrammable(2239)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_SplitterProgrammable(2340)
    

    def BndEvt__mLeftOutputList_K2Node_ComponentBoundEvent_0_OnAddClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SplitterProgrammable(2373)
    

    def BndEvt__mCenterOutputList_K2Node_ComponentBoundEvent_1_OnAddClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SplitterProgrammable(2378)
    

    def BndEvt__mRightOutputList_K2Node_ComponentBoundEvent_2_OnAddClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SplitterProgrammable(15)
    

    def ExecuteUbergraph_Widget_SplitterProgrammable(self):
        goto(ComputedJump("EntryPoint"))
        SplitterSortRule2.ItemClass = None
        SplitterSortRule2.OutputIndex = 1
        self.OnRuleAdded(SplitterSortRule2)
        SplitterSortRule2.ItemClass = None
        SplitterSortRule2.OutputIndex = 1
        ReturnValue2: int32 = self.GetLastRuleIndex()
        
        SplitterSortRule2 = None
        self.AddRuleToOutput(ReturnValue2, Ref[SplitterSortRule2])
        goto(ExecutionFlow.Pop())
        self.UpdateRuleIndexes()
        goto(ExecutionFlow.Pop())
        self.Widget_ProgrammableSplitter_List.SetVisibility(2)
        # Label 260
        goto(ExecutionFlow.Pop())
        
        RCO = None
        # Label 261
        self.GetDefaultRCO(Ref[RCO])
        RCO.Server_AddSortRule(self.mSplitterSmart, RuleData)
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 207, UUID = -1611680896, ExecutionFunction = "ExecuteUbergraph_Widget_SplitterProgrammable", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        
        RCO1 = None
        # Label 415
        self.GetDefaultRCO(Ref[RCO1])
        RCO1.Server_RemoveSortRule(self.mSplitterSmart, SplitterRule1.mRuleIndex)
        self.UpdateRuleIndexes()
        goto(ExecutionFlow.Pop())
        
        RCO2 = None
        # Label 529
        self.GetDefaultRCO(Ref[RCO2])
        RCO2.Server_UpdateSortRule(self.mSplitterSmart, RuleIndex, RuleData1)
        goto(ExecutionFlow.Pop())
        self.PreConstruct(IsDesignTime)
        self.SetWindowTitle()
        goto(ExecutionFlow.Pop())
        # Label 650
        SplitterSortRule.ItemClass = None
        SplitterSortRule.OutputIndex = 2
        self.OnRuleAdded(SplitterSortRule)
        SplitterSortRule.ItemClass = None
        SplitterSortRule.OutputIndex = 2
        ReturnValue: int32 = self.GetLastRuleIndex()
        
        SplitterSortRule = None
        self.AddRuleToOutput(ReturnValue, Ref[SplitterSortRule])
        goto(ExecutionFlow.Pop())
        # Label 842
        SplitterSortRule1.ItemClass = None
        SplitterSortRule1.OutputIndex = 0
        self.OnRuleAdded(SplitterSortRule1)
        SplitterSortRule1.ItemClass = None
        SplitterSortRule1.OutputIndex = 0
        ReturnValue1: int32 = self.GetLastRuleIndex()
        
        SplitterSortRule1 = None
        self.AddRuleToOutput(ReturnValue1, Ref[SplitterSortRule1])
        goto(ExecutionFlow.Pop())
        # Label 1034
        self.GenerateRules()
        self.Widget_ProgrammableSplitter_List.GenerateDescriptorList(self.mSplitterSmart)
        OutputDelegate.BindUFunction(self, UpdateRuleFromDescriptorList)
        self.Widget_ProgrammableSplitter_List.OnSelectionChanged.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        ReturnValue_0: bool = NotEqual_ObjectObject(SplitterRule, self.mActiveRule)
        if not ReturnValue_0:
            goto('L1372')
        self.mActiveRule = SplitterRule
        self.Widget_ProgrammableSplitter_List.SetVisibility(0)
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.Widget_ProgrammableSplitter_List.PlayAnimation(self.Widget_ProgrammableSplitter_List.FadeInList, 0, 1, 0, 1)
        self.DeslectAllRules()
        goto(ExecutionFlow.Pop())
        # Label 1372
        self.HideDescriptors()
        goto(ExecutionFlow.Pop())
        self.mActiveRule = None
        ReturnValue1_0: Ptr[UMGSequencePlayer] = self.Widget_ProgrammableSplitter_List.PlayAnimation(self.Widget_ProgrammableSplitter_List.FadeInList, 0, 1, 1, 1)
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 222, UUID = -122024525, ExecutionFunction = "ExecuteUbergraph_Widget_SplitterProgrammable", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(self.mActiveRule)
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        ReturnValue_3: SplitterSortRule = self.mSplitterSmart.GetSortRuleAt(self.mActiveRule.mRuleIndex)
        SplitterSortRule3.ItemClass = SelectedDescriptor
        SplitterSortRule3.OutputIndex = ReturnValue_3.OutputIndex
        self.OnRuleUpdated(self.mActiveRule.mRuleIndex, SplitterSortRule3)
        SplitterSortRule4.ItemClass = SelectedDescriptor
        SplitterSortRule4.OutputIndex = self.mActiveRule.mCachedRule.OutputIndex
        self.mActiveRule.ForceRefreshButton(SplitterSortRule4)
        # Label 1974
        self.HideDescriptors()
        goto(ExecutionFlow.Pop())
        # Label 1989
        self.HideDescriptors()
        goto('L415')
        # Label 2008
        self.HideDescriptors()
        goto('L261')
        goto('L2008')
        # Label 2032
        Smart: Ptr[FGBuildableSplitterSmart] = Cast[FGBuildableSplitterSmart](self.mInteractObject)
        bSuccess: bool = Smart
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        self.mSplitterSmart = Smart
        self.InitWindow()
        self.CheckIfSmartSplitter()
        self.SetAddButtonVisibility()
        goto('L1034')
        # Label 2173
        self.Construct()
        goto('L2032')
        goto('L529')
        SplitterRule1.RemoveFromParent()
        goto('L1989')
        goto('L2173')
        Default__KismetSystemLibrary.PrintString(self, "UpdateList", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        self.UpdateRuleIndexes()
        goto(ExecutionFlow.Pop())
        self.mSplitterSmart.OnSortRulesChangedDelegate.Clear()
        goto(ExecutionFlow.Pop())
        goto('L650')
        goto('L842')
    
