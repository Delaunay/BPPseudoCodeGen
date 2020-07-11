
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Game.FactoryGame.Buildable.-Shared.WorkBench.BP_ManualManufacturingComponent import ExecuteUbergraph_BP_ManualManufacturingComponent
from Game.FactoryGame.Character.Player.BP_PlayerState import BP_PlayerState
from Script.Engine import GetController
from Script.FactoryGame import GetPlayerWorkingAtBench
from Script.FactoryGame import GetCurrentRecipe
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Script.FactoryGame import GetInventory
from Script.FactoryGame import FGRecipe
from Script.FactoryGame import FGWorkBench
from Script.FactoryGame import FGInventoryComponent

class BP_ManualManufacturingComponent(FGWorkBench):
    OnCraftCompleted: FMulticastScriptDelegate
    mManufacturingSpeed = 1
    mFatigueMultiplier = 0.20000000298023224
    mFatigueDecreaseSpeedMultiplier = 3
    mHoldProduceTime = 0.20000000298023224
    mFatigueUpdaterInterval = 10
    mCooldownDelay = 1.5
    mIsFatigueEnabled = True
    PrimaryComponentTick = Namespace(EndTickGroup=0, TickGroup=2, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    bAutoActivate = True
    
    def AwardRewards(self):
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetPlayerWorkingAtBench()
        ReturnValue_0: Ptr[Controller] = ReturnValue.GetController()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_0)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L287')
        ReturnValue_1: Ptr[FGInventoryComponent] = self.GetInventory()
        ReturnValue_2: TSubclassOf[FGRecipe] = self.GetCurrentRecipe()
        ReturnValue_3: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_3.Server_RemoveIngredientsAndAwardRewards(self, ReturnValue_1, ReturnValue_2)
    

    def CraftComplete(self):
        self.ExecuteUbergraph_BP_ManualManufacturingComponent(10)
    

    def ExecuteUbergraph_BP_ManualManufacturingComponent(self):
        self.AwardRewards()
        self.OnCraftCompleted.ProcessMulticastDelegate()
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetPlayerWorkingAtBench()
        State: Ptr[BP_PlayerState] = Cast[BP_PlayerState](ReturnValue.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
            goto('L234')
        ReturnValue_0: TSubclassOf[FGRecipe] = self.GetCurrentRecipe()
        State.RemoveRecipeFromShoppingList(ReturnValue_0, 1)
    

    def OnCraftCompleted__DelegateSignature(self):
        pass
    
