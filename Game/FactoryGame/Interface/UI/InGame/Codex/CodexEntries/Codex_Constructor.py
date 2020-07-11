
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_CodexEntry_Buildings import Widget_CodexEntry_Buildings

class Codex_Constructor(Widget_CodexEntry_Buildings):
    BuildingType = NewObject[Desc_ConstructorMk1]()
    mAdditionalStats = ['NSLOCTEXT("", "B487710E4A96AA0F47A1D1A9C52D7C63", "Custom Stat;So Custom")']
    
