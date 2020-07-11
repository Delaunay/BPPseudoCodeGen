
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.Engine import Default__KismetInputLibrary
from Script.UMG import GetViewportSize
from Script.Engine import Conv_TextToString
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import GetDisplayName
from Script.Engine import Pawn
from Script.InputCore import Key
from Script.UMG import Default__WidgetLayoutLibrary
from Script.FactoryGame import HasEnoughSpaceForStack
from Script.FactoryGame import SetShowInventory
from Script.Engine import Not_PreBool
from Script.Engine import HUD
from Script.Engine import FTrunc
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import OnKeyUp
from Script.Engine import FormatArgumentData
from Script.Engine import GetHUD
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import ExecuteUbergraph_Widget_UseableBase.K2Node_Event_IsDesignTime
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.FactoryGame import FGUseableInterface
from Script.Engine import BreakVector2D
from Script.FactoryGame import FGInteractWidget
from Script.FactoryGame import GetGameUI
from Script.Engine import Format
from Script.FactoryGame import SetWindowWantsInventoryAddon
from Script.Engine import SetMouseLocation
from Script.FactoryGame import FGHUD
from Script.Engine import GetKey
from Script.FactoryGame import FGGameUI
from Script.UMG import OnKeyDown
from Script.Engine import EqualEqual_KeyKey
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.UMG import GetOwningPlayerPawn
from Script.CoreUObject import Vector2D
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import ExecuteUbergraph_Widget_UseableBase
from Script.Engine import PrintString
from Script.UMG import EventReply
from Script.CoreUObject import LinearColor

class Widget_UseableBase(FGInteractWidget):
    mShouldOpenInventory: bool
    InventorySlotStackMoveEvent: FMulticastScriptDelegate
    mDidPressModifier: bool
    ModifierPressed: FMulticastScriptDelegate
    ModifierReleased: FMulticastScriptDelegate
    mRestoreFocusWhenLost = True
    mCallCustomTickOnConstruct = True
    
    def OnKeyDown(self):
        ReturnValue: EventReply = self.OnKeyDown(MyGeometry, InKeyEvent)
        
        ReturnValue_0: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_1: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue_0, Key(KeyName = "LeftControl"))
        if not ReturnValue_1:
            goto('L271')
        ReturnValue_2: bool = Not_PreBool(self.mDidPressModifier)
        if not ReturnValue_2:
            goto('L271')
        self.mDidPressModifier = True
        self.ModifierPressed.ProcessMulticastDelegate(self)
        # Label 271
        ReturnValue_3: EventReply = ReturnValue
    

    def OnKeyUp(self):
        ReturnValue: EventReply = self.OnKeyUp(MyGeometry, InKeyEvent)
        
        ReturnValue_0: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_1: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue_0, Key(KeyName = "LeftControl"))
        ReturnValue_2: bool = ReturnValue_1 and self.mDidPressModifier
        if not ReturnValue_2:
            goto('L266')
        self.mDidPressModifier = False
        self.ModifierReleased.ProcessMulticastDelegate(self)
        # Label 266
        ReturnValue_3: EventReply = ReturnValue
    

    def DropInventoryStackOnInventoryComponent(self, InventorySlot: Ptr[Widget_InventorySlot], inventoryComponent: Ptr[FGInventoryComponent]):
        
        Stack = None
        InventorySlot.GetStack(Ref[Stack])
        
        Stack = None
        ReturnValue: bool = inventoryComponent.HasEnoughSpaceForStack(Ref[Stack])
        if not ReturnValue:
            goto('L387')
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_0)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L398')
        ReturnValue_1: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_1.Server_MoveItemIfSpace(InventorySlot.mCachedInventoryComponent, InventorySlot.mSlotIdx, inventoryComponent)
        Result = True
        # End
        # Label 387
        Result = False
    

    def DropInventoryStackOnInventoryWidget(self, InventorySlot: Ptr[Widget_InventorySlot], WidgetInventory: Ptr[Widget_Inventory]):
        
        Result = None
        self.DropInventoryStackOnInventoryComponent(InventorySlot, WidgetInventory.mInventoryComponent, Ref[Result])
        Result = Result
    

    def InitInventoryWidgetCallbacks(self, inventoryComponent: Ptr[Widget_Inventory]):
        ExecutionFlow.Push("L432")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        inventoryComponent.mInventorySlots = None
        # Label 51
        ReturnValue: int32 = len(inventoryComponent.mInventorySlots)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L358")
        
        inventoryComponent.mInventorySlots = None
        Item = None
        Item = inventoryComponent.mInventorySlots[Variable_0]
        OutputDelegate.BindUFunction(self, OnInventorySlotStackMove)
        Item.OnMoveStack.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 358
        ReturnValue_1: int32 = Variable + 1
        Variable = ReturnValue_1
        goto('L51')
    

    def OnInventorySlotStackMove(self, InventorySlot: Ptr[Widget_InventorySlot]):
        self.InventorySlotStackMoveEvent.ProcessMulticastDelegate(InventorySlot, 1)
    

    def DropInventorySlotStack(self, InventorySlot: Ptr[Widget_InventorySlot]):
        ReturnValue: FString = Default__KismetSystemLibrary.GetDisplayName(self)
        # Label 51
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue)
        FormatArgumentData.ArgumentName = "WidgetName"
        FormatArgumentData.ArgumentValueType = 4
        # Label 178
        FormatArgumentData.ArgumentValue = ReturnValue_0
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 378, 'Value': 'DropInventorySlotStack was not overriden on {WidgetName}'}", Array)
        
        ReturnValue_2: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_1])
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_2, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 5)
        WasStackMoved = False
    

    def SetInventoryVisibility(self, visible: bool):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[HUD] = ReturnValue.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_0)
        bSuccess: bool = AsFGHUD
        ReturnValue_1: Ptr[FGGameUI] = AsFGHUD.GetGameUI()
        ReturnValue_1.SetShowInventory(visible)
    

    def GetDefaultRCO(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L178')
        ReturnValue_0: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        RCO = ReturnValue_0
        # End
        # Label 178
        Default__KismetSystemLibrary.PrintString(self, "Error: Failed to get default remote call object", True, True, LinearColor(R = 1, G = 0, B = 0, A = 1), 2)
        RCO = None
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_UseableBase.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_UseableBase(10)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_UseableBase(890)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_UseableBase(1267)
    

    def ExecuteUbergraph_Widget_UseableBase(self):
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue: Ptr[HUD] = ReturnValue3.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue)
        bSuccess6: bool = AsFGHUD
        ReturnValue_0: Ptr[FGGameUI] = AsFGHUD.GetGameUI()
        ReturnValue_0.SetWindowWantsInventoryAddon(self.mShouldOpenInventory)
        ReturnValue3 = self.GetOwningPlayer()
        ReturnValue = ReturnValue3.GetHUD()
        AsFGHUD = Cast[FGHUD](ReturnValue)
        bSuccess6 = AsFGHUD
        ReturnValue_0 = AsFGHUD.GetGameUI()
        ReturnValue_0.SetShowInventory(self.mShouldOpenInventory)
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: bool = Not_PreBool(ReturnValue_1.bShowMouseCursor)
        ReturnValue_3: bool = self.mUseMouse and ReturnValue_2
        if not ReturnValue_3:
            goto('L1845')
        ReturnValue_4: Vector2D = Default__WidgetLayoutLibrary.GetViewportSize(self)
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_4, Ref[X], Ref[Y])
        ReturnValue_5: float = Y / 2
        ReturnValue1: float = X / 2
        ReturnValue_6: int32 = FTrunc(ReturnValue_5)
        ReturnValue1_0: int32 = FTrunc(ReturnValue1)
        ReturnValue4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue4.SetMouseLocation(ReturnValue1_0, ReturnValue_6)
        # End
        Interface: TScriptInterface[FGUseableInterface] = QueryInterface[FGUseableInterface](self.mInteractObject)
        bSuccess: bool = Interface
        if not bSuccess:
            goto('L1845')
        ReturnValue1_1: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue1_1)
        bSuccess2: bool = Controller
        if not bSuccess2:
            goto('L1845')
        ReturnValue_7: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_7)
        bSuccess1: bool = Player
        ReturnValue_8: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_8.ServerRegisterInteractingPlayerOnUseInterface(self.mInteractObject, Player)
        # End
        ReturnValue5: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_2: Ptr[HUD] = ReturnValue5.GetHUD()
        AsFGHUD1: Ptr[FGHUD] = Cast[FGHUD](ReturnValue1_2)
        bSuccess7: bool = AsFGHUD1
        ReturnValue1_3: Ptr[FGGameUI] = AsFGHUD1.GetGameUI()
        ReturnValue1_3.SetWindowWantsInventoryAddon(False)
        Interface1: TScriptInterface[FGUseableInterface] = QueryInterface[FGUseableInterface](self.mInteractObject)
        bSuccess3: bool = Interface1
        if not bSuccess3:
            goto('L1845')
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller1: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue2)
        bSuccess5: bool = Controller1
        if not bSuccess5:
            goto('L1845')
        ReturnValue1_4: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player1: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue1_4)
        bSuccess4: bool = Player1
        ReturnValue1_5: Ptr[BP_RemoteCallObject] = Controller1.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue1_5.ServerUnregisterInteractingPlayerOnUseInterface(self.mInteractObject, Player1)
    

    def ModifierReleased__DelegateSignature(self, Owner: Ptr[FGInteractWidget]):
        pass
    

    def ModifierPressed__DelegateSignature(self, NewParam: Ptr[FGInteractWidget]):
        pass
    

    def InventorySlotStackMoveEvent__DelegateSignature(self, InventorySlot: Ptr[Widget_InventorySlot], InteractionDirection: uint8):
        pass
    
