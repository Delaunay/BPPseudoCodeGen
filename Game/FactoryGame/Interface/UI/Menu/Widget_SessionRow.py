
from codegen.ue4_stub import *

from Script.UMG import SetUserFocus
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Interface.UI.Menu.Widget_SessionRow import Widget_SessionRow
from Script.Engine import SetObjectPropertyByName
from Script.Engine import AsTimeZoneDateTime_DateTime
from Script.UMG import GetChildrenCount
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.Engine import Not_PreBool
from Script.FactoryGame import SaveHeader
from Game.FactoryGame.Interface.UI.Menu.Widget_SessionSaveRow import Widget_SessionSaveRow
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.Menu.Widget_SessionRow import ExecuteUbergraph_Widget_SessionRow
from Script.UMG import GetChildAt
from Script.UMG import GetRenderOpacity
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Script.UMG import PlayAnimation
from Script.FactoryGame import GetSaveDateTime
from Script.UMG import ESlateVisibility
from Script.Engine import SetStructurePropertyByName
from Script.UMG import Handled
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_MouseOver import Play_UI_MainMenu_MouseOver
from Script.FactoryGame import GetAdminInterface
from Script.Engine import Len
from Script.FactoryGame import DeleteSaveSession
from Script.CoreUObject import Object
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.Menu.Widget_SessionRow import ExecuteUbergraph_Widget_SessionRow.K2Node_CustomEvent_success
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import EqualEqual_StrStr
from Game.FactoryGame.Interface.UI.Menu.Widget_SessionRow import ExecuteUbergraph_Widget_SessionRow.K2Node_Event_IsDesignTime
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Now
from Script.Engine import Conv_StringToText
from Script.CoreUObject import DateTime
from Game.FactoryGame.Interface.UI.Menu.Widget_LoadSession import Widget_LoadSession
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGGameState
from Script.Engine import BooleanOR
from Script.UMG import Widget
from Script.FactoryGame import SessionSaveStruct
from Script.FactoryGame import FGPlayerControllerBase
from Script.FactoryGame import GetSaveSessionName
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import WidgetAnimation
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.UMG import UserWidget
from Script.FactoryGame import GetName
from Script.Engine import NotEqual_ObjectObject
from Script.FactoryGame import FGAdminInterface
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import SelectColor
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Interface.UI.Menu.Widget_SessionRow import ExecuteUbergraph_Widget_SessionRow.K2Node_CustomEvent_confirmed
from Script.FactoryGame import Default__FGSaveSession
from Script.UMG import Create
from Script.Engine import GetGameState
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_Click import Play_UI_MainMenu_Click
from Script.UMG import SetContentColorAndOpacity
from Script.FactoryGame import AddPopupWithCloseDelegate
from Script.SlateCore import SlateColor
from Script.FactoryGame import GetSessionName
from Script.AkAudio import AkComponent
from Script.UMG import EventReply
from Script.CoreUObject import LinearColor

class Widget_SessionRow(UserWidget):
    HideSessionContentAnim: Ptr[WidgetAnimation]
    mSaveSession: SessionSaveStruct
    mLoadSessionWidget: Ptr[Widget_LoadSession]
    isSelected: bool
    mRecentSave: SaveHeader
    mWhiteHoverObjects: List[Ptr[Object]]
    mMainTextHoverObjects: List[Ptr[Object]]
    mSecondTextHoverObjects: List[Ptr[Object]]
    mButtonHoverObjects: List[Ptr[Object]]
    mSetButtonInfoToCurrentSession: bool
    bIsFocusable = True
    
    def SetDisabled(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        self.mTintBorder.SetContentColorAndOpacity(Graphics)
    

    def GetPointerVisibility(self):
        Variable: uint8 = 3
        Variable1: uint8 = 1
        Variable_0: bool = self.isSelected
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue = switch.get(Variable_0, None)
    

    def OnButtonClicked(self):
        ExecutionFlow.Push("L1168")
        if not self.isSelected:
            goto('L247')
        self.isSelected = False
        self.mLoadSessionWidget.mSavesContainer.ClearChildren()
        self.mLoadSessionWidget.mCurrentSession = SessionSaveStruct(SaveHeaders = List[StructProperty /Script/FactoryGame.SessionSaveStruct:SaveHeaders.SaveHeaders]([]))
        ReturnValue1: Ptr[UMGSequencePlayer] = self.mLoadSessionWidget.PlayAnimation(self.mLoadSessionWidget.ShowDeleteSessionButton, 0, 1, 1, 1)
        goto(ExecutionFlow.Pop())
        # Label 247
        self.isSelected = True
        Variable: int32 = 0
        # Label 281
        ReturnValue: int32 = self.mLoadSessionWidget.mSessionVBox.GetChildrenCount()
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L705')
        ExecutionFlow.Push("L1094")
        ReturnValue_1: Ptr[Widget] = self.mLoadSessionWidget.mSessionVBox.GetChildAt(Variable)
        ReturnValue_2: bool = NotEqual_ObjectObject(ReturnValue_1, self)
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        ReturnValue_1 = self.mLoadSessionWidget.mSessionVBox.GetChildAt(Variable)
        Row: Ptr[Widget_SessionRow] = Cast[Widget_SessionRow](ReturnValue_1)
        bSuccess: bool = Row
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Row.isSelected = False
        goto(ExecutionFlow.Pop())
        # Label 705
        self.mLoadSessionWidget.mCurrentSession = self.mSaveSession
        self.mLoadSessionWidget.PopulateSavesFromSession(self.mSaveSession)
        self.mLoadSessionWidget.mSaves.OnSpawnAnim(None)
        ReturnValue_3: float = self.mLoadSessionWidget.DeleteSessionButton.GetRenderOpacity()
        ReturnValue_4: bool = ReturnValue_3 > 0
        ReturnValue_5: bool = Not_PreBool(ReturnValue_4)
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        ReturnValue_6: Ptr[UMGSequencePlayer] = self.mLoadSessionWidget.PlayAnimation(self.mLoadSessionWidget.ShowDeleteSessionButton, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 1094
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L281')
    

    def GetMostRecentSaveFromSession(self):
        
        self.mSaveSession.SaveHeaders = None
        Item = None
        Item = self.mSaveSession.SaveHeaders[0]
        
        Item = None
        ReturnValue: FString = Default__FGSaveSession.GetSessionName(Ref[Item])
        ReturnValue_0: int32 = Default__KismetStringLibrary.Len(ReturnValue)
        ReturnValue_1: bool = ReturnValue_0 > 0
        if not ReturnValue_1:
            goto('L321')
        
        self.mSaveSession.SaveHeaders = None
        Item = None
        Item = self.mSaveSession.SaveHeaders[0]
        self.mRecentSave = Item
    

    def GetLastSaveTime(self):
        if not self.mSetButtonInfoToCurrentSession:
            goto('L153')
        ReturnValue: DateTime = Now()
        
        ReturnValue_0: FText = Default__KismetTextLibrary.AsTimeZoneDateTime_DateTime("", Ref[ReturnValue])
        self.mSaveTime.SetText(ReturnValue_0)
        # End
        
        self.mSaveSession.SaveHeaders = None
        # Label 153
        ReturnValue_1: int32 = len(self.mSaveSession.SaveHeaders)
        ReturnValue_2: bool = ReturnValue_1 > 0
        if not ReturnValue_2:
            goto('L503')
        
        self.mSaveSession.SaveHeaders = None
        Item = None
        # Label 269
        Item = self.mSaveSession.SaveHeaders[0]
        
        Item = None
        ReturnValue_3: DateTime = Default__FGSaveSession.GetSaveDateTime(Ref[Item])
        
        ReturnValue1: FText = Default__KismetTextLibrary.AsTimeZoneDateTime_DateTime("", Ref[ReturnValue_3])
        self.mSaveTime.SetText(ReturnValue1)
        # End
        # Label 503
        self.mSaveTime.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 540, 'Value': '-'}")
    

    def GetSessionName(self):
        if not self.mSetButtonInfoToCurrentSession:
            goto('L281')
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue)
        bSuccess: bool = State
        ReturnValue_0: FString = State.GetSessionName()
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_0)
        self.mTitle.SetText(ReturnValue_1)
        # End
        
        # Label 281
        ReturnValue_2: FString = Default__FGSaveSession.GetSaveSessionName(Ref[self.mSaveSession])
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_2)
        self.mTitle.SetText(ReturnValue1)
    

    def GetLastSaveName(self):
        
        self.mSaveSession.SaveHeaders = None
        ReturnValue: int32 = len(self.mSaveSession.SaveHeaders)
        ReturnValue_0: bool = ReturnValue > 0
        if not ReturnValue_0:
            goto('L348')
        
        self.mSaveSession.SaveHeaders = None
        Item = None
        # Label 116
        Item = self.mSaveSession.SaveHeaders[0]
        
        Item = None
        ReturnValue_1: FString = Default__FGSaveSession.GetName(Ref[Item])
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_1)
        self.mLastSaveName.SetText(ReturnValue_2)
        # End
        # Label 348
        self.mLastSaveName.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 385, 'Value': '(No Previous Saves)'}")
    

    def PopulateSavesFromSession(self, session: SessionSaveStruct):
        ExecutionFlow.Push("L684")
        self.mLoadSessionWidget.mSavesContainer.ClearChildren()
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        session.SaveHeaders = None
        # Label 109
        ReturnValue: int32 = len(session.SaveHeaders)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L610")
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        # Label 281
        ReturnValue_2: Ptr[Widget_SessionSaveRow] = Default__WidgetBlueprintLibrary.Create(self, Widget_SessionSaveRow, ReturnValue_1)
        
        session.SaveHeaders = None
        Item = None
        Item = session.SaveHeaders[Variable_0]
        
        Item = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_2, "mSaveHeader", Ref[Item])
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "LoadSessionWidget", self.mLoadSessionWidget)
        ReturnValue_3: Ptr[PanelSlot] = self.mLoadSessionWidget.mSavesContainer.AddChild(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 610
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L109')
    

    def OnFocusReceived(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mSessionRowButton.SetUserFocus(ReturnValue)
        ReturnValue_0: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_1: EventReply = ReturnValue_0
    

    def GetSaveTextColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        Variable: bool = self.isSelected
        
        TextWhite = None
        GraphicsWhite = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        ReturnValue: bool = self.mSessionRowButton.IsHovered()
        
        TextWhite1 = None
        GraphicsWhite1 = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite1], Ref[GraphicsWhite1])
        Variable1: bool = ReturnValue
        
        switch = {
            False: Text,
            True: TextWhite
        }
        
        switch_0 = {
            False: switch.get(Variable, None),
            True: TextWhite1
        }
        ReturnValue_0: SlateColor = switch_0.get(Variable1, None)
    

    def GetIconColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue: bool = self.mSessionRowButton.IsHovered()
        ReturnValue_0: LinearColor = SelectColor(Orange, Graphics, ReturnValue)
        ReturnValue_1: LinearColor = ReturnValue_0
    

    def GetButtonHoverColor(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mLoadSessionWidget)
        # Label 51
        if not ReturnValue:
            goto('L626')
        
        self.mLoadSessionWidget.mCurrentSession = None
        ReturnValue_0: FString = Default__FGSaveSession.GetSaveSessionName(Ref[self.mLoadSessionWidget.mCurrentSession])
        
        Text1 = None
        Graphics1 = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text1], Ref[Graphics1])
        
        ReturnValue1: FString = Default__FGSaveSession.GetSaveSessionName(Ref[self.mSaveSession])
        ReturnValue_1: bool = Default__KismetStringLibrary.EqualEqual_StrStr(ReturnValue_0, ReturnValue1)
        ReturnValue_2: bool = self.mSessionRowButton.IsHovered()
        ReturnValue_3: bool = BooleanOR(ReturnValue_1, self.isSelected)
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue_4: LinearColor = SelectColor(Graphics1, LinearColor(R = 0, G = 0, B = 0, A = 0), ReturnValue_3)
        ReturnValue1_0: LinearColor = SelectColor(Orange, ReturnValue_4, ReturnValue_2)
        ReturnValue_5: LinearColor = ReturnValue1_0
        goto('L823')
        # Label 626
        Variable: LinearColor = LinearColor(R = 0, G = 0, B = 0, A = 0)
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        Variable_0: bool = self.isSelected
        
        switch = {
            False: Variable,
            True: Graphics
        }
        ReturnValue_5 = switch.get(Variable_0, None)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_120_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SessionRow(290)
    

    def BndEvt__mSessionRowButton_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SessionRow(430)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SessionRow(558)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_SessionRow.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SessionRow(563)
    

    def BndEvt__mLoadButton_K2Node_ComponentBoundEvent_1_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SessionRow(610)
    

    def BndEvt__mDeleteSessionButton_K2Node_ComponentBoundEvent_2_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SessionRow(615)
    

    def ConfirmDeleteSessionPopUp(self):
        self.ExecuteUbergraph_Widget_SessionRow(634)
    

    def Event DeleteSession(self, confirmed: bool):
        ExecuteUbergraph_Widget_SessionRow.K2Node_CustomEvent_confirmed = confirmed #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SessionRow(929)
    

    def BndEvt__mSessionRowButton_K2Node_ComponentBoundEvent_3_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SessionRow(1333)
    

    def OnDeleteSessionDone(self, success: bool):
        ExecuteUbergraph_Widget_SessionRow.K2Node_CustomEvent_success = success #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SessionRow(10)
    

    def ExecuteUbergraph_Widget_SessionRow(self):
        self.mLoadSessionWidget.PopulateSessionList()
        # End
        # Label 51
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mLoadSessionWidget)
        if not ReturnValue:
            goto('L269')
        # Label 116
        Variable: uint8 = 2
        Variable_0: bool = self.isSelected
        Variable1: uint8 = 0
        
        switch = {
            False: Variable,
            True: Variable1
        }
        self.mLoadDelBox.SetVisibility(switch.get(Variable_0, None))
        # End
        # Label 269
        self.SetVisibility(3)
        goto('L116')
        self.OnButtonClicked()
        self.mLoadSessionWidget.HideLoadAndDeleteButtons()
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Click, ReturnValue_0, True)
        # End
        self.mLoadDelBox.SetVisibility(0)
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_MouseOver, ReturnValue1, True)
        # End
        goto('L51')
        self.GetLastSaveName()
        self.GetSessionName()
        self.GetLastSaveTime()
        # End
        # Label 610
        # End
        self.ConfirmDeleteSessionPopUp()
        # End
        OutputDelegate1.BindUFunction(self, Event DeleteSession)
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        
        OutputDelegate1 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue2, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 723, 'Value': 'Delete Session'}", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 777, 'Value': 'Are you sure you want to delete this session? \r\nThis will delete all save files in the session!'}", 1, None, None, Ref[OutputDelegate1])
        # End
        if not confirmed:
            goto('L1414')
        self.mLoadSessionWidget.mOwningMenu.RestoreFocusOnPopupClosed(False)
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        Base: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue3)
        bSuccess: bool = Base
        if not bSuccess:
            goto('L1414')
        ReturnValue_2: Ptr[FGAdminInterface] = Base.GetAdminInterface()
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_2)
        if not ReturnValue1_1:
            goto('L1414')
        OutputDelegate.BindUFunction(self, OnDeleteSessionDone)
        ReturnValue_2 = Base.GetAdminInterface()
        
        ReturnValue_2.DeleteSaveSession(False, OutputDelegate, Ref[self.mSaveSession])
        # End
        ReturnValue_3: bool = Not_PreBool(self.isSelected)
        if not ReturnValue_3:
            goto('L1414')
        self.mLoadDelBox.SetVisibility(2)
    
