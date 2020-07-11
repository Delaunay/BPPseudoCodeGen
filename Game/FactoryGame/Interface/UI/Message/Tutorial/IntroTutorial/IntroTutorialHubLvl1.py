
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class IntroTutorialHubLvl1(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_4_3.Play_VO_ADA_TUTORIAL_4_3'}, 'Subtitle': 'NSLOCTEXT("", "B27FDF0E44CD8F26B01A87B617D48B19", "Congratulations! You have unlocked: HUB Feature: Manual Craft Bench. HUB Feature: HUB Terminal.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_5_0.Play_VO_ADA_TUTORIAL_5_0'}, 'Subtitle': 'NSLOCTEXT("", "4D4AECDA4CBC1FFDC0469BA45F6FF838", "Fifth Objective: Complete HUB Upgrade 1. Note: The Craft Bench and HUB Terminal are essential for progression to the next objective. ")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.07500000298023224
    mTitle = NSLOCTEXT("", "05E9735548A6CD593841EFA28D551A40", "Onboarding: Complete HUB Upgrade 1")
    mSenderClass = NewObject[Sender_ADA]()
    mType = EMessageType::MT_TUTORIAL
    
