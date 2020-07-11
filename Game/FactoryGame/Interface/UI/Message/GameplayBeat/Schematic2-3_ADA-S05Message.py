
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic2-3_ADA-S05Message(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_2_3_0.Play_VO_ADA_MILESTONE_2_3_0'}, 'Subtitle': 'NSLOCTEXT("", "12645BA44038A7953E6B22BE35A91CF6", "Milestone reached. Biofuel will ensure maximum efficiency of biomass burners. To aid in Biofuel production, you are now capable of removing foliage that consists primarily of wood. Additionally, R&D inflated your pocket-dimension.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "8D8FECE14BC6F56FDD77E385A24A4A77", "Milestone 2-3: Biofuel")
    mPreviewText = NSLOCTEXT("", "681DBD4C404A999123970E9F6124598E", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
