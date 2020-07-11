
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import Actor
from Script.UMG import SetRenderScale
from Script.CoreUObject import Vector2D
from Script.UMG import UserWidget

class Widget_ObjectScannerMenuItem(UserWidget):
    mIsSelected: bool
    mText: FText
    OnItemSelected: FMulticastScriptDelegate
    mDescription: FText
    mCirclePosition: Vector2D
    mScannedActorClass: TSubclassOf[Actor]
    
    def GetButtonFeedback(self):
        if not self.mIsSelected:
            goto('L135')
        self.SetRenderScale(Vector2D(X = 1.2000000476837158, Y = 1.2000000476837158))
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Graphics
        goto('L251')
        # Label 135
        self.SetRenderScale(Vector2D(X = 1, Y = 1))
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Graphics
    

    def GetTextColor(self):
        if not self.mIsSelected:
            goto('L101')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Text
        goto('L183')
        
        Text = None
        Graphics = None
        # Label 101
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Text
    

    def OnItemSelected__DelegateSignature(self, scannedActorClass: TSubclassOf[Actor]):
        pass
    
