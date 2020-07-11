
from codegen.ue4_stub import *

from Script.FactoryGame import FGAISystem

class BP_AISystem(FGAISystem):
    mDisableAIDistance = 24000
    mNavWalkingDistance = 4000
    mMeshTickEnableDistance = 20000
    mMeshUpdateDistance = 12000
    mActivateSpawnerDistance = 12000
    mDisablePawnMovement = True
    mMaxCreatureIterationsPerTick = 10
    mMaxSpawnerIterationsPerTick = 10
    mMaxSpawnWeight = 10
    mMinSpawnDistance = 2500
    mKeepAliveDistanceToPlayer = 4000
    
