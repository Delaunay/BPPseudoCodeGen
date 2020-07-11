
from codegen.ue4_stub import *

from Script.CoreUObject import Interface

class BPI_UnlockableInterface(Interface):
    
    
    def GetUnlockDataStruct(self):
        pass
    

    def GetUnlockRewardWidgets(self, OwningPlayer: Ptr[PlayerController], SchematicClass: TSubclassOf[FGSchematic], TradingPostWidget: Ptr[UserWidget]):
        pass
    

    def GetStingerWidgetRewardData(self):
        pass
    
