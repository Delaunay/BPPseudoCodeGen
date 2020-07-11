
from codegen.ue4_stub import *

from Script.FactoryGame import Default__FGResearchTree
from Script.Engine import SetScalarParameterValue
from Script.Engine import EqualEqual_ClassClass
from Script.Engine import K2_SetTimerDelegate
from Script.FactoryGame import IsResesearchTreeUnlocked
from Script.FactoryGame import GetPreUnlockDisplayName
from Script.FactoryGame import GetNodes
from Script.Engine import MaterialInstanceDynamic
from Script.FactoryGame import GetResearchTreeIcon
from Script.Engine import Conv_IntToFloat
from Game.FactoryGame.AvailabilityDependencies.BPI_AvailabilityDependencyInterface import BPI_AvailabilityDependencyInterface
from Script.Engine import Not_PreBool
from Script.FactoryGame import GetDisplayName
from Script.FactoryGame import FGResearchTreeNode
from Script.Engine import Ease
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Default__FGResearchManager
from Script.Engine import PlayerController
from Script.FactoryGame import Get
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import ESlateVisibility
from Script.Engine import TimerHandle
from Script.Engine import GreaterEqual_FloatFloat
from Script.UMG import GetDynamicMaterial
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import NotEqual_FloatFloat
from Game.FactoryGame.Interface.UI.InGame.MAMTree.BPW_MAMTree_ListButtonInfo import ExecuteUbergraph_BPW_MAMTree_ListButtonInfo
from Script.FactoryGame import FGResearchManager
from Script.FactoryGame import GetPreUnlockDescription
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.UMG import UserWidget
from Script.FactoryGame import GetUnlockDependencies
from Script.Engine import NotEqual_ObjectObject
from Script.FactoryGame import GetPostUnlockDescription
from Script.FactoryGame import IsSchematicPurchased
from Script.Engine import AsPercent_Float
from Script.FactoryGame import FGSchematicManager
from Script.FactoryGame import FGResearchTree
from Script.SlateCore import SlateBrush
from Game.FactoryGame.Schematics.Research.BPD_ResearchTreeNode import BPD_ResearchTreeNode
from Script.Engine import Array_Clear
from Script.FactoryGame import Default__FGSchematicManager
from Script.FactoryGame import FGAvailabilityDependency
from Game.FactoryGame.Schematics.Research.BPD_ResearchTree_HardDrive import BPD_ResearchTree_HardDrive

class BPW_MAMTree_ListButtonInfo(UserWidget):
    mResearchTree: TSubclassOf[FGResearchTree]
    mLerpT: float
    mLerpDuration: float = 5
    mLerpUpdate: float = 0.009999999776482582
    mLerpEndValue: float
    mLerpTimer: TimerHandle
    mFullDuration: float = 2
    
    def StartProgressBarLerp(self, EndValue: float):
        ReturnValue: bool = NotEqual_FloatFloat(EndValue, 0)
        if not ReturnValue:
            goto('L259')
        self.mLerpEndValue = EndValue
        self.mLerpT = 0
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mLerpTimer])
        OutputDelegate.BindUFunction(self, LerpProgressBar)
        ReturnValue_0: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mLerpUpdate, True)
        self.mLerpTimer = ReturnValue_0
    

    def SetContent(self, researchTree: TSubclassOf[FGResearchTree]):
        ExecutionFlow.Push("L3313")
        localMaxResearchedNodes = 0
        localIsTreeUnlocked = False
        self.mResearchTree = researchTree
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue)
        ReturnValue_1: bool = ReturnValue_0.IsResesearchTreeUnlocked(self.mResearchTree)
        localIsTreeUnlocked = ReturnValue_1
        ReturnValue_2: bool = EqualEqual_ClassClass(self.mResearchTree, BPD_ResearchTree_HardDrive)
        Variable5: bool = ReturnValue_2
        Variable4: uint8 = 0
        Variable5_0: uint8 = 2
        
        switch = {
            False: Variable4,
            True: Variable5_0
        }
        self.mProgressBarContainer.SetVisibility(switch.get(Variable5, None))
        ReturnValue_3: List[Ptr[FGAvailabilityDependency]] = Default__FGResearchTree.GetUnlockDependencies(self.mResearchTree)
        
        Item = None
        Item = ReturnValue_3[0]
        Interface: TScriptInterface[BPI_AvailabilityDependencyInterface] = QueryInterface[BPI_AvailabilityDependencyInterface](Item)
        bSuccess: bool = Interface
        if not bSuccess:
            goto('L2856')
        
        DependecyData = None
        GetInterfaceUObject(Interface).GetDependecyData(Ref[DependecyData])
        # Label 628
        ReturnValue_4: SlateBrush = Default__FGResearchTree.GetResearchTreeIcon(self.mResearchTree)
        ReturnValue_5: bool = NotEqual_ObjectObject(ReturnValue_4.ResourceObject, None)
        Variable4_0: bool = ReturnValue_5
        
        DependecyData = None
        Item1 = None
        Item1 = DependecyData[0]
        SlateBrush.ImageSize = self.mIcon.Brush.ImageSize
        SlateBrush.Margin = self.mIcon.Brush.Margin
        SlateBrush.TintColor = self.mIcon.Brush.TintColor
        
        switch_0 = {
            False: Item1.DependencyIcon_28_3E3B124C41C68907A6EB9FAD36C04BC4,
            True: ReturnValue_4.ResourceObject
        }
        SlateBrush.ResourceObject = switch_0.get(Variable4_0, None)
        SlateBrush.DrawAs = self.mIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mIcon.Brush.Tiling
        SlateBrush.Mirroring = self.mIcon.Brush.Mirroring
        
        SlateBrush = None
        self.mIcon.SetBrush(Ref[SlateBrush])
        Variable2: uint8 = 0
        Variable3: uint8 = 2
        Variable1: bool = localIsTreeUnlocked
        
        switch_1 = {
            False: Variable3,
            True: Variable2
        }
        self.mIcon.SetVisibility(switch_1.get(Variable1, None))
        Variable: uint8 = 0
        Variable1_0: uint8 = 2
        ReturnValue_6: bool = Not_PreBool(localIsTreeUnlocked)
        Variable_0: bool = ReturnValue_6
        
        switch_2 = {
            False: Variable1_0,
            True: Variable
        }
        self.mUnavailableIcon.SetVisibility(switch_2.get(Variable_0, None))
        Variable3_0: bool = localIsTreeUnlocked
        ReturnValue_7: FText = Default__FGResearchTree.GetDisplayName(self.mResearchTree)
        ReturnValue_8: FText = Default__FGResearchTree.GetPreUnlockDisplayName(self.mResearchTree)
        
        switch_3 = {
            False: ReturnValue_8,
            True: ReturnValue_7
        }
        self.mTreeName.SetText(switch_3.get(Variable3_0, None))
        Variable2_0: bool = localIsTreeUnlocked
        ReturnValue_9: FText = Default__FGResearchTree.GetPostUnlockDescription(self.mResearchTree)
        ReturnValue_10: FText = Default__FGResearchTree.GetPreUnlockDescription(self.mResearchTree)
        
        switch_4 = {
            False: ReturnValue_10,
            True: ReturnValue_9
        }
        self.mDescription.SetText(switch_4.get(Variable2_0, None))
        if not localIsTreeUnlocked:
           goto(ExecutionFlow.Pop())
        ReturnValue_11: List[Ptr[FGResearchTreeNode]] = Default__FGResearchTree.GetNodes(self.mResearchTree)
        
        ReturnValue1: int32 = len(ReturnValue_11)
        localMaxResearchedNodes = ReturnValue1
        Variable_1: int32 = 0
        Variable_2: int32 = 0
        
        # Label 2315
        ReturnValue_12: int32 = len(ReturnValue_11)
        ReturnValue_13: bool = Variable_1 <= ReturnValue_12
        if not ReturnValue_13:
            goto('L2902')
        Variable_2 = Variable_1
        ExecutionFlow.Push("L3239")
        
        Item2 = None
        Item2 = ReturnValue_11[Variable_2]
        Node: Ptr[BPD_ResearchTreeNode] = Cast[BPD_ResearchTreeNode](Item2)
        bSuccess1: bool = Node
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_1: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue1_0)
        ReturnValue_14: bool = ReturnValue1_1.IsSchematicPurchased(Node.mNodeDataStruct.Schematic_27_3663A42446FDB4387D0C81AFC23E225B)
        if not ReturnValue_14:
           goto(ExecutionFlow.Pop())
        ReturnValue1_2: int32 = localResearchedNodes + 1
        Variable_3: int32 = ReturnValue1_2
        localResearchedNodes = Variable_3
        goto(ExecutionFlow.Pop())
        
        DependecyData = None
        # Label 2856
        Default__KismetArrayLibrary.Array_Clear(Ref[DependecyData])
        goto('L628')
        # Label 2902
        ReturnValue_15: float = Conv_IntToFloat(localMaxResearchedNodes)
        ReturnValue1_3: float = Conv_IntToFloat(localResearchedNodes)
        ReturnValue_16: float = ReturnValue1_3 / ReturnValue_15
        ReturnValue_17: float = self.mFullDuration * ReturnValue_16
        self.mLerpDuration = ReturnValue_17
        ReturnValue_15 = Conv_IntToFloat(localMaxResearchedNodes)
        ReturnValue1_3 = Conv_IntToFloat(localResearchedNodes)
        ReturnValue_16 = ReturnValue1_3 / ReturnValue_15
        self.StartProgressBarLerp(ReturnValue_16)
        goto(ExecutionFlow.Pop())
        # Label 3239
        ReturnValue_18: int32 = Variable_1 + 1
        Variable_1 = ReturnValue_18
        goto('L2315')
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_MAMTree_ListButtonInfo(10)
    

    def LerpProgressBar(self):
        self.ExecuteUbergraph_BPW_MAMTree_ListButtonInfo(130)
    

    def ExecuteUbergraph_BPW_MAMTree_ListButtonInfo(self):
        self.SetContent(self.mResearchTree)
        ReturnValue1: Ptr[MaterialInstanceDynamic] = self.mProgressBar.GetDynamicMaterial()
        ReturnValue1.SetScalarParameterValue("Value", 0)
        # End
        ReturnValue: float = self.mLerpUpdate / self.mLerpDuration
        ReturnValue_0: float = ReturnValue + self.mLerpT
        self.mLerpT = ReturnValue_0
        ReturnValue_1: Ptr[MaterialInstanceDynamic] = self.mProgressBar.GetDynamicMaterial()
        ReturnValue_2: float = Ease(0, self.mLerpEndValue, self.mLerpT, 3, 2, 2)
        ReturnValue_1.SetScalarParameterValue("Value", ReturnValue_2)
        ReturnValue_2 = Ease(0, self.mLerpEndValue, self.mLerpT, 3, 2, 2)
        ReturnValue_3: FText = Default__KismetTextLibrary.AsPercent_Float(ReturnValue_2, 0, False, True, 1, 324, 0, 0)
        self.mProgress.SetText(ReturnValue_3)
        ReturnValue_4: bool = GreaterEqual_FloatFloat(self.mLerpT, 1)
        if not ReturnValue_4:
            goto('L689')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mLerpTimer])
    
