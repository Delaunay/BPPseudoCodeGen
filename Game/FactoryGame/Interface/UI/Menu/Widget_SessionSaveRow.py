
from codegen.ue4_stub import *

from Script.UMG import GetParent
from Script.AkAudio import PostAkEvent
from Script.Engine import AsTimeZoneDateTime_DateTime
from Script.UMG import GetChildrenCount
from Script.CoreUObject import Timespan
from Script.Engine import Not_PreBool
from Script.Engine import MakeTimespan
from Script.FactoryGame import SaveHeader
from Game.FactoryGame.Interface.UI.Menu.Widget_SessionSaveRow import Widget_SessionSaveRow
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.UMG import GetRenderOpacity
from Game.FactoryGame.Interface.UI.Menu.Widget_SessionSaveRow import ExecuteUbergraph_Widget_SessionSaveRow.K2Node_CustomEvent_Confirm
from Script.Engine import PlayerController
from Script.FactoryGame import GetAdminInterface
from Script.UMG import PlayAnimation
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetSaveDateTime
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_MouseOver import Play_UI_MainMenu_MouseOver
from Script.UMG import ESlateVisibility
from Script.Engine import IsValid
from Script.FactoryGame import Default__FGSaveSystem
from Script.Engine import EqualEqual_StrStr
from Game.FactoryGame.Interface.UI.Menu.Widget_SessionSaveRow import ExecuteUbergraph_Widget_SessionSaveRow
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Game.FactoryGame.Interface.UI.Menu.Widget_SessionSaveRow import ExecuteUbergraph_Widget_SessionSaveRow.K2Node_CustomEvent_success
from Script.FactoryGame import ESaveState
from Script.CoreUObject import DateTime
from Game.FactoryGame.Interface.UI.Menu.Widget_LoadSession import Widget_LoadSession
from Script.UMG import Widget
from Script.FactoryGame import FGPlayerControllerBase
from Script.Engine import BreakTimespan
from Script.UMG import PanelWidget
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.Menu.Widget_SessionSaveRow import ExecuteUbergraph_Widget_SessionSaveRow.K2Node_Event_IsDesignTime
from Script.FactoryGame import GetSaveState
from Script.Engine import Default__KismetStringLibrary
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import NotEqual_ByteByte
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.UMG import UserWidget
from Script.FactoryGame import GetName
from Script.Engine import NotEqual_ObjectObject
from Script.FactoryGame import FGAdminInterface
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import DeleteSaveFile
from Script.Engine import SelectColor
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import Default__FGSaveSession
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_Click import Play_UI_MainMenu_Click
from Script.FactoryGame import AddPopupWithCloseDelegate
from Script.SlateCore import SlateColor
from Script.AkAudio import AkComponent
from Script.FactoryGame import GetPlayDurationSeconds
from Script.CoreUObject import LinearColor

class Widget_SessionSaveRow(UserWidget):
    mSaveHeader: SaveHeader
    LoadSessionWidget: Ptr[Widget_LoadSession]
    mCurrentSave: SaveHeader
    mIsSelected: bool
    
    def SetSelected(self, isSelected: bool):
        ExecutionFlow.Push("L912")
        self.mIsSelected = isSelected
        if not self.mIsSelected:
            goto('L457')
        self.LoadSessionWidget.mCurrentSave = self.mCurrentSave
        Variable: int32 = 0
        # Label 110
        ReturnValue: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_0: int32 = ReturnValue.GetChildrenCount()
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L602')
        ExecutionFlow.Push("L838")
        ReturnValue = self.GetParent()
        ReturnValue_2: Ptr[Widget] = ReturnValue.GetChildAt(Variable)
        Row: Ptr[Widget_SessionSaveRow] = Cast[Widget_SessionSaveRow](ReturnValue_2)
        bSuccess: bool = Row
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_3: bool = NotEqual_ObjectObject(Row, self)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Row.mIsSelected = False
        goto(ExecutionFlow.Pop())
        # Label 457
        self.LoadSessionWidget.mCurrentSave = SaveHeader()
        ReturnValue_4: Ptr[UMGSequencePlayer] = self.LoadSessionWidget.PlayAnimation(self.LoadSessionWidget.ShowLoadDeleteButtons, 0, 1, 1, 1)
        goto(ExecutionFlow.Pop())
        # Label 602
        ReturnValue_5: float = self.LoadSessionWidget.LoadSave.GetRenderOpacity()
        ReturnValue_6: bool = ReturnValue_5 > 0
        ReturnValue_7: bool = Not_PreBool(ReturnValue_6)
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        ReturnValue1: Ptr[UMGSequencePlayer] = self.LoadSessionWidget.PlayAnimation(self.LoadSessionWidget.ShowLoadDeleteButtons, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 838
        ReturnValue_8: int32 = Variable + 1
        Variable = ReturnValue_8
        goto('L110')
    

    def GetIconColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        
        # Label 110
        ReturnValue: FString = Default__FGSaveSession.GetName(Ref[self.mSaveHeader])
        
        self.LoadSessionWidget.mCurrentSave = None
        ReturnValue1: FString = Default__FGSaveSession.GetName(Ref[self.LoadSessionWidget.mCurrentSave])
        ReturnValue_0: bool = Default__KismetStringLibrary.EqualEqual_StrStr(ReturnValue, ReturnValue1)
        ReturnValue_1: bool = self.mSaveRowButton.IsHovered()
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue_2: LinearColor = SelectColor(Orange, GraphicsWhite, ReturnValue_0)
        ReturnValue1_0: LinearColor = SelectColor(Graphics, ReturnValue_2, ReturnValue_1)
        ReturnValue_3: LinearColor = ReturnValue1_0
    

    def GetTextColor(self):
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        
        ReturnValue: FString = Default__FGSaveSession.GetName(Ref[self.mSaveHeader])
        
        self.LoadSessionWidget.mCurrentSave = None
        ReturnValue1: FString = Default__FGSaveSession.GetName(Ref[self.LoadSessionWidget.mCurrentSave])
        ReturnValue_0: bool = Default__KismetStringLibrary.EqualEqual_StrStr(ReturnValue, ReturnValue1)
        ReturnValue_1: bool = self.mSaveRowButton.IsHovered()
        Variable: bool = ReturnValue_0
        Variable1: bool = ReturnValue_1
        
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
        ReturnValue_2: SlateColor = switch_0.get(Variable1, None)
    

    def GetPlayDurationTextColor(self):
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        
        ReturnValue: FString = Default__FGSaveSession.GetName(Ref[self.mSaveHeader])
        
        self.LoadSessionWidget.mCurrentSave = None
        ReturnValue1: FString = Default__FGSaveSession.GetName(Ref[self.LoadSessionWidget.mCurrentSave])
        ReturnValue_0: bool = Default__KismetStringLibrary.EqualEqual_StrStr(ReturnValue, ReturnValue1)
        ReturnValue_1: bool = self.mSaveRowButton.IsHovered()
        Variable: bool = ReturnValue_0
        Variable1: bool = ReturnValue_1
        
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
        ReturnValue_2: SlateColor = switch_0.get(Variable1, None)
    

    def GetIconBGColor(self):
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        
        TextWhite1 = None
        GraphicsWhite1 = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite1], Ref[GraphicsWhite1])
        
        # Label 110
        ReturnValue: FString = Default__FGSaveSession.GetName(Ref[self.mSaveHeader])
        
        self.LoadSessionWidget.mCurrentSave = None
        ReturnValue1: FString = Default__FGSaveSession.GetName(Ref[self.LoadSessionWidget.mCurrentSave])
        ReturnValue_0: bool = Default__KismetStringLibrary.EqualEqual_StrStr(ReturnValue, ReturnValue1)
        ReturnValue_1: bool = self.mSaveRowButton.IsHovered()
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue_2: LinearColor = SelectColor(GraphicsWhite, Orange, ReturnValue_0)
        ReturnValue1_0: LinearColor = SelectColor(GraphicsWhite1, ReturnValue_2, ReturnValue_1)
        ReturnValue_3: LinearColor = ReturnValue1_0
    

    def GetHoverColor(self):
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
        ReturnValue: LinearColor = SelectColor(Graphics, LinearColor, self.mIsSelected)
        ReturnValue_0: bool = self.mSaveRowButton.IsHovered()
        ReturnValue1: LinearColor = SelectColor(Orange, ReturnValue, ReturnValue_0)
        ReturnValue_1: LinearColor = ReturnValue1
    

    def GetPlayDuration(self):
        
        ReturnValue: int32 = Default__FGSaveSession.GetPlayDurationSeconds(Ref[self.mSaveHeader])
        ReturnValue_0: Timespan = MakeTimespan(0, 0, 0, ReturnValue, 0)
        
        Days = None
        Hours = None
        Minutes = None
        Seconds = None
        Milliseconds = None
        BreakTimespan(ReturnValue_0, Ref[Days], Ref[Hours], Ref[Minutes], Ref[Seconds], Ref[Milliseconds])
        ReturnValue_1: int32 = Days * 24
        FormatArgumentData.ArgumentName = "sec"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = Seconds
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue_2: int32 = ReturnValue_1 + Hours
        FormatArgumentData1.ArgumentName = "min"
        FormatArgumentData1.ArgumentValueType = 0
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = Minutes
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        FormatArgumentData2.ArgumentName = "hours"
        FormatArgumentData2.ArgumentValueType = 0
        FormatArgumentData2.ArgumentValue = 
        FormatArgumentData2.ArgumentValueInt = ReturnValue_2
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData2, FormatArgumentData1, FormatArgumentData]
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 920, 'Value': 'Play Duration: {hours}h {min}m {sec}s'}", Array)
        self.mPlayDuration.SetText(ReturnValue_3)
    

    def GetSaveTimeText(self):
        
        ReturnValue: DateTime = Default__FGSaveSession.GetSaveDateTime(Ref[self.mSaveHeader])
        
        ReturnValue_0: FText = Default__KismetTextLibrary.AsTimeZoneDateTime_DateTime("", Ref[ReturnValue])
        self.mSaveTime.SetText(ReturnValue_0)
    

    def GetSaveNameText(self):
        
        ReturnValue: FString = Default__FGSaveSession.GetName(Ref[self.mSaveHeader])
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue)
        self.mTitle.SetText(ReturnValue_0)
    

    def BndEvt__mSaveRowButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SessionSaveRow(15)
    

    def BndEvt__mSaveRowButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SessionSaveRow(143)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_SessionSaveRow.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SessionSaveRow(256)
    

    def BndEvt__mDeleteButton_K2Node_ComponentBoundEvent_3_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SessionSaveRow(537)
    

    def ConfirmDeleteSavePopUp(self):
        self.ExecuteUbergraph_Widget_SessionSaveRow(552)
    

    def Event DeleteSave(self, confirm: bool):
        ExecuteUbergraph_Widget_SessionSaveRow.K2Node_CustomEvent_Confirm = confirm #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SessionSaveRow(797)
    

    def BndEvt__mSaveRowButton_K2Node_ComponentBoundEvent_8_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SessionSaveRow(1250)
    

    def OnDeleteSaveDone(self, success: bool):
        ExecuteUbergraph_Widget_SessionSaveRow.K2Node_CustomEvent_success = success #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SessionSaveRow(1251)
    

    def ExecuteUbergraph_Widget_SessionSaveRow(self):
        goto(ComputedJump("EntryPoint"))
        self.mCurrentSave = self.mSaveHeader
        self.SetSelected(True)
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Click, ReturnValue, True)
        goto(ExecutionFlow.Pop())
        self.mCurrentSave = self.mSaveHeader
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_MouseOver, ReturnValue1, True)
        goto(ExecutionFlow.Pop())
        self.GetSaveNameText()
        self.GetSaveTimeText()
        self.GetPlayDuration()
        Variable: uint8 = 0
        Variable1: uint8 = 2
        
        ReturnValue_1: uint8 = Default__FGSaveSystem.GetSaveState(Ref[self.mSaveHeader])
        ReturnValue_2: bool = NotEqual_ByteByte(ReturnValue_1, 2)
        Variable_0: bool = ReturnValue_2
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mWarningIcon.SetVisibility(switch.get(Variable_0, None))
        goto(ExecutionFlow.Pop())
        self.ConfirmDeleteSavePopUp()
        goto(ExecutionFlow.Pop())
        OutputDelegate.BindUFunction(self, Event DeleteSave)
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        
        OutputDelegate = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue2, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 641, 'Value': 'Delete Save File'}", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 697, 'Value': 'Are you sure you want to delete this save file?'}", 1, None, None, Ref[OutputDelegate])
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1190")
        if not Confirm:
           goto(ExecutionFlow.Pop())
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        Base: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue3)
        bSuccess: bool = Base
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_3: Ptr[FGAdminInterface] = Base.GetAdminInterface()
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_3)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        
        ReturnValue_5: FString = Default__FGSaveSession.GetName(Ref[self.mCurrentSave])
        OutputDelegate1.BindUFunction(self, OnDeleteSaveDone)
        ReturnValue_3 = Base.GetAdminInterface()
        ReturnValue_3.DeleteSaveFile(False, ReturnValue_5, OutputDelegate1)
        goto(ExecutionFlow.Pop())
        # Label 1190
        self.LoadSessionWidget.mOwningMenu.RestoreFocusOnPopupClosed(False)
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        if not success:
           goto(ExecutionFlow.Pop())
        self.mCurrentSave = SaveHeader
        self.LoadSessionWidget.PopulateSessionList()
        self.LoadSessionWidget.UpdateCurrentSession()
        goto(ExecutionFlow.Pop())
    
