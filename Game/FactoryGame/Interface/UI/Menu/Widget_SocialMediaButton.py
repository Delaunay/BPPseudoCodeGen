
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Interface.UI.Menu.Graphics.Discord_Icon import Discord_Icon
from Script.SlateCore import Margin
from Game.FactoryGame.Interface.UI.Menu.Graphics.Facebook_Icon import Facebook_Icon
from Script.MediaAssets import MediaPlayer
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Game.FactoryGame.Interface.UI.Menu.Graphics.Twitter_Icon import Twitter_Icon
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_MouseOver import Play_UI_MainMenu_MouseOver
from Script.CoreUObject import Object
from Game.FactoryGame.Interface.UI.Menu.Graphics.Reddit_Icon import Reddit_Icon
from Game.FactoryGame.Interface.UI.Menu.Widget_SocialMediaButton import ExecuteUbergraph_Widget_SocialMediaButton
from Script.CoreUObject import LinearColor
from Game.FactoryGame.Interface.UI.Menu.Graphics.Instagram_Icon import Instagram_Icon
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import LaunchURL
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_Click import Play_UI_MainMenu_Click
from Script.CoreUObject import Vector2D
from Script.SlateCore import SlateColor
from Script.AkAudio import AkComponent
from Game.FactoryGame.Interface.UI.Menu.SocialMediaEnum import SocialMediaEnum

class Widget_SocialMediaButton(UserWidget):
    mSocialMediaType: uint8
    NewVar_0: Ptr[MediaPlayer]
    
    def GetHoverState(self):
        ReturnValue: bool = self.IsHovered()
        if not ReturnValue:
            goto('L95')
        ReturnValue_0: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        goto('L147')
        # Label 95
        ReturnValue_0 = LinearColor(R = 1, G = 1, B = 1, A = 0.6000000238418579)
    

    def GetIcon(self):
        Variable: Ptr[Object] = Twitter_Icon
        Variable1: Ptr[Object] = Discord_Icon
        Variable2: Ptr[Object] = Instagram_Icon
        Variable3: Ptr[Object] = Facebook_Icon
        Variable4: Ptr[Object] = Reddit_Icon
        # Label 95
        Variable_0: uint8 = self.mSocialMediaType
        SlateBrush.ImageSize = Vector2D(X = 48, Y = 48)
        SlateBrush.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush.TintColor = SlateColor(SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1), ColorUseRule = 0)
        
        switch = {
            0: Variable4,
            1: Variable3,
            2: Variable2,
            3: Variable1,
            4: Variable
        }
        SlateBrush.ResourceObject = switch.get(Variable_0, None)
        SlateBrush.DrawAs = 3
        SlateBrush.Tiling = 0
        SlateBrush.Mirroring = 0
        ReturnValue = SlateBrush
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_55_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SocialMediaButton(15)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SocialMediaButton(529)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SocialMediaButton(10)
    

    def ExecuteUbergraph_Widget_SocialMediaButton(self):
        # End
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Click, ReturnValue, True)
        Variable: FString = "www.twitter.com/SatisfactoryAF"
        Variable1: FString = "https://discord.gg/satisfactory"
        Variable2: FString = "www.instagram.com/coffee_stain_studios"
        Variable3: FString = "www.facebook.com/SatisfactoryGame"
        Variable4: FString = "www.reddit.com/r/SatisfactoryGame"
        Variable_0: uint8 = self.mSocialMediaType
        
        switch = {
            0: Variable4,
            1: Variable3,
            2: Variable2,
            3: Variable1,
            4: Variable
        }
        Default__KismetSystemLibrary.LaunchURL(switch.get(Variable_0, None))
        # End
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_MouseOver, ReturnValue1, True)
    
