
from codegen.ue4_stub import *

from Script.UMG import AddChild
from Script.FactoryGame import SaveHeader
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.Engine import FormatArgumentData
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveList import ExecuteUbergraph_Widget_SaveList.K2Node_CustomEvent_WasSuccessful
from Script.UMG import ESlateVisibility
from Script.UMG import SetText
from Script.FactoryGame import SortSaves
from Script.Engine import IsValid
from Script.FactoryGame import Default__FGSaveSystem
from Script.Engine import EqualEqual_StrStr
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.Engine import NotEqual_StrStr
from Script.UMG import GetText
from Script.Engine import Default__KismetStringLibrary
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveList import ExecuteUbergraph_Widget_SaveList.K2Node_ComponentBoundEvent_Text
from Script.UMG import ScrollToStart
from Script.Engine import NotEqual_ObjectObject
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import Create
from Script.Engine import GetGameState
from Script.FactoryGame import AddPopupWithCloseDelegate
from Script.Engine import Array_Clear
from Game.FactoryGame.Interface.UI.Menu.Widget_SessionRow import Widget_SessionRow
from Script.Engine import EqualEqual_ByteByte
from Script.Engine import SetObjectPropertyByName
from Script.UMG import GetChildrenCount
from Script.UMG import AddChildToVerticalBox
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveList import ExecuteUbergraph_Widget_SaveList.K2Node_CustomEvent_errorMessage
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import BP_MenuBase
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveList import ExecuteUbergraph_Widget_SaveList.K2Node_ComponentBoundEvent_Text1
from Script.FactoryGame import ESaveExists
from Script.FactoryGame import FGGameState
from Script.FactoryGame import GetSaveSessionName
from Script.Engine import Conv_IntToString
from Script.Engine import NotEqual_ByteByte
from Script.FactoryGame import EnumerateSaveGames
from Script.FactoryGame import GetName
from Script.FactoryGame import DeleteSaveFile
from Script.UMG import VerticalBoxSlot
from Script.FactoryGame import Default__FGSaveSession
from Script.FactoryGame import GetSessionName
from Script.FactoryGame import GetAdminInterface
from Script.Engine import GetSubstring
from Script.Engine import Delay
from Script.UMG import PanelSlot
from Script.Engine import LatentActionInfo
from Script.Engine import PlayerController
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import OnMenuEnter
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Replace
from Script.Engine import Now
from Script.Engine import SetBoolPropertyByName
from Script.Engine import Default__GameplayStatics
from Script.CoreUObject import DateTime
from Script.FactoryGame import SessionSaveStruct
from Script.FactoryGame import FGPlayerControllerBase
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveList import ExecuteUbergraph_Widget_SaveList
from Script.Engine import Format
from Script.Engine import EqualEqual_ObjectObject
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveList import ExecuteUbergraph_Widget_SaveList.K2Node_Event_prevMenu
from Script.FactoryGame import SortSessions
from Script.FactoryGame import SaveGame
from Script.Engine import Conv_TextToString
from Script.UMG import ScrollWidgetIntoView
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveListRow import Widget_SaveListRow
from Script.Engine import Len
from Script.FactoryGame import GetCachedSaveExists
from Script.UMG import Widget
from Game.FactoryGame.Interface.UI.Menu.Widget_SaveList import ExecuteUbergraph_Widget_SaveList.K2Node_ComponentBoundEvent_CommitMethod
from Script.FactoryGame import FGAdminInterface
from Script.Engine import BreakDateTime
from Script.FactoryGame import GroupSavesPerSession
from Script.Engine import Concat_StrStr

class Widget_SaveList(BP_MenuBase):
    mSaveRows: List[Ptr[Widget_SaveListRow]]
    mSelectedSave: Ptr[Widget_SaveListRow]
    mNewSaveGameSlot: Ptr[Widget_SaveListRow]
    OnSaveClicked: FMulticastScriptDelegate
    OnBackClicked: FMulticastScriptDelegate
    mCachedSaves: List[SaveHeader]
    
    def OnSaveFileDeleted(self, success: bool):
        if not success:
            goto('L42')
        self.RefreshSaveList()
        self.PopulateSessions()
    

    def OnSavesUpdated(self, success: bool, saves: Ref[List[SaveHeader]]):
        ExecutionFlow.Push("L915")
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mSaveRows])
        self.ClearSaves()
        self.mCachedSaves = saves
        
        Default__FGSaveSystem.SortSaves(1, 1, Ref[self.mCachedSaves])
        if not success:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L788")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 193
        ReturnValue: int32 = len(self.mCachedSaves)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L803')
        Variable_0 = Variable
        ExecutionFlow.Push("L841")
        
        Item = None
        Item = self.mCachedSaves[Variable_0]
        
        Item = None
        ReturnValue_1: FString = Default__FGSaveSession.GetSessionName(Ref[Item])
        ReturnValue_2: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue_2)
        bSuccess: bool = State
        ReturnValue1: FString = State.GetSessionName()
        ReturnValue_3: bool = Default__KismetStringLibrary.EqualEqual_StrStr(ReturnValue_1, ReturnValue1)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = self.mCachedSaves[Variable_0]
        
        rowWidget = None
        self.AddSaveGame(Item, Ref[rowWidget])
        goto(ExecutionFlow.Pop())
        # Label 788
        self.PopulateSessions()
        goto(ExecutionFlow.Pop())
        # Label 803
        self.mSaves.OnSpawnAnim(None)
        goto(ExecutionFlow.Pop())
        # Label 841
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L193')
    

    def GetSaveErrorMessage(self, saveFileExists: uint8):
        Variable: uint8 = saveFileExists
        Variable_0: FText = STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/SaveTable.SaveTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 112, 'Value': 'OverwriteSaveGameExistsInOtherSession'}"
        Variable1: FText = STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/SaveTable.SaveTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 236, 'Value': 'OverwriteSaveGameExistsInSameSession'}"
        Variable2: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 294, 'Value': 'Invalid Value'}"
        
        switch = {
            0: Variable2,
            1: Variable1,
            2: Variable_0
        }
        errorMessage = switch.get(Variable, None)
    

    def ConvertIntToTwoDidgitText(self, int: int32):
        ReturnValue: bool = int <= 10
        ReturnValue_0: FString = Default__KismetStringLibrary.Conv_IntToString(int)
        Variable: bool = ReturnValue
        # Label 112
        ReturnValue_1: FString = Default__KismetStringLibrary.Concat_StrStr("0", ReturnValue_0)
        
        switch = {
            False: ReturnValue_0,
            True: ReturnValue_1
        }
        # Label 174
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_StringToText(switch.get(Variable, None))
        ReturnValue_3: FText = ReturnValue_2
    

    def ClearSaves(self):
        ExecutionFlow.Push("L647")
        ReturnValue: int32 = self.mSavesVbox.GetChildrenCount()
        ReturnValue_0: bool = ReturnValue > 0
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ReturnValue = self.mSavesVbox.GetChildrenCount()
        ReturnValue1: int32 = ReturnValue - 1
        TempChildCount = ReturnValue1
        Variable: int32 = 0
        # Label 241
        ReturnValue_1: bool = Variable <= TempChildCount
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L573")
        ReturnValue_2: int32 = TempChildCount - Variable
        ReturnValue_3: Ptr[Widget] = self.mSavesVbox.GetChildAt(ReturnValue_2)
        ReturnValue_4: bool = NotEqual_ObjectObject(ReturnValue_3, self.Widget_SaveInputBox)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        ReturnValue_2 = TempChildCount - Variable
        ReturnValue_3 = self.mSavesVbox.GetChildAt(ReturnValue_2)
        ReturnValue_3.RemoveFromParent()
        goto(ExecutionFlow.Pop())
        # Label 573
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L241')
    

    def PopulateSessions(self):
        ExecutionFlow.Push("L1619")
        self.mSessionsVbox.ClearChildren()
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_SessionRow] = Default__WidgetBlueprintLibrary.Create(self, Widget_SessionRow, ReturnValue)
        
        SessionSaveStruct = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_0, "mSaveSession", Ref[SessionSaveStruct])
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_0, "mSetButtonInfoToCurrentSession", True)
        ReturnValue_1: Ptr[VerticalBoxSlot] = self.mSessionsVbox.AddChildToVerticalBox(ReturnValue_0)
        NewSession = ReturnValue_0
        groupedBySession: List[SessionSaveStruct] = []
        
        Default__FGSaveSystem.GroupSavesPerSession(Ref[self.mCachedSaves], Ref[groupedBySession])
        
        Default__FGSaveSystem.SortSessions(1, 1, Ref[groupedBySession])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 466
        ReturnValue_2: int32 = len(groupedBySession)
        ReturnValue_3: bool = Variable <= ReturnValue_2
        if not ReturnValue_3:
            goto('L1328')
        Variable_0 = Variable
        ExecutionFlow.Push("L1508")
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[Widget_SessionRow] = Default__WidgetBlueprintLibrary.Create(self, Widget_SessionRow, ReturnValue1)
        
        Item = None
        Item = groupedBySession[Variable_0]
        
        Item = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue1_0, "mSaveSession", Ref[Item])
        ReturnValue1_1: Ptr[VerticalBoxSlot] = self.mSessionsVbox.AddChildToVerticalBox(ReturnValue1_0)
        
        Item = None
        Item = groupedBySession[Variable_0]
        
        Item = None
        ReturnValue_4: FString = Default__FGSaveSession.GetSaveSessionName(Ref[Item])
        ReturnValue_5: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue_5)
        bSuccess: bool = State
        ReturnValue_6: FString = State.GetSessionName()
        ReturnValue_7: bool = Default__KismetStringLibrary.EqualEqual_StrStr(ReturnValue_4, ReturnValue_6)
        if not ReturnValue_7:
            goto('L1582')
        ReturnValue1_0.isSelected = True
        SessionFound = True
        self.mSessionsScrollbox.mScrollBox.ScrollWidgetIntoView(ReturnValue1_0, False, 0)
        goto(ExecutionFlow.Pop())
        # Label 1328
        if not SessionFound:
            goto('L1416')
        NewSession.RemoveFromParent()
        # Label 1378
        self.mSessions.OnSpawnAnim(None)
        goto(ExecutionFlow.Pop())
        # Label 1416
        NewSession.isSelected = True
        self.mSessionsScrollbox.mScrollBox.ScrollToStart()
        goto('L1378')
        # Label 1508
        ReturnValue_8: int32 = Variable + 1
        Variable = ReturnValue_8
        goto('L466')
        # Label 1582
        ReturnValue1_0.SetDisabled()
        goto(ExecutionFlow.Pop())
    

    def DeleteSaveGame(self, confirm: bool):
        ExecutionFlow.Push("L422")
        ExecutionFlow.Push("L384")
        if not confirm:
           goto(ExecutionFlow.Pop())
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Base: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue)
        bSuccess: bool = Base
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_0: Ptr[FGAdminInterface] = Base.GetAdminInterface()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        OutputDelegate.BindUFunction(self, OnSaveFileDeleted)
        ReturnValue_0 = Base.GetAdminInterface()
        
        desiredFileName = None
        self.mSelectedSave.GetDesiredFileName(Ref[desiredFileName])
        ReturnValue_0.DeleteSaveFile(False, desiredFileName, OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 384
        self.mOwningMenu.RestoreFocusOnPopupClosed(False)
        goto(ExecutionFlow.Pop())
    

    def GetDeleteButtonVisibility(self):
        Variable: uint8 = 2
        Variable1: uint8 = 0
        ReturnValue: bool = EqualEqual_ObjectObject(self.mSelectedSave, self.mNewSaveGameSlot)
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_0: uint8 = switch.get(Variable_0, None)
    

    def SaveGame(self, Confrim: bool):
        ExecutionFlow.Push("L475")
        ExecutionFlow.Push("L437")
        if not Confrim:
           goto(ExecutionFlow.Pop())
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Base: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue)
        bSuccess: bool = Base
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_0: Ptr[FGAdminInterface] = Base.GetAdminInterface()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        OutputDelegate.BindUFunction(self, OnWorldSave)
        ReturnValue_0 = Base.GetAdminInterface()
        
        saveName = None
        self.GetDesiredSaveGameName(Ref[saveName])
        ReturnValue_0.SaveGame(False, saveName, OutputDelegate)
        self.Widget_SaveInputBox.mSaveInputBox.SetText()
        self.OnSaveClicked.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
        # Label 437
        self.mOwningMenu.RestoreFocusOnPopupClosed(False)
        goto(ExecutionFlow.Pop())
    

    def GetSaveButtonVisibility(self):
        Variable: uint8 = 0
        Variable1: uint8 = 1
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mSelectedSave)
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_0: uint8 = switch.get(Variable_0, None)
    

    def GetDesiredSaveGameName(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mSelectedSave)
        if not ReturnValue:
            goto('L178')
        
        self.mSelectedSave.mSaveHeader = None
        ReturnValue_0: FString = Default__FGSaveSession.GetName(Ref[self.mSelectedSave.mSaveHeader])
        saveName = ReturnValue_0
        # End
        # Label 178
        ReturnValue_1: DateTime = Now()
        
        Year = None
        Month = None
        Day = None
        Hour = None
        Minute = None
        Second = None
        Millisecond = None
        BreakDateTime(ReturnValue_1, Ref[Year], Ref[Month], Ref[Day], Ref[Hour], Ref[Minute], Ref[Second], Ref[Millisecond])
        ReturnValue_2: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_3: FText = self.ConvertIntToTwoDidgitText(Second)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue_2)
        bSuccess: bool = State
        # Label 437
        FormatArgumentData.ArgumentName = "Second"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_3
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue_4: FString = State.GetSessionName()
        ReturnValue1: FText = self.ConvertIntToTwoDidgitText(Minute)
        ReturnValue_5: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_4)
        FormatArgumentData1.ArgumentName = "Minute"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue1
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        FormatArgumentData2.ArgumentName = "SaveName"
        FormatArgumentData2.ArgumentValueType = 4
        FormatArgumentData2.ArgumentValue = ReturnValue_5
        FormatArgumentData2.ArgumentValueInt = 0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        ReturnValue2: FText = self.ConvertIntToTwoDidgitText(Hour)
        ReturnValue3: FText = self.ConvertIntToTwoDidgitText(Day)
        FormatArgumentData3.ArgumentName = "Hour"
        FormatArgumentData3.ArgumentValueType = 4
        FormatArgumentData3.ArgumentValue = ReturnValue2
        FormatArgumentData3.ArgumentValueInt = 0
        FormatArgumentData3.ArgumentValueFloat = 0
        FormatArgumentData3.ArgumentValueGender = 0
        FormatArgumentData4.ArgumentName = "Day"
        FormatArgumentData4.ArgumentValueType = 4
        FormatArgumentData4.ArgumentValue = ReturnValue3
        FormatArgumentData4.ArgumentValueInt = 0
        FormatArgumentData4.ArgumentValueFloat = 0
        FormatArgumentData4.ArgumentValueGender = 0
        ReturnValue4: FText = self.ConvertIntToTwoDidgitText(Month)
        ReturnValue_6: FString = Default__KismetStringLibrary.Conv_IntToString(Year)
        FormatArgumentData5.ArgumentName = "Month"
        FormatArgumentData5.ArgumentValueType = 4
        FormatArgumentData5.ArgumentValue = ReturnValue4
        FormatArgumentData5.ArgumentValueInt = 0
        FormatArgumentData5.ArgumentValueFloat = 0
        FormatArgumentData5.ArgumentValueGender = 0
        ReturnValue_7: FString = Default__KismetStringLibrary.Replace(ReturnValue_6, "20", "", 1)
        ReturnValue1_0: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_7)
        FormatArgumentData6.ArgumentName = "Year"
        FormatArgumentData6.ArgumentValueType = 4
        FormatArgumentData6.ArgumentValue = ReturnValue1_0
        FormatArgumentData6.ArgumentValueInt = 0
        FormatArgumentData6.ArgumentValueFloat = 0
        FormatArgumentData6.ArgumentValueGender = 0
        ReturnValue_8: FText = self.Widget_SaveInputBox.mSaveInputBox.GetText()
        Array: List[FormatArgumentData] = [FormatArgumentData2, FormatArgumentData4, FormatArgumentData5, FormatArgumentData6, FormatArgumentData3, FormatArgumentData1, FormatArgumentData]
        
        ReturnValue_9: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_8])
        ReturnValue_10: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2496, 'Value': '{SaveName}_{Day}{Month}{Year}-{Hour}{Minute}{Second}'}", Array)
        ReturnValue_11: bool = Default__KismetStringLibrary.NotEqual_StrStr(ReturnValue_9, "")
        
        ReturnValue1_1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_10])
        Variable: bool = ReturnValue_11
        
        switch = {
            False: ReturnValue1_1,
            True: ReturnValue_9
        }
        saveName = switch.get(Variable, None)
    

    def AddNewSaveSlot(self):
        
        newRow = None
        self.AddNewSaveGame(Ref[newRow])
    

    def RefreshSaveList(self):
        self.mSelectedSave = None
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mSaveRows])
        self.ClearSaves()
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Base: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue)
        bSuccess: bool = Base
        if not bSuccess:
            goto('L397')
        ReturnValue_0: Ptr[FGAdminInterface] = Base.GetAdminInterface()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L397')
        OutputDelegate.BindUFunction(self, OnSavesUpdated)
        ReturnValue_0 = Base.GetAdminInterface()
        ReturnValue_0.EnumerateSaveGames(False, OutputDelegate)
    

    def InternalSetupSaveGame(self, saveRow: Ptr[Widget_SaveListRow]):
        ReturnValue: Ptr[PanelSlot] = self.mSavesVbox.AddChild(saveRow)
        OutputDelegate.BindUFunction(self, OnSaveClickedEvent)
        saveRow.OnClicked.AddUnique(OutputDelegate)
        
        ReturnValue_0: int32 = self.mSaveRows.append(saveRow)
    

    def InternalAddSaveGame(self, Header: SaveHeader, isNewGame: bool):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Widget_SaveListRow] = Default__WidgetBlueprintLibrary.Create(self, Widget_SaveListRow, ReturnValue)
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_0, "mSaveHeader", Ref[Header])
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_0, "mIsNewSave", isNewGame)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_0, "mSaveList", self)
        self.InternalSetupSaveGame(ReturnValue_0)
        saveRow = ReturnValue_0
    

    def AddNewSaveGame(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mNewSaveGameSlot)
        if not ReturnValue:
            goto('L112')
        self.InternalSetupSaveGame(self.mNewSaveGameSlot)
        newRow = self.mNewSaveGameSlot
        # End
        
        saveRow = None
        # Label 112
        self.InternalAddSaveGame(SaveHeader(), True, Ref[saveRow])
        self.mNewSaveGameSlot = saveRow
        newRow = self.mNewSaveGameSlot
    

    def OnSaveClickedEvent(self, clickedSave: Ptr[Widget_SaveListRow]):
        ExecutionFlow.Push("L531")
        ReturnValue: bool = NotEqual_ObjectObject(clickedSave, self.mSelectedSave)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        self.mSelectedSave = clickedSave
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 118
        ReturnValue_0: int32 = len(self.mSaveRows)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L457")
        
        Item = None
        Item = self.mSaveRows[Variable_0]
        ReturnValue1: bool = NotEqual_ObjectObject(Item, self.mSelectedSave)
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = self.mSaveRows[Variable_0]
        Item.mIsSelected = False
        goto(ExecutionFlow.Pop())
        # Label 457
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L118')
    

    def AddSaveGame(self, SaveHeader: SaveHeader):
        
        saveRow = None
        self.InternalAddSaveGame(SaveHeader, False, Ref[saveRow])
        rowWidget = saveRow
    

    def BndEvt__mDeleteButton_K2Node_ComponentBoundEvent_6_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SaveList(251)
    

    def OnEscape(self):
        self.ExecuteUbergraph_Widget_SaveList(266)
    

    def ConfirmDeleteSessionPopUp(self):
        self.ExecuteUbergraph_Widget_SaveList(303)
    

    def ConfirmOverwriteSavePopup(self):
        self.ExecuteUbergraph_Widget_SaveList(782)
    

    def OnWorldSave(self, WasSuccessful: bool, errorMessage: Const[Ref[FText]]):
        ExecuteUbergraph_Widget_SaveList.K2Node_CustomEvent_WasSuccessful = WasSuccessful #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_SaveList.K2Node_CustomEvent_errorMessage = errorMessage #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SaveList(1690)
    

    def BndEvt__Widget_SaveInputBox_K2Node_ComponentBoundEvent_7_OnTextCommited__DelegateSignature(self, text: FText, CommitMethod: uint8):
        ExecuteUbergraph_Widget_SaveList.K2Node_ComponentBoundEvent_Text1 = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_SaveList.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SaveList(2533)
    

    def BndEvt__Widget_SaveInputBox_K2Node_ComponentBoundEvent_9_OnTextChanged__DelegateSignature(self, text: FText):
        ExecuteUbergraph_Widget_SaveList.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SaveList(2589)
    

    def BndEvt__Widget_FrontEnd_Button_K2Node_ComponentBoundEvent_11_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SaveList(2756)
    

    def BndEvt__mDeleteSaveButton_K2Node_ComponentBoundEvent_12_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SaveList(2761)
    

    def BndEvt__Widget_SaveInputBox_K2Node_ComponentBoundEvent_13_OnFocused__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SaveList(2776)
    

    def OnMenuEnter(self):
        ExecuteUbergraph_Widget_SaveList.K2Node_Event_prevMenu = prevMenu #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SaveList(2804)
    

    def ExecuteUbergraph_Widget_SaveList(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        adminInterface = None
        Default__HUDHelpers.GetAdminInterface(ReturnValue, self, Ref[adminInterface])
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(adminInterface)
        if not ReturnValue_0:
            goto('L174')
        self.RefreshSaveList()
        goto(ExecutionFlow.Pop())
        # Label 174
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 15, UUID = -876024115, ExecutionFunction = "ExecuteUbergraph_Widget_SaveList", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.ConfirmDeleteSessionPopUp()
        goto(ExecutionFlow.Pop())
        self.mOwningMenu.OnEscape()
        goto(ExecutionFlow.Pop())
        OutputDelegate.BindUFunction(self, DeleteSaveGame)
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        OutputDelegate = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue1, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 392, 'Value': 'Delete Save'}", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 443, 'Value': 'Are you sure you want to delete this save file?'}", 1, None, None, Ref[OutputDelegate])
        goto(ExecutionFlow.Pop())
        # Label 543
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(self.mNewSaveGameSlot)
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        
        Text = None
        ReturnValue_1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Text])
        ReturnValue_2: FString = Default__KismetStringLibrary.GetSubstring(ReturnValue_1, 0, 25)
        self.mNewSaveGameSlot.mNewSaveFileName = ReturnValue_2
        goto(ExecutionFlow.Pop())
        
        saveName = None
        self.GetDesiredSaveGameName(Ref[saveName])
        ReturnValue_3: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue_3)
        bSuccess: bool = State
        ReturnValue_4: FString = State.GetSessionName()
        
        ReturnValue_5: uint8 = Default__FGSaveSystem.GetCachedSaveExists(saveName, ReturnValue_4, Ref[self.mCachedSaves])
        CmpSuccess: bool = NotEqual_ByteByte(ReturnValue_5, 0)
        if not CmpSuccess:
            goto('L1176')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_5, 1)
        if not CmpSuccess:
            goto('L1192')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_5, 2)
        if not CmpSuccess:
            goto('L1192')
        goto(ExecutionFlow.Pop())
        # Label 1176
        self.SaveGame(True)
        goto(ExecutionFlow.Pop())
        # Label 1192
        OutputDelegate1.BindUFunction(self, SaveGame)
        
        saveName = None
        self.GetDesiredSaveGameName(Ref[saveName])
        ReturnValue_3 = Default__GameplayStatics.GetGameState(self)
        State = Cast[FGGameState](ReturnValue_3)
        bSuccess = State
        ReturnValue_4 = State.GetSessionName()
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        
        ReturnValue_5 = Default__FGSaveSystem.GetCachedSaveExists(saveName, ReturnValue_4, Ref[self.mCachedSaves])
        
        errorMessage = None
        self.GetSaveErrorMessage(ReturnValue_5, Ref[errorMessage])
        
        OutputDelegate1 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue2, STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/SaveTable.SaveTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1636, 'Value': 'OverwriteSave'}", errorMessage, 1, None, None, Ref[OutputDelegate1])
        goto(ExecutionFlow.Pop())
        # Label 1675
        self.ConfirmOverwriteSavePopup()
        goto(ExecutionFlow.Pop())
        self.RefreshSaveList()
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1724, 'Value': 'Save Successful!'}"
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1798, 'Value': 'Save Failed!'}"
        Variable_0: bool = WasSuccessful
        Variable2: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1887, 'Value': 'Your game was saved!'}"
        Variable1_0: bool = WasSuccessful
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        OutputDelegate2.BindUFunction(self.mOwningMenu, RestoreFocusOnPopupClosed)
        
        switch = {
            False: Variable1,
            True: Variable
        }
        
        switch_0 = {
            False: errorMessage,
            True: Variable2
        }
        
        OutputDelegate2 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue3, switch.get(Variable_0, None), switch_0.get(Variable1_0, None), 0, None, None, Ref[OutputDelegate2])
        goto(ExecutionFlow.Pop())
        # Label 2180
        ExecutionFlow.Push("L2345")
        ReturnValue_6: Ptr[Widget] = self.mSavesVbox.GetChildAt(Variable_1)
        Row: Ptr[Widget_SaveListRow] = Cast[Widget_SaveListRow](ReturnValue_6)
        bSuccess1: bool = Row
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Row.mIsSelected = False
        goto(ExecutionFlow.Pop())
        # Label 2345
        ReturnValue_7: int32 = Variable_1 + 1
        Variable_1: int32 = ReturnValue_7
        # Label 2414
        ReturnValue_8: int32 = self.mSavesVbox.GetChildrenCount()
        ReturnValue_9: bool = Variable_1 <= ReturnValue_8
        if not ReturnValue_9:
            goto('L2521')
        goto('L2180')
        # Label 2521
        self.mSelectedSave = None
        goto(ExecutionFlow.Pop())
        ReturnValue_10: bool = EqualEqual_ByteByte(CommitMethod, 1)
        if not ReturnValue_10:
           goto(ExecutionFlow.Pop())
        self.ConfirmOverwriteSavePopup()
        goto(ExecutionFlow.Pop())
        
        Text = None
        ReturnValue_1 = Default__KismetTextLibrary.Conv_TextToString(Ref[Text])
        ReturnValue_11: int32 = Default__KismetStringLibrary.Len(ReturnValue_1)
        ReturnValue_12: bool = ReturnValue_11 <= 25
        if not ReturnValue_12:
           goto(ExecutionFlow.Pop())
        goto('L543')
        goto('L1675')
        self.ConfirmDeleteSessionPopUp()
        goto(ExecutionFlow.Pop())
        Variable_1 = 0
        goto('L2414')
        self.OnMenuEnter(prevMenu)
        goto('L15')
    

    def OnBackClicked__DelegateSignature(self):
        pass
    

    def OnSaveClicked__DelegateSignature(self):
        pass
    
