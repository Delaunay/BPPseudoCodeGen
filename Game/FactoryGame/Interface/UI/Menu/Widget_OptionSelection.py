
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Interface.UI.Menu.Widget_OptionSelection import ExecuteUbergraph_Widget_OptionSelection
from Script.FactoryGame import GetFGGameUserSettings
from Script.FactoryGame import SetFloatOptionValue
from Script.Engine import EqualEqual_FloatFloat
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Interface.UI.Menu.Widget_OptionValueController import Widget_OptionValueController
from Script.FactoryGame import FGGameUserSettings
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.FactoryGame import Default__FGGameUserSettings
from Script.FactoryGame import SetIntOptionValue
from Script.Engine import NotEqual_StrStr
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import WidgetAnimation
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import NotEqual_ByteByte
from Script.Engine import Map_Find
from Script.FactoryGame import GetIntOptionValue
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import GetNewSelectionKey
from Script.Engine import SelectColor
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_Click import Play_UI_MainMenu_Click
from Script.Engine import Map_Keys
from Script.UMG import SetContentColorAndOpacity
from Script.FactoryGame import GetFloatOptionValue
from Script.AkAudio import AkComponent
from Script.Engine import Default__BlueprintMapLibrary
from Script.CoreUObject import LinearColor

class Widget_OptionSelection(Widget_OptionValueController):
    onPressedAnimation: Ptr[WidgetAnimation]
    mText: FText
    currentKey: FString
    
    def HandleSelection(self, incrementSelection: bool):
        if not self.mIsDynamicOption:
            goto('L755')
        ReturnValue: FString = self.GetNewSelectionKey(self.currentKey, incrementSelection)
        ReturnValue_0: bool = Default__KismetStringLibrary.NotEqual_StrStr(self.currentKey, ReturnValue)
        if not ReturnValue_0:
            goto('L755')
        ReturnValue = self.GetNewSelectionKey(self.currentKey, incrementSelection)
        self.currentKey = ReturnValue
        CmpSuccess: bool = NotEqual_ByteByte(self.mOptionRowData.OptionType, 1)
        if not CmpSuccess:
            goto('L320')
        CmpSuccess = NotEqual_ByteByte(self.mOptionRowData.OptionType, 2)
        if not CmpSuccess:
            goto('L540')
        # End
        # Label 320
        ReturnValue1: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        
        self.mOptionRowData.IntegerSelectionValues = None
        Value1 = None
        ReturnValue1_0: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mOptionRowData.IntegerSelectionValues], Ref[self.currentKey], Ref[Value1])
        ReturnValue1.SetIntOptionValue(self.mOptionRowData.ConsoleVariable, Value1, self.mOptionRowData.UpdateInstantly, self.mOptionRowData.RequireRestart)
        # End
        # Label 540
        ReturnValue_1: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        
        self.mOptionRowData.FloatSelectionValues = None
        Value = None
        ReturnValue_2: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mOptionRowData.FloatSelectionValues], Ref[self.currentKey], Ref[Value])
        ReturnValue_1.SetFloatOptionValue(self.mOptionRowData.ConsoleVariable, Value, self.mOptionRowData.UpdateInstantly, self.mOptionRowData.RequireRestart)
    

    def UpdateSelectionValue(self):
        ExecutionFlow.Push("L1584")
        ReturnValue: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        CmpSuccess: bool = NotEqual_ByteByte(self.mOptionRowData.OptionType, 1)
        if not CmpSuccess:
            goto('L156')
        CmpSuccess = NotEqual_ByteByte(self.mOptionRowData.OptionType, 2)
        if not CmpSuccess:
            goto('L911')
        goto(ExecutionFlow.Pop())
        # Label 156
        Keys1: List[FString] = []
        
        self.mOptionRowData.IntegerSelectionValues = None
        Default__BlueprintMapLibrary.Map_Keys(Ref[self.mOptionRowData.IntegerSelectionValues], Ref[Keys1])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 272
        ReturnValue_0: int32 = len(Keys1)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L837")
        
        Item1 = None
        Item1 = Keys1[Variable_0]
        
        self.mOptionRowData.IntegerSelectionValues = None
        Item1 = None
        Value = None
        ReturnValue_2: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mOptionRowData.IntegerSelectionValues], Ref[Item1], Ref[Value])
        ReturnValue_3: int32 = ReturnValue.GetIntOptionValue(self.mOptionRowData.ConsoleVariable)
        ReturnValue_4: bool = EqualEqual_IntInt(Value, ReturnValue_3)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        
        Item1 = None
        Item1 = Keys1[Variable_0]
        self.currentKey = Item1
        # Label 750
        ReturnValue_5: FText = Default__KismetTextLibrary.Conv_StringToText(self.currentKey)
        self.mText = ReturnValue_5
        goto(ExecutionFlow.Pop())
        # Label 837
        ReturnValue_6: int32 = Variable + 1
        Variable = ReturnValue_6
        goto('L272')
        # Label 911
        Keys: List[FString] = []
        
        self.mOptionRowData.FloatSelectionValues = None
        Default__BlueprintMapLibrary.Map_Keys(Ref[self.mOptionRowData.FloatSelectionValues], Ref[Keys])
        Variable1: int32 = 0
        Variable1_0: int32 = 0
        
        # Label 1027
        ReturnValue1: int32 = len(Keys)
        ReturnValue1_0: bool = Variable1 <= ReturnValue1
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        Variable1_0 = Variable1
        ExecutionFlow.Push("L1510")
        
        Item = None
        Item = Keys[Variable1_0]
        
        self.mOptionRowData.FloatSelectionValues = None
        Item = None
        Value1 = None
        ReturnValue1_1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mOptionRowData.FloatSelectionValues], Ref[Item], Ref[Value1])
        ReturnValue_7: float = ReturnValue.GetFloatOptionValue(self.mOptionRowData.ConsoleVariable)
        ReturnValue_8: bool = EqualEqual_FloatFloat(Value1, ReturnValue_7)
        if not ReturnValue_8:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = Keys[Variable1_0]
        self.currentKey = Item
        goto('L750')
        # Label 1510
        ReturnValue1_2: int32 = Variable1 + 1
        Variable1 = ReturnValue1_2
        goto('L1027')
    

    def GetHoverColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue: bool = self.IsHovered()
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue_0: LinearColor = SelectColor(Orange, Graphics, ReturnValue)
        ReturnValue_1: LinearColor = ReturnValue_0
    

    def GetOptionName(self):
        ReturnValue = self.mText
    

    def BndEvt__mButtonOptionRight_K2Node_ComponentBoundEvent_170_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_OptionSelection(115)
    

    def OnRowHovered(self):
        self.ExecuteUbergraph_Widget_OptionSelection(220)
    

    def OnRowUnhovered(self):
        self.ExecuteUbergraph_Widget_OptionSelection(266)
    

    def BndEvt__mButtonOptionRight_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_OptionSelection(312)
    

    def OnInitValueController(self):
        self.ExecuteUbergraph_Widget_OptionSelection(317)
    

    def BndEvt__mButtonOptionLeft_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_OptionSelection(336)
    

    def OnOptionValueUpdated(self):
        self.ExecuteUbergraph_Widget_OptionSelection(341)
    

    def BndEvt__mButtonOptionLeft_K2Node_ComponentBoundEvent_188_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_OptionSelection(10)
    

    def ExecuteUbergraph_Widget_OptionSelection(self):
        self.HandleSelection(False)
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Click, ReturnValue, True)
        # End
        self.HandleSelection(True)
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Click, ReturnValue1, True)
        # End
        self.mTintBorder.SetContentColorAndOpacity(self.mHoveredColor)
        # End
        self.mTintBorder.SetContentColorAndOpacity(self.mUnhoveredColor)
        # End
        # End
        self.UpdateSelectionValue()
        # End
        # End
        self.UpdateSelectionValue()
    
