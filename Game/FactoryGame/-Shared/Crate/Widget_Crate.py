
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Pawn
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.-Shared.Crate.Widget_Crate import ExecuteUbergraph_Widget_Crate.K2Node_Event_InDeltaTime
from Script.Engine import PlayerController
from Script.Engine import K2_GetPawn
from Script.FactoryGame import GetInventory
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.Engine import IsValid
from Script.FactoryGame import FGInventoryComponent
from Game.FactoryGame.-Shared.Crate.BP_Crate import BP_Crate
from Script.Engine import BooleanOR
from Script.UMG import Tick
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import Init
from Script.FactoryGame import IsEmpty
from Game.FactoryGame.-Shared.Crate.Widget_Crate import ExecuteUbergraph_Widget_Crate.K2Node_Event_MyGeometry
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Game.FactoryGame.-Shared.Crate.Widget_Crate import ExecuteUbergraph_Widget_Crate
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Destruct
from Script.FactoryGame import FGCrate

class Widget_Crate(Widget_UseableBase):
    mCrate: Ptr[FGCrate]
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
    bHasScriptImplementedTick = True
    
    def DropInventorySlotStack(self):
        
        Result = None
        self.DropInventoryStackOnInventoryWidget(InventorySlot, self.mInventory, Ref[Result])
        WasStackMoved = Result
    

    def Cleanup(self):
        self.Widget_GlowingFactoryButton.mButton.OnClicked.Clear()
        self.Widget_Window_DarkMode.OnClose.Clear()
    

    def Init(self):
        self.ExecuteUbergraph_Widget_Crate(769)
    

    def Tick(self):
        ExecuteUbergraph_Widget_Crate.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Crate.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Crate(784)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Crate(817)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_Crate(1066)
    

    def OnGrabAll(self):
        self.ExecuteUbergraph_Widget_Crate(1324)
    

    def ExecuteUbergraph_Widget_Crate(self):
        # Label 10
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mCrate)
        if not ReturnValue:
            goto('L310')
        ReturnValue1: Ptr[FGInventoryComponent] = self.mCrate.GetInventory()
        ReturnValue2: bool = Default__KismetSystemLibrary.IsValid(self.mCrate)
        ReturnValue_0: bool = ReturnValue1.IsEmpty()
        ReturnValue_1: bool = Not_PreBool(ReturnValue2)
        ReturnValue_2: bool = BooleanOR(ReturnValue_0, ReturnValue_1)
        if not ReturnValue_2:
            goto('L1329')
        self.OnEscapePressed()
        # End
        # Label 310
        self.OnEscapePressed()
        # End
        # Label 329
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(self.mCrate)
        if not ReturnValue1_0:
            goto('L1329')
        ReturnValue_3: Ptr[FGInventoryComponent] = self.mCrate.GetInventory()
        ReturnValue_4: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue3: Ptr[FGInventoryComponent] = Player.GetInventory()
        ReturnValue_4.Server_GrabAllItemsFromInventory(ReturnValue_3, ReturnValue3, None)
        # End
        # Label 589
        ReturnValue3_0: bool = Default__KismetSystemLibrary.IsValid(self.mCrate)
        if not ReturnValue3_0:
            goto('L1329')
        ReturnValue2_0: Ptr[FGInventoryComponent] = self.mCrate.GetInventory()
        self.mInventory.Init(ReturnValue2_0)
        self.InitInventoryWidgetCallbacks(self.mInventory)
        # End
        self.Init()
        goto('L589')
        self.Tick(MyGeometry, InDeltaTime)
        goto('L10')
        self.Construct()
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
        OutputDelegate1.BindUFunction(self, OnGrabAll)
        self.Widget_GlowingFactoryButton.mButton.OnClicked.AddUnique(OutputDelegate1)
        Crate: Ptr[BP_Crate] = Cast[BP_Crate](self.mInteractObject)
        bSuccess1: bool = Crate
        self.mCrate = Crate
        # End
        self.Destruct()
        self.Cleanup()
        # End
        # Label 1095
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_5)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L1329')
        ReturnValue_6: Ptr[Pawn] = Controller.K2_GetPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_6)
        bSuccess2: bool = Player
        if not bSuccess2:
            goto('L1329')
        goto('L329')
        goto('L1095')
    
