
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class IntroTutorialHub(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_4_0.Play_VO_ADA_TUTORIAL_4_0'}, 'Subtitle': 'NSLOCTEXT("", "3F49E759458903E639023FB5FB2F561A", "Fourth Objective: Build the HUB.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_4_1.Play_VO_ADA_TUTORIAL_4_1'}, 'Subtitle': 'NSLOCTEXT("", "50CD523B4BDE0EFBEC783FA38C7BD5DC", "Note: To complete this objective the resources salvaged from the drop pod will be consumed.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_4_2.Play_VO_ADA_TUTORIAL_4_2'}, 'Subtitle': 'NSLOCTEXT("", "898E66F741F9453767D9BC95CB6E02CE", "Caution: Ensure the HUB is built on spacious, open terrain, close to the presence of iron sources. Failure to do so will likely result in non-optimal progress.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.07000000029802322
    mTitle = NSLOCTEXT("", "25D1E17D4CBC6578C86C869A1BE18638", "Onboarding: Build the HUB framework")
    mSenderClass = NewObject[Sender_ADA]()
    mType = EMessageType::MT_TUTORIAL
    
