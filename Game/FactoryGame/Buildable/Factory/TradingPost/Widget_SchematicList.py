
from codegen.ue4_stub import *

from Script.Engine import SetClassPropertyByName
from Script.Engine import EqualEqual_ByteByte
from Script.FactoryGame import GetAvailableSchematics
from Script.Engine import SetObjectPropertyByName
from Script.UMG import HorizontalBoxSlot
from Script.FactoryGame import GetHighestAvailableTechTier
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Player.BP_PlayerState import BP_PlayerState
from Script.FactoryGame import Get
from Script.FactoryGame import GetType
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicButton import Widget_SchematicButton
from Script.FactoryGame import GetTechTier
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import EqualEqual_IntInt
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_SchematicList import ExecuteUbergraph_Widget_SchematicList
from Script.Engine import BooleanOR
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGSchematic
from Script.FactoryGame import FGBuildableTradingPost
from Script.FactoryGame import ESchematicType
from Script.UMG import UserWidget
from Script.UMG import AddChildToHorizontalBox
from Script.FactoryGame import FGSchematicManager
from Script.UMG import Create
from Script.FactoryGame import Default__FGSchematic
from Script.Engine import GetGameState
from Game.FactoryGame.Buildable.Factory.TradingPost.Widget_TradingPost import Widget_TradingPost
from Script.FactoryGame import Default__FGSchematicManager

class Widget_SchematicList(UserWidget):
    mHighestTier: int32
    mSchematicManager: Ptr[FGSchematicManager]
    mTradingPost: Ptr[FGBuildableTradingPost]
    mTradingPostWidget: Ptr[Widget_TradingPost]
    mNumSchematicsPerRow: int32 = 3
    mCurrentDisplayedTier: int32
    padding = Namespace(Bottom=16, Left=16, Right=16, Top=16)
    
    def GetTradingPostWidget(self):
        pass
    

    def PopulateSchematicForTier(self, inTier: int32):
        ExecutionFlow.Push("L870")
        schematics: List[TSubclassOf[FGSchematic]] = []
        
        self.mSchematicManager.GetAvailableSchematics(Ref[schematics])
        allSchematics = schematics
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 130
        ReturnValue: int32 = len(allSchematics)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L764')
        Variable_0 = Variable
        ExecutionFlow.Push("L796")
        
        Item = None
        Item = allSchematics[Variable_0]
        ReturnValue_1: uint8 = Default__FGSchematic.GetType(Item)
        ReturnValue_2: bool = EqualEqual_ByteByte(ReturnValue_1, 2)
        ReturnValue1: bool = EqualEqual_ByteByte(ReturnValue_1, 3)
        ReturnValue_3: int32 = Default__FGSchematic.GetTechTier(Item)
        ReturnValue_4: bool = BooleanOR(ReturnValue1, ReturnValue_2)
        ReturnValue_5: bool = EqualEqual_IntInt(ReturnValue_3, inTier)
        ReturnValue_6: bool = ReturnValue_4 and ReturnValue_5
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = allSchematics[Variable_0]
        
        Item = None
        ReturnValue_7: int32 = localSchematics.append(Item)
        goto(ExecutionFlow.Pop())
        # Label 764
        schematicsInRing = localSchematics
        # End
        # Label 796
        ReturnValue_8: int32 = Variable + 1
        Variable = ReturnValue_8
        goto('L130')
    

    def CreateSchematicButtons(self):
        ExecutionFlow.Push("L709")
        self.mGrid.ClearChildren()
        
        schematicsInRing = None
        self.PopulateSchematicForTier(self.mCurrentDisplayedTier, Ref[schematicsInRing])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        schematicsInRing = None
        # Label 119
        ReturnValue: int32 = len(schematicsInRing)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L635")
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Widget_SchematicButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_SchematicButton, ReturnValue_1)
        
        schematicsInRing = None
        Item = None
        Item = schematicsInRing[Variable_0]
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_2, "mSchematicClass", Item)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mSchematicList", self)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mTradingPostWidget", self.mTradingPostWidget)
        ReturnValue_3: Ptr[HorizontalBoxSlot] = self.mGrid.AddChildToHorizontalBox(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 635
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L119')
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SchematicList(266)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_SchematicList(384)
    

    def ExecuteUbergraph_Widget_SchematicList(self):
        # Label 10
        ReturnValue: int32 = self.mSchematicManager.GetHighestAvailableTechTier()
        self.mHighestTier = ReturnValue
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        State: Ptr[BP_PlayerState] = Cast[BP_PlayerState](ReturnValue_0.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
            goto('L558')
        self.mCurrentDisplayedTier = State.mLastSchematicTierInUI
        # End
        ReturnValue_1: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_2: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue_1)
        self.mSchematicManager = ReturnValue_2
        goto('L10')
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        State1: Ptr[BP_PlayerState] = Cast[BP_PlayerState](ReturnValue1.PlayerState)
        bSuccess1: bool = State1
        if not bSuccess1:
            goto('L558')
        State1.mLastSchematicTierInUI = self.mCurrentDisplayedTier
    
