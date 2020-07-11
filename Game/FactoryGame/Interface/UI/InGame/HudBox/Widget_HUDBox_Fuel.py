
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Fuel import ExecuteUbergraph_Widget_HUDBox_Fuel
from Script.UMG import GetOwningPlayerPawn
from Script.FactoryGame import GetFuelClass
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import FGItemDescriptor
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Fuel import ExecuteUbergraph_Widget_HUDBox_Fuel.K2Node_Event_MyGeometry
from Script.Engine import Pawn
from Script.FactoryGame import FGChainsaw
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Equipment_Parent import Widget_HUDBox_Equipment_Parent
from Script.Engine import Conv_IntToText
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Fuel import ExecuteUbergraph_Widget_HUDBox_Fuel.K2Node_Event_InDeltaTime
from Script.Engine import Default__KismetTextLibrary

class Widget_HUDBox_Fuel(Widget_HUDBox_Equipment_Parent):
    mFuelClass: TSubclassOf[FGItemDescriptor] = NewObject[Desc_Biofuel]()
    bHasScriptImplementedTick = True
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_HUDBox_Fuel(179)
    

    def Tick(self):
        ExecuteUbergraph_Widget_HUDBox_Fuel.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_HUDBox_Fuel.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_HUDBox_Fuel(324)
    

    def ExecuteUbergraph_Widget_HUDBox_Fuel(self):
        # Label 10
        Variable: bool = False
        if not Variable1:
            goto('L40')
        # End
        # Label 40
        Variable1: bool = True
        self.mHudBoxParent.StartWarningSign()
        # End
        # Label 92
        Variable1 = False
        self.mHudBoxParent.StopWarningSign()
        # End
        # Label 144
        if not Variable:
            goto('L163')
        # End
        # Label 163
        Variable = True
        goto('L92')
        AsFGChainsaw: Ptr[FGChainsaw] = Cast[FGChainsaw](self.mEquipment)
        bSuccess: bool = AsFGChainsaw
        if not bSuccess:
            goto('L911')
        ReturnValue: TSubclassOf[FGItemDescriptor] = AsFGChainsaw.GetFuelClass()
        self.mFuelClass = ReturnValue
        # End
        ReturnValue_0: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        numItems1 = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue_0, self.mFuelClass, self, Ref[numItems1])
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_IntToText(numItems1, False, True, 1, 324)
        self.mFuelCurrent.SetText(ReturnValue_1)
        ReturnValue1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue1, self.mFuelClass, self, Ref[numItems])
        ItemAmount.ItemClass = self.mFuelClass
        ItemAmount.amount = numItems
        ReturnValue1_0: bool = numItems > 0
        self.FuelSlot.Setup CostIcon(None, ItemAmount, None, 0, 0, False, False, ReturnValue1_0)
        ReturnValue1 = self.GetOwningPlayerPawn()
        
        numItems = None
        Default__HUDHelpers.GetNumItemsFromPlayerInventory(ReturnValue1, self.mFuelClass, self, Ref[numItems])
        ReturnValue_2: bool = numItems > 0
        if not ReturnValue_2:
            goto('L10')
        goto('L144')
    
