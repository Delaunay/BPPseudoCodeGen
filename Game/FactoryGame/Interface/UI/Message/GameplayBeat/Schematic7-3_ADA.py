
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic7-3_ADA(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_7_3_0.Play_VO_ADA_MILESTONE_7_3_0'}, 'Subtitle': 'NSLOCTEXT("", "D1ADB1934D5A24C29B7ED78E3505B542", "Milestone reached. With the new Hazmat suit and Iodine Infused Filters you will be protected against Uranium-based radiation.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "AE682B3746C87F57A2F2EBB9E2419BB9", "Milestone 7-3: Hazmat Suit")
    mPreviewText = NSLOCTEXT("", "925A5A3B440C6565256CAC85A2D51C1C", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
