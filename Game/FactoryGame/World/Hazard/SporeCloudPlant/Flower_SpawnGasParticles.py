
from codegen.ue4_stub import *

from Game.FactoryGame.World.Hazard.SporeCloudPlant.BP_SporeFlower import BP_SporeFlower
from Script.Engine import Actor
from Script.Engine import AnimNotify
from Script.Engine import GetOwner

class Flower_SpawnGasParticles(AnimNotify):
    
    
    def Received_Notify(self):
        ReturnValue: Ptr[Actor] = MeshComp.GetOwner()
        Flower: Ptr[BP_SporeFlower] = Cast[BP_SporeFlower](ReturnValue)
        bSuccess: bool = Flower
        if not bSuccess:
            goto('L157')
        Flower.SpawnGasParticles()
        # Label 157
        ReturnValue_0: bool = True
    
