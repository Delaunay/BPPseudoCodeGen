
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic4-2_ADA-S09Message(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_4_2_0.Play_VO_ADA_MILESTONE_4_2_0'}, 'Subtitle': 'NSLOCTEXT("", "0E3011A84FD2676138C22183A8A829CF", "Milestone reached. R&D inflated your pocket-dimension, added an additional hand-equipment slot, and have provided an improved xeno-zapper with increased strength and range.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "D07DC7874D9281581CDD70AA5D44A968", "Milestone 4-2: Improved Melee Combat")
    mPreviewText = NSLOCTEXT("", "9BD52CF342BE2DB80DA17B9D3FA680C1", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
