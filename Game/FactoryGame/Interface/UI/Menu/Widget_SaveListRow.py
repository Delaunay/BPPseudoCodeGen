
from codegen.ue4_stub import *

from Script.UMG import SetUserFocus
from Script.FactoryGame import SaveGame
from Script.UMG import GetParent
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveListRow import ExecuteUbergraph_Widget_SaveListRow.K2Node_CustomEvent_errorMessage
from Script.AkAudio import PostAkEvent
from Script.UMG import GetChildIndex
from Script.Engine import AsTimeZoneDateTime_DateTime
from Script.CoreUObject import Timespan
from Script.Engine import MakeTimespan
from Script.FactoryGame import SaveHeader
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveListRow import ExecuteUbergraph_Widget_SaveListRow.K2Node_CustomEvent_WasSuccessful
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import Handled
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetAdminInterface
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_MouseOver import Play_UI_MainMenu_MouseOver
from Script.FactoryGame import GetSaveDateTime
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveListRow import ExecuteUbergraph_Widget_SaveListRow.K2Node_CustomEvent_confirmed
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import SetColorAndOpacity
from Script.Engine import Conv_IntToText
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.FactoryGame import GetMapName
from Script.CoreUObject import DateTime
from Script.Engine import BooleanOR
from Script.FactoryGame import FGPlayerControllerBase
from Script.Engine import BreakTimespan
from Script.UMG import PanelWidget
from Script.Engine import EqualEqual_ObjectObject
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveListRow import ExecuteUbergraph_Widget_SaveListRow.K2Node_CustomEvent_success
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveList import Widget_SaveList
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.UMG import UserWidget
from Script.FactoryGame import GetName
from Script.FactoryGame import FGAdminInterface
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import DeleteSaveFile
from Script.Engine import SelectColor
from Script.FactoryGame import Default__FGSaveSession
from Script.FactoryGame import GetVersion
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_Click import Play_UI_MainMenu_Click
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveListRow import ExecuteUbergraph_Widget_SaveListRow
from Script.FactoryGame import AddPopupWithCloseDelegate
from Script.SlateCore import SlateColor
from Script.FactoryGame import GetSessionName
from Script.AkAudio import AkComponent
from Script.FactoryGame import GetPlayDurationSeconds
from Script.UMG import EventReply
from Script.CoreUObject import LinearColor

class Widget_SaveListRow(UserWidget):
    mSaveHeader: SaveHeader
    mIsSelected: bool
    OnClicked: FMulticastScriptDelegate
    mIsNewSave: bool
    mNewSaveFileName: FString
    mSaveList: Ptr[Widget_SaveList]
    bIsFocusable = True
    
    def SetColorForImage(self, ImageBG: Ptr[Image], Color: LinearColor):
        ImageBG.SetColorAndOpacity(Color)
    

    def GetNewSaveGameVisibility(self):
        if not self.mIsNewSave:
            goto('L39')
        # Label 14
        ReturnValue = 1
        goto('L59')
        # Label 39
        ReturnValue = 0
    

    def GetLoadDeleteVisibility(self):
        ReturnValue: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_0: int32 = ReturnValue.GetChildIndex(self)
        ReturnValue_1: bool = self.mSaveRowButton.IsHovered()
        ReturnValue_2: bool = EqualEqual_IntInt(ReturnValue_0, 0)
        ReturnValue_3: bool = EqualEqual_ObjectObject(self.mSaveList.mSelectedSave, self)
        ReturnValue_4: bool = BooleanOR(ReturnValue_3, ReturnValue_1)
        ReturnValue1: bool = BooleanOR(ReturnValue_4, ReturnValue_2)
        if not ReturnValue1:
            goto('L318')
        ReturnValue_5: uint8 = 0
        goto('L338')
        # Label 318
        ReturnValue_5 = 2
    

    def OnFocusReceived(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mSaveRowButton.SetUserFocus(ReturnValue)
        ReturnValue_0: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_1: EventReply = ReturnValue_0
    

    def GetSaveNameTextColor(self):
        ReturnValue: bool = self.mSaveRowButton.IsHovered()
        # Label 46
        ReturnValue_0: bool = EqualEqual_ObjectObject(self.mSaveList.mSelectedSave, self)
        Variable1: bool = ReturnValue
        Variable: bool = ReturnValue_0
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        
        TextWhite1 = None
        GraphicsWhite1 = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite1], Ref[GraphicsWhite1])
        
        switch = {
            False: OrangeText,
            True: TextWhite
        }
        
        switch_0 = {
            False: switch.get(Variable, None),
            True: TextWhite1
        }
        ReturnValue_1: SlateColor = switch_0.get(Variable1, None)
    

    def GetTextColor(self):
        ReturnValue: bool = self.mSaveRowButton.IsHovered()
        # Label 46
        ReturnValue_0: bool = EqualEqual_ObjectObject(self.mSaveList.mSelectedSave, self)
        Variable1: bool = ReturnValue
        Variable: bool = ReturnValue_0
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        
        TextWhite1 = None
        GraphicsWhite1 = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite1], Ref[GraphicsWhite1])
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        
        switch = {
            False: Text,
            True: TextWhite
        }
        
        switch_0 = {
            False: switch.get(Variable, None),
            True: TextWhite1
        }
        ReturnValue_1: SlateColor = switch_0.get(Variable1, None)
    

    def GetIconBGColor(self):
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue: bool = self.mSaveRowButton.IsHovered()
        
        TextWhite1 = None
        GraphicsWhite1 = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite1], Ref[GraphicsWhite1])
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue_0: bool = EqualEqual_ObjectObject(self.mSaveList.mSelectedSave, self)
        ReturnValue_1: LinearColor = SelectColor(GraphicsWhite, Orange, ReturnValue_0)
        # Label 318
        ReturnValue1: LinearColor = SelectColor(GraphicsWhite1, ReturnValue_1, ReturnValue)
        ReturnValue_2: LinearColor = ReturnValue1
    

    def GetIconColor(self):
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue: bool = self.mSaveRowButton.IsHovered()
        ReturnValue_0: bool = EqualEqual_ObjectObject(self.mSaveList.mSelectedSave, self)
        ReturnValue_1: LinearColor = SelectColor(Orange, GraphicsWhite, ReturnValue_0)
        # Label 318
        ReturnValue1: LinearColor = SelectColor(Graphics, ReturnValue_1, ReturnValue)
        ReturnValue_2: LinearColor = ReturnValue1
    

    def GetButtonColor(self):
        LinearColor.R = 0
        LinearColor.G = 0
        LinearColor.B = 0
        LinearColor.A = 0
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue: bool = EqualEqual_ObjectObject(self.mSaveList.mSelectedSave, self)
        ReturnValue_0: bool = self.mSaveRowButton.IsHovered()
        ReturnValue_1: LinearColor = SelectColor(Graphics, LinearColor, ReturnValue)
        ReturnValue1: LinearColor = SelectColor(Orange, ReturnValue_1, ReturnValue_0)
        ReturnValue_2: LinearColor = ReturnValue1
    

    def GetNewSaveVisibility(self):
        pass
    

    def GetSessionName(self):
        if not self.mIsNewSave:
            goto('L39')
        # Label 14
        ReturnValue = 
        goto('L184')
        
        # Label 39
        ReturnValue_0: FString = Default__FGSaveSession.GetSessionName(Ref[self.mSaveHeader])
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_0)
        ReturnValue = ReturnValue_1
    

    def GetSaveDuration(self):
        localText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': '00:00'}"
        if not self.mIsNewSave:
            goto('L109')
        # Label 77
        ReturnValue = localText
        goto('L1146')
        
        # Label 109
        ReturnValue_0: int32 = Default__FGSaveSession.GetPlayDurationSeconds(Ref[self.mSaveHeader])
        ReturnValue_1: Timespan = MakeTimespan(0, 0, 0, ReturnValue_0, 0)
        
        Days = None
        Hours = None
        Minutes = None
        Seconds = None
        Milliseconds = None
        BreakTimespan(ReturnValue_1, Ref[Days], Ref[Hours], Ref[Minutes], Ref[Seconds], Ref[Milliseconds])
        ReturnValue_2: int32 = Days * 24
        FormatArgumentData.ArgumentName = "sec"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = Seconds
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue_3: int32 = ReturnValue_2 + Hours
        FormatArgumentData1.ArgumentName = "min"
        FormatArgumentData1.ArgumentValueType = 0
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = Minutes
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        FormatArgumentData2.ArgumentName = "hours"
        FormatArgumentData2.ArgumentValueType = 0
        FormatArgumentData2.ArgumentValue = 
        FormatArgumentData2.ArgumentValueInt = ReturnValue_3
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData2, FormatArgumentData1, FormatArgumentData]
        ReturnValue_4: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1029, 'Value': 'Play Duration: {hours}h {min}m {sec}s'}", Array)
        localText = ReturnValue_4
        goto('L77')
    

    def GetDesiredFileName(self):
        
        ReturnValue: FString = Default__FGSaveSession.GetName(Ref[self.mSaveHeader])
        # Label 59
        Variable: bool = self.mIsNewSave
        
        switch = {
            False: ReturnValue,
            True: self.mNewSaveFileName
        }
        desiredFileName = switch.get(Variable, None)
    

    def Clicked(self):
        self.mIsSelected = True
        self.OnClicked.ProcessMulticastDelegate(self)
    

    def GetSaveMap(self):
        Text: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': '(Fill this with current map)'}"
        if not self.mIsNewSave:
            goto('L132')
        # Label 100
        ReturnValue = Text
        goto('L282')
        
        # Label 132
        ReturnValue_0: FString = Default__FGSaveSession.GetMapName(Ref[self.mSaveHeader])
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_0)
        Text = ReturnValue_1
        goto('L100')
    

    def GetSaveVersion(self):
        if not self.mIsNewSave:
            goto('L46')
        # Label 14
        ReturnValue = Text
        goto('L208')
        
        # Label 46
        ReturnValue_0: int32 = Default__FGSaveSession.GetVersion(Ref[self.mSaveHeader])
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_0, False, True, 1, 324)
        Text: FText = ReturnValue_1
        goto('L14')
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SaveListRow(10)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_2_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SaveListRow(100)
    

    def BndEvt__Button_1_K2Node_ComponentBoundEvent_1_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SaveListRow(210)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_3_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SaveListRow(229)
    

    def OnWorldSave(self, WasSuccessful: bool, errorMessage: Const[Ref[FText]]):
        ExecuteUbergraph_Widget_SaveListRow.K2Node_CustomEvent_WasSuccessful = WasSuccessful #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_SaveListRow.K2Node_CustomEvent_errorMessage = errorMessage #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SaveListRow(597)
    

    def ConfirmDeleteSessionPopUp(self):
        self.ExecuteUbergraph_Widget_SaveListRow(1082)
    

    def DeleteSave(self, confirmed: bool):
        ExecuteUbergraph_Widget_SaveListRow.K2Node_CustomEvent_confirmed = confirmed #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SaveListRow(1241)
    

    def BndEvt__mSaveRowButton_K2Node_ComponentBoundEvent_4_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SaveListRow(1623)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SaveListRow(1628)
    

    def OnDeleteSaveDone(self, success: bool):
        ExecuteUbergraph_Widget_SaveListRow.K2Node_CustomEvent_success = success #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SaveListRow(1961)
    

    def ExecuteUbergraph_Widget_SaveListRow(self):
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_MouseOver, ReturnValue1, True)
        # End
        # Label 100
        self.OnClicked.ProcessMulticastDelegate(self)
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Click, ReturnValue, True)
        # End
        self.ConfirmDeleteSessionPopUp()
        # End
        ReturnValue5: Ptr[PlayerController] = self.GetOwningPlayer()
        Base1: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue5)
        bSuccess1: bool = Base1
        # Label 318
        if not bSuccess1:
            goto('L2011')
        ReturnValue1_1: Ptr[FGAdminInterface] = Base1.GetAdminInterface()
        ReturnValue1_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_1)
        if not ReturnValue1_2:
            goto('L2011')
        OutputDelegate.BindUFunction(self, OnWorldSave)
        
        desiredFileName1 = None
        self.GetDesiredFileName(Ref[desiredFileName1])
        ReturnValue1_1 = Base1.GetAdminInterface()
        ReturnValue1_1.SaveGame(False, desiredFileName1, OutputDelegate)
        # End
        self.mSaveList.RefreshSaveList()
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 653, 'Value': 'Your game was saved!'}"
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 731, 'Value': 'Save Failed!'}"
        Variable2: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 801, 'Value': 'Save Successful!'}"
        Variable_0: bool = WasSuccessful
        Variable1_0: bool = WasSuccessful
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        
        switch = {
            False: Variable1,
            True: Variable2
        }
        
        switch_0 = {
            False: errorMessage,
            True: Variable
        }
        
        Variable_1 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue2, switch.get(Variable_0, None), switch_0.get(Variable1_0, None), 0, None, None, Ref[Variable_1])
        # End
        OutputDelegate2.BindUFunction(self, DeleteSave)
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        
        OutputDelegate2 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue3, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1171, 'Value': 'Delete Save'}", , 1, None, None, Ref[OutputDelegate2])
        # End
        if not confirmed:
            goto('L2011')
        ReturnValue4: Ptr[PlayerController] = self.GetOwningPlayer()
        Base: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue4)
        bSuccess: bool = Base
        if not bSuccess:
            goto('L2011')
        ReturnValue_1: Ptr[FGAdminInterface] = Base.GetAdminInterface()
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_1)
        if not ReturnValue_2:
            goto('L2011')
        OutputDelegate1.BindUFunction(self, OnDeleteSaveDone)
        
        desiredFileName = None
        self.GetDesiredFileName(Ref[desiredFileName])
        ReturnValue_1 = Base.GetAdminInterface()
        ReturnValue_1.DeleteSaveFile(False, desiredFileName, OutputDelegate1)
        # End
        # End
        
        ReturnValue_3: FString = Default__FGSaveSession.GetName(Ref[self.mSaveHeader])
        ReturnValue_4: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_3)
        self.mTitle.SetText(ReturnValue_4)
        
        ReturnValue_5: DateTime = Default__FGSaveSession.GetSaveDateTime(Ref[self.mSaveHeader])
        
        ReturnValue_6: FText = Default__KismetTextLibrary.AsTimeZoneDateTime_DateTime("", Ref[ReturnValue_5])
        self.Date.SetText(ReturnValue_6)
        # End
        if not success:
            goto('L2011')
        self.mSaveList.RefreshSaveList()
    

    def OnClicked__DelegateSignature(self, clickedRow: Ptr[Widget_SaveListRow]):
        pass
    
