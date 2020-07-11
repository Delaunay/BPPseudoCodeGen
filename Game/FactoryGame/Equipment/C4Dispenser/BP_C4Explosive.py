
from codegen.ue4_stub import *

from Script.Engine import ParticleSystemComponent
from Game.FactoryGame.Equipment.C4Dispenser.BP_C4Explosive import ExecuteUbergraph_BP_C4Explosive.K2Node_Event_saveVersion3
from Script.Engine import K2_GetActorLocation
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGC4Explosive
from Game.FactoryGame.Equipment.C4Dispenser.Particles.C4Explosion import C4Explosion
from Game.FactoryGame.Equipment.C4Dispenser.BP_C4Explosive import ExecuteUbergraph_BP_C4Explosive
from Game.FactoryGame.Equipment.C4Dispenser.BP_C4Explosive import ExecuteUbergraph_BP_C4Explosive.K2Node_Event_gameVersion2
from Script.CoreUObject import Vector
from Game.FactoryGame.Equipment.C4Dispenser.BP_C4Explosive import ExecuteUbergraph_BP_C4Explosive.K2Node_Event_gameVersion3
from Game.FactoryGame.Equipment.C4Dispenser.BP_C4Explosive import ExecuteUbergraph_BP_C4Explosive.K2Node_Event_saveVersion1
from Script.CoreUObject import Object
from Game.FactoryGame.Equipment.C4Dispenser.BP_C4Explosive import ExecuteUbergraph_BP_C4Explosive.K2Node_Event_gameVersion1
from Game.FactoryGame.Equipment.C4Dispenser.BP_C4Explosive import ExecuteUbergraph_BP_C4Explosive.K2Node_Event_gameVersion
from Script.Engine import SpawnEmitterAtLocation
from Game.FactoryGame.Equipment.C4Dispenser.BP_C4Explosive import ExecuteUbergraph_BP_C4Explosive.K2Node_Event_saveVersion
from Game.FactoryGame.Equipment.C4Dispenser.BP_C4Explosive import ExecuteUbergraph_BP_C4Explosive.K2Node_Event_saveVersion2

class BP_C4Explosive(FGC4Explosive):
    mBaseDamage = 40
    mDamageRadius = 500
    mDamageType = NewObject[DamageType_C4]()
    bReplicateMovement = True
    bReplicates = True
    RemoteRole = 1
    
    def ShouldSave(self):
        ReturnValue = True
    

    def GatherDependencies(self):
        Array: List[Ptr[Object]] = []
        dependentObjects: List[Ptr[Object]] = Array
    

    def NeedTransform(self):
        ReturnValue = False
    

    def PostSaveGame(self):
        ExecuteUbergraph_BP_C4Explosive.K2Node_Event_saveVersion3 = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_C4Explosive.K2Node_Event_gameVersion3 = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_C4Explosive(10)
    

    def PreLoadGame(self):
        ExecuteUbergraph_BP_C4Explosive.K2Node_Event_saveVersion2 = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_C4Explosive.K2Node_Event_gameVersion2 = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_C4Explosive(174)
    

    def PreSaveGame(self):
        ExecuteUbergraph_BP_C4Explosive.K2Node_Event_saveVersion1 = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_C4Explosive.K2Node_Event_gameVersion1 = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_C4Explosive(179)
    

    def PlayExplosionEffects(self):
        self.ExecuteUbergraph_BP_C4Explosive(184)
    

    def PostLoadGame(self):
        ExecuteUbergraph_BP_C4Explosive.K2Node_Event_saveVersion = SaveVersion #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_C4Explosive.K2Node_Event_gameVersion = GameVersion #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_C4Explosive(189)
    

    def ExecuteUbergraph_BP_C4Explosive(self):
        # End
        # Label 15
        self.RadialForce.FireImpulse()
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue_0: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, C4Explosion, ReturnValue, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        # End
        # End
        # End
        goto('L15')
    
