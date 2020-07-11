
from codegen.ue4_stub import *

from Script.FactoryGame import GetConsumeable
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Consumable import ExecuteUbergraph_Widget_HUDBox_Consumable
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Equipment_Parent import Widget_HUDBox_Equipment_Parent
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Consumable import ExecuteUbergraph_Widget_HUDBox_Consumable.K2Node_Event_InDeltaTime
from Script.Engine import Conv_IntToText
from Script.FactoryGame import FGConsumableEquipment
from Game.FactoryGame.Interface.UI.InGame.HudBox.Widget_HUDBox_Consumable import ExecuteUbergraph_Widget_HUDBox_Consumable.K2Node_Event_MyGeometry

class Widget_HUDBox_Consumable(Widget_HUDBox_Equipment_Parent):
    mConsumableEquipment: Ptr[FGConsumableEquipment]
    bHasScriptImplementedTick = True
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_HUDBox_Consumable(10)
    

    def Tick(self):
        ExecuteUbergraph_Widget_HUDBox_Consumable.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_HUDBox_Consumable.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_HUDBox_Consumable(113)
    

    def ExecuteUbergraph_Widget_HUDBox_Consumable(self):
        Equipment: Ptr[FGConsumableEquipment] = Cast[FGConsumableEquipment](self.mEquipment)
        bSuccess: bool = Equipment
        if not bSuccess:
            goto('L279')
        self.mConsumableEquipment = Equipment
        # End
        
        consumeable = None
        numConsumeable = None
        self.mConsumableEquipment.GetConsumeable(Ref[consumeable], Ref[numConsumeable])
        ReturnValue: FText = Default__KismetTextLibrary.Conv_IntToText(numConsumeable, False, True, 1, 324)
        self.mAmountObject.SetText(ReturnValue)
    
