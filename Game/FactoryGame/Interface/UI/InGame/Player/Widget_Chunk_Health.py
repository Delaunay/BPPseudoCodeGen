
from codegen.ue4_stub import *

from Script.FactoryGame import FGHealthComponent
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetParent
from Script.UMG import SetRenderScale
from Script.UMG import ESlateVisibility
from Script.CoreUObject import Vector2D
from Script.UMG import PanelWidget
from Script.UMG import GetChildIndex
from Script.Engine import IsValid
from Script.FactoryGame import GetCurrentHealth
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class Widget_Chunk_Health(UserWidget):
    mPlayerHealthComponent: Ptr[FGHealthComponent]
    mAmountOfHealthPerChunk: float
    
    def GetHealthChunkColor(self):
        ReturnValue: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_0: int32 = ReturnValue.GetChildIndex(self)
        ReturnValue_1: bool = ReturnValue_0 <= 4
        if not ReturnValue_1:
            goto('L210')
        self.SetRenderScale(Vector2D(X = 1, Y = 1))
        ReturnValue_2: LinearColor = LinearColor(R = 0, G = 0.02881699986755848, B = 0.06770800054073334, A = 0.800000011920929)
        goto('L296')
        # Label 210
        self.SetRenderScale(Vector2D(X = 0.800000011920929, Y = 0.800000011920929))
        ReturnValue_2 = LinearColor(R = 0.838798999786377, G = 0.8713669776916504, B = 0.887923002243042, A = 1)
    

    def GetChunkVisibility(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mPlayerHealthComponent)
        if not ReturnValue:
            goto('L400')
        Variable: uint8 = 0
        Variable1: uint8 = 1
        ReturnValue_0: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_1: int32 = ReturnValue_0.GetChildIndex(self)
        ReturnValue_2: float = ReturnValue_1 * self.mAmountOfHealthPerChunk
        ReturnValue_3: float = self.mPlayerHealthComponent.GetCurrentHealth()
        ReturnValue_4: bool = ReturnValue_3 > ReturnValue_2
        Variable_0: bool = ReturnValue_4
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_5: uint8 = switch.get(Variable_0, None)
    
