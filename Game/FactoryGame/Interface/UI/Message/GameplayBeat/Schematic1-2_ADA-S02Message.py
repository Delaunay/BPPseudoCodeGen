
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic1-2_ADA-S02Message(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_1_2_0.Play_VO_ADA_MILESTONE_1_2_0'}, 'Subtitle': 'NSLOCTEXT("", "508CA1A74A6DBD604B400D8047CD082B", "Milestone reached. Conveyor belts can now merge, split, and lift to increase the complexity and efficiency of your factory. We encourage you to consider more verticality when it comes to factory logistics to streamline short-range transportation.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_1_2_1.Play_VO_ADA_MILESTONE_1_2_1'}, 'Subtitle': 'NSLOCTEXT("", "6D2A5B3340FAFC66F6756D90754117EE", "The productivity display will help you measure and improve the productivity of individual buildings to aid with optimization.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "984E586847318B47D9F96890A7940377", "Milestone 1-2: Logistics")
    mPreviewText = NSLOCTEXT("", "AD57B1284BBFE0109E0C96908AEE8CDC", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
