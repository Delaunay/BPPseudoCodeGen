
from codegen.ue4_stub import *

from Script.Engine import Conv_StringToText
from Script.Engine import EqualEqual_TextText
from Script.UMG import SetText
from Game.FactoryGame.Interface.UI.Message.Tutorial.TutorialMails.Tutorial_Map import ExecuteUbergraph_Tutorial_Map
from Script.FactoryGame import FGMessageBase
from Script.Engine import Default__KismetTextLibrary

class Tutorial_Map(FGMessageBase):
    mText: FText
    mTitle = NSLOCTEXT("", "0AD66D084C16EAEC60C53D8DA8CBA15B", "Tutorial Map")
    mPreviewText = NSLOCTEXT("", "A07D4D6347A0996290FAEEBB639375AD", "Added new functionality: Map [ Z ]")
    mType = EMessageType::MT_TUTORIAL
    
    def Construct(self):
        self.ExecuteUbergraph_Tutorial_Map(10)
    

    def ExecuteUbergraph_Tutorial_Map(self):
        ReturnValue: FText = Default__KismetTextLibrary.Conv_StringToText("")
        
        ReturnValue_0: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[self.mText], Ref[ReturnValue])
        if not ReturnValue_0:
            goto('L141')
        # End
        
        # Label 141
        self.RichTextBlock_0.SetText(Ref[self.mText])
    
