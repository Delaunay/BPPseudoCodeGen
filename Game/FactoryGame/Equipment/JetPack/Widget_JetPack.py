
from codegen.ue4_stub import *

from Script.Engine import FClamp
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Pawn
from Script.Engine import MapRangeUnclamped
from Script.Engine import FFloor
from Script.FactoryGame import IsEquipped
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Script.FactoryGame import FGEquipment
from Script.FactoryGame import GetActiveEquipments
from Script.Engine import IsValid
from Game.FactoryGame.Equipment.JetPack.Equip_JetPack import Equip_JetPack
from Game.FactoryGame.Equipment.JetPack.Widget_JetPack import ExecuteUbergraph_Widget_JetPack.K2Node_Event_MyGeometry
from Script.Engine import Conv_IntToText
from Script.Engine import Default__KismetTextLibrary
from Script.UMG import Tick
from Script.Engine import Format
from Script.Engine import LinearColorLerp
from Script.Engine import MakeLiteralText
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Equipment.JetPack.Widget_JetPack import ExecuteUbergraph_Widget_JetPack.K2Node_Event_InDeltaTime
from Script.UMG import UserWidget
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Equipment.JetPack.Widget_JetPack import ExecuteUbergraph_Widget_JetPack
from Script.CoreUObject import LinearColor

class Widget_JetPack(UserWidget):
    aJetpackColour: Ptr[WidgetAnimation]
    
    def GetFuelText(self):
        
        JetPack = None
        self.GetJetPack(Ref[JetPack])
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(JetPack)
        if not ReturnValue:
            goto('L942')
        ReturnValue_0: FText = Default__KismetSystemLibrary.MakeLiteralText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 139, 'Value': '%'}")
        FormatArgumentData.ArgumentName = "%"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_0
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue_1: float = MapRangeUnclamped(JetPack.mCurrentFuel, 0, JetPack.mMaxFuel, 0, 100)
        ReturnValue_2: int32 = FFloor(ReturnValue_1)
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_2, False, True, 1, 324)
        FormatArgumentData1.ArgumentName = "Range"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue_3
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_4: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 852, 'Value': '{Range}{%}'}", Array)
        ReturnValue_5: FText = ReturnValue_4
        goto('L962')
        # Label 942
        ReturnValue_5 = 
    

    def GetJetPack(self):
        ExecutionFlow.Push("L637")
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 146
        ReturnValue_0: List[Ptr[FGEquipment]] = Player.GetActiveEquipments()
        
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
            goto('L547')
        Variable_0 = Variable
        ExecutionFlow.Push("L563")
        ReturnValue_0 = Player.GetActiveEquipments()
        
        Item = None
        Item = ReturnValue_0[Variable_0]
        Pack: Ptr[Equip_JetPack] = Cast[Equip_JetPack](Item)
        bSuccess1: bool = Pack
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Jetpack = Pack
        # End
        # Label 547
        Jetpack = None
        # End
        # Label 563
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L146')
    

    def GetFuelColor(self):
        
        JetPack = None
        self.GetJetPack(Ref[JetPack])
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(JetPack)
        if not ReturnValue:
            goto('L294')
        ReturnValue_0: float = FClamp(JetPack.mCurrentFuel, 0, 1)
        ReturnValue_1: LinearColor = LinearColorLerp(LinearColor(R = 0, G = 0.02881699986755848, B = 0.06770800054073334, A = 1), LinearColor(R = 0.838798999786377, G = 0.8713669776916504, B = 0.887923002243042, A = 1), ReturnValue_0)
        ReturnValue_2: LinearColor = ReturnValue_1
        goto('L346')
        # Label 294
        ReturnValue_2 = LinearColor(R = 0, G = 0, B = 0, A = 0)
    

    def GetFuelPct(self):
        
        JetPack = None
        self.GetJetPack(Ref[JetPack])
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(JetPack)
        if not ReturnValue:
            goto('L142')
        ReturnValue_0: float = JetPack.mCurrentFuel
        goto('L165')
        # Label 142
        ReturnValue_0 = 0
    

    def Tick(self):
        ExecuteUbergraph_Widget_JetPack.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_JetPack.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_JetPack(240)
    

    def ExecuteUbergraph_Widget_JetPack(self):
        
        JetPack = None
        # Label 10
        self.GetJetPack(Ref[JetPack])
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(JetPack)
        if not ReturnValue:
            goto('L197')
        ReturnValue_0: bool = JetPack.IsEquipped()
        if not ReturnValue_0:
            goto('L197')
        self.Border1.SetVisibility(0)
        # End
        # Label 197
        self.Border1.SetVisibility(2)
        # End
        self.Tick(MyGeometry, InDeltaTime)
        goto('L10')
    
