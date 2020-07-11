
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_PickUp_Harddrive(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Exploration/Harddrive/Play_VO_ADA_PICKUP_Harddrive.Play_VO_ADA_PICKUP_Harddrive'}, 'Subtitle': 'NSLOCTEXT("", "0B23D8E14EA478FB541E128B6C394D6D", "Data on the harddrive has been salvaged, and can be repurposed to unlock an alternate recipe. Salvaging more harddrives will provide additional alternate recipes.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "0D08A3B540E11E7665DDE8857416086E", "Exploration: Harddrive")
    mPreviewText = NSLOCTEXT("", "055DF9574C100C8A70BF81BF30E9AD32", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
