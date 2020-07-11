
from codegen.ue4_stub import *

from Script.FactoryGame import GetMaxNumberOfPlayers
from Script.FactoryGame import IsValid_Friend
from Script.OnlineSubsystemUtils import BlueprintSessionResult
from Script.FactoryGame import NetIdHasValidPresence
from Script.FactoryGame import GetPresenceString
from Script.FactoryGame import IsPlayingThisGame
from Script.Engine import GreaterEqual_IntInt
from Script.FactoryGame import FGPlayerState
from Script.Engine import UniqueNetIdRepl
from Script.FactoryGame import IsValid_UniqueNetId
from Script.FactoryGame import OnlinePresence
from Script.Engine import Not_PreBool
from Script.FactoryGame import Default__FGInviteLibrary
from Script.FactoryGame import IsOnline
from Script.Engine import GameStateBase
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import ESessionVisibility
from Game.FactoryGame.-Shared.Blueprint.FCompactPresence import FCompactPresence
from Script.FactoryGame import IsValid_OnlinePresence
from Script.FactoryGame import GetSessionFromPresence
from Script.FactoryGame import CheckIsCompatibleVersion
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import GetPresenceFromNetId
from Script.FactoryGame import Default__FGNetworkLibrary
from Script.FactoryGame import GetInviteSenderUniqueNetId
from Script.Engine import EqualEqual_ObjectObject
from Script.FactoryGame import IsPlayingOtherGame
from Script.FactoryGame import Default__FGPresenceLibrary
from Script.FactoryGame import EqualEqual_NetIdNetId
from Script.Engine import Map_Find
from Script.FactoryGame import GetFriendUniqueNetId
from Script.FactoryGame import IsSessionValid
from Script.FactoryGame import Default__FGSessionLibrary
from Script.FactoryGame import GetUniqeNetId
from Script.Engine import GetGameState
from Script.FactoryGame import Default__FGFriendsLibrary
from Script.Engine import Default__BlueprintMapLibrary
from Script.FactoryGame import FGOnlineSessionSettings
from Script.Engine import BlueprintFunctionLibrary
from Script.FactoryGame import GetSessionSettings

class BP_OnlineHelpers(BlueprintFunctionLibrary):
    
    
    def InsertionAddButton(self, NewParam: Ptr[PanelWidget], __WorldContext: Ptr[Object]):
        pass
    

    def GetSessionFromFriendNetId(self, WorldContext: Ptr[Object], friendNetId: UniqueNetIdRepl, __WorldContext: Ptr[Object]):
        
        ReturnValue: OnlinePresence = Default__FGPresenceLibrary.GetPresenceFromNetId(WorldContext, Ref[friendNetId])
        
        ReturnValue_0: BlueprintSessionResult = Default__FGPresenceLibrary.GetSessionFromPresence(Ref[ReturnValue])
        session = ReturnValue_0
    

    def IsHost(self, PlayerState: Ptr[PlayerState], OwningPlayer: Ptr[PlayerController], __WorldContext: Ptr[Object]):
        ReturnValue: bool = EqualEqual_ObjectObject(PlayerState, OwningPlayer.PlayerState)
        isOurself = ReturnValue
    

    def CanJoinInvite(self, WorldContext: Ptr[Object], invite: PendingInvite, __WorldContext: Ptr[Object]):
        
        presence = None
        self.GetInvitePresence(WorldContext, invite, WorldContext, Ref[presence])
        
        presence = None
        ReturnValue: bool = Default__FGPresenceLibrary.IsOnline(Ref[presence])
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        if not ReturnValue_0:
            goto('L169')
        Result = 2
        # End
        
        presence = None
        # Label 169
        self.GetInvitePresence(WorldContext, invite, WorldContext, Ref[presence])
        
        presence = None
        ReturnValue_1: BlueprintSessionResult = Default__FGPresenceLibrary.GetSessionFromPresence(Ref[presence])
        ReturnValue_2: bool = Default__FGSessionLibrary.IsSessionValid(ReturnValue_1)
        ReturnValue1: bool = Not_PreBool(ReturnValue_2)
        if not ReturnValue1:
            goto('L397')
        Result = 1
        # End
        
        presence = None
        # Label 397
        self.GetInvitePresence(WorldContext, invite, WorldContext, Ref[presence])
        
        presence = None
        ReturnValue_1 = Default__FGPresenceLibrary.GetSessionFromPresence(Ref[presence])
        
        ReturnValue_3: int32 = Default__FGSessionLibrary.GetMaxNumberOfPlayers(Ref[ReturnValue_1])
        
        ReturnValue1_0: FGOnlineSessionSettings = Default__FGSessionLibrary.GetSessionSettings(Ref[ReturnValue_1])
        ReturnValue_4: bool = GreaterEqual_IntInt(ReturnValue1_0.NumConnectedPlayers, ReturnValue_3)
        if not ReturnValue_4:
            goto('L710')
        # Label 685
        Result = 0
        # End
        
        presence = None
        # Label 710
        self.GetInvitePresence(WorldContext, invite, WorldContext, Ref[presence])
        
        presence = None
        ReturnValue_1 = Default__FGPresenceLibrary.GetSessionFromPresence(Ref[presence])
        
        ReturnValue_5: FGOnlineSessionSettings = Default__FGSessionLibrary.GetSessionSettings(Ref[ReturnValue_1])
        
        ReturnValue_6: bool = Default__FGSessionLibrary.CheckIsCompatibleVersion(Ref[ReturnValue_5])
        ReturnValue2: bool = Not_PreBool(ReturnValue_6)
        if not ReturnValue2:
            goto('L997')
        Result = 3
        # End
        # Label 997
        Result = 4
    

    def IsInThisGame(self, onlineFriend: Ref[FGOnlineFriend], WorldContext: Ptr[Object], __WorldContext: Ptr[Object]):
        ExecutionFlow.Push("L759")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(WorldContext)
        
        ReturnValue.PlayerArray = None
        ReturnValue_0: int32 = len(ReturnValue.PlayerArray)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L669')
        Variable_0 = Variable
        ExecutionFlow.Push("L685")
        ReturnValue = Default__GameplayStatics.GetGameState(WorldContext)
        
        ReturnValue.PlayerArray = None
        Item = None
        Item = ReturnValue.PlayerArray[Variable_0]
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](Item)
        bSuccess: bool = State
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        
        ReturnValue_2: UniqueNetIdRepl = Default__FGFriendsLibrary.GetFriendUniqueNetId(Ref[onlineFriend])
        ReturnValue_3: UniqueNetIdRepl = State.GetUniqeNetId()
        
        ReturnValue_4: bool = Default__FGNetworkLibrary.EqualEqual_NetIdNetId(Ref[ReturnValue_3], Ref[ReturnValue_2])
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        inThisGame = True
        # End
        # Label 669
        inThisGame = False
        # End
        # Label 685
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L51')
    

    def CanSendInvite(self, WorldContext: Ptr[Object], friend: FGOnlineFriend, __WorldContext: Ptr[Object]):
        
        ReturnValue: OnlinePresence = self.GetFriendPresence(WorldContext, WorldContext, Ref[friend])
        
        ReturnValue_0: bool = Default__FGPresenceLibrary.IsPlayingThisGame(Ref[ReturnValue])
        if not ReturnValue_0:
            goto('L213')
        
        inThisGame = None
        self.IsInThisGame(WorldContext, WorldContext, Ref[friend], Ref[inThisGame])
        if not inThisGame:
            goto('L238')
        canSend = 1
        # End
        # Label 213
        canSend = 0
        # End
        # Label 238
        canSend = 3
    

    def IsFriendInOnlineSession(self, WorldContext: Ptr[Object], frriend: Ref[FGOnlineFriend], __WorldContext: Ptr[Object]):
        
        ReturnValue: bool = Default__FGFriendsLibrary.IsValid_Friend(Ref[frriend])
        # Label 51
        if not ReturnValue:
            goto('L190')
        
        session = None
        self.GetFriendSession(frriend, WorldContext, WorldContext, Ref[session])
        ReturnValue_0: bool = Default__FGSessionLibrary.IsSessionValid(session)
        inSession = ReturnValue_0
        # End
        # Label 190
        inSession = False
    

    def GetCompactPresence(self, presence: OnlinePresence, __WorldContext: Ptr[Object]):
        
        ReturnValue: bool = Default__FGPresenceLibrary.IsValid_OnlinePresence(Ref[presence])
        # Label 51
        if not ReturnValue:
            goto('L429')
        
        ReturnValue_0: bool = Default__FGPresenceLibrary.IsPlayingOtherGame(Ref[presence])
        
        ReturnValue_1: bool = Default__FGPresenceLibrary.IsPlayingThisGame(Ref[presence])
        
        ReturnValue_2: bool = Default__FGPresenceLibrary.IsOnline(Ref[presence])
        
        ReturnValue_3: FString = Default__FGPresenceLibrary.GetPresenceString(Ref[presence])
        FCompactPresence.PresenceString_8_73B095B54A983F2391EE189D60CC1495 = ReturnValue_3
        FCompactPresence.IsOnline_3_0B4A819747012DC786FA4097038402CD = ReturnValue_2
        FCompactPresence.IsPlayingThisGame_6_D07FB68E4051EB599EEFC5B695C2B0FA = ReturnValue_1
        FCompactPresence.IsPlayingOtherGame_7_ED9DBFB84A164DABCD8A488B070BE8C3 = ReturnValue_0
        # Label 397
        compactPresence = FCompactPresence
        # End
        # Label 429
        compactPresence = FCompactPresence(PresenceString_8_73B095B54A983F2391EE189D60CC1495 = "", IsOnline_3_0B4A819747012DC786FA4097038402CD = False, IsPlayingThisGame_6_D07FB68E4051EB599EEFC5B695C2B0FA = False, IsPlayingOtherGame_7_ED9DBFB84A164DABCD8A488B070BE8C3 = False)
    

    def GetFriendSession(self, friend: FGOnlineFriend, WorldContext: Ptr[Object], __WorldContext: Ptr[Object]):
        
        ReturnValue: OnlinePresence = self.GetFriendPresence(WorldContext, WorldContext, Ref[friend])
        
        ReturnValue_0: bool = Default__FGPresenceLibrary.IsValid_OnlinePresence(Ref[ReturnValue])
        if not ReturnValue_0:
            goto('L274')
        
        ReturnValue = self.GetFriendPresence(WorldContext, WorldContext, Ref[friend])
        
        ReturnValue_1: BlueprintSessionResult = Default__FGPresenceLibrary.GetSessionFromPresence(Ref[ReturnValue])
        session = ReturnValue_1
        # End
        # Label 274
        session = BlueprintSessionResult()
    

    def GetInvitePresence(self, WorldContext: Ptr[Object], invite: PendingInvite, __WorldContext: Ptr[Object]):
        
        ReturnValue: UniqueNetIdRepl = Default__FGInviteLibrary.GetInviteSenderUniqueNetId(Ref[invite])
        
        ReturnValue_0: OnlinePresence = Default__FGPresenceLibrary.GetPresenceFromNetId(WorldContext, Ref[ReturnValue])
        presence = ReturnValue_0
    

    def GetFriendPresence(self, onlineFriend: Const[Ref[FGOnlineFriend]], WorldContext: Ptr[Object], __WorldContext: Ptr[Object]):
        
        ReturnValue: UniqueNetIdRepl = Default__FGFriendsLibrary.GetFriendUniqueNetId(Ref[onlineFriend])
        
        ReturnValue_0: bool = Default__FGNetworkLibrary.IsValid_UniqueNetId(Ref[ReturnValue])
        if not ReturnValue_0:
            goto('L416')
        
        ReturnValue = Default__FGFriendsLibrary.GetFriendUniqueNetId(Ref[onlineFriend])
        
        ReturnValue_1: bool = Default__FGPresenceLibrary.NetIdHasValidPresence(WorldContext, Ref[ReturnValue])
        if not ReturnValue_1:
            goto('L416')
        
        ReturnValue = Default__FGFriendsLibrary.GetFriendUniqueNetId(Ref[onlineFriend])
        
        ReturnValue_2: OnlinePresence = Default__FGPresenceLibrary.GetPresenceFromNetId(WorldContext, Ref[ReturnValue])
        ReturnValue_3: OnlinePresence = ReturnValue_2
        goto('L448')
        # Label 416
        ReturnValue_3 = OnlinePresence()
    

    def SessionVisibilityStringToEnum(self, string: FString, __WorldContext: Ptr[Object]):
        MakeVariableOutput: Dict[FString, uint8] = {0: "Private", 1: "Friends Only"}
        sessionVisibilityLookup = MakeVariableOutput
        
        Value = None
        ReturnValue: bool = Default__BlueprintMapLibrary.Map_Find(Ref[sessionVisibilityLookup], Ref[string], Ref[Value])
        Enum = Value
    
