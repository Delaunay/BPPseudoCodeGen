
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic5-3_ADA-S12Message(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_5_3_0.Play_VO_ADA_MILESTONE_5_3_0'}, 'Subtitle': 'NSLOCTEXT("", "2C804801434D5E0EE7C87D8DD2A143A2", "Milestone reached. Gasmasks and filter parts will ensure increased odds of survival in gas-based hazardous environments. FICSIT Inc. would like to extend the friendly advice to not forget to change filters regularly.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "486CF29746395FE71AF3B1B01D66725F", "Milestone 5-3: Gas Mask")
    mPreviewText = NSLOCTEXT("", "7D75BE414E9FE4044FD9AB9268CFB643", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
