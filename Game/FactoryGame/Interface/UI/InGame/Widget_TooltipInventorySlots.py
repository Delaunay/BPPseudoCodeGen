
from codegen.ue4_stub import *

from Script.Engine import Conv_StringToText
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import SetTextPropertyByName
from Script.Engine import PlayerController
from Script.UMG import AddChild
from Script.UMG import UserWidget
from Script.UMG import Create
from Game.FactoryGame.Interface.UI.InGame.Widget_TooltipInventorySlots import ExecuteUbergraph_Widget_TooltipInventorySlots
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetStringLibrary
from Game.FactoryGame.-Shared.Blueprint.BP_SchematicHelper import Default__BP_SchematicHelper
from Script.FactoryGame import FGSchematic
from Script.Engine import Conv_IntToString
from Script.UMG import PanelSlot
from Script.Engine import Concat_StrStr
from Script.Engine import IsValidClass
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Interface.UI.InGame.Widget_RewardInventoryItems import Widget_RewardInventoryItems

class Widget_TooltipInventorySlots(UserWidget):
    mSchematic: TSubclassOf[FGSchematic]
    
    def GetExtraInventorySlotText(self):
        
        numSlots = None
        Default__BP_SchematicHelper.GetNumInventorySlotsUnlocked(self.mSchematic, self, Ref[numSlots])
        ReturnValue: FString = Default__KismetStringLibrary.Conv_IntToString(numSlots)
        ReturnValue_0: FString = Default__KismetStringLibrary.Concat_StrStr("+", ReturnValue)
        ReturnValue1: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_0, " Inventory Slots")
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue1)
        NewParam = ReturnValue_1
    

    def GetExtraArmsSlotText(self):
        
        numSlots = None
        Default__BP_SchematicHelper.GetNumArmEquipmentSlotsUnlocked(self.mSchematic, self, Ref[numSlots])
        ReturnValue: FString = Default__KismetStringLibrary.Conv_IntToString(numSlots)
        ReturnValue_0: FString = Default__KismetStringLibrary.Concat_StrStr("+", ReturnValue)
        ReturnValue1: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_0, " Arms Slots")
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue1)
        NewParam = ReturnValue_1
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_TooltipInventorySlots(206)
    

    def ExecuteUbergraph_Widget_TooltipInventorySlots(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: Ptr[Widget_RewardInventoryItems] = Default__WidgetBlueprintLibrary.Create(self, Widget_RewardInventoryItems, None)
        
        NewParam = None
        self.GetExtraArmsSlotText(Ref[NewParam])
        
        NewParam = None
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue, "mText", Ref[NewParam])
        ReturnValue1: Ptr[PanelSlot] = self.mContainer.AddChild(ReturnValue)
        goto(ExecutionFlow.Pop())
        self.mContainer.ClearChildren()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValidClass(self.mSchematic)
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L596")
        
        Result = None
        Default__BP_SchematicHelper.GetUnlocksInventorySlot(self.mSchematic, self, Ref[Result])
        if not Result:
           goto(ExecutionFlow.Pop())
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[Widget_RewardInventoryItems] = Default__WidgetBlueprintLibrary.Create(self, Widget_RewardInventoryItems, ReturnValue_1)
        
        NewParam = None
        self.GetExtraInventorySlotText(Ref[NewParam])
        
        NewParam = None
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue1_0, "mText", Ref[NewParam])
        ReturnValue_2: Ptr[PanelSlot] = self.mContainer.AddChild(ReturnValue1_0)
        goto(ExecutionFlow.Pop())
        
        Result = None
        # Label 596
        Default__BP_SchematicHelper.GetUnlocksHandSlots(self.mSchematic, self, Ref[Result])
        if not Result:
           goto(ExecutionFlow.Pop())
        goto('L15')
    
