
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipment
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.HUDHelpers.Widget_HUDBox import Widget_HUDBox

class Widget_HUDBox_Equipment_Parent(UserWidget):
    mEquipment: Ptr[FGEquipment]
    mHudBoxParent: Ptr[Widget_HUDBox]
    
