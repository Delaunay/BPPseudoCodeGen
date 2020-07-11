
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import LostSignificance
from Game.FactoryGame.Resource.BP_ResourceNodeGeyser import ExecuteUbergraph_BP_ResourceNodeGeyser.K2Node_Event_newIsOccupied
from Script.AkAudio import PostAkEvent
from Script.Engine import BooleanOR
from Game.FactoryGame.Resource.BP_ResourceNodeGeyser import ExecuteUbergraph_BP_ResourceNodeGeyser
from Script.Engine import RandomFloatInRange
from Script.Engine import Delay
from Script.AkAudio import AkComponent
from Script.FactoryGame import GainedSignificance
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.FactoryGame import FGResourceNodeGeyser
from Script.FactoryGame import OnIsOccupiedChanged

class BP_ResourceNodeGeyser(FGResourceNodeGeyser):
    mMinEruptDelay: float = 10
    mMaxEruptDelay: float = 20
    mAudioSyncTimer: float
    m_RandomStartDelayMin: float = 3
    m_RandomStartDelayMax: float = 9
    mIsSignificant: bool
    mEruptLoopOngoing: bool
    mResourceClass = NewObject[Desc_Geyser]()
    mPurity = 1
    mAmount = 3
    mCanPlaceResourceExtractor = True
    mExtractMultiplier = 1
    mDoSpawnParticle = True
    mAddToSignificanceManager = True
    bReplicates = True
    RemoteRole = 1
    
    def OnIsOccupiedChanged(self):
        ExecuteUbergraph_BP_ResourceNodeGeyser.K2Node_Event_newIsOccupied = newIsOccupied #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_ResourceNodeGeyser(582)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_BP_ResourceNodeGeyser(659)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_BP_ResourceNodeGeyser(771)
    

    def EruptLoop(self):
        self.ExecuteUbergraph_BP_ResourceNodeGeyser(956)
    

    def ExecuteUbergraph_BP_ResourceNodeGeyser(self):
        goto(ComputedJump("EntryPoint"))
        self.GeyserEruption_02.Activate(True)
        if not self.mIsSignificant:
            goto('L199')
        # Label 66
        self.mEruptLoopOngoing = True
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(None, self, True)
        Default__KismetSystemLibrary.Delay(self, 15, LatentActionInfo(Linkage = 211, UUID = -978391255, ExecutionFunction = "ExecuteUbergraph_BP_ResourceNodeGeyser", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 199
        self.mEruptLoopOngoing = False
        goto(ExecutionFlow.Pop())
        ReturnValue2: bool = self.IsOccupied()
        if not ReturnValue2:
            goto('L250')
        goto(ExecutionFlow.Pop())
        # Label 250
        Default__KismetSystemLibrary.Delay(self, self.mAudioSyncTimer, LatentActionInfo(Linkage = 15, UUID = 1033054131, ExecutionFunction = "ExecuteUbergraph_BP_ResourceNodeGeyser", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue: bool = self.IsOccupied()
        ReturnValue2_0: bool = Not_PreBool(self.mIsSignificant)
        ReturnValue_0: bool = BooleanOR(ReturnValue, ReturnValue2_0)
        if not ReturnValue_0:
            goto('L66')
        self.mEruptLoopOngoing = False
        goto(ExecutionFlow.Pop())
        # Label 448
        self.Geyser_02.Deactivate()
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(None, self, True)
        goto(ExecutionFlow.Pop())
        # Label 530
        self.Geyser_02.Activate(True)
        self.EruptLoop()
        goto(ExecutionFlow.Pop())
        self.OnIsOccupiedChanged(newIsOccupied)
        if not self.mIsSignificant:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: bool = Not_PreBool(newIsOccupied)
        if not ReturnValue_2:
            goto('L448')
        goto('L530')
        self.GainedSignificance()
        self.mIsSignificant = True
        ReturnValue1_0: bool = self.IsOccupied()
        if not ReturnValue1_0:
            goto('L719')
        goto(ExecutionFlow.Pop())
        # Label 719
        self.EruptLoop()
        self.Geyser_02.Activate(True)
        goto(ExecutionFlow.Pop())
        self.LostSignificance()
        self.mIsSignificant = False
        self.Geyser_02.Deactivate()
        goto(ExecutionFlow.Pop())
        # Label 829
        ReturnValue_3: float = RandomFloatInRange(self.m_RandomStartDelayMin, self.m_RandomStartDelayMax)
        Default__KismetSystemLibrary.Delay(self, ReturnValue_3, LatentActionInfo(Linkage = 331, UUID = -492186008, ExecutionFunction = "ExecuteUbergraph_BP_ResourceNodeGeyser", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue1_1: bool = Not_PreBool(self.mEruptLoopOngoing)
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        goto('L829')
    
