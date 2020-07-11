
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Pawn
from Script.FactoryGame import HasEnoughSpaceForItem
from Game.FactoryGame.Buildable.Vehicle.Golfcart.Widget_GolfCart import ExecuteUbergraph_Widget_GolfCart
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.FactoryGame import GetInventory
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.FactoryGame import FGInventoryComponent
from Script.FactoryGame import GetDriver
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import Init
from Script.Engine import RandomInteger
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Destruct
from Script.FactoryGame import InventoryItem
from Script.FactoryGame import GetStorageInventory
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Script.FactoryGame import FGWheeledVehicle

class Widget_GolfCart(Widget_UseableBase):
    mGolfCart: Ptr[FGWheeledVehicle]
    mGolfCartItem: InventoryItem = Namespace(ItemClass='/Game/FactoryGame/Resource/Equipment/GolfCart/Desc_GolfCart.Desc_GolfCart_C', ItemState={'ActorPtr': {'$Empty': True}})
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
    
    def InitCallbacks(self):
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
    

    def Init(self):
        self.ExecuteUbergraph_Widget_GolfCart(10)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_GolfCart(746)
    

    def BndEvt__mButtonPickUpMiner_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_GolfCart(1029)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_GolfCart(1034)
    

    def ExecuteUbergraph_Widget_GolfCart(self):
        self.Init()
        Vehicle: Ptr[FGWheeledVehicle] = Cast[FGWheeledVehicle](self.mInteractObject)
        bSuccess: bool = Vehicle
        self.mGolfCart = Vehicle
        self.InitCallbacks()
        ReturnValue: Ptr[FGInventoryComponent] = self.mGolfCart.GetStorageInventory()
        self.Widget_Inventory.Init(ReturnValue)
        # End
        # Label 210
        ReturnValue_0: Ptr[FGCharacterPlayer] = self.mGolfCart.GetDriver()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L322')
        # End
        # Label 322
        ReturnValue_2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_2)
        bSuccess1: bool = Player
        if not bSuccess1:
            goto('L1416')
        ReturnValue_3: Ptr[FGInventoryComponent] = Player.GetInventory()
        
        ReturnValue_4: bool = ReturnValue_3.HasEnoughSpaceForItem(Ref[self.mGolfCartItem])
        if not ReturnValue_4:
            goto('L727')
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_5)
        bSuccess2: bool = Controller
        if not bSuccess2:
            goto('L1416')
        ReturnValue_6: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_6.ServerDismantleGolfCart(self.mGolfCart)
        # Label 727
        self.OnEscapePressed()
        # End
        self.Construct()
        self.bIsFocusable = True
        ReturnValue_7: int32 = RandomInteger(5)
        CmpSuccess: bool = ReturnValue_7 != 0
        if not CmpSuccess:
            goto('L938')
        self.Widget_Window_DarkMode.SetTitle("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 885, 'Value': 'Golf Cart'}")
        # End
        # Label 938
        self.Widget_Window_DarkMode.SetTitle("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 975, 'Value': 'Puny Vroom'}")
        # End
        goto('L210')
        self.Destruct()
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mGolfCart)
        if not ReturnValue1:
            goto('L1416')
        ReturnValue1_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player1: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue1_0)
        bSuccess3: bool = Player1
        if not bSuccess3:
            goto('L1416')
        ReturnValue1_1: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller_0: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1_1)
        bSuccess4: bool = Controller_0
        if not bSuccess4:
            goto('L1416')
        ReturnValue1_2: Ptr[BP_RemoteCallObject] = Controller_0.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue1_2.ServerCloseVehicleTrunk(self.mGolfCart, Player1)
    
