
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic4-4_ADA(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_4_4_0.Play_VO_ADA_MILESTONE_4_4_0'}, 'Subtitle': 'NSLOCTEXT("", "3DF0C053446AE0E58C9F31AE9B53684B", "Milestone reached. FICSIT Inc. has processed and incorporated frequent pioneer requests for pipe-based personal transport.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_4_4_1.Play_VO_ADA_MILESTONE_4_4_1'}, 'Subtitle': 'NSLOCTEXT("", "1E273AF447098738B79708ADC651F639", "Introducing: Hypertubes. Safe, aesthetic, adaptable, fun. Enjoy a view of your hard work as you soar through incredibly tight turns. Build them today.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_4_4_2.Play_VO_ADA_MILESTONE_4_4_2'}, 'Subtitle': 'NSLOCTEXT("", "E62A718D4D29CB82B4C1878098495F2E", "Note: FICSIT Inc. is not responsible for any harm caused by irresponsible use of this product.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "02F4B36C4BF31862C1DD79B8B06B03A2", "Milestone 4-4: Hypertubes")
    mPreviewText = NSLOCTEXT("", "28A692AC4045FABAF3C6D7A9B1D1A511", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
