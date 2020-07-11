
from codegen.ue4_stub import *

from Script.Engine import SetTextPropertyByName
from Script.Engine import Delay
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_LetterSpacedText import ExecuteUbergraph_Widget_LetterSpacedText.K2Node_Event_IsDesignTime
from Script.UMG import SetPadding
from Script.Slate import ETextJustify
from Script.UMG import OverlaySlot
from Script.UMG import GetChildrenCount
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.UMG import SlotAsOverlaySlot
from Script.Engine import Conv_IntToFloat
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_LetterSpacedLetter import Widget_LetterSpacedLetter
from Script.UMG import PlayAnimation
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import ToUpper
from Script.Engine import Conv_StringToText
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_LetterSpacedText import ExecuteUbergraph_Widget_LetterSpacedText.K2Node_CustomEvent_Text
from Script.UMG import Widget
from Script.SlateCore import SlateFontInfo
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Script.SlateCore import SlateColor
from Script.UMG import SetRenderOpacity
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_LetterSpacedText import ExecuteUbergraph_Widget_LetterSpacedText
from Script.Engine import GetCharacterArrayFromString

class Widget_LetterSpacedText(UserWidget):
    mText: FString = Works
    TempText: FString
    mCapitalLetters: bool = True
    mFont: SlateFontInfo = Namespace(FontMaterial={'$Empty': True}, FontObject={'$AssetPath': '/Game/FactoryGame/Interface/Font/DescriptionText.DescriptionText'}, OutlineSettings={'OutlineSize': 0, 'bSeparateFillAlpha': False, 'bApplyOutlineToDropShadows': True, 'OutlineMaterial': {'$Empty': True}, 'OutlineColor': {'R': 0, 'G': 0, 'B': 0, 'A': 1}}, Size=15, TypefaceFontName='Regular')
    mColor: SlateColor = Namespace(ColorUseRule=0, SpecifiedColor={'R': 1, 'G': 1, 'B': 1, 'A': 1})
    mSpacingText: FString
    mJustification: uint8
    mLetterSpacing: float = 3
    mLetterObjects: List[Ptr[Widget_LetterSpacedLetter]]
    mAnimate: bool
    mLetterSpacingTemp: float = 1.5
    
    def PreConstruct(self):
        ExecuteUbergraph_Widget_LetterSpacedText.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_LetterSpacedText(2297)
    

    def SetTitle(self, text: FString):
        ExecuteUbergraph_Widget_LetterSpacedText.K2Node_CustomEvent_Text = text #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_LetterSpacedText(2369)
    

    def OnAnimateText(self):
        self.ExecuteUbergraph_Widget_LetterSpacedText(2437)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_LetterSpacedText(2442)
    

    def ExecuteUbergraph_Widget_LetterSpacedText(self):
        goto(ComputedJump("EntryPoint"))
        ExecutionFlow.Push("L170")
        
        Item1 = None
        Item1 = self.mLetterObjects[Variable]
        ReturnValue: Ptr[UMGSequencePlayer] = Item1.PlayAnimation(Item1.SpawnAnim, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 170
        ReturnValue_0: int32 = Variable + 1
        Variable: int32 = ReturnValue_0
        
        # Label 239
        ReturnValue1: int32 = len(self.mLetterObjects)
        ReturnValue_1: int32 = ReturnValue1 - 1
        ReturnValue1_0: bool = Variable <= ReturnValue_1
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, 0.05000000074505806, LatentActionInfo(Linkage = 15, UUID = -864829183, ExecutionFunction = "ExecuteUbergraph_Widget_LetterSpacedText", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        if not self.mAnimate:
           goto(ExecutionFlow.Pop())
        self.OnAnimateText()
        goto(ExecutionFlow.Pop())
        # Label 490
        ReturnValue_2: Ptr[Widget_LetterSpacedLetter] = Default__WidgetBlueprintLibrary.Create(self, Widget_LetterSpacedLetter, None)
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_StringToText(self.TempText)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_2, "mText", Ref[ReturnValue_3])
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_2, "mFont", Ref[self.mFont])
        ReturnValue_4: Ptr[PanelSlot] = self.mContent.AddChild(ReturnValue_2)
        ReturnValue_5: float = self.mLetterSpacingTemp * 0.10000000149011612
        ReturnValue_6: Ptr[OverlaySlot] = Default__WidgetLayoutLibrary.SlotAsOverlaySlot(ReturnValue_2.mTextBlock)
        ReturnValue_7: float = Conv_IntToFloat(self.mFont.Size)
        ReturnValue1_1: float = ReturnValue_5 * ReturnValue_7
        Margin.Left = 0
        Margin.Top = 0
        Margin.Right = ReturnValue1_1
        Margin.Bottom = 0
        ReturnValue_6.SetPadding(Margin)
        goto(ExecutionFlow.Pop())
        # Label 1160
        Variable_0: int32 = 0
        # Label 1183
        ReturnValue_8: List[FString] = Default__KismetStringLibrary.GetCharacterArrayFromString(self.mText)
        
        ReturnValue_9: int32 = len(ReturnValue_8)
        ReturnValue_10: bool = Variable_1 <= ReturnValue_9
        if not ReturnValue_10:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable_1
        ExecutionFlow.Push("L1604")
        if not self.mCapitalLetters:
            goto('L1678')
        ReturnValue_8 = Default__KismetStringLibrary.GetCharacterArrayFromString(self.mText)
        
        Item = None
        Item = ReturnValue_8[Variable_0]
        ReturnValue_11: FString = Default__KismetStringLibrary.ToUpper(Item)
        self.TempText = ReturnValue_11
        goto('L490')
        # Label 1604
        ReturnValue2: int32 = Variable_1 + 1
        Variable_1: int32 = ReturnValue2
        goto('L1183')
        # Label 1678
        ReturnValue_8 = Default__KismetStringLibrary.GetCharacterArrayFromString(self.mText)
        
        Item = None
        Item = ReturnValue_8[Variable_0]
        self.TempText = Item
        goto('L490')
        # Label 1828
        Variable = 0
        goto('L239')
        # Label 1856
        ExecutionFlow.Push("L2093")
        ReturnValue_12: Ptr[Widget] = self.mContent.GetChildAt(Variable1)
        Letter: Ptr[Widget_LetterSpacedLetter] = Cast[Widget_LetterSpacedLetter](ReturnValue_12)
        bSuccess: bool = Letter
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Letter.SetRenderOpacity(0)
        
        ReturnValue_13: int32 = self.mLetterObjects.append(Letter)
        goto(ExecutionFlow.Pop())
        # Label 2093
        ReturnValue1_2: int32 = Variable1 + 1
        Variable1: int32 = ReturnValue1_2
        # Label 2162
        ReturnValue_14: int32 = self.mContent.GetChildrenCount()
        ReturnValue_15: bool = Variable1 <= ReturnValue_14
        if not ReturnValue_15:
            goto('L1828')
        goto('L1856')
        # Label 2269
        Variable1 = 0
        goto('L2162')
        self.SetTitle(self.mText)
        goto(ExecutionFlow.Pop())
        # Label 2321
        self.mSpacingText = ""
        Variable_1 = 0
        goto('L1160')
        self.mText = Text
        self.mContent.ClearChildren()
        goto('L2321')
        goto('L2269')
        Default__KismetSystemLibrary.Delay(self, 0.009999999776482582, LatentActionInfo(Linkage = 465, UUID = -1839244040, ExecutionFunction = "ExecuteUbergraph_Widget_LetterSpacedText", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
    
