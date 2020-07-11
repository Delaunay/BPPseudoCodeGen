
from codegen.ue4_stub import *

from Script.Engine import Default__KismetTextLibrary
from Script.UMG import GetParent
from Script.UMG import UserWidget
from Script.Engine import FormatArgumentData
from Script.FactoryGame import Default__FGBuildCategory
from Script.UMG import PanelWidget
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu_SubCategoryButton import ExecuteUbergraph_Widget_BuildMenu_SubCategoryButton.K2Node_CustomEvent_inClass
from Script.FactoryGame import FGBuildSubCategory
from Script.UMG import GetChildIndex
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu_SubCategoryButton import ExecuteUbergraph_Widget_BuildMenu_SubCategoryButton
from Script.FactoryGame import GetCategoryName

class Widget_BuildMenu_SubCategoryButton(UserWidget):
    mSubCategory: TSubclassOf[FGBuildSubCategory]
    mSubCategoryText: FText
    
    def GetSubcategoryNameTest(self, inClass: TSubclassOf[FGBuildCategory]):
        ExecuteUbergraph_Widget_BuildMenu_SubCategoryButton.K2Node_CustomEvent_inClass = inClass #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_BuildMenu_SubCategoryButton(10)
    

    def ExecuteUbergraph_Widget_BuildMenu_SubCategoryButton(self):
        ReturnValue: FText = Default__FGBuildCategory.GetCategoryName(inClass)
        self.mSubCategoryText = ReturnValue
        FormatArgumentData.ArgumentName = "Subcategory Name"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = self.mSubCategoryText
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue_0: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_1: int32 = ReturnValue_0.GetChildIndex(self)
        ReturnValue_2: int32 = ReturnValue_1 + 1
        FormatArgumentData1.ArgumentName = "Index"
        FormatArgumentData1.ArgumentValueType = 0
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = ReturnValue_2
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 681, 'Value': '{Index}. {Subcategory Name}'}", Array)
        self.mSubcategoryName.SetText(ReturnValue_3)
    
