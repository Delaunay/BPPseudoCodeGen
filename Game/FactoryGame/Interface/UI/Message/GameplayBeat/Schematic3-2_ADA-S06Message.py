
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic3-2_ADA-S06Message(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_3_2_0.Play_VO_ADA_MILESTONE_3_2_0'}, 'Subtitle': 'NSLOCTEXT("", "EDC192364969DD9E44A8FC9D2F602185", "Milestone reached. Long-range transportation, as well as the construction of outposts, is now encouraged. Vehicle stations have built-in functionality to refuel, and re-stock or collect parts.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "BC7C0A284E253D7AA9ABB49F6E8AD0B8", "Milestone 3-2: Vehicular Transport")
    mPreviewText = NSLOCTEXT("", "670D714D48BC8F04CAE9AEA5BE9450AE", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
