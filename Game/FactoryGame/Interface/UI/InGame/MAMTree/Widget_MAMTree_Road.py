
from codegen.ue4_stub import *

from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import DrawLines
from Script.CoreUObject import Vector2D
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Interface.UI.InGame.MAMTree.MAMTree_Vector2D_Array import MAMTree_Vector2D_Array
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class Widget_MAMTree_Road(UserWidget):
    mHighlightTint: LinearColor = Namespace(A=1, B=0.118477001786232, G=0.118477001786232, R=0.11979199945926666)
    mDefaultTint: LinearColor = Namespace(A=1, B=0.05729199945926666, G=0.05612500011920929, R=0.05612500011920929)
    mThickness: float = 4
    mTempRoad: List[Vector2D]
    mConvertedRoadData: List[MAMTree_Vector2D_Array]
    mHighlightedRoadData: List[MAMTree_Vector2D_Array]
    Visibility = ESlateVisibility::HitTestInvisible
    
    def OnPaint(self):
        ExecutionFlow.Push("L906")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue1: int32 = len(self.mConvertedRoadData)
        ReturnValue1_0: bool = Variable <= ReturnValue1
        if not ReturnValue1_0:
            goto('L332')
        Variable_0 = Variable
        ExecutionFlow.Push("L758")
        
        Item1 = None
        Item1 = self.mConvertedRoadData[Variable_0]
        
        Item1.Vector2D_3_76B5E3A240A6EA60DBBF68A46C881CB3 = None
        Default__WidgetBlueprintLibrary.DrawLines(self.mDefaultTint, True, self.mThickness, Ref[Context], Ref[Item1.Vector2D_3_76B5E3A240A6EA60DBBF68A46C881CB3])
        goto(ExecutionFlow.Pop())
        
        # Label 332
        Default__WidgetBlueprintLibrary.DrawLines(LinearColor(R = 1, G = 0, B = 0.2193879932165146, A = 1), False, self.mThickness, Ref[Context], Ref[self.mTempRoad])
        Variable1: int32 = 0
        Variable1_0: int32 = 0
        
        # Label 472
        ReturnValue: int32 = len(self.mHighlightedRoadData)
        ReturnValue_0: bool = Variable1 <= ReturnValue
        if not ReturnValue_0:
            goto('L753')
        Variable1_0 = Variable1
        ExecutionFlow.Push("L832")
        
        Item = None
        Item = self.mHighlightedRoadData[Variable1_0]
        
        Item.Vector2D_3_76B5E3A240A6EA60DBBF68A46C881CB3 = None
        Default__WidgetBlueprintLibrary.DrawLines(self.mHighlightTint, True, self.mThickness, Ref[Context], Ref[Item.Vector2D_3_76B5E3A240A6EA60DBBF68A46C881CB3])
        goto(ExecutionFlow.Pop())
        # Label 753
        # End
        # Label 758
        ReturnValue_1: int32 = Variable + 1
        Variable = ReturnValue_1
        goto('L51')
        # Label 832
        ReturnValue1_1: int32 = Variable1 + 1
        Variable1 = ReturnValue1_1
        goto('L472')
    
