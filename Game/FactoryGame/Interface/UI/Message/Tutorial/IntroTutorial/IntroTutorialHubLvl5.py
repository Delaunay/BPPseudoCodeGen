
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class IntroTutorialHubLvl5(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_9_1.Play_VO_ADA_TUTORIAL_9_1'}, 'Subtitle': 'NSLOCTEXT("", "6AFBF6C547E9F34DE35ED3B0C1AD60B5", "Congratulations! You have unlocked: Building: Miner Mk1. Building: Storage container. HUB Feature: Additional Biomass Burner.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_10_0.Play_VO_ADA_TUTORIAL_10_0'}, 'Subtitle': 'NSLOCTEXT("", "D6398C0C4AC31753CEF5AA9D35F78B50", "Tenth objective: Complete HUB Upgrade 6. Note: There are no notes.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.07500000298023224
    mTitle = NSLOCTEXT("", "9783376D4E8B39D45BF4AAABC68F01B3", "Onboarding: Complete HUB Upgrade 6")
    mSenderClass = NewObject[Sender_ADA]()
    mType = EMessageType::MT_TUTORIAL
    
