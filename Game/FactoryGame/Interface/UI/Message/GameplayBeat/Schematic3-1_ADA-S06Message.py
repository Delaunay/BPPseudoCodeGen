
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic3-1_ADA-S06Message(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_3_1_0.Play_VO_ADA_MILESTONE_3_1_0'}, 'Subtitle': 'NSLOCTEXT("", "FFFD667242B4DE4E47EA1FA95BA6E69F", "Milestone reached. Coal is an improved alternative power source to biomass and can be fully automated, if provided water with the new pipeline buildings, and power throughout the initial set-up. Coal has been added to the resource scanner.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_3_1_1.Play_VO_ADA_MILESTONE_3_1_1'}, 'Subtitle': 'NSLOCTEXT("", "FAC4115A4E399FFB96F2DD9A94122711", "Note: Ensure the close proximity of water to the coal production line. Note: Pumps will aid in vertical transport of fluids through pipes. Note: Throughput and volume indicators are added to each pipe-section automatically.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "25A4BE4F43F559F28D1E76B3F032793B", "Milestone 3-1: Coal Power")
    mPreviewText = NSLOCTEXT("", "05DD8B73410A1137A96462AD7E05DC62", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
