
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class IntroTutorialHubLvl4(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_8_1.Play_VO_ADA_TUTORIAL_8_1'}, 'Subtitle': 'NSLOCTEXT("", "DDF90E66447DDB71E4934AAA7925EB37", "Congratulations! You have unlocked: Building: Conveyor belts and poles. Inventory: Additional slots.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_9_0.Play_VO_ADA_TUTORIAL_9_0'}, 'Subtitle': 'NSLOCTEXT("", "0E0B289049E65E658175519487D05AFA", "Ninth Objective: Complete HUB Upgrade 5. Note: Portable Miners cannot be connected to conveyor belts. Advice: when planning the construction of buildings, note the placement of conveyor belts.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.07500000298023224
    mTitle = NSLOCTEXT("", "EACC997F4F45068E064744932F0554DA", "Onboarding: Complete HUB Upgrade 5")
    mSenderClass = NewObject[Sender_ADA]()
    mType = EMessageType::MT_TUTORIAL
    
