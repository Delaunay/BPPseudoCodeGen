
from codegen.ue4_stub import *

from Script.FactoryGame import ShowOutline
from Game.FactoryGame.World.Benefit.DropPod.Widget_DropPod_Repair import Widget_DropPod_Repair
from Game.FactoryGame.World.Benefit.DropPod.BP_DropPod import ExecuteUbergraph_BP_DropPod.K2Node_Event_state
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import HasItems
from Script.Engine import Controller
from Game.FactoryGame.Resource.Environment.CrashSites.Desc_ServerRack import Desc_ServerRack
from Script.FactoryGame import StartIsLookedAt
from Game.FactoryGame.World.Benefit.DropPod.BP_DropPod import ExecuteUbergraph_BP_DropPod.K2Node_Event_InteractingCharacter
from Script.FactoryGame import StopIsLookedAt
from Script.FactoryGame import GetTargetConsumption
from Script.Engine import ReceiveBeginPlay
from Script.FactoryGame import FGDropPod
from Script.FactoryGame import DropPackage
from Game.FactoryGame.World.Benefit.DropPod.BP_DropPod import ExecuteUbergraph_BP_DropPod
from Script.FactoryGame import SetPowerInfo
from Script.Engine import HasAuthority
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import HUD
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import RollDropPackage
from Script.Engine import GetController
from Script.FactoryGame import GetInventory
from Game.FactoryGame.World.Benefit.DropPod.BP_DropPod import ExecuteUbergraph_BP_DropPod.K2Node_Event_byCharacter2
from Script.FactoryGame import FGInventoryComponent
from Script.FactoryGame import Open
from Script.FactoryGame import HideOutline
from Script.Engine import GetHUD
from Script.FactoryGame import OnRepair
from Script.FactoryGame import OnUse
from Game.FactoryGame.World.Benefit.DropPod.BP_DropPod import ExecuteUbergraph_BP_DropPod.K2Node_Event_state2
from Game.FactoryGame.Resource.Environment.CrashSites.Desc_HardDrive import Desc_HardDrive
from Game.FactoryGame.World.Benefit.DropPod.BP_DropPod import ExecuteUbergraph_BP_DropPod.K2Node_Event_state1
from Script.Engine import FlushNetDormancy
from Game.FactoryGame.World.Benefit.DropPod.BP_DropPod import ExecuteUbergraph_BP_DropPod.K2Node_Event_byCharacter1
from Game.FactoryGame.World.Benefit.DropPod.BP_DropPod import ExecuteUbergraph_BP_DropPod.K2Node_Event_byCharacter
from Script.FactoryGame import FGHUD
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.FactoryGame import SetTargetConsumption
from Script.FactoryGame import FGItemDescriptor
from Script.FactoryGame import ItemAmount
from Script.FactoryGame import Remove
from Script.Engine import Array_Clear
from Script.Engine import IsValidClass

class BP_DropPod(FGDropPod):
    mContainsServerRack: bool
    mContainsHardDrive: bool
    mPowerConsumption: float
    mRepairAmount: ItemAmount
    LootItems: List[TSubclassOf[FGItemDescriptor]]
    mAmountOfInventorySlots = 1
    mPowerInfo = Namespace(ObjectClass='/Script/FactoryGame.FGPowerInfoComponent', ObjectFlags=2883617, ObjectName='PowerInfoComponent')
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=1.7666829824447632, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    
    def RequiresPowerToOpen(self):
        ReturnValue: bool = self.mPowerConsumption > 0
        ReturnValue_0: bool = ReturnValue
    

    def GetPowerConnection(self):
        ReturnValue = self.PowerInput
    

    def Repair(self, byCharacter: Ptr[FGCharacterPlayer]):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L394')
        ReturnValue_0: Ptr[FGInventoryComponent] = byCharacter.GetInventory()
        ReturnValue_1: bool = ReturnValue_0.HasItems(self.mRepairAmount.ItemClass, self.mRepairAmount.amount)
        if not ReturnValue_1:
            goto('L394')
        ReturnValue_0 = byCharacter.GetInventory()
        ReturnValue_0.Remove(self.mRepairAmount.ItemClass, self.mRepairAmount.amount)
        self.FlushNetDormancy()
        ItemAmount.ItemClass = self.mRepairAmount.ItemClass
        ItemAmount.amount = 0
        self.mRepairAmount = ItemAmount
        self.Open()
    

    def GetRepairAmount(self):
        amount = self.mRepairAmount
    

    def GetPowerConsumption(self):
        Power = self.mPowerConsumption
    

    def NeedsPower(self):
        ReturnValue: float = self.mPowerInfo.GetTargetConsumption()
        ReturnValue_0: bool = ReturnValue > 0
        NeedsPower = ReturnValue_0
    

    def NeedsRepair(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mRepairAmount.ItemClass)
        ReturnValue_0: bool = self.mRepairAmount.amount > 0
        ReturnValue_1: bool = ReturnValue and ReturnValue_0
        NeedsRepair = ReturnValue_1
    

    def RollLoot(self):
        self.ExecuteUbergraph_BP_DropPod(10)
    

    def OnOpened(self):
        self.ExecuteUbergraph_BP_DropPod(389)
    

    def StopIsLookedAt(self):
        ExecuteUbergraph_BP_DropPod.K2Node_Event_byCharacter2 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_DropPod.K2Node_Event_state2 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_DropPod(394)
    

    def StartIsLookedAt(self):
        ExecuteUbergraph_BP_DropPod.K2Node_Event_byCharacter1 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_DropPod.K2Node_Event_state1 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_DropPod(427)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_DropPod(460)
    

    def OnUse(self):
        ExecuteUbergraph_BP_DropPod.K2Node_Event_byCharacter = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_DropPod.K2Node_Event_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_DropPod(557)
    

    def OnRepair(self):
        ExecuteUbergraph_BP_DropPod.K2Node_Event_InteractingCharacter = InteractingCharacter #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_DropPod(938)
    

    def ExecuteUbergraph_BP_DropPod(self):
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.LootItems])
        if not self.mContainsServerRack:
            goto('L152')
        Variable1: Const[TSubclassOf[FGItemDescriptor]] = Desc_ServerRack
        
        ReturnValue1: int32 = self.LootItems.append(Variable1)
        # Label 152
        if not self.mContainsHardDrive:
            goto('L253')
        Variable: Const[TSubclassOf[FGItemDescriptor]] = Desc_HardDrive
        
        ReturnValue: int32 = self.LootItems.append(Variable)
        # Label 253
        ReturnValue_0: DropPackage = self.RollDropPackage(self.LootItems)
        # End
        # Label 295
        Default__FGBlueprintFunctionLibrary.HideOutline(self.StaticMesh)
        # End
        # Label 341
        Default__FGBlueprintFunctionLibrary.ShowOutline(self.StaticMesh, 252)
        # End
        # End
        
        state2 = None
        # Label 394
        self.StopIsLookedAt(byCharacter2, Ref[state2])
        goto('L295')
        
        state1 = None
        self.StartIsLookedAt(byCharacter1, Ref[state1])
        goto('L341')
        self.ReceiveBeginPlay()
        self.PowerInput.SetPowerInfo(self.mPowerInfo)
        self.mPowerInfo.SetTargetConsumption(self.mPowerConsumption)
        # End
        
        state = None
        self.OnUse(byCharacter, Ref[state])
        ReturnValue_1: bool = byCharacter.IsLocallyControlled()
        if not ReturnValue_1:
            goto('L980')
        ReturnValue_2: Ptr[Controller] = byCharacter.GetController()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L980')
        ReturnValue_3: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_3)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
            goto('L980')
        AsFGHUD.OpenInteractUI(Widget_DropPod_Repair, self)
        # End
        self.OnRepair(InteractingCharacter)
        self.Repair(InteractingCharacter)
    
