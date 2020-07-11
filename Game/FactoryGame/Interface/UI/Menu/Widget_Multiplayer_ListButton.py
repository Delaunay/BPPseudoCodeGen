
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Menu.Widget_Multiplayer_ListButton import ExecuteUbergraph_Widget_Multiplayer_ListButton.K2Node_Event_IsDesignTime
from Script.Engine import Conv_TextToString
from Script.Engine import GetPlayerName
from Script.OnlineSubsystemUtils import BlueprintSessionResult
from Game.FactoryGame.Interface.UI.Menu.ECanJoinInviteResult import ECanJoinInviteResult
from Game.FactoryGame.Interface.UI.Assets.MainMenu.Multiplayer.Menu_PlayerIcon_Satisfactory import Menu_PlayerIcon_Satisfactory
from Game.FactoryGame.Interface.UI.Assets.MainMenu.Multiplayer.Menu_PlayerIcon import Menu_PlayerIcon
from Script.FactoryGame import GetPresenceString
from Script.Engine import EqualEqual_ByteByte
from Script.FactoryGame import IsPlayingThisGame
from Script.FactoryGame import FGLocalPlayer
from Script.Engine import UniqueNetIdRepl
from Script.Engine import Conv_ByteToInt
from Script.UMG import GetChildrenCount
from Script.SlateCore import Margin
from Script.FactoryGame import OnlinePresence
from Script.CoreUObject import Timespan
from Script.Engine import Not_PreBool
from Script.Engine import MakeTimespan
from Script.FactoryGame import GetSessionVisibility
from Script.UMG import SetToolTipText
from Script.FactoryGame import Default__FGInviteLibrary
from Script.Engine import PlayerController
from Script.UMG import GetChildAt
from Script.FactoryGame import IsOnline
from Script.Engine import FormatArgumentData
from Script.FactoryGame import ESessionVisibility
from Script.UMG import ESlateVisibility
from Script.FactoryGame import ECantJoinReason
from Script.FactoryGame import GetNameFromUniqueNetId
from Game.FactoryGame.-Shared.Blueprint.BP_OnlineHelpers import Default__BP_OnlineHelpers
from Script.UMG import SetColorAndOpacity
from Script.FactoryGame import GetSessionFromPresence
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import IsServerAdmin
from Script.Engine import Conv_StringToText
from Script.FactoryGame import IsWaitingForData
from Script.FactoryGame import ECachedNATType
from Script.FactoryGame import NATTypeToText
from Script.Engine import BooleanOR
from Script.FactoryGame import GetPresenceFromNetId
from Script.FactoryGame import Default__FGNetworkLibrary
from Script.UMG import Widget
from Script.FactoryGame import GetInviteSenderUniqueNetId
from Script.Engine import BreakTimespan
from Script.UMG import PanelWidget
from Script.Engine import Format
from Script.FactoryGame import Default__FGPresenceLibrary
from Game.FactoryGame.Interface.UI.Menu.Widget_Multiplayer_ListButton import Widget_Multiplayer_ListButton
from Script.Engine import NotEqual_ByteByte
from Script.FactoryGame import GetCachedNATType
from Script.FactoryGame import GetSessionSettings
from Script.UMG import Image
from Script.Engine import NotEqual_ObjectObject
from Game.FactoryGame.Interface.UI.Menu.ECantInviteResult import ECantInviteResult
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import IsSessionValid
from Game.FactoryGame.Interface.UI.Menu.Widget_Multiplayer_ListButton import ExecuteUbergraph_Widget_Multiplayer_ListButton
from Script.FactoryGame import Default__FGSessionLibrary
from Script.FactoryGame import GetUniqeNetId
from Script.FactoryGame import GetFriendName
from Script.UMG import SetBrushTintColor
from Script.CoreUObject import Vector2D
from Script.FactoryGame import Default__FGFriendsLibrary
from Script.UMG import SetContentColorAndOpacity
from Game.FactoryGame.Interface.UI.Assets.MainMenu.Multiplayer.Menu_PlayerIcon_Offline import Menu_PlayerIcon_Offline
from Script.UMG import SetStyle
from Script.FactoryGame import FGWidgetMultiplayer
from Script.FactoryGame import FGOnlineSessionSettings
from Script.FactoryGame import IsFriendJoinable
from Script.CoreUObject import LinearColor
from Script.Engine import LocalPlayer

class Widget_Multiplayer_ListButton(FGWidgetMultiplayer):
    mAdditionalInfo: FText = NSLOCTEXT("", "AE287AD0496B3B10298C5E956F7F0EF6", "Playing Satisfactory")
    mPlayersInSession: int32
    mPrivateSession: bool
    mTimePlayed: int32
    mParentWidget: Ptr[PanelWidget]
    OnActionButtonClicked: FMulticastScriptDelegate
    mActionButtonText: FText
    mHideSessionInfo: bool
    mHideActionButton: bool
    mHideSecondaryActionButton: bool = True
    mDisableActionButton: bool
    mActionButtonTooltip: FText
    mInAGame: bool
    mIsSelected: bool
    mSession: BlueprintSessionResult
    OnSessionSelected: FMulticastScriptDelegate
    OnButtonClicked: FMulticastScriptDelegate
    OnSessionDeselected: FMulticastScriptDelegate
    mIsSelectable: bool = True
    IsNonInteractable: bool
    mNatType: uint8
    mIsHost: bool
    mCareAboutNAT: bool
    mShowWarning: bool
    
    def UpdateNATWarningForClient(self):
        ReturnValue: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L492')
        ReturnValue_0: uint8 = Default__FGNetworkLibrary.GetCachedNATType(Player)
        
        isIssue = None
        self.IsNATIssue(self.mNatType, ReturnValue_0, Ref[isIssue])
        Variable: uint8 = 0
        Variable1: uint8 = 1
        Variable_0: bool = isIssue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.Widget_NatInformation.SetVisibility(switch.get(Variable_0, None))
        ReturnValue_0 = Default__FGNetworkLibrary.GetCachedNATType(Player)
        
        toolTip = None
        self.GetConnectingNATIsse(self.mNatType, ReturnValue_0, Ref[toolTip])
        
        toolTip = None
        self.Widget_NatInformation.SetToolTipText(Ref[toolTip])
    

    def GetHostingNATIsse(self, HostNAT: uint8, ClientNat: uint8):
        ReturnValue: FText = Default__FGNetworkLibrary.NATTypeToText(HostNAT)
        ReturnValue1: FText = Default__FGNetworkLibrary.NATTypeToText(ClientNat)
        FormatArgumentData.ArgumentName = "hostNat"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "clientNat"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue1
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData, FormatArgumentData1]
        ReturnValue_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 588, 'Value': 'Your friend will most likely not be able to connect to you as you have  {hostNat} NAT while your friend has {clientNat} NAT unless you are on the same network'}", Array)
        Tooltip = ReturnValue_0
    

    def GetConnectingNATIsse(self, HostNAT: uint8, ClientNat: uint8):
        ReturnValue: FText = Default__FGNetworkLibrary.NATTypeToText(HostNAT)
        ReturnValue1: FText = Default__FGNetworkLibrary.NATTypeToText(ClientNat)
        FormatArgumentData.ArgumentName = "hostNat"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "clientNat"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue1
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData, FormatArgumentData1]
        ReturnValue_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 588, 'Value': 'You will most likely not be able to connect to host as your friend has {hostNat} NAT while you have {clientNat} NAT unless you are on the same network'}", Array)
        Tooltip = ReturnValue_0
    

    def IsNATIssue(self, HostNAT: uint8, ClientNat: uint8):
        CmpSuccess: bool = NotEqual_ByteByte(HostNAT, 0)
        if not CmpSuccess:
            goto('L185')
        CmpSuccess = NotEqual_ByteByte(HostNAT, 1)
        if not CmpSuccess:
            goto('L201')
        CmpSuccess = NotEqual_ByteByte(HostNAT, 2)
        if not CmpSuccess:
            goto('L386')
        CmpSuccess = NotEqual_ByteByte(HostNAT, 3)
        if not CmpSuccess:
            goto('L386')
        # End
        # Label 185
        isIssue = False
        # End
        # Label 201
        CmpSuccess_0: bool = NotEqual_ByteByte(ClientNat, 0)
        if not CmpSuccess_0:
            goto('L185')
        CmpSuccess_0 = NotEqual_ByteByte(ClientNat, 1)
        if not CmpSuccess_0:
            goto('L185')
        CmpSuccess_0 = NotEqual_ByteByte(ClientNat, 2)
        if not CmpSuccess_0:
            goto('L386')
        CmpSuccess_0 = NotEqual_ByteByte(ClientNat, 3)
        if not CmpSuccess_0:
            goto('L386')
        # End
        # Label 386
        isIssue = True
    

    def UpdateNATWarningForHost(self):
        ReturnValue: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L492')
        ReturnValue_0: uint8 = Default__FGNetworkLibrary.GetCachedNATType(Player)
        
        isIssue = None
        self.IsNATIssue(ReturnValue_0, self.mNatType, Ref[isIssue])
        Variable: uint8 = 0
        Variable1: uint8 = 1
        Variable_0: bool = isIssue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.Widget_NatInformation.SetVisibility(switch.get(Variable_0, None))
        ReturnValue_0 = Default__FGNetworkLibrary.GetCachedNATType(Player)
        
        toolTip = None
        self.GetHostingNATIsse(ReturnValue_0, self.mNatType, Ref[toolTip])
        
        toolTip = None
        self.Widget_NatInformation.SetToolTipText(Ref[toolTip])
    

    def SetupForManagePlayers(self, PlayerState: Ptr[FGPlayerState]):
        ReturnValue: bool = PlayerState.IsServerAdmin()
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 62, 'Value': 'Kick the player'}"
        ReturnValue_0: FString = PlayerState.GetPlayerName()
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_0)
        ReturnValue_2: int32 = Conv_ByteToInt(PlayerState.Ping)
        ReturnValue_3: UniqueNetIdRepl = PlayerState.GetUniqeNetId()
        ReturnValue_4: int32 = ReturnValue_2 * 4
        FormatArgumentData.ArgumentName = "Ping"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = ReturnValue_4
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 583, 'Value': 'Only server admin can kick players'}"
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        
        valid = None
        Default__HUDHelpers.HasValidAdminInterface(ReturnValue_5, self, Ref[valid])
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        Variable_0: bool = valid
        
        ReturnValue_6: OnlinePresence = Default__FGPresenceLibrary.GetPresenceFromNetId(ReturnValue1, Ref[ReturnValue_3])
        
        ReturnValue_7: BlueprintSessionResult = Default__FGPresenceLibrary.GetSessionFromPresence(Ref[ReturnValue_6])
        
        ReturnValue_8: FString = Default__FGPresenceLibrary.GetPresenceString(Ref[ReturnValue_6])
        ReturnValue_9: bool = Default__FGSessionLibrary.IsSessionValid(ReturnValue_7)
        ReturnValue1_0: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_8)
        ReturnValue_10: bool = Not_PreBool(valid)
        FormatArgumentData1.ArgumentName = "Activity"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue1_0
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_11: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1377, 'Value': '{Activity} | {Ping}ms'}", Array)
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.Internal_UpdateButton(ReturnValue_1, True, ReturnValue_11, 0, False, 0, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1491, 'Value': 'Kick'}", True, True, ReturnValue, True, ReturnValue_10, switch.get(Variable_0, None), ReturnValue_9, BlueprintSessionResult(), False, False, 0, False, False, False)
    

    def SetupForJoinInvite(self, invite: Ref[PendingInvite]):
        
        ReturnValue: UniqueNetIdRepl = Default__FGInviteLibrary.GetInviteSenderUniqueNetId(Ref[invite])
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        
        result = None
        Default__BP_OnlineHelpers.CanJoinInvite(ReturnValue_0, invite, self, Ref[result])
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 167, 'Value': "Can't join as the game is full"}"
        ReturnValue_1: bool = NotEqual_ByteByte(result, 4)
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 286, 'Value': 'Invite sender is not in a game anymore'}"
        Variable2: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 382, 'Value': 'Invite sender is not online anymore'}"
        Variable3: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 475, 'Value': 'Friend is running other version of the game than you'}"
        Variable4: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 585, 'Value': 'Join friend'}"
        ReturnValue_2: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Variable_0: uint8 = result
        
        name = None
        ReturnValue_3: bool = Default__FGNetworkLibrary.GetNameFromUniqueNetId(ReturnValue_2, Ref[ReturnValue], Ref[name])
        ReturnValue_4: FText = Default__KismetTextLibrary.Conv_StringToText(name)
        
        presence = None
        Default__BP_OnlineHelpers.GetInvitePresence(ReturnValue_2, invite, self, Ref[presence])
        
        presence = None
        ReturnValue_5: BlueprintSessionResult = Default__FGPresenceLibrary.GetSessionFromPresence(Ref[presence])
        
        presence = None
        ReturnValue_6: FString = Default__FGPresenceLibrary.GetPresenceString(Ref[presence])
        ReturnValue_7: bool = Default__FGSessionLibrary.IsSessionValid(ReturnValue_5)
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_6)
        ReturnValue_8: bool = Not_PreBool(ReturnValue_7)
        
        ReturnValue_9: uint8 = Default__FGSessionLibrary.GetSessionVisibility(Ref[ReturnValue_5])
        
        ReturnValue_10: FGOnlineSessionSettings = Default__FGSessionLibrary.GetSessionSettings(Ref[ReturnValue_5])
        ReturnValue_11: bool = EqualEqual_ByteByte(ReturnValue_9, 0)
        
        presence = None
        ReturnValue_12: bool = Default__FGPresenceLibrary.IsPlayingThisGame(Ref[presence])
        
        presence = None
        ReturnValue_13: bool = Default__FGPresenceLibrary.IsOnline(Ref[presence])
        ReturnValue1_0: bool = Not_PreBool(ReturnValue_12)
        ReturnValue_14: bool = BooleanOR(ReturnValue1_0, ReturnValue_8)
        
        switch = {
            0: Variable,
            1: Variable1,
            2: Variable2,
            3: Variable3,
            4: Variable4
        }
        self.Internal_UpdateButton(ReturnValue_4, ReturnValue_13, ReturnValue1, ReturnValue_10.NumConnectedPlayers, ReturnValue_11, ReturnValue_10.PlayDuration, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1539, 'Value': 'Accept'}", ReturnValue_14, ReturnValue_12, False, True, ReturnValue_1, switch.get(Variable_0, None), ReturnValue_7, BlueprintSessionResult(), True, False, ReturnValue_10.natType, False, True, False)
    

    def SetupForSendInvite(self, friend: Ref[FGOnlineFriend]):
        ReturnValue: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        
        ReturnValue_0: bool = Default__FGFriendsLibrary.IsWaitingForData(ReturnValue, Ref[friend])
        if not ReturnValue_0:
            goto('L412')
        ReturnValue1: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        
        displayName = None
        ReturnValue_1: bool = Default__FGFriendsLibrary.GetFriendName(ReturnValue1, Ref[friend], Ref[displayName])
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_StringToText(displayName)
        self.Internal_UpdateButton(ReturnValue_2, False, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 275, 'Value': 'Offline'}", 0, False, 0, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 333, 'Value': 'Invite'}", True, False, True, True, False, , False, BlueprintSessionResult(), False, False, 0, True, False, False)
        # End
        # Label 412
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 432, 'Value': 'Online'}"
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 496, 'Value': 'Invite friend'}"
        Variable2: FText = 
        Variable3: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 587, 'Value': 'Friend already in game'}"
        Variable4: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 667, 'Value': 'Friend not playing Satisfactory'}"
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        
        canSend = None
        Default__BP_OnlineHelpers.CanSendInvite(ReturnValue_3, friend, self, Ref[canSend])
        
        inSession = None
        Default__BP_OnlineHelpers.IsFriendInOnlineSession(ReturnValue1_0, self, Ref[friend], Ref[inSession])
        Variable_0: uint8 = canSend
        ReturnValue_4: bool = Not_PreBool(inSession)
        ReturnValue_5: bool = NotEqual_ByteByte(canSend, 3)
        Variable5: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1019, 'Value': 'Offline'}"
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1 = self.GetOwningLocalPlayer()
        
        ReturnValue_6: OnlinePresence = Default__BP_OnlineHelpers.GetFriendPresence(ReturnValue2, self, Ref[friend])
        
        displayName = None
        ReturnValue_1 = Default__FGFriendsLibrary.GetFriendName(ReturnValue1, Ref[friend], Ref[displayName])
        
        compactPresence = None
        Default__BP_OnlineHelpers.GetCompactPresence(ReturnValue_6, self, Ref[compactPresence])
        ReturnValue_2 = Default__KismetTextLibrary.Conv_StringToText(displayName)
        ReturnValue_7: bool = BooleanOR(compactPresence.IsPlayingThisGame_6_D07FB68E4051EB599EEFC5B695C2B0FA, compactPresence.IsPlayingOtherGame_7_ED9DBFB84A164DABCD8A488B070BE8C3)
        ReturnValue1_1: bool = Not_PreBool(compactPresence.IsPlayingThisGame_6_D07FB68E4051EB599EEFC5B695C2B0FA)
        Variable_1: bool = ReturnValue_7
        ReturnValue1_2: bool = BooleanOR(ReturnValue1_1, ReturnValue_4)
        Variable1_0: bool = compactPresence.IsOnline_3_0B4A819747012DC786FA4097038402CD
        ReturnValue1_3: FText = Default__KismetTextLibrary.Conv_StringToText(compactPresence.PresenceString_8_73B095B54A983F2391EE189D60CC1495)
        
        session = None
        Default__BP_OnlineHelpers.GetFriendSession(friend, ReturnValue1, self, Ref[session])
        
        session = None
        ReturnValue_8: FGOnlineSessionSettings = Default__FGSessionLibrary.GetSessionSettings(Ref[session])
        
        session = None
        ReturnValue_9: uint8 = Default__FGSessionLibrary.GetSessionVisibility(Ref[session])
        ReturnValue_10: bool = EqualEqual_ByteByte(ReturnValue_9, 0)
        
        switch = {
            False: Variable,
            True: ReturnValue1_3
        }
        
        switch_0 = {
            False: Variable5,
            True: switch.get(Variable_1, None)
        }
        
        switch_1 = {
            0: Variable4,
            1: Variable3,
            2: Variable2,
            3: Variable1
        }
        self.Internal_UpdateButton(ReturnValue_2, compactPresence.IsOnline_3_0B4A819747012DC786FA4097038402CD, switch_0.get(Variable1_0, None), ReturnValue_8.NumConnectedPlayers, ReturnValue_10, ReturnValue_8.PlayDuration, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2012, 'Value': 'Invite'}", ReturnValue1_2, compactPresence.IsPlayingThisGame_6_D07FB68E4051EB599EEFC5B695C2B0FA, False, True, ReturnValue_5, switch_1.get(Variable_0, None), inSession, BlueprintSessionResult(), False, compactPresence.IsPlayingOtherGame_7_ED9DBFB84A164DABCD8A488B070BE8C3, ReturnValue_8.natType, True, True, False)
    

    def Internal_UpdateButton(self, Title: FText, IsOnline: bool, AdditionalInfo: FText, playersInSession: int32, privateSession: bool, TimePlayed: int32, ActionButtonText: FText, hideSessionInfo: bool, isPlayingSatisfactory: bool, hideActionButton: bool, hideSecondaryActionButton: bool, disableActionButton: bool, actionButtonTooltip: FText, inAGame: bool, session: BlueprintSessionResult, isSelectable: bool, IsNonInteractable: bool, natType: uint8, IsHost: bool, careAboutNAT: bool, ShowWarning: bool):
        
        ReturnValue: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Title])
        self.mTitle = ReturnValue
        self.mIsOnline = IsOnline
        self.mAdditionalInfo = AdditionalInfo
        self.mPlayersInSession = playersInSession
        self.mPrivateSession = privateSession
        self.mTimePlayed = TimePlayed
        self.mActionButtonText = ActionButtonText
        self.mHideSessionInfo = hideSessionInfo
        self.mIsPlayingSatisfactory = isPlayingSatisfactory
        self.mHideActionButton = hideActionButton
        self.mHideSecondaryActionButton = hideSecondaryActionButton
        self.mDisableActionButton = disableActionButton
        self.mActionButtonTooltip = actionButtonTooltip
        # Label 354
        self.mInAGame = inAGame
        self.mSession = session
        self.mIsSelectable = isSelectable
        self.IsNonInteractable = IsNonInteractable
        self.mNatType = natType
        self.mIsHost = IsHost
        self.mCareAboutNAT = careAboutNAT
        self.mShowWarning = ShowWarning
        self.UpdateButton()
    

    def SetupForJoinGame(self, friend: Ref[FGOnlineFriend]):
        ReturnValue: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        
        session1 = None
        Default__BP_OnlineHelpers.GetFriendSession(friend, ReturnValue, self, Ref[session1])
        
        session1 = None
        ReturnValue_0: FGOnlineSessionSettings = Default__FGSessionLibrary.GetSessionSettings(Ref[session1])
        SessionSettings = ReturnValue_0
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 194, 'Value': 'Offline'}"
        Variable_0: BlueprintSessionResult = BlueprintSessionResult()
        # Label 271
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 291, 'Value': 'Join'}"
        Variable2: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 353, 'Value': "Can't join game as game is full"}"
        Variable3: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 442, 'Value': 'Friend is running other version of the game than you'}"
        Variable4: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 552, 'Value': "Can't join game as game is private"}"
        Variable5: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 644, 'Value': "Can't join game as friend is playing another game"}"
        Variable6: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 751, 'Value': "Can't join game as friend is not currently in a game"}"
        Variable7: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 861, 'Value': "Game is invalid (shouldn't happen)"}"
        Variable8: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 953, 'Value': 'Online'}"
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        Variable3_0: bool = True
        
        session = None
        Default__BP_OnlineHelpers.GetFriendSession(friend, ReturnValue_1, self, Ref[session])
        ReturnValue_2: bool = Default__FGSessionLibrary.IsSessionValid(session)
        Variable4_0: bool = False
        Variable1_0: bool = ReturnValue_2
        ReturnValue_3: bool = Not_PreBool(ReturnValue_2)
        Variable5_0: bool = False
        Variable6_0: bool = False
        Variable7_0: bool = True
        Variable8_0: bool = True
        ReturnValue = self.GetOwningLocalPlayer()
        Variable9: bool = False
        
        displayName = None
        ReturnValue_4: bool = Default__FGFriendsLibrary.GetFriendName(ReturnValue, Ref[friend], Ref[displayName])
        
        ReturnValue_5: uint8 = Default__FGFriendsLibrary.IsFriendJoinable(ReturnValue, Ref[friend])
        ReturnValue_6: FText = Default__KismetTextLibrary.Conv_StringToText(displayName)
        Variable_1: uint8 = ReturnValue_5
        ReturnValue_7: bool = NotEqual_ByteByte(ReturnValue_5, 6)
        ReturnValue1: bool = Not_PreBool(ReturnValue_7)
        
        session1 = None
        Default__BP_OnlineHelpers.GetFriendSession(friend, ReturnValue, self, Ref[session1])
        
        ReturnValue_8: OnlinePresence = Default__BP_OnlineHelpers.GetFriendPresence(ReturnValue, self, Ref[friend])
        
        compactPresence = None
        Default__BP_OnlineHelpers.GetCompactPresence(ReturnValue_8, self, Ref[compactPresence])
        
        session1 = None
        ReturnValue_9: uint8 = Default__FGSessionLibrary.GetSessionVisibility(Ref[session1])
        ReturnValue_10: bool = BooleanOR(compactPresence.IsPlayingThisGame_6_D07FB68E4051EB599EEFC5B695C2B0FA, compactPresence.IsPlayingOtherGame_7_ED9DBFB84A164DABCD8A488B070BE8C3)
        ReturnValue_11: bool = EqualEqual_ByteByte(ReturnValue_9, 0)
        Variable2_0: bool = ReturnValue_10
        ReturnValue2: bool = Not_PreBool(compactPresence.IsPlayingThisGame_6_D07FB68E4051EB599EEFC5B695C2B0FA)
        Variable_2: bool = compactPresence.IsOnline_3_0B4A819747012DC786FA4097038402CD
        ReturnValue1_0: bool = BooleanOR(ReturnValue2, ReturnValue_3)
        ReturnValue1_1: FText = Default__KismetTextLibrary.Conv_StringToText(compactPresence.PresenceString_8_73B095B54A983F2391EE189D60CC1495)
        Variable1_1: uint8 = ReturnValue_5
        
        switch = {
            0: Variable3_0,
            1: Variable4_0,
            2: Variable5_0,
            3: Variable6_0,
            4: Variable7_0,
            5: Variable8_0,
            6: Variable9
        }
        ReturnValue2_0: bool = BooleanOR(ReturnValue1_0, switch.get(Variable1_1, None))
        
        switch_0 = {
            False: Variable8,
            True: ReturnValue1_1
        }
        
        switch_1 = {
            False: Variable,
            True: switch_0.get(Variable2_0, None)
        }
        
        switch_2 = {
            0: Variable7,
            1: Variable6,
            2: Variable5,
            3: Variable4,
            4: Variable3,
            5: Variable2,
            6: Variable1
        }
        
        switch_3 = {
            False: Variable_0,
            True: session
        }
        
        switch_4 = {
            0: Variable3_0,
            1: Variable4_0,
            2: Variable5_0,
            3: Variable6_0,
            4: Variable7_0,
            5: Variable8_0,
            6: Variable9
        }
        self.Internal_UpdateButton(ReturnValue_6, compactPresence.IsOnline_3_0B4A819747012DC786FA4097038402CD, switch_1.get(Variable_2, None), SessionSettings.NumConnectedPlayers, ReturnValue_11, SessionSettings.PlayDuration, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2467, 'Value': 'Join'}", ReturnValue2_0, compactPresence.IsPlayingThisGame_6_D07FB68E4051EB599EEFC5B695C2B0FA, True, True, ReturnValue_7, switch_2.get(Variable_1, None), ReturnValue_2, switch_3.get(Variable1_0, None), ReturnValue1, ReturnValue2, SessionSettings.natType, False, True, switch_4.get(Variable1_1, None))
    

    def SetButtonColor(self, Color: LinearColor):
        SlateColor.SpecifiedColor = Color
        SlateColor.ColorUseRule = 0
        SlateBrush.ImageSize = self.mButton.WidgetStyle.Normal.ImageSize
        SlateBrush.Margin = self.mButton.WidgetStyle.Normal.Margin
        SlateBrush.TintColor = SlateColor
        SlateBrush.ResourceObject = self.mButton.WidgetStyle.Normal.ResourceObject
        SlateBrush.DrawAs = self.mButton.WidgetStyle.Normal.DrawAs
        SlateBrush.Tiling = self.mButton.WidgetStyle.Normal.Tiling
        SlateBrush.Mirroring = self.mButton.WidgetStyle.Normal.Mirroring
        ButtonStyle.Normal = SlateBrush
        ButtonStyle.Hovered = self.mButton.WidgetStyle.Hovered
        ButtonStyle.Pressed = self.mButton.WidgetStyle.Pressed
        ButtonStyle.Disabled = self.mButton.WidgetStyle.Disabled
        ButtonStyle.NormalPadding = self.mButton.WidgetStyle.NormalPadding
        ButtonStyle.PressedPadding = self.mButton.WidgetStyle.PressedPadding
        ButtonStyle.PressedSlateSound = self.mButton.WidgetStyle.PressedSlateSound
        ButtonStyle.HoveredSlateSound = self.mButton.WidgetStyle.HoveredSlateSound
        
        ButtonStyle = None
        self.mButton.SetStyle(Ref[ButtonStyle])
    

    def ClearListSelection(self):
        ExecutionFlow.Push("L501")
        Variable: int32 = 0
        # Label 28
        ReturnValue: int32 = self.mParentWidget.GetChildrenCount()
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L427")
        ReturnValue_1: Ptr[Widget] = self.mParentWidget.GetChildAt(Variable)
        Button: Ptr[Widget_Multiplayer_ListButton] = Cast[Widget_Multiplayer_ListButton](ReturnValue_1)
        bSuccess: bool = Button
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: bool = NotEqual_ObjectObject(Button, self)
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        Button.mIsSelected = False
        Button.UpdateButton()
        Button.ActionButtonContainer.SetVisibility(2)
        goto(ExecutionFlow.Pop())
        # Label 427
        ReturnValue_3: int32 = Variable + 1
        # Label 469
        Variable = ReturnValue_3
        goto('L28')
    

    def UpdateButton(self):
        ExecutionFlow.Push("L4338")
        self.ActionButtonText.SetText(self.mActionButtonText)
        ReturnValue1: bool = Not_PreBool(self.mHideSessionInfo)
        ReturnValue: bool = ReturnValue1 and self.mIsPlayingSatisfactory
        if not ReturnValue:
            goto('L3189')
        self.SessionInfo.SetVisibility(3)
        # Label 169
        self.mTitleObject.SetTitle(self.mTitle)
        self.mAdditionalInfoObject.SetText(self.mAdditionalInfo)
        if not self.mIsOnline:
            goto('L3232')
        if not self.mIsPlayingSatisfactory:
            goto('L3582')
        if not self.mInAGame:
            goto('L3582')
        
        TextWhite2 = None
        GraphicsWhite2 = None
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite2], Ref[GraphicsWhite2])
        SlateBrush1.ImageSize = Vector2D(X = 64, Y = 64)
        SlateBrush1.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush1.TintColor = TextWhite2
        SlateBrush1.ResourceObject = Menu_PlayerIcon_Satisfactory
        SlateBrush1.DrawAs = 3
        SlateBrush1.Tiling = 0
        SlateBrush1.Mirroring = 0
        LocalIconBrush = SlateBrush1
        
        # Label 646
        self.mIcon.SetBrush(Ref[LocalIconBrush])
        Variable: int32 = 0
        # Label 714
        ReturnValue1_0: int32 = self.PlayersInSessionContainer.GetChildrenCount()
        ReturnValue_0: bool = Variable <= ReturnValue1_0
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L3932")
        LocalPlayerInt = Variable
        ReturnValue_1: Ptr[Widget] = self.PlayersInSessionContainer.GetChildAt(LocalPlayerInt)
        AsImage: Ptr[Image] = Cast[Image](ReturnValue_1)
        bSuccess: bool = AsImage
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: int32 = self.PlayersInSessionContainer.GetChildrenCount()
        ReturnValue_3: int32 = ReturnValue_2 - self.mPlayersInSession
        ReturnValue_4: bool = LocalPlayerInt <= ReturnValue_3
        if not ReturnValue_4:
            goto('L4006')
        
        Text1 = None
        Graphics1 = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text1], Ref[Graphics1])
        AsImage.SetBrushTintColor(Text1)
        # Label 1214
        ReturnValue_5: Timespan = MakeTimespan(0, 0, 0, self.mTimePlayed, 0)
        
        Days = None
        Hours = None
        Minutes = None
        Seconds = None
        Milliseconds = None
        BreakTimespan(ReturnValue_5, Ref[Days], Ref[Hours], Ref[Minutes], Ref[Seconds], Ref[Milliseconds])
        FormatArgumentData.ArgumentName = "Minutes"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = Minutes
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue_6: int32 = Days * 24
        ReturnValue1_1: int32 = ReturnValue_6 + Hours
        FormatArgumentData1.ArgumentName = "Hours"
        FormatArgumentData1.ArgumentValueType = 0
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = ReturnValue1_1
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_7: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1883, 'Value': '{Hours}h {Minutes}m'}", Array)
        self.TimePlayed.SetText(ReturnValue_7)
        ReturnValue2: bool = Not_PreBool(self.mPrivateSession)
        if not ReturnValue2:
            goto('L4107')
        self.playersInSession.SetVisibility(0)
        self.LockIcon.SetVisibility(1)
        # Label 2114
        if not self.mIsSelected:
            goto('L4188')
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        self.SetButtonColor(Graphics)
        
        TextWhite3 = None
        GraphicsWhite3 = None
        # Label 2206
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite3], Ref[GraphicsWhite3])
        self.TimePlayed.SetColorAndOpacity(TextWhite3)
        self.mAdditionalInfoObject.SetColorAndOpacity(TextWhite3)
        Variable1: uint8 = 1
        Variable2: uint8 = 0
        Variable_0: bool = self.mHideActionButton
        
        switch = {
            False: Variable2,
            True: Variable1
        }
        self.ActionButtonContainer.SetVisibility(switch.get(Variable_0, None))
        Variable_1: uint8 = 0
        Variable3: uint8 = 1
        Variable1_0: bool = self.mHideSecondaryActionButton
        
        switch_0 = {
            False: Variable_1,
            True: Variable3
        }
        self.ActionButtonContainer2.SetVisibility(switch_0.get(Variable1_0, None))
        ReturnValue_8: bool = Not_PreBool(self.mDisableActionButton)
        self.ActionButton.SetIsEnabled(ReturnValue_8)
        self.ActionButtonContainer.SetIsEnabled(ReturnValue_8)
        
        self.ActionButton.SetToolTipText(Ref[self.mActionButtonTooltip])
        Variable4: uint8 = 0
        Variable5: uint8 = 3
        Variable2_0: bool = self.IsNonInteractable
        
        switch_1 = {
            False: Variable4,
            True: Variable5
        }
        self.SetVisibility(switch_1.get(Variable2_0, None))
        Variable_2: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        Variable1_1: LinearColor = LinearColor(R = 0.09530699998140335, G = 0.09530699998140335, B = 0.09530699998140335, A = 1)
        Variable3_0: bool = self.IsNonInteractable
        
        switch_2 = {
            False: Variable_2,
            True: Variable1_1
        }
        self.mTintBorder.SetContentColorAndOpacity(switch_2.get(Variable3_0, None))
        if not self.mShowWarning:
            goto('L4241')
        
        self.Widget_NatInformation.SetToolTipText(Ref[self.mActionButtonTooltip])
        goto(ExecutionFlow.Pop())
        # Label 3189
        self.SessionInfo.SetVisibility(1)
        goto('L169')
        
        Text = None
        Graphics = None
        # Label 3232
        Default__HUDHelpers.GetFactoryGameLightGray(self, Ref[Text], Ref[Graphics])
        SlateBrush2.ImageSize = Vector2D(X = 64, Y = 64)
        SlateBrush2.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush2.TintColor = Text
        SlateBrush2.ResourceObject = Menu_PlayerIcon_Offline
        SlateBrush2.DrawAs = 3
        SlateBrush2.Tiling = 0
        SlateBrush2.Mirroring = 0
        LocalIconBrush = SlateBrush2
        goto('L646')
        
        TextWhite1 = None
        GraphicsWhite1 = None
        # Label 3582
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite1], Ref[GraphicsWhite1])
        SlateBrush.ImageSize = Vector2D(X = 64, Y = 64)
        SlateBrush.Margin = Margin(Left = 0, Top = 0, Right = 0, Bottom = 0)
        SlateBrush.TintColor = TextWhite1
        SlateBrush.ResourceObject = Menu_PlayerIcon
        SlateBrush.DrawAs = 3
        SlateBrush.Tiling = 0
        SlateBrush.Mirroring = 0
        LocalIconBrush = SlateBrush
        goto('L646')
        # Label 3932
        ReturnValue_9: int32 = Variable + 1
        Variable = ReturnValue_9
        goto('L714')
        
        TextWhite = None
        GraphicsWhite = None
        # Label 4006
        Default__HUDHelpers.GetFactoryGameWhite(self, Ref[TextWhite], Ref[GraphicsWhite])
        AsImage.SetBrushTintColor(TextWhite)
        goto('L1214')
        # Label 4107
        self.playersInSession.SetVisibility(1)
        self.LockIcon.SetVisibility(0)
        goto('L2114')
        # Label 4188
        self.SetButtonColor(LinearColor(R = 0, G = 0, B = 0, A = 0))
        goto('L2206')
        # Label 4241
        if not self.mCareAboutNAT:
            goto('L4299')
        if not self.mIsHost:
            goto('L4284')
        self.UpdateNATWarningForHost()
        goto(ExecutionFlow.Pop())
        # Label 4284
        self.UpdateNATWarningForClient()
        goto(ExecutionFlow.Pop())
        # Label 4299
        self.Widget_NatInformation.SetVisibility(1)
        goto(ExecutionFlow.Pop())
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_Multiplayer_ListButton.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Multiplayer_ListButton(10)
    

    def BndEvt__ActionButton_K2Node_ComponentBoundEvent_1_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Multiplayer_ListButton(252)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_2_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Multiplayer_ListButton(296)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Multiplayer_ListButton(378)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_5_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Multiplayer_ListButton(464)
    

    def ExecuteUbergraph_Widget_Multiplayer_ListButton(self):
        self.UpdateButton()
        # End
        # Label 29
        self.mActionButtons.SetVisibility(1)
        # End
        # Label 72
        self.ClearListSelection()
        self.mIsSelected = True
        self.UpdateButton()
        ReturnValue: bool = Default__FGSessionLibrary.IsSessionValid(self.mSession)
        if not ReturnValue:
            goto('L228')
        self.OnSessionSelected.ProcessMulticastDelegate(self.mSession)
        # Label 204
        self.OnButtonClicked.ProcessMulticastDelegate()
        # End
        # Label 228
        self.OnSessionDeselected.ProcessMulticastDelegate()
        goto('L204')
        if not self.mDisableActionButton:
            goto('L271')
        # End
        # Label 271
        self.OnActionButtonClicked.ProcessMulticastDelegate(self)
        # End
        if not self.mIsSelectable:
            goto('L354')
        if not self.mIsSelected:
            goto('L72')
        self.mIsSelected = False
        self.UpdateButton()
        goto('L228')
        # Label 354
        self.OnButtonClicked.ProcessMulticastDelegate()
        # End
        ReturnValue_0: bool = Not_PreBool(self.mHideActionButton)
        if not ReturnValue_0:
            goto('L469')
        self.mActionButtons.SetVisibility(0)
        # End
        goto('L29')
    

    def OnSessionDeselected__DelegateSignature(self):
        pass
    

    def OnButtonClicked__DelegateSignature(self):
        pass
    

    def OnSessionSelected__DelegateSignature(self, session: BlueprintSessionResult):
        pass
    

    def OnActionButtonClicked__DelegateSignature(self, ClickedButton: Ptr[Widget_Multiplayer_ListButton]):
        pass
    
