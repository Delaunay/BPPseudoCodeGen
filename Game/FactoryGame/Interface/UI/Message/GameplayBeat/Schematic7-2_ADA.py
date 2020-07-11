
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic7-2_ADA(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_7_2_0.Play_VO_ADA_MILESTONE_7_2_0'}, 'Subtitle': 'NSLOCTEXT("", "16F9A5A6443AA23E585A9F9CA8471FCF", "Milestone reached. Advanced aluminum parts can now be produced, which are necessary to build the Miner Mk3. Batteries can be used as a fuel source for vehicles.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "532BEDD54ABDB617483AE7BCA98686A3", "Milestone 7-2: Advanced Aluminum Production")
    mPreviewText = NSLOCTEXT("", "A1038EAB44B64011309A279B5EC4339C", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
