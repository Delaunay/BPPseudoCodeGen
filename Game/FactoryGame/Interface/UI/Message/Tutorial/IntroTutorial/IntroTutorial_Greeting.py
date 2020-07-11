
from codegen.ue4_stub import *

from Script.UMG import GetOwningPlayerPawn
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.FactoryGame import FGTutorialIntroManager
from Game.FactoryGame.Interface.UI.Message.Tutorial.IntroTutorial.IntroTutorial_Greeting import ExecuteUbergraph_IntroTutorial_Greeting
from Script.Engine import Pawn
from Script.FactoryGame import Default__FGTutorialIntroManager
from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Destruct
from Script.FactoryGame import UpdateTutorial
from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage
from Script.Engine import HasAuthority

class IntroTutorial_Greeting(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_0_0.Play_VO_ADA_TUTORIAL_0_0'}, 'Subtitle': 'NSLOCTEXT("", "C2145E4341399D8476054FB5DBE204E3", "Welcome to planet MASSAGE-2(AB) b, your designated sector in the binary star-system of Akycha.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_0_1.Play_VO_ADA_TUTORIAL_0_1'}, 'Subtitle': 'NSLOCTEXT("", "294D33D846B1934E480E758B49390E9D", "I am ADA, also known as Artificial Directory and Assistant, tasked to support pioneers, such as you, in their mission. You are the third of your sector to survive planetfall. Congratulations.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_0_4.Play_VO_ADA_TUTORIAL_0_4'}, 'Subtitle': 'NSLOCTEXT("", "EEA3488943673CE203C0D883CA440F0C", "Note: Objective-based introduction initialized. Welcome to: Onboarding.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.07500000298023224
    mTitle = NSLOCTEXT("", "7871A2BB4931C39430BB2D84AD6F5980", "Onboarding: Welcome")
    mSenderClass = NewObject[Sender_ADA]()
    mType = EMessageType::MT_TUTORIAL
    
    def Destruct(self):
        self.ExecuteUbergraph_IntroTutorial_Greeting(10)
    

    def ExecuteUbergraph_IntroTutorial_Greeting(self):
        self.Destruct()
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_0: bool = ReturnValue.HasAuthority()
        if not ReturnValue_0:
            goto('L205')
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[FGTutorialIntroManager] = Default__FGTutorialIntroManager.Get(ReturnValue_1)
        ReturnValue_2.UpdateTutorial(2)
    
