
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_MAM_5_Resource(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/MAM/Play_VO_ADA_MAM_5_Resource.Play_VO_ADA_MAM_5_Resource'}, 'Subtitle': 'NSLOCTEXT("", "40B01ADC474AF792BCBE09B7E4505D45", "New Resource added to the Resource Scanner")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "163B613B4B7D41412D0938AC37C012FD", "MAM: Resource")
    mPreviewText = NSLOCTEXT("", "84433C3F4ABD7FB04EE3B390F9C5225F", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
