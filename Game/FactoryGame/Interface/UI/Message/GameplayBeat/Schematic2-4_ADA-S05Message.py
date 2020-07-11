
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Schematic2-4_ADA-S05Message(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Milestones/General/Play_VO_ADA_MILESTONE_2_4_0.Play_VO_ADA_MILESTONE_2_4_0'}, 'Subtitle': 'NSLOCTEXT("", "66A0C1074F67A57FD07181BE563C2C72", "Milestone reached. Several buildings aimed at factory traversal can now be accessed in the build menu. Caution is recommended during use of these products.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "21DC207E4674ECC69BADA7B9CD637A54", "Milestone 2-4: Jump Pads")
    mPreviewText = NSLOCTEXT("", "9ACF4A464D7CD786CDACD78D5E595F04", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
