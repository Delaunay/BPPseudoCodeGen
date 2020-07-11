
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic6-2_ADA-S14Message(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_6_2_0.Play_VO_ADA_MILESTONE_6_2_0'}, 'Subtitle': 'NSLOCTEXT("", "0F698F614DD067E96E3A61870C3B60BA", "R&D inflated your pocket-dimension and has provided a Jetpack, which operates on oil-based fuel, for increased navigational capabilities as well as odds of survival.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "9ED3254F4AF1E76C40A1A4B273CE0C2C", "Milestone 6-2: Jetpack")
    mPreviewText = NSLOCTEXT("", "FDFD127143074370E33BCB801F779865", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
