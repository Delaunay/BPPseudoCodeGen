
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_PickUp_Nutrients(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Exploration/Nutrients/Play_VO_ADA_PICKUP_Nutrients.Play_VO_ADA_PICKUP_Nutrients'}, 'Subtitle': 'NSLOCTEXT("", "DA88956A4A4229A79850429DBDA3D40E", "This is one of multiple edibles we have detected in your vicinity which are within approved nutritional and medical categories as established by R&D. A new research tree can now be accessed in the MAM.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "BBF7404D4BAC5DEF012F10AAAAAB7BBB", "Exploration: Nutrients")
    mPreviewText = NSLOCTEXT("", "AB9121B043EE585FC0226C952628014F", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
