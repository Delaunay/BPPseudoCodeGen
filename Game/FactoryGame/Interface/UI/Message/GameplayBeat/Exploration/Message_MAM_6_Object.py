
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_MAM_6_Object(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/MAM/Play_VO_ADA_MAM_6_Object.Play_VO_ADA_MAM_6_Object'}, 'Subtitle': 'NSLOCTEXT("", "0EAB60A34C4796A585A93CA807A94456", "New Object added to the Object Scanner.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "F09EF498483B9841A97A87854B7DD082", "MAM: Object")
    mPreviewText = NSLOCTEXT("", "BC6A23864E9276EBED92E681A0C67D3F", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
