
from codegen.ue4_stub import *

from Script.Engine import Conv_StringToText
from Game.FactoryGame.Interface.UI.InGame.Widget_AggroText import ExecuteUbergraph_Widget_AggroText.K2Node_Event_MyGeometry
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.InGame.Widget_AggroText import ExecuteUbergraph_Widget_AggroText.K2Node_Event_InDeltaTime
from Script.Engine import Conv_FloatToString
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import EqualEqual_StrStr
from Script.Engine import Concat_StrStr
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Interface.UI.InGame.Widget_AggroText import ExecuteUbergraph_Widget_AggroText

class Widget_AggroText(UserWidget):
    mActualAggro: float
    mDisplayedAggro: float
    IngoreStatus: FString
    ActorName: FString
    
    def Get_Text_Text_0(self):
        ReturnValue: FString = Default__KismetStringLibrary.Concat_StrStr(self.ActorName, " aggro ")
        ReturnValue_0: FString = Default__KismetStringLibrary.Conv_FloatToString(self.mDisplayedAggro)
        ReturnValue1: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue, ReturnValue_0)
        ReturnValue2: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue1, "status =")
        ReturnValue3: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue2, self.IngoreStatus)
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue3)
        ReturnValue_2: FText = ReturnValue_1
    

    def SetAggroData(self, Aggro: float, ActorName: FString, Status: FString):
        self.IngoreStatus = Status
        self.ActorName = ActorName
        self.mActualAggro = Aggro
        ReturnValue: bool = self.mActualAggro > 0
        if not ReturnValue:
            goto('L156')
        self.mDisplayedAggro = self.mActualAggro
    

    def Tick(self):
        ExecuteUbergraph_Widget_AggroText.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_AggroText.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_AggroText(53)
    

    def ExecuteUbergraph_Widget_AggroText(self):
        # Label 10
        self.text.SetText()
        # End
        ReturnValue: bool = Default__KismetStringLibrary.EqualEqual_StrStr(self.ActorName, "")
        if not ReturnValue:
            goto('L125')
        goto('L10')
        # Label 125
        ReturnValue_0: FString = Default__KismetStringLibrary.Conv_FloatToString(self.mDisplayedAggro)
        ReturnValue_1: FString = Default__KismetStringLibrary.Concat_StrStr(self.ActorName, " aggro ")
        ReturnValue1: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue_1, ReturnValue_0)
        ReturnValue2: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue1, "status =")
        ReturnValue3: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue2, self.IngoreStatus)
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue3)
        self.text.SetText(ReturnValue_2)
    
