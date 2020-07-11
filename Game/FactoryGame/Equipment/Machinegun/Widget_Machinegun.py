
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.Machinegun.Equip_Machinegun import Equip_Machinegun
from Game.FactoryGame.Equipment.Machinegun.Widget_Machinegun import ExecuteUbergraph_Widget_Machinegun.K2Node_Event_MyGeometry
from Game.FactoryGame.Equipment.Machinegun.Widget_Machinegun import ExecuteUbergraph_Widget_Machinegun
from Script.UMG import UserWidget
from Script.FactoryGame import GetMagSize
from Script.Engine import FormatArgumentData
from Script.UMG import Tick
from Script.Engine import Format
from Script.FactoryGame import GetSpareAmmunition
from Script.UMG import WidgetAnimation
from Script.Engine import Conv_IntToText
from Script.FactoryGame import GetCurrentAmmo
from Game.FactoryGame.Equipment.Machinegun.Widget_Machinegun import ExecuteUbergraph_Widget_Machinegun.K2Node_Event_InDeltaTime
from Script.Engine import Default__KismetTextLibrary

class Widget_Machinegun(UserWidget):
    TextGoesFlash: Ptr[WidgetAnimation]
    TestDiscoAnimation: Ptr[WidgetAnimation]
    mNailGun: Ptr[Equip_Machinegun]
    
    def GetAmmoAvailable(self):
        ReturnValue: int32 = self.mNailGun.GetSpareAmmunition()
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue, False, True, 1, 324)
        FormatArgumentData.ArgumentName = "A"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_0
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 380, 'Value': 'Total:{A}'}", Array)
        ReturnValue_2: FText = ReturnValue_1
    

    def GetAmmoText(self):
        ReturnValue: int32 = self.mNailGun.GetMagSize()
        ReturnValue_0: int32 = self.mNailGun.GetCurrentAmmo()
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue, False, True, 1, 324)
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_0, False, True, 1, 324)
        FormatArgumentData.ArgumentName = "MagSize"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_1
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "Current"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue1
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_2: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 710, 'Value': '{Current}/{MagSize}'}", Array)
        ReturnValue_3: FText = ReturnValue_2
    

    def Tick(self):
        ExecuteUbergraph_Widget_Machinegun.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Machinegun.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Machinegun(10)
    

    def ExecuteUbergraph_Widget_Machinegun(self):
        self.Tick(MyGeometry, InDeltaTime)
    
