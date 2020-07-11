
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic4-1_ADA-S08Message(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_4_1_0.Play_VO_ADA_MILESTONE_4_1_0'}, 'Subtitle': 'NSLOCTEXT("", "76C93AC8429DEB275B48FE9DB824810C", "Milestone reached. Improved miner included to double extraction rates and improve efficiency of new pipelines. A collection of new, more complex parts is now available for crafting. ")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_4_1_1.Play_VO_ADA_MILESTONE_4_1_1'}, 'Subtitle': 'NSLOCTEXT("", "7EF804624667CD069A5ADFA293FE30C1", "An additional Project Part can now be constructed, further progress to the next Phase is now possible.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "4D1ABF05438B4E8467C1A2ADB72F340F", "Milestone 4-1: Advanced Steel Production")
    mPreviewText = NSLOCTEXT("", "EB7C5880486643BAD3166F8BE16EC4F0", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
