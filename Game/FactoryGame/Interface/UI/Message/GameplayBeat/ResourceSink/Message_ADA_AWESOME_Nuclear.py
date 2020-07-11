
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_ADA_AWESOME_Nuclear(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/AwesomeBonus/Play_VO_ADA_AWESOME_NuclearWaste.Play_VO_ADA_AWESOME_NuclearWaste'}, 'Subtitle': 'NSLOCTEXT("", "43F6B42A4202804E390693912C4E9013", "Radioactive items are not allowed in the AWESOME Resource Sink. R&D kindly requests that you stop contaminating their results. R&D would like to remind you they control any future technologies provided to you.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "35EE494D4E3E42EFCB4D5EA9B5B449E2", "Nuclear Waste")
    mPreviewText = NSLOCTEXT("", "1D9B7F2242B1EFE7CF4270B974ED6D5E", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
