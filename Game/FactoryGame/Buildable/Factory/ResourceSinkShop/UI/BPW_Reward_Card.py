
from codegen.ue4_stub import *

from Script.UMG import UserWidget
from Script.Engine import FormatArgumentData
from Script.UMG import Create
from Script.UMG import Widget
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_Reward_Card import ExecuteUbergraph_BPW_Reward_Card.K2Node_Event_IsDesignTime
from Script.Engine import Format
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.UI.BPW_Reward_Card import ExecuteUbergraph_BPW_Reward_Card
from Script.CoreUObject import Object
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Unlocks.FUnlockDataStruct import FUnlockDataStruct
from Game.FactoryGame.Interface.UI.InGame.Widget_Tooltip import Widget_Tooltip
from Script.Engine import Conv_IntToText
from Script.Engine import Default__KismetTextLibrary

class BPW_Reward_Card(UserWidget):
    mItemNameText: FText
    mIconPreviewTexture: Ptr[Object]
    mUnlockDataStruct: FUnlockDataStruct
    mAmountText: FText
    
    def SetAmountText(self, UnlockDataStruct: FUnlockDataStruct):
        ReturnValue: bool = UnlockDataStruct.UnlockAmount_13_F32234CC46ECA4C99973A28AA05BE30E > 0
        if not ReturnValue:
            goto('L526')
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_IntToText(UnlockDataStruct.UnlockAmount_13_F32234CC46ECA4C99973A28AA05BE30E, False, True, 1, 324)
        self.mAmountText = ReturnValue_0
        FormatArgumentData.ArgumentName = "A"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = self.mAmountText
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 423, 'Value': 'x {A}'}", Array)
        self.mAmount.SetText(ReturnValue_1)
        # End
        # Label 526
        self.mAmountText = 
        self.mAmount.SetText(self.mAmountText)
    

    def CreateTooltipWidget(self):
        ReturnValue: Ptr[Widget_Tooltip] = Default__WidgetBlueprintLibrary.Create(self, Widget_Tooltip, None)
        ReturnValue_0: Ptr[Widget] = ReturnValue
    

    def SetName(self, UnlockDataStruct: FUnlockDataStruct):
        self.mItemNameText = UnlockDataStruct.UnlockName_2_490383D6421D4A92D86E1F835769488A
        self.mItemName.SetText(self.mItemNameText)
    

    def SetIcon(self, UnlockDataStruct: FUnlockDataStruct):
        self.mIconPreviewTexture = UnlockDataStruct.UnlockIcon_9_3E3B124C41C68907A6EB9FAD36C04BC4
        SlateBrush.ImageSize = self.mIconPreview.Brush.ImageSize
        SlateBrush.Margin = self.mIconPreview.Brush.Margin
        SlateBrush.TintColor = self.mIconPreview.Brush.TintColor
        SlateBrush.ResourceObject = self.mIconPreviewTexture
        SlateBrush.DrawAs = self.mIconPreview.Brush.DrawAs
        SlateBrush.Tiling = self.mIconPreview.Brush.Tiling
        SlateBrush.Mirroring = self.mIconPreview.Brush.Mirroring
        
        SlateBrush = None
        self.mIconPreview.SetBrush(Ref[SlateBrush])
    

    def PreConstruct(self):
        ExecuteUbergraph_BPW_Reward_Card.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_Reward_Card(38)
    

    def ExecuteUbergraph_BPW_Reward_Card(self):
        # Label 10
        self.SetAmountText(self.mUnlockDataStruct)
        # End
        self.SetIcon(self.mUnlockDataStruct)
        self.SetName(self.mUnlockDataStruct)
        goto('L10')
    
