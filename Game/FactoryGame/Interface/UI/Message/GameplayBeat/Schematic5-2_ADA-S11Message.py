
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic5-2_ADA-S11Message(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_5_2_0.Play_VO_ADA_MILESTONE_5_2_0'}, 'Subtitle': 'NSLOCTEXT("", "141A972249F4ACAD7A56D285C6D16616", "Milestone reached. The manufacturer increases production complexity, a critical look at production line logistics and efficiency is recommended during integration. ")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_5_2_1.Play_VO_ADA_MILESTONE_5_2_1'}, 'Subtitle': 'NSLOCTEXT("", "4144F067410A7E4F91D0FAA2F321FC15", "The truck allows for increased efficiency in transportation, automated or otherwise. New Project Parts enable progress to the next phase.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "B89A374F43D81C6D11C969BB500363C4", "Milestone 5-2: Industrial Manufacturing")
    mPreviewText = NSLOCTEXT("", "D59AA64A41A734419336FEA089D44E23", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
