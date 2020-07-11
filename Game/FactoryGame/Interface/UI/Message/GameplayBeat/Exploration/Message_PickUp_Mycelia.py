
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_PickUp_Mycelia(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Exploration/Mycelia/Play_VO_ADA_PICKUP_Mycelia.Play_VO_ADA_PICKUP_Mycelia'}, 'Subtitle': 'NSLOCTEXT("", "A9B9E4CA4AFF26AA0B3552AE347B943C", "The mycelia within this fungus suggest strong molecular bonding features frequently observed in adhesives and medicine, both beneficial for field research. A new research tree can now be accessed in the MAM. ")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "0C9A19664F0043A4A4CBF6B2C9C91009", "Exploration: Mycelia")
    mPreviewText = NSLOCTEXT("", "8F0EE08E4B2793F0FD34C2AECED683B4", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
