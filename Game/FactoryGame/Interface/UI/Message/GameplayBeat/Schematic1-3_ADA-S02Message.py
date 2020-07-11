
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic1-3_ADA-S02Message(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_1_3_0.Play_VO_ADA_MILESTONE_1_3_0'}, 'Subtitle': 'NSLOCTEXT("", "D87E454C43DEFB9B178092A557C9D060", "Milestone reached. The Molecular Analysis Machine, referred to as the MAM, will allow R&D to provide new technologies, items, and buildings based on samples collected in the field.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_1_3_1.Play_VO_ADA_MILESTONE_1_3_1'}, 'Subtitle': 'NSLOCTEXT("", "2A2C515F4DB079E87F1D039CE0839B47", "To ensure a greater chance of success during exploration, an upgraded toolbelt has been provided, as well as an Object Scanner and Beacons.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_1_3_2.Play_VO_ADA_MILESTONE_1_3_2'}, 'Subtitle': 'NSLOCTEXT("", "433216484674B8B46356E798384A2891", "Note: The Object Scanner requires calibration via the MAM to enable detection of specific objects.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "6077E4B94E331FA72AC93CB033C7FDBD", "Milestone 1-3: Field Research")
    mPreviewText = NSLOCTEXT("", "80C731914AD25206DD6B708D3085FC56", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
