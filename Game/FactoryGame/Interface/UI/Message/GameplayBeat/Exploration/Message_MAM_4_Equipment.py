
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_MAM_4_Equipment(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/MAM/Play_VO_ADA_MAM_4_Equipment.Play_VO_ADA_MAM_4_Equipment'}, 'Subtitle': 'NSLOCTEXT("", "29DBAEB3458FA1940A035E889F3BF46E", "New Equipment unlocked.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "01D4DB184C4A4727CE9B77977D451B3C", "MAM: Equipment")
    mPreviewText = NSLOCTEXT("", "A9F7AE6B4DC52CAD13EEDE864199572B", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
