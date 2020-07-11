
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class IntroTutorialHubLvl1_5(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_5_1.Play_VO_ADA_TUTORIAL_5_1'}, 'Subtitle': 'NSLOCTEXT("", "96C1B9A043B4F38E6878C49CCCB3B196", "Congratulations! You have unlocked: Building: Workshop. Equipment: Portable Miner. Inventory: Additional Slots. HUB Feature: Personal Storage.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_6_0.Play_VO_ADA_TUTORIAL_6_0'}, 'Subtitle': 'NSLOCTEXT("", "34B0D6E74ADB697F0DAA9D96FF75E284", "Sixth Objective: Complete HUB Upgrade 2. Note: Portable miners require no power and will mine a node until their inventory is full. Note: Multiple portable miners can be used on a single node.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.07500000298023224
    mTitle = NSLOCTEXT("", "1437459F4A234750842276853366A990", "Onboarding: Upgrade HUB to level 2")
    mSenderClass = NewObject[Sender_ADA]()
    mType = EMessageType::MT_TUTORIAL
    
