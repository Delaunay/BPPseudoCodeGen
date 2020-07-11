
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic6-1_ADA-S13Message(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_6_1_0.Play_VO_ADA_MILESTONE_6_1_0'}, 'Subtitle': 'NSLOCTEXT("", "1919F9554083FB0254C74E905918267A", "Milestone reached. The fuel generator will match power generation to the increased consumption of recently acquired technologies and buildings. Additionally, improved conveyor belts and lifts can now be constructed. Caterium scanning unlocked.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "F2D3A76944E71EEF4D21BB80AC14B4A8", "Milestone 6-1: Expanded Power Infrastructure")
    mPreviewText = NSLOCTEXT("", "9542ED1140938FD5C45689AF40A6B8B0", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
