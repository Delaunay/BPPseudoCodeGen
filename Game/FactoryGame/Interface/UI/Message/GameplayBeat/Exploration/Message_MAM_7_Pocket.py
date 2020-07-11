
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_MAM_7_Pocket(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/MAM/Play_VO_ADA_MAM_7_Pocket.Play_VO_ADA_MAM_7_Pocket'}, 'Subtitle': 'NSLOCTEXT("", "7D75C9CF4439B120BDF91E8F4991F3BB", "Pocket-dimension has been inflated.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "0911E4934A2553FFF69B66B3422C31AB", "MAM: Pocket")
    mPreviewText = NSLOCTEXT("", "156DD6914352FE6FA9B05B94640A79D8", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
