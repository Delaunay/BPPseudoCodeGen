
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic5-1_ADA-S10Message(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_5_1_0.Play_VO_ADA_MILESTONE_5_1_0'}, 'Subtitle': 'NSLOCTEXT("", "6BEF755D450F32959F791DB33632B897", "Milestone reached. Oil acquisition and refining unlocked. Oil-based products can now be made. By-products of oil-refinement can be used after further processing, as seen in the refinery.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_5_1_1.Play_VO_ADA_MILESTONE_5_1_1'}, 'Subtitle': 'NSLOCTEXT("", "594A324C430E1853DC519289D64A05F3", "Caution: this is a reminder to minimize the chance of expiration during out-of-base activities.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "EF693CA54738262F98B39BAF51EB57FD", "Milestone 5-1: Oil Processing")
    mPreviewText = NSLOCTEXT("", "8F9276E8451417F50DF35D9439FA6752", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
