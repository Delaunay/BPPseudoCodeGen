
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic2-2_ADA-S04Message(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_2_2_0.Play_VO_ADA_MILESTONE_2_2_0'}, 'Subtitle': 'NSLOCTEXT("", "6FAD125647B9D3BDEB9AF8B40DA617EE", "Milestone reached. More complex assembly of parts can now be automated. Project Assembly Parts can now be constructed and sent up via the Space Elevator.Note: Project Parts are too complex to produce by hand.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "2A326CB24AF9C4004F71948DE3EC88FB", "Milestone 2-2: Part Assembly")
    mPreviewText = NSLOCTEXT("", "F053FA1D4F3AF4F2F2FB95B398D399FF", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
