
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_MAM_10_Overclock(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/DebugTools/Play_Debug_1SecSilence.Play_Debug_1SecSilence'}, 'Subtitle': 'NSLOCTEXT("", "5A2EE6824B8A81DAEBF4C18EF271027E", "Buildings can now be Overclocked with the use of Power Shards.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "F6C6C3334E618827A8C44E95373B4D38", "MAM: Overclocking")
    mPreviewText = NSLOCTEXT("", "F097E440478DBFC51027B6A01A6E718B", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
