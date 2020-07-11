
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Widget_Expansion(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/DebugTools/Play_DebugSound_OneShot.Play_DebugSound_OneShot'}, 'Subtitle': 'NSLOCTEXT("", "FBB80C50450615F43E2BC8BDAC6A1C15", "ADA: New Project Assembly phase: Framework")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "BAC03BB94677CEF64B19108F66304EB9", "Project Assembly: Framework")
    mPreviewText = NSLOCTEXT("", "D9E9A69F4108A158934C5FA7C91447A3", "Preview text")
    mSenderClass = NewObject[Sender_ADA]()
    
