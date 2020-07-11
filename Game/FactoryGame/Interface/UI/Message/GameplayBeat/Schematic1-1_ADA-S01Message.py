
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic1-1_ADA-S01Message(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_1_1_0.Play_VO_ADA_MILESTONE_1_1_0'}, 'Subtitle': 'NSLOCTEXT("", "1D04EFC4484FD1B4B496FF95A1424007", "Milestone reached. You have unlocked several structures, aimed to provide the first needed to build basic factory infrastructure and improved overview. Building these will provide a grid for more advanced organizing and sectioning of your factory.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "698CACBF4AF9681A3E0C46B6027EC30E", "Milestone 1-1: Base Building")
    mPreviewText = NSLOCTEXT("", "B08F063A49FEC4A80855F1BBFBA1098F", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
