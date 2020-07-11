
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Widget_Development(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/DebugTools/Play_DebugSound_OneShot.Play_DebugSound_OneShot'}, 'Subtitle': 'NSLOCTEXT("", "BE1275BF47B85A65E37966B7B2E9E5A1", "ADA: New Project Assembly phase: Construction Platform")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "A4A18E3E4870A9F861F5AFB69CC118EF", "Project Assembly: Construction Platform")
    mPreviewText = NSLOCTEXT("", "7A992E374CD60DAD4B6C53B488BBC415", "Preview Text")
    mSenderClass = NewObject[Sender_ADA]()
    
