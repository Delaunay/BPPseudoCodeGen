
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Widget_Retention(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/DebugTools/Play_DebugSound_OneShot.Play_DebugSound_OneShot'}, 'Subtitle': 'NSLOCTEXT("", "7D9D9A7A4E09B5ABD8ABE997C9388FBE", "ADA: New Project Assembly phase: Systems")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "20ACA724432B25E2B64C80954A1BFD7D", "Project Assembly: Systems")
    mPreviewText = NSLOCTEXT("", "BD255D93440079F8CA4AC1AC38D018F4", "Preview text")
    mSenderClass = NewObject[Sender_ADA]()
    
