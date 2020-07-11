
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.Compass.Widget_CompassObjectCardinalDirection import ExecuteUbergraph_Widget_CompassObjectCardinalDirection
from Script.SlateCore import Margin
from Script.UMG import ESlateVisibility
from Script.CoreUObject import Vector2D
from Script.FactoryGame import FGCompassObjectWidget
from Script.Engine import IsValid
from Script.UMG import SetAutoSize
from Script.UMG import SetLayout
from Game.FactoryGame.Interface.UI.Compass.Widget_CompassObjectCardinalDirection import ExecuteUbergraph_Widget_CompassObjectCardinalDirection.K2Node_Event_parentSlot

class Widget_CompassObjectCardinalDirection(FGCompassObjectWidget):
    
    
    def GetVisibility_0(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mTexture)
        if not ReturnValue:
            goto('L90')
        ReturnValue_0: uint8 = 2
        goto('L110')
        # Label 90
        ReturnValue_0 = 0
    

    def OnCompassObjectAddedToPanel(self):
        ExecuteUbergraph_Widget_CompassObjectCardinalDirection.K2Node_Event_parentSlot = parentSlot #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_CompassObjectCardinalDirection(122)
    

    def ExecuteUbergraph_Widget_CompassObjectCardinalDirection(self):
        # Label 10
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mTexture)
        if not ReturnValue:
            goto('L451')
        self.mPositionOffset = Vector2D(X = 0, Y = -20)
        # End
        parentSlot.SetAutoSize(True)
        Anchors.Minimum = Vector2D(X = 0.5, Y = 0)
        Anchors.Maximum = Vector2D(X = 0.5, Y = 0)
        AnchorData.Offsets = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        AnchorData.Anchors = Anchors
        AnchorData.Alignment = Vector2D(X = 0.5, Y = 0.5)
        
        AnchorData = None
        parentSlot.SetLayout(Ref[AnchorData])
        goto('L10')
    
