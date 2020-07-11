
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_MAM_8_Toolbelt(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/MAM/Play_0VO_ADA_MAM_8_Toolbelt.Play_0VO_ADA_MAM_8_Toolbelt'}, 'Subtitle': 'NSLOCTEXT("", "5CEEB36F433ECB578D93839A38B3E20B", "Toolbelt has been expanded.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "46B1CE0C4AA4EAF6F42219A11287FE05", "MAM: Toolbelt")
    mPreviewText = NSLOCTEXT("", "75D2A6FC450244C194B803801591AF01", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
