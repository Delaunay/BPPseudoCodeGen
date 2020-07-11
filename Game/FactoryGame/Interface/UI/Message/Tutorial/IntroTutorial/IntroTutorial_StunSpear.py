
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class IntroTutorial_StunSpear(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_2_0.Play_VO_ADA_TUTORIAL_2_0'}, 'Subtitle': 'NSLOCTEXT("", "2739DDFD4B684039E7C324977ABCD322", "Second Objective: Please ensure you have your FICSIT Incorporated ‘Xeno-Zapper’ equipped before leaving the drop-zone.")', 'SenderClass': 'None'}, {'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Onboarding/Tutorial/General/Play_VO_ADA_TUTORIAL_2_1.Play_VO_ADA_TUTORIAL_2_1'}, 'Subtitle': 'NSLOCTEXT("", "A8D01DCE4504D08EC50AD28607B91A10", "Note: According to FICSIT regulations every pioneer should have access to a means of defence against extraterrestrial threats.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "804F2BFB45EE3BAD3821BCB5BB6525FD", "Onboarding: Equip Xenozapper")
    mSenderClass = NewObject[Sender_ADA]()
    mType = EMessageType::MT_TUTORIAL
    
