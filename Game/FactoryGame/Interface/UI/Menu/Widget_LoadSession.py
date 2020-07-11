
from codegen.ue4_stub import *

from Script.UMG import SetUserFocus
from Game.FactoryGame.Interface.UI.Menu.Widget_SessionRow import Widget_SessionRow
from Script.Engine import SetObjectPropertyByName
from Game.FactoryGame.Interface.UI.Menu.Widget_LoadSession import ExecuteUbergraph_Widget_LoadSession.K2Node_Event_prevMenu
from Script.UMG import AddChildToVerticalBox
from Script.UMG import GetChildrenCount
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.Engine import Not_PreBool
from Script.FactoryGame import SaveHeader
from Game.FactoryGame.Interface.UI.Menu.Widget_SessionSaveRow import Widget_SessionSaveRow
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import SetStructurePropertyByName
from Script.UMG import GetChildAt
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import DeleteSaveSession
from Script.Engine import FormatArgumentData
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import BP_MenuBase
from Game.FactoryGame.Interface.UI.Menu.Widget_LoadSession import ExecuteUbergraph_Widget_LoadSession.K2Node_CustomEvent_success
from Game.FactoryGame.Interface.UI.Menu.Widget_LoadSession import ExecuteUbergraph_Widget_LoadSession.K2Node_CustomEvent_Confirm
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import OnMenuEnter
from Script.Engine import IsValid
from Script.FactoryGame import Default__FGSaveSystem
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import EqualEqual_StrStr
from Game.FactoryGame.Interface.UI.Menu.Widget_LoadSession import ExecuteUbergraph_Widget_LoadSession
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Interface.UI.Menu.Widget_LoadSession import ExecuteUbergraph_Widget_LoadSession.K2Node_CustomEvent_Confirm1
from Script.Engine import Conv_StringToText
from Script.FactoryGame import ESaveState
from Game.FactoryGame.Interface.UI.Menu.Widget_LoadSession import ExecuteUbergraph_Widget_LoadSession.K2Node_Event_PlayBackgroundAnim
from Script.UMG import Widget
from Script.FactoryGame import SessionSaveStruct
from Script.FactoryGame import FGPlayerControllerBase
from Script.Engine import Format
from Script.FactoryGame import GetSaveState
from Script.FactoryGame import GetSaveSessionName
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import WidgetAnimation
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.Engine import NotEqual_ByteByte
from Script.FactoryGame import EnumerateSaveGames
from Script.FactoryGame import LoadGame
from Game.FactoryGame.Interface.UI.Menu.Widget_LoadSession import ExecuteUbergraph_Widget_LoadSession.K2Node_CustomEvent_ConfirmClicked
from Script.FactoryGame import GetName
from Script.UMG import ScrollToStart
from Script.FactoryGame import FGAdminInterface
from Script.FactoryGame import DeleteSaveFile
from Script.UMG import VerticalBoxSlot
from Script.FactoryGame import Default__FGSaveSession
from Script.UMG import Create
from Script.UMG import HasAnyChildren
from Game.FactoryGame.Interface.UI.Menu.Widget_LoadSession import ExecuteUbergraph_Widget_LoadSession.K2Node_CustomEvent_success1
from Script.FactoryGame import SortSessions
from Script.FactoryGame import GroupSavesPerSession
from Script.FactoryGame import AddPopupWithCloseDelegate
from Script.FactoryGame import GetSessionName
from Script.Engine import Array_Clear
from Script.UMG import SetRenderOpacity
from Script.FactoryGame import GetAdminInterface
from Script.Engine import NotEqual_StriStri

class Widget_LoadSession(BP_MenuBase):
    ShowDeleteSessionButton: Ptr[WidgetAnimation]
    ShowLoadDeleteButtons: Ptr[WidgetAnimation]
    OnBackClicked: FMulticastScriptDelegate
    OnLoadClicked: FMulticastScriptDelegate
    mCurrentSave: SaveHeader
    mCurrentSession: SessionSaveStruct
    isSelected: bool
    mCachedSaves: List[SaveHeader]
    UsesSubmenuBackground = True
    
    def OnSavesEnumerated(self, success: bool, saves: Ref[List[SaveHeader]]):
        ExecutionFlow.Push("L1010")
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mCachedSaves])
        if not success:
           goto(ExecutionFlow.Pop())
        self.mCachedSaves = saves
        groupedBySession: List[SessionSaveStruct] = []
        
        Default__FGSaveSystem.GroupSavesPerSession(Ref[self.mCachedSaves], Ref[groupedBySession])
        
        Default__FGSaveSystem.SortSessions(1, 1, Ref[groupedBySession])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 235
        ReturnValue: int32 = len(groupedBySession)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L692')
        Variable_0 = Variable
        ExecutionFlow.Push("L936")
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[Widget_SessionRow] = Default__WidgetBlueprintLibrary.Create(self, Widget_SessionRow, ReturnValue1)
        
        Item = None
        Item = groupedBySession[Variable_0]
        
        Item = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_1, "mSaveSession", Ref[Item])
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_1, "mLoadSessionWidget", self)
        ReturnValue_2: Ptr[VerticalBoxSlot] = self.mSessionVBox.AddChildToVerticalBox(ReturnValue_1)
        goto(ExecutionFlow.Pop())
        # Label 692
        ReturnValue_3: int32 = self.mSessionVBox.GetChildrenCount()
        ReturnValue_4: bool = ReturnValue_3 > 0
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_6: Ptr[Widget] = self.mSessionVBox.GetChildAt(0)
        ReturnValue_6.SetUserFocus(ReturnValue_5)
        self.UpdateCurrentSession()
        self.PopulateSavesFromSession(self.mCurrentSession)
        goto(ExecutionFlow.Pop())
        # Label 936
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L235')
    

    def PopulateSavesFromSession(self, session: SessionSaveStruct):
        ExecutionFlow.Push("L665")
        self.mSavesContainer.ClearChildren()
        
        IsValid = None
        self.IsValidCurrentSession(Ref[IsValid])
        if not IsValid:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        session.SaveHeaders = None
        # Label 120
        ReturnValue: int32 = len(session.SaveHeaders)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L591")
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Widget_SessionSaveRow] = Default__WidgetBlueprintLibrary.Create(self, Widget_SessionSaveRow, ReturnValue_1)
        
        session.SaveHeaders = None
        Item = None
        # Label 353
        Item = session.SaveHeaders[Variable_0]
        
        Item = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_2, "mSaveHeader", Ref[Item])
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "LoadSessionWidget", self)
        ReturnValue_3: Ptr[PanelSlot] = self.mSavesContainer.AddChild(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 591
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L120')
    

    def ShowLoadButtons(self):
        
        IsValid = None
        self.IsValidCurrentSave(Ref[IsValid])
        if not IsValid:
            goto('L62')
        ReturnValue = 0
        goto('L82')
        # Label 62
        ReturnValue = 2
    

    def IsDeleteSessionButtonEnabled(self):
        
        IsValid = None
        self.IsValidCurrentSession(Ref[IsValid])
        ReturnValue = IsValid
    

    def IsValidCurrentSession(self):
        
        self.mCurrentSession.SaveHeaders = None
        ReturnValue: int32 = len(self.mCurrentSession.SaveHeaders)
        ReturnValue_0: bool = ReturnValue > 0
        IsValid = ReturnValue_0
    

    def UpdateCurrentSession(self):
        ExecutionFlow.Push("L840")
        groupedBySession: List[SessionSaveStruct] = []
        
        Default__FGSaveSystem.GroupSavesPerSession(Ref[self.mCachedSaves], Ref[groupedBySession])
        
        Default__FGSaveSystem.SortSessions(1, 1, Ref[groupedBySession])
        Variable: bool = False
        Variable_0: int32 = 0
        Variable_1: int32 = 0
        # Label 168
        ReturnValue: bool = Not_PreBool(Variable)
        
        ReturnValue_0: int32 = len(groupedBySession)
        ReturnValue_1: bool = Variable_0 <= ReturnValue_0
        ReturnValue_2: bool = ReturnValue and ReturnValue_1
        if not ReturnValue_2:
            goto('L723')
        Variable_1 = Variable_0
        ExecutionFlow.Push("L766")
        
        Item = None
        Item = groupedBySession[Variable_1]
        
        Item = None
        ReturnValue_3: FString = Default__FGSaveSession.GetSaveSessionName(Ref[Item])
        
        ReturnValue1: FString = Default__FGSaveSession.GetSaveSessionName(Ref[self.mCurrentSession])
        ReturnValue_4: bool = Default__KismetStringLibrary.EqualEqual_StrStr(ReturnValue_3, ReturnValue1)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = groupedBySession[Variable_1]
        self.mCurrentSession = Item
        didFind = True
        goto(ExecutionFlow.Pop())
        # Label 723
        if not didFind:
            goto('L738')
        goto(ExecutionFlow.Pop())
        # Label 738
        self.mCurrentSession = SessionSaveStruct
        goto(ExecutionFlow.Pop())
        # Label 766
        ReturnValue_5: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_5
        goto('L168')
    

    def ShouldShowSaveGames(self):
        Variable: uint8 = 0
        Variable1: uint8 = 2
        
        IsValid = None
        self.IsValidCurrentSession(Ref[IsValid])
        Variable_0: bool = IsValid
        
        switch = {
            False: Variable1,
            True: Variable
        }
        # Label 82
        ReturnValue = switch.get(Variable_0, None)
    

    def IsValidCurrentSave(self):
        
        ReturnValue: FString = Default__FGSaveSession.GetSessionName(Ref[self.mCurrentSave])
        ReturnValue_0: bool = Default__KismetStringLibrary.NotEqual_StriStri(ReturnValue, "INVALID_SESSIONNAME")
        IsValid = ReturnValue_0
    

    def OnSaveClicked(self, SaveHeader: SaveHeader):
        self.mCurrentSave = SaveHeader
    

    def PopulateSessionList(self):
        self.mSessionVBox.ClearChildren()
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Base: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue)
        bSuccess: bool = Base
        if not bSuccess:
            goto('L353')
        ReturnValue_0: Ptr[FGAdminInterface] = Base.GetAdminInterface()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L353')
        OutputDelegate.BindUFunction(self, OnSavesEnumerated)
        ReturnValue_0 = Base.GetAdminInterface()
        ReturnValue_0.EnumerateSaveGames(False, OutputDelegate)
    

    def BndEvt__mDeleteSaveGameButton_K2Node_ComponentBoundEvent_115_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_LoadSession(511)
    

    def BndEvt__button2save_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_LoadSession(526)
    

    def ConfirmDeleteSessionPopUp(self):
        self.ExecuteUbergraph_Widget_LoadSession(541)
    

    def EventDeleteSession(self, confirm: bool):
        ExecuteUbergraph_Widget_LoadSession.K2Node_CustomEvent_Confirm1 = confirm #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_LoadSession(1250)
    

    def EventDeleteSave(self, confirm: bool):
        ExecuteUbergraph_Widget_LoadSession.K2Node_CustomEvent_Confirm = confirm #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_LoadSession(1658)
    

    def ConfirmDeleteSavePopUp(self):
        self.ExecuteUbergraph_Widget_LoadSession(2089)
    

    def OnEscape(self):
        self.ExecuteUbergraph_Widget_LoadSession(2742)
    

    def SpawnAnim(self):
        ExecuteUbergraph_Widget_LoadSession.K2Node_Event_PlayBackgroundAnim = PlayBackgroundAnim #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_LoadSession(2831)
    

    def LoadCurrentSave(self):
        self.ExecuteUbergraph_Widget_LoadSession(4183)
    

    def BndEvt__Widget_FrontEnd_Button_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_LoadSession(4188)
    

    def HideLoadAndDeleteButtons(self):
        self.ExecuteUbergraph_Widget_LoadSession(4203)
    

    def BndEvt__DeleteSave_K2Node_ComponentBoundEvent_2_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_LoadSession(4354)
    

    def HideDeleteSessionButton(self):
        self.ExecuteUbergraph_Widget_LoadSession(4369)
    

    def BndEvt__DeleteSessionButton_K2Node_ComponentBoundEvent_3_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_LoadSession(4445)
    

    def OnMenuEnter(self):
        ExecuteUbergraph_Widget_LoadSession.K2Node_Event_prevMenu = prevMenu #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_LoadSession(4460)
    

    def SaveDeleted(self, success: bool):
        ExecuteUbergraph_Widget_LoadSession.K2Node_CustomEvent_success1 = success #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_LoadSession(4484)
    

    def SessionDeleted(self, success: bool):
        ExecuteUbergraph_Widget_LoadSession.K2Node_CustomEvent_success = success #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_LoadSession(4499)
    

    def ClosedLoadPopup(self, ConfirmClicked: bool):
        ExecuteUbergraph_Widget_LoadSession.K2Node_CustomEvent_ConfirmClicked = ConfirmClicked #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_LoadSession(4504)
    

    def ExecuteUbergraph_Widget_LoadSession(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Base: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue)
        bSuccess: bool = Base
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_0: Ptr[FGAdminInterface] = Base.GetAdminInterface()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue_0 = Base.GetAdminInterface()
        
        ReturnValue_0.LoadGame(False, Ref[self.mCurrentSave])
        goto(ExecutionFlow.Pop())
        # Label 302
        self.PopulateSessionList()
        self.mLoadSessions.OnSpawnAnim(None)
        # Label 353
        self.HideDeleteSessionButton()
        goto(ExecutionFlow.Pop())
        # Label 368
        self.mCurrentSave = SaveHeader
        goto('L302')
        # Label 400
        self.mCurrentSession = SessionSaveStruct
        goto('L368')
        # Label 432
        self.mCurrentSave = SaveHeader1
        self.PopulateSessionList()
        self.mLoadSessions.OnSpawnAnim(None)
        goto(ExecutionFlow.Pop())
        self.ConfirmDeleteSessionPopUp()
        goto(ExecutionFlow.Pop())
        self.ConfirmDeleteSavePopUp()
        goto(ExecutionFlow.Pop())
        OutputDelegate.BindUFunction(self, EventDeleteSession)
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        ReturnValue_2: FString = Default__FGSaveSession.GetSaveSessionName(Ref[self.mCurrentSession])
        ReturnValue1_0: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_2)
        FormatArgumentData1.ArgumentName = "SessionName"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue1_0
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData1]
        ReturnValue1_1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 975, 'Value': 'Are you sure you want to delete the session "{SessionName}"?\r\nAll saves in this session will also be deleted.'}", Array1)
        
        OutputDelegate = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue1, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1174, 'Value': 'Delete Session'}", ReturnValue1_1, 1, None, None, Ref[OutputDelegate])
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1620")
        if not Confirm1:
           goto(ExecutionFlow.Pop())
        self.mSavesContainer.ClearChildren()
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        Base1: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue3)
        bSuccess1: bool = Base1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue1_2: Ptr[FGAdminInterface] = Base1.GetAdminInterface()
        ReturnValue1_3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_2)
        if not ReturnValue1_3:
           goto(ExecutionFlow.Pop())
        OutputDelegate3.BindUFunction(self, SessionDeleted)
        ReturnValue1_2 = Base1.GetAdminInterface()
        
        ReturnValue1_2.DeleteSaveSession(False, OutputDelegate3, Ref[self.mCurrentSession])
        goto(ExecutionFlow.Pop())
        # Label 1620
        self.mOwningMenu.RestoreFocusOnPopupClosed(False)
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L2051")
        if not Confirm:
           goto(ExecutionFlow.Pop())
        ReturnValue4: Ptr[PlayerController] = self.GetOwningPlayer()
        Base2: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue4)
        bSuccess2: bool = Base2
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        ReturnValue2: Ptr[FGAdminInterface] = Base2.GetAdminInterface()
        ReturnValue2_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue2)
        if not ReturnValue2_0:
           goto(ExecutionFlow.Pop())
        
        ReturnValue_3: FString = Default__FGSaveSession.GetName(Ref[self.mCurrentSave])
        OutputDelegate4.BindUFunction(self, SaveDeleted)
        ReturnValue2 = Base2.GetAdminInterface()
        ReturnValue2.DeleteSaveFile(False, ReturnValue_3, OutputDelegate4)
        goto(ExecutionFlow.Pop())
        # Label 2051
        self.mOwningMenu.RestoreFocusOnPopupClosed(False)
        goto(ExecutionFlow.Pop())
        OutputDelegate1.BindUFunction(self, EventDeleteSave)
        ReturnValue2_1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        ReturnValue1_4: FString = Default__FGSaveSession.GetName(Ref[self.mCurrentSave])
        ReturnValue_4: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue1_4)
        FormatArgumentData.ArgumentName = "SaveName"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_4
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_5: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2520, 'Value': 'Are you sure you want to delete the save "{SaveName}"?'}", Array)
        
        OutputDelegate1 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue2_1, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2664, 'Value': 'Delete Save File'}", ReturnValue_5, 1, None, None, Ref[OutputDelegate1])
        goto(ExecutionFlow.Pop())
        self.mOwningMenu.OnEscape()
        goto(ExecutionFlow.Pop())
        # Label 2779
        self.PopulateSessionList()
        self.mLoadSessions.OnSpawnAnim(None)
        goto(ExecutionFlow.Pop())
        if not PlayBackgroundAnim:
            goto('L2917')
        self.mLoadSessions.PlayBackgroundSpawnAnim()
        self.mSaves.PlayBackgroundSpawnAnim()
        # Label 2917
        self.mSavesContainer.ClearChildren()
        self.mLoadScrollbox.mScrollBox.ScrollToStart()
        ReturnValue_6: bool = self.mSessionVBox.HasAnyChildren()
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        self.mLoadSessions.OnSpawnAnim(None)
        self.HideDeleteSessionButton()
        goto(ExecutionFlow.Pop())
        # Label 3111
        ReturnValue = self.GetOwningPlayer()
        
        Variable = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue, STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/SaveTable.SaveTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 3242, 'Value': 'UnsupportedSaveHeader'}", STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/SaveTable.SaveTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 3332, 'Value': 'UnsupportedSaveBody'}", 0, None, ReturnValue, Ref[Variable])
        goto(ExecutionFlow.Pop())
        
        # Label 3376
        ReturnValue_7: uint8 = Default__FGSaveSystem.GetSaveState(Ref[self.mCurrentSave])
        CmpSuccess: bool = NotEqual_ByteByte(ReturnValue_7, 0)
        if not CmpSuccess:
            goto('L3111')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_7, 1)
        if not CmpSuccess:
            goto('L3616')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_7, 2)
        if not CmpSuccess:
            goto('L15')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_7, 3)
        if not CmpSuccess:
            goto('L3901')
        goto(ExecutionFlow.Pop())
        # Label 3616
        ReturnValue = self.GetOwningPlayer()
        OutputDelegate2.BindUFunction(self, ClosedLoadPopup)
        
        OutputDelegate2 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue, STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/SaveTable.SaveTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 3770, 'Value': 'VolatileSaveHeader'}", STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/SaveTable.SaveTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 3857, 'Value': 'VolatileSaveVersion'}", 1, None, ReturnValue, Ref[OutputDelegate2])
        goto(ExecutionFlow.Pop())
        # Label 3901
        ReturnValue = self.GetOwningPlayer()
        OutputDelegate2.BindUFunction(self, ClosedLoadPopup)
        
        OutputDelegate2 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue, STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/SaveTable.SaveTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 4055, 'Value': 'VolatileSaveHeader'}", STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/SaveTable.SaveTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 4142, 'Value': 'NewerSaveVersion'}", 1, None, ReturnValue, Ref[OutputDelegate2])
        goto(ExecutionFlow.Pop())
        goto('L3376')
        self.LoadCurrentSave()
        goto(ExecutionFlow.Pop())
        self.LoadSave.SetRenderOpacity(0)
        self.LoadSave.SetVisibility(3)
        self.DeleteSave.SetRenderOpacity(0)
        self.DeleteSave.SetVisibility(3)
        goto(ExecutionFlow.Pop())
        self.ConfirmDeleteSavePopUp()
        goto(ExecutionFlow.Pop())
        self.DeleteSessionButton.SetRenderOpacity(0)
        self.DeleteSessionButton.SetVisibility(3)
        goto(ExecutionFlow.Pop())
        self.ConfirmDeleteSessionPopUp()
        goto(ExecutionFlow.Pop())
        self.OnMenuEnter(prevMenu)
        goto('L2779')
        if not success1:
           goto(ExecutionFlow.Pop())
        goto('L432')
        goto('L400')
        if not ConfirmClicked:
           goto(ExecutionFlow.Pop())
        goto('L15')
    

    def OnLoadClicked__DelegateSignature(self, SaveGame: SaveHeader, IsPrivateGame: bool):
        pass
    

    def OnBackClicked__DelegateSignature(self):
        pass
    
