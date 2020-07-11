
from codegen.ue4_stub import *

from Script.FactoryGame import LostSignificance
from Game.FactoryGame.Resource.BP_ResourceNode import ExecuteUbergraph_BP_ResourceNode
from Script.FactoryGame import GainedSignificance
from Script.FactoryGame import FGResourceNode

class BP_ResourceNode(FGResourceNode):
    mPurity = 1
    mAmount = 3
    mCanPlaceResourceExtractor = True
    mExtractMultiplier = 1
    mPurityTextArray = [{'text': 'NSLOCTEXT("", "76E9FCCD4AE33939793AE39835BDFF55", "<Bold> (Impure)</>")', 'Purity': 0}, {'text': 'NSLOCTEXT("", "0EAFDECF41459ADE162DE5A3FC2CEB8C", "<Bold> (Normal)</>")', 'Purity': 1}, {'text': 'NSLOCTEXT("", "C5FFC08F4501FBDDD5D3DEA66CD04D9C", "<Bold>(Pure)</>")', 'Purity': 2}]
    mDoSpawnParticle = True
    mAddToSignificanceManager = True
    bReplicates = True
    RemoteRole = 1
    
    def GainedSignificance(self):
        self.ExecuteUbergraph_BP_ResourceNode(25)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_BP_ResourceNode(40)
    

    def ExecuteUbergraph_BP_ResourceNode(self):
        # Label 10
        self.LostSignificance()
        # End
        self.GainedSignificance()
        # End
        goto('L10')
    
