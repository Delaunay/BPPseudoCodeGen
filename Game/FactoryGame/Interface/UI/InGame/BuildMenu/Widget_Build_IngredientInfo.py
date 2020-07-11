
from codegen.ue4_stub import *

from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Widget_Build_IngredientInfo import ExecuteUbergraph_Widget_Build_IngredientInfo

class Widget_Build_IngredientInfo(UserWidget):
    mTitle: FText
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_Build_IngredientInfo(10)
    

    def ExecuteUbergraph_Widget_Build_IngredientInfo(self):
        self.mTitleTextBlock.SetText(self.mTitle)
    
