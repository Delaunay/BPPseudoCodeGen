
from codegen.ue4_stub import *

from Script.FactoryGame import GetActiveSchematic
from Script.FactoryGame import GetCost
from Script.FactoryGame import GetItemIcon
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetTechTier
from Script.CoreUObject import Object
from Script.Engine import IsValid
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.FactoryGame import GetPaidOffCostFor
from Script.Engine import Format
from Script.FactoryGame import GetTimeUntilShipReturn
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import FGBuildableTradingPost
from Script.FactoryGame import FGSchematic
from Script.UMG import UserWidget
from Script.FactoryGame import IsShipAtTradingPost
from Script.FactoryGame import FGSchematicManager
from Script.FactoryGame import Default__FGSchematic
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost import Widget_TradingPost
from Script.FactoryGame import IsSchematicPaidOff
from Script.SlateCore import SlateBrush
from Script.FactoryGame import ItemAmount
from Script.FactoryGame import Default__FGSchematicManager
from Script.Engine import IsValidClass
from Script.FactoryGame import GetSchematicDisplayName
from Game.FactoryGame.Buildable.Factory.TradingPost.UI.Hub_PodIcon import Hub_PodIcon
from Script.Engine import TimeSecondsToString

class Widget_TradingPost_ShipAwayFeedback(UserWidget):
    mTradingPost: Ptr[FGBuildableTradingPost]
    mTradingPostWidget: Ptr[Widget_TradingPost]
    CategoryIconImage: Ptr[Object]
    mIsShipAtHub: bool
    
    def GetProgressBarVisibility(self):
        ReturnValue = 2
    

    def GetProgressbarPercent(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L381')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_2: float = ReturnValue_0.GetTimeUntilShipReturn()
        ReturnValue_3: float = ReturnValue_2 / 360
        ReturnValue_4: float = 1 - ReturnValue_3
        ReturnValue_5: float = ReturnValue_4
        goto('L404')
        # Label 381
        ReturnValue_5 = 0
    

    def GetSchematicTitle(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L1965')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_2: bool = ReturnValue_0.IsShipAtTradingPost()
        if not ReturnValue_2:
            goto('L1669')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_3: TSubclassOf[FGSchematic] = ReturnValue_0.GetActiveSchematic()
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_3)
        if not ReturnValue_4:
            goto('L1709')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_3 = ReturnValue_0.GetActiveSchematic()
        ReturnValue_5: bool = ReturnValue_0.IsSchematicPaidOff(ReturnValue_3)
        if not ReturnValue_5:
            goto('L1794')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_3 = ReturnValue_0.GetActiveSchematic()
        ReturnValue_6: int32 = Default__FGSchematic.GetTechTier(ReturnValue_3)
        ReturnValue_7: bool = ReturnValue_6 > 0
        if not ReturnValue_7:
            goto('L1881')
        TitleInfo = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 879, 'Value': 'Ready for Launch!'}"
        # Label 934
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_3 = ReturnValue_0.GetActiveSchematic()
        ReturnValue_8: FText = Default__FGSchematic.GetSchematicDisplayName(ReturnValue_3)
        FormatArgumentData.ArgumentName = "Title"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_8
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "Info"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = TitleInfo
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData, FormatArgumentData1]
        ReturnValue_9: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1573, 'Value': '{Title} - {Info}'}", Array)
        ReturnValue_10: FText = ReturnValue_9
        goto('L1965')
        # Label 1669
        ReturnValue_10 = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1689, 'Value': 'Pod Launched!'}"
        goto('L1965')
        # Label 1709
        ReturnValue_10 = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1729, 'Value': 'No Selected Schematic!'}"
        goto('L1965')
        # Label 1794
        TitleInfo = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1814, 'Value': 'Waiting for resources...'}"
        goto('L934')
        # Label 1881
        TitleInfo = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1901, 'Value': 'Ready to Upgrade Hub!'}"
        goto('L934')
    

    def GetScematicIcon(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L1557')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_2: bool = ReturnValue_0.IsShipAtTradingPost()
        if not ReturnValue_2:
            goto('L1100')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_3: TSubclassOf[FGSchematic] = ReturnValue_0.GetActiveSchematic()
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_3)
        if not ReturnValue_4:
            goto('L1557')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_3 = ReturnValue_0.GetActiveSchematic()
        ReturnValue_5: SlateBrush = Default__FGSchematic.GetItemIcon(ReturnValue_3)
        SlateBrush1.ImageSize = self.SchematicIcon.Brush.ImageSize
        SlateBrush1.Margin = self.SchematicIcon.Brush.Margin
        SlateBrush1.TintColor = self.SchematicIcon.Brush.TintColor
        SlateBrush1.ResourceObject = ReturnValue_5.ResourceObject
        SlateBrush1.DrawAs = self.SchematicIcon.Brush.DrawAs
        # Label 934
        SlateBrush1.Tiling = self.SchematicIcon.Brush.Tiling
        SlateBrush1.Mirroring = self.SchematicIcon.Brush.Mirroring
        ReturnValue_6: SlateBrush = SlateBrush1
        goto('L1557')
        # Label 1100
        SlateBrush.ImageSize = self.SchematicIcon.Brush.ImageSize
        SlateBrush.Margin = self.SchematicIcon.Brush.Margin
        SlateBrush.TintColor = self.SchematicIcon.Brush.TintColor
        SlateBrush.ResourceObject = Hub_PodIcon
        SlateBrush.DrawAs = self.SchematicIcon.Brush.DrawAs
        SlateBrush.Tiling = self.SchematicIcon.Brush.Tiling
        SlateBrush.Mirroring = self.SchematicIcon.Brush.Mirroring
        ReturnValue_6 = SlateBrush
    

    def GetShipTimerText(self):
        ExecutionFlow.Push("L2696")
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue1)
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_0)
        if not ReturnValue:
            goto('L1409')
        ReturnValue1 = self.GetOwningPlayer()
        ReturnValue1_0 = Default__FGSchematicManager.Get(ReturnValue1)
        ReturnValue_0: TSubclassOf[FGSchematic] = ReturnValue1_0.GetActiveSchematic()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValidClass(ReturnValue_0)
        if not ReturnValue_1:
            goto('L1409')
        ReturnValue1 = self.GetOwningPlayer()
        ReturnValue1_0 = Default__FGSchematicManager.Get(ReturnValue1)
        ReturnValue_2: bool = ReturnValue1_0.IsShipAtTradingPost()
        if not ReturnValue_2:
            goto('L1434')
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 504
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue2_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue2)
        ReturnValue1_1: TSubclassOf[FGSchematic] = ReturnValue2_0.GetActiveSchematic()
        ReturnValue_3: List[ItemAmount] = ReturnValue2_0.GetPaidOffCostFor(ReturnValue1_1)
        
        ReturnValue_4: int32 = len(ReturnValue_3)
        ReturnValue_5: bool = Variable <= ReturnValue_4
        if not ReturnValue_5:
            goto('L2045')
        Variable_0 = Variable
        ExecutionFlow.Push("L2622")
        ReturnValue2 = self.GetOwningPlayer()
        ReturnValue2_0 = Default__FGSchematicManager.Get(ReturnValue2)
        ReturnValue1_1 = ReturnValue2_0.GetActiveSchematic()
        ReturnValue_3 = ReturnValue2_0.GetPaidOffCostFor(ReturnValue1_1)
        
        Item = None
        Item = ReturnValue_3[Variable_0]
        ReturnValue2_1: int32 = TotalPaidOff + Item.amount
        TotalPaidOff = ReturnValue2_1
        ReturnValue2 = self.GetOwningPlayer()
        ReturnValue2_0 = Default__FGSchematicManager.Get(ReturnValue2)
        ReturnValue1_1 = ReturnValue2_0.GetActiveSchematic()
        ReturnValue_6: List[ItemAmount] = Default__FGSchematic.GetCost(ReturnValue1_1)
        ReturnValue1_2: int32 = totalCost + ReturnValue_6[Variable_0].amount
        totalCost = ReturnValue1_2
        goto(ExecutionFlow.Pop())
        # Label 1409
        ReturnValue_7: FText = 
        goto('L2696')
        # Label 1434
        ReturnValue_8: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_9: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue_8)
        ReturnValue_10: float = ReturnValue_9.GetTimeUntilShipReturn()
        ReturnValue_11: FString = Default__KismetStringLibrary.TimeSecondsToString(ReturnValue_10)
        ReturnValue_12: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_11)
        FormatArgumentData.ArgumentName = "Time"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_12
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_13: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1939, 'Value': 'Pod will return in: {Time}'}", Array)
        ReturnValue_7 = ReturnValue_13
        goto('L2696')
        # Label 2045
        FormatArgumentData1.ArgumentName = "PaidOff"
        FormatArgumentData1.ArgumentValueType = 0
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = TotalPaidOff
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        FormatArgumentData2.ArgumentName = "Cost"
        FormatArgumentData2.ArgumentValueType = 0
        FormatArgumentData2.ArgumentValue = 
        FormatArgumentData2.ArgumentValueInt = totalCost
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData2]
        ReturnValue1_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2504, 'Value': 'Total parts recieved: {PaidOff}/{Cost}'}", Array1)
        ReturnValue_7 = ReturnValue1_3
        goto('L2696')
        # Label 2622
        ReturnValue_14: int32 = Variable + 1
        Variable = ReturnValue_14
        goto('L504')
    
