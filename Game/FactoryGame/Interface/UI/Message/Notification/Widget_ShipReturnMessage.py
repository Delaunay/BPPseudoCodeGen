
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Widget_ShipReturnMessage(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Milestones/Add_2019_03_19/Play_VO_ADA_FREIGHTER_RETURN_EDITED.Play_VO_ADA_FREIGHTER_RETURN_EDITED'}, 'Subtitle': 'NSLOCTEXT("", "A695FE9943C24043581ED09CA44F0C2F", "ADA: Milestone exchange concluded. FICSIT Freighter re-entry complete.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "B1B67CC9484366B087DAEBAE8F9B5F6B", "Freighter re-entry.")
    mPreviewText = NSLOCTEXT("", "3B9016CC46D4354C050C9DAD5F022135", "Preview Message")
    mSenderClass = NewObject[Sender_ADA]()
    
