
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class IntroTutorial_DismantleDropPod(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_1_0.Play_VO_ADA_TUTORIAL_1_0'}, 'Subtitle': 'NSLOCTEXT("", "D038DD4C438A217B40B0F18B98799080", "First objective: Please dismantle the drop-pod. The resulting materials will be repurposed to construct a Habitat and Utility Base, from now on referred to as: the HUB.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_1_1.Play_VO_ADA_TUTORIAL_1_1'}, 'Subtitle': 'NSLOCTEXT("", "8EECC6AC43FC82899ACD7D981AF6A9E2", "Note: FICSIT Incorporated is cost-effective and efficient. We do not waste.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.07000000029802322
    mTitle = NSLOCTEXT("", "A1A104A147AEB119090523A488871142", "Onboarding: Dismantle drop pod")
    mSenderClass = NewObject[Sender_ADA]()
    mType = EMessageType::MT_TUTORIAL
    
