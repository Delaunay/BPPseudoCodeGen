
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import EqualEqual_FloatFloat
from Script.Engine import PlayerController
from Script.UMG import AddChild
from Game.FactoryGame.Interface.UI.InGame.CursorParticles.CursorParticle_Radiation import ExecuteUbergraph_CursorParticle_Radiation
from Script.UMG import Create
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Smoke import Widget_Smoke
from Script.Engine import FFloor
from Script.UMG import PanelSlot
from Script.Engine import Conv_IntToFloat
from Script.Engine import PrintString
from Game.FactoryGame.Interface.UI.InGame.CursorParticles.BP_CursorParticle import BP_CursorParticle
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.CoreUObject import LinearColor

class CursorParticle_Radiation(BP_CursorParticle):
    
    
    def Construct(self):
        self.ExecuteUbergraph_CursorParticle_Radiation(545)
    

    def ExecuteUbergraph_CursorParticle_Radiation(self):
        # Label 10
        Default__KismetSystemLibrary.PrintString(self, "Radiation", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        ReturnValue: float = Conv_IntToFloat(self.mClickCount)
        ReturnValue_0: float = ReturnValue / 5
        ReturnValue_1: int32 = FFloor(ReturnValue_0)
        ReturnValue1: float = Conv_IntToFloat(ReturnValue_1)
        ReturnValue_2: bool = EqualEqual_FloatFloat(ReturnValue_0, ReturnValue1)
        if not ReturnValue_2:
            goto('L550')
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[Widget_Smoke] = Default__WidgetBlueprintLibrary.Create(self, Widget_Smoke, ReturnValue_3)
        ReturnValue_4: Ptr[PanelSlot] = self.mDarkSmokeContainer.AddChild(ReturnValue1_0)
        ReturnValue_5: Ptr[Widget_Smoke] = Default__WidgetBlueprintLibrary.Create(self, Widget_Smoke, None)
        ReturnValue1_1: Ptr[PanelSlot] = self.mLightSmokeContainer.AddChild(ReturnValue_5)
        # End
        goto('L10')
    
