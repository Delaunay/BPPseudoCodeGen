
from codegen.ue4_stub import *

from Script.Engine import Texture2D
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import FromSeconds
from Script.FactoryGame import GetCost
from Script.Engine import Pawn
from Script.FactoryGame import GetItemIcon
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.CoreUObject import Timespan
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Default__FGResearchManager
from Script.Engine import PlayerController
from Script.FactoryGame import Get
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.InGame.MAMTree.EMamTree_NodeStates import EMamTree_NodeStates
from Script.Engine import FormatArgumentData
from Script.UMG import ESlateVisibility
from Script.FactoryGame import GetInventory
from Script.FactoryGame import IsAnyResearchBeingConducted
from Script.UMG import StopAnimation
from Script.FactoryGame import FGInventoryComponent
from Game.FactoryGame.Interface.UI.InGame.Widget_CostSlotWrapper import Widget_CostSlotWrapper
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Conv_IntToText
from Script.FactoryGame import CanAffordResearch
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import TextToUpper
from Script.FactoryGame import IsResearchBeingConducted
from Script.Engine import SetBoolPropertyByName
from Game.FactoryGame.Interface.UI.InGame.MAMTree.Widget_MAMTree_NodeInfo import ExecuteUbergraph_Widget_MAMTree_NodeInfo
from Script.Engine import BreakTimespan
from Script.FactoryGame import GetTimeToComplete
from Script.FactoryGame import FGResearchManager
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.InGame.-Shared.BPW_GenericSchematicRewardButton import BPW_GenericSchematicRewardButton
from Script.FactoryGame import FGSchematic
from Script.UMG import WidgetAnimation
from Script.Engine import NotEqual_ByteByte
from Script.UMG import UserWidget
from Script.UMG import GetBrushResourceAsTexture2D
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Script.FactoryGame import Default__FGSchematic
from Script.SlateCore import SlateBrush
from Script.FactoryGame import ItemAmount
from Game.FactoryGame.-Shared.Blueprint.BP_SchematicHelper import Default__BP_SchematicHelper
from Script.FactoryGame import GetSchematicDisplayName

class Widget_MAMTree_NodeInfo(UserWidget):
    ButtonFeedbackAnim: Ptr[WidgetAnimation]
    ShowReasearchButtonAnim: Ptr[WidgetAnimation]
    mSchematic: TSubclassOf[FGSchematic]
    mNodeState: uint8
    mIsNodeSelected: bool
    OnClicked: FMulticastScriptDelegate
    
    def GetResearchButtonFeedback(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue)
        ReturnValue_1: bool = ReturnValue_0.IsAnyResearchBeingConducted()
        if not ReturnValue_1:
            goto('L579')
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 151, 'Value': 'OTHER RESEARCH IS BEING CONDUCTED'}"
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 242, 'Value': 'RESEARCHING...'}"
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = Default__FGResearchManager.Get(ReturnValue)
        ReturnValue_2: bool = ReturnValue_0.IsResearchBeingConducted(self.mSchematic)
        Variable_0: bool = ReturnValue_2
        
        switch = {
            False: Variable,
            True: Variable1
        }
        self.mButtonInfo.SetText(switch.get(Variable_0, None))
        # Label 528
        ReturnValue_3: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ButtonFeedbackAnim, 0, 0, 0, 1)
        # End
        # Label 579
        ReturnValue_4: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_4)
        bSuccess: bool = Player
        ReturnValue_5: Ptr[FGInventoryComponent] = Player.GetInventory()
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = Default__FGResearchManager.Get(ReturnValue)
        ReturnValue_6: bool = ReturnValue_0.CanAffordResearch(ReturnValue_5, self.mSchematic)
        if not ReturnValue_6:
            goto('L963')
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ShowReasearchButtonAnim, 0, 1, 0, 1)
        self.mButtonInfo.SetVisibility(2)
        self.StopAnimation(self.ButtonFeedbackAnim)
        # End
        # Label 963
        self.mButtonInfo.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1000, 'Value': "CAN'T AFFORD"}")
        goto('L528')
    

    def UpdateState(self):
        ExecutionFlow.Push("L3854")
        ReturnValue: FText = Default__FGSchematic.GetSchematicDisplayName(self.mSchematic)
        
        ReturnValue_0: FText = Default__KismetTextLibrary.TextToUpper(Ref[ReturnValue])
        self.mSchematicName.SetText(ReturnValue_0)
        ReturnValue_1: SlateBrush = Default__FGSchematic.GetItemIcon(self.mSchematic)
        
        ReturnValue_2: Ptr[Texture2D] = Default__WidgetBlueprintLibrary.GetBrushResourceAsTexture2D(Ref[ReturnValue_1])
        self.mSchematicIcon.SetBrushFromTexture(ReturnValue_2, False)
        if not self.mIsNodeSelected:
            goto('L352')
        self.GetResearchButtonFeedback()
        # Label 352
        self.mCostSlotsContainer.ClearChildren()
        LocalCostText = 
        LocalRewardsText = 
        self.mRewardsContainer.ClearChildren()
        ReturnValue_3: float = Default__FGSchematic.GetTimeToComplete(self.mSchematic)
        ReturnValue_4: Timespan = FromSeconds(ReturnValue_3)
        
        Days = None
        Hours = None
        Minutes = None
        Seconds = None
        Milliseconds = None
        BreakTimespan(ReturnValue_4, Ref[Days], Ref[Hours], Ref[Minutes], Ref[Seconds], Ref[Milliseconds])
        ReturnValue_5: FText = Default__KismetTextLibrary.Conv_IntToText(Seconds, False, True, 2, 324)
        FormatArgumentData.ArgumentName = "s"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_5
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_IntToText(Minutes, False, True, 2, 324)
        FormatArgumentData1.ArgumentName = "m"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue1
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        ReturnValue_6: int32 = Days * 24
        ReturnValue1_0: int32 = ReturnValue_6 + Hours
        FormatArgumentData2.ArgumentName = "h"
        FormatArgumentData2.ArgumentValueType = 0
        FormatArgumentData2.ArgumentValue = 
        FormatArgumentData2.ArgumentValueInt = ReturnValue1_0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData2, FormatArgumentData1, FormatArgumentData]
        ReturnValue_7: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1504, 'Value': '{h}:{m}:{s}'}", Array)
        self.mResearchTime.SetText(ReturnValue_7)
        
        UnlockDataStruct = None
        Default__BP_SchematicHelper.GetUnlockDataStructFromSchematic(self.mSchematic, self, Ref[UnlockDataStruct])
        
        UnlockDataStruct = None
        ReturnValue2: int32 = len(UnlockDataStruct)
        ReturnValue_8: bool = ReturnValue2 > 0
        if not ReturnValue_8:
            goto('L2420')
        Variable: int32 = 0
        Variable1: int32 = 0
        
        UnlockDataStruct = None
        # Label 1816
        Default__BP_SchematicHelper.GetUnlockDataStructFromSchematic(self.mSchematic, self, Ref[UnlockDataStruct])
        
        UnlockDataStruct = None
        ReturnValue1_1: int32 = len(UnlockDataStruct)
        ReturnValue1_2: bool = Variable <= ReturnValue1_1
        if not ReturnValue1_2:
            goto('L2458')
        Variable1 = Variable
        ExecutionFlow.Push("L3780")
        ReturnValue_9: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_10: Ptr[BPW_GenericSchematicRewardButton] = Default__WidgetBlueprintLibrary.Create(self, BPW_GenericSchematicRewardButton, ReturnValue_9)
        
        UnlockDataStruct = None
        Default__BP_SchematicHelper.GetUnlockDataStructFromSchematic(self.mSchematic, self, Ref[UnlockDataStruct])
        
        UnlockDataStruct = None
        Item1 = None
        Item1 = UnlockDataStruct[Variable1]
        
        Item1 = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_10, "mUnlockData", Ref[Item1])
        ReturnValue_11: bool = Not_PreBool(self.mIsNodeSelected)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_10, "mShouldAlwaysAutoScrollText", ReturnValue_11)
        ReturnValue_12: Ptr[PanelSlot] = self.mRewardsContainer.AddChild(ReturnValue_10)
        goto(ExecutionFlow.Pop())
        # Label 2420
        self.mRewardsSection.SetVisibility(1)
        # Label 2458
        Variable1_0: int32 = 0
        Variable_0: int32 = 0
        # Label 2504
        ReturnValue_13: List[ItemAmount] = Default__FGSchematic.GetCost(self.mSchematic)
        
        ReturnValue_14: int32 = len(ReturnValue_13)
        ReturnValue_15: bool = Variable1_0 <= ReturnValue_14
        if not ReturnValue_15:
            goto('L3211')
        Variable_0 = Variable1_0
        ExecutionFlow.Push("L3137")
        ReturnValue1_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_4: Ptr[Widget_CostSlotWrapper] = Default__WidgetBlueprintLibrary.Create(self, Widget_CostSlotWrapper, ReturnValue1_3)
        LocalCostSlot = ReturnValue1_4
        ReturnValue_16: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_13 = Default__FGSchematic.GetCost(self.mSchematic)
        
        Item = None
        Item = ReturnValue_13[Variable_0]
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue_16, Item.ItemClass, self, Ref[numItems])
        LocalCostSlot.Setup CostIcon(None, Item, None, 0, numItems, False, False, False)
        ReturnValue1_5: Ptr[PanelSlot] = self.mCostSlotsContainer.AddChild(LocalCostSlot)
        goto(ExecutionFlow.Pop())
        # Label 3137
        ReturnValue2_0: int32 = Variable1_0 + 1
        Variable1_0 = ReturnValue2_0
        goto('L2504')
        # Label 3211
        CmpSuccess: bool = NotEqual_ByteByte(self.mNodeState, 1)
        if not CmpSuccess:
            goto('L3302')
        CmpSuccess = NotEqual_ByteByte(self.mNodeState, 2)
        if not CmpSuccess:
            goto('L3302')
        goto(ExecutionFlow.Pop())
        # Label 3302
        Variable_1: FText = 
        Variable1_1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 3342, 'Value': 'RESEARCH PARENT  NODE TO MAKE AVAILABLE'}"
        Variable2: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 3439, 'Value': 'NODE RESEARCHED'}"
        Variable3: FText = 
        Variable4: FText = 
        Variable_2: uint8 = self.mNodeState
        
        switch = {
            0: Variable_1,
            1: Variable1_1,
            2: Variable2,
            3: Variable3,
            4: Variable4
        }
        self.mButtonInfo.SetText(switch.get(Variable_2, None))
        self.mButtonInfo.SetVisibility(3)
        ReturnValue_17: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ButtonFeedbackAnim, 0, 0, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 3780
        ReturnValue_18: int32 = Variable + 1
        Variable = ReturnValue_18
        goto('L1816')
    

    def SetSchematic(self, schematic: TSubclassOf[FGSchematic]):
        self.mSchematic = schematic
        self.UpdateState()
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_MAMTree_NodeInfo(10)
    

    def BndEvt__mResearchButton_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_MAMTree_NodeInfo(425)
    

    def ExecuteUbergraph_Widget_MAMTree_NodeInfo(self):
        self.SetSchematic(self.mSchematic)
        Variable: uint8 = 4
        Variable1: uint8 = 1
        ReturnValue: bool = NotEqual_ByteByte(self.mNodeState, 3)
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mContent.SetVisibility(switch.get(Variable_0, None))
        Variable2: uint8 = 4
        Variable3: uint8 = 1
        ReturnValue = NotEqual_ByteByte(self.mNodeState, 3)
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        Variable1_0: bool = ReturnValue_0
        
        switch_0 = {
            False: Variable3,
            True: Variable2
        }
        self.mHiddenInfo.SetVisibility(switch_0.get(Variable1_0, None))
        # End
        self.OnClicked.ProcessMulticastDelegate()
    

    def OnClicked__DelegateSignature(self):
        pass
    
