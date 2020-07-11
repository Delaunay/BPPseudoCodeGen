
from codegen.ue4_stub import *

from Script.Engine import TextToUpper
from Script.UMG import UserWidget
from Script.UMG import ESlateVisibility
from Script.FactoryGame import FGSchematicCategory
from Game.FactoryGame.BPW_ResourceSinkShop_Subcategory_Header import ExecuteUbergraph_BPW_ResourceSinkShop_Subcategory_Header
from Script.UMG import WidgetAnimation
from Script.FactoryGame import GetCategoryName
from Script.FactoryGame import Default__FGSchematicCategory
from Script.Engine import Default__KismetTextLibrary

class BPW_ResourceSinkShop_Subcategory_Header(UserWidget):
    FadeInCategory: Ptr[WidgetAnimation]
    mNameText: FText
    mSchematicSubcategory: TSubclassOf[FGSchematicCategory]
    mHideTitle: bool
    
    def GetResourceShopSubcategoryName(self, mSchematicSubcategory: TSubclassOf[FGSchematicCategory]):
        ReturnValue: FText = Default__FGSchematicCategory.GetCategoryName(mSchematicSubcategory)
        self.mNameText = ReturnValue
        
        ReturnValue_0: FText = Default__KismetTextLibrary.TextToUpper(Ref[self.mNameText])
        self.mSubcategoryName.SetText(ReturnValue_0)
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_ResourceSinkShop_Subcategory_Header(10)
    

    def ExecuteUbergraph_BPW_ResourceSinkShop_Subcategory_Header(self):
        Variable: uint8 = 1
        Variable1: uint8 = 0
        Variable_0: bool = self.mHideTitle
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mTitleContainer.SetVisibility(switch.get(Variable_0, None))
        self.GetResourceShopSubcategoryName(self.mSchematicSubcategory)
    
