
from codegen.ue4_stub import *

from Script.FactoryGame import Default__FGResearchTree
from Script.UMG import SetSize
from Game.FactoryGame.Interface.UI.InGame.MAMTree.Widget_MAMTree_Node import Widget_MAMTree_Node
from Script.UMG import CanvasPanelSlot
from Game.FactoryGame.Interface.UI.InGame.MAMTree.Widget_MAMTree_Grid import ExecuteUbergraph_Widget_MAMTree_Grid.K2Node_CustomEvent_NodeObjects
from Script.FactoryGame import IsResesearchTreeUnlocked
from Script.Engine import Delay
from Script.Engine import EqualEqual_ByteByte
from Script.UMG import AddChildToCanvas
from Script.Engine import GreaterEqual_IntInt
from Script.FactoryGame import GetNodes
from Script.Engine import Not_PreBool
from Game.FactoryGame.Interface.UI.InGame.MAMTree.MAMTree_RoadOccupiedTile import MAMTree_RoadOccupiedTile
from Script.FactoryGame import FGResearchTreeNode
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Interface.UI.InGame.MAMTree.MAMTree_NodeData_Struct import MAMTree_NodeData_Struct
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Default__FGResearchManager
from Script.Engine import PlayerController
from Script.FactoryGame import Get
from Script.Engine import Map_Remove
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import Map_Clear
from Script.Engine import Divide_Vector2DFloat
from Script.UMG import Unhandled
from Game.FactoryGame.Interface.UI.InGame.MAMTree.EMamTree_NodeStates import EMamTree_NodeStates
from Script.Engine import FormatArgumentData
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Array_Append
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Map_Values
from Game.FactoryGame.Interface.UI.InGame.EDirection import EDirection
from Script.FactoryGame import IsResearchBeingConducted
from Script.Engine import BreakVector2D
from Script.Engine import Map_Length
from Script.Engine import SetBoolPropertyByName
from Script.UMG import CanvasPanel
from Script.CoreUObject import LinearColor
from Script.Engine import Array_AddUnique
from Script.Engine import Concat_StrStr
from Script.Engine import Format
from Script.FactoryGame import FGResearchManager
from Script.Engine import Percent_IntInt
from Game.FactoryGame.Interface.UI.InGame.MAMTree.MAMTree_RoadStartEnd import MAMTree_RoadStartEnd
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import Conv_IntToString
from Script.Engine import NotEqual_ByteByte
from Game.FactoryGame.Interface.UI.InGame.MAMTree.MAMTree_Vector2D_Array import MAMTree_Vector2D_Array
from Script.UMG import UserWidget
from Script.Engine import Map_Find
from Script.Engine import Map_Add
from Script.FactoryGame import IsSchematicPurchased
from Game.FactoryGame.Interface.UI.InGame.-Shared.IntVector2d import IntVector2D
from Script.FactoryGame import FGSchematicManager
from Script.UMG import Create
from Script.FactoryGame import FGResearchTree
from Script.CoreUObject import Vector2D
from Script.Engine import Map_Keys
from Script.UMG import SetPosition
from Game.FactoryGame.Interface.UI.InGame.MAMTree.Widget_MAMTree_Grid import ExecuteUbergraph_Widget_MAMTree_Grid
from Game.FactoryGame.Schematics.Research.BPD_ResearchTreeNode import BPD_ResearchTreeNode
from Script.Engine import Default__BlueprintMapLibrary
from Script.FactoryGame import Default__FGSchematicManager
from Script.Engine import Array_Clear
from Script.Engine import Add_Vector2DVector2D
from Script.Engine import IsValidClass
from Script.Engine import PrintString
from Script.UMG import EventReply
from Game.FactoryGame.Interface.UI.InGame.MAMTree.Widget_MAMTree_Road import Widget_MAMTree_Road

class Widget_MAMTree_Grid(UserWidget):
    mTileSize: Vector2D = Namespace(X=128, Y=128)
    mNodeData: Dict[IntVector2D, MAMTree_NodeData_Struct]
    mGridSize: IntVector2D = Namespace(X_2_3FF107F84D30EB52DD50898C7D2CAD67=7, Y_4_F18C5B824136D7759146338CAA496F0A=12)
    mSelectedNodeCoordinates: IntVector2D = Namespace(X_2_3FF107F84D30EB52DD50898C7D2CAD67=-1, Y_4_F18C5B824136D7759146338CAA496F0A=-1)
    mLastRoadDirection: uint8 = 2
    mRoadOccupiedTiles: Dict[IntVector2D, MAMTree_RoadOccupiedTile]
    mTempRoadOccupiedTiles: List[IntVector2D]
    mNodeObjects: Dict[IntVector2D, Widget_MAMTree_Node*]
    mUnHiddenNodes: List[IntVector2D]
    SelectedResearchTree: TSubclassOf[FGResearchTree]
    mConvertedRoadData: List[MAMTree_Vector2D_Array]
    mAllResearchTrees: List[TSubclassOf[FGResearchTree]]
    OnLoadClicked: FMulticastScriptDelegate
    OnSaveTree: FMulticastScriptDelegate
    mParentGridCanvas: Ptr[CanvasPanel]
    mParentNodeCavas: Ptr[CanvasPanel]
    mParentRoads: Ptr[Widget_MAMTree_Road]
    OnResearchSelectedSchematic: FMulticastScriptDelegate
    mConvertedHighlightRoadData: List[MAMTree_Vector2D_Array]
    mIsEditor: bool
    
    def OnPreviewMouseButtonDown(self):
        ReturnValue: bool = Not_PreBool(self.mIsEditor)
        if not ReturnValue:
            goto('L411')
        
        IsValid = None
        self.IsSelectedNodeValid(Ref[IsValid])
        if not IsValid:
            goto('L411')
        
        Value = None
        ReturnValue_0: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeObjects], Ref[self.mSelectedNodeCoordinates], Ref[Value])
        ReturnValue_1: bool = Value.IsHovered()
        ReturnValue1: bool = Not_PreBool(ReturnValue_1)
        if not ReturnValue1:
            goto('L334')
        self.ResetSelectedNode()
        ReturnValue1_0: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_2: EventReply = ReturnValue1_0
        goto('L411')
        # Label 334
        ReturnValue_3: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_2 = ReturnValue_3
    

    def GetNodeState(self, Coordinates: IntVector2D, NewNodeData: Dict[IntVector2D, MAMTree_NodeData_Struct]):
        ExecutionFlow.Push("L2294")
        IsAvailable = False
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue1)
        
        Value = None
        ReturnValue: bool = Default__BlueprintMapLibrary.Map_Find(Ref[NewNodeData], Ref[Coordinates], Ref[Value])
        ReturnValue_0: bool = ReturnValue1_0.IsResearchBeingConducted(Value.Schematic_27_3663A42446FDB4387D0C81AFC23E225B)
        ReturnValue2: bool = Not_PreBool(ReturnValue_0)
        if not ReturnValue2:
            goto('L1216')
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue_1)
        ReturnValue_3: bool = ReturnValue_2.IsResesearchTreeUnlocked(self.SelectedResearchTree)
        if not ReturnValue_3:
            goto('L1241')
        
        Value1 = None
        ReturnValue1_1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[NewNodeData], Ref[Coordinates], Ref[Value1])
        ReturnValue_4: bool = self.IsSchematicResearched(Value1.Schematic_27_3663A42446FDB4387D0C81AFC23E225B)
        ReturnValue3: bool = Not_PreBool(ReturnValue_4)
        # Label 543
        if not ReturnValue3:
            goto('L1266')
        IsAvailable = True
        IsUnhidden = True
        Variable1: bool = False
        Variable: int32 = 0
        Variable1_0: int32 = 0
        # Label 636
        ReturnValue1_2: bool = Not_PreBool(Variable1)
        
        Value4 = None
        ReturnValue4: bool = Default__BlueprintMapLibrary.Map_Find(Ref[NewNodeData], Ref[Coordinates], Ref[Value4])
        
        Value4.Parents_20_7A099B96409362536B743BA1CC77C234 = None
        ReturnValue1_3: int32 = len(Value4.Parents_20_7A099B96409362536B743BA1CC77C234)
        ReturnValue1_4: bool = Variable <= ReturnValue1_3
        ReturnValue1_5: bool = ReturnValue1_2 and ReturnValue1_4
        if not ReturnValue1_5:
            goto('L1291')
        # Label 892
        Variable1_0 = Variable
        ExecutionFlow.Push("L2220")
        IsAvailable = False
        
        Value4 = None
        ReturnValue4 = Default__BlueprintMapLibrary.Map_Find(Ref[NewNodeData], Ref[Coordinates], Ref[Value4])
        
        Value4.Parents_20_7A099B96409362536B743BA1CC77C234 = None
        Item1 = None
        Item1 = Value4.Parents_20_7A099B96409362536B743BA1CC77C234[Variable1_0]
        
        Item1 = None
        Value5 = None
        ReturnValue5: bool = Default__BlueprintMapLibrary.Map_Find(Ref[NewNodeData], Ref[Item1], Ref[Value5])
        ReturnValue2_0: bool = self.IsSchematicResearched(Value5.Schematic_27_3663A42446FDB4387D0C81AFC23E225B)
        if not ReturnValue2_0:
           goto(ExecutionFlow.Pop())
        IsAvailable = True
        Variable1 = True
        goto(ExecutionFlow.Pop())
        # Label 1216
        NodeState = 4
        # End
        # Label 1241
        NodeState = 3
        # Label 1261
        # End
        # Label 1266
        NodeState = 2
        # End
        # Label 1291
        Variable_0: bool = False
        Variable1_1: int32 = 0
        Variable_1: int32 = 0
        # Label 1348
        ReturnValue_5: bool = Not_PreBool(Variable_0)
        
        Value2 = None
        ReturnValue2_1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[NewNodeData], Ref[Coordinates], Ref[Value2])
        
        Value2.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63 = None
        ReturnValue_6: int32 = len(Value2.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63)
        ReturnValue_7: bool = Variable1_1 <= ReturnValue_6
        ReturnValue_8: bool = ReturnValue_5 and ReturnValue_7
        if not ReturnValue_8:
            goto('L2002')
        Variable_1 = Variable1_1
        ExecutionFlow.Push("L1928")
        IsUnhidden = False
        
        Value2 = None
        ReturnValue2_1 = Default__BlueprintMapLibrary.Map_Find(Ref[NewNodeData], Ref[Coordinates], Ref[Value2])
        
        Value2.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63 = None
        Item = None
        Item = Value2.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63[Variable_1]
        
        Item = None
        Value3 = None
        ReturnValue3_0: bool = Default__BlueprintMapLibrary.Map_Find(Ref[NewNodeData], Ref[Item], Ref[Value3])
        ReturnValue1_6: bool = self.IsSchematicResearched(Value3.Schematic_27_3663A42446FDB4387D0C81AFC23E225B)
        if not ReturnValue1_6:
           goto(ExecutionFlow.Pop())
        IsUnhidden = True
        Variable_0 = True
        goto(ExecutionFlow.Pop())
        # Label 1928
        ReturnValue1_7: int32 = Variable1_1 + 1
        Variable1_1 = ReturnValue1_7
        goto('L1348')
        # Label 2002
        Variable_2: uint8 = 3
        Variable1_2: uint8 = 1
        Variable_3: bool = IsUnhidden
        Variable2: uint8 = 0
        Variable1_3: bool = IsAvailable
        
        switch = {
            False: Variable1_2,
            True: Variable2
        }
        
        switch_0 = {
            False: Variable_2,
            True: switch.get(Variable1_3, None)
        }
        NodeState = switch_0.get(Variable_3, None)
        # End
        # Label 2220
        ReturnValue_9: int32 = Variable + 1
        Variable = ReturnValue_9
        goto('L636')
    

    def IsSchematicResearched(self, SchematicClass: TSubclassOf[FGSchematic]):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_1: bool = ReturnValue_0.IsSchematicPurchased(SchematicClass)
        ReturnValue_2: bool = ReturnValue_1
    

    def ResetSelectedNode(self):
        
        Value = None
        ReturnValue: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeObjects], Ref[self.mSelectedNodeCoordinates], Ref[Value])
        if not ReturnValue:
            goto('L310')
        
        Value = None
        ReturnValue = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeObjects], Ref[self.mSelectedNodeCoordinates], Ref[Value])
        Value.SetIsSelected(False)
        IntVector2D.X_2_3FF107F84D30EB52DD50898C7D2CAD67 = -1
        IntVector2D.Y_4_F18C5B824136D7759146338CAA496F0A = -1
        self.mSelectedNodeCoordinates = IntVector2D
        self.TellNodesIfOtherNodeIsSelected(False)
        self.OnNodeClicked(False)
    

    def OnResearchStarted(self):
        
        IsValid = None
        self.IsSelectedNodeValid(Ref[IsValid])
        if not IsValid:
            goto('L143')
        
        Value = None
        ReturnValue: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[self.mSelectedNodeCoordinates], Ref[Value])
        self.OnResearchSelectedSchematic.ProcessMulticastDelegate(Value.Schematic_27_3663A42446FDB4387D0C81AFC23E225B)
    

    def OnParentNodeUnhovered(self, Coordinates: IntVector2D):
        ExecutionFlow.Push("L1171")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        Value2 = None
        # Label 51
        ReturnValue2: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[Coordinates], Ref[Value2])
        
        Value2.NodesToUnhide_33_A6E465554D49C98EE2A0ECB493BE5CBA = None
        ReturnValue1: int32 = len(Value2.NodesToUnhide_33_A6E465554D49C98EE2A0ECB493BE5CBA)
        ReturnValue1_0: bool = Variable <= ReturnValue1
        if not ReturnValue1_0:
            goto('L516')
        Variable_0 = Variable
        ExecutionFlow.Push("L1097")
        
        Value2 = None
        ReturnValue2 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[Coordinates], Ref[Value2])
        
        Value2.NodesToUnhide_33_A6E465554D49C98EE2A0ECB493BE5CBA = None
        Item1 = None
        Item1 = Value2.NodesToUnhide_33_A6E465554D49C98EE2A0ECB493BE5CBA[Variable_0]
        
        Item1 = None
        Value3 = None
        ReturnValue3: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeObjects], Ref[Item1], Ref[Value3])
        Value3.ShowHideUnlockIcon(False)
        goto(ExecutionFlow.Pop())
        # Label 516
        Variable1: int32 = 0
        Variable1_0: int32 = 0
        
        Value = None
        # Label 562
        ReturnValue: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[Coordinates], Ref[Value])
        
        Value.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63 = None
        ReturnValue_0: int32 = len(Value.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63)
        ReturnValue_1: bool = Variable1 <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable1_0 = Variable1
        ExecutionFlow.Push("L1023")
        
        Value = None
        ReturnValue = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[Coordinates], Ref[Value])
        
        Value.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63 = None
        Item = None
        Item = Value.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63[Variable1_0]
        
        Item = None
        Value1 = None
        ReturnValue1_1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeObjects], Ref[Item], Ref[Value1])
        Value1.ShowHideKeyIcon(False)
        goto(ExecutionFlow.Pop())
        # Label 1023
        ReturnValue1_2: int32 = Variable1 + 1
        Variable1 = ReturnValue1_2
        goto('L562')
        # Label 1097
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L51')
    

    def OnParentNodeHovered(self, Coordinates: IntVector2D):
        ExecutionFlow.Push("L2657")
        
        Value1 = None
        ReturnValue1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[Coordinates], Ref[Value1])
        ReturnValue: bool = self.IsSchematicResearched(Value1.Schematic_27_3663A42446FDB4387D0C81AFC23E225B)
        ReturnValue1_0: bool = Not_PreBool(ReturnValue)
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        Variable1: int32 = 0
        Variable1_0: int32 = 0
        
        Value1 = None
        # Label 201
        ReturnValue1 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[Coordinates], Ref[Value1])
        
        Value1.NodesToUnhide_33_A6E465554D49C98EE2A0ECB493BE5CBA = None
        ReturnValue1_1: int32 = len(Value1.NodesToUnhide_33_A6E465554D49C98EE2A0ECB493BE5CBA)
        ReturnValue1_2: bool = Variable1 <= ReturnValue1_1
        if not ReturnValue1_2:
            goto('L1205')
        Variable1_0 = Variable1
        ExecutionFlow.Push("L2430")
        
        Value1 = None
        ReturnValue1 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[Coordinates], Ref[Value1])
        
        Value1.NodesToUnhide_33_A6E465554D49C98EE2A0ECB493BE5CBA = None
        Item2 = None
        Item2 = Value1.NodesToUnhide_33_A6E465554D49C98EE2A0ECB493BE5CBA[Variable1_0]
        
        Item2 = None
        Value3 = None
        ReturnValue3: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeObjects], Ref[Item2], Ref[Value3])
        ReturnValue_0: bool = EqualEqual_ByteByte(Value3.mNodeState, 3)
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        
        Value1 = None
        ReturnValue1 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[Coordinates], Ref[Value1])
        
        Value1.NodesToUnhide_33_A6E465554D49C98EE2A0ECB493BE5CBA = None
        Item2 = None
        Item2 = Value1.NodesToUnhide_33_A6E465554D49C98EE2A0ECB493BE5CBA[Variable1_0]
        
        Item2 = None
        Value3 = None
        ReturnValue3 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeObjects], Ref[Item2], Ref[Value3])
        
        Value3 = None
        ReturnValue1_3: int32 = LocalNodeObjects.append(Value3)
        
        Value1 = None
        ReturnValue1 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[Coordinates], Ref[Value1])
        
        Value1.NodesToUnhide_33_A6E465554D49C98EE2A0ECB493BE5CBA = None
        Item2 = None
        Item2 = Value1.NodesToUnhide_33_A6E465554D49C98EE2A0ECB493BE5CBA[Variable1_0]
        
        Item2 = None
        Value3 = None
        ReturnValue3 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeObjects], Ref[Item2], Ref[Value3])
        # Label 1171
        Value3.mShowUnlockIcon = True
        goto(ExecutionFlow.Pop())
        
        # Label 1205
        self.ShowUnlockIconOnNodes(Ref[LocalNodeObjects])
        Variable: bool = False
        Variable2: int32 = 0
        Variable2_0: int32 = 0
        # Label 1285
        ReturnValue_1: bool = Not_PreBool(Variable)
        
        Value = None
        ReturnValue_2: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[Coordinates], Ref[Value])
        
        Value.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63 = None
        ReturnValue2: int32 = len(Value.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63)
        ReturnValue2_0: bool = Variable2 <= ReturnValue2
        ReturnValue_3: bool = ReturnValue_1 and ReturnValue2_0
        if not ReturnValue_3:
            goto('L2139')
        Variable2_0 = Variable2
        ExecutionFlow.Push("L2504")
        
        Value = None
        ReturnValue_2 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[Coordinates], Ref[Value])
        
        Value.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63 = None
        Item1 = None
        Item1 = Value.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63[Variable2_0]
        
        Item1 = None
        Value4 = None
        ReturnValue4: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[Item1], Ref[Value4])
        ReturnValue1_4: bool = self.IsSchematicResearched(Value4.Schematic_27_3663A42446FDB4387D0C81AFC23E225B)
        ReturnValue2_1: bool = Not_PreBool(ReturnValue1_4)
        if not ReturnValue2_1:
            goto('L2578')
        
        Value = None
        ReturnValue_2 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[Coordinates], Ref[Value])
        
        Value.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63 = None
        Item1 = None
        Item1 = Value.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63[Variable2_0]
        
        Item1 = None
        Value2 = None
        ReturnValue2_2: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeObjects], Ref[Item1], Ref[Value2])
        
        Value2 = None
        ReturnValue_4: int32 = LocalUnhiddenBy.append(Value2)
        goto(ExecutionFlow.Pop())
        # Label 2139
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        
        # Label 2185
        ReturnValue_5: int32 = len(LocalUnhiddenBy)
        ReturnValue_6: bool = Variable_0 <= ReturnValue_5
        if not ReturnValue_6:
            goto('L2425')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L2583")
        
        Item = None
        Item = LocalUnhiddenBy[Variable_1]
        Item.ShowHideKeyIcon(True)
        goto(ExecutionFlow.Pop())
        # Label 2425
        # End
        # Label 2430
        ReturnValue1_5: int32 = Variable1 + 1
        Variable1 = ReturnValue1_5
        goto('L201')
        # Label 2504
        ReturnValue2_3: int32 = Variable2 + 1
        Variable2 = ReturnValue2_3
        goto('L1285')
        # Label 2578
        # End
        # Label 2583
        ReturnValue_7: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_7
        goto('L2185')
    

    def TellNodesIfOtherNodeIsSelected(self, isSelected: bool):
        ExecutionFlow.Push("L495")
        Keys: List[IntVector2D] = []
        
        Default__BlueprintMapLibrary.Map_Keys(Ref[self.mNodeObjects], Ref[Keys])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 112
        ReturnValue: int32 = len(Keys)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L421")
        
        Item = None
        Item = Keys[Variable_0]
        
        Item = None
        Value = None
        # Label 310
        ReturnValue_1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeObjects], Ref[Item], Ref[Value])
        Value.mIsOtherSelected = isSelected
        goto(ExecutionFlow.Pop())
        # Label 421
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L112')
    

    def SetupCavases(self, GridCanvas: Ptr[CanvasPanel], NodeCanvas: Ptr[CanvasPanel], Roads: Ptr[Widget_MAMTree_Road]):
        self.mParentGridCanvas = GridCanvas
        self.mParentNodeCavas = NodeCanvas
        self.mParentRoads = Roads
    

    def EditorOnly_SetupTileFeedback(self, Coordinates: IntVector2D, NodeToUnhide: IntVector2D):
        pass
    

    def OnGenerateTree(self):
        pass
    

    def OnNodeClicked(self, NewCoordinates: bool):
        pass
    

    def EditorOnly_OnActiveNodesUpdated(self, text: FText):
        pass
    

    def OnDataCleared(self):
        pass
    

    def OnTreeLoaded(self):
        pass
    

    def IsSelectedNodeValid(self):
        ReturnValue: bool = GreaterEqual_IntInt(self.mSelectedNodeCoordinates.X_2_3FF107F84D30EB52DD50898C7D2CAD67, 0)
        ReturnValue1: bool = GreaterEqual_IntInt(self.mSelectedNodeCoordinates.Y_4_F18C5B824136D7759146338CAA496F0A, 0)
        ReturnValue_0: bool = ReturnValue and ReturnValue1
        IsValid = ReturnValue_0
    

    def OnParentNodeClicked(self, Coordinate: IntVector2D):
        
        IsValid = None
        self.IsSelectedNodeValid(Ref[IsValid])
        if not IsValid:
            goto('L143')
        
        Value1 = None
        ReturnValue1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeObjects], Ref[self.mSelectedNodeCoordinates], Ref[Value1])
        Value1.SetIsSelected(False)
        # Label 143
        ReturnValue: bool = EqualEqual_IntInt(Coordinate.X_2_3FF107F84D30EB52DD50898C7D2CAD67, self.mSelectedNodeCoordinates.X_2_3FF107F84D30EB52DD50898C7D2CAD67)
        ReturnValue1_0: bool = EqualEqual_IntInt(Coordinate.Y_4_F18C5B824136D7759146338CAA496F0A, self.mSelectedNodeCoordinates.Y_4_F18C5B824136D7759146338CAA496F0A)
        ReturnValue_0: bool = ReturnValue and ReturnValue1_0
        if not ReturnValue_0:
            goto('L326')
        self.ResetSelectedNode()
        # End
        # Label 326
        self.mSelectedNodeCoordinates = Coordinate
        
        Value = None
        ReturnValue_1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeObjects], Ref[self.mSelectedNodeCoordinates], Ref[Value])
        Value.SetIsSelected(True)
        self.TellNodesIfOtherNodeIsSelected(True)
        self.OnNodeClicked(True)
    

    def UpdateRoads(self):
        ExecutionFlow.Push("L1342")
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mConvertedRoadData])
        Keys: List[IntVector2D] = []
        
        Default__BlueprintMapLibrary.Map_Keys(Ref[self.mNodeData], Ref[Keys])
        Variable1: int32 = 0
        Variable: int32 = 0
        
        # Label 153
        ReturnValue: int32 = len(Keys)
        # Label 212
        ReturnValue_0: bool = Variable1 <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable = Variable1
        ExecutionFlow.Push("L701")
        
        Item = None
        Item = Keys[Variable]
        
        Item = None
        Value = None
        ReturnValue_1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[Item], Ref[Value])
        Keys1: List[IntVector2D] = []
        
        Value.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A = None
        Default__BlueprintMapLibrary.Map_Keys(Ref[Value.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A], Ref[Keys1])
        
        ReturnValue2: int32 = len(Keys1)
        ReturnValue_2: bool = EqualEqual_IntInt(ReturnValue2, 0)
        # Label 583
        if not ReturnValue_2:
            goto('L775')
        Array: List[IntVector2D] = []
        
        Item = None
        Item = Keys[Variable]
        
        self.DrawRoad(Item, False, Ref[Array])
        goto(ExecutionFlow.Pop())
        # Label 701
        ReturnValue1: int32 = Variable1 + 1
        Variable1 = ReturnValue1
        goto('L153')
        # Label 775
        Variable_0: int32 = 0
        Variable1_0: int32 = 0
        
        # Label 821
        ReturnValue1_0: int32 = len(Keys1)
        ReturnValue1_1: bool = Variable_0 <= ReturnValue1_0
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        Variable1_0 = Variable_0
        ExecutionFlow.Push("L1268")
        
        Item = None
        Item = Keys[Variable]
        
        Item = None
        Value = None
        ReturnValue_1 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[Item], Ref[Value])
        
        Item1 = None
        Item1 = Keys1[Variable1_0]
        
        Value.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A = None
        Item1 = None
        Value1 = None
        ReturnValue1_2: bool = Default__BlueprintMapLibrary.Map_Find(Ref[Value.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A], Ref[Item1], Ref[Value1])
        
        Value1.Points_10_9533B9104470D8E053E7ACA5C4C9F865 = None
        self.DrawRoad(Item, False, Ref[Value1.Points_10_9533B9104470D8E053E7ACA5C4C9F865])
        goto(ExecutionFlow.Pop())
        # Label 1268
        ReturnValue_3: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_3
        goto('L821')
    

    def ClearData(self):
        self.mParentGridCanvas.ClearChildren()
        self.mParentNodeCavas.ClearChildren()
        
        Default__BlueprintMapLibrary.Map_Clear(Ref[self.mNodeData])
        IntVector2D.X_2_3FF107F84D30EB52DD50898C7D2CAD67 = -1
        IntVector2D.Y_4_F18C5B824136D7759146338CAA496F0A = -1
        self.mSelectedNodeCoordinates = IntVector2D
        self.mLastRoadDirection = 2
        
        Default__BlueprintMapLibrary.Map_Clear(Ref[self.mNodeObjects])
        
        Default__BlueprintMapLibrary.Map_Clear(Ref[self.mRoadOccupiedTiles])
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mTempRoadOccupiedTiles])
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mUnHiddenNodes])
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mConvertedRoadData])
        
        self.mParentRoads.mTempRoad = None
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mParentRoads.mTempRoad])
        
        self.mParentRoads.mConvertedRoadData = None
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mParentRoads.mConvertedRoadData])
        
        self.mParentRoads.mHighlightedRoadData = None
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mParentRoads.mHighlightedRoadData])
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mConvertedHighlightRoadData])
        self.OnDataCleared()
    

    def GetRoadPointsFromCoordinates(self, StartCoordinates: IntVector2D, EndCoordinates: IntVector2D):
        ReturnValue: uint8 = self.GetRoadDirection(StartCoordinates, EndCoordinates)
        LocalRoadDirection = ReturnValue
        CmpSuccess: bool = NotEqual_ByteByte(LocalRoadDirection, 2)
        if not CmpSuccess:
            goto('L217')
        CmpSuccess = NotEqual_ByteByte(LocalRoadDirection, 3)
        # Label 153
        if not CmpSuccess:
            goto('L443')
        CmpSuccess = NotEqual_ByteByte(LocalRoadDirection, 4)
        if not CmpSuccess:
            goto('L443')
        # Label 212
        # End
        # Label 217
        self.mLastRoadDirection = LocalRoadDirection
        
        Position2 = None
        self.GetPixelPosOnGrid(EndCoordinates, Ref[Position2])
        ReturnValue_0: Vector2D = Divide_Vector2DFloat(self.mTileSize, 2)
        ReturnValue2: Vector2D = Add_Vector2DVector2D(Position2, ReturnValue_0)
        Array2: List[Vector2D] = [ReturnValue2]
        ConvertedRoadPoints = Array2
        # Label 411
        RoadDirection = LocalRoadDirection
        # End
        # Label 443
        CmpSuccess_0: bool = NotEqual_ByteByte(self.mLastRoadDirection, 2)
        if not CmpSuccess_0:
            goto('L892')
        CmpSuccess_0 = NotEqual_ByteByte(self.mLastRoadDirection, 3)
        if not CmpSuccess_0:
            goto('L583')
        CmpSuccess_0 = NotEqual_ByteByte(self.mLastRoadDirection, 4)
        if not CmpSuccess_0:
            goto('L583')
        # End
        # Label 583
        self.mLastRoadDirection = LocalRoadDirection
        
        Position = None
        self.GetPixelPosOnGrid(EndCoordinates, Ref[Position])
        
        X = None
        Y = None
        BreakVector2D(self.mTileSize, Ref[X], Ref[Y])
        ReturnValue_1: float = X / 2
        ReturnValue_2: Vector2D = Vector2D(ReturnValue_1, Y)
        ReturnValue_3: Vector2D = Add_Vector2DVector2D(Position, ReturnValue_2)
        Array: List[Vector2D] = [ReturnValue_3]
        ConvertedRoadPoints = Array
        RoadDirection = LocalRoadDirection
        # End
        # Label 892
        self.mLastRoadDirection = LocalRoadDirection
        
        Position = None
        self.GetPixelPosOnGrid(EndCoordinates, Ref[Position])
        
        Position1 = None
        self.GetPixelPosOnGrid(StartCoordinates, Ref[Position1])
        
        X = None
        Y = None
        BreakVector2D(self.mTileSize, Ref[X], Ref[Y])
        ReturnValue_1 = X / 2
        
        X1 = None
        Y1 = None
        BreakVector2D(self.mTileSize, Ref[X1], Ref[Y1])
        ReturnValue_2 = Vector2D(ReturnValue_1, Y)
        ReturnValue1: float = X1 / 2
        ReturnValue_3 = Add_Vector2DVector2D(Position, ReturnValue_2)
        ReturnValue1_0: Vector2D = Vector2D(ReturnValue1, Y1)
        ReturnValue1_1: Vector2D = Add_Vector2DVector2D(Position1, ReturnValue1_0)
        Array1: List[Vector2D] = [ReturnValue1_1, ReturnValue_3]
        ConvertedRoadPoints = Array1
        RoadDirection = LocalRoadDirection
    

    def GetRoadDirection(self, StartCoordinates: IntVector2D, EndCoordinates: IntVector2D):
        ExecutionFlow.Push("L873")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        Array = None
        # Label 51
        self.GetRoadHighlightOffsets_OLD(StartCoordinates, Ref[Array])
        
        Array = None
        ReturnValue: int32 = len(Array)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        # Label 217
        ExecutionFlow.Push("L799")
        LocalDirectionalIndex = Variable_0
        
        Array = None
        self.GetRoadHighlightOffsets_OLD(StartCoordinates, Ref[Array])
        
        Array = None
        Item = None
        Item = Array[Variable_0]
        ReturnValue_1: int32 = EndCoordinates.Y_4_F18C5B824136D7759146338CAA496F0A - StartCoordinates.Y_4_F18C5B824136D7759146338CAA496F0A
        ReturnValue_2: bool = EqualEqual_IntInt(ReturnValue_1, Item.Y_4_F18C5B824136D7759146338CAA496F0A)
        ReturnValue1: int32 = EndCoordinates.X_2_3FF107F84D30EB52DD50898C7D2CAD67 - StartCoordinates.X_2_3FF107F84D30EB52DD50898C7D2CAD67
        ReturnValue1_0: bool = EqualEqual_IntInt(ReturnValue1, Item.X_2_3FF107F84D30EB52DD50898C7D2CAD67)
        # Label 562
        ReturnValue_3: bool = ReturnValue1_0 and ReturnValue_2
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Variable_1: uint8 = 4
        Variable1: uint8 = 2
        Variable2: uint8 = 3
        Variable_2: int32 = LocalDirectionalIndex
        
        switch = {
            0: Variable2,
            1: Variable1,
            2: Variable_1
        }
        ReturnValue_4: uint8 = switch.get(Variable_2, None)
        goto('L873')
        # Label 799
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L51')
    

    def DrawRoad(self, Coordinates: IntVector2D, mTempRoadTiles: Ref[List[IntVector2D]], HighlightedRoad: bool):
        ExecutionFlow.Push("L1067")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(mTempRoadTiles)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L671')
        Variable_0 = Variable
        ExecutionFlow.Push("L993")
        
        Item = None
        Item = mTempRoadTiles[Variable_0]
        LocalEndCoordinate = Item
        ReturnValue_1: bool = EqualEqual_IntInt(Variable_0, 0)
        if not ReturnValue_1:
            goto('L543')
        LocalStartCoordinate = Coordinates
        ReturnValue_2: Vector2D = Divide_Vector2DFloat(self.mTileSize, 2)
        
        Position = None
        self.GetPixelPosOnGrid(LocalStartCoordinate, Ref[Position])
        ReturnValue_3: Vector2D = Add_Vector2DVector2D(Position, ReturnValue_2)
        
        ReturnValue_4: int32 = TempConvertedRoadPoints.append(ReturnValue_3)
        
        ConvertedRoadPoints = None
        RoadDirection = None
        # Label 543
        self.GetRoadPointsFromCoordinates(LocalStartCoordinate, LocalEndCoordinate, Ref[ConvertedRoadPoints], Ref[RoadDirection])
        
        ConvertedRoadPoints = None
        Default__KismetArrayLibrary.Array_Append(Ref[TempConvertedRoadPoints], Ref[ConvertedRoadPoints])
        LocalStartCoordinate = LocalEndCoordinate
        goto(ExecutionFlow.Pop())
        # Label 671
        if not HighlightedRoad:
            goto('L839')
        Array.Vector2D_3_76B5E3A240A6EA60DBBF68A46C881CB3 = TempConvertedRoadPoints
        
        Array = None
        ReturnValue_5: int32 = Default__KismetArrayLibrary.Array_AddUnique(Ref[self.mConvertedHighlightRoadData], Ref[Array])
        self.mParentRoads.mHighlightedRoadData = self.mConvertedHighlightRoadData
        goto(ExecutionFlow.Pop())
        # Label 839
        Array1.Vector2D_3_76B5E3A240A6EA60DBBF68A46C881CB3 = TempConvertedRoadPoints
        
        Array1 = None
        ReturnValue1: int32 = Default__KismetArrayLibrary.Array_AddUnique(Ref[self.mConvertedRoadData], Ref[Array1])
        self.mParentRoads.mConvertedRoadData = self.mConvertedRoadData
        goto(ExecutionFlow.Pop())
        # Label 993
        ReturnValue_6: int32 = Variable + 1
        Variable = ReturnValue_6
        goto('L51')
    

    def GenerateOccupiedTilesFromRoadPoints(self, Road: MAMTree_RoadStartEnd):
        self.UpdateOccupiedRoadTiles_OLD(Road)
    

    def GenerateTree(self, NodeData: Dict[IntVector2D, MAMTree_NodeData_Struct]):
        ExecutionFlow.Push("L4124")
        self.ClearData()
        self.OnGenerateTree()
        Keys3: List[IntVector2D] = []
        
        Default__BlueprintMapLibrary.Map_Keys(Ref[NodeData], Ref[Keys3])
        Variable4: int32 = 0
        Variable3: int32 = 0
        
        # Label 140
        ReturnValue4: int32 = len(Keys3)
        ReturnValue4_0: bool = Variable4 <= ReturnValue4
        if not ReturnValue4_0:
            goto('L1261')
        Variable3 = Variable4
        ExecutionFlow.Push("L3341")
        
        Item4 = None
        Item4 = Keys3[Variable3]
        LocalCoordinate = Item4
        
        Value5 = None
        ReturnValue5: bool = Default__BlueprintMapLibrary.Map_Find(Ref[NodeData], Ref[LocalCoordinate], Ref[Value5])
        LocalNodeData = Value5
        self.CreateNodeObject(LocalNodeData)
        FormatArgumentData.ArgumentName = "y"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = LocalCoordinate.Y_4_F18C5B824136D7759146338CAA496F0A
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "currentText"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = localText
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        FormatArgumentData2.ArgumentName = "x"
        FormatArgumentData2.ArgumentValueType = 0
        FormatArgumentData2.ArgumentValue = 
        FormatArgumentData2.ArgumentValueInt = LocalCoordinate.X_2_3FF107F84D30EB52DD50898C7D2CAD67
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData2, FormatArgumentData]
        ReturnValue: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1163, 'Value': '{currentText}{x}:{y}\r\n'}", Array)
        localText = ReturnValue
        goto(ExecutionFlow.Pop())
        # Label 1261
        self.EditorOnly_OnActiveNodesUpdated(localText)
        Keys2: List[IntVector2D] = []
        
        Default__BlueprintMapLibrary.Map_Keys(Ref[NodeData], Ref[Keys2])
        Variable2: int32 = 0
        Variable2_0: int32 = 0
        
        # Label 1391
        ReturnValue3: int32 = len(Keys2)
        ReturnValue3_0: bool = Variable2 <= ReturnValue3
        if not ReturnValue3_0:
           goto(ExecutionFlow.Pop())
        Variable2_0 = Variable2
        ExecutionFlow.Push("L3267")
        
        Item3 = None
        Item3 = Keys2[Variable2_0]
        LocalCoordinate = Item3
        
        Value2 = None
        ReturnValue2: bool = Default__BlueprintMapLibrary.Map_Find(Ref[NodeData], Ref[LocalCoordinate], Ref[Value2])
        LocalNodeData = Value2
        
        NodeState = None
        self.GetNodeState(LocalCoordinate, NodeData, Ref[NodeState])
        
        Value1 = None
        ReturnValue1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeObjects], Ref[LocalCoordinate], Ref[Value1])
        Value1.SetNodeState(NodeState)
        Keys1: List[IntVector2D] = []
        
        LocalNodeData.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A = None
        Default__BlueprintMapLibrary.Map_Keys(Ref[LocalNodeData.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A], Ref[Keys1])
        Variable: int32 = 0
        Variable1: int32 = 0
        
        # Label 1983
        ReturnValue1_0: int32 = len(Keys1)
        ReturnValue1_1: bool = Variable <= ReturnValue1_0
        if not ReturnValue1_1:
            goto('L3415')
        Variable1 = Variable
        ExecutionFlow.Push("L3976")
        Variable3_0: int32 = 0
        Variable_0: int32 = 0
        
        Item1 = None
        # Label 2172
        Item1 = Keys1[Variable1]
        
        LocalNodeData.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A = None
        Item1 = None
        Value3 = None
        ReturnValue3_1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[LocalNodeData.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A], Ref[Item1], Ref[Value3])
        
        Value3.Points_10_9533B9104470D8E053E7ACA5C4C9F865 = None
        ReturnValue2_0: int32 = len(Value3.Points_10_9533B9104470D8E053E7ACA5C4C9F865)
        ReturnValue2_1: bool = Variable3_0 <= ReturnValue2_0
        if not ReturnValue2_1:
           goto(ExecutionFlow.Pop())
        # Label 2425
        Variable_0 = Variable3_0
        ExecutionFlow.Push("L4050")
        
        Item1 = None
        Item1 = Keys1[Variable1]
        
        LocalNodeData.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A = None
        Item1 = None
        Value3 = None
        ReturnValue3_1 = Default__BlueprintMapLibrary.Map_Find(Ref[LocalNodeData.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A], Ref[Item1], Ref[Value3])
        
        Value3.Points_10_9533B9104470D8E053E7ACA5C4C9F865 = None
        Item2 = None
        Item2 = Value3.Points_10_9533B9104470D8E053E7ACA5C4C9F865[Variable_0]
        
        Item2 = None
        Value4 = None
        ReturnValue4_1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mRoadOccupiedTiles], Ref[Item2], Ref[Value4])
        TempOccupiedTiles = Value4.Roads_16_A42C107B4337EA6F58623680B876D371
        
        Item1 = None
        Item1 = Keys1[Variable1]
        RoadStartEnd.StartCoordinates_2_83B7BFD546264BAE632A5787A046FEEA = LocalCoordinate
        RoadStartEnd.EndCoordinates_4_202B84034EC084E34F1935958692341D = Item1
        
        RoadStartEnd = None
        ReturnValue_0: int32 = TempOccupiedTiles.append(RoadStartEnd)
        RoadOccupiedTile.Roads_16_A42C107B4337EA6F58623680B876D371 = TempOccupiedTiles
        
        Item1 = None
        Item1 = Keys1[Variable1]
        
        LocalNodeData.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A = None
        Item1 = None
        Value3 = None
        ReturnValue3_1 = Default__BlueprintMapLibrary.Map_Find(Ref[LocalNodeData.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A], Ref[Item1], Ref[Value3])
        
        Value3.Points_10_9533B9104470D8E053E7ACA5C4C9F865 = None
        Item2 = None
        Item2 = Value3.Points_10_9533B9104470D8E053E7ACA5C4C9F865[Variable_0]
        
        Item2 = None
        RoadOccupiedTile = None
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mRoadOccupiedTiles], Ref[Item2], Ref[RoadOccupiedTile])
        goto(ExecutionFlow.Pop())
        # Label 3267
        ReturnValue2_2: int32 = Variable2 + 1
        Variable2 = ReturnValue2_2
        goto('L1391')
        # Label 3341
        ReturnValue4_2: int32 = Variable4 + 1
        Variable4 = ReturnValue4_2
        goto('L140')
        # Label 3415
        ReturnValue_1: bool = self.IsSchematicResearched(LocalNodeData.Schematic_27_3663A42446FDB4387D0C81AFC23E225B)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Keys: List[IntVector2D] = []
        
        LocalNodeData.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A = None
        Default__BlueprintMapLibrary.Map_Keys(Ref[LocalNodeData.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A], Ref[Keys])
        Variable1_0: int32 = 0
        Variable4_0: int32 = 0
        
        # Label 3583
        ReturnValue_2: int32 = len(Keys)
        ReturnValue_3: bool = Variable1_0 <= ReturnValue_2
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Variable4_0 = Variable1_0
        ExecutionFlow.Push("L3902")
        
        Item = None
        Item = Keys[Variable4_0]
        
        LocalNodeData.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A = None
        Item = None
        Value = None
        ReturnValue_4: bool = Default__BlueprintMapLibrary.Map_Find(Ref[LocalNodeData.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A], Ref[Item], Ref[Value])
        
        Value.Points_10_9533B9104470D8E053E7ACA5C4C9F865 = None
        self.DrawRoad(LocalCoordinate, True, Ref[Value.Points_10_9533B9104470D8E053E7ACA5C4C9F865])
        goto(ExecutionFlow.Pop())
        # Label 3902
        ReturnValue1_2: int32 = Variable1_0 + 1
        Variable1_0 = ReturnValue1_2
        goto('L3583')
        # Label 3976
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L1983')
        # Label 4050
        ReturnValue3_2: int32 = Variable3_0 + 1
        Variable3_0 = ReturnValue3_2
        goto('L2172')
    

    def LoadSelectedTree(self):
        ExecutionFlow.Push("L714")
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.SelectedResearchTree)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        
        Default__BlueprintMapLibrary.Map_Clear(Ref[self.mNodeData])
        ReturnValue_0: List[Ptr[FGResearchTreeNode]] = Default__FGResearchTree.GetNodes(self.SelectedResearchTree)
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 212
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
            goto('L602')
        Variable_0 = Variable
        ExecutionFlow.Push("L640")
        
        Item = None
        Item = ReturnValue_0[Variable_0]
        Node: Ptr[BPD_ResearchTreeNode] = Cast[BPD_ResearchTreeNode](Item)
        bSuccess: bool = Node
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        
        Node.mNodeDataStruct.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292 = None
        Node.mNodeDataStruct = None
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mNodeData], Ref[Node.mNodeDataStruct.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292], Ref[Node.mNodeDataStruct])
        goto(ExecutionFlow.Pop())
        # Label 602
        self.GenerateTree(self.mNodeData)
        self.OnTreeLoaded()
        goto(ExecutionFlow.Pop())
        # Label 640
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L212')
    

    def SelectResearchTree(self, researchTree: TSubclassOf[FGResearchTree]):
        self.SelectedResearchTree = researchTree
        self.LoadSelectedTree()
    

    def GetInvalidCoordinates(self):
        IntVector2D.X_2_3FF107F84D30EB52DD50898C7D2CAD67 = -1
        IntVector2D.Y_4_F18C5B824136D7759146338CAA496F0A = -1
        Coordinates = IntVector2D
    

    def RemoveRelevantRoadOccupiedTiles(self, RoadStartEnd: MAMTree_RoadStartEnd):
        ExecutionFlow.Push("L2716")
        
        ReturnValue: int32 = Default__BlueprintMapLibrary.Map_Length(Ref[self.mRoadOccupiedTiles])
        ReturnValue_0: FString = Default__KismetStringLibrary.Conv_IntToString(ReturnValue)
        ReturnValue_1: FString = Default__KismetStringLibrary.Concat_StrStr("Get key length: ", ReturnValue_0)
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_1, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        Values: List[MAMTree_RoadOccupiedTile] = []
        
        Default__BlueprintMapLibrary.Map_Values(Ref[self.mRoadOccupiedTiles], Ref[Values])
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 401
        ReturnValue_2: bool = Not_PreBool(Variable)
        
        ReturnValue2: int32 = len(Values)
        ReturnValue1: bool = Variable_0 <= ReturnValue2
        ReturnValue_3: bool = ReturnValue_2 and ReturnValue1
        if not ReturnValue_3:
            goto('L1596')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L2507")
        LocalTileIndex = Variable_1
        Variable1: int32 = 0
        Variable2: int32 = 0
        
        Item1 = None
        # Label 684
        Item1 = Values[Variable_1]
        
        Item1.Roads_16_A42C107B4337EA6F58623680B876D371 = None
        ReturnValue3: int32 = len(Item1.Roads_16_A42C107B4337EA6F58623680B876D371)
        ReturnValue2_0: bool = Variable1 <= ReturnValue3
        if not ReturnValue2_0:
           goto(ExecutionFlow.Pop())
        Variable2 = Variable1
        ExecutionFlow.Push("L2581")
        LocalRoadIndex = Variable2
        
        Item1 = None
        Item1 = Values[Variable_1]
        
        Item1.Roads_16_A42C107B4337EA6F58623680B876D371 = None
        Item2 = None
        Item2 = Item1.Roads_16_A42C107B4337EA6F58623680B876D371[Variable2]
        ReturnValue_4: bool = EqualEqual_IntInt(Item2.EndCoordinates_4_202B84034EC084E34F1935958692341D.Y_4_F18C5B824136D7759146338CAA496F0A, RoadStartEnd.EndCoordinates_4_202B84034EC084E34F1935958692341D.Y_4_F18C5B824136D7759146338CAA496F0A)
        ReturnValue1_0: bool = EqualEqual_IntInt(Item2.EndCoordinates_4_202B84034EC084E34F1935958692341D.X_2_3FF107F84D30EB52DD50898C7D2CAD67, RoadStartEnd.EndCoordinates_4_202B84034EC084E34F1935958692341D.X_2_3FF107F84D30EB52DD50898C7D2CAD67)
        ReturnValue2_1: bool = EqualEqual_IntInt(RoadStartEnd.StartCoordinates_2_83B7BFD546264BAE632A5787A046FEEA.X_2_3FF107F84D30EB52DD50898C7D2CAD67, Item2.StartCoordinates_2_83B7BFD546264BAE632A5787A046FEEA.X_2_3FF107F84D30EB52DD50898C7D2CAD67)
        ReturnValue3_0: bool = EqualEqual_IntInt(RoadStartEnd.StartCoordinates_2_83B7BFD546264BAE632A5787A046FEEA.Y_4_F18C5B824136D7759146338CAA496F0A, Item2.StartCoordinates_2_83B7BFD546264BAE632A5787A046FEEA.Y_4_F18C5B824136D7759146338CAA496F0A)
        ReturnValue1_1: bool = ReturnValue2_1 and ReturnValue3_0
        ReturnValue2_2: bool = ReturnValue1_1 and ReturnValue1_0
        ReturnValue3_1: bool = ReturnValue2_2 and ReturnValue_4
        if not ReturnValue3_1:
           goto(ExecutionFlow.Pop())
        Keys1: List[IntVector2D] = []
        
        Default__BlueprintMapLibrary.Map_Keys(Ref[self.mRoadOccupiedTiles], Ref[Keys1])
        
        Keys1[LocalTileIndex] = None
        Default__BlueprintMapLibrary.Map_Add(Ref[LocalTileToUpdateArray], Ref[Keys1[LocalTileIndex]], Ref[LocalRoadIndex])
        goto(ExecutionFlow.Pop())
        # Label 1596
        Keys: List[IntVector2D] = []
        
        Default__BlueprintMapLibrary.Map_Keys(Ref[LocalTileToUpdateArray], Ref[Keys])
        Variable2_0: int32 = 0
        Variable1_0: int32 = 0
        
        # Label 1703
        ReturnValue_5: int32 = len(Keys)
        ReturnValue_6: bool = Variable2_0 <= ReturnValue_5
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        Variable1_0 = Variable2_0
        ExecutionFlow.Push("L2433")
        
        Item = None
        Item = Keys[Variable1_0]
        LocalTileToUpdate = Item
        
        Value2 = None
        # Label 1928
        ReturnValue2_3: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mRoadOccupiedTiles], Ref[LocalTileToUpdate], Ref[Value2])
        
        Value2.Roads_16_A42C107B4337EA6F58623680B876D371 = None
        ReturnValue1_2: int32 = len(Value2.Roads_16_A42C107B4337EA6F58623680B876D371)
        ReturnValue_7: bool = ReturnValue1_2 > 1
        if not ReturnValue_7:
            goto('L2655')
        
        Value1 = None
        ReturnValue1_3: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mRoadOccupiedTiles], Ref[LocalTileToUpdate], Ref[Value1])
        TempRoads = Value1.Roads_16_A42C107B4337EA6F58623680B876D371
        
        Value = None
        ReturnValue_8: bool = Default__BlueprintMapLibrary.Map_Find(Ref[LocalTileToUpdateArray], Ref[LocalTileToUpdate], Ref[Value])
        
        TempRoads.remove(Value)
        RoadOccupiedTile.Roads_16_A42C107B4337EA6F58623680B876D371 = TempRoads
        
        RoadOccupiedTile = None
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mRoadOccupiedTiles], Ref[LocalTileToUpdate], Ref[RoadOccupiedTile])
        goto(ExecutionFlow.Pop())
        # Label 2433
        ReturnValue2_4: int32 = Variable2_0 + 1
        Variable2_0 = ReturnValue2_4
        goto('L1703')
        # Label 2507
        ReturnValue_9: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_9
        goto('L401')
        # Label 2581
        ReturnValue1_4: int32 = Variable1 + 1
        Variable1 = ReturnValue1_4
        goto('L684')
        
        # Label 2655
        ReturnValue_10: bool = Default__BlueprintMapLibrary.Map_Remove(Ref[self.mRoadOccupiedTiles], Ref[LocalTileToUpdate])
        goto(ExecutionFlow.Pop())
    

    def UpdateOccupiedRoadTiles_OLD(self, Road: MAMTree_RoadStartEnd):
        ExecutionFlow.Push("L893")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(self.mTempRoadOccupiedTiles)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L508')
        Variable_0 = Variable
        ExecutionFlow.Push("L550")
        
        Item = None
        Item = self.mTempRoadOccupiedTiles[Variable_0]
        LocalCoordinate = Item
        
        Value = None
        ReturnValue_1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mRoadOccupiedTiles], Ref[LocalCoordinate], Ref[Value])
        ReturnValue_2: bool = Not_PreBool(ReturnValue_1)
        if not ReturnValue_2:
            goto('L624')
        Array: List[MAMTree_RoadStartEnd] = [Road]
        RoadOccupiedTile1.Roads_16_A42C107B4337EA6F58623680B876D371 = Array
        
        RoadOccupiedTile1 = None
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mRoadOccupiedTiles], Ref[LocalCoordinate], Ref[RoadOccupiedTile1])
        goto(ExecutionFlow.Pop())
        
        # Label 508
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mTempRoadOccupiedTiles])
        goto(ExecutionFlow.Pop())
        # Label 550
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        # Label 619
        goto('L51')
        
        Value = None
        # Label 624
        ReturnValue_1 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mRoadOccupiedTiles], Ref[LocalCoordinate], Ref[Value])
        # Label 693
        TempRoadPoints = Value.Roads_16_A42C107B4337EA6F58623680B876D371
        
        ReturnValue_4: int32 = TempRoadPoints.append(Road)
        RoadOccupiedTile.Roads_16_A42C107B4337EA6F58623680B876D371 = TempRoadPoints
        
        RoadOccupiedTile = None
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mRoadOccupiedTiles], Ref[LocalCoordinate], Ref[RoadOccupiedTile])
        # Label 892
        goto(ExecutionFlow.Pop())
    

    def AddOrUpdateNodeObject(self, Coordinate: Const[Ref[IntVector2D]], NodeData: Const[Ref[MAMTree_NodeData_Struct]]):
        
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mNodeData], Ref[Coordinate], Ref[NodeData])
        self.UpdateRoads()
        
        Value = None
        ReturnValue: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeObjects], Ref[Coordinate], Ref[Value])
        Value.UpdateNodeIcon(NodeData)
    

    def PositionWidgetOnGrid(self, CanvasPanel: Ptr[CanvasPanel], Widget: Ptr[Widget], Coordinates: IntVector2D):
        ReturnValue: Ptr[CanvasPanelSlot] = CanvasPanel.AddChildToCanvas(Widget)
        
        Position = None
        # Label 51
        self.GetPixelPosOnGrid(Coordinates, Ref[Position])
        ReturnValue.SetPosition(Position)
        ReturnValue.SetSize(self.mTileSize)
    

    def GetPixelPosOnGrid(self, Coordinates: IntVector2D):
        ReturnValue: int32 = Percent_IntInt(Coordinates.X_2_3FF107F84D30EB52DD50898C7D2CAD67, 2)
        
        X = None
        Y = None
        # Label 51
        BreakVector2D(self.mTileSize, Ref[X], Ref[Y])
        ReturnValue_0: bool = EqualEqual_IntInt(ReturnValue, 0)
        ReturnValue_1: float = Y / 2
        Variable: bool = ReturnValue_0
        
        X1 = None
        Y1 = None
        BreakVector2D(self.mTileSize, Ref[X1], Ref[Y1])
        ReturnValue_2: float = Coordinates.X_2_3FF107F84D30EB52DD50898C7D2CAD67 * X1
        ReturnValue1: float = Coordinates.Y_4_F18C5B824136D7759146338CAA496F0A * Y1
        ReturnValue_3: float = ReturnValue1 + ReturnValue_1
        
        switch = {
            False: ReturnValue1,
            True: ReturnValue_3
        }
        ReturnValue_4: Vector2D = Vector2D(ReturnValue_2, switch.get(Variable, None))
        Position = ReturnValue_4
    

    def IsTileRoadHighlighted(self, Coordinates: IntVector2D):
        ExecutionFlow.Push("L693")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        Array = None
        # Label 51
        self.GetRoadHighlightOffsets_OLD(self.mSelectedNodeCoordinates, Ref[Array])
        
        Array = None
        ReturnValue: int32 = len(Array)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L603')
        Variable_0 = Variable
        ExecutionFlow.Push("L619")
        
        Array = None
        self.GetRoadHighlightOffsets_OLD(self.mSelectedNodeCoordinates, Ref[Array])
        
        Array = None
        Item = None
        Item = Array[Variable_0]
        ReturnValue1: int32 = Item.Y_4_F18C5B824136D7759146338CAA496F0A + self.mSelectedNodeCoordinates.Y_4_F18C5B824136D7759146338CAA496F0A
        ReturnValue2: int32 = Item.X_2_3FF107F84D30EB52DD50898C7D2CAD67 + self.mSelectedNodeCoordinates.X_2_3FF107F84D30EB52DD50898C7D2CAD67
        ReturnValue_1: bool = EqualEqual_IntInt(Coordinates.Y_4_F18C5B824136D7759146338CAA496F0A, ReturnValue1)
        ReturnValue1_0: bool = EqualEqual_IntInt(Coordinates.X_2_3FF107F84D30EB52DD50898C7D2CAD67, ReturnValue2)
        ReturnValue_2: bool = ReturnValue1_0 and ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        Return = True
        # End
        # Label 603
        Return = False
        # End
        # Label 619
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L51')
    

    def GetRoadHighlightOffsets_OLD(self, Coordinates: IntVector2D):
        ReturnValue: int32 = Percent_IntInt(Coordinates.X_2_3FF107F84D30EB52DD50898C7D2CAD67, 2)
        # Label 51
        Variable: int32 = 1
        ReturnValue_0: bool = EqualEqual_IntInt(ReturnValue, 0)
        Variable_0: bool = ReturnValue_0
        Variable1: int32 = 0
        IntVector2D.X_2_3FF107F84D30EB52DD50898C7D2CAD67 = 0
        IntVector2D.Y_4_F18C5B824136D7759146338CAA496F0A = 1
        IntVector2D1.X_2_3FF107F84D30EB52DD50898C7D2CAD67 = 1
        
        switch = {
            False: Variable1,
            True: Variable
        }
        IntVector2D1.Y_4_F18C5B824136D7759146338CAA496F0A = switch.get(Variable_0, None)
        # Label 326
        IntVector2D2.X_2_3FF107F84D30EB52DD50898C7D2CAD67 = -1
        
        switch_0 = {
            False: Variable1,
            True: Variable
        }
        IntVector2D2.Y_4_F18C5B824136D7759146338CAA496F0A = switch_0.get(Variable_0, None)
        Array: List[IntVector2D] = [IntVector2D2, IntVector2D, IntVector2D1]
        Array_0: List[IntVector2D] = Array
    

    def CreateNodeObject(self, NodeData: MAMTree_NodeData_Struct):
        ExecutionFlow.Push("L2552")
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_MAMTree_Node] = Default__WidgetBlueprintLibrary.Create(self, Widget_MAMTree_Node, ReturnValue)
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_0, "mNodeData", Ref[NodeData])
        # Label 153
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_0, "mIsEditor", self.mIsEditor)
        LocalWidget = ReturnValue_0
        
        NodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292 = None
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mNodeObjects], Ref[NodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292], Ref[LocalWidget])
        OutputDelegate3.BindUFunction(self, OnParentNodeClicked)
        # Label 326
        LocalWidget.OnClicked.AddUnique(OutputDelegate3)
        OutputDelegate2.BindUFunction(self, OnParentNodeHovered)
        LocalWidget.OnHovered.AddUnique(OutputDelegate2)
        OutputDelegate1.BindUFunction(self, OnParentNodeUnhovered)
        LocalWidget.OnUnhovered.AddUnique(OutputDelegate1)
        # Label 495
        OutputDelegate.BindUFunction(self, OnResearchStarted)
        LocalWidget.OnResearchStarted.AddUnique(OutputDelegate)
        self.PositionWidgetOnGrid(self.mParentNodeCavas, LocalWidget, NodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292)
        Struct1.Schematic_27_3663A42446FDB4387D0C81AFC23E225B = NodeData.Schematic_27_3663A42446FDB4387D0C81AFC23E225B
        Struct1.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292 = NodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292
        Struct1.Parents_20_7A099B96409362536B743BA1CC77C234 = NodeData.Parents_20_7A099B96409362536B743BA1CC77C234
        Struct1.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A = NodeData.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A
        Struct1.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63 = NodeData.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63
        Struct1.NodesToUnhide_33_A6E465554D49C98EE2A0ECB493BE5CBA = NodeData.NodesToUnhide_33_A6E465554D49C98EE2A0ECB493BE5CBA
        
        NodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292 = None
        Struct1 = None
        self.AddOrUpdateNodeObject(Ref[NodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292], Ref[Struct1])
        
        NodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292 = None
        Value2 = None
        ReturnValue2: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mRoadOccupiedTiles], Ref[NodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292], Ref[Value2])
        if not ReturnValue2:
           goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.PrintString(self, "Tile Occuptied", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        NodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292 = None
        Value2 = None
        # Label 1136
        ReturnValue2 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mRoadOccupiedTiles], Ref[NodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292], Ref[Value2])
        
        Value2.Roads_16_A42C107B4337EA6F58623680B876D371 = None
        ReturnValue_1: int32 = len(Value2.Roads_16_A42C107B4337EA6F58623680B876D371)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L2478")
        
        NodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292 = None
        Value2 = None
        ReturnValue2 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mRoadOccupiedTiles], Ref[NodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292], Ref[Value2])
        
        Value2.Roads_16_A42C107B4337EA6F58623680B876D371 = None
        Item = None
        Item = Value2.Roads_16_A42C107B4337EA6F58623680B876D371[Variable_0]
        LocalOccupiedRoadStart = Item.StartCoordinates_2_83B7BFD546264BAE632A5787A046FEEA
        
        Value1 = None
        ReturnValue1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[LocalOccupiedRoadStart], Ref[Value1])
        TempChildrenAndRoads = Value1.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A
        
        NodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292 = None
        Value2 = None
        ReturnValue2 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mRoadOccupiedTiles], Ref[NodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292], Ref[Value2])
        
        Value2.Roads_16_A42C107B4337EA6F58623680B876D371 = None
        Item = None
        Item = Value2.Roads_16_A42C107B4337EA6F58623680B876D371[Variable_0]
        
        Item.EndCoordinates_4_202B84034EC084E34F1935958692341D = None
        ReturnValue_3: bool = Default__BlueprintMapLibrary.Map_Remove(Ref[TempChildrenAndRoads], Ref[Item.EndCoordinates_4_202B84034EC084E34F1935958692341D])
        
        Value = None
        ReturnValue_4: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mNodeData], Ref[LocalOccupiedRoadStart], Ref[Value])
        Struct.Schematic_27_3663A42446FDB4387D0C81AFC23E225B = Value.Schematic_27_3663A42446FDB4387D0C81AFC23E225B
        Struct.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292 = Value.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292
        Struct.Parents_20_7A099B96409362536B743BA1CC77C234 = Value.Parents_20_7A099B96409362536B743BA1CC77C234
        Struct.ChildrenAndRoads_34_758C9E0D4F09DAF4BBAD309358952A0A = TempChildrenAndRoads
        Struct.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63 = Value.UnhiddenBy_38_909B07D7461225A33C48A68A7139FE63
        Struct.NodesToUnhide_33_A6E465554D49C98EE2A0ECB493BE5CBA = Value.NodesToUnhide_33_A6E465554D49C98EE2A0ECB493BE5CBA
        
        Struct = None
        self.AddOrUpdateNodeObject(Ref[LocalOccupiedRoadStart], Ref[Struct])
        
        NodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292 = None
        Value2 = None
        ReturnValue2 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mRoadOccupiedTiles], Ref[NodeData.Coordinates_23_5A3DE6C040C7026EDEA49E9CE8612292], Ref[Value2])
        
        Value2.Roads_16_A42C107B4337EA6F58623680B876D371 = None
        Item = None
        Item = Value2.Roads_16_A42C107B4337EA6F58623680B876D371[Variable_0]
        RoadStartEnd.StartCoordinates_2_83B7BFD546264BAE632A5787A046FEEA = Item.StartCoordinates_2_83B7BFD546264BAE632A5787A046FEEA
        RoadStartEnd.EndCoordinates_4_202B84034EC084E34F1935958692341D = Item.EndCoordinates_4_202B84034EC084E34F1935958692341D
        self.RemoveRelevantRoadOccupiedTiles(RoadStartEnd)
        goto(ExecutionFlow.Pop())
        # Label 2478
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L1136')
    

    def ShowUnlockIconOnNodes(self, NodeObjects: Const[Ref[List[Ptr[Widget_MAMTree_Node]]]]):
        ExecuteUbergraph_Widget_MAMTree_Grid.K2Node_CustomEvent_NodeObjects = NodeObjects #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_MAMTree_Grid(589)
    

    def ExecuteUbergraph_Widget_MAMTree_Grid(self):
        goto(ComputedJump("EntryPoint"))
        ExecutionFlow.Push("L266")
        
        NodeObjects = None
        ReturnValue: int32 = len(NodeObjects)
        ReturnValue_0: int32 = ReturnValue - 1
        ReturnValue1: bool = Variable <= ReturnValue_0
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        
        NodeObjects = None
        Item = None
        Item = NodeObjects[Variable]
        Item.ShowHideUnlockIcon(True)
        goto(ExecutionFlow.Pop())
        # Label 266
        ReturnValue_1: int32 = Variable + 1
        Variable: int32 = ReturnValue_1
        
        NodeObjects = None
        # Label 335
        ReturnValue = len(NodeObjects)
        ReturnValue_0 = ReturnValue - 1
        ReturnValue_2: bool = Variable <= ReturnValue_0
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, 0.05000000074505806, LatentActionInfo(Linkage = 15, UUID = -1055183482, ExecutionFunction = "ExecuteUbergraph_Widget_MAMTree_Grid", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 561
        Variable = 0
        goto('L335')
        goto('L561')
    

    def OnResearchSelectedSchematic__DelegateSignature(self, schematic: TSubclassOf[FGSchematic]):
        pass
    

    def OnSaveTree__DelegateSignature(self, researchTree: TSubclassOf[FGResearchTree]):
        pass
    

    def OnLoadClicked__DelegateSignature(self):
        pass
    
