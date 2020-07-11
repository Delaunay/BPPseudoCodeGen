
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic7-4_ADA(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_7_4_0.Play_VO_ADA_MILESTONE_7_4_0'}, 'Subtitle': 'NSLOCTEXT("", "872DBA5D4C71C496DEFED0ACDDF4A298", "Milestone reached. With the provided buildings and parts you can now set up nuclear power generation, which balances an increase of fuel production complexity with improved power output. Uranium scanning unlocked.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_7_4_1.Play_VO_ADA_MILESTONE_7_4_1'}, 'Subtitle': 'NSLOCTEXT("", "0FAE6B8F49EB11ABE0C1DBA77CF25E6F", "Note: this method of power generation creates nuclear waste.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "FCBBF52A4BF9A09466FFFE99BE379F70", "Milestone 7-4: Nuclear Power")
    mPreviewText = NSLOCTEXT("", "1AA0617C4D021D4D93806AB82E2BDA29", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
