
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import FormatArgumentData
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_TrainStation import ExecuteUbergraph_Widget_ActorDetails_TrainStation
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Parent import Construct
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Parent import Destruct
from Script.Engine import Conv_FloatToText
from Script.Engine import Format
from Script.FactoryGame import FGBuildableRailroadStation
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Parent import Widget_ActorDetails_Parent
from Script.FactoryGame import GetActualConsumption
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.FactoryGame import FGPowerInfoComponent
from Script.FactoryGame import HasPower
from Script.FactoryGame import GetPowerInfo
from Script.Engine import Default__KismetTextLibrary

class Widget_ActorDetails_TrainStation(Widget_ActorDetails_Parent):
    mPowerComponent: Ptr[FGPowerInfoComponent]
    mTrainStation: Ptr[FGBuildableRailroadStation]
    
    def GetPowerConsumption(self, TrainStation: Ptr[FGBuildableFactory]):
        ReturnValue: Ptr[FGPowerInfoComponent] = TrainStation.GetPowerInfo()
        ReturnValue_0: float = ReturnValue.GetActualConsumption()
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_0, 0, False, True, 1, 324, 1, 1)
        FormatArgumentData.ArgumentName = "Value"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_1
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_2: FText = Default__KismetTextLibrary.Format(STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/ST_Units.ST_Units", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 496, 'Value': 'Value_MWh'}", Array)
        self.mPowerConsumptionText.SetText(ReturnValue_2)
    

    def CheckIfPowerConnected(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mTrainStation)
        if not ReturnValue:
            goto('L413')
        ReturnValue_0: Ptr[FGPowerInfoComponent] = self.mTrainStation.GetPowerInfo()
        ReturnValue_1: bool = ReturnValue_0.HasPower()
        Variable: bool = ReturnValue_1
        Variable_0: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 188, 'Value': 'Connected'}"
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 255, 'Value': 'Disconnected'}"
        
        switch = {
            False: Variable1,
            True: Variable_0
        }
        self.mHasPowerText.SetText(switch.get(Variable, None))
        mTrainStation = self.mTrainStation
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ActorDetails_TrainStation(61)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_ActorDetails_TrainStation(476)
    

    def UpdateTrainStationStats(self):
        self.ExecuteUbergraph_Widget_ActorDetails_TrainStation(533)
    

    def ExecuteUbergraph_Widget_ActorDetails_TrainStation(self):
        
        mTrainStation = None
        # Label 10
        self.CheckIfPowerConnected(Ref[mTrainStation])
        self.GetPowerConsumption(mTrainStation)
        # End
        self.Construct()
        self.Widget_ActorDetails_Container.SetShowPointer(self.ShowPointer)
        Station: Ptr[FGBuildableRailroadStation] = Cast[FGBuildableRailroadStation](self.mActor)
        bSuccess: bool = Station
        if not bSuccess:
            goto('L538')
        self.mTrainStation = Station
        self.Widget_ActorDetails_Container.SetTitle(self.mTrainStation.mDisplayName)
        ReturnValue: Ptr[FGPowerInfoComponent] = self.mTrainStation.GetPowerInfo()
        self.mPowerComponent = ReturnValue
        self.UpdateTrainStationStats()
        OutputDelegate.BindUFunction(self, UpdateTrainStationStats)
        ReturnValue_0: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.30000001192092896, True)
        self.mActorDetailsUpdateTimer = ReturnValue_0
        # End
        self.Destruct()
        
        self.mActorDetailsUpdateTimer = None
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mActorDetailsUpdateTimer])
        # End
        goto('L10')
    
