
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import UserWidget
from Script.FactoryGame import Default__FGBuildingDescriptor
from Script.Engine import FormatArgumentData
from Script.Engine import Conv_FloatToText
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu_PowerProduction import ExecuteUbergraph_Widget_BuildMenu_PowerProduction
from Script.FactoryGame import GetPowerConsumption
from Script.Engine import IsValidClass
from Script.FactoryGame import GetPowerProduction
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu_PowerProduction import ExecuteUbergraph_Widget_BuildMenu_PowerProduction.K2Node_Event_IsDesignTime
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import FGBuildingDescriptor

class Widget_BuildMenu_PowerProduction(UserWidget):
    mBuildingDesc: TSubclassOf[FGBuildingDescriptor]
    
    def GetStatText(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mBuildingDesc)
        if not ReturnValue:
            goto('L999')
        ReturnValue_0: float = Default__FGBuildingDescriptor.GetPowerProduction(self.mBuildingDesc)
        ReturnValue1: bool = ReturnValue_0 > 0.10000000149011612
        if not ReturnValue1:
            goto('L705')
        ReturnValue_0 = Default__FGBuildingDescriptor.GetPowerProduction(self.mBuildingDesc)
        ReturnValue1_0: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_0, 0, False, True, 1, 324, 0, 3)
        FormatArgumentData.ArgumentName = "Value"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue1_0
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_1: FText = Default__KismetTextLibrary.Format(STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/ST_Units.ST_Units", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 635, 'Value': 'Value_MW'}", Array)
        self.mStatText.SetText(ReturnValue_1)
        # End
        # Label 705
        ReturnValue_2: float = Default__FGBuildingDescriptor.GetPowerConsumption(self.mBuildingDesc)
        ReturnValue_3: bool = ReturnValue_2 > 0.10000000149011612
        if not ReturnValue_3:
            goto('L999')
        ReturnValue_2 = Default__FGBuildingDescriptor.GetPowerConsumption(self.mBuildingDesc)
        ReturnValue_4: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_2, 0, False, True, 1, 324, 0, 3)
        self.mStatText.SetText(ReturnValue_4)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_BuildMenu_PowerProduction.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_BuildMenu_PowerProduction(29)
    

    def ExecuteUbergraph_Widget_BuildMenu_PowerProduction(self):
        # Label 10
        self.GetStatText()
        # End
        goto('L10')
    
