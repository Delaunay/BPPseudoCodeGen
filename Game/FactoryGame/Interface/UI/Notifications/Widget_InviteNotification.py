
from codegen.ue4_stub import *

from Script.Engine import Conv_StringToText
from Script.FactoryGame import Default__FGInviteLibrary
from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import Default__FGNetworkLibrary
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.Notifications.Widget_InviteNotification import ExecuteUbergraph_Widget_InviteNotification.K2Node_CustomEvent_receivedInvite
from Game.FactoryGame.Interface.UI.Notifications.Widget_InviteNotification import ExecuteUbergraph_Widget_InviteNotification
from Script.FactoryGame import GetInviteSenderUniqueNetId
from Script.FactoryGame import FGLocalPlayer
from Script.Engine import UniqueNetIdRepl
from Script.UMG import WidgetAnimation
from Script.FactoryGame import GetNameFromUniqueNetId
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import LocalPlayer

class Widget_InviteNotification(UserWidget):
    SpawnAnim: Ptr[WidgetAnimation]
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_InviteNotification(182)
    

    def OnInviteReceived(self, receivedInvite: Const[Ref[PendingInvite]]):
        ExecuteUbergraph_Widget_InviteNotification.K2Node_CustomEvent_receivedInvite = receivedInvite #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_InviteNotification(354)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_InviteNotification(661)
    

    def ExecuteUbergraph_Widget_InviteNotification(self):
        # Label 10
        ReturnValue: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L666')
        OutputDelegate.BindUFunction(self, OnInviteReceived)
        Player.mOnInviteReceived.Remove(OutputDelegate)
        # End
        ReturnValue1: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player1: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue1)
        bSuccess1: bool = Player1
        if not bSuccess1:
            goto('L666')
        OutputDelegate.BindUFunction(self, OnInviteReceived)
        Player1.mOnInviteReceived.AddUnique(OutputDelegate)
        # End
        ReturnValue2: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        
        receivedInvite = None
        ReturnValue_0: UniqueNetIdRepl = Default__FGInviteLibrary.GetInviteSenderUniqueNetId(Ref[receivedInvite])
        
        name = None
        ReturnValue_1: bool = Default__FGNetworkLibrary.GetNameFromUniqueNetId(ReturnValue2, Ref[ReturnValue_0], Ref[name])
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_StringToText(name)
        self.mPlayerName.SetText(ReturnValue_2)
        ReturnValue_3: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SpawnAnim, 0, 1, 2, 1)
        # End
        goto('L10')
    
