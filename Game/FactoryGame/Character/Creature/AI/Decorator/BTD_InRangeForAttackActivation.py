
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import IsWithinRange
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import BTDecorator_BlueprintBase
from Script.CoreUObject import LinearColor
from Script.FactoryGame import Default__FGAttack
from Script.FactoryGame import Default__FGCombatFunctionLibrary
from Script.AIModule import BlackboardKeySelector
from Script.CoreUObject import Object
from Script.FactoryGame import FGAttack
from Script.FactoryGame import GetAttackActivationDistance
from Script.Engine import IsValidClass
from Script.AIModule import GetBlackboardValueAsObject
from Script.Engine import PrintString
from Script.FactoryGame import FGAggroTargetInterface

class BTD_InRangeForAttackActivation(BTDecorator_BlueprintBase):
    mAttack: TSubclassOf[FGAttack]
    mEnemyBBKey: BlackboardKeySelector
    bIsObservingBB = True
    
    def PerformConditionCheckAI(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mAttack)
        if not ReturnValue:
            goto('L334')
        
        ReturnValue_0: Ptr[Object] = Default__BTFunctionLibrary.GetBlackboardValueAsObject(self, Ref[self.mEnemyBBKey])
        Interface: TScriptInterface[FGAggroTargetInterface] = QueryInterface[FGAggroTargetInterface](ReturnValue_0)
        bSuccess: bool = Interface
        ReturnValue_1: float = Default__FGAttack.GetAttackActivationDistance(self.mAttack)
        ReturnValue_2: bool = Default__FGCombatFunctionLibrary.IsWithinRange(ControlledPawn, Interface, ReturnValue_1)
        ReturnValue_3: bool = ReturnValue_2
        goto('L458')
        # Label 334
        Default__KismetSystemLibrary.PrintString(self, "no valid class in BTD_InrangeForAttackActivation", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
    
