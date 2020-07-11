
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_MAM_2_Recipe(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/MAM/Play_VO_ADA_MAM_2_Recipe.Play_VO_ADA_MAM_2_Recipe'}, 'Subtitle': 'NSLOCTEXT("", "A691B24244DF5718394DE99655EA66A5", "New Recipe unlocked.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "CF0F92F7461FA61E9D9D4785F455B56E", "MAM: Recipe")
    mPreviewText = NSLOCTEXT("", "EC85EE5E480D8CDD834B5E8449215592", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
