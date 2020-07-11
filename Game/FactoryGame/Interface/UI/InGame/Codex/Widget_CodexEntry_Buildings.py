
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_CodexEntryParent import Widget_CodexEntryParent
from Script.FactoryGame import GetBuildCategory
from Script.Engine import Texture2D
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_CodexEntry_Buildings import ExecuteUbergraph_Widget_CodexEntry_Buildings
from Script.FactoryGame import GetCategoryName
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetItemName
from Script.FactoryGame import GetBigIcon
from Script.Engine import Conv_FloatToText
from Script.FactoryGame import Default__FGBuildDescriptor
from Script.FactoryGame import GetPowerProduction
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import Default__FGBuildingDescriptor
from Script.Engine import Format
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import Default__FGBuildCategory
from Script.FactoryGame import FGBuildCategory
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_CodexEntry_Buildings import ExecuteUbergraph_Widget_CodexEntry_Buildings.K2Node_Event_IsDesignTime
from Script.FactoryGame import GetPowerConsumption
from Script.FactoryGame import FGBuildingDescriptor

class Widget_CodexEntry_Buildings(Widget_CodexEntryParent):
    BuildingType: TSubclassOf[FGBuildingDescriptor]
    
    def PreConstruct(self):
        ExecuteUbergraph_Widget_CodexEntry_Buildings.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_CodexEntry_Buildings(10)
    

    def ExecuteUbergraph_Widget_CodexEntry_Buildings(self):
        ReturnValue: FText = Default__FGItemDescriptor.GetItemName(self.BuildingType)
        self.mName = ReturnValue
        ReturnValue_0: float = Default__FGBuildingDescriptor.GetPowerConsumption(self.BuildingType)
        ReturnValue_1: bool = ReturnValue_0 > 0
        if not ReturnValue_1:
            goto('L752')
        ReturnValue_0 = Default__FGBuildingDescriptor.GetPowerConsumption(self.BuildingType)
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_0, 0, False, True, 1, 324, 0, 1)
        FormatArgumentData1.ArgumentName = "Power"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue_2
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData1]
        ReturnValue1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 608, 'Value': 'Power Consumption;{Power} MW'}", Array1)
        
        self.mStats = None
        ReturnValue1_0: int32 = self.mStats.append(ReturnValue1)
        # Label 752
        ReturnValue_3: float = Default__FGBuildingDescriptor.GetPowerProduction(self.BuildingType)
        ReturnValue1_1: bool = ReturnValue_3 > 0
        if not ReturnValue1_1:
            goto('L1407')
        ReturnValue_3 = Default__FGBuildingDescriptor.GetPowerProduction(self.BuildingType)
        ReturnValue1_2: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_3, 0, False, True, 1, 324, 0, 1)
        FormatArgumentData2.ArgumentName = "Power"
        FormatArgumentData2.ArgumentValueType = 4
        FormatArgumentData2.ArgumentValue = ReturnValue1_2
        FormatArgumentData2.ArgumentValueInt = 0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array2: List[FormatArgumentData] = [FormatArgumentData2]
        ReturnValue2: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1264, 'Value': 'Power Production;{Power} MW'}", Array2)
        
        self.mStats = None
        ReturnValue2_0: int32 = self.mStats.append(ReturnValue2)
        # Label 1407
        ReturnValue_4: TSubclassOf[FGBuildCategory] = Default__FGBuildDescriptor.GetBuildCategory(self.BuildingType)
        ReturnValue_5: FText = Default__FGBuildCategory.GetCategoryName(ReturnValue_4)
        FormatArgumentData.ArgumentName = "Category"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_5
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_6: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1783, 'Value': 'Building Category;{Category}'}", Array)
        
        self.mStats = None
        ReturnValue_7: int32 = self.mStats.append(ReturnValue_6)
        ReturnValue_8: Ptr[Texture2D] = Default__FGItemDescriptor.GetBigIcon(self.BuildingType)
        self.mIcon = ReturnValue_8
    
