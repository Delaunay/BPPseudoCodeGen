
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class IntroTutorialHubLvl3(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_7_2.Play_VO_ADA_TUTORIAL_7_2'}, 'Subtitle': 'NSLOCTEXT("", "50659206427417E2066A778C6483829D", "Congratulations! You have unlocked: Scanner Feature: Limestone. New buildings and recipes, which can be found in the build menu and craft bench respectively.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_8_0.Play_VO_ADA_TUTORIAL_8_0'}, 'Subtitle': 'NSLOCTEXT("", "D40427624C500CA9C0C66188532C4896", "Eighth Objective: Complete HUB Upgrade 4. Note: Use power poles to expand the power network for optimal results.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.07500000298023224
    mTitle = NSLOCTEXT("", "8194A0094E60DE8CE149FFB0D07B918D", "Onboarding: Complete HUB Upgrade 4")
    mSenderClass = NewObject[Sender_ADA]()
    mType = EMessageType::MT_TUTORIAL
    
