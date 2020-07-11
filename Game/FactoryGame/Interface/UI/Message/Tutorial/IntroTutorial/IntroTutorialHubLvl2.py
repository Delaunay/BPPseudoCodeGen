
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class IntroTutorialHubLvl2(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_6_1.Play_VO_ADA_TUTORIAL_6_1'}, 'Subtitle': 'NSLOCTEXT("", "4F88DD5545B175AEFD4F428F8740E74C", "Congratulations! You have unlocked: HUB Feature: Biomass Burner. Scanner Feature: Copper. New buildings and recipes, which can be found in the build menu and craft bench respectively.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_7_0.Play_VO_ADA_TUTORIAL_7_0'}, 'Subtitle': 'NSLOCTEXT("", "F0356ECE4E546B3824766E8BF4728C24", "Seventh Objective: Complete HUB Upgrade 3 Note: Connect buildings to a Biomass Burner for power. Note: Buildings such as the smelter require a Recipe to be set.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_7_1.Play_VO_ADA_TUTORIAL_7_1'}, 'Subtitle': 'NSLOCTEXT("", "BA0B2B6B42590A4ADBB95287BCE12258", "Advice: Automate the smelting process and use portable miners for optimal results. ")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.07500000298023224
    mTitle = NSLOCTEXT("", "8C2E1E8F4260D3FD15377BB6EFB3BAE4", "Onboarding: Complete HUB Upgrade 3")
    mSenderClass = NewObject[Sender_ADA]()
    mType = EMessageType::MT_TUTORIAL
    
