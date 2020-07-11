
from codegen.ue4_stub import *

from Script.Engine import K2_SetTimerDelegate
from Script.Engine import FromSeconds
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Parent import Widget_ActorDetails_Parent
from Script.FactoryGame import FGBuildableRadarTower
from Script.CoreUObject import Timespan
from Script.FactoryGame import FGActorRepresentationInterface
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_RadarTower import ExecuteUbergraph_Widget_ActorDetails_RadarTower
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetCurrentExpansionStep
from Script.Engine import TimerHandle
from Script.Engine import Conv_IntToText
from Script.FactoryGame import IsProductionPaused
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import BreakTimespan
from Script.Engine import Format
from Script.Engine import AsPercent_Float
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Parent import Construct
from Script.FactoryGame import GetTimeToNextExpansion
from Script.FactoryGame import GetNormalizedProgressValueForStep
from Script.Engine import K2_ClearAndInvalidateTimerHandle

class Widget_ActorDetails_RadarTower(Widget_ActorDetails_Parent):
    mRadarTower: Ptr[FGBuildableRadarTower]
    mUpdateTimer: TimerHandle
    
    def GetScannedPercentText(self):
        ReturnValue: int32 = self.mRadarTower.GetCurrentExpansionStep()
        ReturnValue_0: float = self.mRadarTower.GetNormalizedProgressValueForStep(ReturnValue)
        ReturnValue_1: FText = Default__KismetTextLibrary.AsPercent_Float(ReturnValue_0, 0, False, True, 1, 324, 0, 0)
        Result = ReturnValue_1
    

    def GetTimeLeftInText(self):
        ReturnValue: float = self.mRadarTower.GetTimeToNextExpansion()
        ReturnValue_0: Timespan = FromSeconds(ReturnValue)
        
        Days = None
        Hours = None
        Minutes = None
        Seconds = None
        Milliseconds = None
        BreakTimespan(ReturnValue_0, Ref[Days], Ref[Hours], Ref[Minutes], Ref[Seconds], Ref[Milliseconds])
        ReturnValue_1: int32 = Days * 24
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_IntToText(Seconds, False, True, 2, 324)
        ReturnValue_3: int32 = ReturnValue_1 + Hours
        FormatArgumentData.ArgumentName = "seconds"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_2
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue1: int32 = ReturnValue_3 * 60
        ReturnValue1_0: int32 = ReturnValue1 + Minutes
        ReturnValue1_1: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue1_0, False, True, 2, 324)
        FormatArgumentData1.ArgumentName = "minutes"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue1_1
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_4: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 937, 'Value': '{minutes}:{seconds}'}", Array)
        Result = ReturnValue_4
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ActorDetails_RadarTower(10)
    

    def UpdateDetails(self):
        self.ExecuteUbergraph_Widget_ActorDetails_RadarTower(501)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_ActorDetails_RadarTower(986)
    

    def ExecuteUbergraph_Widget_ActorDetails_RadarTower(self):
        self.Construct()
        self.Widget_ActorDetails_Container.SetShowPointer(self.ShowPointer)
        Tower: Ptr[FGBuildableRadarTower] = Cast[FGBuildableRadarTower](self.mActor)
        bSuccess: bool = Tower
        if not bSuccess:
            goto('L1028')
        self.mRadarTower = Tower
        Interface: TScriptInterface[FGActorRepresentationInterface] = QueryInterface[FGActorRepresentationInterface](self.mRadarTower)
        bSuccess1: bool = Interface
        if not bSuccess1:
            goto('L476')
        ReturnValue: FText = GetInterfaceUObject(Interface).GetActorRepresentationText()
        # Label 297
        self.Widget_ActorDetails_Container.SetTitle(ReturnValue)
        self.UpdateDetails()
        OutputDelegate.BindUFunction(self, UpdateDetails)
        ReturnValue_0: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.5, True)
        self.mUpdateTimer = ReturnValue_0
        # End
        # Label 476
        ReturnValue = 
        goto('L297')
        
        Result = None
        self.GetTimeLeftInText(Ref[Result])
        self.mTimeLeft.SetText(Result)
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 589, 'Value': 'NO POWER'}"
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 655, 'Value': 'PAUSED'}"
        
        Result = None
        self.GetScannedPercentText(Ref[Result])
        ReturnValue_1: bool = self.mRadarTower.HasPower()
        ReturnValue_2: bool = self.mRadarTower.IsProductionPaused()
        Variable_0: bool = ReturnValue_1
        Variable1_0: bool = ReturnValue_2
        
        switch = {
            False: Variable,
            True: Result
        }
        
        switch_0 = {
            False: switch.get(Variable_0, None),
            True: Variable1
        }
        self.mScannedpercent.SetText(switch_0.get(Variable1_0, None))
        # End
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mUpdateTimer])
    
