
from codegen.ue4_stub import *

from Script.Engine import Delay
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import HasItems
from Script.FactoryGame import HasBeenOpened
from Script.Engine import Pawn
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.Engine import Not_PreBool
from Script.FactoryGame import GetLootInventory
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import SetRenderTranslation
from Script.FactoryGame import GetItemName
from Script.Engine import FormatArgumentData
from Script.UMG import PlayAnimation
from Script.FactoryGame import GetInventory
from Script.UMG import ESlateVisibility
from Script.UMG import StopAnimation
from Script.FactoryGame import FGInventoryComponent
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Smoke import Widget_Smoke
from Script.FactoryGame import Init
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.UMG import WidgetAnimation
from Script.FactoryGame import GetHasPower
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import Default__FGItemDescriptor
from Script.UMG import Create
from Script.CoreUObject import Vector2D
from Game.FactoryGame.World.Benefit.DropPod.BP_DropPod import BP_DropPod
from Game.FactoryGame.World.Benefit.DropPod.Widget_DropPod_Repair import ExecuteUbergraph_Widget_DropPod_Repair

class Widget_DropPod_Repair(Widget_UseableBase):
    PartPulse: Ptr[WidgetAnimation]
    PowerPulse: Ptr[WidgetAnimation]
    ShakeAnim: Ptr[WidgetAnimation]
    LampPulseAnim: Ptr[WidgetAnimation]
    OpenDoorAnim: Ptr[WidgetAnimation]
    mDropPod: Ptr[BP_DropPod]
    mPowerText: FText = NSLOCTEXT("", "5E39967541ED642240847989DD21A74C", "Battery Broken")
    mPartText: FText = NSLOCTEXT("", "39E9245F46DB829C56893E8944EFF644", "Pod Damaged")
    SparkIndex: int32
    mShouldOpenInventory = True
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mUseGamepadCursor = True
    mCallCustomTickOnConstruct = True
    
    def GetHasAllRepairParts(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L288')
        
        Amount = None
        self.mDropPod.GetRepairAmount(Ref[Amount])
        ReturnValue_0: Ptr[FGInventoryComponent] = Player.GetInventory()
        # Label 186
        ReturnValue_1: bool = ReturnValue_0.HasItems(Amount.ItemClass, Amount.amount)
        Has All Parts = ReturnValue_1
        # End
        # Label 288
        Has All Parts = False
    

    def SetHasDoorBeenOpened(self):
        ReturnValue: bool = self.mDropPod.HasBeenOpened()
        self.Widget_DropPod_Door.SetHasBeenOpened(ReturnValue)
        ReturnValue = self.mDropPod.HasBeenOpened()
        if not ReturnValue:
            goto('L199')
        self.Widget_DropPod_Door.SetRenderTranslation(Vector2D(X = -306, Y = 0))
    

    def SetupScreenText(self):
        self.PartText.SetText(self.mPartText)
        self.PowerText.SetText(self.mPowerText)
        ReturnValue: bool = self.GetHasPartsAndPower()
        if not ReturnValue:
            goto('L296')
        self.RepairInfo.SetVisibility(1)
        self.OpenDoorText.SetVisibility(0)
        self.StatusText.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 241, 'Value': 'OPERATIONAL'}")
        # End
        
        NeedsRepair = None
        # Label 296
        self.mDropPod.NeedsRepair(Ref[NeedsRepair])
        if not NeedsRepair:
            goto('L1567')
        self.PartInfo.SetVisibility(0)
        
        Parts = None
        self.GetHasAllRepairParts(Ref[Parts])
        if not Parts:
            goto('L1610')
        
        Amount = None
        self.mDropPod.GetRepairAmount(Ref[Amount])
        ReturnValue_0: FText = Default__FGItemDescriptor.GetItemName(Amount.ItemClass)
        FormatArgumentData.ArgumentName = "Item"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_0
        # Label 641
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 805, 'Value': '{Item} Recieved'}", Array)
        self.PartValue.SetText(ReturnValue_1)
        
        NeedsPower = None
        # Label 913
        self.mDropPod.NeedsPower(Ref[NeedsPower])
        if not NeedsPower:
            goto('L2358')
        self.powerInfo.SetVisibility(0)
        
        Power = None
        self.mDropPod.GetPowerConsumption(Ref[Power])
        FormatArgumentData1.ArgumentName = "Amount"
        FormatArgumentData1.ArgumentValueType = 2
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = Power
        FormatArgumentData1.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData1]
        ReturnValue1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1316, 'Value': 'Needs {Amount} MW'}", Array1)
        self.PowerValue.SetText(ReturnValue1)
        ReturnValue_2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.PowerPulse, 0, 0, 0, 1)
        # Label 1472
        self.StatusText.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1509, 'Value': 'REPAIRS NEEDED'}")
        # End
        # Label 1567
        self.PartInfo.SetVisibility(1)
        goto('L913')
        
        Amount1 = None
        # Label 1610
        self.mDropPod.GetRepairAmount(Ref[Amount1])
        FormatArgumentData2.ArgumentName = "Amount"
        FormatArgumentData2.ArgumentValueType = 0
        FormatArgumentData2.ArgumentValue = 
        FormatArgumentData2.ArgumentValueInt = Amount1.amount
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        ReturnValue1_0: FText = Default__FGItemDescriptor.GetItemName(Amount1.ItemClass)
        FormatArgumentData3.ArgumentName = "Item"
        FormatArgumentData3.ArgumentValueType = 4
        FormatArgumentData3.ArgumentValue = ReturnValue1_0
        FormatArgumentData3.ArgumentValueInt = 0
        FormatArgumentData3.ArgumentValueFloat = 0
        FormatArgumentData3.ArgumentValueGender = 0
        Array2: List[FormatArgumentData] = [FormatArgumentData2, FormatArgumentData3]
        ReturnValue2: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2193, 'Value': 'Needs {Amount} {Item}'}", Array2)
        self.PartValue.SetText(ReturnValue2)
        ReturnValue1_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.PartPulse, 0, 0, 0, 1)
        goto('L913')
        # Label 2358
        self.powerInfo.SetVisibility(1)
        goto('L1472')
    

    def SetupCostSlot(self):
        
        NeedsRepair = None
        self.mDropPod.NeedsRepair(Ref[NeedsRepair])
        if not NeedsRepair:
            goto('L453')
        self.FanCover.SetVisibility(2)
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L453')
        ReturnValue_0: Ptr[FGInventoryComponent] = Player.GetInventory()
        
        Amount = None
        self.mDropPod.GetRepairAmount(Ref[Amount])
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromInventory(ReturnValue_0, Amount.ItemClass, self, Ref[numItems])
        self.Widget_CostSlotWrapper.Setup CostIcon(None, Amount, None, 0, numItems, False, False, False)
        self.Widget_CostSlotWrapper.mForceEmptyAnim = True
    

    def GetHasPartsAndPower(self):
        
        Parts = None
        self.GetHasAllRepairParts(Ref[Parts])
        
        NeedsPower = None
        self.mDropPod.NeedsPower(Ref[NeedsPower])
        if not NeedsPower:
            goto('L186')
        ReturnValue: bool = self.mDropPod.GetHasPower()
        ReturnValue_0: bool = Parts and ReturnValue
        ReturnValue_1: bool = ReturnValue_0
        goto('L205')
        # Label 186
        ReturnValue_1 = Parts
    

    def GetRepairButtonVisibility(self):
        Variable: uint8 = 0
        Variable1: uint8 = 1
        
        NeedsRepair = None
        self.mDropPod.NeedsRepair(Ref[NeedsRepair])
        Variable_0: bool = NeedsRepair
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue = switch.get(Variable_0, None)
    

    def GetRepairConditionText(self):
        
        NeedsRepair = None
        self.mDropPod.NeedsRepair(Ref[NeedsRepair])
        if not NeedsRepair:
            goto('L770')
        
        Amount = None
        self.mDropPod.GetRepairAmount(Ref[Amount])
        FormatArgumentData1.ArgumentName = "NUM"
        FormatArgumentData1.ArgumentValueType = 0
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = Amount.amount
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        ReturnValue: FText = Default__FGItemDescriptor.GetItemName(Amount.ItemClass)
        FormatArgumentData2.ArgumentName = "ITEM"
        FormatArgumentData2.ArgumentValueType = 4
        FormatArgumentData2.ArgumentValue = ReturnValue
        FormatArgumentData2.ArgumentValueInt = 0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData2]
        ReturnValue1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 639, 'Value': 'Repair using {NUM}x {ITEM} to open the access hatch'}", Array1)
        ReturnValue_0: FText = ReturnValue1
        goto('L1254')
        
        NeedsPower = None
        # Label 770
        self.mDropPod.NeedsPower(Ref[NeedsPower])
        if not NeedsPower:
            goto('L1254')
        
        Power = None
        self.mDropPod.GetPowerConsumption(Ref[Power])
        FormatArgumentData.ArgumentName = "MW"
        FormatArgumentData.ArgumentValueType = 2
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = Power
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1131, 'Value': 'Connect {MW}MW of power to open the access hatch'}", Array)
        ReturnValue_0 = ReturnValue_1
    

    def BndEvt__mGrabAllButton_K2Node_ComponentBoundEvent_3_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_DropPod_Repair(1048)
    

    def Init(self):
        self.ExecuteUbergraph_Widget_DropPod_Repair(35)
    

    def OnDoorOpen(self):
        self.ExecuteUbergraph_Widget_DropPod_Repair(814)
    

    def PodUnlocked(self):
        self.ExecuteUbergraph_Widget_DropPod_Repair(1043)
    

    def SpawnSmoke(self):
        self.ExecuteUbergraph_Widget_DropPod_Repair(1053)
    

    def ExecuteUbergraph_Widget_DropPod_Repair(self):
        goto(ComputedJump("EntryPoint"))
        self.StopAnimation(self.ShakeAnim)
        goto(ExecutionFlow.Pop())
        self.Init()
        Pod: Ptr[BP_DropPod] = Cast[BP_DropPod](self.mInteractObject)
        bSuccess1: bool = Pod
        self.mDropPod = Pod
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
        OutputDelegate1.BindUFunction(self, OnEscapePressed)
        self.Widget_StandardButton.OnClicked.AddUnique(OutputDelegate1)
        OutputDelegate2.BindUFunction(self, OnDoorOpen)
        self.Widget_DropPod_Door.OnDoorOpen.AddUnique(OutputDelegate2)
        ReturnValue: bool = self.GetHasPartsAndPower()
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        self.Widget_DropPod_Door.IsLocked = ReturnValue_0
        self.Widget_DropPod_Door.SetLEDVisibility()
        self.SetupCostSlot()
        self.SetupScreenText()
        ReturnValue_1: Ptr[FGInventoryComponent] = self.mDropPod.GetLootInventory()
        self.Widget_InventorySlot.mCachedInventoryComponent = ReturnValue_1
        OutputDelegate3.BindUFunction(self, OnInventorySlotStackMove)
        self.Widget_InventorySlot.OnMoveStack.AddUnique(OutputDelegate3)
        self.SetHasDoorBeenOpened()
        goto(ExecutionFlow.Pop())
        # Label 641
        ReturnValue_2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_2)
        bSuccess: bool = Player
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        
        RCO = None
        self.GetDefaultRCO(Ref[RCO])
        RCO.Server_RepairDropPod(self.mDropPod, Player)
        goto(ExecutionFlow.Pop())
        ReturnValue2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ShakeAnim, 0, 0, 0, 1)
        ReturnValue_3: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.OpenDoorAnim, 0, 1, 0, 1)
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.LampPulseAnim, 0, 0, 0, 1)
        self.PodUnlocked()
        Default__KismetSystemLibrary.Delay(self, 3, LatentActionInfo(Linkage = 15, UUID = -166940195, ExecutionFunction = "ExecuteUbergraph_Widget_DropPod_Repair", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L641')
        goto('L641')
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: Ptr[Widget_Smoke] = Default__WidgetBlueprintLibrary.Create(self, Widget_Smoke, ReturnValue_4)
        ReturnValue_6: Ptr[PanelSlot] = self.SmokeContainer.AddChild(ReturnValue_5)
        goto(ExecutionFlow.Pop())
    
