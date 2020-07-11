
from codegen.ue4_stub import *

from Script.UMG import GetOwningPlayerPawn
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.Engine import Default__GameplayStatics
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Interface.UI.Message.Tutorial.IntroTutorial.IntroTutorial_Complete import ExecuteUbergraph_IntroTutorial_Complete
from Script.FactoryGame import CompleteTutorial
from Script.FactoryGame import FGTutorialIntroManager
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import SetTutorialMode
from Script.Engine import Pawn
from Script.Engine import GetAllActorsOfClass
from Script.FactoryGame import Default__FGTutorialIntroManager
from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Destruct
from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage
from Script.Engine import HasAuthority

class IntroTutorial_Complete(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_10_1.Play_VO_ADA_TUTORIAL_10_1'}, 'Subtitle': 'NSLOCTEXT("", "952224574E67630E9FBCD59E5F2CDBC4", "Congratulations! You have unlocked: Building: Space Elevator. Building: Biomass Burner. Part: Biomass.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/End/Play_VO_ADA_TUTORIAL_END_0.Play_VO_ADA_TUTORIAL_END_0'}, 'Subtitle': 'NSLOCTEXT("", "A771E24E4650B6353AF727B001FEA052", "Motivational message: Congratulations, you succeeded in every provided task. On behalf of FICSIT Incorporated I thank you for your current, and future, service. ")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/End/Play_VO_ADA_TUTORIAL_END_1.Play_VO_ADA_TUTORIAL_END_1'}, 'Subtitle': 'NSLOCTEXT("", "CA86D6804013A55D09B7A9A6DD16E5A2", "Additional knowledge: The HUB terminal has been converted to give access to Milestones, there to ensure you progress along FICSIT-approved protocols. ")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/End/Play_VO_ADA_TUTORIAL_END_2.Play_VO_ADA_TUTORIAL_END_2'}, 'Subtitle': 'NSLOCTEXT("", "F9CD51A148744E8CAF46E094DB366F71", "Note: Future developments should be aimed at constructing the Space Elevator and, as such, initiating Project Assembly.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.07500000298023224
    mTitle = NSLOCTEXT("", "ED847D0746273DFE18A3BAB92076AC4A", "Onboarding: Congratulations")
    mSenderClass = NewObject[Sender_ADA]()
    mType = EMessageType::MT_TUTORIAL
    
    def Destruct(self):
        self.ExecuteUbergraph_IntroTutorial_Complete(429)
    

    def ExecuteUbergraph_IntroTutorial_Complete(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        OutActors: List[Ptr[FGPlayerController]] = []
        
        Default__GameplayStatics.GetAllActorsOfClass(self, FGPlayerController, Ref[OutActors])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 123
        ReturnValue: int32 = len(OutActors)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L355")
        
        Item = None
        Item = OutActors[Variable_0]
        Item.SetTutorialMode(False)
        goto(ExecutionFlow.Pop())
        # Label 355
        ReturnValue_1: int32 = Variable + 1
        Variable = ReturnValue_1
        goto('L123')
        self.Destruct()
        ReturnValue_2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_3: bool = ReturnValue_2.HasAuthority()
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: Ptr[FGTutorialIntroManager] = Default__FGTutorialIntroManager.Get(ReturnValue_4)
        ReturnValue_5.CompleteTutorial()
        goto('L15')
    
