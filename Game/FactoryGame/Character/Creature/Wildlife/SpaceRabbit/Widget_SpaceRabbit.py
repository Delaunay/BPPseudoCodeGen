
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Actor
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Destruct
from Script.CoreUObject import LinearColor
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.Engine import GetComponentByClass
from Script.FactoryGame import Init
from Script.Engine import IsValid
from Script.FactoryGame import FGInventoryComponent
from Script.FactoryGame import FGCreature
from Script.Engine import PrintString
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Widget_SpaceRabbit import ExecuteUbergraph_Widget_SpaceRabbit

class Widget_SpaceRabbit(Widget_UseableBase):
    mSpaceRabbit: Ptr[FGCreature]
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
    
    def DropInventorySlotStack(self):
        
        Result = None
        self.DropInventoryStackOnInventoryWidget(InventorySlot, self.mInventoryUI, Ref[Result])
        WasStackMoved = Result
    

    def Cleanup(self):
        self.Widget_Window_DarkMode.OnClose.Clear()
    

    def Init(self):
        self.ExecuteUbergraph_Widget_SpaceRabbit(10)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SpaceRabbit(1034)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_SpaceRabbit(1049)
    

    def ExecuteUbergraph_Widget_SpaceRabbit(self):
        self.Init()
        AsActor: Ptr[Actor] = Cast[Actor](self.mInteractObject)
        bSuccess: bool = AsActor
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(AsActor)
        ReturnValue_0: Ptr[FGInventoryComponent] = AsActor.GetComponentByClass(FGInventoryComponent)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        ReturnValue_1: bool = ReturnValue and ReturnValue1
        if not ReturnValue_1:
            goto('L890')
        AsActor = Cast[Actor](self.mInteractObject)
        bSuccess = AsActor
        ReturnValue_0 = AsActor.GetComponentByClass(FGInventoryComponent)
        self.mInventoryUI.Init(ReturnValue_0)
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.Remove(OutputDelegate)
        Variable: int32 = 0
        
        self.mInventoryUI.mInventorySlots = None
        # Label 538
        ReturnValue_2: int32 = len(self.mInventoryUI.mInventorySlots)
        ReturnValue_3: bool = Variable <= ReturnValue_2
        if not ReturnValue_3:
            goto('L1073')
        
        self.mInventoryUI.mInventorySlots = None
        Item = None
        Item = self.mInventoryUI.mInventorySlots[Variable]
        OutputDelegate1.BindUFunction(self, OnInventorySlotStackMove)
        Item.OnMoveStack.AddUnique(OutputDelegate1)
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L538')
        # Label 890
        Default__KismetSystemLibrary.PrintString(self, "Error::Invalid input class in Widget_SpaceRabbit, INVESTIGATE! ", False, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        # End
        self.Construct()
        # End
        self.Destruct()
        self.Cleanup()
    
