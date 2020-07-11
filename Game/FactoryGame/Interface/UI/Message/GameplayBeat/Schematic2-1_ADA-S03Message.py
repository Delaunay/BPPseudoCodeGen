
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic2-1_ADA-S03Message(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_2_1_0.Play_VO_ADA_MILESTONE_2_1_0'}, 'Subtitle': 'NSLOCTEXT("", "6421120645FB232D2A4339A774CFBA0E", "Milestone Reached. You have been given Early Access to the Anti-Waste Effort for Stress-testing of Materials on Exoplanets Bonus Program. ")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_2_1_1.Play_VO_ADA_MILESTONE_2_1_1'}, 'Subtitle': 'NSLOCTEXT("", "12ECE46C425D6BC7CD87EC901C26112D", "Funneling parts into the AWESOME Resource Sink, depending on their amount and complexity, will grant you Coupons in the AWESOME store, which can be exchanged for bonus rewards.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_2_1_2.Play_VO_ADA_MILESTONE_2_1_2'}, 'Subtitle': 'NSLOCTEXT("", "1AC143BE487E61672B9DFDA62D19BE29", "Examples of bonus content are: parts, walls, factory attachments, and cosmetics. FICSIT is working hard to develop additional options which will be added to the AWESOME store in the future.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_2_1_3.Play_VO_ADA_MILESTONE_2_1_3'}, 'Subtitle': 'NSLOCTEXT("", "648A357345D42B7B91B08C94603AF437", "Go that extra kilometer, go AWESOME.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "EEFFA2C346F696CA9583F5A9B3DB63C7", "Milestone 2-1: Resource Sink Bonus Program")
    mPreviewText = NSLOCTEXT("", "31FED48C45DDBBC22D3E1C9E592B70B8", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
