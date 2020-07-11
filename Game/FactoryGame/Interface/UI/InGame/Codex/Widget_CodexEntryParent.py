
from codegen.ue4_stub import *

from Script.Engine import SetTextPropertyByName
from Script.Engine import Conv_TextToString
from Script.Engine import Texture
from Script.Engine import Split
from Script.UMG import AddChildToVerticalBox
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_CodexEntryParent import ExecuteUbergraph_Widget_CodexEntryParent
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_CodexStats import Widget_CodexStats
from Script.Engine import PlayerController
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_CodexContent import Widget_CodexContent
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import Array_Append
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_CodexStatItem import Widget_CodexStatItem
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import GetAllWidgetsOfClass
from Script.UMG import VerticalBoxSlot
from Script.UMG import Create

class Widget_CodexEntryParent(Widget_CodexContent):
    mName: FText
    mIcon: Ptr[Texture]
    mRelatedEntries: List[Ptr[Widget_CodexContent]]
    mStats: List[FText]
    mAdditionalStats: List[FText]
    
    def GetStats(self):
        ExecutionFlow.Push("L2201")
        FoundWidgets: List[Ptr[Widget_CodexStats]] = []
        
        Default__WidgetBlueprintLibrary.GetAllWidgetsOfClass(self, Widget_CodexStats, False, Ref[FoundWidgets])
        Variable1: int32 = 0
        Variable1_0: int32 = 0
        
        # Label 114
        ReturnValue: int32 = len(FoundWidgets)
        ReturnValue_0: bool = Variable1 <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable1_0 = Variable1
        ExecutionFlow.Push("L2053")
        
        Item1 = None
        Item1 = FoundWidgets[Variable1_0]
        CodexStats = Item1
        CodexStats.mNameText.SetText(self.mName)
        SlateBrush.ImageSize = CodexStats.mIcon.Brush.ImageSize
        SlateBrush.Margin = CodexStats.mIcon.Brush.Margin
        SlateBrush.TintColor = CodexStats.mIcon.Brush.TintColor
        SlateBrush.ResourceObject = self.mIcon
        SlateBrush.DrawAs = CodexStats.mIcon.Brush.DrawAs
        SlateBrush.Tiling = CodexStats.mIcon.Brush.Tiling
        SlateBrush.Mirroring = CodexStats.mIcon.Brush.Mirroring
        
        SlateBrush = None
        CodexStats.mIcon.SetBrush(Ref[SlateBrush])
        
        Default__KismetArrayLibrary.Array_Append(Ref[self.mStats], Ref[self.mAdditionalStats])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 1123
        ReturnValue1: int32 = len(self.mStats)
        ReturnValue1_0: bool = Variable <= ReturnValue1
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L2127")
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Widget_CodexStatItem] = Default__WidgetBlueprintLibrary.Create(self, Widget_CodexStatItem, ReturnValue_1)
        
        Item = None
        Item = self.mStats[Variable_0]
        
        Item = None
        ReturnValue_3: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Item])
        
        LeftS = None
        RightS = None
        ReturnValue_4: bool = Default__KismetStringLibrary.Split(ReturnValue_3, ";", 1, 0, Ref[LeftS], Ref[RightS])
        ReturnValue1_1: FText = Default__KismetTextLibrary.Conv_StringToText(LeftS)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_2, "mInfo", Ref[ReturnValue1_1])
        
        Item = None
        Item = self.mStats[Variable_0]
        
        Item = None
        ReturnValue_3 = Default__KismetTextLibrary.Conv_TextToString(Ref[Item])
        
        LeftS = None
        RightS = None
        ReturnValue_4 = Default__KismetStringLibrary.Split(ReturnValue_3, ";", 1, 0, Ref[LeftS], Ref[RightS])
        ReturnValue_5: FText = Default__KismetTextLibrary.Conv_StringToText(RightS)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_2, "mValue", Ref[ReturnValue_5])
        ReturnValue_6: Ptr[VerticalBoxSlot] = CodexStats.mStatsContainer.AddChildToVerticalBox(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 2053
        ReturnValue_7: int32 = Variable1 + 1
        Variable1 = ReturnValue_7
        goto('L114')
        # Label 2127
        ReturnValue1_2: int32 = Variable + 1
        Variable = ReturnValue1_2
        goto('L1123')
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_CodexEntryParent(29)
    

    def ExecuteUbergraph_Widget_CodexEntryParent(self):
        # Label 10
        self.GetStats()
        # End
        goto('L10')
    
