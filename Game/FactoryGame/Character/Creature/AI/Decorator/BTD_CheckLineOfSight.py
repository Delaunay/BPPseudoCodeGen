
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Actor
from Script.Engine import Default__GameplayStatics
from Script.AIModule import BTDecorator_BlueprintBase
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Char_Spitter import Char_Spitter
from Script.CoreUObject import Vector
from Script.Engine import BreakHitResult
from Script.Engine import LineTraceSingle
from Script.Engine import GetActorForwardVector
from Script.CoreUObject import LinearColor

class BTD_CheckLineOfSight(BTDecorator_BlueprintBase):
    bIsObservingBB = True
    
    def PerformConditionCheckAI(self):
        Array: Const[List[Ptr[Actor]]] = [ControlledPawn]
        ReturnValue: Vector = ControlledPawn.GetActorForwardVector()
        Spitter: Ptr[Char_Spitter] = Cast[Char_Spitter](ControlledPawn)
        bSuccess: bool = Spitter
        ReturnValue_0: Vector = ReturnValue * 2000
        ReturnValue_1: Vector = Spitter.Mesh.GetSocketLocation("head")
        ReturnValue_2: Vector = ReturnValue_1 + ReturnValue_0
        
        OutHit = None
        ReturnValue_3: bool = Default__KismetSystemLibrary.LineTraceSingle(self, ReturnValue_1, ReturnValue_2, 1, False, 0, True, LinearColor(R = 1, G = 0, B = 0, A = 1), LinearColor(R = 0, G = 1, B = 0, A = 1), 5, Ref[Array], Ref[OutHit])
        
        OutHit = None
        bBlockingHit = None
        bInitialOverlap = None
        Time = None
        Distance = None
        Location = None
        ImpactPoint = None
        Normal = None
        ImpactNormal = None
        PhysMat = None
        HitActor = None
        HitComponent = None
        HitBoneName = None
        HitItem = None
        FaceIndex = None
        TraceStart = None
        TraceEnd = None
        Default__GameplayStatics.BreakHitResult(Ref[OutHit], Ref[bBlockingHit], Ref[bInitialOverlap], Ref[Time], Ref[Distance], Ref[Location], Ref[ImpactPoint], Ref[Normal], Ref[ImpactNormal], Ref[PhysMat], Ref[HitActor], Ref[HitComponent], Ref[HitBoneName], Ref[HitItem], Ref[FaceIndex], Ref[TraceStart], Ref[TraceEnd])
        Spitter1: Ptr[Char_Spitter] = Cast[Char_Spitter](HitActor)
        bSuccess1: bool = Spitter1
        if not bSuccess1:
            goto('L750')
        ReturnValue_4: bool = True
        goto('L761')
        # Label 750
        ReturnValue_4 = False
    
