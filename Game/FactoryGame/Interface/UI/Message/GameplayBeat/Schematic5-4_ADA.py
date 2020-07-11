
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic5-4_ADA(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_5_4_0.Play_VO_ADA_MILESTONE_5_4_0'}, 'Subtitle': 'NSLOCTEXT("", "94EA32244B99A0DAC2D35FA321738DD8", "Milestone reached. Fluids can now be packaged to allow for transportation via vehicle and conveyor belts. Additionally, highly improved Biofuel can now be produced.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "44009C9441F538715E0B6EB73D62A192", "Milestone 5-4: Alternative Fluid Transportation")
    mPreviewText = NSLOCTEXT("", "9C07590F4F99F684A7073582481699F4", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
