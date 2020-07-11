
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class IntroTutorial_IronOre(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_3_0.Play_VO_ADA_TUTORIAL_3_0'}, 'Subtitle': 'NSLOCTEXT("", "AE1116CF4D6354D35D3799913B6D548E", "Third Objective: Please familiarize yourself with the Resource Scanner to find Iron.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_3_1.Play_VO_ADA_TUTORIAL_3_1'}, 'Subtitle': 'NSLOCTEXT("", "2825920B4876ACB05F2BABB2D79E5FE7", "Note: The acquisition of Iron is considered essential in preparation for all future objectives.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "C222F0AE412B0C84B36D3FAC12A4D3B8", "Onboarding: Find iron ore")
    mSenderClass = NewObject[Sender_ADA]()
    mType = EMessageType::MT_TUTORIAL
    
