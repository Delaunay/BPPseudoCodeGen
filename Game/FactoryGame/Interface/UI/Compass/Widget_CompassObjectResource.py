
from codegen.ue4_stub import *

from Script.UMG import SetSize
from Script.Engine import FClamp
from Script.FactoryGame import FGCompassObjectWidget
from Script.FactoryGame import OnCompassObjectUpdated
from Script.Engine import Pawn
from Script.UMG import EUMGSequencePlayMode
from Script.Engine import VSize
from Game.FactoryGame.Interface.UI.Compass.Widget_CompassObjectResource import ExecuteUbergraph_Widget_CompassObjectResource.K2Node_Event_parentSlot
from Script.UMG import SetAutoSize
from Script.Engine import FTrunc
from Script.Engine import GetPlayerPawn
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import SetRenderScale
from Script.Engine import FormatArgumentData
from Script.UMG import PlayAnimation
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.Compass.Widget_CompassObjectResource import ExecuteUbergraph_Widget_CompassObjectResource
from Script.Engine import Default__KismetTextLibrary
from Script.UMG import SetOpacity
from Script.Engine import Default__GameplayStatics
from Script.UMG import Construct
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.Engine import Format
from Script.UMG import WidgetAnimation
from Script.Engine import NormalizeToRange
from Script.Engine import K2_GetActorLocation
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import GetActorLocation
from Script.FactoryGame import GetActorRepresentation
from Script.FactoryGame import OnCompassObjectAddedToPanel
from Script.CoreUObject import Vector2D
from Script.Engine import Abs
from Script.FactoryGame import FGActorRepresentation
from Game.FactoryGame.Interface.UI.Compass.Widget_CompassObjectResource import ExecuteUbergraph_Widget_CompassObjectResource.K2Node_Event_MyGeometry
from Script.FactoryGame import GetAlphaAmount
from Game.FactoryGame.Interface.UI.Compass.Widget_CompassObjectResource import ExecuteUbergraph_Widget_CompassObjectResource.K2Node_Event_centered
from Game.FactoryGame.Interface.UI.Compass.Widget_CompassObjectResource import ExecuteUbergraph_Widget_CompassObjectResource.K2Node_Event_InDeltaTime

class Widget_CompassObjectResource(FGCompassObjectWidget):
    NewAnimation_1: Ptr[WidgetAnimation]
    mTextAlpha: float
    minIconSize: float = 0.5
    maxIconSize: float = 1
    MinRangeFromTarget: float = 8000
    MaxRangeFromTarget: float = 30000
    mPositionOffset = Namespace(X=0, Y=-55)
    mClampPosition = True
    mCheckForBlockingInCompass = True
    
    def GetText_0(self):
        ReturnValue: Ptr[FGActorRepresentation] = self.GetActorRepresentation()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L764')
        ReturnValue_1: Ptr[Pawn] = Default__GameplayStatics.GetPlayerPawn(self, 0)
        ReturnValue = self.GetActorRepresentation()
        ReturnValue_2: Vector = ReturnValue_1.K2_GetActorLocation()
        ReturnValue_3: Vector = ReturnValue.GetActorLocation()
        ReturnValue_4: Vector = Subtract_VectorVector(ReturnValue_3, ReturnValue_2)
        ReturnValue_5: float = VSize(ReturnValue_4)
        ReturnValue_6: float = ReturnValue_5 / 100
        ReturnValue_7: int32 = FTrunc(ReturnValue_6)
        FormatArgumentData.ArgumentName = "Distance"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = ReturnValue_7
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_8: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 678, 'Value': '{Distance}m'}", Array)
        ReturnValue_9: FText = ReturnValue_8
    

    def OnCompassObjectAddedToPanel(self):
        ExecuteUbergraph_Widget_CompassObjectResource.K2Node_Event_parentSlot = parentSlot #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_CompassObjectResource(15)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_CompassObjectResource(2036)
    

    def OnCompassObjectUpdated(self):
        self.ExecuteUbergraph_Widget_CompassObjectResource(2093)
    

    def Tick(self):
        ExecuteUbergraph_Widget_CompassObjectResource.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_CompassObjectResource.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_CompassObjectResource(2150)
    

    def OnObjectCentered(self):
        ExecuteUbergraph_Widget_CompassObjectResource.K2Node_Event_centered = centered #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_CompassObjectResource(2155)
    

    def ExecuteUbergraph_Widget_CompassObjectResource(self):
        goto(ComputedJump("EntryPoint"))
        self.OnCompassObjectAddedToPanel(parentSlot)
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.NewAnimation_1, 0, 1, 0, 1)
        parentSlot.SetAutoSize(False)
        parentSlot.SetSize(Vector2D(X = 50, Y = 50))
        goto(ExecutionFlow.Pop())
        # Label 170
        ReturnValue_0: float = self.GetAlphaAmount()
        self.mTextAlpha = ReturnValue_0
        goto(ExecutionFlow.Pop())
        # Label 226
        if not self.mIsBlocking:
            goto('L397')
        self.mDistanceText.SetOpacity(self.mTextAlpha)
        ReturnValue_1: float = InDeltaTime * 5
        ReturnValue3: float = self.mTextAlpha - ReturnValue_1
        self.mTextAlpha = ReturnValue3
        goto(ExecutionFlow.Pop())
        # Label 397
        ReturnValue_0 = self.GetAlphaAmount()
        self.mDistanceText.SetOpacity(ReturnValue_0)
        goto('L170')
        # Label 471
        ExecutionFlow.Push("L1958")
        ExecutionFlow.Push("L226")
        ReturnValue_2: Ptr[Pawn] = Default__GameplayStatics.GetPlayerPawn(self, 0)
        ReturnValue_3: Vector = ReturnValue_2.K2_GetActorLocation()
        ReturnValue_4: float = FClamp(self.minIconSize, 0, 1)
        ReturnValue_5: float = ReturnValue_4 - 1
        ReturnValue1: float = FClamp(self.maxIconSize, 0, 1)
        ReturnValue_6: float = Abs(ReturnValue_5)
        ReturnValue1_0: float = ReturnValue1 - 1
        ReturnValue1_1: float = Abs(ReturnValue1_0)
        ReturnValue_7: Vector = self.mActorRepresentation.GetActorLocation()
        ReturnValue_8: Vector = Subtract_VectorVector(ReturnValue_7, ReturnValue_3)
        ReturnValue_9: float = VSize(ReturnValue_8)
        ReturnValue_10: float = NormalizeToRange(ReturnValue_9, self.MinRangeFromTarget, self.MaxRangeFromTarget)
        ReturnValue2: float = FClamp(ReturnValue_10, ReturnValue1_1, ReturnValue_6)
        ReturnValue2_0: float = ReturnValue2 - 1
        ReturnValue2_1: float = Abs(ReturnValue2_0)
        ReturnValue_11: Vector2D = Vector2D(ReturnValue2_1, ReturnValue2_1)
        self.mImage.SetRenderScale(ReturnValue_11)
        ReturnValue_2 = Default__GameplayStatics.GetPlayerPawn(self, 0)
        ReturnValue_3 = ReturnValue_2.K2_GetActorLocation()
        ReturnValue_4 = FClamp(self.minIconSize, 0, 1)
        ReturnValue_5 = ReturnValue_4 - 1
        ReturnValue1 = FClamp(self.maxIconSize, 0, 1)
        ReturnValue_6 = Abs(ReturnValue_5)
        ReturnValue1_0 = ReturnValue1 - 1
        ReturnValue1_1 = Abs(ReturnValue1_0)
        ReturnValue_7 = self.mActorRepresentation.GetActorLocation()
        ReturnValue_8 = Subtract_VectorVector(ReturnValue_7, ReturnValue_3)
        ReturnValue_9 = VSize(ReturnValue_8)
        ReturnValue_10 = NormalizeToRange(ReturnValue_9, self.MinRangeFromTarget, self.MaxRangeFromTarget)
        ReturnValue2 = FClamp(ReturnValue_10, ReturnValue1_1, ReturnValue_6)
        ReturnValue2_0 = ReturnValue2 - 1
        ReturnValue2_1 = Abs(ReturnValue2_0)
        self.Widget_MapCompass_Icon.SetScale(ReturnValue2_1)
        goto(ExecutionFlow.Pop())
        # Label 1958
        ReturnValue_12: FText = self.GetText_0()
        self.Widget_MapCompass_Icon.SetDescription(ReturnValue_12)
        goto(ExecutionFlow.Pop())
        self.Construct()
        self.Widget_MapCompass_Icon.UpdateActor(self.mActorRepresentation, True)
        goto(ExecutionFlow.Pop())
        self.OnCompassObjectUpdated()
        self.Widget_MapCompass_Icon.UpdateActor(self.mActorRepresentation, True)
        goto(ExecutionFlow.Pop())
        goto('L471')
        Variable: uint8 = 1
        Variable1: uint8 = 0
        Variable_0: bool = centered
        
        switch = {
            False: Variable,
            True: Variable1
        }
        ReturnValue1_2: Ptr[UMGSequencePlayer] = self.Widget_MapCompass_Icon.PlayAnimation(self.Widget_MapCompass_Icon.ShowDescription, 0, 1, switch.get(Variable_0, None), 1)
        goto(ExecutionFlow.Pop())
    
