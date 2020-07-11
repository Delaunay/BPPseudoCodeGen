
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_MAM_3_Building(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/MAM/Play_VO_ADA_MAM_3_Building.Play_VO_ADA_MAM_3_Building'}, 'Subtitle': 'NSLOCTEXT("", "B3254BA145255464AA56BAA695808A2F", "New Building unlocked.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "942C51F4479CCEAE3BCE8D93B5EA87F6", "MAM: Building")
    mPreviewText = NSLOCTEXT("", "E76FCFD74379B4764FDFC8A00F6307CB", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
