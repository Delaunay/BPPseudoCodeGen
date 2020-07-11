
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic4-3_ADA(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_4_3_0.Play_VO_ADA_MILESTONE_4_3_0'}, 'Subtitle': 'NSLOCTEXT("", "592494914569984EE90E4181FAFAACFE", "Milestone reached. Logistics can be improved with a larger storage container and enhanced conveyor belt efficiency.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "A58E6F7B4061F0AEEA7BE39BCE24E373", "Milestone 4-3: Logistics Mk. 3")
    mPreviewText = NSLOCTEXT("", "965664674A5130B283516080AFBE037B", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
