
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_PickUp_Quartz(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Exploration/Quartz/Play_VO_ADA_PICKUP_Quartz.Play_VO_ADA_PICKUP_Quartz'}, 'Subtitle': 'NSLOCTEXT("", "3162D66147CE3713800462ADA957237B", "This mineral shows purity levels akin to synthetic quartz manufactured on earth, and can be used to improve communication and exploration technologies. A new research tree can now be accessed in the MAM.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "13B5A8F04812184206DE119A23D7ADAA", "Exploration: Quartz")
    mPreviewText = NSLOCTEXT("", "AD8D27CA4A00E7E7F9A7B9AEA6F233F4", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
