
from codegen.ue4_stub import *

from Script.Engine import Texture2D
from Script.UMG import UserWidget
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers

class Widget_Subtitle(UserWidget):
    SpawnAnimation: Ptr[WidgetAnimation]
    mSpeakerIcon: Ptr[Texture2D]
    
    def GetLightGrayText(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Text
    

    def GetOrangeText(self):
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue = OrangeText
    
