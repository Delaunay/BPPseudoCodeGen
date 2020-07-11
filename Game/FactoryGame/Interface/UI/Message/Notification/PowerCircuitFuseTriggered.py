
from codegen.ue4_stub import *

from Script.Engine import Conv_StringToText
from Game.FactoryGame.Interface.UI.Message.Notification.PowerCircuitFuseTriggered import ExecuteUbergraph_PowerCircuitFuseTriggered
from Script.Engine import EqualEqual_TextText
from Script.UMG import SetText
from Script.FactoryGame import FGMessageBase
from Script.Engine import Default__KismetTextLibrary

class PowerCircuitFuseTriggered(FGMessageBase):
    mText: FText
    mTitle = NSLOCTEXT("", "EB6E3F1C4B7231855A814FB81365452E", "Power Circuit Notification")
    mPreviewText = NSLOCTEXT("", "BC3FE56047ECE8F69595C5B015C3551A", "A fuse has been triggered! Be sure to check your power circuits from time to time.")
    mSenderClass = NewObject[Sender_Checkit]()
    
    def Construct(self):
        self.ExecuteUbergraph_PowerCircuitFuseTriggered(10)
    

    def ExecuteUbergraph_PowerCircuitFuseTriggered(self):
        ReturnValue: FText = Default__KismetTextLibrary.Conv_StringToText("")
        
        ReturnValue_0: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[self.mText], Ref[ReturnValue])
        if not ReturnValue_0:
            goto('L141')
        # End
        
        # Label 141
        self.RichTextBlock_26.SetText(Ref[self.mText])
    
