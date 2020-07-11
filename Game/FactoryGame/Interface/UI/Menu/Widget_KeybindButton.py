
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.FactoryGame import GetKeyNameForAxis
from Script.Engine import SetObjectPropertyByName
from Game.FactoryGame.Interface.UI.Menu.Widget_KeybindButton import ExecuteUbergraph_Widget_KeybindButton
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.FactoryGame import RebindActionKey
from Script.Engine import EqualEqual_BoolBool
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Game.FactoryGame.Interface.UI.Menu.Widget_KeyBindFocus import Widget_KeyBindFocus
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_MouseOver import Play_UI_MainMenu_MouseOver
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Interface.UI.Menu.KeyBindData import KeyBindData
from Script.Engine import EqualEqual_NameName
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.Widget_KeyBind import Widget_KeyBind
from Script.Engine import BooleanOR
from Script.FactoryGame import CreateFGKeyMappingStruct
from Script.FactoryGame import FGKeyMapping
from Script.FactoryGame import GetOverlappingKeyMapping
from Script.FactoryGame import FGPlayerControllerBase
from Script.Engine import Format
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.AkAudio import Default__AkGameplayStatics
from Script.UMG import UserWidget
from Script.FactoryGame import GetKeyNameForAction
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import SelectColor
from Script.UMG import Create
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_Click import Play_UI_MainMenu_Click
from Script.FactoryGame import AddPopupWithCloseDelegate
from Script.FactoryGame import IsFGKeyMappingAvailable
from Script.UMG import AddToViewport
from Script.AkAudio import AkComponent
from Script.FactoryGame import Default__FGInputLibrary
from Script.CoreUObject import LinearColor

class Widget_KeybindButton(UserWidget):
    mCaptureInput: bool
    mKeyBindData: KeyBindData
    mCachedFGKeyMapping: FGKeyMapping
    mKeyBindParent: Ptr[Widget_KeyBind]
    
    def UpdateKeyMapping(self):
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': '...'}"
        Variable1: bool = self.mCaptureInput
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: FText = Default__FGInputLibrary.GetKeyNameForAction(ReturnValue, self.mKeyBindData.ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885, False, False)
        ReturnValue_1: FText = Default__FGInputLibrary.GetKeyNameForAxis(ReturnValue, self.mKeyBindData.ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885, self.mKeyBindData.PositiveAxisScale_10_3C123C154A1C495D35EE54B5CEA682C6, False)
        Variable_0: bool = self.mKeyBindData.AxisMapping_7_F80A67E0493A9BB92D5041A364C12ACF
        
        switch = {
            False: ReturnValue_0,
            True: ReturnValue_1
        }
        
        switch_0 = {
            False: switch.get(Variable_0, None),
            True: Variable
        }
        self.mKeyNameTextfield.SetText(switch_0.get(Variable1, None))
    

    def RebindKey(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Base: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue)
        bSuccess: bool = Base
        if not bSuccess:
            goto('L165')
        ReturnValue_0: bool = Base.RebindActionKey(self.mCachedFGKeyMapping)
        self.mCaptureInput = False
    

    def KeyBindingOverrideConfirmed(self, confirmed: bool):
        self.mKeyBindParent.mOwningWidget.mOwningMenu.RestoreFocusOnPopupClosed(False)
        if not confirmed:
            goto('L114')
        self.RebindKey()
        # End
        # Label 114
        self.ShowKeyBindWidget()
    

    def GetHoverColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue: bool = self.mButton.IsHovered()
        ReturnValue_0: bool = BooleanOR(ReturnValue, self.mCaptureInput)
        ReturnValue_1: LinearColor = SelectColor(Orange, Graphics, ReturnValue_0)
        ReturnValue_2: LinearColor = ReturnValue_1
    

    def HandleInput(self, InputEvent: InputEvent, keyPressed: Key):
        ExecutionFlow.Push("L1830")
        ReturnValue: FGKeyMapping = Default__FGInputLibrary.CreateFGKeyMappingStruct(self.mKeyBindData.ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885, self.mKeyBindData.AxisMapping_7_F80A67E0493A9BB92D5041A364C12ACF, self.mKeyBindData.PositiveAxisScale_10_3C123C154A1C495D35EE54B5CEA682C6, InputEvent, keyPressed)
        self.mCachedFGKeyMapping = ReturnValue
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        ReturnValue_0: bool = Default__FGInputLibrary.IsFGKeyMappingAvailable(ReturnValue1, Ref[self.mCachedFGKeyMapping])
        if not ReturnValue_0:
            goto('L267')
        self.RebindKey()
        goto(ExecutionFlow.Pop())
        # Label 267
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 324
        ReturnValue_1: bool = Not_PreBool(Variable)
        
        self.mKeyBindParent.mKeyInputsData = None
        ReturnValue_2: int32 = len(self.mKeyBindParent.mKeyInputsData)
        ReturnValue_3: bool = Variable_0 <= ReturnValue_2
        ReturnValue_4: bool = ReturnValue_1 and ReturnValue_3
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        Variable_1 = Variable_0
        ExecutionFlow.Push("L1116")
        
        self.mKeyBindParent.mKeyInputsData = None
        Item = None
        Item = self.mKeyBindParent.mKeyInputsData[Variable_1]
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        
        ReturnValue_6: FGKeyMapping = Default__FGInputLibrary.GetOverlappingKeyMapping(ReturnValue_5, Ref[self.mCachedFGKeyMapping])
        Variable1: bool = ReturnValue_6.IsAxisMapping
        Variable_2: bool = ReturnValue_6.IsAxisMapping
        ReturnValue_7: bool = ReturnValue_6.AxisKeyMapping.Scale > 0
        ReturnValue_8: bool = EqualEqual_BoolBool(Item.PositiveAxisScale_10_3C123C154A1C495D35EE54B5CEA682C6, ReturnValue_7)
        
        switch = {
            False: ReturnValue_6.ActionKeyMapping.ActionName,
            True: ReturnValue_6.AxisKeyMapping.AxisName
        }
        ReturnValue_9: bool = EqualEqual_NameName(Item.ActionName_4_C7B4F53E48A16B3F01376F97B2DA4885, switch.get(Variable_2, None))
        ReturnValue1_0: bool = ReturnValue_9 and ReturnValue_8
        
        switch_0 = {
            False: ReturnValue_9,
            True: ReturnValue1_0
        }
        if not switch_0.get(Variable1, None):
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1190")
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 1116
        ReturnValue_10: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_10
        goto('L324')
        
        self.mKeyBindParent.mKeyInputsData = None
        Item = None
        # Label 1190
        Item = self.mKeyBindParent.mKeyInputsData[Variable_1]
        FormatArgumentData.ArgumentName = "DisplayName"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = Item.DisplayName_5_0A86F675465E0C811D17A287BB986630
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_11: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1549, 'Value': 'This binding is currently bound to {DisplayName}. Rebind anyway?'}", Array)
        OutputDelegate.BindUFunction(self, KeyBindingOverrideConfirmed)
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        
        OutputDelegate = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue2, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1750, 'Value': 'Rebinding Conflict'}", ReturnValue_11, 1, None, None, Ref[OutputDelegate])
        goto(ExecutionFlow.Pop())
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_KeybindButton(40)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_25_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_KeybindButton(113)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_3_OnButtonReleasedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_KeybindButton(380)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_KeybindButton(385)
    

    def ShowKeyBindWidget(self):
        self.ExecuteUbergraph_Widget_KeybindButton(475)
    

    def ExecuteUbergraph_Widget_KeybindButton(self):
        # Label 10
        self.mCaptureInput = True
        self.UpdateKeyMapping()
        # End
        self.mLabel.SetText(self.mKeyBindData.DisplayName_5_0A86F675465E0C811D17A287BB986630)
        self.UpdateKeyMapping()
        # End
        # Label 113
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_KeyBindFocus] = Default__WidgetBlueprintLibrary.Create(self, Widget_KeyBindFocus, ReturnValue)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_0, "mKeyOwner", self)
        ReturnValue_0.AddToViewport(0)
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Click, ReturnValue1, True)
        goto('L10')
        # End
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_MouseOver, ReturnValue2, True)
        # End
        goto('L113')
    
