
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_PickUp_AlienCarapace(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Exploration/Alien/Play_VO_ADA_PICKUP_AlienCarapace.Play_VO_ADA_PICKUP_AlienCarapace'}, 'Subtitle': 'NSLOCTEXT("", "23260FD44C2124114F63DA9F96FE1D48", "The remains of this creature might shed light on how to increase chances of survival. A new research tree can now be accessed in the MAM.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "C8B109704E25B2E5FAB0FF89C16857DF", "Exploration: Alien Carapace")
    mPreviewText = NSLOCTEXT("", "3A53A88A4F7DC72CA49BAD9E0AD3429F", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
