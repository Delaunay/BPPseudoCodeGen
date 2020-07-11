
from codegen.ue4_stub import *

from Script.FactoryGame import FGChatManager

class BP_ChatManager(FGChatManager):
    mMaxNumMessagesInHistory = 50
    mMessageVisibleDuration = 10
    bAlwaysRelevant = True
    bReplicates = True
    RemoteRole = 1
    
