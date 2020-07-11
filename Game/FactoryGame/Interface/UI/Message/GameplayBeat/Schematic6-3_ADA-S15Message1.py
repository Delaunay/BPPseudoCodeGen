
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic6-3_ADA-S15Message1(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_6_3_0.Play_VO_ADA_MILESTONE_6_3_0'}, 'Subtitle': 'NSLOCTEXT("", "A283CD0345B159DFE17F79A00067D289", "Milestone reached. A new set of buildings and vehicles needed for long-range transportation has been made available. ")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_6_3_1.Play_VO_ADA_MILESTONE_6_3_1'}, 'Subtitle': 'NSLOCTEXT("", "BB863F164BCAB0500A469B962D765322", "In addition to built-in power conduction, rails-based transit ensures increased efficiency and reliability for both the transport of pioneers and cargo. ")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "9D2494E9442CDBF101F5FCBD0B8666A0", "Milestone 6-3: Monorail-Train Technology")
    mPreviewText = NSLOCTEXT("", "080872AE4228E14569B986837E7C3927", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
