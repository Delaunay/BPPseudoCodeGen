
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Message.Widget_AudioMessage import Widget_AudioMessage

class Message_Pickup_FlowerPetals(Widget_AudioMessage):
    mAudioEvents = [{'audioEvent': {'$AssetPath': '/Game/FactoryGame/-Shared/Audio/VO/Rework/Exploration/FlowerPetals/Play_VO_ADA_PICKUP_FlowerPetals.Play_VO_ADA_PICKUP_FlowerPetals'}, 'Subtitle': 'NSLOCTEXT("", "037ABC254978962E6D895FA25C398292", "Pigment could be harvested from these flower petals and turned into dye. A new research tree can now be accessed in the MAM.")', 'SenderClass': 'None'}]
    mSubtitleTimeMultiplier = 0.06499999761581421
    mTitle = NSLOCTEXT("", "B3B793CE4191681CA031F595A14141A2", "Exploration: Flower Petals")
    mPreviewText = NSLOCTEXT("", "BFE684A24CD43B55E17980AAF060500F", "Preview message")
    mSenderClass = NewObject[Sender_ADA]()
    
