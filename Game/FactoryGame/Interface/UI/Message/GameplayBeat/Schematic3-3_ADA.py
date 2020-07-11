
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic3-3_ADA(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_3_3_0.Play_VO_ADA_MILESTONE_3_3_0'}, 'Subtitle': 'NSLOCTEXT("", "171C3F774171FD285020D38DE754B714", "Milestone reached. Steel production unlocked. Foundry grants access to new, simple steel parts. An additional Project Part can now be constructed, progress to the next Phase is now possible.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "4245F03D446571D0E967AA8CECD52037", "Milestone 3-3: Basic Steel Production")
    mPreviewText = NSLOCTEXT("", "63A1C8074668F8A15490BBB4F59698F9", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
