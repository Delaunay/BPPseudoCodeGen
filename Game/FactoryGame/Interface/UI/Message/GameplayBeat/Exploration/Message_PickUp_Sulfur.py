
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_PickUp_Sulfur(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Exploration/Sulfur/Play_VO_ADA_PICKUP_Sulfur.Play_VO_ADA_PICKUP_Sulfur'}, 'Subtitle': 'NSLOCTEXT("", "ABA8DD32480DF59B911304B1DDBE6FA4", "Data shows this is a mix of sulfide and sulfate minerals. It could be an indication of recent volcanic activity. A new research tree exploring volatile self-defense applications can now be accessed in the MAM.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "DAE93DAD41F4B779FC3794B1F2B7AFB6", "Exploration: Sulfur")
    mPreviewText = NSLOCTEXT("", "B20706EC437B93DB327F989AA1D9D1B0", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
