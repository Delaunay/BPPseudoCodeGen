
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic2-5_ADA(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_2_5_0.Play_VO_ADA_MILESTONE_2_5_0'}, 'Subtitle': 'NSLOCTEXT("", "795645D1484BC697E268579D810371B1", "Milestone reached. Improved versions of conveyor belts and conveyor lifts are now accessible. To encourage additional verticality conveyor poles now have a stackable variant.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "428CBC9A4E5C8B417DC992BD1F2E1586", "Milestone 2-5: Logistics Mk2")
    mPreviewText = NSLOCTEXT("", "68888E214067FF6C09DABDA482877C76", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
