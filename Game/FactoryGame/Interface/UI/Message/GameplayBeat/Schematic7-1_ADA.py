
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic7-1_ADA(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_7_1_0.Play_VO_ADA_MILESTONE_7_1_0'}, 'Subtitle': 'NSLOCTEXT("", "58754E0B4838751FCC83878C61A59190", "Milestone reached. Quartz and Bauxite scanning unlocked. A new generation of basic aluminum parts is now available, which can be constructed from bauxite after a complex process of refinement. Additionally, improved conveyor belts and lifts can now be constructed.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "DEC945CC43967E36C9F304A164A8E8F3", "Milestone 7-1: Bauxite Refinement")
    mPreviewText = NSLOCTEXT("", "B48BC32948EB95596DAE888AB9F8466E", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
