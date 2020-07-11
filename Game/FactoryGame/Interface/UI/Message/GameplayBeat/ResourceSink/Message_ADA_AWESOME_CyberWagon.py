
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_ADA_AWESOME_CyberWagon(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/AwesomeBonus/Play_VO_ADA_AWESOME_CyberWagon.Play_VO_ADA_AWESOME_CyberWagon'}, 'Subtitle': 'NSLOCTEXT("", "4001204C4B6A1FFE5638AD87E63063AC", "FICSIT Inc. does not waste. As a reward for your ‘creative input’ I have been given permission to grant you a gift. You can find it in the AWESOME store. I hope you like it. It was my first solo project.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "317B868C4F0C01B349362EA3BA6BDA47", "Nuclear Waste")
    mPreviewText = NSLOCTEXT("", "577B485E4359BB8792C8E6AE75C547F2", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
