
from codegen.ue4_stub import *

from Script.Engine import Conv_StringToText
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.BPW_Graph_DataPreview import ExecuteUbergraph_BPW_Graph_DataPreview
from Script.UMG import UserWidget
from Script.UMG import SetColorAndOpacity
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.BPW_Graph_DataPreview import ExecuteUbergraph_BPW_Graph_DataPreview.K2Node_Event_IsDesignTime
from Script.Engine import Default__KismetTextLibrary
from Script.CoreUObject import LinearColor

class BPW_Graph_DataPreview(UserWidget):
    mTitle: FString
    mStartingValue: FText
    mPrimaryColor: LinearColor = Namespace(A=1, B=1, G=1, R=1)
    mSecondaryColor: LinearColor = Namespace(A=1, B=0.13563300669193268, G=0.13286800682544708, R=0.13286800682544708)
    OnHovered: FMulticastScriptDelegate
    OnUnhovered: FMulticastScriptDelegate
    
    def SetValue(self, Value: FText):
        self.mGraphValue.SetText(Value)
    

    def SetGraphID(self, mTitle: FString):
        self.mTitle = mTitle
        ReturnValue: FText = Default__KismetTextLibrary.Conv_StringToText(self.mTitle)
        self.mGraphName.SetText(ReturnValue)
    

    def PreConstruct(self):
        ExecuteUbergraph_BPW_Graph_DataPreview.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_Graph_DataPreview(38)
    

    def BndEvt__mPreviewButton_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_Graph_DataPreview(319)
    

    def BndEvt__mPreviewButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_Graph_DataPreview(345)
    

    def ExecuteUbergraph_BPW_Graph_DataPreview(self):
        # Label 10
        self.SetValue(self.mStartingValue)
        # End
        self.SetGraphID(self.mTitle)
        self.mGraphNameBackground.SetColorAndOpacity(self.mPrimaryColor)
        SlateColor.SpecifiedColor = self.mPrimaryColor
        SlateColor.ColorUseRule = 0
        self.mGraphValue.SetColorAndOpacity(SlateColor)
        SlateColor1.SpecifiedColor = self.mSecondaryColor
        SlateColor1.ColorUseRule = 0
        self.mGraphName.SetColorAndOpacity(SlateColor1)
        goto('L10')
        self.OnHovered.ProcessMulticastDelegate("")
        # End
        self.OnUnhovered.ProcessMulticastDelegate("")
    

    def OnUnhovered__DelegateSignature(self, GraphID: FString):
        pass
    

    def OnHovered__DelegateSignature(self, GraphID: FString):
        pass
    
