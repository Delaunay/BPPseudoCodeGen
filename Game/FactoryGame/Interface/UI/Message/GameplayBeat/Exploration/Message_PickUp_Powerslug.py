
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_PickUp_Powerslug(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Exploration/Powerslug/Play_VO_ADA_PICKUP_Powerslug.Play_VO_ADA_PICKUP_Powerslug'}, 'Subtitle': 'NSLOCTEXT("", "72E10D3C421AFFE9C39C1FA5F1CCF8E2", "This semi-slug seems to emit unfamiliar energy readings which could potentially be retrofitted into FICSIT technology. A new research tree can now be accessed in the MAM.  ")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "1C4B0CED4548730DDB4F8583D2303465", "Exploration: Powerslug")
    mPreviewText = NSLOCTEXT("", "E8A4B00C4CA987C94219D1A7365DE470", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
