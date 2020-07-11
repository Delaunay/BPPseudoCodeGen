
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_MAM_9_Map(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/MAM/Play_VO_ADA_MAM_9_Map.Play_VO_ADA_MAM_9_Map'}, 'Subtitle': 'NSLOCTEXT("", "6856189F46EB9F7B79F0A4AAF7A680CA", "The Map has been unlocked.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "1CF80557489A38C32030BF9DEE5FE0EC", "MAM: Map")
    mPreviewText = NSLOCTEXT("", "391779854DE5587F3EFDA19CB01BEE6D", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
