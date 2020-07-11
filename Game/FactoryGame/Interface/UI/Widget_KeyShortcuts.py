
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import PlayerController
from Script.FactoryGame import Get
from Game.FactoryGame.Interface.UI.Assets.HUD_Elements.Keybord_Shortcuts.map_active import map_active
from Script.FactoryGame import FGSchematicManager
from Script.UMG import Construct
from Script.Engine import Delay
from Script.FactoryGame import FGPlayerController
from Game.FactoryGame.Interface.UI.Widget_KeyShortcuts import ExecuteUbergraph_Widget_KeyShortcuts.K2Node_CustomEvent_Unused
from Script.Engine import IsValid
from Script.FactoryGame import GetIsMapUnlocked
from Game.FactoryGame.Interface.UI.Widget_KeyShortcuts import ExecuteUbergraph_Widget_KeyShortcuts
from Script.FactoryGame import Default__FGSchematicManager
from Script.FactoryGame import Default__FGUnlockSubsystem
from Script.FactoryGame import FGUnlockSubsystem
from Script.Engine import LatentActionInfo
from Script.UMG import UserWidget

class Widget_KeyShortcuts(UserWidget):
    
    
    def UpdateShortcutText(self):
        
        keyText = None
        self.GetKeyForAction("ToggleBuildGun", Ref[keyText])
        self.mBuildgunText.SetText(keyText)
        
        keyText6 = None
        self.GetKeyForAction("ToggleDismantle", Ref[keyText6])
        self.mDismantleText.SetText(keyText6)
        
        keyText5 = None
        self.GetKeyForAction("Flashlight", Ref[keyText5])
        self.mFlashlightText.SetText(keyText5)
        
        keyText4 = None
        self.GetKeyForAction("ResourceScanner_ToggleVehicleRecording", Ref[keyText4])
        self.mScannerText.SetText(keyText4)
        
        keyText3 = None
        self.GetKeyForAction("inventory", Ref[keyText3])
        self.mInventoryText.SetText(keyText3)
        
        keyText2 = None
        self.GetKeyForAction("OpenCodex", Ref[keyText2])
        self.mCodexText.SetText(keyText2)
        
        keyText1 = None
        self.GetKeyForAction("ToggleMap_BuildGunNoSnapMode", Ref[keyText1])
        self.mMinimapText.SetText(keyText1)
    

    def GetKeyForAction(self, ActionName: FName):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        button = None
        Default__HUDHelpers.GetKeyNameForActionSimple(ReturnValue, ActionName, self, Ref[button])
        keyText = button
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_KeyShortcuts(950)
    

    def UpdateShortcutAvilability(self, Unused: TSubclassOf[FGSchematic]):
        ExecuteUbergraph_Widget_KeyShortcuts.K2Node_CustomEvent_Unused = Unused #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_KeyShortcuts(723)
    

    def ExecuteUbergraph_Widget_KeyShortcuts(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue1)
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue2: Ptr[FGUnlockSubsystem] = Default__FGUnlockSubsystem.Get(ReturnValue3)
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue2)
        ReturnValue_1: bool = ReturnValue_0 and ReturnValue1_0
        if not ReturnValue_1:
            goto('L474')
        ReturnValue1 = self.GetOwningPlayer()
        ReturnValue = Default__FGSchematicManager.Get(ReturnValue1)
        OutputDelegate1.BindUFunction(self, UpdateShortcutAvilability)
        ReturnValue.PurchasedSchematicDelegate.AddUnique(OutputDelegate1)
        self.UpdateShortcutAvilability(None)
        goto(ExecutionFlow.Pop())
        # Label 474
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 15, UUID = -817032248, ExecutionFunction = "ExecuteUbergraph_Widget_KeyShortcuts", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 551
        self.UpdateShortcutText()
        ReturnValue_2: Ptr[PlayerController] = self.GetOwningPlayer()
        OutputDelegate.BindUFunction(self, UpdateShortcutText)
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        Controller.OnInputChanged.AddUnique(OutputDelegate)
        goto('L15')
        ReturnValue2_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_1: Ptr[FGUnlockSubsystem] = Default__FGUnlockSubsystem.Get(ReturnValue2_0)
        ReturnValue_3: bool = ReturnValue1_1.GetIsMapUnlocked()
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        self.mMinimap.SetBrushFromTexture(map_active, False)
        self.mMinimapText.SetVisibility(0)
        goto(ExecutionFlow.Pop())
        # Label 935
        self.Construct()
        goto('L551')
        goto('L935')
    
