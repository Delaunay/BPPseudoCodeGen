
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_MAM_1_Research(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/MAM/Play_VO_ADA_MAM_1_Research.Play_VO_ADA_MAM_1_Research'}, 'Subtitle': 'NSLOCTEXT("", "1065FEDA44E037716C5514ACAE6D86C5", "New research available in the MAM.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "8A6AECCB408CCF3B6BA63883B62323E6", "MAM: Research")
    mPreviewText = NSLOCTEXT("", "8BD8E6C24D8D357CA044A9B498C18951", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
