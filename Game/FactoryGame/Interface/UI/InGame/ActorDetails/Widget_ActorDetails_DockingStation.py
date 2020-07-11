
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildableDockingStation
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Parent import Destruct
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Parent import Construct
from Script.FactoryGame import GetInventory
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_DockingStation import ExecuteUbergraph_Widget_ActorDetails_DockingStation
from Script.FactoryGame import GetFuelInventory
from Game.FactoryGame.Interface.UI.InGame.ActorDetails.Widget_ActorDetails_Parent import Widget_ActorDetails_Parent
from Script.FactoryGame import FGInventoryComponent

class Widget_ActorDetails_DockingStation(Widget_ActorDetails_Parent):
    mDockingStation: Ptr[FGBuildableDockingStation]
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_ActorDetails_DockingStation(10)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_ActorDetails_DockingStation(686)
    

    def ExecuteUbergraph_Widget_ActorDetails_DockingStation(self):
        self.Construct()
        self.Widget_ActorDetails_Container.SetShowPointer(self.ShowPointer)
        Station: Ptr[FGBuildableDockingStation] = Cast[FGBuildableDockingStation](self.mActor)
        bSuccess: bool = Station
        if not bSuccess:
            goto('L696')
        self.mDockingStation = Station
        self.Widget_ActorDetails_Container.SetTitle(self.mDockingStation.mDisplayName)
        ReturnValue: Ptr[FGInventoryComponent] = self.mDockingStation.GetInventory()
        self.mStorage.Init(ReturnValue)
        ReturnValue_0: Ptr[FGInventoryComponent] = self.mDockingStation.GetFuelInventory()
        self.mFuelSlot.mCachedInventoryComponent = ReturnValue_0
        ReturnValue_1: bool = self.mDockingStation.GetIsInLoadMode()
        Variable: bool = ReturnValue_1
        Variable_0: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 485, 'Value': 'Receive'}"
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 550, 'Value': 'Send'}"
        
        switch = {
            False: Variable1,
            True: Variable_0
        }
        self.mDeliverySetting.SetText(switch.get(Variable, None))
        # End
        self.Destruct()
    
