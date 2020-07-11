
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_PickUp_Caterium(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Exploration/Caterium/Play_VO_ADA_PICKUP_Caterium.Play_VO_ADA_PICKUP_Caterium'}, 'Subtitle': 'NSLOCTEXT("", "4A6915B343E2D65D23B5D0BACC3F2C30", "New technologies can be developed based on this new, superconductive gold-like element, primarily in power and electronics. A new research tree can now be accessed in the MAM.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "2BFBDC7B417A17AB85E4C78849CCCD97", "Exploration: Caterium")
    mPreviewText = NSLOCTEXT("", "E2E51FF4413D71F9F15FBBB8AE18ECF6", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
